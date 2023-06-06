---
title: "Improving Domain Adaptation of Transformer Models For Generating Reddit Comments"
layout: post
tags: [machine-learning, project]
cover: rainier_view.avif
cover_preview: rainier_view.avif
caption: Skyline Loop Trail, Mount Rainier National Park, Washington, USA
class: post-template
navigation: True
author: fanpu
toc:
  sidebar: left
giscus_comments: true
description: >
  We improve upon the recent success of large language models based on the
  transformer architecture by investigating and showing several methods that
  have empirically improved its performance in domain adaptation. We use a
  pre-trained GPT-2 model and perform fine-tuning on 5 different subreddits,
  and use different methods of ordering the training data based on our priors
  about the input to see how this affects the prediction quality of the trained
  model. We propose a new metric for evaluating causal language modeling tasks
  called APES (Average Perplexity Evaluation for Sentences) to address the
  limitations of existing metrics, and apply them to our results. Our results
  are evaluated against both LSTM and GPT-2 baselines.
---

### Summary
We improve upon the recent success of large language models based on the
transformer architecture by investigating and showing several methods that
have empirically improved its performance in domain adaptation. We use a
pre-trained GPT-2 model and perform fine-tuning on 5 different subreddits,
and use different methods of ordering the training data based on our priors
about the input to see how this affects the prediction quality of the trained
model. We propose a new metric for evaluating causal language modeling tasks
called APES (Average Perplexity Evaluation for Sentences) to address the
limitations of existing metrics, and apply them to our results. Our results
are evaluated against both LSTM and GPT-2 baselines.

There have been many exciting breakthroughts in language generation models in
recent years. From the simple n-gram model that has been studied since the
early 20th century, to the introduction of neural language models that utilizes
word embeddings at the turn of the century (2001), in the past few years we saw
the development of powerful language models such as Word2Vec (2013),
Transformer (2017), BERT (2018), GPT (2018), GPT-3 (2020). Such models have
already beaten humans in accuracy in tasks such as reading comprehension, and
have displayed high levels of fluency in language-generation tasks. These
successes can be attributed to the great strides taken in Deep Learning, the
increase in computational resources, and the proliferation of publicly
available datasets and benchmarks.

We aim to replicate and build upon existing work in causal language models by
investigating and answering the following research questions in this paper:

1. Can we improve the performance of domain adaptation of transformer language
   models by various methods of ordering the inputs seen at training time,
   based on our priors about the input?

2. Can we successfully perform domain adaptation using just commodity hardware
   on unstruc- tured internet discourse that can contain new vocabulary, carry
   unique speech patterns, and require expert domain knowledge in order to
   provide a cogent response to a prompt?

3. Can we successfully perform domain adaptation on large language models with
   billions of parameters even with very small datasets?

4. What is a suitable evaluation metric to determine the success of domain
   adaptation for text generation, given the limitations of existing metrics
   for evaluating causal language models?
     
Our paper shows mild results for point 1, and answers points 2 and 3
affirmatively empirically. We propose a new metric to address point 4 which we
call APES (Average Perplexity Evaluation for Sentences), and use it to evaluate
our results. We achieve our results by fine-tuning a pre-trained GPT-2 language
model using data from 5 subreddits with distinct topics and talking styles, and
use various methods of ordering the input data to improve the performance of
fine-tuning as measured by the Bilingual Evaluation Understudy (BLEU) score and
a qualitative evaluation of the results given a prompt from different
subreddits. Finally, we use the APES metric to manually score 200 results from
the test set from each dataset from 1 to 5. Our results are evaluated against a
LSTM baseline and a GPT-2 model without fine-tuning.

Joint work with Joseph Salmento
for the course project of 
[10-617 Intermediate Deep Learning](https://rsalakhucmu.github.io/10417-22/).

### Paper

[Link to our paper]({% link /assets/research/Improving_Domain_Adaptation_Of_Transformer_Models_For_Generating_Reddit_Comments.pdf %}).