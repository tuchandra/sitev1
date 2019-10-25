<!-- date: 2019-10-24 -->
# Netflix and Polynote
Netflix [announced yesterday](https://medium.com/netflix-techblog/open-sourcing-polynote-an-ide-inspired-polyglot-notebook-7f929d3f447) that they are open-sourcing Polynote, a new notebook with features like Spark integration, as-you-type autocomplete, and more. At a glance, it seems to address almost every common complaint with notebooks. How much of that is too good to be true?


## What I don't like about Jupyter notebooks
Jupyter notebooks are an essential part of the data scientist's toolkit. Being able to mix Markdown, code, results, and images is great for documenting your work, and inline plotting is fantastic given how painful plotting in Python can be. Notebooks also make the field more accessible to beginners, though arguably at the risk of instilling poor practices. I use notebooks weekly as a professional data scientist.

With all this said, one of my favorite talks is ["I don't like notebooks" by Joel Grus](https://www.youtube.com/watch?v=7jiPeIFXb6U). I recommend that everyone watch this--not to convince you that notebooks are bad, but to begin thinking about *how your tools limit you.* Some of Joel's complaints, which I largely agree with, are listed below:

 * tons and tons of hidden state, coming from out of order execution, being able to edit cells after you run them, and (importantly) lack of beginner-focused resources and tutorials addressing this issue
 * discouraging good software engineering practices like unit testing
 * poor autocomplete compared to IDEs
 * inability to interface with other dev tools: type checkers ([mypy](https://github.com/python/mypy)), linters ([flake8](http://flake8.pycqa.org/en/latest/)), autoformatters ([black](https://github.com/psf/black))
 * lack of reproducibility

In other words, notebooks--while great to get started with--make real software development harder. That's not to say that notebooks are the only way to write bad software; it's rather that they, in Joel's words, "implicitly encourage a workflow that has these issues." Again, I highly recommend Joel's talk.


## A walk through the features
Honestly, while reading the Medium post, I was stunned. My first thought while reading it was "this can't be real"--that Polynote addresses almost all of my complaints about vanilla Jupyter notebooks.

**Reproducibility**: Netflix built the interpreter from scratch and made an unusual design decision: a cell's input state is defined exclusively by the cells above it. This means that later cells cannot affect earlier cells, which makes reproducibility a lot easier.

**Dependency and config management**: you can specify notebook-level dependencies and Spark configuration. This *couples* notebooks and their computing environment. At first glance, this might seem backwards; normal software projects will have a `Dockerfile` or `requirements.txt` to document the environment. But given that most notebooks don't document their environments at all, I'll happily take this.

**Inline data visualization**: from the GIFs and screenshots on Medium, it seems like Polynote has some kind of inspector to create plots basd off data. It supports both matplotlib and [Vega](https://vega.github.io/vega/), the latter of which I am very excited for.

**First-class Spark and Scala support**: huge. I haven't used Scala myself, but having Spark tightly integrated into the kernel is what [Databricks](https://databricks.com) does, and it makes scaling up easily.

**Better autocomplete**: they have it! At least according to the demo screenshots on Medium.

**Other features**: multi-language support (I only code in Python, but that's certainly nice for others), visibility into what the kernel is doing (nice because the Spark UI can be extremely opaque), combining Markdown and code (apparently [not fully](https://github.com/polynote/polynote/issues/106) yet).


## Some of my concerns
My main concern is how long this will last: corporate open source has a long history of being published, maintained briefly, and then abandoned. Granted, that's true of normal open source too, but usually when there's a company behind it one hopes that the project will last longer. If maintained, this project has the potential to revolutionize notebook computing. If not, it'll fall by the wayside as another failed alternative to Jupyter.

Another is that there are some nice-to-have features missing: [renaming notebooks](https://github.com/polynote/polynote/issues/445), [conda support](https://github.com/polynote/polynote/issues/405), a [restart and run all button](https://github.com/polynote/polynote/issues/381), [auto-indentation](https://github.com/polynote/polynote/issues/265), and [links in a text cell](https://github.com/polynote/polynote/issues/106). This is clearly a beta product, and so the support it receives over the next few months will be critical for its adoption.

Likewise, the documentation doesn't really exist [at all](https://polynote.org/docs/) yet. Again: it's a project in its infancy, so I don't expect much now but hope for more later.


## Final thoughts
Polynote shows a ton of promise; at first glance, it appears to address many common concerns with Jupyter notebooks. When Netflix [said](https://medium.com/netflix-techblog/notebook-innovation-591ee3221233) that they built their data science organization on notebooks, I didn't realize it was on a tool as powerful as this. I hope that I have the chance to try it out myself soon.

