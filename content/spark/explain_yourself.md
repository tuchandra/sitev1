# Explain Yourself: why you get the recommendations you do

## Niels Hanson (KPMG), Kishori Konwar (Broad Institute @ Harvard/MIT), Guohao Xiao (KPMG)

## Recommender engines

… are now essential tools for personalizing the web, but there's a huge problem with explainable recommendations. There is a growing need for transparency, but most models are viewed as black boxes. We should be striving for models that are both effective and understandable.

This talk is about explaining recommendations from the ALS Recommender model in Spark ML.

There are two ways to develop a recommender system: **collaborative filtering** which looks at user / item interactions ("you're starting to look like somebody who consumes these kinds of things …") and **content-based filtering** which recommends items that are similar to other items. Collaborative filtering has the cold-start problem (what do you recommend to a new person?) but content-based filtering makes it difficult to move beyond the starting point.

They are often combined to form **hybrid recommender systems.**

## Matrix-based collaborative filtering

This is the most widely used recommender model; try to predict missing values of the user-item matrix by decomposing the matrix into latent factors, whcih represent general trends of user-item consumption. This is also the model implemented in [Spark ML](https://spark.apache.org/docs/2.4.0/ml-collaborative-filtering.html).

The model has a number of tuneable factors: rank (number of factors to fit), lambda (regularization parameter), alpha (confidence on user data), model type (is user interaction actively given or inferred from observations).

An overlooked aspect is that implicit factors capture tons of information about how customers consume products:

* you can find users and items with similar consumption patterns easily; similar users will have similar user factors, similar items will have similar item factors
* Grouping users might inform advertising campaigns around interests
* Grouping items might inform cross-selling initiatives

## User-specific item spaces

They propose a **user-specific item space** where you create a linear mapping $$W^u$$ that linearly tarnsforms item similarities based on the user's interests $$C^u$$. Holy linear algebra! OK, time to stop trying to write down everything on the slide and actually understand.

For a runner, you might warp their itemspace so that there is more distance between the running shoes, and move the musical instruments closer together. Do the opposite weighting for a musician. But why?

The user-specific item-space allows you to decompose recommendations into their component parts; decomposing the recommended value into the sum of the distances (within the space) as weightings times the scores. Now you can say "you got this recommendation because you clicked on this, bought this, and added this to your cart."

This lets you decompose recommendations!

* relative numbers explain which items have a strong influence over specific recommendations
* absolute numbers let us look at items that drive popular recommendations in general
* and gives intuition about how CF works
* lets you add new prior information or perform man-in-the-middle corrections

They created a new class ALSExplain that lets you do this on the SparkML ALS implementation, and they've made a PR against Spark itself to add this in. They showed a demo of how this works on the MovieLens dataset, why someone would be recommended *Home Alone* or *Fight Club*.

## Future work

Currently ALSExplain only generates recommendations and decomposition scores without explicitly generating the full user-specific item-item matrix; it does it for the recommendations only. This might be interesting, but performance.

Performance improvements can come — approximations to the matrix inverse and sparse matrix algorithms.

Their proposed code design is their first attempt to change Spark ML, so they've gotta work with the community on that.

And the ALS paper is 10 years old, but this wasn't implemented in Spark! They want to explore generating explainable recommendations from more complex models (autoencoders, feed-forward neural nets, etc.). The paper they've been referencing just has this in the back!

