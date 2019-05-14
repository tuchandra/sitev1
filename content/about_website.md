<!-- date: 2019-04-29 -->
# How I built this website
You may have noticed that the [Github repo](https://github.com/tuchandra/tuchandra.github.io) for this website has a tagline "... for people who *aren't* web developers." I am a data scientist and certainly fit that description, and so I'm going to talk about how I built this site using the tools I already know.

This website is hosted on Github Pages at tuchandra.github.io. I write posts in Markdown and render them via a 150-line Python script (`python makesite.py`). Since the content and the publishing tools all live in this repo, everything is managed by Git.

Sounds simple, right? It is.

## Motivation
My requirements are simple, and can be boiled down to a website that:
 * has basic, static content like my contact info, my resume, and some blog posts
 * lets me write blog posts in Markdown
 * uses minimal styling to make everything look nice
 * does not use JavaScript at all

In short, I don't need anything fancy. Notably, I also want my toolchain to have a similar degree of simplicity.

This post isn't about setting up a Github Pages site, or about hooking up your domain name to it. I followed some tutorial a month ago, and while I don't remember the exact one, [any](https://dev.to/trentyang/how-to-setup-google-domain-for-github-pages-1p58) [of](https://hackernoon.com/use-custom-domain-with-github-pages-2-straightforward-steps-cf561eee244f) [these](https://medium.com/employbl/launch-a-website-with-a-custom-url-using-github-pages-and-google-domains-3dd8d90cc33b) should probably work.

## Static site generators
Like any programmer, I started by Googling for solutions that did what I wanted. The term "static site generator" captured what I wanted, and I came across common ones like [Jekyll](https://jekyllrb.com/), [Gatsby](https://www.gatsbyjs.org/), or [Hugo](https://gohugo.io/). These were seriously impressive, offering things like:
 * easy installation via NPM
 * joining data sources using GraphQL
 * hundreds of themes
 * powerful templating syntax

... and I didn't need any of it.

I don't want to manage an NPM installation on the Chromebook from which I'm writing this. I don't even *know* React, and though my roommate loves it, I am certain that I don't need to learn it just to build this simple website. And the idea of a [static site generator rendering pages entirely in JavaScript](https://old.reddit.com/r/programming/comments/adbu86/why_medium_is_no_longer_the_goto_platform_for/edfyuj4/?context=2) still sounds like an oxymoron to me -- again, nothing on my site needs JS.

Please do note that I'm not trying to hate on these technologies -- rather the opposite. I know that React is incredibly powerful, and that much of the modern web is built in it, and that it can do almost anything. These are exactly the reasons why I *don't* want it. Using a powerful SSG would introduce unnecessary complexity to this process, and I am a firm believer in not overengineering. My requirements are minimal and well-defined, so there's no reason my toolchain can't be.

## Another approach: makesite.py
After static site generators seemed to be overkill, I started searching for more basic solutions. One stuck out: makesite.py ([Github link](https://github.com/sunainapai/makesite)), which described itself as a "simple, lightweight, and magic-free static site/blog generator for Python coders." I know Python well, and this seemed easy enough to understand. Great!

This turned out to be awesome: write in Markdown, run the script, have it all render as HTML. It sounded dead simple, and yet I still didn't need everything that this offered me. But I figured that this was as simple as I was going to find online, so I dove into the code and started stripping things down myself. Let's walk through some of the changes that I made:
 * removed everything to do with RSS feeds, three custom layouts, and date parsing
 * removed optional config from a `params.json` file, since I can just specify parameters in code
 * added code to get the title of a Markdown file as the first top-level heading, since otherwise you had to specify it with a redundant `<!-- title: Name of Post -->` comment
 * added code to replace links to Markdown pages with links to their generated HTML pages, since otherwise you get broken links
 * removed the try/except logic surrounding the optional commonmark dependency, since I definitely need it

I also used some newer features of Python that I encourage everyone to check out:
 * [Pathlib](https://docs.python.org/3/library/pathlib.html), because it's great to be able to distinguish between strings and paths
 * [type hints](https://www.python.org/dev/peps/pep-0484/) in my function signatures and a [mypy](http://mypy-lang.org/) to catch bugs ahead of time
 * [Poetry](https://github.com/sdispater/poetry/) for environment management, since I like it better than basic virtualenvs or pipenv, and I don't have conda on my Chromebook

Finally, I cleaned up the main function `make_pages` to be considerably simpler. I wanted to throw everything into a `content/` directory and have my generated site retain that structure, so I wrote a straightforward recursion to take care of it for me.

### sakura.css - minimal, classless CSS
I came across [sakura.css](https://github.com/oxalorg/sakura), which described itself as a "minimal classless CSS theme." In theory, you drop it in your folder, include it in your HTML files, and everything magically gets prettier. In practice, that's exactly what happened; I added the file to my `static` folder and updated the template, and that was it.

My site uses a slightly modified version of this file -- I used a sans-serif font, made the headings smaller, and changed some of the colors (still a work in progress). CSS is one of the things that I appreciate and respect, but, as a data scientist, also dread working with. Having a single, easy to modify file made applying a theme to my site painless.

### Workflow
The entire `makesite.py` script is just over 150 lines of code, including comments and whitespace, and it handles my use case flawlessly. See the script [here](https://github.com/tuchandra/tuchandra.github.io/blob/master/makesite.py).

I can write my blog posts in Markdown -- see the [source of this page](https://github.com/tuchandra/tuchandra.github.io/blob/master/content/about_website.md) for an example -- and then type `poetry run python makesite.py` to generate the `site/` directory. Note that because Github Pages hosts the entire repo, the rendered website actually lives at tusharc.dev/site; to get around this, [index.html](https://github.com/tuchandra/tuchandra.github.io/blob/master/index.html) in my home directory just redirects to that page.

## Wrapping up
This post describes how I wrote my own minimal website by using an equally minimal set of tools. While I'm still working on adding content to my website, it feels great knowing that I can write in Markdown, run a Python script, and have everything *just work*.

For the Python programmer out there who has no experience with the web, I promise that it's not all NPM hell and React apps -- you can build your own nice-looking site with the tools you already know!
