# How Graph Technology is Changing AI

Jake Graham and Alicia Frame (Neo4j) - 4/24
___

## Introduction

There's always the quote "it's not what you know … it's who you know," and that's a graph-centered view. Questions about connections and relationships are often very difficult to represent as rows and columns. You need a graph — what are some of the use cases?

* **fraud detection**, by understanding what community a particular acount is part of
* **drug discovery**, by looking into the relationships between drugs
* **recommendations**, thinking about the paths people take between products
* **customer segmentation**, by looking into clusters of customers, how people are connected to each other, how people are making decisions
* **cybersecurity**, looking into paths for intrusion networks
* **churn prediction** 
* **predictive maintenance**, looking at dependency chains
* **search**, and pagerank, obviously

You have **nodes** and **relationships** that connect them, but the nodes and relationships also have **properties**.

## Motivation

Graphs provide more accurate predictions with the data that you already have: SOTA data science models ignore network structure and complex relationships, and graph models add highly predictive features to existing ML models. They're here to talk about how you can start adding graph information to current models, without rebuilding everything from the ground up.

They showed an article "[Google ponders the shortcomings of machine learning](https://www.zdnet.com/article/google-ponders-the-shortcomings-of-machine-learning/)", which summarizes a [paper ("Relational inductive biases, deep learning, and graph networks")](https://arxiv.org/abs/1806.01261), and they talk about how graphs add a structure that traditional ML models do not have. 

## Graph Building

In Spark, you're *exploring graphs* by taking advantage of the massive scalability, powerful data pipelining, and robust ML libraries. But Spark is non-persistent and non-native, so it's best to understand where you have graphs and what your graph features are.

In Neo4j, you build persistent and dynamic graphs, and have graph-native querying and algorithms. They are always adding more graph algorithms, embeddings, and approaches. Note that the speakers are from Neo4j.

The steps of graph data science, in increasing order of complexity and abstraction:

* **Query-based knowledge graph**, building a knowledge graph to help individual users make decisions
* **Query-based feature engineering**, moving towards a model, but you still have domain experts
* **Graph algorithm feature engineering**, run unsupervised models to find graph features, then throw them into an ML model)
* **Graph embeddings**, where you create embeddings of a graph, very active area of research
* **Graph neural networks**, what the fuck? [Towards Data Science article](https://towardsdatascience.com/a-gentle-introduction-to-graph-neural-network-basics-deepwalk-and-graphsage-db5d540d50b3) and [Neural Graph Learning paper](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46568.pdf)

Note that the last few are active areas of research.

### Query-based knowledge graph

NASA is using Neo4j to put together a knowledge graph; someone from the Orion project found information from the Apollo project that let them present an issue, saving $1M and at least two years of work. They digitized thousands of documents that were functionally useless to individuals, but were able to be combined into a "lessons learned knowledge graph."

### Query-based feature engineering

Once you have a knowledge graph, that's great; but you still have to know what you're trying to get out. How do you make inferences from the knowledge graph?

One use case is [HetioNet](https://het.io/), which integrates 50 years of biomedical data. It is used to predict new uses for drugs: it uses graph algorithms to create features that predict where new links might be. For example, they see IRF1 and multiple sclerosis without an explicit edge between them … but they see that they're second degree connections via a lot of other genes. They create a score that captures how far you have to go to get from one node to another, and this score can be fed into an ML model.

### Graph algorithm feature engineering

Make use of your existing machine learning pipeline by taking your tabular data and adding graph-based features, then combining those into a stronger pipeline. Features include:

* **community detection**, detecting group clustering or partitioning
* **centrality / importance**, determining the importance of distinct nodes in the network
* **pathfinding & search**, finding optimal paths or evaluating route availability / quality
* **heuristic link prediction**, estimating likelihood of nodes forming a relationship
* **embeddings**, capturing connectivity or topology in vectors
* **similarity**, wondering how similar two nodes are given their connections

Case study: financial crime to detect fraud. Many financial institutions have existing pipelines to identify fraud, but adding graph based features improves accuracy. Adding **connected components** to identify disjoint subgraphs (seeing if there are fraud rings), **PageRank** to measure influence of individuals (could tell you about unusual transaction volumes, money laundering, etc.), **Louvain** to identify communities (looking at accounts that interact with each other really frequently in an unsupervised manner), and **Jaccard** to measure account similarity (who else behaves similarly to this account).

This is where Neo4j is now, with early adopters. The rest of this is *the future*.

### Graph embeddings 

**Embeddings** transform a graph into a vector or set of vectors that describe … something: topology, connectivity, or other attributes of nodes / edges.

* **vertex embeddings** describe connectivity of a node
* **path embeddings** describe traversals across the graph
* **graph embeddings** encode an entire graph into a single vector

[DeepWalk](http://www.perozzi.net/publications/14_kdd_deepwalk.pdf) takes random nodes, then takes random walks across the graph from those nodes, then trains a skip-gram model too generate embeddings.

Case study: [Explainable Reasoning over Knowledge Graphs for Recommendations](https://arxiv.org/pdf/1811.04540.pdf) (paper). Take a song that a user listened to and predict another based on graph walks. You train an embedding layer based on path traversals between Users and Songs, then feed those into an LSTM to come up with a prediction. 

Neo4j has POC versions of DeepWalk and DeepGL, which do not yet scale well at all … but they're getting there.

### Graph Native Learning

Everyone knows what deep learning is … but **graph native learning** is when you take a graph as an input, perform computations, and return a graph. Paper: [Learning Deep Generative Models of Graphs](https://arxiv.org/pdf/1803.03324.pdf).

Example is electron path prediction: looking at where electrons will end up based on the chemical reaction graphs … holy shit ([paper](https://arxiv.org/pdf/1805.10970.pdf)).

