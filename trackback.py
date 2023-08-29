import requests
import ipdb

# Your post's data
# data = {
#     'title': 'Paper Summary: Efficiently Modeling Long Sequences with Structured State Spaces',
#     'excerpt': 'The paper introduces the Structured State Space sequence model (S4) to address the computational challenges of existing models like Transformers for long-sequence tasks. Using the HiPPO matrix and a novel approach based on Normal Plus Low-Rank (NPLR) representation, the S4 model efficiently captures long-range dependencies, outperforming current state-of-the-art models.',
#     'url': 'https://fanpu.io/summaries/2023-08-25-efficiently-modeling-long-sequences-with-structured-state-spaces/',
#     'blog_name': 'ML Paper Summaries'
# }

data = {
    'title': 'Paper Summary: Dense Passage Retrieval for Open-Domain Question Answering',
    'url': 'https://fanpu.io/summaries/2023-08-10-dense-passage-retrieval-for-open-domain-question-answering/',
    'blog_name': 'ML Paper Summaries'
}

# The TrackBack URL from the post's front matter (or where you stored it)
arXiv_id = '2004.04906'
trackback_url = f'https://arxiv.org/trackback/{arXiv_id}'


response = requests.post(trackback_url, data=data)

if response.status_code == 200:
    print("TrackBack successful!")
else:
    print(f"TrackBack failed with status code: {response.status_code}")

print(response.content.decode())
ipdb.set_trace()

pass
pass
pass
