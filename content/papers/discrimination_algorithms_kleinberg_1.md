<!-- date: 2019-12-29 -->
# Paper: Discrimination in the Age of Algorithms (1/2)
Authors: Jon Kleinberg, Jens Ludwig, Sendhil Mullainathan, Cass R Sunstein

Link: [Journal of Legal Analysis](https://academic.oup.com/jla/article/doi/10.1093/jla/laz001/5476086) (yeah, this was published in a law journal, we'll see how reading this goes)

How I found this paper: from the NYT article, [biased algorithms are easier to fix than biased people](https://www.nytimes.com/2019/12/06/business/algorithm-bias-fix.html)

This is part 1/2; view part 2 [here](discrimination_algorithms_kleinberg_2.md).

## Summary
From the abstract (bolded emphasis mine):

> To understand how algorithms affect discrimination, we must understand how they affect the *detection* of discrimination. With the appropriate requirements in place, algorithms create the potential for new forms of transparency and hence opportunities to detect discrimination that are otherwise unavailable. The specificity of algorithms also makes transparent tradeoffs among competing values. This implies **algorithms are not only a threat to be regulated; with the right safeguards, they can be a potential positive force for equity.**

The central claim of the paper is that "when algorithms are involved, proving discrimination will be easier—or at least it should be, and can be made to be." Regulating the design of algorithms with detailed record-keeping requirements, the authors claim, could provide transparency about the decisions being made. Opaque algorithms do not prevent regulators from studying their construction or behavior, which are both impossible with humans. Crucially, though, this requires that all components of the algorithm be stored, including training data.

The authors state that "a well-regulated process involving algorithms stands out for its *transparency* and *specificity*", in contrast to humans who often do not know why they make the decisions that they do. In other words, answering the questions "on what basis are they choosing" and "why did they pick those factors"—two important questions when evaluating humans for discrimination—are much more feasible with algorithms. The authors make clear that "algorithmic" does not mean "objective," and to conflate the two is dangerous.

Consider a hypothetical, summarized from the paper: a company is accused of gender discrimination in hiring. A plaintiff argues that they have more education than male candidates who were hired, but the company argues that they value work experience as well, of which the plaintiff has less. The plaintiff argues that work experience is cited after the fact ... this goes back and forth, and the point is that it's difficult to know whether or not the company has discriminated based on gender. But "in a well-regulated world with algorithms," one could ask for the screening and training algorithms and the training data, experts could use counterfactuals to statistically evaluate how different applicants are treated, and look for signs of disparate impact.

## Five critical points
The authors make five points, which they develop in detail throughout the paper. I summarize them here.

**1:** "The challenge of regulating discrimination is fundamentally one of attribution": that is, when we observe disparity for a particular group, how do we explain that gap? It could be because the algorithm explicitly takes into account gender. It could be because of average differences in the training data. It could be because there's a proxy for race in a feature.

**2**: "This decomposition becomes easier once an algorithm is in the decision loop." The decisions studied become more specific than why an algorithm decided X; they now include why a particular objective was used (minimize MSE, predict salespeople with the highest revenue, maximize tenure at a company, etc.). This knowledge increases the amount of scrutiny that can be given to these decisions.

**3**: "If we regulate the human choices well, we might be willing to be more permissive towards how the algorithm uses information about personal attributes in certain ways." In some cases, the best way to mitigate the impact of biased data is to incorporate that data into algorithms, so that they can correct for these factors. This point was less clear to me.

**4**: "Algorithms will force us to make more explicit judgments about underlying principles." If there is a tradeoff between the desires to admit more minority students into a college and to maximize first year GPAs, the algorithms can quantify this tradeoff, and decision makers and regulators can decide what tradeoffs are acceptable.

**5**: "If appropriate regulation can protect against malfeasance in their deployment, then algorithms can become a potentially powerful force for good: they can dramatically reduce discrimination of multiple kinds." Implicit biases matter most inn an unstructured decision-making process; while algorithms will certainly have human biases in their e.g., objectives and data, they will reduce human bias present in an ambiguous decision process.


## Summary, continued
The remainder of the 40+ page paper goes into detail about the legal ideas around discrimination (disparate treatment, disparate impact, and fair treatment), challenges with detecting discrimination (individual decisions being hard to explain, the inability to simulate counterfactuals, etc.), and other relevant legal perspectives surrounding these concepts.

The authors take care to discriminate between the *screener* (the algorithm that takes inputs and produces a decision) and the *trainer* (the algorithm that produces the screener). They argue that the distinction between the two is often overlooked, but important in practice. One common concern about algorithms "doing literally anything" can be assuaged when considering that the screener is constrained by the trainer, so given an appropriate trainer we need not worry about this.

The proposed framework is "relevant to the situations where the training algorithm, screening algorithm, and training dataset are all fixed, stored objects that can be inspected." Importantly, this is not the case for e.g., online ad placement, where the algorithms used change rapidly and data flows in quickly. The authors are more concerned with "micro-prediction" tasks that typically affect an individual, like hiring.

The authors discuss where discrimination is and is not likely to arise in algorithmic decision making systems. It can easily arise in the choice of outcome, choice of features, and choice of training procedure (e.g., by using biased data, or more generally by using data that reflects past, biased, human decisions). It is unlikely to arise in choosing which features are used in the selection process (that happens statistically), in the screening algorithm (which is a mechanical result of a training algorithm given data, so discrimination in the screener must come from discrimination earlier in the pipeline), and by systematic differences across groups (which are not, by themselves, discriminatory in the legal sense).

They present four case studies of firms making hiring decisions then evaluate them from a legal perspective. Following that, they discuss how they would and would not be different given the use of algorithms to inform hiring. I don't have the legal background to make very many comments about this, but the theme appears to be that (when properly regulated and documented) there are different questions to be asked like what kinds of proof are necessary and what tradeoffs were made.


