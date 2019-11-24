<!-- date: 2019-11-24 -->
# Paper: A Taxonomy of Ethical Tensions in Inferring Mental Health States from Social Media
Authors: Stevie Chancellor, Michael Birnbaum, Eric Caine, Vince Silenzio, and Munmun De Choudhury.

**Link**: [Stevie Chancellor's website](http://steviechancellor.com/wp-content/uploads/2019/03/taxonomy-prediction-mh-fat2019.pdf) (ACM FAT* 2019)

**How I found this paper**: my sister is taking a class with the lead author next quarter, so I looked them up and found a ton of interesting papers! I'll be posting about several more in the next few weeks.


## Summary
From the abstract: "Recent research has successfully employed social media data to predict mental health states of individuals ... These algorithmic inferences hold great potential in supporting early detection and treatment of mental disorders and in the design of interventions. At the same time, the outcomes of this research can pose great risks to individuals, such as issues of **incorrect, opaque algorithmic predictions, involvement of bad or unaccountable actors, and potential biases from intentional or inadvertent misuse of insights." In other words, it's possible to infer mental health states from social media; but there are a lot of potential issues with this, and (surprise!) research has not explored this yet.

Research has shown lately that it's possible to infer with high accuracy whether one might be suffering from major depression, postpartum depression, PTSD, scizophrenia, and suicidality (collectively referred to as "mental health states"). But there are no ethics boards for managing social media research, and this inference raises questions about consent and vulnerable populations online. The lack of methodological consistency can amplify stereotypes or discrimination, intentionally or not. This paper attempts to address these concerns by presenting **"a first taxonomy of issues in algorithmic prediction of mental health status on social media"**.

### The state of the art, and insights from ethics research
In 2013, De Choudhury et al. (one of the paper's authors) used "clincically validated depression measures" to predict depression with 70% accuracy on Twitter (isn't this an imbalanced dataset? Why accuracy?). Following that, others did the same on other social media platforms (Facebook, Sina Weibo, Instagram, Tumblr, and Reddit), in other languages and cultural contexts, and with different mental disorders. Other data sources, like sensor data, exist now too.

Many of these papers include explicit notes about ethical or methodological tensions in this kind of work. However, there are no accepted guidelines or standards for this work; decisions that are *omitted* from appers are invisible, and raises concern. "Discussions of consent, validity, underlying bias from data collection techniques, or machine learning model selection is very limited, even though applying algorithms in practical scenarios features prominently as an end goal of this research."

The authors briefly summarize existing work in social media research ethics, public health research, and critical data studies. This is all complementary to this wrok, which lies at the intersection of the three. Important concerns include:

 * participant consent and contextual data integrity (what is this?)
 * data protection, anonymization, and privacy
 * methodological rigor
 * bias and validity
 * implications for different stakeholders

### Three areas of tension
**Participants and research oversight**:


**Validity, interpretability, and methods**:


**Implications for stakeholders**:






**The takeaway**: ...

## Thoughts, connections, and questions


A question I've been thinking about lately: lots of technologies can be used for good and evil. An open source tool to infer mental states from Twitter could help design interventions, but it could also open the door to harassers targeting the most vulnerable people. Or OpenAI's GPT-2, which could be used for very convincing synthetic text generation, for better or for worse.

I don't have an answer to this yet. I think software is different because of how much more accessible it is (getting code from Github running compared to, say, synthesizing a newly discovered dangerous chemical). We also have to be careful with the question of who software gives more power to, and who it takes power away from. Does something that infers mental health states actually help the mentally ill, or does it make them less powerful by making it easier for bad actors to take advantage of them?

The questions of consent are also interesting here. If Facebook designs an intervention for individuals that they infer as high risk for suicide, they certainly wouldn't roll it out to everyone at once. But A/B testing this is equivalent to conducting psychological research on (high-risk!) human subjects--while I'd love to give credit to Facebook and [assume that they're at least thinking about this](https://xkcd.com/1390/), there's no chance that it stands up to an actual university's ethics board.

