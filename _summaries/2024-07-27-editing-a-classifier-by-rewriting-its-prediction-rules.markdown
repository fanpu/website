---
layout: summary
title: "Editing a classifier by rewriting its prediction rules"
giscus_comments: true
bib_id: 2112.01008v1
---

### Three Important Things

#### 1. Problem: Spurious Features

Models tend to exploit spurious correlations in the training dataset, which can
result in poor generalizability.
For instance, the typographic attack of attaching a label with the word "iPod"
on common household objects causes classifiers to re-classify the objects as
iPods. In more benign cases, models tend to use the presence of roads or wheels to predict
that the object is a car. This could break the model if it is provided with an
image of a wooden wheel.

One way this can be fixed is to augment the training dataset with such examples of cars with wooden wheels,
but it's difficult to come up with such a dataset in practice, and it's also unclear how well this
might generalize to other contexts (i.e motorcycles with wooden wheels).

So instead of this cumbersome approach, what if we had a way to
surgically alter the prediction rules of these models to generalize
in a way we know is correct?

#### 2. Editing Classifiers

Here's how their proposed approach would work to ensure a model that can
classify cars will also be able to classify cars with wooden wheels.

1. Have an image of a car that contains a wheel, $$x$$
2. Use image segmentation methods or otherwise manually annotate the pixels that correspond to the wheel in this image
3. Now edit the image from a normal wheel to a wooden wheel, call this new image $$x'$$
4. The goal is for the classifier to treat the new image similarly to the old image
5. Choose your favorite layer $$L$$ in your neural network (ok perhaps not exactly just your favorite, but a layer where you think this editing might work well)
6. Update the weights in layer $$L$$ such that it maps the features of $$x'$$ at that stage to be as close
   to $$x$$ as possible. This will be a constrained optimization problem.
   Constraints are necessary so that the other features in the weights are not
   changed too much. The way this is done is the topic of another paper: [Rewriting a Deep Generative Model
   ](https://arxiv.org/abs/2007.15646).

#### 3. Results

They found on the experiments they did that this approach outperforms fine-tuning, even when the edit was
done on a single synthetic sample. They noted there were slight regressions on tasks
related to the concept that was changed.

### Most Glaring Deficiency

It was unclear how to choose $$L$$ (or any recommendations for choosing it),
though it's possible that this was addressed in prior work.

It was also unclear whether the edits in their "Large-scale Synthetic
Evaluation" section were all performed on a single model, or in isolation.
The former would be more realistic so that we now have a model that is very robust
and generalizes well, but if I had to guess they probably did the latter.

### Conclusions for Future Work

We can manually modify the weights of a neural network to map a known concept to
another known concept to rewire it. This can be done with just a little
regression on other tasks if done in a regularized way.
