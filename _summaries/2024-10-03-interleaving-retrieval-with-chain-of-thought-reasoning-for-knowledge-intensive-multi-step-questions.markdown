---
layout: summary
title: "Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions"
giscus_comments: true
bib_id: 2212.10509v2
---

### Two Important Things

#### 1. Interleaved Retrieval guided by Chain-of-Thought

Overall idea seems pretty similar to the 
[Enhancing Retrieval-Augmented Large Language Models with Iterative Retrieval-Generation Synergy]({% link _summaries/
2024-10-03-enhancing-retrieval-augmented-large-language-models-with-iterative-retrieval-generation-synergy.markdown %})
paper, except that instead of having a pre-defined number of iterations, the CoT-guided LLM decides when to stop.

{% include figure.html
    path="/assets/img/summaries/ir_cot_workflow.webp"
    width="600px"
    class="z-depth-1"
%}

#### 2. Results

Unsurprisingly outperforms one-step retrievers and when
no retrievers were used.

{% include figure.html
    path="/assets/img/summaries/ir_cot_workflow.webp"
    width="600px"
    class="z-depth-1"
%}

They also found that IRCoT's CoT trace had fewer factual errors, and remains
effective on smaller models (0.2B to 11B).

### Most Glaring Deficiency

Marginal novelty given other techniques like self-ask that came previously.

### Conclusions for Future Work

Could use a LLM to drive querying of RAG datastores guided by CoT to resolve
complex queries.