---
title: "Evaluating RAG Systems"
layout: post
tags: [llm, RAG]
cover: furano.webp
cover_preview: furano.webp
caption: Lavender Fields in Biei, Kamikawa Subprefecture, Hokkaido, Japan
class: post-template
author: fanpu
toc:
  sidebar: left
giscus_comments: true
description: >
  Notes on the new Llama 3.1 technical report. It's a long paper, but one
  that's well-written with lots of interesting technical details and 
  design choices.
published: false
---

## Faithfulness

```
Please tell if a given piece of information is supported by the context. You
need to answer with either YES or NO. Answer YES if any of the context supports
the information, even if most of the context is unrelated. Some examples are
provided below.

Information: Apple pie is generally double-crusted.
Context: An apple pie is a fruit pie in which the principal filling ingredient
is apples. Apple pie is often served with whipped cream, ice cream ('apple pie à
la mode'), custard, or cheddar cheese. It is generally double-crusted, with
pastry both above and below the filling; the upper crust may be solid or
latticed (woven of crosswise strips).
Answer: YES

Information: Apple pies taste bad.
Context: An apple pie is a fruit pie in which the principal filling ingredient
is apples. Apple pie is often served with whipped cream, ice cream ('apple pie à
la mode'), custard, or cheddar cheese. It is generally double-crusted, with
pastry both above and below the filling; the upper crust may be solid or
latticed (woven of crosswise strips).
Answer: NO

Information: {query_str}
Context: {context_str}
Answer:
```
