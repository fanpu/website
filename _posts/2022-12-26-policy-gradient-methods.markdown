---
title: "Policy Gradient Methods: Natural Policy Gradients, PPO, TRPO"
layout: post
tags: [machine-learning, code]
cover: red_rock.avif
cover_preview: red_rock.avif
caption: Valley of Fire State Park, Overton, Nevada, USA
class: post-template
navigation: True
author: fanpu
toc:
  sidebar: left
description: >
published: false
---
Policy gradient methods are a class of reinforcement learning techniques
that aims to optimize some policy $$\pi_\theta$$ parameterized by its
policy parameters $$\theta$$ by updating it in the direction
of the gradient. Usually, the policy takes the form of a neural network,
and $$\theta$$ will be the associated weights. However, the nature
of trajectory sampling in reinforcement learning means that policy updates 
must be performed carefully as it could result result in the policy
going into an irrecoverable region.
In this post, we discuss three policy gradient methods that are widely used
or are of theoretical interest: Natural Policy Gradients,
Proximal Policy Optimization (PPO), and Trust Region Policy Optimization (TRPO).

## Background
Our goal is to maximize the expected rewards for our policy over the trajectories
that it visits. 
This can be formalized as

\begin{equation}
    \max_\theta \E_{\tau \sim P_\theta(\tau)} [R(\tau)],
\end{equation}

where $$\tau$$ refers to a trajectory of state-action pairs, $$P_\theta(\tau)$$
denotes the probability of experiencing trajectory $$\tau$$ under policy $$\theta$$,
and $$R(\tau)$$ is the reward under trajectory $$\tau$$.

To perform a gradient-based update on $$\theta$$ to increase the reward, we 
need to compute 
$$\nabla_\theta \E_{\tau \sim P(\tau; \theta)} [R(\tau)] $$. We can derive the
following sequence of steps:


\begin{align}
 hello   
\end{align}

## Performing Policy Updates

Policy updates are performed by deploying the current policy $$\pi_theta$$, and
sampling many state-action trajectories



## The Problem with Stepsize Updating Policies

## Natural Policy Gradients


In reinforcement learning,