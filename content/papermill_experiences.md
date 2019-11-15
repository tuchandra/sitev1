<!-- date: 2019-11-15 -->
# Using papermill to wrap model runs
I recently started using [papermill](https://github.com/nteract/papermill/) from nteract to parameterize model runs. I've started to like it a lot, and this post will discuss my experiences with it and my current setup.

## My use case
My current task at work is a modeling problem where I'm trying out different versions of models fairly quickly. I have a lot of freedom in my toolchain; I'm using [Pyro](http://pyro.ai/) for probabilistic models, but beyond that I can use any other libraries to help me with this process.

At first, I was trying out basic models to better understand my problem and my dataset. As those matured, I got into a fairly quick train/diagnose/modify cycle, where I'd (1) train some model, (2) make visualizations to understand what it's doing, (3) update the model based on hunches about how to make it better, and (4) repeat. I think this is a fairly common cycle for data scientists to find themselves in.

The main limitation here was the disconnect between training and visualizations. I want all of my data prep code and modeling code to be in Python scripts, but I want to make visualizations in Jupyter notebooks. I *don't* want my modeling code in notebooks, because notebooks [encourage poor software development](https://www.youtube.com/watch?v=7jiPeIFXb6U). I don't want my visualizations in scripts because they either (1) open up and block the rest of my script or (2) get saved to disk somewhere, and I have to spend time opening them myself and remembering which graph went with which model. More generally, I wanted report-style visualizations, where the graphs were surrounded by code, headings, and prose.

I'd heard of papermill a year ago, but never got around using it; a couple weeks ago, I decided to take the plunge into figuring it out. It has been a huge success.

## My setup
It took a lot of iteration to reach this point, so I'll just describe the final result.

 * data prep code: in an library (e.g., `lib.data`), which has code to initialize my dataset objects, clean them, and transform them 
 * plotting code: in a library (e.g., `lib.plots`), which has code to make common visualizations from datasets of predictions
 * modeling code: my main script (e.g., `model.py`), which is where model classes are declared. The training loop lives in a `main` function here

So far, things are pretty standard. I have code factored out into libraries, testable functions, and the ability to train a model by running the main modeling script. Here is where papermill comes in.

I have a **template visualization notebook** which calls the `main` function of `model.py` to train a model, then goes on to make diagnostic plots and reports for me. It's parameterized at the top with things like the number of hidden units in my neural network, the learning rate, or the number of epochs to train for. Note that *I never run this notebook directly*--only papermill does.

Finally, I have a driver script which (1) uses `papermill` to run the notebook with parameters that I specify there, (2) uses `nbconvert` to convert the notebook to an HTML document. This lets me open up the HTML report directly in my browser without having to have Jupyter running. Additionally, the HTML report is immutable--by design, I can't go back and mess with anything, so I don't have to worry about changing code after it has executed, one of the common pitfalls of notebooks.

Having a driver script lets me run the same model multiple times to check for stability, train models with different hyperparameters, or test out different model architectures. It means I can run `python pm_driver.py`, wait for my model to train (and go write, say, a blog post on papermill), and come back to finished HTML documents with visualizations on how they performed.

## Final thoughts
Papermill is incredible--it's undoubtedly changed my workflow for the better. At first, it was a lot of messing around to get everything to work, and it took a couple of weeks to land on a setup that worked for me. But now that I can separate model code from reporting code, but run both at the same time, iterating has gotten easier and faster.

Because all of this is work code, I unfortunately can't share what I've created. I'm happy to talk about my experiences further if you'd like to email me@[this domain].
