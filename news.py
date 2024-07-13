import argparse
import re
from datetime import date

# title can contain spaces, caps
def filename(title, today):
    title = title.lower()
    title = title.replace(" ", "-")
    title = title.replace(",", "")
    title = title.replace(":", "")
    title = title.strip()
    title = re.sub("-+", "-", title)
    title = ''.join(e for e in title if e.isalnum() or e == "-")
    filepath = f"_news/{today}-{title}.md"
    print("News file created at", filepath)
    return filepath

def news_template(today):
    return f"""---
layout: post
date: {today}
inline: true
---

<add text here>
"""

def main():
    parser = argparse.ArgumentParser(description='Create summary template from arxiv ID')
    parser.add_argument('title', type=str,
                        help='News title')
    parser.add_argument('--date', required=False)
    args = parser.parse_args()

    today = args.date
    if today is None:
        today = date.today()

    filepath = filename(args.title, today)
    with open(filepath, "w") as f:
        f.write(news_template(today))

if __name__ == "__main__":
    main()