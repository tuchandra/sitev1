# Moving a Fraud-fighting random forest from sklearn to Spark with ML, MLflow, and Jupyter

## Josh Johnston (Director of AI Science @ Kount) - 4/24

## Data science lifecycle

Opened by talking about the model lifecycle - stole a slide from Microsoft about the data science lifecycle. Business understanding, modeling, data acquisition & understanding, and deployment; these all connect to each other. Modeling includes feature engineering, training, evaluation. Data acquisition includes the data sources, pipelines, environment (on-prem / cloud), exploration, cleaning.

Focus in this presentation is **modeling** - configuration management, speed, accuracy (how good is the model?), validation (is the model doing the right thing?). There are some **governance** questions about what model you're using and how you access it … e.g., the question "what model is running in production?" which is insane.

There are some really specific questions that people always ask:

* what model are we using?
* do we know what assumptions are made?
* did we sample? how?
* what metrics did we use to decide that this model was working well?
* what parameters did we use?
* how well does it work?

and a lot boil down to "**why did we pick this model and not others?**" because you don't always know that. And this can super important in other industries, too, where you have to be audited or whatever … but that's still not the core problem. 

### Science is repeatable

Fundamentally, this problem isn't just to satisfy your legal department or auditors. Science needs to be repeatable; it's not enough to throw a model in production. As data scientists, we're probably not satisfied until these questions are all answered.

## Fraud detection model

They have a model called Boost, which is their supervised machine learning model for some specific type of fraud detection. This model helped in many quantitative ways (reduced manual reviews by 20% or 200h/month) and also many qualitative ones ("we get fewer complaints from our fraud department" etc.).

Technical details:

* 200 GB of precomputed data after feature engineering
* random forest with 250 trees, 100K nodes per trees, which is about 1GB when serialized
* model training = 150 features *after* feature reduction (before this the cardinality is in the billions, because things are tokenized), 60M observations.

### Old process

"Process" is a loosely defined term here, because a lot of this was very ad-hoc. They had a huge analytics database, then a gigantic computer for all the model training … 400 GB RAM and 1TB into swap, which is absurd. Their model kept pounding their database and making enemies with their DBAs. Training the model took like 24 hours by itself, and the model got logged into a flat file and pickled into network storage.

He says that it took 2.5 days, but that depended on the interruptions; everything running in memory meant if something breaks, it's back to square one.

**What worked**: got a high value model.

**What didn't work**: time-intensive, errors forced restarts, burdened the production database, and pickling tied the training environment to the execution / prod environment (because you serialize the trained model and then have to unpickle it in prod). Also, traceability of errors is just provided by logs and manual documentation. And there were a shitload of ad-hoc experiments.

Thinking back to the governance questions: which model are you using? why? how did you train it? why? how well does it work? why?

### New process, WIP

They made a cluster for distributed computing: 6 nodes, 484 vCores, 1.35 TB RAM, Cloudera and Spark 2.4, mostly Python.

Still using the analytics database because that's what's in prod; but then they pull data out using Sqoop and store it in HDFS. That's the last time they have to deal with the prod database, which is incredible! And so the Spark cluster can do lookups against HDFS (automated with Luigi, for error checking) and train the model with Spark ML. 

They do remote development with Jupyter, claiming that most criticisms of notebooks are things you *could* do, not things you *must* do. Reliance on their tools to enforce good development practices is a sign that your development practices probably aren't very good. Good development practices are independent of tools.

They use Git throughout, despite having notebooks. In increasing order of maturity, they have:

* notebooks, which are mostly research
* Python packages, with code that gets pulled out and shared
* Pyspark applications, that can now be runed
* automated applications, which are refactored, hardened, and fully operationalized

**What works**: faster, failures restart in the middle (the last time you saved to HDFS), reducing burden on the production database, being able to redesign experiments at will, decoupled training and execution environment via MLeap.

**What doesn't work**: Spark tuning is a pain, and non-deterministic Spark ML behavior can be difficult. And Spark pipelines depend on configurations that change based on the input data. They can't go back and recreate a historical model because they don't have access to the historical configuration and state of the data.

## Tools

Repeating the governance questions:

* which model are you using? why?
* how did you train it? why?
* how well does it work? why?

This gets us back to doing *real science*, in his words, instead of "just" being craftsmen making whatever we want.

**Luigi**: appears to be basically Airflow.

**MLflow**: is incredible and they discovered it too. Having everyone look at the same dashboard of parameters and metrics is super useful - avoids ad-hoc experiments and reports and presentations being decoupled. The metrics are preserved forever, and you can come back to the models whenever you want. The comparison plots of different runs help them too. They save artifacts of the model itself, plots, and the code to generate it.

"When you're answering governance questions, if you ever get audited, you don't want to have to answer anything—you don't want to have to *explain* anything. You want to be able to point to something and say 'that one' and look at a dashboard and say 'here's why.'"