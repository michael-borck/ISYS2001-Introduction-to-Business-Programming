import os
import re

def replace_spelling(content):
    # Define common American to British/Australian spelling replacements
    replacements = {
        r'\b(analyz)(e|es|ed|ing)\b': r'analys\2',
        r'\b(organize)(s|d|ing|r)?\b': r'organise\2',
        r'\b(realize)(s|d|ing)?\b': r'realise\2',
        r'\b(recognize)(s|d|ing)?\b': r'recognise\2',
        r'\b(color)\b': r'colour',
        r'\b(favor)\b': r'favour',
        r'\b(honor)\b': r'honour',
        r'\b(behavior)\b': r'behaviour',
        r'\b(labor)\b': r'labour',
        r'\b(neighbor)\b': r'neighbour',
        r'\b(theater)\b': r'theatre',
        r'\b(center)\b': r'centre',
    }

    def preserve_case(match):
        word = match.group()
        replacement = replacements[match.re.pattern]
        if word.isupper():
            return replacement.upper()
        elif word[0].isupper():
            return replacement.capitalize()
        return replacement

    # Perform replacements
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, lambda match: preserve_case(match), content, flags=re.IGNORECASE)
    return content

def process_markdown_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Replace American spelling with British/Australian spelling
                updated_content = replace_spelling(content)

                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"Processed: {file_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python convert_spelling.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    process_markdown_files(directory)
    print("Spelling conversion completed.")
