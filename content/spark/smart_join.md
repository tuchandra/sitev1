# Smart Join Algorithms for Fighting Skew at Scale

Andrew Clegg (Applied ML Group @ Yelp) - 4/24
___

Slides available [here](https://drive.google.com/file/d/1D5vWUAjZBKHmF1uFT--a_U1n8nW3z9Ac/view).

## Data skew

Everyone knows the classical statistical definitions of skew, where the mean and median are very different, whatever; but we are generally interested in the more practical definitions. One example is when you have a few outliers … or maybe you have a multimodal distribution (e.g., two different sub communities, two different processes). 

But one area is particularly important: **power law distributions** ([Wikipedia](<https://en.wikipedia.org/wiki/Power_law>)), which show up all the time when you're working with data from the web. You have a very *very* long tail, and a true power-law will show up linearly if you plot it on a log-log scale. Examples in nature include:

* electrostatic and graviational forces (inverse squares)
* distribution of earthquake magnitudes
* 80/20 rule in the distribution of income / Pareto principle
* Relationship between body size and metabolism

And then they show up in datasets that we have to deal with:

* word frequencies in natural language coprora (Zipf's law)
* degree distribution in social networks (referred to in the past as the "Bieber problem" on Twitter, lol) - this was a problem because if you're sharding by user ID, then as soon as Justin Bieber does something it becomes a problem for whatever machines are processing that action … 
* participation inequality on wikis and forum sites (1% rule)
* popularity of websites and content

But **why is this a problem?** Computer science has come up with solutions to common cases of this:

* **hot shards** in databases: salt your keys, change the schema
* **slow load times** for certain users: look for O(n^2) mistakes, e.g., certain users would use their shopping baskets as bookmarks and that caused some quadratic algorithm in the background to crash in the extreme case.
* **hot mappers** in map-only tasks: repartition randomly
* **hot reducers** during joins and aggregations: … what do …? This talk will focus on joins (aggregations could be another talk).

### Diagnosing hot executors

Usually, you can figure this out by looking at the *max* runtime of things. The example he gave was where quartiles are 0ms / 3s / 5s / 10s / 55m, which is insane. Scheduler delay was 8ms / 14ms / 19ms / 42ms / 1.1h. We're interesting in figuring out what's happening on the tails.

This turns into a cost problem; while all the executors except one are waiting for something to finish, you could be using those nodes for other problems or tasks.

## Joins in Spark

Standard joins in Spark are called "shuffle hash joins." Suppose you have two datasets and you want to join on some key; in order to do this, Spark shuffles the rows by key and partitions based on them. This is because each executor has to have the right rows to be able to join them together. The important point is that you can't have one key split over several executors; they all have to be colocated.

That's usually fine, but when you have very skewed data things become uh oh. You'll end up with one executor that has a ton of rows and others that are just waiting on it.

One way around this is a **broadcast join**, which avoids doing a shuffle altogether. It loads one (small) dataset into memory and broadcasts it to all the executors, so the join can just happen in memory; this becomes a *map-only task*. The problem here is that one of the datasets has to fit in memory, and it can also have reliability issues (sometimes Spark is overoptimistic about what it can broadcast, he turned autobroadcast off).

## Faster joins

We really want to split a single key across multiple tasks, so what we can do is pick a *replication factor R*. In the **skewed data**, randomly append a number between 0 and R to the existing key, so basically you make a composite key. In the **nonskewed data**, replicate the rows R times and append the replica ID to the original key. Then join on the composite key.

Your skewed dataframe now has the big key split up over partitions, and you have the second dataset copied around that can be joined to everything. This is no longer memory bound, so you're not limited by having to have the dataset in memory. 

```python
replication_ids = f.broadcast(
    spark.range(replication_factor).withColumnRenamed("id", "replica_id")
)

# Randomly assign rows in skewed data to buckets
skewed_data_tagged = skewed_data.withColumn(
    "composite_key", f.concat("original_id", f.lit("@"), randint(replication_factor))
)

# Replicate uniform data, one copy of each row per bucket
uniform_data_replicated = (  
    uniform_data  
    .crossJoin(replication_ids)  
    .withColumn(  
        "composite_key",  f.concat("original_id", f.lit("@"), "replica_id")  
    )  
) 

# Now you can join on the composite key
joined = skewed_data_tagged.join(  
    uniform_data_replicated,  
    on="composite_key",  
    how="inner"
) 
```

This only works for inner and left outer joins … so be careful.

**Benchmark:** Generated 100M rows with uniformly-distributed keys, and 100B rows of data with Zipf-distributed keys. A standard inner join ran for **7+ hours** before he killed it (on a super beefy cluster), and a 10x replicated join completed in **1h16m**. 

### Can we do better?

**Differential replication** (which is a term he pulled out of his ass) - well, only the keys that are really common need to be replicated many times. The rare keys don't need to be replicated as much (or at all). Identify the frequent keys before replication, then use a different replication policy for those.

You basically take advantage of Spark's freqItems method that lets you find the most frequent items via an approximation algorithm, which is super powerful.

```python
replication_factor_high = 50  
replication_high = f.broadcast(  
    spark.range(replication_factor_high).withColumnRenamed('id', 'replica_id')  
)  
replication_factor_low = 10  
replication_low = f.broadcast(  
    spark.range(replication_factor_low).withColumnRenamed('id', 'replica_id')  
)  

# Determine which keys are highly over-represented, broadcast everywhere
top_keys = f.broadcast(  
    skewed_data  
    .freqItems(["original_id"], 0.0001)  # return keys with frequency > this
    .select(f.explode("id_freqItems").alias("id_freqItems"))  
)  

uniform_data_top_keys = (
    uniform_data
    .join(
        top_keys,
        uniform_data.original_id == top_keys.id_freqItems,
        how="inner",
    )
    .crossJoin(replication_high)
    .withColumn("composite_key", f.concat("original_id", f.lit("@"), "replica_id"))
)

uniform_data_rest = (
    uniform_data
    .join(
        top_keys,
        uniform_data.original_id == top_keys.id_freqItems,
        how="leftanti",
    )
    .crossJoin(replication_low)
    .withColumn("composite_key", f.concat("original_id", f.lit("@"), "replica_id"))
)

# This is now the entire uniform dataset replicated differentially
uniform_data_replicated = uniform_data_top_keys.union(uniform_data_rest)

# Do the same tagging for skewed data
skewed_data_tagged = (
    skewed_data
    .join(
        top_keys,  # Remember this is broadcasted, no shuffling required
        skewed_data.id == top_keys.id_freqItems,
        how="left",
    )
    .withColumn("replica_id",
        f.when(
            f.isnull(f.col("id_freqItems")), randint(replication_factor_low),
        )
        .otherwise(randint(replication_factor_high))
    )
    .withColumn("composite_key", f.concat("original_id", f.lit("@"), "replica_id"))
)
```

This lets you replicate very frequent keys more often, and the nonskewed data is replicated if needed. This was a really cool example. 

**Benchmark**: Generated 100M rows with uniformly-distributed keys, and 100B rows of data with Zipf-distributed keys, just like before. A 10x replicated join completed in **1h16m**, and the 10x/50x differential replication completed in **under 1h**.

### Partial broadcasting

Identify the very common keys in the skewed data, then select these rows from the uniform data and broadcast join those. The rare keys are joined the traditional way (without replication), and then you can union the resulting joined DataFrames.

Intuitively, this seems like a better way of dealing with the case where they are a few specific outliers that you want to single out and treat differently. Probably not better when you have a sliding scale of popularity behavior, but useful sometimes.

### Dynamic replication

Get the approximate frequency of every key in the skewed data, and replicate the uniform data proportionally to the key frequency. The intuition is that you replicate by an amount somewhere on a sliding scale between the rarest and most common keys; but this can be hard to make work in practice.

### Double-sided skew

Uh oh, what happens if you have two skewed datasets? The intuition is that you have two replication factors, one for each dataset, and create composite keys based off id / left_replica / right_replica … that's an ouch.

## Checklist

Things to ask yourself before you do this:

* is the problem just **outliers**? can you safely ignore them?
* try the **broadcast join** if possible
* **look at your data** to get an idea of the distributions
* **start simple** with a fixed replication factor, then iterate if needed

But this can be a really useful thing to do when broadcasts are insufficient. Wow, awesome talk.