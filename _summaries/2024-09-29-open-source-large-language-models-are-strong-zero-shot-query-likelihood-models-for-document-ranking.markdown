---
layout: summary
title: "Open-source Large Language Models are Strong Zero-shot Query Likelihood Models for Document Ranking"
giscus_comments: true
bib_id: 2310.13243v1
published: false
---

### Three Important Things

#### 1. Query Likelihood Models

To rank the relevance of documents for a supplied query, we can compute the probability of generating a query given a document,
i.e its query likelihood. This can be computed by:

$$S_{Q L M}(\boldsymbol{q}, d)=\frac{1}{|\boldsymbol{q}|} \sum_t \log \operatorname{LLM}\left(q_t \mid \boldsymbol{p}, d, \boldsymbol{q}_{<t}\right),$$

i.e the perplexity of the query given the document $$d$$ and the model and prompt $$\boldsymbol{p}$$.

The paper's insight is to use the LLM to compute this probability, and they

#### 2. Bar

#### 3. Baz

### Most Glaring Deficiency

### Conclusions for Future Work
