# Defending Deep Learning from Adversarial Attacks

## Animesh Singh and Svetlana Levitan (IBM) - 4/25

They work at the "center for open source data and AI technologies" @ IBM.

## Bias throughout the AI lifecycle

There's an open source toolkit [AIF360](https://github.com/IBM/AIF360) ("AI Fairness 360") to monitor and remove bias in machine learning models. It includes 70+ fairness metrics and 10 mitigation algorithms to help remove those. One of those metrics is disparate impact (!!!) along with tons of others, and this actually seems incredible.

##Adversarial attacks

This field is getting a lot noisier (heh) and more research; adding white noise that is imperceptible to humans can blow up models and make their predictions vary wildly. Famous examples include the adversarial patch that makes everything appear to be a toaster; scarier ones include adding adversarial noise to self-driving cars.

**Poisoning attacks** are performed at training, by inserting poisoned samples in training data. This lets a malicious agent use a backdoor later. **Evasion attacks** are performed at test time.

Threat models include:

* **black box vs. white box**; what knowledge does the attacker have about the model? how do they access the model?
* **plausible deniability**: how important is it for the attacker to use adversarial samples that resemble original inputs?
* **type I vs. II errors**: bypass safeguards or increase false alarms?
* one more that I missed

Some evasion attacks push neural networks (or other models) out of their desired operating range — either finding a region of space that's sparse or pushing it out of the range that it was trained on. Key point is that DNNs don't learn to *recognize* a schoolbus, but rather to discriminate it from other objects in the training set.

## Defending adversarial attacks

**Training solely on adversarial examples**, which increases the capacity to maintain accuracy on clean data. Use a specific algorithm to intentionally introduce poisoned data as the model is trained.

**Preprocess data** to remove adversarial noise, and input the cleaned samples into the classifier. But this can be defeated by an adaptive adversary (someone who knows how the cleaning is done).

**Robustness metrics**, e.g., CLEVER, which evaluate how robust neural networks are. Paper: "[Evaluating the Robustness of Neural Networks: An Extreme Value Theory](https://openreview.net/pdf?id=BkUHlMZ0b)."

**Poisoning detection**, where you look at clustering of the training data and see if it's been poisoned.

Many, many others … 

All of this to say that IBM built the [Adversarial Robustness Toolbox](https://github.com/IBM/adversarial-robustness-toolbox), which is open-source and is a library for adversarial machine learning. It includes evasion attacks, evasion defenses, poisioning and evasion detection, and robustness metrics. 

## Demos

These were all super slick. This [demo](https://art-demo.mybluemix.net/) lets you interactively add imperceptible noise to images, and wow this is so cool. Then they showed some Jupyter notebooks with code samples from their toolbox.

Another paper: [Towards Deep Learning Models Resistant to Adversarial Attacks](https://arxiv.org/pdf/1706.06083.pdf).

