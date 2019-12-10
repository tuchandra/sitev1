<!-- date: 2019-12-10 -->
# Features I would like to add to my SSG
I [wrote](https://tusharc.dev/site/about_website.html) about my SSG and how I built this website back in April. Over time, I've started to realize that some of the features I stripped out may actually be useful. This post is a wishlist of features that I would like to add over time.

**Choosing which pages to render**: running `python makesite.py` renders the entire site, but rarely (never) do I want to regenerate every page. Instead, I write posts one at a time, and I would like to be able to specify a filename to render individually, so I can run `python makesite.py <file.md>`.

**Generating the index automatically**: right now, I have to manually add links to pages to my homepage. But the homepage only consists of the header and links to all my posts, in reverse chronological order, so I should be able to generate it automatically and always have it be up to date. I think this was included in the upstream SSG script that I forked, and I got rid of it, so oops.

**Paginate the index**: likewise, the index is currently a list of every post I've made, and I expect this to get unwieldy at some point. Paginating this automatically would be great.

**Add the ability to ignore drafts**: it's often the case that I start a post but don't finish it, and before I finish that post I'll finish another. I'd like to be able to denote posts as being "drafts" that shouldn't be rendered, and commit the Markdown source but not a rendered HTML file.

**Add LaTeX support**: when summarizing a [paper](https://tusharc.dev/site/papers/bayesian_multilevel_estimation_gelman.html) by Gelman, I really wanted to be able to write LaTeX and have it render within the HTML. This is definitely a desired feature as I likely continue reading more mathematical papers.

**Add tags to posts**: being able to tag posts as "paper summary," "talk notes," "personal," "career," etc. would be nice. Adding a filtering feature would be a bonus on top of this.

**Creating templates for posts**: creating a "paper summary" template for when I have repeated fields (authors, how I found the paper, summary, thoughts) would save a lot of time. Even creating a template for normal posts would save time.

After writing this wishlist, I'm left with the question of whether I should write this all myself or defer to a standard SSG, like Hugo. On one hand, other people have solved the problem of "making a personal site and blog" several times; on the other, writing the solution(s) myself can be instructive and make me a better engineer. That's also a question of how much flexibility I'm willing to sacrifice and how much additional bloat I'm willing to accept (by using an existing SSG) compared to how much effort I'm willing to save and how much time I would like to spend on this (by rolling it myself).