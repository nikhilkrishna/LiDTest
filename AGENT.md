# AGENT.md

## Project Overview
LiDTest is a Python tool for converting German history Q&A markdown content into GoCard flashcard format.

## Commands
- **Run conversion**: `python convert_to_go_card.py`
- **Setup**: `python -m venv .venv && source .venv/bin/activate`
- **Install deps**: `pip install -r requirements.txt` (if exists) or manually install as needed
- **Python version**: Check `.python-version` for required version

## Architecture
- **Main script**: `convert_to_go_card.py` - Converts Q&A format to GoCard flashcards
- **Input data**: `input_data/` - Contains source markdown files (Deutsche-Geschichte.md) and images
- **Output**: `GoCard/` - Generated flashcard files with YAML frontmatter
- **Input format**: Q&A blocks with tags (#WW2, #Politik, etc.) and Obsidian-style images

## Code Style
- Python 3.12+ required
- Standard imports: `import re, os, datetime`
- File encoding: UTF-8
- Regex patterns for parsing markdown structure
- YAML frontmatter for flashcard metadata
- Snake_case naming convention
- Strip whitespace from extracted content
