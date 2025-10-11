import sys
import os
import re
import requests
import json
import yaml
import logging
from datetime import date
import argparse

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def anthropic_api_call(messages):
    api_url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
        "anthropic-version": "2023-06-01",
    }
    data = {"model": "claude-3-opus-20240229", "max_tokens": 4000, "messages": messages}

    logger.debug(f"API Request URL: {api_url}")
    logger.debug(f"API Request Headers: {json.dumps(headers, indent=2)}")
    logger.debug(f"API Request Data: {json.dumps(data, indent=2)}")

    try:
        response = requests.post(api_url, headers=headers, json=data)
        logger.debug(f"API Response Status Code: {response.status_code}")
        logger.debug(
            f"API Response Headers: {json.dumps(dict(response.headers), indent=2)}"
        )
        logger.debug(f"API Response Content: {response.text}")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"API call failed: {str(e)}")
        raise


def generate_exciting_topic(topic, description=None):
    logger.info(f"Generating exciting topic for '{topic}'")
    prompt = f"Given the topic '{topic}'"
    if description:
        prompt += f" and the following description: '{description}'"
    prompt += ", create a more exciting and catchy title for a presentation, no more than 8 words long."

    messages = [{"role": "user", "content": prompt}]
    try:
        response = anthropic_api_call(messages)
        exciting_topic = response["content"][0]["text"].strip('" ')
        logger.info(f"Generated exciting topic: '{exciting_topic}'")
        return exciting_topic
    except Exception as e:
        logger.error(f"Error generating exciting topic: {str(e)}")
        raise


def generate_slidedeck(topic, description=None):
    logger.info(f"Generating slidedeck content for '{topic}'")
    prompt = f"""Create a 30-slide presentation on the topic of {topic}."""
    if description:
        prompt += f" Consider this additional context: {description}"
    prompt += """ Follow these rules:
- This is for a Quarto markdown presentation, so each new slide starts with a single '#' for the title.
- Do not include slide numbers in the titles or content.
- No more than 5 bullet points per slide
- No more than 5 words per bullet point
- Each slide should take no more than 5 minutes to present
- Include an agenda slide and a summary/conclusion slide
- Follow the structure: tell them what you're going to tell them (agenda), tell them (main content), tell them what you told them (summary)
- Do not create a title slide
- Output in markdown format
- Use Australian-British spelling

Start with the agenda slide and end with the summary/conclusion slide."""

    messages = [{"role": "user", "content": prompt}]

    try:
        response = anthropic_api_call(messages)
        content = response["content"][0]["text"].strip()
        tokens = response["usage"]["output_tokens"] + response["usage"]["input_tokens"]
        logger.info(f"Slidedeck content generated successfully. Tokens used: {tokens}")
        return content, tokens
    except Exception as e:
        logger.error(f"Error generating slidedeck content: {str(e)}")
        raise


def post_process_content(content):
    # Remove any remaining "Slide X:" from the beginning of lines
    content = re.sub(r"^Slide \d+:\s*", "", content, flags=re.MULTILINE)

    # Ensure each slide title starts with a single '#'
    content = re.sub(r"^##\s+", "# ", content, flags=re.MULTILINE)

    return content


def create_markdown_file(output_folder, topic, exciting_topic, content):
    filename = f"{topic.lower().replace(' ', '_')}.md"
    filepath = os.path.join(output_folder, filename)
    logger.info(f"Creating markdown file: {filepath}")

    frontmatter = {
        "title": exciting_topic,
        "author": "Michael Borck",
        "format": {
            "pptx": {"reference-doc": "../../_assets/template.pptx"},
            "pdf": {"toc": False, "colorlinks": True},
            "docx": {"toc": False, "highlight-style": "github"},
            "html": {"toc": True, "toc-expand": 2, "embed-resources": True},
        },
    }

    try:
        os.makedirs(output_folder, exist_ok=True)
        with open(filepath, "w") as f:
            f.write("---\n")
            yaml.dump(frontmatter, f, default_flow_style=False)
            f.write("---\n\n")
            f.write("# Copyright\n![](../../_assets/curtin-copy-right.png)\n\n")
            f.write("# Acknowledgement of Country\n")
            f.write(
                "I acknowledge the traditional custodians of the land on which I work and live,\n"
            )
            f.write(
                "and recognise their continuing connection to land, water and community. I pay\n"
            )
            f.write("respect to elders past, present and emerging.\n\n")
            f.write("![](../../_assets/ack_country.png)\n\n")
            f.write(content)
        logger.info(f"Markdown file created successfully: {filepath}")
    except Exception as e:
        logger.error(f"Error creating markdown file: {str(e)}")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Generate a slidedeck on a given topic."
    )
    parser.add_argument("topic", help="The main topic of the slidedeck")
    parser.add_argument(
        "-d", "--description", help="Optional description or context for the topic"
    )
    parser.add_argument(
        "-o",
        "--output",
        default=".",
        help="Output folder for the generated markdown file",
    )
    args = parser.parse_args()

    logger.info("Starting slidedeck generation process")
    logger.info(f"Topic received: '{args.topic}'")
    if args.description:
        logger.info(f"Description: '{args.description}'")
    logger.info(f"Output folder: '{args.output}'")

    try:
        exciting_topic = generate_exciting_topic(args.topic, args.description)
        content, tokens = generate_slidedeck(args.topic, args.description)
        content = post_process_content(content)
        create_markdown_file(args.output, args.topic, exciting_topic, content)

        cost_per_1k_tokens = 0.015  # Assuming $0.015 per 1K tokens for Claude 3 Opus
        total_cost = (tokens / 1000) * cost_per_1k_tokens

        logger.info(f"Slidedeck generated successfully!")
        logger.info(f"Tokens used: {tokens}")
        logger.info(f"Estimated cost: ${total_cost:.4f}")

        print(f"Slidedeck generated successfully!")
        print(f"Tokens used: {tokens}")
        print(f"Estimated cost: ${total_cost:.4f}")
    except Exception as e:
        logger.error(
            f"An error occurred during the slidedeck generation process: {str(e)}"
        )
        print(f"An error occurred. Please check the log file for details.")
        sys.exit(1)


if __name__ == "__main__":
    main()
