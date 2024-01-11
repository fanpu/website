---
layout: summary
title: "In-context Learning and Induction Heads"
giscus_comments: true
bib_id: 2209.11895v1
published: false
---

### Three Important Things

#### 1. Induction Heads

This paper aims to mechanistically understand why in-context learning works, and
proposes that this is due to the induction head hypothesis.

The induction head is a circuit where given some current token (i.e `A`)
and tasked with predicting a future token,
it tries to look back for an instance of `A` in its history and find
what follows. So if there used to be some sequence `[A][B]...`, it will
complete `B` as the next token.

The induction heads hypothesis claims that the induction head mechanism
can account for most of the success of in-context learning.

#### 2. Bar

#### 3. Baz

### Most Glaring Deficiency

### Conclusions for Future Work
