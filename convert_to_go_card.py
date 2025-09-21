import re
import os
from datetime import datetime


# Path to your input markdown file
input_file = "Deutsche-Geschichte.md"

# Output directory for GoCard flashcards
output_dir = "GoCard"
os.makedirs(output_dir, exist_ok=True)

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Regex to match each Q&A block
pattern = re.compile(
    r"^##\s*(\d+):\s*(.*?)\n###\s*A:\s*(.*?)\n(.*?)(?=\n---|\Z)",
    re.DOTALL | re.MULTILINE,
)

# Extract tags (e.g. #Politics #Easy)
tag_pattern = re.compile(r"#([\w-]+)")

# Extract Obsidian-style image references (e.g. ![[image.png]])
image_pattern = re.compile(r"!\[\[(.*?)\]\]")

for match in pattern.finditer(content):
    qnum, question, answer, rest = match.groups()

    # Extract tags from the rest block (and remove duplicates)
    tags = list(dict.fromkeys(tag_pattern.findall(rest)))

    # Also check question and answer for tags, just in case
    tags += [t for t in tag_pattern.findall(question + answer) if t not in tags]

    # Extract images from the whole block
    images = image_pattern.findall(question + answer + rest)

    # YAML frontmatter for GoCard
    frontmatter = [
        "---",
        f"tags: [{', '.join(tags)}]",
        f"created: {datetime.now().date()}",
        "review_interval: 0",
        "---",
    ]
    title = f"Question {qnum}"

    # Form the output directory
    md = "\n".join(frontmatter)
    md += f"\n\n# {title}\n\n## Question\n\n{question.strip()}\n\n## Answer\n\n{answer.strip()}\n"
    for img in images:
        md += f"\n![]({img})\n"

    # Write each card as a separate markdown file
    filename = os.path.join(output_dir, f"question_{qnum}.md")
    with open(filename, "w", encoding="utf-8") as out:
        out.write(md)

print("Conversion complete. Check the GoCard directory for output files.")
