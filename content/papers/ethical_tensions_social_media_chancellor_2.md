<!-- date: 2019-11-25 -->
# Paper: A Taxonomy of Ethical Tensions in Inferring Mental Health States from Social Media (part 1/2)
Authors: Stevie Chancellor, Michael Birnbaum, Eric Caine, Vince Silenzio, and Munmun De Choudhury.

**Link**: [Stevie Chancellor's website](http://steviechancellor.com/wp-content/uploads/2019/03/taxonomy-prediction-mh-fat2019.pdf) (ACM FAT* 2019)

**This is part 2 of this write-up. See the previous part [here](ethical_tensions_social_media_chancellor_1.md).**

## Calls to action
Research in this space "will continue to grow, with new algorithms, data collection means, and new implications for practical use of these algorithms." The authors call the community to begin work on these issues.

**Participatory algorithmic design**: "researchers should include key stakeholders in the research process, including clinicians, social networks, and individuals who are the object of these predictions." Interdiscplinary seminars and workshops are increasing in number, but more generally CS practiioners should seek out clinicians and domain experts for this work. Platform owners and ethicists can help to tackle issues of bias, fairness, and privacy. They also suggest that those who are the targets of predictions are considered and involved through focus groups, interviews, or other human-centric design strategies.

**Developing best practices for methods**: "researchers should disclose study design and methods decisions to promote reproducibility, and the field should agree on what best practices are." This requires identifying gaps through meta-analyses and literature reviews (this is part of why this paper exists), and more generally speaking researchers should be more transparent about recruitment, methodology, and design.

**Beyond ethics boards**: "consider and discuss the implications of this research, outside of the normal considerations of ethics committees. Incorporate ethics as a key value in the research process from the beginning." Human-centered research dictates that these predictions are on *people's data*, not on abstract "data." Researchers should consider and disclose potential for benefit and harm themselves, rather than relying on (often insufficient) ethics boards.


**The takeaway**: social media offers many new ways of inferring people's mental states, but there are a host of ethical issue with this. This paper creates a taxonomy of some of these. Generally speaking, ethical considerations need to be at the forefront of the research process, and an interdisciplinary approach blending data science and clinical expertise is necessary.


## Thoughts, connections, and questions
I loved how this paper was organized. They organized all of their proposed tensions clear, and I particularly appreciated how the paper posed dozens of questions without attempting to answer them. There are no easy answers when someone's well-being is on the line.

A question I've been thinking about lately: lots of technologies can be used for good and evil. One unrelated example is OpenAI's GPT-2, which could be used for very convincing synthetic text generation, for better or for worse. But, from the paper, an open source tool to infer mental states from Twitter could help design interventions, but it could also open the door to harassers targeting those who are most vulnerable. The authors bring this up when they ask "do these algorithms only help the proverbial 'rich get richer' by predicting mental health status on those already likely to seek treatment?", and this is perhaps the most important question of the paper.

I don't have an answer to this yet. I think software is different because of how much more accessible it is (getting code from Github running compared to, say, synthesizing a newly discovered dangerous chemical). We also have to be careful with the question of who software gives more power to, and who it takes power away from. Does something that infers mental health states actually help the mentally ill, or does it make them less powerful by making it easier for bad actors to take advantage of them?

The questions of consent are also interesting here. If Facebook designs an intervention for individuals that they infer as high risk for suicide, they certainly wouldn't roll it out to everyone at once. But A/B testing this is equivalent to conducting psychological research on (high-risk!) human subjects--while I'd love to give credit to Facebook and [assume that they're at least thinking about this](https://xkcd.com/1390/), there's no chance that it stands up to an actual university's ethics board.

How much responsibility falls onto platform designers for disclosing that people's data can be (or has been) used in a study? Is it their responsibility to ensure that people are aware that their "data" (posts, profiles, etc.) are public? How much does this differ by platform? I believe that Facebook could, for instance, do more in this area; but it's shocking that anyone wouldn't realize that everything on Reddit is public. And to what extent should researchers disclose that people's posts have been used as part of a study? How should they disclose this, if at all?