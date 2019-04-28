# Predicting communities via graph algorithms

Amy Holder and Soren Reichardt (Neo4j) - 4/24
___

## Intro
Graphs are everywhere; anything with connections can be represented as a graph. And for them, graphs drive innovation. One of the questions they get is "is this a graph analytics problem?"

 * **propogation pathways**, diseases, traffic, etc.
 * **flow & dynamics**, what happens when I constrain my network, do things flow in a different way, like with routing
 * **interactions and resiliency**, community detection, influence within communities, understanding how things may break apart or become more cohesive

All require you to understand the structure of your data.

## Real-World Data
If you assume that most nodes have the same number of relationships, then you would have a Gaussian distributions of relationships ... but network science tells us that this doesn't happen in nature.

Instead, number relationships and nodes follows a quasi-power law distribtuion.

```
number of relationships
| *
| **
| **
| ****
| ************
|________________
 number of nodes
```

## Graph algorithms
You could either **query** the graph for real-time, local decisioning and pattern matching. Or use **graph algorithms** for global analysis, learning the overall structure of a network an dmaking predictions.

Common graph algorithms include:

 * pathfinding / search
 * basic stats
 * decomposition, covering, coloring
 * network flow
 * centrality or importance
 * community detection

Uncommon ones include:

 * similarity
 * link prediction
 * ML workflow (@DSS)
 * many others ... 

**Spark 3.0** is going to have "property graph model" with Cypher queries and graph algorithms. Unclear what all this means tbh. Meanwhile, Neo4j is a native graph platform.

## Demo
They're gonna use a Game of Thrones script dataset, making a graph based on how close names are to each other within the script. Tools include Spark GraphFrames (which will be deprecated in favor of Cypher in 3.0) and the Neo4j platform.

### Triangles and the clustering coefficient
Use these tools for:

 * basic network analysis (does it have small-world structures)
 * estimating stability
 * finding structural holes
 * scoring for other analyses

An example is spam classification; using a semi-streaming webpage analysis, you can look at if webpages are linked to others or just sitting by themselves. The clustering coefficient is the **measure of how much nodes tend to cluster together**.

The demo showed off generating the degree of the different characters and the clustering coefficient. Some of them have a high degree (many connections) but low clustering coefficient (but their connections aren't very conneted to each ohter), and others have the opposite.

### Closeness centrality
Use when you're finding which nodes disseminate things the fastest. Weighted relationships are helpful in evaluating interaction speeds in communication and behavioral analysis. This can be used as a heuristic for logistics or arrival times; another example is terrorist network analysis, where they ask "who in this network could acquire the most vital information?"

Looks at **which nodes have the smallest distance to all other nodes**. "Which node can most easily reach the others?"

Demo: the Spark version doesn't run on his computer because of all the UDFs ... then talked about **aggregate messages**, which for every vertex computes something and sends it to the neighbors. This ... didn't make a ton of sense.

### PageRank
Use when you're looking for **broad influence over a network**. There are *tons* of domain specific variations of this, e.g., personalized recommendations. Exampes include recommendations on Twitter (who to follow) or fraud detection (super interesting but unclear how). 

Measures the transitive influence of nodes, considering the influence of neighbors and their neighbors. People acquire credibility and influence from others with credibility and influence. You gotta be careful with node types here, because this compares node types to each other; you can't use this on a graph of e.g., products and humans (unless you're interested in open research questions).

Demo: was a one-liner in the GraphFrames API. Not interesting, but showed off who the most "influential" characters within GoT are. 

###Betweenness Centrality

 Use for:

* identifying bridges
* uncovering control points
* finding bottlenecks or vulnerabilities within your network

Study that looked at network resilience in Italy, looking for the key points of cascading failure. They actually learned that they should *remove* some nodes to increase reliability.

Betweenness centrality is the sum of the % of the shortest paths that pass through a node, intuitively looking for bridges within a graph. Computationally intensive, but has approximation algorithms.

This demo showed off Neo4j Desktop, where they used their GUI to show that Joffrey was the most important node … apparently many important conversations flow through him. ¯\\\_(ツ)_/¯ 

### Label propogation

Use for getting started analysing a graph, like:

* large scale networks with initial clustering
* preprocessing data (initial classification)
* where groups are less clear but weights can be used

Interesting example uses graphs and label propagation to look at drug combinations to see if they might be dangerous; they use chemical similarity and side effects to see what drugs should not be prescribed together.

Nodes adapt labels based on neighbors to infer clusters; weight relationships or nodes. This is non-deterministic, and seed labels are very powerful and can propogate through a network. That means this can be used as a semi-supervised learning technique.

The demo used Spark again, and assigned random labels and watched them propogate. They say that this loosely matched the houses in GoT, which … okay. Then they went into Neo4j and looked at the clusters visually - that was awesome, showed one cluster that's super disconnected because they're an island, one cluster that's King's Landing (?) and man I know nothing about GoT.

### Louvain Modularity

Use for:

* community detection in large networks
* uncovering hierarchical structures
* evaluating different grouping thresholds

This continually maximizes the modularity (optimal grouping) by comparing relationship weights and densities to an estimate. What? The algorithm is trying to find an optimal grouping of nodes; intuitively like a what-if analysis, like if I move this node to that group what happens, repeat. But *then* it groups those into supergroupings and repeats that to smash groups together. 

It helps you when the question is "how far out do I want to go," like going to just close communities or ones that are further or very far or whatever … interesting. The demo showed, for each character, 3 levels of communities; the first one had the most granular communities, then some of them got absorbed, then even more others got absorbed.

## Resources

Dataset collections:

* Stanford network analysis project (SNAP)
* Colorado Index of Complex Networks (ICON)
* Koblenz Network Collection (KONECT)
* Girvan-Newman (random, reference dataset for testing)

Question: how do you take advantage of local processing e.g., in networkx. Do that for starting out, and switch to a more enterprise platform (Spark, Neo4j) when you need to. Those can help by providing approximation algorithms too.

Question: with Spark 3.0 and Cypher coming in, will you have access to the machine learning algorithms within Cypher as well? Not sure, but Databricks is planning on having the API have parity with the GraphFrames API.

