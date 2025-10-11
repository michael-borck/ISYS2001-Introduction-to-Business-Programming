import requests
import os
import logging
import json
import argparse
import sys

# Set up logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Define cost per 1000 tokens (as of current pricing)
INPUT_COST_PER_1K = 0.01  # $0.01 per 1K input tokens
OUTPUT_COST_PER_1K = 0.03  # $0.03 per 1K output tokens

# API keys
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY")
PIXABAY_API_KEY = os.environ.get("PIXABAY_API_KEY")


def calculate_cost(input_tokens, output_tokens):
    input_cost = (input_tokens / 1000) * INPUT_COST_PER_1K
    output_cost = (output_tokens / 1000) * OUTPUT_COST_PER_1K
    total_cost = input_cost + output_cost
    return input_cost, output_cost, total_cost


def extract_key_concepts(text):
    """
    Use Claude API to extract key concepts from the text.
    """
    prompt = f"""Extract 5 key concepts or entities from the following text.
    Each concept should be a single word or a short, specific phrase (2-3 words maximum).
    Focus on nouns and adjectives that represent important ideas, objects, or themes.
    Avoid generic words, articles, conjunctions, and prepositions.
    Provide only the list of concepts, with no additional explanation:

    {text}

    Key concepts:"""

    api_url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
    }
    data = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1000,
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()

        response_data = response.json()
        concepts = response_data["content"][0]["text"].strip().split("\n")
        # Clean up the concepts
        concepts = [
            concept.strip().strip("•-").strip()
            for concept in concepts
            if concept.strip()
        ]
        input_tokens = response_data["usage"]["input_tokens"]
        output_tokens = response_data["usage"]["output_tokens"]

        input_cost, output_cost, total_cost = calculate_cost(
            input_tokens, output_tokens
        )

        logger.info(
            f"Claude API call successful. Input tokens: {input_tokens}, Output tokens: {output_tokens}"
        )
        logger.info(
            f"Costs - Input: ${input_cost:.4f}, Output: ${output_cost:.4f}, Total: ${total_cost:.4f}"
        )

        return concepts, input_tokens, output_tokens, total_cost
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making request to Claude API: {e}")
        if hasattr(e, "response"):
            logger.error(f"Response Status Code: {e.response.status_code}")
            logger.error(
                f"Response Headers: {json.dumps(dict(e.response.headers), indent=2)}"
            )
            logger.error(f"Response Content: {e.response.text}")
        return [], 0, 0, 0


def get_image_url(keyword, api):
    """
    Get an image URL from Pexels or Pixabay API based on the keyword.
    """
    # Ensure keyword is not longer than 100 characters
    keyword = keyword[:100]

    if api == "pexels":
        url = f"https://api.pexels.com/v1/search?query={keyword}&per_page=1"
        headers = {"Authorization": PEXELS_API_KEY}
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            if data["photos"]:
                logger.info(
                    f"Successfully retrieved image URL from Pexels for keyword: {keyword}"
                )
                return data["photos"][0]["src"]["medium"]
            else:
                logger.warning(f"No images found on Pexels for keyword: {keyword}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting image URL from Pexels API: {e}")
    elif api == "pixabay":
        url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={keyword}&image_type=photo&per_page=3"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["hits"]:
                logger.info(
                    f"Successfully retrieved image URL from Pixabay for keyword: {keyword}"
                )
                return data["hits"][0]["webformatURL"]
            else:
                logger.warning(f"No images found on Pixabay for keyword: {keyword}")
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting image URL from Pixabay API: {e}")
    return None


def main(description):
    # Get key concepts from Claude
    concepts, input_tokens, output_tokens, total_cost = extract_key_concepts(
        description
    )

    if concepts:
        logger.info(f"Generated {len(concepts)} key concepts")
        # Find image URLs for each concept
        for concept in concepts:
            pexels_url = get_image_url(concept, "pexels")
            pixabay_url = get_image_url(concept, "pixabay")

            print(f"Concept: {concept}")
            print(f"Pexels URL: {pexels_url}")
            print(f"Pixabay URL: {pixabay_url}")
            print()
    else:
        logger.error("Failed to generate key concepts")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Extract key concepts and find related images."
    )
    parser.add_argument(
        "description",
        nargs="+",
        help="The text to extract concepts from and find images for.",
    )

    args = parser.parse_args()

    # Join all words in the description argument
    description = " ".join(args.description)

    if not description:
        logger.error(
            "No description provided. Please provide a description as a command-line argument."
        )
        sys.exit(1)

    main(description)
