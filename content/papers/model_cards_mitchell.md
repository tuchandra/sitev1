<!-- date: 2019-11-17 -->
# Paper: Model Cards for Model Reporting
Authors: Margaret Mitchell, Simone Wu, Andrew Zaldivar, Parker Barnes, Lucy Vasserman, Ben Hutchinson, Elena Spitzer, Inioluwa Deborah Raji, Timnit Gebru

Link: [arXiv](https://arxiv.org/abs/1810.03993)

How I found this paper: from a talk at Spark+AI Summit given by Patrick Hall, called [Interpretable AI: not just for regulators](https://databricks.com/session/interpretable-ai-not-just-for-regulators). One of the many papers cited in the talk was this one, as an example of how we can do better when reporting model performance.

## Summary
This paper proposes a framework called "model cards" for reporting not only the performance, but also the limitations and expected usage, of machine learning models. The authors write in the abstract "in order to clarify the intended use case of machine learning models and minimize their usage in contexts for which they are not well suited, we recommend that released models be accompanied by documentation detailing their performance characteristics." There are not really any standards for reporting on machine learning models, and this paper takes a step towards creating those.

Model cards should have the following sections:
 
 * **Model details**: basic housekeeping about who developed the model and when, how it was trained, relevant papers, who to send questions to, etc.
 * **Intended use**: primary intended uses and users, use cases that are out-of-scope (important!). An example is "not for text examples shorter than 100 tokens," where it's easy for people to apply a model to something that they shouldn't.
 * **Factors**: model performance across primarily groups (in an intersectional analysis, which requires thinking about the intended use cases and people it affects), but also instruments (what camera was used for the pictures in a face detection model?) and environment (e.g., lighting). They also suggest talking about forseeable salient factors and why the evaluation factors were chosen.
 * **Metrics**: what measures of performance were chosen and why? What thresholds were used and why?
 * **Evaluation data**: What datasets were used, why were they chosen, and how were they preprocessed? Is the evaluation dataset representative of the intended use cases?
 * **Training data**: basically the same as evaluation data. If the data is proprietary, they recommend discussing distributions over groups or other features.
 * **Quantitative analyses**: Diaggregated metrics over different factors, including how the model performed w.r.t. each factor and an intersectional combination of factors.
 * **Ethical considerations**: Does the model use sensitive data? Is the model intended to inform decisions about human health or safety? What risks might be present and what mitigation strategies were used? Are there use cases that are ethically questionable?
 * **Caveats and recommendations**: anything else not mentioned. Is there further testing required? What recommendations are there for model use?

They cite another paper, [Datasheets for Datasets](https://arxiv.org/abs/1803.09010?context=cs), which shares the author Timnit Gebru, as a complement to (and possibly inspiration for?) this idea. More generally, the authors discuss how more mature industries have well-defined standards for documenting how systems work (e.g., nutrition labels for food or datasheets for electronic hardware). There are also governmental regulations about how e.g., clinical trials must be conducted, but nothing close to that exists for ML models. "Those looking to use trained machine learning models in a particular context have no way of understanding the systemic impacts of these models before deploying them," they write. Anyone can lift a pretrained model off Github, but they might have no idea what the model was trained on, what it *wasn't* trained on, how well it performs, etc.

Model cards are important for many people:

 * ML practitioners can understand how well the model will work for its intended use case
 * Model developers can compare results across models
 * Software developers can use these to inform design decisions (e.g., by knowing that the model should never be run on certain types of inputs)
 * Policymakers can understand how a system may fail or succeed in ways that affect different groups of people
 * Organizations (what are these?) can be better informed about adopting ML systems
 * ML-knowledgeable people can learn more about models that exist
 * General people who the systems effect can better understand how it works

Going through this process "encourages forward-looking model analysis techniques" by asking these questions up front.

The authors present a two examples. The first is an image classifier for if someone is smiling, and a hidden issue is that the classifier misclassifies older men as smiling more often than other groups. A text toxicity classifier has unstable performance for text featuring the terms "lesbian," "gay," or "homosexual," indicating that an incorrect application of this classifier could cause disparate impact w.r.t. LGBTQ+ groups.

**The takeaway**: model cards are one proposal for how to increase transparency in machine learning models. By adding to models discussions about what they should and shouldn't be used for, how they were trained and evaluated, and metrics for performance on intersectional groups, we can improve transparency across machine learning researchers, users, and stakeholders.

## Thoughts, connections, and questions
This is definitely a *framework* for how to do this, and not a well-defined standard. The authors hedge their suggestions several times and discuss how their proposal may not be complete--which is great!--and so this is clearly a first step towards doing better at this. It's unlikely that this will emerge as a standard over time, too, so we have to consider this in the context of other transparency approaches.

One of the things that Hall said in the Interpretable AI talk linked above is that "our failure to address [these things] on our own could very well result in potentially draconian overregulation ... that government bodies that are not as educated about what we do will come in and say you can't do this, you can't do this, you can't do this." I completely agree with this--not that I'm against regulation, but that I trust machine learning researchers to do this much more than I trust governments to. That's why this kind of research is so interesting and necessary.

The authors discuss "performance on different groups" several times, and I think this is the single most important application of model cards. Knowing how a machine learning model affects different groups of people is imprortant, but more important is that this question gets asked throughout the model development process. They also repeatedly discuss *intersectional* analysis for human-centric models, pulling in sociology concepts to ensure that researchers treat individuals as "a complex combination of many factors," not just shaped by e.g., their age, gender, and race.

This is just one approach to increasing transparency in machine learning. Another class of research is that on interpretable models, so that we can know why models are making the decisions that they are (without resorting to post-hoc methods like LIME or SHAP). Adversarial attacks are also interesting, though I know less about them. I like these because they're information sheets about models, when currently models are often just some code and parameter weights.
