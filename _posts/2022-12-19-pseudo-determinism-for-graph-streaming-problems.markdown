---
title: "Pseudo-determinism for Graph Streaming Problems"
layout: post
tags: [theory, project]
cover: rainier_top.jpg
cover_preview: rainier_top.avif
caption: View from Skyline Loop Trail, Mount Rainier National Park, Washington, USA
class: post-template
navigation: True
author: fanpu
toc: true
giscus_comments: true
description: >
   Given a fixed input for a search problem, pseudo-deterministic algorithms
   produce the same answer over multiple independent runs, with high probability.
   For example, we can efficiently find a certificate for inequality of
   multivariate polynomials pseudo-deterministically, but it is not known how to
   do so deterministically. The same notion can be extended to the streaming
   model. The problem of finding a nonzero element from a turnstile stream is
   previously shown to require linear space for both deterministic and
   pseudo-deterministic algorithms. Another model of streaming problems is that
   of graphs, where edge insertions and deletions occur along a stream. Some
   natural problems include connectivity, bipartiteness, and colorability of a
   graph. While the randomized and deterministic graph streaming algorithms
   have been mostly well-studied, we investigate pseudo-deterministic space
   lower bounds and upper bounds for graph theoretic streaming problems.
---

### Summary
Given a fixed input for a search problem, pseudo-deterministic algorithms
produce the same answer over multiple independent runs, with high probability.
For example, we can efficiently find a certificate for inequality of
multivariate polynomials pseudo-deterministically, but it is not known how to
do so deterministically. The same notion can be extended to the streaming
model. The problem of finding a nonzero element from a turnstile stream is
previously shown to require linear space for both deterministic and
pseudo-deterministic algorithms. Another model of streaming problems is that
of graphs, where edge insertions and deletions occur along a stream. Some
natural problems include connectivity, bipartiteness, and colorability of a
graph. While the randomized and deterministic graph streaming algorithms
have been mostly well-studied, we investigate pseudo-deterministic space
lower bounds and upper bounds for graph theoretic streaming problems.

Joint work with [Albert Gao](https://adbforlife.github.io/),
[Andrew Caosun](https://www.linkedin.com/in/andrew-caosun-a237ab19b/),
[Puhua Cheng](https://www.linkedin.com/in/puhuacheng/)
for the course project of 
[15-859CC Algorithms for Big Data](https://www.cs.cmu.edu/~dwoodruf/teaching/15859-fall22/index.html).

### Paper
[Link to our paper]({% link /assets/research/Pseudodeterminism_For_Graph_Streaming_Problems.pdf %}).