# Beyond reason codes: a blueprint for human-centered, low-risk ML

## Patrick Hall (H2O.ai) - 4/24

## The ML Lifecycle

Opened with a slide about the same data science lifecycle that we've seen over and over. "Here's the workflow that you wouldn't shoot yourself in the foot with … and also take into consideration a lot of human aspects of what we do." He said that it's important for fairness concerns, ethical concerns, and much more.

He is very worried that if we (data scientists, engineers, etc.) don't take it upon ourselves to regulate practices, then a government will come in and be like "you can't do this, you can't do that, you can only do this" in some crazy draconian way. Which … yeah that's true.

Don't let perfect be the enemy of good here: it would be difficult for everyone to do everything on this slide, but you gotta start somewhere.

This talk *starts* with the assumption that you have all your data in one place, that it's all clean, etc.; other talks at this conference can go into how you get there.

### EDA and Data Visualization

This is basically business as usual. References:

* H2O-3 aggregator
* The Grammar of Graphics

### Establish Benchmarks

You have to start with some kinds of benchmarks, before any feature engineering gets done - run a linear regression or single decision tree. Don't *only* think about accuracy, think about disparate impact or security or privacy or other things … accuracy is important, but not as important as a lot of people think it is (we measure accuracy on static test datasets and then apply it in the real world).

Establish benchmark —> then you can gauge improvements in fairness, interpretability, privacy, or security.

### Feature engineering

References:

* Pandas Profiler
* FeatureTools
* Deep Feature Synthesis ([paper](http://www.jmaxkanter.com/static/papers/DSAA_DSM_2015.pdf))

Features will have to be explained and justified. Don't introduce undue complexity in feature engineering; if you're using autoencoder features you might have to explain them one day.

### Preprocessing for fairness, privacy, or security

There are lots of things you can do to make data more "private" or "fair." Preprocess data to remove disparate impact ("when your predictions are more than 20% different for one group vs. another group", which is a legal definition). There are tools to preprocess causes of disparate impact out of your data, if you want to use them.

You can also preprocess to remove PII, which is super *super* important.

### Modeling: constrained, fair, interpretable, private, or simple models

We all want to do deep learning … but when we do the most complex ones, we get ourselves into trouble w.r.t. explanation, or proving a lack of disparate impact, or proving that your model wasn't hacked (e.g., adversarially).

If your model is so complex that you can't explain it, how do you know no one has changed it?

* Explainable Neural Networks based on Additive Index Models (XNN)
* Learning Fair Representations (LFR)
* LIME, LIME-SUP (the SUP is supervised partitioning)
* Private Aggregation of Teacher Ensembles (PATE, secure and private)
* Scalable Bayesian Rule Lists (SBRL, rules printed in orders of importance)

Favorite example: monotonic gradient boosting trees. This lets you explain things by being able to say "if this input goes up, our probability *only* goes up." **Monotonicity** is a super useful and popular part of interpretability. You're not just stuck with linear models and random forests!

###Traditional model assessment and diagnostics

The same metrics as usual matter; AUC on train, test, validation, accuracy, whatever. This isn't that different.

### Post-hoc explanations

**OSS resources**: LIME or SHAP. Papers include:

* [Why should I trust you? Explaining the predictions of any classifier](https://www.kdd.org/kdd2016/papers/files/rfp0573-ribeiroA.pdf) — this is the LIME paper
* [A unified approach to interpreting model predictions](http://papers.nips.cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf) — this is the SHAP paper
* [Please stop explaining black box models for high stakes decisions](https://arxiv.org/abs/1811.10154) - criticism

Also talked about **Shapley values**, which came from the 1950s but didn't make it into ML until 2017. It is "the player's contribution to a cooperative game," but instead we think about features in a model. They disaggregate the contribution of each variable for every prediction, much like the value of every person to a game. Lloyd Shapley won the Nobel Prize for this in 2012.

The 2017 SHAP paper managed to take Shapley values from being exponential time to log polynomial time, which is huge! They are consistent (if you change your model or data a little bit, this is pretty stable). It tells you the feature contribution of every single row in your dataset very accurately, which is incredible!

### Model debugging

This is related to model diagnostics, but the first academic workshop about this will probably happen in two weeks at ICLR. It can mostly be defined as testing your model to find problems with accuracy or security that you can fix. OSS libraries include **cleverhans**, pdpbox, and **what-if-tool.** They're all based on sensitivity analysis (which you should probably always be doing in ML).

Cleverhans looks for the minimal change you can make to change the output of the model; this shows how models can be hackable. If you have a prediction API out there, then people know how to steal your model … and they can do sensitivity analysis and understand how they can get the output to flip the predictions.

pdpbox does partial dependence, telling you how much data you have in certain regions of feature space. If your data is sparse, pdpbox can identify that and tell you about it.

what-if-tool is from Google and answers the question "what happens if you do this" like switch someone's gender. If you change your data and see what happens, that's a very impactful testing tool.

Papers include:

* [A Marauder's Map of Security and Privacy in Machine Learning: an overview of current and future research directions for making machine learning secure and private](https://arxiv.org/pdf/1811.01134.pdf)
* [Modeltracker: Redesigning Performance Analysis Tools for ML](http://saleemaamershi.com/papers/amershi.CHI2015.ModelTracker.pdf)
* [The Security of Machine Learning](https://people.eecs.berkeley.edu/~adj/publications/paper-files/SecML-MLJ2010.pdf)

This kind of testing is super *super* important to do, because you have to understand what happens when you see something outside of your training data.

### Post-hoc disparate impact analysis and remediation

Again, disparate impact is legally defined, "when your predictions are more than 20% different for one group vs. another group." If you're doing ML that involves people, this is essential to do.

There's a concept called the "multiplicity of good models," where for any good dataset there are usually lots of good models. You can probably find a model without disparate impact that is just as good as one that does have it.

OSS includes **aequitas** and **themis**.

Papers include:

* [Equality of Opportunity in Supervised Learning](https://papers.nips.cc/paper/6374-equality-of-opportunity-in-supervised-learning.pdf)
* [Certifying and Removing Disparate Impact](http://sorelle.friedler.net/papers/kdd_disparate_impact.pdf)

### Human Review and Documentation

This is the most important part even when people don't care about the other stuff - this is how you preserve knowledge so you have reports of what people did ("when all your hotshot data scientists leave for other jobs"). Google just wrote a paper ([Model Cards for Model Reporting](https://arxiv.org/pdf/1810.03993.pdf)) about this, but it's something banks have been doing for decades.

For every model they train at H2O.ai, they generate a very basic report - what was the data, what was the model, what features were used, who trained it, when was it trained, etc. - and that saves a ton of time and is a sound business practice.

### Deployment

A lot of data scientist struggle with the problem of "I've got all my beautiful and perfect Python code on my laptop, and now it has to run on this server in C#?" Deployment is the most important part of the process — until you've deployed you're just a cost center. Undue complexity will harm deployment, and that will cost you accuracy (because the time between train and prod will increase).

### Human Appeal

If you are doing machine learning that involves making decisions on people, they should be allowed to appeal those decisions; full stop. We all know that there can be all kinds of data quality problems, the data can be completely wrong, or the model may do a bad job.

He gave an example of apps that may have rankings for babysitters, and if you are a babysitter who gets a bad ranking based on some model, then suddenly you might lose your part time job … again, all banks follow this, if you're denied a credit card they have to tell you how you can improve. But that's not the case (yet) in ML.

### Iterate

Think about things besides accuracy - the test data accuracy is probably not as meaningful as we hope it is. Think about privacy, security, interpretability, fairness. KPIs should not just be restricted to accuracy (or related metrics).

## Open Questions

How much automation of this is appropriate? How much is possible?

How do you automate learning by iteration, e.g., via reinforcement learning? We're trying to keep people in the process, but one of the reasons we take people *out* of the process is because they have these inherent biases.

How do you implement human appeals, from an HCI perspective?

Links:

* [Awesome Machine Learning Interpretability](https://github.com/jphall663/awesome-machine-learning-interpretability)
* [Interpretable Machine Learning with Python](https://github.com/jphall663/interpretable_machine_learning_with_python)

Question from the audience was "what would you do?" Monotonic xgboost with partial dependence and ICE plots, notebook [here](https://github.com/jphall663/interpretable_machine_learning_with_python/blob/master/xgboost_pdp_ice.ipynb). 

Another question: you can kind of explain any model, but also don't use autoencoder features, is that a contradiction? Answer is that you *can* explain them, but it's way harder than other features. Whether that matters or not depends on your use case.

This talk was awesome.