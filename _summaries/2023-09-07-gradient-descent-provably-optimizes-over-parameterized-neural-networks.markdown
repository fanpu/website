---
layout: summary
title: "Gradient Descent Provably Optimizes Over-parameterized Neural Networks"
giscus_comments: true
bib_id: 1810.02054v2
---

### Three Important Things

#### 1. Foo

This paper shows theoretically how overparameterization of a two-layer neural
network can result in a linear rate of convergence (linear when logarithms are
taken, hence it really converges exponentially fast).

The setup of the paper is a standard two-layer neural network of the following form:

$$
f(\mathbf{W}, \mathbf{a}, \mathbf{x})=\frac{1}{\sqrt{m}} \sum_{r=1}^{m} a_{r} \sigma\left(\mathbf{w}_{r}^{\top} \mathbf{x}\right)
$$

The first layer is initialized with random Gaussians, and the second layer is initialized
uniformly with either -1 or +1. The reason $$\pm 1$$ initialization was used in the second
layer is because it simplifies the Gram matrix of the weights.

The main result of the paper states that if the following conditions hold:

1. The width $$m$$ of the network is large enough,
2. The neural network is initialized in the manner mentioned previously,
3. The Gram matrix is well-conditioned, i.e its smallest eigenvalue $$\lambda_0$$ is bounded away from 0

The Gram matrix $$\bH$$ here
is defined as the matrix product of the differential map
of $$f$$ with its transpose, i.e $$\nabla_W f \, \nabla_W f^{\top} $$.
This is similar to the kernel in the [neural tangent kernel paper](https://arxiv.org/abs/1806.07572).
Note that the eigenvalues of the Gram matrix are always non-negative since the Gram matrix is positive semi-definite.


Theorem 4.1 (Convergence Rate of Gradient Descent). Under the same assumptions as in Theorem 3.2. if we set the number of hidden nodes $m=\Omega\left(\frac{n^{6}}{\lambda_{0}^{4} \delta^{3}}\right)$, we i.i.d. initialize $\mathbf{w}_{r} \sim N(\mathbf{0}, \mathbf{I})$, $a_{r} \sim$ unif $[\{-1,1\}]$ for $r \in[m]$, and we set the step size $\eta=O\left(\frac{\lambda_{0}}{n^{2}}\right)$ then with probability at least $1-\delta$ over the random initialization we have for $k=0,1,2, \ldots$

$$
\|\mathbf{u}(k)-\mathbf{y}\|_{2}^{2} \leq\left(1-\frac{\eta \lambda_{0}}{2}\right)^{k}\|\mathbf{u}(0)-\mathbf{y}\|_{2}^{2}
$$





There are two main contributions in the paper:

1. If the least eigenvalue of the Gram matrix of the weight of the parameters can
be lower bounded, then gradient descent converges at a linear rate.

2. The Gram matrix is only related to the activation
function used, and if most of the values of the activation
does not change during training, then the Gram matrix
is close to its value at initialization.

3. Over-parameterization, random initialization, and 

$$
    \newcommand{\wr}{\mathbf{w}_r}
$$

#### 2. Bar

#### 3. Baz

### Most Glaring Deficiency

### Conclusions for Future Work
