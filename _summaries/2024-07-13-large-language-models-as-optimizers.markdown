---
layout: summary
title: "Large Language Models as Optimizers"
giscus_comments: true
bib_id: 2309.03409v3
---

### Three Important Things

#### 1. OPRO Framework

The paper introduces the Optimization by PROmpting (OPRO)
framework to make use of LLMs as optimizers.

This works as follows. The user first comes up with a meta-prompt,
which defines the problem of optimizing for the prompt that we actually care about. 

The example below shows a meta-prompt for optimizing for a CoT-style prompt:

```text
I have some texts along with their corresponding scores. The texts are arranged in ascending order
based on their scores, where higher scores indicate better quality.

text:
Let’s figure it out!
score:
61

text:
Let’s solve the problem.
score:
63

(. . . more instructions and scores . . . )

The following exemplars show how to apply your text: you replace <INS> in each input with your
text, then read the input and give an output. We say your output is wrong if your output is different
from the given output, and we say your output is correct if they are the same.

input:
Q: Alannah, Beatrix, and Queen are preparing for the new school year and have been given books
by their parents. Alannah has 20 more books than Beatrix. Queen has 1/5 times more books than
Alannah. If Beatrix has 30 books, how many books do the three have together?
A: <INS>
output:
140

(. . . more exemplars . . . )

Write your new text that is different from the old ones and has a score as high as possible. Write the
text in square brackets.
```

Once the LLM produces a new solution, it can then be evaluated, and the 
solution-score pairs added back into the meta-prompt, allowing the next iteration to learn from previous trajectories.

This loop of optimization continues until the LLM plateaus in the scores
of the proposed solutions, or the number of optimization steps is reached.

Overall, the OPRO optimization loop looks like this:

{% include figure.html
    path="/assets/img/summaries/opro_architecture.webp"
    width="400px"
    class="z-depth-1"
%}

#### 2. Bar

#### 3. Baz

### Most Glaring Deficiency

### Conclusions for Future Work
