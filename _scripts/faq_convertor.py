import argparse
import os
import re
import html
import sys

# --- HTML Templates (Preserving Inline Styles) ---

HTML_HEAD_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    </head>
<body>
<h1 style="margin: 10px 20px; padding: 5px;">{title}</h1>
<div style="margin: 10px 20px; padding: 5px;">
"""

# Template for each FAQ item using <details> and <summary>
FAQ_ITEM_TEMPLATE = """<details style="margin-bottom: 15px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
<summary style="cursor: pointer; font-weight: bold; padding: 10px; background-color: #f9f9f9; border: 1px solid #ddd;">{question_text} <span style="font-weight: normal; margin-left: 5px;">[+]</span></summary>
<p style="margin: 10px 20px; padding: 5px;">{answer_text}</p>
</details>"""

HTML_FOOT_TEMPLATE = """</div>
</body>
</html>
"""

DEFAULT_TITLE = "FAQ - Please Provide a Title Using --title"

# --- Functions ---

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Convert a text file with numbered Q&A pairs into an HTML FAQ page.",
        formatter_class=argparse.RawDescriptionHelpFormatter # Nicer help text
    )
    parser.add_argument(
        "input_file",
        help="Path to the input text file (e.g., faq.txt)"
    )
    parser.add_argument(
        "-t", "--title",
        help="Optional title for the HTML page header and <title> tag."
    )
    return parser.parse_args()

def parse_faq_file(filename):
    """
    Parses the input text file to extract questions and answers.

    Args:
        filename (str): The path to the input text file.

    Returns:
        list: A list of dictionaries, where each dictionary has
              'question' and 'answer' keys. Returns an empty list
              if parsing fails or no Q&A pairs are found.
    """
    faqs = []
    current_question = None
    current_answer_lines = []
    # Regex to reliably find question lines (allows leading whitespace)
    # Captures the full question line including the number.
    question_pattern = re.compile(r"^\s*(\d+\.\s+.*)")

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                stripped_line = line.strip()
                match = question_pattern.match(line) # Match against original for ^

                if match:
                    # --- Found a new question ---
                    # 1. Save the previous Q&A pair if one exists
                    if current_question:
                        # Join collected answer lines with a space, trim final result
                        answer = ' '.join(current_answer_lines).strip()
                        # Replace multiple spaces resulting from joins/strips with single space
                        answer = re.sub(r'\s+', ' ', answer)
                        faqs.append({
                            'question': current_question.strip(),
                            'answer': answer
                        })

                    # 2. Start the new Q&A pair
                    current_question = match.group(1) # Get the captured question text
                    current_answer_lines = [] # Reset answer lines

                elif current_question and stripped_line:
                    # --- Found an answer line for the current question ---
                    # Add the non-empty, stripped line to the current answer
                    current_answer_lines.append(stripped_line)

                # Ignore blank lines when no question is active or between Q&A pairs

            # --- After the loop: Add the last Q&A pair ---
            if current_question:
                answer = ' '.join(current_answer_lines).strip()
                answer = re.sub(r'\s+', ' ', answer)
                faqs.append({
                    'question': current_question.strip(),
                    'answer': answer
                })

    except FileNotFoundError:
        print(f"Error: Input file '{filename}' not found.", file=sys.stderr)
        return [] # Return empty list on error
    except Exception as e:
        print(f"Error reading or parsing file '{filename}': {e}", file=sys.stderr)
        return [] # Return empty list on error

    return faqs

def generate_html(faqs, title):
    """
    Generates the full HTML content string.

    Args:
        faqs (list): The list of Q&A dictionaries.
        title (str): The title for the HTML page.

    Returns:
        str: The complete HTML document as a string.
    """
    # Escape the main title for safety
    safe_title = html.escape(title)
    html_content = HTML_HEAD_TEMPLATE.format(title=safe_title)

    # Build the FAQ items section
    for faq in faqs:
        # Escape question and answer text *before* inserting into template
        safe_question = html.escape(faq.get('question', ''))
        safe_answer = html.escape(faq.get('answer', ''))

        # Add line breaks <br> for newlines within the original answer if desired
        # safe_answer = safe_answer.replace('\n', '<br>\n') # Uncomment if needed

        html_content += FAQ_ITEM_TEMPLATE.format(
            question_text=safe_question,
            answer_text=safe_answer
        )

    html_content += HTML_FOOT_TEMPLATE
    return html_content

def main():
    """Main execution function."""
    args = parse_arguments()
    input_filename = args.input_file

    # Determine output filename
    base_name = os.path.splitext(input_filename)[0]
    output_filename = base_name + ".html"

    # Determine the page title
    page_title = args.title if args.title else DEFAULT_TITLE

    print(f"Reading FAQ data from: {input_filename}")
    faqs_data = parse_faq_file(input_filename)

    if not faqs_data:
        print("No valid Q&A pairs found or error reading file. Exiting.")
        sys.exit(1) # Exit with an error code

    print(f"Generating HTML content ({len(faqs_data)} questions)...")
    html_output = generate_html(faqs_data, page_title)

    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(html_output)
        print(f"Successfully generated HTML file: {output_filename}")
    except IOError as e:
        print(f"Error writing HTML file '{output_filename}': {e}", file=sys.stderr)
        sys.exit(1) # Exit with an error code
    except Exception as e:
        print(f"An unexpected error occurred during file writing: {e}", file=sys.stderr)
        sys.exit(1) # Exit with an error code

# --- Main execution block ---
if __name__ == "__main__":
    main()