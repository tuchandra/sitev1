<!-- date: 2019-12-21 -->
# What I read this week
Summaries of articles and blog posts that I've read this week.

## [A sobering message about the future at AI's biggest party](https://www.wired.com/story/sobering-message-future-ai-party)
**Author:** Tom Simonite

**How I found this**: The [Skynet Today](https://www.skynettoday.com/) newsletter

**Summary**: This article talks about a recurring theme at NeurIPS 2019, which took place last week. "Leaders in artificial intelligence warn that progress is slowing, big challenges remain, and simply throwing more computers at a problem isn't sustainable," reads the subheading. It's becoming more and more clear that this is true—advances in compute can, in my opinion, only take us so far, and researchers warned of the limitations of the current state of AI.

**Commentary**: AI research is encountering some of the same roadblocks it always has—progress is slow and incremental, no one knows what or when the next breakthrough will be. But that's research!—that's always been the case. Now, though, the field has to combat increasing hype about AI, (somehow simultaneously) public skepticism (see, e.g., the [biased algorithms](https://www.nytimes.com/2019/12/06/business/algorithm-bias-fix.html) article from last week), and the looming threat of regulatory overreach. Facebook's head of AI Jerome Pesenti argued that AI research will soon hit the wall, but some might say it already has.

## [The AI community needs to take responsibility for its actions]
**Author**: Karen Hao

**How I found this**: from Skynet Today

From the article, emphasis mine:

> **"There’s no such thing as a neutral platform,"** the influential scientist [Celeste Kidd] and prominent #metoo figurehead told those gathered at the NeurIPS conference in Vancouver. "The algorithms pushing content online have profound impacts on what we believe."

As we consume more recommended or otherwise algorithmically curated content, there is no "control group." YouTube can't suggest "neutral" recommendations short of showing us totally random suggestions—every algorithmic decision made impacts what we see in some way. Google can't show us "neutral" search results; they can only show us what they believe are "best," "most relevant," or (for the cynical) "most likely to help them sell ads to us." As Kidd said, "I don’t think there’s enough sensitivity in tech to how the decisions that you make behind the scenes about how to push content impact people’s lives."

This was awesome—I have to watch the talk itself soon. 

## [How to stay productive when you're understaffed](https://blog.veamly.com/stay-productive/)
**Author**: Valentin Sawadski

**How I found this**: from [Pointer](https://pointer.io)

This article describes how to avoid getting burnt out, especially in the case where you're overworked and understaffed. From the article: "You will not know when you are close to a burnout, so trust the people around you." In the author's case, they took reasonable precautions (working < 50 hours, not working weekends, taking breaks, etc.) but still got burned out at work. They suggest the following:

 * **self-care**, aka spending time outside the office
 * **realistic planning**, consisting of macro reality checks (looking at how long things have taken in the past to make sure you have reasonable estimates) and micro reality checks (looking at your calendar and putting tasks in it)
 * **optimize efficiency**, meaning increasing focus time and removing gaps, removing meetings where possible and making sure to build in prep / followup time otherwise, and stop fighting biorhythms (if you're tired after lunch (me!) just use that time for email or some other nonsense)
 * figure out what you can do to make things easier *permanently*

## [Organizational complexity is the best predictor of bugs in a software module](https://augustl.com/blog/2019/best_bug_predictor_is_organizational_complexity)
**Author**: August Lileaas

**How I found this**: from our head of data science sharing in Slack

In 2008, Microsoft Research published a statistical model for predicting the risk of having bugs in some software. The best predictor (based on both precision and recall) of bugs was **organizational complexity**, above code churn, code complexity, dependencies, code coverage, and pre-release bugs. The study has apparently been successfully replicated.

This is consistent with my experience. Code that is touched by multiple people across an organization is likely to be harder to work with. Code that a small team writes is easier to verify for correctness. Software development is a team activity which gets harder with more people ("too many cooks"), and this reflects that.

## [What makes Python a great language?](https://stevedower.id.au/blog/python-a-great-language/)
**Author** Steve Dower

**How I found this**: from Pointer

From the article: "What makes Python a great language? It gets the *need to know* balance right." Dower likens this to a military operation, where people at the lowest level have decision making delegated up, so that each person can focus on a small number of decisions that are important to them individually. "They can focus on exactly what they need to know, trusting that their superiors have taken into account anything else that they don’t need to know."

This is the same story as software abstractions, where other developers have taken context into account, and so users can focus on what they need to. One of the easiest examples is memory management; Python abstracts this away, so instead of spending time thinking about memory, Python users can focus on their actual task. This has obvious limitations, but Dower goes on to claim that Python gets the various levels of this right.

> Python very effectively hides unnecessary details from those who just want to use it.

Some examples:

 * `x, y = get_point_coordinates()` is obvious, and you don't have to know about return values
 * `for x in some_list` doesn't require you to know about iterators
 * `with open(f)` doesn't require you to know about the `io` module
 * other general examples about how Python tries to reduce boilerplate for you

What happens when it breaks down? (It does break down, and to claim otherwise would be foolish—not every abstraction is useful all of the time.)

 * There are no *truly* private members, so you can introspect everything to figure out what's going on in as much depth as you want
 * Duck typing lets things behave as other things so that you can overcome otherwise limiting abstractions
 * There's lots of public code; you don't have to know how everything works, but you have the option of learning

Python code isn't shared in a minified or obfuscated way. Python code doesn't emphasize privacy or information hiding. These enable you to get past challenging abstractions.

There are also many features that 90% of users *don't* need to know about. Assignments, function calls, attributes, built-in collections, and loops are probably enough for 90% of people. But the remaining 10% leaves room for creativity and expression:

> The next level up is where things get interesting. ... When I adopt classes, operator overloading, generators, custom collection types, type checking, and more, Python does not force my users to adopt them as well. When I expand my focus to include more complexity, I get to make decisions that preserve my users’ need to know.

> For example, my users know that calling something returns a value, and that returned values have attributes or methods. Whether the callable is a function or a class is irrelevant to them in Python. But compare with most other languages, where they would have to change their syntax if I changed a function into a class.

Going another level up, you get crazy stuff: "metaclasses, object factories, decorator implementations, slots, ... allow a developer to fundamentally rewrite how the language works." The knowledge needed to use these is much lower than the knowledge needed to create these, but the latter isn't hidden in any way.

> By actively helping library developers write complex code that is not complex to use, Python has been able to build an amazing ecosystem. And that amazing ecosystem is driving the popularity of the language.

This article is absolutely consistent with my experience, and it helps me to better understand why I like Python so much.


## Other articles 
I read [The Amazon Premium](http://calpaterson.com/amazon-premium.html) by Cal Paterson, and the tl;dr was that big tech providers charge a considerable premium for their cloud services.

[The Largest Contentful Paint Metric](https://calendar.perfplanet.com/2019/developing-the-largest-contentful-paint-metric/) by Annie Sullivan, on the Google Chrome team, is a new metric in Chrome 77 for measuring when the largest meaningful, visible paint on a website occurs. The article walks through how the metric was developed and how it compares to other current metrics.

[Don't Use Booleans](https://www.luu.io/posts/dont-use-booleans/) by Steven Luu discusses how *generally*, "the use of enums is often a better choice compared to booleans." The tl;dr is that `fetch(account_id, False, True, True)` is unreadable, and `fetch(account_id, ItemStatus.Disabled, FetchOptions.History, FetchOptions.Details)` is immediately understandable. You also get the benefit of static type checking so that you avoid flipping the order of arguments. This is a reasonable take, especially when flags start proliferating.

