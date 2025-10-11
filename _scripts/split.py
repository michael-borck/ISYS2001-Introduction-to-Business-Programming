import re
import os

def split_quarto_markdown(input_file):
    front_matter = """---
title: "[TITLE]"
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

    with open(input_file, 'r') as f:
        content = f.read()

    lines = content.split('\n')
    current_file = None
    current_content = ""
    in_code_block = False

    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block

        if line.startswith('#') and not in_code_block:
            words = line.split()
            if len(words) > 1 and words[1].lower() != 'example':
                if current_file:
                    with open(current_file, 'w') as f:
                        f.write(current_content)

                # Extract title and create filename
                title = ' '.join(words[1:])
                filename = "_".join(title.lower().split()) + ".md"
                
                # Prepare content for the new file
                current_file = filename
                current_content = front_matter.replace("[TITLE]", title) + "\n" + line + "\n"
            else:
                current_content += line + "\n"
        else:
            current_content += line + "\n"

    # Write the last file
    if current_file:
        with open(current_file, 'w') as f:
            f.write(current_content)

if __name__ == "__main__":
    input_file = input("Enter the path to the Quarto markdown file: ")
    split_quarto_markdown(input_file)
    print("Splitting complete. Check the current directory for the output files.")
