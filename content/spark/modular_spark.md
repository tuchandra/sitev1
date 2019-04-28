# Modular Apache Spark: Transform Your Code into Pieces

Albert Franzi (SWE @ Alpha Health) - 4/25
___

Slides available [here](https://docs.google.com/presentation/d/19XWds36PwDeYQw3A9UwaRBZvDi5g2p79-9aljEWHknI/edit#slide=id.g41055d5fd6_0_62). The audience was 60–70% data engineers, remainder data scientists and random others.

## Simplifying Spark code

This is "how we simplified our Spark code by modularizing it." Asked the questions to the data engineers:

* have you ever played with duplicated code in your Spark jobs?
* have you ever had a code review turn into chaos?

Talked about how the Spark job can be fragmented into:

* readers
* transformers, including aliases, joins, formattesr, etc.
* task context
* writers

For the **Readers and Writers**, he recommends:

* enforce schemas
* use schemas to read only the fields you are going to use
* provide Readers per dataset, and attach its sources to it
* share schemas and sources between Readers and Writers
* GDPR compliant *by design*

For **Readers**, he went through the code examples — just look at the slides. 

For **Transformers**, he recommends providing a list of available trasnformations to your data scientists. That's what Uni is trying to do, so that's nice. Recommends the libraries [spark-daria](https://github.com/MrPowers/spark-daria) for Spark and [quinn](https://github.com/MrPowers/quinn) for Pyspark specifically.

For **Task Contexts,** you should … do … something. Have your data scientists write job runners that accept Readers and Writers as parameters (which also increases testability of the code, that's just dependency injection).

A question was asked about how you socialize available Transformers, and what data scientists do if they don't find what they need … the answer boils down to organizational communication, and having data scientists contribute back to your codebase.

Use currying within your Transformers to reduce reliance on schemas: 

* [Chaining Custom DataFrame Transformations in Spark](https://medium.com/@mrpowers/chaining-custom-dataframe-transformations-in-spark-a39e315f903c)

* [Schema Independent DataFrame Transformations with Spark](https://medium.com/@mrpowers/schema-independent-dataframe-transformations-d6b36e12dca6)

## Increasing test coverage of Spark code

Asked the question "who here has put untested Spark code into production?" and someone responded "if we test in production then everything is tested!"

Library [spark-testing-base](https://github.com/holdenk/spark-testing-base) from Holden Karau at Google. It lets you use a shared SparkContext across tests. This boils down to "please test your code," and this is made easier by testing each piece independently.

## Reducing test time execution

"How many of you are experiencing issues where your tests take too long? … Are the rest of you the ones who aren't testing?"

This was fairly Scala specific, sadly, since he talked about the package Junit4Git. It basically lets you skip tests whose related code wasn't changed by integrating with Git. Great talk.