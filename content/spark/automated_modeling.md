# Automating Predictive Modeling at Zynga with Pandas UDFs

## Ben Weber (Principal Data Scientist @ Zynga) - 4/25

Zynga is a mobile gaming company that has a rich portfolio of games … they have a ton of analytics folks and run an annual internal analytics conference. It brings together all of their analytics folks for knowledge sharing internally.

* analytics engineering: handling ingestion and data platform, and also live production services
* embedded analysts: work on product / game teams, whose job is to improve games and understand how changes might impact games
* central analytics: focused on publishing functions, marketing, advertising, corporate development; build data products that any team could use and plug in and scale.

## Challenge

Their challenge is that they want to support game teams to act on their data, but they have a variety of types of games … card games have "hands played" but match three games have "matches made" but etc etc etc ...

In other words, they want to build game-specific models for behaviors such as likelihood to purchase, likelihood to churn, etc., but the games have diverse event taxonomies. They have tnes tens of millions of players and dozens of games for multiple platforms.

## AutoModel

Tool set: **Featuretools** for automating feature engineering, **Pandas UDFs** for distributing Featuretools, and **Databricks / Pyspark** for building the model pipeline.

So they created **AutoModel**, which is their first portfolio-scale product. It generates hundreds of propensity models and powers features in their games & live services. They can plug it in to any new game and have it work out of the game.

The data pipeline is:

* **data extract**, from S3 and parquet files
  * handled by their ingestion and platform team
  * they use Spark SQL to transform this 
* **feature engineering**, with featuretools
  * "here's a deep but narrow format … we want to create a shallow but wide format that we can use later"
  * use featuretools to do this programatically and at scale
* **feature application**, where you take the featuretools output
  * using Pandas UDFs on Spark
* model training using Spark ML
* model publish

### Automated Feature Engineering with FeatureTools

Goals include:

* translate narrow and deep data tables into a shallow and wide representation
* support dozens of titles with diverse event taxonomies
* scale to billions of records and millions of players
* minimize manual data science workflows

Instead of a data scientist saying "count the number of distinct days played," they use this to automate that and much more.

**[Feature Tools](https://github.com/Featuretools/featuretools)** is a library for deep feature synthesis. Represent your data as entity sets and identify feature descriptors for transforming data into new representations. They went into detail about the entity set; you have entities customers and transactions, which share a customer_id relationship … etc. 

Once you've done that, you can perform **deep feature synthesis**. It comes up with a ton of different features for you. He went on and demoed some code about how they did this.

"For anyone worried about GDPR, this isn't our dataset, it's a sample dataset … that's a note for our legal team." Love it.

### Scaling up via Pandas UDFs

FeatureTools only works on a Pandas dataframe, so uh oh. Their options were to either (1) parallelize the process, (2) translate feature descriptions to Spark SQL, or (3) find a way to distribute the task.

* Parallelizing the process was just way too daunting to be able to do
* Translating to Spark SQL worked but still didn't work very well, it was still slow
* So they had to learn about Pandas UDFs.

**Pandas UDFs** were introduced in Spark 2.3, and it lets you partition the Spark DF into Pandas DFs across your cluster, do a computation, then bring it back to Spark. Each worker takes a Pandas input, runs UDFs on it, and generates a Pandas output. PyArrow does the conversion between Spark and Pandas.

You can use Pandas UDFs when:

* you need to operate on Pandas data frames
* your data can be represented as a single Spark data frame
* and you can partition your dataset.

See this [Towards Data Science article](https://towardsdatascience.com/automated-feature-engineering-for-predictive-modeling-d8c9fa4e478b) for an example of distributing this.

But then they hit a lot of issues:

* debugging is a challenge; since you're executing on worker nodes, you have to go to the Spark logs to see what's going on when an exception occurs
* pushing the limits of PyArrow, they found some edge cases that were open Github issues
* Pandas UDFs are also newer and so you're going to hit some edge case bugs
* data type mismatches between Pandas and Spark caused bugs, too
* the schema needs to be known before the UDF is computed; for them, this means they have to do a sampling step where they figure out what the schema will be after deep feature synthesis happens … but you can't just distribute DFS and go.

### Modeling and Publishing

They use gradient boosted trees and XGBoost for classification. They tune hyperparameters with ParamGridBuilder and CrossValidator. Great, that's all standard.

They publish to Couchbase for game teams to use. Then they decided to productionalize with Databricks — a driver notebook can use the jobs API to have different models running for different games in different notebooks.

### Other uses of Pandas UDFs

They found out ways to distribute statsmodels, scipy, and numpy to help distribute experimentation. None of these were intended to be run on Spark, but Pandas UDFs enables this … as long as you can partition your data in some way.

**Old approach**: custom data science and engineering work for each model, months-long development process, and an ad-hoc process for productionalizing models.

**New approach**: minimal effort for building new propensity models, and no custom work for new games. Predictions are deployed to their application database. Gonna start using MLflow soon.

Pandas UDFs unlock a new magnitude of processing for Python libraries. Zynga can now use Pyspark to build portfolio-scale data products.

