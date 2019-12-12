<!-- date: 2019-12-14 -->
# What I read this week
Similar to last week, here are summaries of blog posts, articles, or news that I read this week.

## [The grim conclusions of the largest-ever study of fake news](https://www.theatlantic.com/technology/archive/2018/03/largest-study-ever-fake-news-mit-twitter/555104/)
**Author:** Robinson Meyer

**How I found this**: ?

This is an article summarizing a research paper, [The spread of true and false news online](http://science.sciencemag.org/cgi/doi/10.1126/science.aap9559), by Vosoughi, Roy, and Aral in *Science* (that paper is on my list!). This study analyzed "every major contested news study" across Twitter, coming out to ~126K stories and 3M users over 10 years. The project was inspired by the Boston Marathon bombings in 2013, as the MIT researchers were confined to their own homes for days as the police searched for the suspects, hindered by a great deal of false information on Twitter (and [Reddit](https://www.theatlantic.com/national/archive/2013/04/reddit-find-boston-bombers-founder-interview/315987/)). Following that, the researchers started studying how false information moved across Twitter. Its conclusions were grim: "fake news" reaches more people, penetrates deeper into social networks, and spreads much faster than accurate stories. 

Fake news reached a larger audience (more total retweets) *and* propagated deeper into networks (longer average length of the retweet chains "A retweeted B retweeted C ..."). They identified two possible reasons: fake news seemed more "novel," and that it evoked more emotion than the average tweet. This was true even in spite of the fact that users who shared accurate information had been on Twitter longer, were more likely to be verified, and had more followers—in other words, they had *every structural advantage possible*, and the truth still lost. Another key finding was that Twitter bots amplified true stories as much as false ones, so they're not to blame either.

> In short, social media seems to systematically amplify falsehood at the expense of the truth, and no one—neither experts nor politicians nor tech companies—knows how to reverse that trend. It is a dangerous moment for any system of government premised on a common public reality.

**My commentary**: the last bit (evoking more emotion) is one of the most worrisome problems in social media. The fact that platforms optimize for engagement, and engagement is often facilitated by outrage, speaks to the danger of social media. The amount of influence that they have over people's information consumption is even more worrisome. And it only seems to be getting worse, especially as our lawmakers seem increasingly technologically inept, the platforms continue to grow, and false information continues to provoke outrage.

## [No, AI is not for social good](https://venturebeat.com/2019/11/23/no-ai-is-not-for-social-good/)
**Author**: Jared Moore

**How I found this**: from the newsletter [Skynet Today](https://www.skynettoday.com/)

This article is essentially a critique of the idea of "AI for social good," commonly tossed around as an application of advances in AI. One particular quote stands out:

> Likewise, the promise of “AI for the good” ignores the fact that problems like poverty, recidivism, and the distribution of resources are political ones; they’re often the results of institutional failure. Technologies, when not aimed at the root of problems, divert our attention. On top of that, do we really want to leave big tech to “solve” these social problems when it has shown it’s capable of creating substantial social problems of its own — I’m thinking here of Facebook with its Cambridge Analytica deal, for example.

Put otherwise, technology cannot be used to solve complex social problems (see [xkcd](https://xkcd.com/1831/)). Moreover, it's not unlikely that it's currently *creating* more complex social problems than it's solving. A great deal of "AI for social good" commentary is "AI to [try to] solve [as of yet unsolvable] social issues," like policing, terrorism, healthcare, or content moderation. While it certainly offers great promise, taking a technology-first approach to these problems means we're all but certain to ignore, and possibly even amplify, institutional and systemic issues that create these problems in the first place. 

## [https://ux.christmas/2019/11](The UX of APIs)
**Author**: Linda Christin Halvorsen

**How I found this**: from [Pointer](https://pointer.io)

Written by a designer, this article discusses some surprising (to me) aspects of the UX of APIs. The author found that their teams were making APIs that "worked" in that they did their job and provided the necessary functionality ... but they were not at all enjoyable to use.

> The key take-away for me, from the user interviews, was **how important a user centric view was even when developing APIs.** We had developed APIs based on functional specs – API this shall make that possible. And when it was possible – we were done. ... [But] fairly soon, we experienced exactly what you would expect when you don’t pay attention to the user experience of your product or service: our users found our APIs difficult to use.

The author continues with a list of steps their teams took to treat APIs more like products. APIs are part of the delivery, and they're likely the part that developers are *most* responsible for (the author mentioned that they were, as a designer, too far away from the code internals to be able to design an effective one). "Once I started interviewing developers – as good old fashioned user insight – I found different sets of needs, of motivational factors, barriers – and examples and stories of how APIs can delight them, frustrate them, confuse them, and make them want to build more with them."

It's easy to think about "delightful APIs" in the context of my favorite libraries. Most notable is scikit-learn, whose [clear object model](https://scikit-learn.org/stable/modules/classes.html) makes working with the library a breeze. Likewise, I've found PyTorch to be intuitive to work with in large part because of its clear APIs. As consumers of software, we love these well-designed APIs; naturally that means that, when we're writing our own, we need to think about them in the same way.

