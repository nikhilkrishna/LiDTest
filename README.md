# LiDTest

A Python tool for converting German Living in Deutschland (LiD) Q&A markdown content into GoCard flashcard format.
Use the GoCard TUI (<https://github.com/DavidMiserak/GoCard>) to display the Output flashcards.

## Features

- Converts structured Q&A markdown files into individual GoCard flashcards
- Preserves tags and metadata from source content
- Supports Obsidian-style image references
- Generates YAML frontmatter for each flashcard
- Handles German language content with proper encoding

## Requirements

- Python 3.12+
- uv
- GoCard (<https://github.com/DavidMiserak/GoCard>)

## Setup

### Using uv (Recommended)

1. Install uv if you haven't already:

  ```bash
   
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
  ```

2. Clone the repository:

  ```bash

   git clone <repository-url>
   cd LiDTest
   
  ```

3. Create and activate virtual environment:

   ```bash
   
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   
   ```

## Usage

1. Place your LiDTest Q&A markdown file in the `input_data/` directory as `Deutsche-Geschichte.md`

2. Run the conversion:

   ```bash

  python convert_to_go_card.py
  
  ```

3. Find the generated GoCard flashcards in the `GoCard/` directory

## Input Format

The input markdown should follow this structure:

```markdown
## 001: Question text here?
### A: Answer text here
#Tag1 #Tag2 #Tag3

---
## 002: Next question?
### A: Next answer
#Tag1 #Tag4
```

## Output Format

Each question generates a separate markdown file with YAML frontmatter:

```markdown
---
tags: [Tag1, Tag2, Tag3]
created: 2025-06-16
review_interval: 0
---

# Question 001

## Question

Question text here?

## Answer

Answer text here
```

## How do I use the flash cards

The GoCard github repository has a TUI program that will take these generated flashcards and show them in the terminal.
You need to install it and point it at the output folder with the generated cards.

## What is pending

The biggest thing that is pending at this point is embedding the pictures.
