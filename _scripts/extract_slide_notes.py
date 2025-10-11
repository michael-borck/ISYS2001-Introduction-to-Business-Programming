import re
import os
import argparse
from pathlib import Path

def extract_slide_notes(input_file, output_folder):
    with open(input_file, 'r') as file:
        content = file.read()

    slides = re.split(r'\n#', content)

    # Counter for slides with notes
    note_number = 0

    for slide in slides:
        lines = slide.strip().split('\n')
        if lines:
            title = lines[0].strip()

            # Special handling for 'Today' slide
            if title.lower() == 'today':
                title = 'Overview'
                slide = slide.replace('Today', 'Overview').replace("today's", "Overview's")

            notes_match = re.search(r'::: \{\.notes\}(.*?):::', slide, re.DOTALL)
            if notes_match:
                note_number += 1
                notes = notes_match.group(1).strip()

                # Create filename with numbered prefix
                filename = f"{note_number:02d}_{title.lower().replace(' ', '_')}.md"

                # Replace 'Slide' with 'Lesson' and 'slide' with 'lesson'
                notes = notes.replace('Slide', 'Lesson').replace('slide', 'lesson')

                # Replace "in Today's presentation" or "in Overview's presentation" with "in this lesson"
                notes = re.sub(r"in (Today's|Overview's) presentation", "in this lesson", notes, flags=re.IGNORECASE)

                # Replace any remaining instances of 'Today' with 'Overview'
                notes = notes.replace('Today', 'Overview').replace('today', 'overview')

                # Create YAML front matter
                yaml_front_matter = f"""---
title: "{title}"
format:
  pdf:
      toc: false
      colorlinks: true
  docx:
      toc: false
      highlight-style: github
  html:
      toc: true
      toc-expand: 2
      embed-resources: true
---

"""

                output_path = Path(output_folder) / filename
                with open(output_path, 'w') as output_file:
                    output_file.write(yaml_front_matter + notes)
                print(f"Saved notes for '{title}' to {output_path}")
            else:
                print(f"No notes found for '{title}'")

def main():
    parser = argparse.ArgumentParser(description="Extract and number slides with notes from a markdown presentation, with special handling for 'Today' slide.")
    parser.add_argument("input_file", help="Path to the input markdown file")
    parser.add_argument("output_folder", help="Path to the output folder for extracted notes")
    args = parser.parse_args()

    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    extract_slide_notes(args.input_file, args.output_folder)

if __name__ == "__main__":
    main()
