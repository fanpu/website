---
title: "Impagliazzo's Five Worlds, or The Computational (Im)Possibilities of The World That We Live In"
layout: post
tags: [complexity-theory, computer-science]
cover: denali.webp
cover_preview: denali.webp
caption: Denali National Park, Alaska
description: >
    Most people have probably heard of the P = NP? problem in some shape or
    form, which asks whether the class of languages decidable in deterministic
    polynomial time is the same as the class of languages decidable in
    non-deterministic polynomial time. However, there are also
    several other interesting classes of intermediate possibilities that can arise
    if it was the case that P != NP, as this post explores.
class: post-template
author: fanpu
toc:
  sidebar: left 
giscus_comments: true
---
Most people have probably heard of the $$\mathsf{P} = \mathsf{NP}?$$ problem in some shape or
form, which asks whether the class of languages decidable in deterministic
polynomial time is the same as the class of languages decidable in
non-deterministic polynomial time. An affirmative answer in either direction
will have profound implications on complexity theory and on our world, as we
will soon see.

It is generally believed that $$\mathsf{P} \neq \mathsf{NP} $$ among complexity theorists, and
in fact, it is not uncommon for many theorems to make use of even stronger
assumptions such as the Exponential Time Hypothesis (ETH) in order to push some
theorems through.   

In this post, we extend the discussion to other possible possible outcomes based
on Impagliazzo's influential 1995 paper [A personal view of average-case
complexity](https://ieeexplore.ieee.org/document/514853).

# A Primer on Complexity Classes
This is a short primer on some common complexity classes that will be repeatedly mentioned through the article,
meant for people without much complexity exposure.
Feel free to skip it if you already know what they are.
 
$$ \mathsf{P} $$ (polynomial time) is the class of languages that can be solved
deterministically by a Turing machine in polynomial time with respect to the
size of the input. This means that there exists an algorithm that can solve the
problem with an input of length $$n$$ in time $$ O(n^c) $$ for some constant
$$c$$.
 
$$ \mathsf{NP} $$ (non-deterministic polynomial time) is the class of languages that can
be solved by a non-deterministic Turing machine in polynomial time. A helpful
way of looking at it is that the Turing machine is able to branch on all
possibilities in parallel (non-determinism), and therefore it can simply try all
solutions in parallel and check if it works. Therefore, an equivalent
formulation is that a problem is in $$ \mathsf{NP} $$ if it is easy to verify the
solution to an input in polynomial time.
 
$$ \BPP $$ (bounded-error probabilistic polynomial time) is the class of
languages that can be solved in polynomial time by a Turing machine that has
access to random coins, and returns results with a constant error (say 1/3 of
the time). The exact constant does not matter since execution can be simply
repeated an additional polynomial number of times to bring the error down
exponentially, without changing the total polytime execution time. A language in
$$\BPP$$ means that we can have a very efficient algorithm in practice since the
error can be reduced to become negligible using the aforementioned technique.

# The Five Worlds
Here, we discuss each of the Five Worlds - Algorithmica, Heuristica, Pessiland,
Minicrypt, and Cryptomania, Strictly speaking, there are other intermediate
possibilities that Impagliazzo excluded which Arora and Barak calls "Weirdland",
such as if $$ \SAT $$ takes superpolynomial time to solve, or the complexity of
$$ \SAT $$ differs wildly depending on the input size. Do refer to their book mentioned in the [References](#references) section if you are interested.

## Algorithmica
In Algorithmica, either $$ \mathsf{P} = \mathsf{NP} $$ or some moral equivalent like $$\mathsf{NP} \subseteq
\BPP$$ holds true.  This means that whenever we have a problem where it is easy
to check whether a solution is valid (meaning it is in $$ \mathsf{NP} $$), we also have an
algorithm to efficiently recover the solution.
 
A major implication is that almost all optimization problems become easy:
instead of maximizing an objective function $$f$$, we can reduce the problem to
asking if there exists a solution $$ (x_1, x_2, \cdots, x_n) $$ that results in
an objective value $$ f(x_1, x_2, \cdots, x_n) \geq c $$ for some threshold
$$c$$.  Verifying whether the solution meets the threshold is easy and therefore
in $$\mathsf{NP}$$, which admits an efficient algorithm under our Algorithmica
assumption.  Binary search can be performed on $$c$$ to find a solution with the
best value.  This will bring paradise to many areas of engineering and science.
 
On the other hand, cryptography is now dead. Cryptography is founded on the
assumption of one-way functions, where given some function $$ f $$, it is easy
to compute $$ y = f ( x ) $$ given $$ x $$ but hard to invert $$ f $$ to
recover $$ x $$ given $$ y $$. This is because one-way functions are in $$ \mathsf{NP}
$$, which voids such an assumption.

## Heuristica
In Heuristica, problems in $$ \mathsf{NP} $$ have worst-case hardness, but all problems
that we encounter in practice can be solved in polynomial time.  To make it
precise, we can think of inputs to all our problems as being coming from a
probability distribution that is generated by an algorithm that runs in
polytime. This could be an algorithm that computes the cumulative distribution
function for the distribution.  The constrained running time of this algorithm
therefore limits how adversarial the probability distribution can be.
 
Levin (of Cook-Levin fame) argues that if we believe in the strong Church-Turing
thesis, which states that the universe is essentially a Turing machine, then all
problems that we encounter in real life must be generated by something like a
polytime Turing machine. Then $$ \mathsf{NP} $$ problems are easy on average, or have
polynomial average-case complexity.  In computational complexity literature,
this is saying that $$ \distNP \subseteq \distP $$ (a formal introduction of
these two complexity classes is beyond the scope of this post. There are a lot
of nuances involved in their formulation in order to make it robust to different
computational models, and therefore interested readers are directed to Arora and
Barak's book for further reading).
 
In addition, cryptography is still dead, because it is extremely hard to come up
with any puzzles that an adversary can't solve efficiently. 

## Pessiland
Pessiland is named as such as it is the worst possible world, where problems in
$$ \mathsf{NP} $$ are not easy on average, and one-way functions also do not exist. 
 
This means that it is easy to come up with many hard unsolved instances of
problems (perhaps by randomness), but hard to come up with solved instances that
could be used for one-way functions. 
 
In such a world, applying generic algorithms to solve problems will not take one
very far, and most advances will be made by understanding the specific problem
domain better, and making tailored optimizations and finding good heuristics,
not very much unlike what we currently do.

## Minicrypt
In Minicrypt, one-way functions exist, but not public key cryptography. One of
the two most popular primitives used in public-key cryptography protocols are
the Diffie-Hellman key-exchange protocol, and the RSA asymmetric encryption
algorithm.
 
The Diffie-Hellman key exchange protocol is one of the most widespread protocols
used for performing a secret key exchange, and it relies on the Decisional
Diffie-Hellman (DDH) assumption. The DDH states that given any cyclic group $$ G
$$ with generator $$ g $$ and order $$ q $$, the following two probability
distributions are computationally indistinguishable:

<div>
$$ ( g^a, g^b, g^{ab})$$
$$ ( g^a, g^b, g^c) $$
</div>

where $$ a, b, c \in \mathbb{Z}_q $$.
 
RSA encryption relies on the assumption of the hardness of factorization, which
is already untrue in the quantum computation model. This is thanks to the celebrated Shor's
algorithm, published in 1994 by Peter Shor, which performs integer
factorization in $$ \BQP $$, i.e in polynomial time on a quantum computer.  This
has also caused a general shift among the cryptography community to start moving
standards towards post-quantum cryptography, which relies on cryptosystems that
are believed to be resistant to quantum computers.

## Cryptomania
Finally, Cryptomania is the world that most computational complexity experts
believe that we live in. Public key cryptography exists (which implies the
existence of one-way functions), allowing for many exciting applications such as
secure multi-party computation and electronic money systems like Bitcoin.  It's
a pity that we lose the ability to solve $$ \mathsf{NP} $$ problems efficiently like in
Algorithmica and Heuristica, but at least now we get something back!

# Some Closing Thoughts
I found it illuminating to consider a more nuanced debate of the computational
possibilities of our world beyond just a simplistic $$ \mathsf{P} = \mathsf{NP}? $$ view. Most
experts think that we are in Minicrypt or Cryptomania. It would be interesting
to see if the cryptosystems that we rely so heavily on today (Diffie-Hellman,
elliptic curve cryptography, etc) will be broken in the coming decades, since we
have no real reason to believe that the assumptions are hard other than the fact
that a ton of smart people have tried for years to break it and failed. 

# References
- [Personal View of Average-Case
Complexity](https://www2.karlin.mff.cuni.cz/~krajicek/ri5svetu.pdf)
- [Average Case Complexity](
https://www2.cs.sfu.ca/~kabanets/881/scribe_notes/lec8.pdf)
- Arora, S., &amp; Barak, B. (2016). Computational Complexity: A Modern
Approach. Cambridge University Press. 