import re
import requests
import json
import os
import logging
import argparse
import sys

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define cost per 1000 tokens (as of current pricing)
INPUT_COST_PER_1K = 0.01  # $0.01 per 1K input tokens
OUTPUT_COST_PER_1K = 0.03  # $0.03 per 1K output tokens


def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def write_markdown_file(file_path, content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(content)


def calculate_cost(input_tokens, output_tokens):
    input_cost = (input_tokens / 1000) * INPUT_COST_PER_1K
    output_cost = (output_tokens / 1000) * OUTPUT_COST_PER_1K
    total_cost = input_cost + output_cost
    return input_cost, output_cost, total_cost


def generate_presenter_notes(slide_content, all_slide_titles):
    lines = slide_content.split("\n")
    slide_title = ""
    for line in lines:
        if line.strip().startswith("#"):
            slide_title = line.strip().lstrip('#').strip()
            break
    if not slide_title:
        slide_title = "Untitled Slide"

    if not slide_title or slide_title in [
        "Acknowledgement of Country",
        "Acknowledge of Country",
        "Copyright",
        "Copyright Notice",
        "Copyright Information",
        "End of Module",
        "Questions?",
    ]:
        logger.info(f"Skipping notes generation for slide: {slide_title}")
        return "", 0, 0, 0

    bullet_points = [
        line.strip("- ").strip() for line in lines if line.strip().startswith("-")
    ]

    prompt = f"""
Generate presenter notes for a slide titled "{slide_title}".
The slide contains the following bullet points:
{json.dumps(bullet_points)}

The presentation also includes slides on the following topics:
{json.dumps(all_slide_titles)}

Please provide detailed presenter notes in 2 paragraphs summarise the slide content.

Please use Australian-British spelling and ensure the notes are clear and concise.

Please do not prefix or postfix with explanatory text.

Strictly follow this requirement: your response should not include any of the following words and phrases: meticulous, meticulously, navigating, complexities, realm, understanding, dive, shall, tailored, towards, underpins, everchanging, ever-evolving, the world of, not only, alright, embark, Journey, In today's digital age, hey, game changer, designed to enhance, it is advisable, daunting, when it comes to, in the realm of, amongst, unlock the secrets, unveil the secrets, and robust, diving, elevate, unleash, power, cutting-edge, rapidly, expanding, mastering, excels, harness, imagine, It's important to note, Delve into, Tapestry, Bustling, In summary, Remember that…, Take a dive into, Navigating, Landscape, Testament, In the world of, Realm, Embark, Analogies to being a conductor or to music, Vibrant, Metropolis, Firstly, Moreover, Crucial, To consider, Essential, There are a few considerations, Ensure, It's essential to, Furthermore, Vital, Keen, Fancy, As a professional, However, Therefore, Additionally, Specifically, Generally, Consequently, Importantly, Indeed, Thus, Alternatively, Notably, As well as, Despite, Essentially, While, Unless, Also, Even though, Because, In contrast, Although, In order to, Due to, Even if, Given that, Arguably, You may want to, On the other hand, As previously mentioned, It's worth noting that, To summarize, Ultimately, To put it simply, Promptly, Dive into, In today's digital era, Reverberate, Enhance, Emphasize / Emphasize, Revolutionize, Foster, Remnant, Subsequently, Nestled, Game changer, Labyrinth, Gossamer, Enigma, Whispering, Sights unseen, Sounds unheard, Indelible, My friend, In conclusion
"""

    api_url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": os.environ.get("ANTHROPIC_API_KEY"),
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
        generated_text = response_data["content"][0]["text"]
        input_tokens = response_data["usage"]["input_tokens"]
        output_tokens = response_data["usage"]["output_tokens"]
        input_cost, output_cost, total_cost = calculate_cost(input_tokens, output_tokens)
        return generated_text, input_tokens, output_tokens, total_cost
    except requests.exceptions.RequestException as e:
        logger.error(f"Error making request: {e}")
        if hasattr(e, "response"):
            logger.error(f"Response Status Code: {e.response.status_code}")
            logger.error(f"Response Headers: {json.dumps(dict(e.response.headers), indent=2)}")
            logger.error(f"Response Content: {e.response.text}")
        return f"Error generating notes: {str(e)}", 0, 0, 0


def parse_slides(content, separator_type):
    """
    Parses content into slides based on the specified separator type.
    """
    if separator_type == '---':
        slides = content.split('\n---\n')
        return [slide.strip() for slide in slides if slide.strip()]
    
    elif separator_type == 'heading':
        slides = []
        current_slide = ""
        in_code_block = False
        in_notes = False
        for line in content.split('\n'):
            if line.strip().startswith("```"):
                in_code_block = not in_code_block
            elif line.strip() == "::: {.notes}":
                in_notes = True
            elif line.strip() == ":::" and in_notes:
                in_notes = False

            if line.startswith('# ') and not in_code_block and not in_notes:
                if current_slide:
                    slides.append(current_slide.strip())
                current_slide = line
            else:
                current_slide += '\n' + line
        if current_slide:
            slides.append(current_slide.strip())
        return slides
    return []

def add_presenter_notes(file_path, preserve_existing, separator_type):
    content = read_markdown_file(file_path)
    
    # Use re.search to find an optional YAML block
    yaml_match = re.search(r"(^---\s*\n.*?\n---\s*\n)", content, re.DOTALL)
    yaml_front_matter = ""
    content_without_yaml = content

    if yaml_match:
        yaml_front_matter = yaml_match.group(1)
        content_without_yaml = content[len(yaml_front_matter):]
    
    slides = parse_slides(content_without_yaml, separator_type)
    
    all_slide_titles = [
        line.strip().lstrip('#').strip()
        for slide in slides
        for line in slide.split('\n')
        if line.strip().startswith("#")
    ]
    
    processed_slides = []
    total_input_tokens = 0
    total_output_tokens = 0
    total_cost = 0

    for index, slide in enumerate(slides, 1):
        slide_title = "Untitled Slide"
        for line in slide.split('\n'):
            if line.strip().startswith("#"):
                slide_title = line.strip().lstrip('#').strip()
                break
        
        logger.info(f"Processing slide {index}/{len(slides)}: {slide_title}")
        
        existing_notes = re.search(r"::: {\.notes}(.*?):::", slide, re.DOTALL)
        
        if preserve_existing and existing_notes:
            logger.info("  Preserving existing notes")
            processed_slides.append(slide)
            continue

        slide_without_notes = re.sub(r"\n*::: {\.notes}.*?:::\n*", "", slide, flags=re.DOTALL).strip()
        
        notes, input_tokens, output_tokens, cost = generate_presenter_notes(slide_without_notes, all_slide_titles)
        
        total_input_tokens += input_tokens
        total_output_tokens += output_tokens
        total_cost += cost
        
        if input_tokens > 0:
            logger.info(f"  Input tokens: {input_tokens}")
            logger.info(f"  Output tokens: {output_tokens}")
            logger.info(f"  Cost: ${cost:.4f}")

        new_slide_content = slide_without_notes
        if notes and not notes.startswith("Error generating notes"):
            new_slide_content += f"\n\n::: {{.notes}}\n{notes}\n:::"
        
        processed_slides.append(new_slide_content)

    # Reassemble the file correctly
    separator_string = "\n\n---\n\n" if separator_type == '---' else "\n\n\n"
    final_slides_content = separator_string.join(processed_slides)
    
    # The yaml_front_matter variable already contains the trailing newline.
    # Simply concatenate it with the joined slide content.
    final_content = yaml_front_matter + final_slides_content

    write_markdown_file(file_path, final_content.strip() + "\n")
    
    print("\nPresenter notes have been added to the Quarto markdown file.")
    print(f"\nTotal Statistics:")
    print(f"Total Input Tokens: {total_input_tokens}")
    print(f"Total Output Tokens: {total_output_tokens}")
    print(f"Total Tokens: {total_input_tokens + total_output_tokens}")
    print(f"Total Cost: ${total_cost:.4f}")


def main():
    parser = argparse.ArgumentParser(description="Add presenter notes to a Quarto markdown file.")
    parser.add_argument("file_path", help="Path to the input Quarto markdown file")
    parser.add_argument(
        "--separator", 
        default='---', 
        choices=['---', 'heading'], 
        help="The slide separator style ('---' or 'heading' for #)"
    )
    parser.add_argument(
        "--preserve-existing", 
        action="store_true", 
        help="Preserve existing notes instead of replacing them"
    )
    args = parser.parse_args()

    if not os.path.exists(args.file_path):
        print(f"Error: The file '{args.file_path}' does not exist.")
        sys.exit(1)

    add_presenter_notes(args.file_path, args.preserve_existing, args.separator)

if __name__ == "__main__":
    main()