# How I built this website
You may notice that the [Github repo](https://github.com/tuchandra/tuchandra.github.io) for this website has a tagline "... for people who aren't web developers." I most certainly fit that description, and so I'm going to talk about my very simple website structure.

## Motivation
My requirements were simple; all I *really* needed was a website that I could give to others that had basic things like my contact information, a web version of my resume, and some blog posts. I wanted to be able to write posts in Markdown and have them render as HTML. I wanted minimal styling to make the whole thing look nice. And, whatever tool I chose, I didn't want it to do more than necessary.

## Static site generators
So, like any programmer, I started Googling for solutions. Common **static site generators** like [Jekyll](https://jekyllrb.com/), [Gatsby](https://www.gatsbyjs.org/), or [Hugo](https://gohugo.io/) are seriously impressive. They offer things like:
 * easy installation via NPM
 * being able to pull data from multiple sources
 * hundreds of themes
 * powerful templating syntax
 * and much, much, more

... but I don't need any of it. I didn't want to have to manage an NPM installation on the basic Chromebook from which I'm writing this. I don't even *know* React, and though my roommate loves it, I don't need it to build my simple website. And the idea of a [static site generator rendering pages entirely in JS](https://old.reddit.com/r/programming/comments/adbu86/why_medium_is_no_longer_the_goto_platform_for/edfyuj4/?context=2) sounded like an oxymoron to me -- nothing on my site even needs JS.

Note that I'm not trying to rag on these technologies -- rather the opposite. I know React is super powerful, and that you can do almost anything in it, and that's exactly why I know I don't need it. I am a firm believer in not overengineering, and so throughout this whole progress I intentionally avoided solutions that would be overkill for this simple website.

## Finding puzzle pieces
So I took another approach: what smaller pieces did I need to bring this together?

### sakura.css
I came across [sakura.css](https://github.com/oxalorg/sakura), which described itself as a "minimal classless CSS theme." You just drop it in your folder and include it in your HTML files, and everything magically gets prettier. Perfect!

At the time of writing, I am using a [modified version](https://github.com/tuchandra/tuchandra.github.io/blob/master/static/sakura.css) of sakura.css - I made the headings smaller, used a sans-serif font, and moved the footer a bit lower. The file being so simple allowed me to change this easily!

### makesite.py


