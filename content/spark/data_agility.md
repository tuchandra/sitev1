# Data Agility - A Journey to Advanced Analytics and ML at Scale

## Hari Subramanian (Eng. Manager @ Uber) - 4/25

At the time of writing the talk proposal, he was leading the "big data analytics and data science workbench" teams at Uber, but now he's running "customer obsession engineering."

## Introduction

Data-driven company - make data-driven decisions throughout the org. Their scale is millions of Uber trips daily, 2T messages processed by Kafka, 1M queries across Hive / Vertica / Presto, and 150TB of data ingested into HDFS. They're constantly at the limits of OSS, and so they often have to build their own tools (like the data platform).

## Data Platform

Walked through the layers of their data platform:

* They have lots of data sources, which is where raw data comes from; tons of in-house storage infrastructure. 
* Then ETL frameworks and data integrity to keep the data sane, enforce constraints, etc.
* Modeled tables and custom datasets live on top of the ETL layer, which is useful for business analysts or people with well-defined data needs. 
* And then there are the data-driven applications: mining business insights, experimentation, and data science / machine learning. This is the data exploration, query engines, and knowledge bases.
* Finally, on top, are the business insights and conclusions that are for nontechnical people.

The problem that new employees faced was that getting started with data processing was hard; everyone had their own expertise and packages, and getting access to data was (as usual) super challenging. There was no standardized environment, so lots of local analyses and local environments, and this made collaboration difficult. People transferring internally had to learn new sets of tools. People's environments different from what was happening in prod meant that challenges arose unexpectedly.

## Data Science Workbench

The mission for the Data Science Workbench team was to build a platform that:

* worked for many users, and not necessarily technical ones
* handle the different infrastructure needs (CPUs vs. GPUs, cloud, etc.)
* have single window access to bring together everything instead of run four different programs
* met cost and compliance requirements, was secure, met GDPR, etc.

And so DSW started as a web-based applicaiton for hosting notebooks, but now its mission is to "democratize data science by enabling access to reliable infrastructure and advanced tooling in a community-driven learning environment." That's a mouthful, but wow that's great.

### Today's version

* 1-click access to get started with Jupyter Notebooks or RStudio
* Secure access to all internal data sources, stored in multiple data centers, and GDPR compliant
* Pre-baked environments that meet common needs and also increase standardization
* Easy ways to share notebooks internally to get feedback or present results
* 1-click Shiny dashboard publication
* Scalability, via various session types, machine sizes, access to compute engines
* Great documentation

Some of the key features include:

* **interactive workspaces**, for exploration, preparation, ad-hoc analyses, or model exploration
* **advanced dashboards**, visualizing insights from complex analyses or dsiplaying business metrics
* **business process automations**, which was not planned; but it allows them to automate complex processes, train small models, or schedule data pulls

To the last point: each operations team across the world has different requirements (for compliance with the local laws, for reporting, for growth strategies, etc.). And DSW was able to automate a ton of operational analyses or data pulls that previously required manual work. A central engineering team was never able to do this because the requirements were so disparate, but baking in automation into DSW made it possible.

### Architecture

The **workbench** is Shiny / Bokey, RStudio, or Jupyter. This interfaces with an **application management service** that lets you create / delete / search / share / publish / schedule your sessions / files / dashboards / jobs. Then there are **docker containers** hosting different environments on a dedicated cluster, all with access to a **shared filesystem**. And they have connections to all their **data sources**, obviously.

### Problems Solved

Uber has a fairly mature data science environment; so DSW turned into a swiss army knife. If something didn't exist, data scientists would typically go into a notebook and start writing it.

It helped them to enable operations folks or MBAs to do simple analyses that helped them make decisions. It seems to me that the big wins came here from reducing the barrier to entry by giving everyone access to DSW and creating useful interfaces.

Business process automation is huge, which yeah good. Business analysts were able to automate analyses that were super maual before.

And, of course, engineers or data scientists or researchers were able to do exploratory work, model training, and productionalization. Tons of models were built for specific problems and then deployed on DSW.

### Case study

He went into a case study about the customer success team that I was only listening to, and not taking notes on.

## Lessons Learned

Build tools for the experts but design for the less technical. Open up services via APIs, but keep everyone in mind when designing.

Don't stop building what's known, but rather empower people to look for the unknown.

Create communities with both data scientists and non-data scientists; let them work together and collaborate.

