# High Performance Transfer Learning for Classifying Intent of Sales Engagement Emails: An Experimental Study

Yong Liu (Outreach) and Corey Zumar (Databricks) - 4/24
___

## Data Science Research Objectives

To establish a high-performance transfer learning evaluation framework for email classification. Research questions include:

* which embeddings and pre-trained language models should we use?
* which transfer learning implementation strategies (feature-based vs. fine-tuning) should we use?
* how many labeled samples are needed?

### Sales Engagement Platform

This is a new category of software, and where Outreach sits. It sits on top of CRMs (e.g., Salesforce, SAP, Microsoft Dynamics). SEPs encode and automate sales activities into workflows. Examples include:

* automating execution and capture of activities, which get recorded in a CRM
* scheduling and remidning the rep when it is time to do manual tasks
* enabling reps to perform 1:1 personalized outreach up to 10x faster than before

### So why email classification?

Email content is critical to driving sales, obviously. A replier's email *intent* is much more powerful than a simple "reply rate" metric. If you A/B test the metrics themselves, you can pick winners even more confidently.

But this is hard. You have different contexts (emails could be anywhere in the sales process from prospecting to closing) and different players (multiple audiences, multiple organizations, multiple levels of importance within an org). You also have a limited dataset, especially when factoring in privacy cnosiderations (maybe emails are so tightly locked down that it's not even possible to label them).

### Which brings us to transfer learning

Because pretrained language models open the doors for high performance transfer learning (fewer training samples necessary, better accuracy, reduced training time). And we know that pretrained language models like BERT are SOTA, though it is unclear whether they can be translated to practical applications.

## Experiment Setup

They used four pretrained language models:

* GloVe (2014): count-based, context-free word embeddings
* ELMo (2018): context-aware character-based embeddings, based on RNN
* Flair (2018): contextual string embeddings
* BERT (2018): SOTA transformer-based deep bidirectional language model, from Google

Then they annotated their own email dataset into four categories: not sure, objection, positive, unsubscribe. The dataset is unbalanced and only has 3K examples or so. 

So they designed two sets of experiments, both using the feature-based and fine-tuning approaches: 

* using the full set of training examples
* using different training sizes

The feature-based approach tuned the last 4 layers to extract vectors, and used the uncased (small) BERT model.

### Results

The first set of experiments found that BERT fine-tuning had the best F1 score, and GloVe did the best of the feature-based approaches. Classical ML models (LightGBM + TF-IDF) underperformed BERT. 

The second set of experiments found that BERT fine-tuning outperformed all feature-based approaches, but only when training size > 300. BERT fine-tuning required 500 training examples to get F1 > 0.8, whereas feature-based approaches required 2000 examples.

### MLflow

They used MLflow to manage experiments and keep track of results here. Corey talked about the different components of it, which I already knew about. This was mostly just a demo of what MLflow can do.

## Summary

Transfer learning using fine-tuning BERT outperformed *all* feature-based approaches that were using different embeddings … given sufficient (300+) training examples.

Pretrained language models solve the cold start problem when there is very little training data; but to get F1 > 0.8, you may still need 1–2K examples for a feature-based approach or 300+ for fine-tuning.

MLflow enabled all of this work. Future work includes using MLflow to track what's going on in production, and not just in experiments. They are considering extending this to cross-org transfer learning, too.