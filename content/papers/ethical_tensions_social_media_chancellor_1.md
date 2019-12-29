<!-- date: 2019-11-24 -->
# Paper: A Taxonomy of Ethical Tensions in Inferring Mental Health States from Social Media (part 1/2)
Authors: Stevie Chancellor, Michael Birnbaum, Eric Caine, Vince Silenzio, and Munmun De Choudhury.

**Link**: [Stevie Chancellor's website](http://steviechancellor.com/wp-content/uploads/2019/03/taxonomy-prediction-mh-fat2019.pdf) (ACM FAT* 2019)

**How I found this paper**: my sister is taking a class with the lead author next quarter, so I looked them up and found a ton of interesting papers! I'll be posting about several more in the next few weeks.

This is part 1 of this write-up; the paper isn't long, but my "summary" of it certainly is! I wanted to make sure I gave it appropriate attention. View part 2 [here](ethical_tensions_social_media_chancellor_2.md).

## Summary
From the abstract: "Recent research has successfully employed social media data to predict mental health states of individuals ... These algorithmic inferences hold great potential in supporting early detection and treatment of mental disorders and in the design of interventions. At the same time, the outcomes of this research can pose great risks to individuals, such as issues of **incorrect, opaque algorithmic predictions, involvement of bad or unaccountable actors, and potential biases from intentional or inadvertent misuse of insights." In other words, it's possible to infer mental health states from social media; but there are a lot of potential issues with this, and (surprise!) research has not explored this yet.

Research has shown lately that it's possible to infer with high accuracy whether one might be suffering from major depression, postpartum depression, PTSD, schizophrenia, and suicidality. But there are no ethics boards for managing social media research, and this inference raises questions about consent and vulnerable populations online. The lack of methodological consistency can amplify stereotypes or discrimination, intentionally or not. This paper attempts to address these concerns by presenting **"a first taxonomy of issues in algorithmic prediction of mental health status on social media"**.

### The state of the art, and insights from ethics research
In 2013, De Choudhury et al. (one of the paper's authors) used "clinically validated depression measures" to predict depression with 70% accuracy on Twitter (isn't this an imbalanced dataset? Why accuracy?). Following that, others did the same on other social media platforms (Facebook, Sina Weibo, Instagram, Tumblr, and Reddit), in other languages and cultural contexts, and with different mental disorders. Other data sources, like sensor data, exist now too.

Many of these papers include explicit notes about ethical or methodological tensions in this kind of work. However, there are no accepted guidelines or standards for this work, and decisions that are omitted from papers are invisible. "Discussions of consent, validity, underlying bias from data collection techniques, or machine learning model selection is very limited, even though applying algorithms in practical scenarios features prominently as an end goal of this research." The rest of the paper described the various tensions and then calls to action.

### Participants and research oversight
**The unclear role of ethics committees:** analysis of public social media data is often exempt from ethics committees because (1) the studies are observational and (2) the data is (at the time of collection) public, so an argument can be made that this is no different than data available through the census or in courthouses. But should it be exempt? One could reasonably argue that this borders on medical diagnosis, and mental health is a complex and potentially isolating topic. Ethics boards have no clear way of handling this kind of research.

**Consent at scale**: obtaining individual consent at scale is practically impossible, and once your studies go from observational to experimental, things get really murky. People are also generally unaware that their public content could be used by researchers. Whose responsibility is it to inform them of this?

**Vulnerable populations and risk**: vulnerable populations have additional protections under the US IRB. How do we treat them differently (e.g., in eating disorders research, when a large number of those affected are minors)? In traditional studies with interventions, there are always safeguards in place for when the harms outweigh the benefits; social media research lacks these. In observational studies, the *knowledge* that researchers are observing behavior may upset people. Moreover, when people "drop out" of traditional studies, there are protocols for how to handle this; when people "drop out" of social media, it could mean anything from making a new account to moving to a different platform to being at risk for suicide.

**Contextual integrity of communities**: it's unclear if people realize their public communities can be surveilled. Are researchers violating the norms of these communities by studying them? It's feasible to ask community leaders for permission on some platforms, like Reddit or Facebook groups, but not others like Twitter.

### Validity, interpretability, and methods
**Construct validity**: there are very clear standards for making accurate psychiatric diagnoses; see the DSM, the patient health questionnaire, or the GAD-7 scale for anxiety. How do we integrate these into social media models? How should we gather "ground truth" labels (training data) for these models--from self-disclosure, specific hashtags, community participation, actual clinicians? Are we measuring the phenomena that we think we are? Must we involve clinicians to assess ground truth?

**Data bias**: all of these studies are biased to those who use social media (younger and more technologically literate than the average person). If a study uses (as many do) self-diagnoses ("I was diagnosed with XXX"), the sampling is becomes biased towards people who have (likely) sought professional treatment (and therefore have the means to do so) and people who are comfortable disclosing their mental health status to others. What does this mean for people who don't have the means to seek professional help, or those who are newly diagnosed and not comfortable sharing? How do these studies (fail to) account for those people?

**Algorithmic interpretability**: my favorite! Deep learning is the SOTA here, but it doesn't produce interpretable features. This can lead to biased conclusions, poor accountability, or an inability to correct failing algorithms. These models can also challenge human interpretability; what happens when results don't align with a clinically-grounded understanding of mental health? Are the insights new signs of mental illness, or are they red herrings? Also, mental health is a continuum, and SOTA models are not yet able to understand the subtleties of this.

**Performance tradeoffs**: false positives can be stigmatizing and embarrassing, cause undue stress, or overburden stakeholders (in the case of content moderation). False negatives can mean that one's mental health status goes untreated, raising questions about responsibility and accountability. What should these algorithms prioritize? If they miss someone, who is responsible for not intervening?

**Data sharing and protection**: scientists share data for reproducibility, but rarely are these datasets cleaned of deleted or removed data. How can we share data while protecting participants? What does a benchmark dataset even look like? If examples are used in papers, how do we ensure those individuals cannot be identified?

### Implications for stakeholders
**Emotional vulnerability**: computer science researchers aren't trained to manage complex emotions in vulnerable populations, and also manage their own emotions when dealing with sensitive or emotionally burdening data. How do we do that?

**Skillset mismatches**: interdisciplinary work is hard. Algorithms might not be interpretable to computer scientists, leave alone outsiders. CS researchers lack training in the skills clinicians possess. What happens if a clinician suggests removing a highly predictive feature because it's not relevant to predicting depression? How do we navigate interdisciplinary partnerships?

**Role of the clinician**: clinicians are bound by a "duty to treat" in their work. Do they have this duty after annotating a dataset for suicide risk? One might reasonably argue no, because they don't have a patient / physician relationship. But what about a "duty to rescue," where a bystander should help someone in peril? Does this apply here? Who has this duty, if they see a Facebook post that says someone will harm themselves? Additionally, if insights from this kind of work is given to clinicians to help, how do we design systems and interfaces that do this effectively while respecting patients and not overburdening clinicians?

**Designing interventions**: this is the most mentioned application of this work, but this is plagued with ethical questions. If we detect someone might be suicidal, do we alert experts? Their family? What if an abusive family is the reason? Furthermore, if we alert individuals of their own inferred mental health status, are we doing more harm than good?

**Bad actors and fairness / discrimination**: what happens if one of these tools falls into the hands of a bad actor, and it's used to harass someone who is vulnerable? What if health insurance agencies use this to raise premiums for those who are inferred to have a mental illness? Moreover, previous research has found that these oversample affluent white women, which could make generalizability challenging. What impact does this have on predicting for people who don't use social media (lower income people, older people)?




