---
title: "Analysis of Symmetry and Conventions in Off-Belief Learning (OBL) in Hanabi"
layout: post
tags: [machine-learning, project]
cover: boston.avif
cover_preview: boston.avif
caption: Boston, Massachusetts, USA
class: post-template
navigation: True
author: fanpu
toc:
  sidebar: left
giscus_comments: true
description: >
  Hanabi has been proposed as the new frontier for developing strategies in
  cooperative AI, currently a very nascent area of AI research. A recent
  algorithm that has been developed for multi-agent reinforcement learning in a
  cooperative context is the Off-Belief Learning (OBL) algorithm, which is
  based on iterated reasoning starting from a base policy. We investigate if
  policies learnt by agents using the OBL algorithm in the multi-player
  cooperative game Hanabi in the zero-shot coordination (ZSC) context are
  invariant across symmetries of the game, and if any conventions formed during
  training are arbitrary or natural, both of which are desirable properties.
---

### Summary
We investigate if policies learnt by agents using the Off-Belief Learning (OBL)
algorithm in the multi-player cooperative game Hanabi in the zero-shot
coordination (ZSC) context are invariant across symmetries of the game, and if
any conventions formed during training are arbitrary or natural. We do this by
a convention analysis on the action matrix of what the agent does, introduce a
novel technique called the Intervention Analysis to estimate if the actions
taken by the policies learnt are equivalent between isomorphisms of the same
game state, and finally evaluate if our observed results also hold in a
simplified version of Hanabi which we call Mini-Hanabi.

Joint work with [William Zhang](https://17zhangw.github.io/)
for the course project of 
[15-784 Foundations of Cooperative AI](https://www.cs.cmu.edu/~15784/)

### Paper

[Link to our paper]({% link /assets/research/Analysis_Of_Symmetry_And_Conventions_In_Off_Belief_Learning_In_Hanabi.pdf %}).