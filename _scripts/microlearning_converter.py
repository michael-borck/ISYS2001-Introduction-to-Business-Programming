import os
import re
import json
import requests
import logging
from datetime import datetime
import argparse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# API configuration
API_URL = "https://api.anthropic.com/v1/messages"
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
HEADERS = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
    "anthropic-version": "2023-06-01",
}


def extract_yaml_front_matter(content):
    yaml_match = re.search(r"^---\s*\n(.+?)\n---\s*\n", content, re.DOTALL)
    if yaml_match:
        return yaml_match.group(0)
    return ""


def extract_content(markdown_content):
    # Extract title
    title_match = re.search(r'title:\s*"(.+)"', markdown_content)
    title = title_match.group(1) if title_match else "Untitled"

    # Extract aim
    aim_match = re.search(r"\*\*Aim\*\*(.*?)(?=\*\*)", markdown_content, re.DOTALL)
    aim = aim_match.group(1).strip() if aim_match else ""

    # Extract context
    context_match = re.search(
        r"\*\*Context\*\*(.*?)(?=\*\*)", markdown_content, re.DOTALL
    )
    context = context_match.group(1).strip() if context_match else ""

    # Extract main content
    main_content = re.sub(r"---.*?---", "", markdown_content, flags=re.DOTALL)
    main_content = re.sub(
        r"\*\*Aim\*\*.*?\*\*Context\*\*.*?(?=\*\*)", "", main_content, flags=re.DOTALL
    )
    main_content = main_content.strip()

    return title, aim, context, main_content


def extract_json_from_text(text):
    json_match = re.search(r"\{.*\}", text, re.DOTALL)
    if json_match:
        return json_match.group(0)
    return None


def generate_missing_sections(title, aim, context, main_content):
    prompt = f"""
    Given the following content from a lesson, please generate the missing sections for a micro-learning markdown file:

    Title: {title}
    Aim: {aim}
    Context: {context}
    Main Content: {main_content}

    Please provide the following sections:
    1. Learning Objectives (2-3 specific, measurable goals)
    2. Key Takeaways (3-5 bullet points summarizing main points)
    3. Quick Quiz (2-3 questions to reinforce learning)
    4. Additional Resources (2-3 links or references for further learning)

    Format the response as a JSON object with keys: "learning_objectives", "key_takeaways", "quick_quiz", and "additional_resources".
    Do not include any explanatory text before or after the JSON object.
    """

    data = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=data)
        response.raise_for_status()

        response_data = response.json()

        if "content" not in response_data or not response_data["content"]:
            logger.error("Unexpected API response structure. 'content' not found.")
            logger.error(f"Full API response: {json.dumps(response_data, indent=2)}")
            return None, 0, 0

        generated_text = response_data["content"][0]["text"]

        # Extract JSON from the generated text
        json_text = extract_json_from_text(generated_text)
        if json_text is None:
            logger.error("Failed to extract JSON from the generated text.")
            logger.error(f"Generated text: {generated_text}")
            return None, 0, 0

        try:
            generated_sections = json.loads(json_text)
        except json.JSONDecodeError as json_err:
            logger.error(f"Failed to parse extracted JSON: {json_err}")
            logger.error(f"Extracted JSON text: {json_text}")
            return None, 0, 0

        input_tokens = response_data["usage"]["input_tokens"]
        output_tokens = response_data["usage"]["output_tokens"]

        return generated_sections, input_tokens, output_tokens
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making request: {e}")
        if hasattr(e, "response"):
            logger.error(f"Response Status Code: {e.response.status_code}")
            logger.error(
                f"Response Headers: {json.dumps(dict(e.response.headers), indent=2)}"
            )
            logger.error(f"Response Content: {e.response.text}")
        return None, 0, 0


def format_list(items):
    return "\n".join(f"- {item}" for item in items)


def format_quiz(quiz_items):
    formatted_quiz = ""
    for i, item in enumerate(quiz_items, 1):
        if isinstance(item, dict):
            question = item.get('question', 'No question provided')
            answer = item.get('answer', 'No answer provided')
        elif isinstance(item, str):
            question = item
            answer = "Answer not provided"
        else:
            logger.warning(f"Unexpected format for quiz item: {item}")
            continue
        
        formatted_quiz += f"{i}. {question}\n   Answer: {answer}\n\n"
    return formatted_quiz.strip()

def format_additional_resources(resources):
    formatted_resources = []
    for item in resources:
        if isinstance(item, dict):
            formatted_resources.append(f"{item['title']}: {item['url']}")
        elif isinstance(item, str):
            formatted_resources.append(item)
        else:
            logger.warning(f"Unexpected format for additional resource: {item}")
    return format_list(formatted_resources)


def create_microlearning_markdown(
    title, aim, context, main_content, generated_sections, yaml_front_matter
):
    current_date = datetime.now().strftime("%Y-%m-%d")

    markdown = f"""{yaml_front_matter}
**Learning Objectives**

{format_list(generated_sections.get('learning_objectives', ['No learning objectives provided']))}

**Introduction**

{context}

{main_content}

**Key Takeaways**

{format_list(generated_sections.get('key_takeaways', ['No key takeaways provided']))}

**Quick Quiz**

{format_quiz(generated_sections.get('quick_quiz', ['No quiz questions provided']))}

**Additional Resources**

{format_additional_resources(generated_sections.get('additional_resources', ['No additional resources provided']))}

*Created on: {current_date}*
"""
    return markdown


def process_file(input_file, output_folder):
    with open(input_file, 'r') as file:
        content = file.read()

    yaml_front_matter = extract_yaml_front_matter(content)
    title, aim, context, main_content = extract_content(content)
    generated_sections, input_tokens, output_tokens = generate_missing_sections(title, aim, context, main_content)

    if generated_sections:
        try:
            microlearning_md = create_microlearning_markdown(
                title, aim, context, main_content, generated_sections, yaml_front_matter
            )

            output_file = os.path.join(output_folder, f"microlearning_{os.path.basename(input_file)}")
            with open(output_file, 'w') as file:
                file.write(microlearning_md)

            return output_file, len(content), input_tokens, output_tokens
        except Exception as e:
            logger.error(f"Error creating microlearning markdown for {input_file}: {str(e)}")
            return None, len(content), input_tokens, output_tokens
    else:
        logger.error(f"Failed to generate missing sections for {input_file}.")
        return None, len(content), 0, 0


def calculate_cost(input_tokens, output_tokens):
    input_cost = (input_tokens / 1000) * 0.015  # $0.015 per 1K tokens for input
    output_cost = (output_tokens / 1000) * 0.075  # $0.075 per 1K tokens for output
    total_cost = input_cost + output_cost
    return input_cost, output_cost, total_cost


def main():
    parser = argparse.ArgumentParser(description="Process markdown files for microlearning.")
    parser.add_argument("input_folder", help="Path to the input folder containing .md and .qmd files")
    parser.add_argument("output_folder", help="Path to the output folder for processed files")
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    total_input_tokens = 0
    total_output_tokens = 0
    total_files_processed = 0
    total_files_failed = 0

    for filename in os.listdir(input_folder):
        if filename.endswith(('.md', '.qmd')):
            input_file = os.path.join(input_folder, filename)
            logger.info(f"Processing file: {input_file}")

            output_file, input_file_tokens, api_input_tokens, api_output_tokens = process_file(input_file, output_folder)

            if output_file:
                total_input_tokens += api_input_tokens
                total_output_tokens += api_output_tokens
                total_files_processed += 1

                logger.info(f"Processed: {input_file}")
                logger.info(f"Output: {output_file}")
                logger.info(f"Input file tokens: {input_file_tokens}")
                logger.info(f"API input tokens: {api_input_tokens}")
                logger.info(f"API output tokens: {api_output_tokens}")
            else:
                total_files_failed += 1

    total_tokens = total_input_tokens + total_output_tokens
    input_cost, output_cost, total_cost = calculate_cost(total_input_tokens, total_output_tokens)

    logger.info(f"\nProcessing complete.")
    logger.info(f"Total files processed: {total_files_processed}")
    logger.info(f"Total files failed: {total_files_failed}")
    logger.info(f"Total API input tokens: {total_input_tokens}")
    logger.info(f"Total API output tokens: {total_output_tokens}")
    logger.info(f"Total API tokens: {total_tokens}")
    logger.info(f"Total input cost: ${input_cost:.4f}")
    logger.info(f"Total output cost: ${output_cost:.4f}")
    logger.info(f"Total cost: ${total_cost:.4f}")

if __name__ == "__main__":
    main()