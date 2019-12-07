<!-- date: 2019-12-06 -->
# What I read this week
I am considering posting regularly about other things I'm reading, particularly blog posts and articles. I don't think individual blog posts deserve their own summary, so I'll write a quick paragraph or two about interesting articles I find.

## [A comment is an invitation for refactoring](https://blog.pragmaticengineer.com/a-comment-is-an-invitation-for-refactoring)
**Author:** Gergely Orosz

**How I found this**: from [Pointer](http://www.pointer.io/)

This post re-examined Uncle Bob's often-quoted advice "a comment is an apology." The premise of the post was that a comment is an invitation to refactor the code in a way that makes the comment unnecessary. Put another way, "*most* inline comments can be eliminated by refactoring the code itself." The three examples they cited were comments for (1) methods that are too long, (2) saying that code fixes a particular bug, and (3) temporarily commented out code. Each of these cases, the author argues, could be refactored (or in (3), deleted) to make the purpose of the code more clear. 

A related quote from Jeff Atwood at the end of the article:

> If your feel your code is too complex to understand without comments, your code is probably just bad. Rewrite it until it doesn't need comments anymore. If, at the end of that effort, you still feel comments are necessary, then by all means, add comments. Carefully.

I'm not really sure how much this applies to modeling code. Methodology comments are a huge part of my codebase, and eliminating them would make my code substantially less clear. At that point, it would be akin to a bunch of equations without motivation or justification.

