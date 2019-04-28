# Understanding Query Plans and Spark UIs

Xiao Li (Databricks) - 4/25
___

One of the core committers to Spark, @gatorsmile on Twitter.

## Intro: how queries get executed

* you have SQL / datasets / dataframes
* that turn into an unresolved logical plan via a parser
* that turn into a logical plan via an analyzer (and metadata catalog)
* that turn into an optimized logical plan via an optimizer (and cache manager)
* that turns into man physical plans via a planner, which uses a cost model to select one
* which then finally gets executed into DAGs

In the Spark UI, you can read the parsed plan, analyzed plan, optimized plan, and physical plan. Great. How do you understand and tune them?

## Understanding and tuning plans

This section is a bunch of examples followed by pieces of advice.

### Read the analyzed plan to check implicit type casting

This followed an example where you got different results with a constraint `where x != 0` vs. `where x != 0.0`, due to implict type casting within the analyzed plan. His suggestion is to explicitly cast the types in your queries.

### Create native tables 

Not sure what this was about … create native data source tables for better performance and stability. Using something called ORC.

### Collapse projects

Look out for UDFs being called multiple times in the query plan.

```
df.select(
    some_udf("col1").alias("new_col1")
).selectExpr(
    "new_col1",
    "new_col1 + new_col1",
)

# --> causes udf to be executed three times. forgot what to do to fix this.
```

### Cross-session SQL cache

If a query is cached in one session, the new queries in all sessions might be impacted.

```
# ?
```

### Join hints in Spark 3.0

They'll help you with broadcasting and … other things that I didn't see in time.

## Tracking Execution in the Spark UI

A single SQL query can correspond to multiple Spark jobs: broadcast exchange, suffle exchange, subqueries, … and each Spark job is an RDD DAG.

In query execution (selected physical plan —> DAGs) you can see both the higher level SQL physical operators (Filter, Project, HashAggregate, Exchange, etc.) and lower level Spark RDD primitives.

The Stages tab has task-specific information, letting you know how time is spent, what tasks are blocking others, how well things are balanced, etc. … each task corresponds to a partition, so maybe you have to repartition things. You can use the Duration column to see if task execution times are balanced, Input Size / Records column to look for skew in your data (based on partitioning).

The Executors tab tells you about … the executors, crazy. You can see used/free memory of each executor, task time, and the size of data transferred between stages.

Then he showed off how when you change `using parquet` to `using delta` you reduce write time from 8M to 27S, hahaha.

Lots of resources on the last slide.

