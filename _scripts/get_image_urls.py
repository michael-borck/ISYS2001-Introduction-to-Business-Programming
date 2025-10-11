import os
import argparse
from openai import OpenAI

# Retrieve the OpenAI API key from environment variables
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def generate_keywords(description):
    # Use OpenAI API to generate keywords
    prompt = f"Given the description '{description}', generate four keywords:"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=10
    )

    keywords = response.choices[0].message.content.strip().split(", ")
    return keywords

def generate_image(keyword):
    # Use OpenAI API to generate an image based on the keyword
    response = client.images.generate(
        prompt=keyword,
        n=1,
        size="1024x1024"
    )

    image_url = response.data[0].url
    return image_url

def main(description):
    keywords = generate_keywords(description)
    images = {}
    for keyword in keywords:
        image_url = generate_image(keyword)
        images[keyword] = image_url
    return images

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Generate images from a description.')
    parser.add_argument('description', type=str, help='The description to generate keywords and images from.')
    args = parser.parse_args()

    images = main(args.description)

    for keyword, image_url in images.items():
        print(f"Keyword: {keyword} - Image URL: {image_url}")
