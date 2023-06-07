---
title: "Graphical Bayesian Networks with Topic Modeling Priors for Predicting Asset Covariances"
layout: post
tags: [machine-learning, project]
cover: rainier.avif
cover_preview: rainier.avif
caption: Mount Rainier, Mount Rainier National Park, Washington, USA
class: post-template
author: fanpu
toc:
  sidebar: left
giscus_comments: true
description: >
  Covariance matrix prediction is a long-standing challenge in modern portfolio
  theory and quantitative finance. In this project, we investigate the
  effectiveness of Bayesian networks in predicting the covariance matrix of
  financial assets (specifically a subset of the S&P 500), evaluated against
  Heterogeneous Autoregressive (HAR) models. In particular, we consider both
  HAR-DRD, based on the DRD decomposition of the covariance matrix, and Graphical
  HAR (GHAR)-DRD, which is also based on DRD decomposition but also makes use of
  graphical relationships between the assets. To build the graph representing
  relationships between the assets, we apply Latent Dirichlet allocation (LDA) on
  the 10-K filings of each of the companies, and infer edges based on topic
  overlap. 
---

### Summary

Covariance matrix prediction is a long-standing challenge in modern portfolio
theory and quantitative finance. In this project, we investigate the
effectiveness of Bayesian networks in predicting the covariance matrix of
financial assets (specifically a subset of the S&P 500), evaluated against
Heterogeneous Autoregressive (HAR) models. In particular, we consider both
HAR-DRD, based on the DRD decomposition of the covariance matrix, and Graphical
HAR (GHAR)-DRD, which is also based on DRD decomposition but also makes use of
graphical relationships between the assets. To build the graph representing
relationships between the assets, we apply Latent Dirichlet allocation (LDA) on
the 10-K filings of each of the companies, and infer edges based on topic
overlap. We show that this technique has limited usefulness in our setup, but
provides recommendations on how it could be further improved based on our
observations of its predictions.

Joint work with [Kevin Minghan
Li](https://www.cmu.edu/mscf/student-experience/meet-our-current-students/2023-minghanl.html)
for the course project of [10-708 Probabilistic Graphical Models](https://andrejristeski.github.io/10708-F22/).

### Paper

[Link to our paper]({% link /assets/research/Graphical_Bayesian_Networks_For_Predicting_Asset_Covariances.pdf %}).