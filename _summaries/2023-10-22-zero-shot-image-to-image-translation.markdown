---
layout: summary
title: "Zero-shot Image-to-Image Translation"
giscus_comments: true
bib_id: 2302.03027v1
---

### Three Important Things

#### 1. pix2pix-zero

The authors tackle the problem of ensuring faithfulness to the original source
image in image-to-image translation driven by diffusion models. The difficulty
of image-to-image translation is that while we specify the edits that we want
(i.e changing a dog in the scene to a cat), we do not specify what we want to
preserve, which is implicit.

They come up with a technique that they call `pix2pix-zero`, which 
is training-free and prompt-free. Training-free means that it
does not require any fine-tuning on existing diffusion models, 
and prompt-free means that the user does not have to specify a prompt, 
but simply only the desired changes from the source domain to the
target domain, i.e cat -> dog.

Samples of their results:

{% include figure.html
    path="/assets/img/summaries/pix2pix-zero-results.webp"
    width="600px"
    class="z-depth-1"
%}

Their approach consists of two main contributions:
1. An efficient, automatic editing direction discovery mechanism without input
text prompting,
2. Content preservation via cross-attention guidance.

The two techniques are discussed in the following sections.

#### 2. Discovering Edit Directions

Given just a textual description of the edit (i.e cat -> dog), the first problem
is how we can translate this to a direction in embedding space.

To do this, they used GPT-3 to generate two groups of a large number of diverse
sentences: one containing the source text, and one containing the target text.
They then took the average CLIP embeddings of each group, and took their
difference as the edit direction to use. They found that this approach of taking
the mean CLIP embedding of many sentences containing the word instead of just
the embedding of the word itself to be more robust.

The following diagram summarizes the process:

{% include figure.html
    path="/assets/img/summaries/pix2pix-zero-directions.webp"
    width="600px"
    class="z-depth-1"
%}

Computing the edit directions takes about 5 seconds, and only
needs to be performed once for each source-target edit pair.

#### 3. Editing via Cross-Attention Guidance

They base their image generation model off Stable Diffusion, 
which is a latent diffusion model. The Stable Diffusion
generation process allows conditioning on an input text,
which is converted into a text embedding $$c$$. This conditioning
is performed by the attention mechanism:

$$\operatorname{Attention}(Q, K, V)=M \cdot V,$$

where $$M=\operatorname{Softmax}\left(\frac{Q K^T}{\sqrt{d}}\right)$$ with:

- $$\varphi(x_t)$$ being the intermediate features from the denoising UNet,
- $$c$$ being the text embedding obtained via BLIP from the input image,
- $$W_Q, W_K, W_V$$ being learnt projections,
- Query $$Q = W_Q \varphi(x_t)$$ being applied on the spatial features,
- Key $$K = W_K c$$ and value $$V = W_V c$$ being applied on the text embeddings.

Intuitively, $$M_{i,j}$$ is the importance of the $$j$$th text token to the
$$i$$th spatial location. Note that $$M$$ actually depends on the time step
$$t$$ due to its dependence on $$x_t$$, so we have different attention maps for
each time step.

{% include figure.html
    path="/assets/img/summaries/pix2pix-zero-attention.webp"
    width="600px"
    class="z-depth-1"
%}


### Most Glaring Deficiency

### Conclusions for Future Work
