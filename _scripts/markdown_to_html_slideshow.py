import os
import re
import json
import markdown
from markdown.extensions.fenced_code import FencedCodeExtension
import argparse


def remove_front_matter(content):
    pattern = r'^---\s*\n.*?\n---\s*\n'
    return re.sub(pattern, '', content, flags=re.DOTALL)


def preprocess_content(content):
    content = re.sub(r'(\*\*.*?\*\*)(.)', r'\1\n\2', content)
    return content


def format_list_sections(content, title):
    if title in ["Learning Outcomes", "Key Takeaways", "Quiz"]:
        lines = content.split('\n')
        formatted_lines = ['<ul>']
        for line in lines:
            if line.strip().startswith('-'):
                formatted_lines.append(f'<li>{line.strip()[1:].strip()}</li>')
            elif line.strip().startswith('Answer:'):
                formatted_lines.append(f'<br><strong>{line.strip()}</strong>')
            else:
                formatted_lines.append(line)
        formatted_lines.append('</ul>')
        return '\n'.join(formatted_lines)
    return content


def parse_markdown(file_content):
    content = remove_front_matter(file_content)
    content = preprocess_content(content)
    slides = re.split(r'\n(?=\*\*)', content)
    parsed_slides = []

    for slide in slides:
        match = re.match(r'\*\*(.*?)\*\*(.*)', slide, re.DOTALL)
        if match:
            title = match.group(1).strip()
            content = match.group(2).strip()
        else:
            title = "Introduction"
            content = slide.strip()

        content = format_list_sections(content, title)
        content = re.sub(r'```(\w+)?\n(.*?)\n```', replace_code_block, content, flags=re.DOTALL)
        html_content = markdown.markdown(content, extensions=[FencedCodeExtension()])

        parsed_slides.append({
            "title": title,
            "content": html_content
        })

    return parsed_slides


def replace_code_block(match):
    code = match.group(2)
    indented_code = '\n'.join('    ' + line for line in code.split('\n'))
    return f'\n\n{indented_code}\n\n'


def generate_html(title, slides, output_file):
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <style>
            .slide {{ display: none; }}
            .slide.active {{ display: block; }}
            pre {{ white-space: pre-wrap; word-wrap: break-word; background-color: #f0f0f0; padding: 1em; }}
        </style>
    </head>
    <body class="bg-gray-100 flex items-center justify-center min-h-screen">
        <div class="bg-white rounded-lg shadow-lg p-6 max-w-2xl mx-auto">
            <div id="slideContent" class="mb-4"></div>
            <div class="flex justify-between items-center mt-4">
                <button onclick="changeSlide(-1)" class="bg-blue-500 text-white px-4 py-2 rounded flex items-center">
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-2"><polyline points="15 18 9 12 15 6"></polyline></svg>
                    Previous
                </button>
                <span id="slideNumber" class="text-gray-600"></span>
                <button onclick="changeSlide(1)" class="bg-blue-500 text-white px-4 py-2 rounded flex items-center">
                    Next
                    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="ml-2"><polyline points="9 18 15 12 9 6"></polyline></svg>
                </button>
            </div>
        </div>

        <script>
            const slides = {slides_json};

            let currentSlide = 0;

            function updateSlide() {{
                const slideContent = document.getElementById('slideContent');
                slideContent.innerHTML = `
                    <h2 class="text-2xl font-bold mb-2">${{slides[currentSlide].title}}</h2>
                    <div class="text-lg">${{slides[currentSlide].content}}</div>
                `;
                document.getElementById('slideNumber').textContent = `Slide ${{currentSlide + 1}} of ${{slides.length}}`;
            }}

            function changeSlide(direction) {{
                currentSlide = (currentSlide + direction + slides.length) % slides.length;
                updateSlide();
            }}

            updateSlide();
        </script>
    </body>
    </html>
    """

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_template.format(
            title=title,
            slides_json=json.dumps(slides)
        ))


def process_markdown_files(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(input_directory):
        if filename.endswith('.md'):
            input_path = os.path.join(input_directory, filename)
            output_path = os.path.join(output_directory, filename.replace('.md', '_slideshow.html'))

            with open(input_path, 'r', encoding='utf-8') as f:
                file_content = f.read()

            slides = parse_markdown(file_content)
            title = os.path.splitext(filename)[0].replace('-', ' ').title()
            generate_html(title, slides, output_path)
            print(f"Processed {filename}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert markdown files to HTML slideshows.")
    parser.add_argument("input_dir", help="Directory containing markdown files")
    parser.add_argument("output_dir", help="Directory to save HTML slideshows")
    args = parser.parse_args()

    process_markdown_files(args.input_dir, args.output_dir)
