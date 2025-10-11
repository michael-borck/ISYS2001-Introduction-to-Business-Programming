import requests
from bs4 import BeautifulSoup
from datetime import datetime
import PyPDF2
import io
import re
import sys


def get_webpage_info(url):
    try:
        response = requests.get(url)
        content_type = response.headers.get('Content-Type', '').lower()

        if 'application/pdf' in content_type:
            return get_pdf_info(response.content)
        else:
            return get_html_info(response.text)
    except Exception as e:
        print(f"Error processing {url}: {str(e)}")
        return "Error retrieving page", "Error retrieving page", None


def get_html_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    title = soup.title.string if soup.title else "No title found"

    author = soup.find('meta', {'name': 'author'})
    author = author['content'] if author else "No author found"

    return title.strip(), author.strip(), None


def get_pdf_info(pdf_content):
    pdf_file = io.BytesIO(pdf_content)
    reader = PyPDF2.PdfReader(pdf_file)

    info = reader.metadata

    title = info.get('/Title', "No title found")
    author = info.get('/Author', "No author found")
    date = info.get('/CreationDate', None)

    if date:
        date = re.search(r'D:(\d{4})(\d{2})(\d{2})', date)
        if date:
            date = f"{date.group(1)}-{date.group(2)}-{date.group(3)}"

    return title, author, date


def create_chicago_reference(url):
    title, author, date = get_webpage_info(url)
    current_date = datetime.now().strftime("%B %d, %Y")

    if author != "No author found":
        if date:
            reference = f"{author}. \"{title}.\" {date}. {url}."
        else:
            reference = f"{author}. \"{title}.\" Accessed {current_date}. {url}."
    else:
        if date:
            reference = f"\"{title}.\" {date}. {url}."
        else:
            reference = f"\"{title}.\" Accessed {current_date}. {url}."

    return reference


def process_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()

    references = []
    for url in urls:
        url = url.strip()
        if url:
            reference = create_chicago_reference(url)
            references.append(reference)

    return references


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_url_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    references = process_file(file_path)

    print("\nChicago Style References:")
    for ref in references:
        print(ref)
        print()


if __name__ == "__main__":
    main()
