---
title: "LaTeX-ing Like Your Grades Depended On It: Common Mistakes and Tips for Typesetting Beautiful, Delightful Proofs"
layout: post
tags: [code]
cover: ubin_pond.jpg
cover_preview: ubin_pond.jpg
caption: Pulau Ubin, Singapore
class: post-template
navigation: True
author: fanpu
toc: true
giscus_comments: true
description: >
hidden: true
---

When was the first time you had to use [LaTeX](https://www.latex-project.org/)?
If you are like most people, it was probably suddenly forced upon you during
your first math or CS class where you had to start writing proofs, with minimal
guidance on how to get started other than something along the lines of``hey,
check out this link on how to get things setup, and here are some basic
commands, now go wild!''.

Unfortunately, this meant that while many people have good operational knowledge
of LaTeX and can get the job done, very often there are still many small mistakes and
best practices which are not followed, and which are often not corrected by TAs
as they are either not severe enough to warrant a note, or oftentimes even the TAs themselves
are not aware of it.

In this post, we cover some common mistakes that are made by LaTeX practitioners.
This post assumes that the reader has some working knowledge of LaTeX.

### Typesetting as a Form of Art
It is important to get into the right mindset whenever you typeset a
document. You are not simply ``writing'' a document - you are crafting a work
of art that combines both the precision and creativity of your logical
thinking, as well as the elegance of a beautifully typeset writing. The amount
of attention and care you put into the presentation is indicative of the amount
of thought you put into the content. Therefore, having good style is not
only delightful and aesthetically pleasing to read, but it also serves to establish 
your ethos and character. One can tell that someone puts a lot of effort into their
work and takes great pride in them when they pay attention even to the smallest of
details.

Furthermore, adopting good practices also helps to avoid you making
typographical mistakes in your proof, such as missing parenthesis or wrong
positioning. This could often lead to cascading errors that are very annoying
to fix when you discover them later on. There are ways to replicate the strict
typechecking of statically typed languages to ensure that mistakes in your
expressions can be caught at compile-time.

### Common Mistakes, and How To Fix Them
In this section, we take a look at common mistakes that people make, and how they 
can be avoided or fixed.

#### Paired Delimiters
Parenthesis, brackets, and pipes are examples of delimiters that are used to mark the start
and end of formula expressions. As they come in pairs, a common mistake is accidentally 
leaving out the closing delimiter, especially for nested expressions. Even if you don't
forget to do so, there is the issue of incorrect sizing. 

For instance, consider
the following way of expressing the Topologist's sine curve, which is an example of a topology
that is connected but not path connected:

{% highlight latex %}
T = \{ ( x, \sin \frac{1}{x} ) : x \in (0, 1] \} \cup \{ ( 0, 0 ) \}
{% endhighlight %}

which is rendered as follows:

$$
    T = \{(x, \sin \frac{1}{x} ) : x \in (0, 1] \} \cup \{ ( 0, 0 ) \}
$$

The problem here is that the curly braces have the wrong
size, as they should be large enough to cover the $$\sin \frac{1}{x}$$ expression vertically.

The wrong way of resolving this would be to use delimiter size modifiers, i.e
`\bigl, \Bigl, \biggl` paired with `\bigr, \Bigr, \biggr`  and the like. This
is tedious and error-prone, since it will even happily let you match delimiters
with different sizes. Indeed, I came across the following formula in a
paper recently, where the outer right square brackets was missing and the left one
had the wrong size:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/paired_delim.png"
    width="500px"
    class="z-depth-1"
    caption="What happens when you don't use paired delimiters"
%}

The correct way to do this would be to use paired delimiters,
which will automatically adjust its size based on
its contents, and automatically result in a compile error if the matching
right delimiter is not included, or nested at the wrong level.
Some of them are given below:

| Raw LaTeX                               | Rendered                                    |
|-----------------------------------------|---------------------------------------------|
| `\left( \frac{1}{x} \right)   `         | $$ \left( \frac{1}{x} \right)    $$         |
| `\left[ \frac{1}{x} \right]   `         | $$ \left[ \frac{1}{x} \right]    $$         |
| `\left\{ \frac{1}{x} \right\} `         | $$ \left\{ \frac{1}{x} \right\}  $$         |
| `\left\| \frac{1}{x} \right\| `         | $$ \left\| \frac{1}{x} \right\|  $$         |
| `\lvert \frac{1}{x} \rvert    `         | $$ \lvert \frac{1}{x} \rvert     $$         |
| `\left\| \frac{1}{x} \right\| `         | $$ \left\| \frac{1}{x} \right\|  $$         |
| `\left\lceil \frac{1}{x} \right\rceil ` | $$ \left\lceil \frac{1}{x} \right\rceil  $$ |
{: .table .table-bordered .table-sm }

In fact, to make things even simpler and more readable, you can declare paired delimiters 
for use based on the `mathtools` package:

{% highlight latex %}
% Make sure you include \usepackage{mathtools}
\DeclarePairedDelimiter\parens{\lparen}{\rparen}
\DeclarePairedDelimiter\abs{\lvert}{\rvert}
\DeclarePairedDelimiter\norm{\lVert}{\rVert}
\DeclarePairedDelimiter\floor{\lfloor}{\rfloor}
\DeclarePairedDelimiter\ceil{\lceil}{\rceil}
\DeclarePairedDelimiter\braces{\lbrace}{\rbrace}
\DeclarePairedDelimiter\bracks{\lbrack}{\rbrack}
\DeclarePairedDelimiter\angles{\langle}{\rangle}
{% endhighlight %}

Then you can now use the custom delimiters as follows, taking note that you need the `*`
for it to auto-resize:

{% highlight latex %}
T = \braces*{ \parens*{ x, \sin \frac{1}{x} } : x \in (0, 1] } \cup \braces*{ \parens*{ 0, 0 }}
{% endhighlight %}

which gives 

$$
T = \left\{ \left( x, \sin \frac{1}{x} \right) : x \in (0, 1] \right\} \cup \left\{ \left( 0, 0 \right) \right\} \\
$$

The biggest downside of using custom paired delimiters is having to remember to
add the `*`, otherwise, the delimiters will not auto-resize. This is pretty unfortunate
as it still makes it error-prone. There is a [proposed
solution](https://tex.stackexchange.com/questions/1742/automatic-left-and-right-commands/1744#1744)
floating around on StackExchange that relies on a custom command that makes auto-resizing
the default, but it's still a far cry from a parsimonious solution.

#### Non-breaking lines
Expressions which are logically a single unit should stay on the same line, instead
of being split apart mid-sentence. Cue the following bad example from another paper:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/nbsp.png"
    width="300px"
    class="z-depth-1"
    caption="Expressions that are broken apart"
%}

In the area marked in red, we had the expression that was defining $$\tau^i$$
get cut in half, which is very jarring visually and interrupts the reader's
train of thought.

To ensure that expressions do not get split, simply wrap it around in curly braces.
For instance, 

{% highlight latex %}
\tau=\left(s_1, a_1, \ldots, a_{t-1}, s_t\right)
{% endhighlight %}

would be wrapped by `{` and `}` on both sides and become


{% highlight latex %}
{ \tau=\left(s_1, a_1, \ldots, a_{t-1}, s_t\right) }
{% endhighlight %}

So if we render the following snippet, which would otherwise have expressions
split in half without the wrapped curly braces:

{% highlight latex %}
We denote the historical trajectory as 
${ \tau=\left(s_1, a_1, \ldots, a_{t-1}, s_t\right) }$
and action-observation history $(\mathrm{AOH})$ for
player $i$ as 
${ \tau^i=\left(\Omega^i\left(s_1\right), a_1, \ldots, a_{t-1}, \Omega^i\left(s_t\right)\right) }$,
 which encodes the trajectory from player $i$ 's point of view.
{% endhighlight %}

we get the following positive result where there is additional whitespace between
the justified text on the first line, to compensate for the expression assigning $$\tau$$
to stay on the same line:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/nbsp-positive.png"
    width="300px"
    class="z-depth-1"
    caption="Expressions that brace together stays together"
%}

#### Expressions Should Be Punctuated Like Sentences
Your document is meant to be read, and it should follow the rules and structures
of English (or whichever language you are writing in). This means that
mathematical expressions should also be punctuated appropriately, which
allows it to flow more naturally and make it easier for the reader to follow.

Consider the following example that does not use punctuation:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/sentence-negative.png"
    width="400px"
    class="z-depth-1"
    caption="Expressions which are not punctuated are tiring to read"
%}

In the region highlighted in red, the expressions do not carry any punctuation at all,
and by the end of the last equation (Equation 15), I am almost out of breathe trying
to process all of the information. In addition, it does not end in a full stop, which
does not give me an affordance to take a break, which makes it a very tiring read mentally.

Instead, commas should be added after each expression where the expression does not terminate,
and the final equation should be ended by a full stop. Here is a good example of punctuation
that helps to guide the reader along the author's train of thought:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/sentence-multiline.png"
    width="400px"
    class="z-depth-1"
    caption="Appropriate use of commas and full stop to guide the reader"
%}

Here is another good example of how using commas for the equations 
allow the text to flow naturally, where it takes the form of
"analogously, observe that we have [foo] and [bar], where the inequality...":

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/sentence-two-exp.png"
    width="400px"
    class="z-depth-1"
    caption="Punctuation allows the content to flow naturally"
%}

This even extends to when you pack several equations on a single line, which
is common when you are trying to fit the page limit for conference submissions:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/sentence-singleline.png"
    width="400px"
    class="z-depth-1"
    caption="Appropriate use of punctuation when multiple equations are on a single line"
%}

#### The `proof` environment
The `proof` environment from the `amsthm` package is great for signposting to your readers
where a proof starts and ends. For instance, consider how it is used in the following example:

{% highlight latex %}
\textit{Problem: Show that if $(x_n)_n$ converges to $x$ in the usual sense, then
$\lim_{n \to \infty} x_n = \lim_{\mathcal{F}} x_n$.}

Suppose that $(x_n)_n$ converges to $x$. We show that this $x$ is also the
$\mathcal{F}$-limit of $(x_n)_n$.

\begin{proof}
    Take any $\varepsilon$. Then we know that for some large enough $N$, if $n \geq N$, then
    $x_n \in B_\varepsilon(x)$. Since every non-principal ultrafilter on $\N$ contains
    $\mathcal{F}_\infty$, then $\mathcal{F}$ also contains $ \left\{ n : n \geq N \right\} $,
    since the complement is finite. Therefore since filters are closed upwards, any
    sequence items $x_n$ with $n < N$ that happen to fall in the ball around $x$,
    i.e, $x_n \in B_\varepsilon(x)$
    is also contained in some filter element, so 
    $\left\{  n \in \N : \lvert x_n - x \rvert < \varepsilon \right\} \in \mathcal{F}$,
    as desired.
\end{proof}
{% endhighlight %}

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/proof.png"
    width="600px"
    class="z-depth-1"
    caption="Signposting using the `proof` environment"
%}

This will helpfully highlight the start of your argument with *"Proof"*, and
terminate it with a square that symbolizes QED.

#### Terminate Proofs with Explicit `\qedhere`

Consider the same example as previously, but now you accidentally added an additional
newline before the closing `\end{proof}`, which happens pretty often:

{% highlight latex %}
% Same as previously, contents elided for brevity
\begin{proof}
    % Same as previously, contents elided for brevity
    $x_n \in B_\varepsilon(x)$
    is also contained in some filter element, so 
    $\left\{  n \in \N : \lvert x_n - x \rvert < \varepsilon \right\} \in \mathcal{F}$,
    as desired.

    % Extra newline here!
\end{proof}
{% endhighlight %}

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/qedhere.png"
    width="600px"
    class="z-depth-1"
    caption="Misaligned QED symbol"
%}

This results in the above scenario, where the QED symbol now appears on the next line by itself,
which throws the entire text off-balance visually. To avoid such things happening,
always include an explicit `\qedhere` marker at the end of your proof, which would cause it
to always appear on the line that it appears after:

{% highlight latex %}
% Same as previously, contents elided for brevity
\begin{proof}
    % Same as previously, contents elided for brevity
    $x_n \in B_\varepsilon(x)$
    is also contained in some filter element, so 
    $\left\{  n \in \N : \lvert x_n - x \rvert < \varepsilon \right\} \in \mathcal{F}$,
    as desired. \qedhere % Always add \qedhere once you are done!

    % Extra newline here!
\end{proof}
{% endhighlight %}

We would then get the same result as before originally, when we did not have the extra newline.

#### Spacing
Spacing matters a lot in readability, as it helps to separate logical components.
For instance, the following example fails to add spacing before the differential
of the variable $$dz$$:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/integral.png"
    width="500px"
    class="z-depth-1"
    caption='Lack of spacing before "dz"'
%}

This might seem innocuous, but consider the following example that makes the issue more explicit:

{% highlight latex %}
P(X) = \int xyz dx
{% endhighlight %}

$$P(X) = \int xyz dx$$

Now we can really see that the quantities are running into each other, and it
becomes hard to interpret. Instead, we can add math-mode spacing, summarized in
the following table:

| Spacing Expression | Type        |
|--------------------|-------------|
| `\;`               | Thick space |
| `\:`               | Medium space |
| `\,`               | Thin space |
{: .table .table-bordered .table-sm }

So our new expression now looks like

{% highlight latex %}
P(X) = \int xyz \, dx
{% endhighlight %}

$$P(X) = \int xyz \, dx,$$

which is much more readable.

#### `align*` Environment for Multiline Equations

#### Double quotes
This is more of a rookie mistake since it's visually very obvious something is
wrong. Double quotes don't work the way you would expect:

{% highlight latex %}
\text{"Hello World!"}
{% endhighlight %}

$$\text{"Hello World!"}$$

Instead, surround them in double backticks and single quotes, which is 
supposed to be reminiscent of the directional strokes of an actual double quote.
This allows it to know which side to orient the ticks:

{% highlight latex %}
\text{``Hello World!''}
{% endhighlight %}

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/quotes.png"
    width="100px"
    class="z-depth-1"
    caption="Output of correct usage of quotes"
%}

Unfortunately I had to demonstrate this with a screenshot since MathJax only
performs math-mode typesetting, but this is an instance of text-mode typesetting.

#### Epsilons
This is a common mistake due to laziness. Many times, people use `\epsilon` ($$\epsilon$$)
when they really meant to write `\varepsilon` ($$\varepsilon$$). For instance, in analysis
this is usually the case, and therefore writing `\epsilon` results in a very uncomfortable
read:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/epsilon-wrong.png"
    width="600px"
    class="z-depth-1"
    caption='Using "\epsilon" looks weird'
%}

Using `\varepsilon` makes the reader feel much more at peace:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/epsilon-right.png"
    width="600px"
    class="z-depth-1"
    caption='"\varepsilon" is usually what should be used'
%}

#### Sets: `mathbbm` Instead Of `mathbb`
For sets like $$\mathbb{N}$$, you should use `\mathbbm{N}` instead of `mathbb{N}`. See the
difference for yourself, using the same example as the previous section:

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/mathbbm.png"
    width="600px"
    class="z-depth-1"
    caption='Use `mathbbm` instead of `mathbb`'
%}

`mathbbm` causes the symbols to be bolded, which is what you want.

#### Dots
`...`  and `\dots` are different. See the difference for yourself:

{% highlight latex %}
X = \left( X_1, ..., X_n \right)
X = \left( X_1, \dots, X_n \right)
{% endhighlight %}

{% include figure.html 
    path="/assets/img/posts/latex-mistakes/dots.png"
    width="300px"
    class="z-depth-1"
    caption='Output of "..." versus "\dots"'
%}

When using "...", the spacing between each dot, and between the final dot
and the comma character is wrong. Always use "\dots".

### Mid

### Angle Brackets

### Math Operators

### `\textnormal`

### Non-breaking space with `~`



$$
    Hello!
    \hfill \square
$$
