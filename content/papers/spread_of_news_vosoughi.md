<!-- date: 2019-12-12 -->
# Paper: The spread of true and false news online
Authors: Soroush Vosoughi, Deb Roy, Sinan Aral

Link: [Science website](https://science.sciencemag.org/content/359/6380/1146)

How I found this paper: from the Atlantic article, [*The grim conclusions of the largest ever study on fake news*](https://www.theatlantic.com/technology/archive/2018/03/largest-study-ever-fake-news-mit-twitter/555104/). This is the original paper.

## Summary
From the abstract: "we investigated the differential diffusion of all the verified true and false news stories distributed on Twitter from 2006 to 2017 ... falsehood diffused significantly **farther, faster, deeper, and more broadly than the truth in all categories of information**, and the effects were more pronounced for false political news than for false news about [a list of other things]." Also, this wasn't due to bots.

Some context for the paper:

 * previous work studied the spread of single rumors, developed theoretical models for rumor diffusion, or designed interventions. But none studied the differences between true and false rumors, and none operated at such a large scale.
 * the authors adopt a very broad definition of "news" as "any asserted claim made on Twitter"
 * they were particularly interested in "rumor cascades" which are basically (1) someone making an assertion in a tweet and (2) the subsequent retweets of the rumor.

The authors studied a dataset of 126,000 rumor cascades spread by 3M people 4.5M times. The rumors were evaluated for truthiness according to six independent fact-checking organizations (e.g., Snopes, Politifact). They quantified the cascades' depth (# of unique retweets over time), size (# of users involved in the cascade), breadth (max number of users involved at any depth) and virality (a measure where the extremes are one large broadcast and many individuals sharing the same thing).

The conclusions are worrying:

 * "falsehood diffused significantly farther, faster, deeper, and more broadly" in all categories of information.
 * more false cascades exceeded a depth of 10, and the top 0.01% of false cascades had a depth 8 longer than truth
 * truth never diffused beyond a depth of 10
 * truth rarely diffused to more than 1K people, but the top 1% of false cascades regularly reached between 1K and 100K
 * it took the truth 6x as long as falsehood to reach 1500 people
 * falsehood was retweeted by more unique users than truth at every level of depth

It gets worse. Users who spread false news had fewer followers, followed fewer people, were less active on Twitter, were verified less often, and had been on Twitter for less time. Falsehood spread so well in spite of the truth having every possible structural advantage.

A possible explanation: novelty attracts attention. The authors studied this by fitting a Latent Dirichlet Allocation model to 10M tweets, which generated a probability distribution over 200 topics, and they were able to compare the topics of the rumor tweets with the topics of the tweets that the rumor-spreaders had seen in the 60 days prior. The false rumors were more novel than the truth.

The authors then studied users' perceptions of information in true and false rumors by comparing the emotional content of the replies. They used the NRC lexicon to create emotion weight vectors, finding that false rumors inspired greater surprise, and truth inspired sadness, anticipation, joy, and trust. 

They used still more diagnostics:

 * because there were multiple cascades for every rumor, the variance and errors associated with the cascades for each rumor were correlated. They specified cluster-robust errors and refit their models, but found that none of their conclusions changed.
 * there may have been selection bias from the fact-checking organizations. The authors recruited some undergrads to independently gather and annotate other rumors, and the results held up on this dataset.
 * bots may have skewed the results. In the main analysis, the authors algorithmically removed bot activity, but adding it back didn't change any conclusions either. This held up when using a second bot-detection algorithm, when removing tweet cascades starting by bots, and when removing human retweets of bot tweets.

**The takeaway**: fake news spreads faster than the truth on Twitter, no matter how you look at it. We are doomed.

## Thoughts, connections, and questions
It's crazy that this paper came out in March 2018 and this is the first large-scale study of its kind; not because research was slow, but rather that no one thought to study this until a year and a half ago. Given how much blame we place on false information on social media for things like the 2016 election, it's astounding that either people didn't see it coming at all or they didn't think it was a large problem. The authors point out that previous work analysed the spread of single rumors, but none compared true and false information, and none operated at such a large scale.

I also don't think I've ever seen a paper whose conclusions are so one-sided. Many papers I read have a narrow scope and have many qualifiers on their conclusions ("in certain conditions, X is true"). There is zero ambiguity in the conclusions of this paper, and all of the assertions about true vs. false rumor cascades support the same result. 

The use of LDA is interesting, and not something I had seen in the summary that I read. LDA is a pretty standard example used in Bayesian inference, so I've heard about it a lot lately even though I'm not doing any work related to it. This is a perhaps surprising application of it (the focus of this paper is not topic modeling), but it helped support the findings by validating the explanation that false rumors are novel. Likewise, the application of a simple sentiment analysis model (8-vector of emotion weights) helped to support their findings from yet another angle.

I'm curious to know how the authors got all of this data. Searching for historical data on Twitter is challenging, and I wonder if they were able to get it from Twitter directly. This is relevant to the column I read earlier today, which asserted that biased algorithms are easier to fix than biased people, but was criticized for understating the difficulty in getting access to these algorithms. The same is true of data.

To me, this seems like one of the most important research areas in HCI going forward. False information is anecdotally a huge problem online, and it's come to the point where *facts* are politicized (climate change, vaccines). Understanding how this information spreads and designing interventions for it is critical.
