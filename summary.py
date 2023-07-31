import argparse
from arxiv2bib import arxiv2bib
from datetime import date

def retrieve_arxiv_bib(id):
    return arxiv2bib([id])[0]

# title can contain spaces, caps
def filename(title):
    today = date.today()
    title = title.lower()
    title = title.replace(" ", "-")
    return f"_summaries/{today}-{title}.markdown"

def template(title, bib_id):
    return \
f"""---
layout: summary
title: {title}
giscus_comments: true
bib_id: {bib_id}
---

### Three Important Things

#### 1. Foo

#### 2. Bar

#### 3. Baz

### Most Glaring Deficiency

### Conclusions for Future Work
"""

def create_summary_template(title, bib_id):
    filepath = filename(title)

    with open(filepath, "w") as f:
        f.write(template(title, bib_id))

    print(f"New summary template created at {filepath}")

def update_summary_bib(bibtex):
    with open("_bibliography/summaries.bib", "a") as f:
        f.write("\n\n")
        f.write(bibtex)
    
    print("Updated _bibliography/summaries.bib with")
    print(bibtex)

def main():
    parser = argparse.ArgumentParser(description='Create summary template from arxiv ID')
    parser.add_argument('arxiv_id', type=str,
                        help='arXiv article ID')
    args = parser.parse_args()

    bib = retrieve_arxiv_bib(args.arxiv_id)
    title = bib.title
    bib_id = bib.id

    create_summary_template(title, bib_id)
    update_summary_bib(bib.bibtex())


if __name__ == "__main__":
    main()