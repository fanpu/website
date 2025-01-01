---
layout: summary
title: "RAGAS: Automated Evaluation of Retrieval Augmented Generation"
giscus_comments: true
bib_id: 2309.15217v1
---

### Three Important Things

The paper proposes metrics to use for RAG evaluation:

#### 1. Faithfulness

First decompose answer into smaller statements:

```
Given a question and answer, create one
or more statements from each sentence
in the given answer.
question: [question]
answer: [answer]
```

Then verify if each of the statements are
supported:

```
Consider the given context and following
statements, then determine whether they
are supported by the information present
in the context. Provide a brief explanation for each statement before arriving
at the verdict (Yes/No). Provide a final
verdict for each statement in order at the
end in the given format. Do not deviate
from the specified format.
statement: [statement 1]
...
statement: [statement n]
```

Final faithfulness score is the number of supported statements divided by the
total number of statements:

$$F = \frac{|V|}{|S|}$$

#### 2. Answer Relevance

This metric assesses whether the answer actually addresses the question, but not the
factuality of the answer.

This is done by generating questions using the answer:

```
Generate a question for the given answer.
answer: [answer]
```

and then taking embeddings of these question.

The answer relevance score is the average of the cosine similarity between the
embeddings of each of the generated questions, and the actual question:

$$\mathrm{AR}=\frac{1}{n} \sum_{i=1}^n \operatorname{sim}\left(q, q_i\right)$$

#### 3. Context Relevance

This metric helps to measure how much of the retrieved
context is actually relevant to answer the question, and hence penalizes the retrieval of extraneous information.

Provided with a question and the retrieved context,
the following prompt is used to extract the relevant statements:

```
Please extract relevant sentences from
the provided context that can potentially
help answer the following question. If no
relevant sentences are found, or if you
believe the question cannot be answered
from the given context, return the phrase
"Insufficient Information". While extracting
candidate sentences you’re not
allowed to make any changes to sentences
from given context.
```

The context relevance score is then computed as:

$$\mathrm{CR}=\frac{\text { number of extracted sentences }}{\text { total number of sentences in } c(q)}$$

### Most Glaring Deficiency

Very little experimental data in the paper. Some people on Reddit also
complained that it doesn't work well in practice as reasonable answers are
scored very poorly, and it fails to differentiate good/bad responses.

### Conclusions for Future Work

Despite its limitations RAGAS is still pretty influential in the sphere of LLM
metrics, and some of these can probably be used to evaluate RAG systems with a
YMMV caveat.
