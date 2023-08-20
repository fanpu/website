---
layout: summary
title: "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer"
giscus_comments: true
bib_id: 1910.10683v3
---

### Three Important Things

#### 1. Text-to-Text Transfer Transformer (T5)
The **T**ext-**t**o-**T**ext **T**ransfer **T**ransformer (T5) model
has an encoder-decoder architecture. 

The encoder has a "fully-visible"
attention mask, meaning that the attention mechanism can attend to any position
in the input. On the other hand, the decoder has a "causal" attention mask,
and can only attend to tokens $$j < i$$ when it is trying to compute the token
at position $$i$$, to prevent it from seeing the future inputs which would otherwise
trivialize the training process.

#### 2. Prefix LM

#### 3. Baz


### Most Glaring Deficiency

### Conclusions for Future Work
