<!-- date: 2019-12-30 -->
# Paper: Discrimination in the Age of Algorithms (2/2)
Authors: Jon Kleinberg, Jens Ludwig, Sendhil Mullainathan, Cass R Sunstein

Link: [Journal of Legal Analysis](https://academic.oup.com/jla/article/doi/10.1093/jla/laz001/5476086) (yeah, this was published in a law journal, we'll see how reading this goes)

How I found this paper: from the NYT article, [biased algorithms are easier to fix than biased people](https://www.nytimes.com/2019/12/06/business/algorithm-bias-fix.html)

This is part 2/2; view part 1 [here](discrimination_algorithms_kleinberg_1.md).

## Regulation of algorithms
Regulation of algorithms, the authors posit, requires us to be able to understand human choices on (1) the outcome to predict, (2) the inputs available to the algorithm for consideration, and (3) the training procedure used. Transparency is therefore necessary to the process; fortunately, the use of algorithms makes it more feasible and productive compared to human decision making. It's unclear what kinds of record keeping requirements would need to be passed, and the authors make several suggestions.

The authors claim early on, then prove in the Appendix, that algorithmic bias can be completely decomposed into bias from those three factors (the choice of outcome, the choice of input variables, and the design of the training procedure). Once those are accounted for, what remains is the structural disadvantage between groups. That's an interesting claim that I haven't been able to totally wrap my head around, and it certainly merits further thought.

> Our central claim ... is that safeguards against the biases of people who build algorithms, rather than against algorithms per se, could play a key role in ensuring that algorithms are not being built in a way that discriminates ... If we do that, then algorithms go beyond merely being a threat to be regulated; they can also be a positive force for social justice.


## Algorithms for equity
"Algorithms have the potential to help us to excise disparate treatment," the authors write, and "to reduce discrimination relative to human decision-making," which they call "disparate benefit" of algorithms. They discuss how algorithms have no hidden agendas; any agendas they have must be specified in code. They mention that, in contrast to humans, access to protected variables *promotes* equity for a properly designed algorithm can promote equity.

The authors consider a controversial example of two college applicants who scored 1100 on the SAT: one who went to school at New Trier and one who went to school in Englewood. Barring extraordinary circumstances, the authors write, "it *cannot* be the case that the amount of effort, persistence, and extra learning on one's own required to score 1100 on the SAT is the same for the student who starts with every possible advantage as for the one forced to overcome a long list of difficult obstacles." Yet a race-blind (and perhaps neighborhood-blind, economic-circumstances-blind, and other-proxies-for-race-blind) algorithm is *precisely* forced to assume that this is the case. They create a mathematical model of this to further demonstrate the point.

Yet another point is that equity improvements may come simply from algorithms being better predictors than humans. Better prediction in tenant risk assessments might allow landlords to relax collateral requirements. Better prediction of missed payment risk might allow lenders to lower interest rates for families who would otherwise have unmanageably high ones. More generally, shrinking systems that otherwise disproportionately harm disadvantaged groups is a major possible outcome of algorithmic decision making.

One final potential benefit is that algorithms can help reveal our own biases. If a hiring algorithm trained on past applicant data ends up hiring mostly men, then an evaluation of this algorithm would reveal biased past behavior. This is likely what happened when Amazon tried to do this.


## Thoughts, connections, and questions
A great quote from the introduction:

> Algorithms do not build themselves. The Achilles' heel of all algorithms is the humans who build them and the choices they make about outcomes, candidate predictors for the algorithm to consider, and the training sample. A critical element of regulating algorithms is regulating humans.

I love this idea. Regulating algorithms independently of the humans that develop them is bound to fail; this is how we end up with senseless blanket bans on technologies or tedious lists of what we can and can't do. I'm influenced by Patrick Hall [discussing](../spark/interpretable_ai.md) how if we (as ML researchers and practitioners) don't learn to regulate ourselves, then the government will likely do so in a draconian fashion. While the suggestions made in this paper are all taken from a legal perspective, perhaps a company could choose to keep this kind of documentation on their own as they build models. This is complementary to [model cards](model_cards_mitchell.md), I think, which IMO focuses more on documentation of a finished model and not of the model buliding process.

The discussion of access to protected variables being able to increase equity is counterintuitive, but seems to make sense. A properly designed algorithm would be able to take those into account. This reminds me of hierarchical models, where you can specify group-level predictors and learn different coefficients for those explicitly. Accounting for these explicitly in a model might allow one to later negate them by "flipping" the value of that predictor (white to black, female to male, etc.), and to understand the impact of that predictor by looking at (in a linear model) the coefficients.

I think a likely underappreciated point (well, I have no idea how much anyone appreciates any point in this paper) is the importance of choosing the right objective function. [Aguera discussed](../posts/talk_kidd_neurips.md) how few problems can be specified in terms of a loss function, and the authors here make clear that the choice of this objective is one of the keys to understanding discrimination in algorithms. A related problem, then, is how we *develop* these objectives for complex problems that don't have any sort of mathematical formulation, and how we do so in a legal and fair way.

Another question (which I haven't thought too much about) is the extent to which this process deals with "black box" algorithms. I suppose that given any training procedure, the objective must be clear (and this paper mandates that it must be documented), and the possible features are readily available. The output of the trainer (the "screener") is easy to evaluate by passing arbitrary inputs through it in order to see how it responds, and if necessary one could take a linear approximation to an otherwise black-box screener.

This paper was great. Reading 40+ pages was challenging, but it was a really interesting read. Seeing the connection between algorithmic bias and the existing legal framework around discrimination was a unique read; to date, I haven't seen any treatment as in-depth as this one. Kleinberg and the other authors did an excellent job at making both complex legal concepts and complex CS concepts accessible to people of either background.
