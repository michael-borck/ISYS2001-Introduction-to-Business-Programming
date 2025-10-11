---
title: "Web Scraping in Python: A Weather-Themed Guide for Beginners"
subtitle: "Learning the Basics with `requests`, `BeautifulSoup`, and `pandas`"
author: "Michael Borck"
format: 
  pptx:
    reference-doc: ../../../_assets/template.pptx
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
# Copyright Information

![](../../../_assets/curtin-copy-right.png)



# Acknowledge of Country

I acknowledge the traditional custodians of the land on which I work and live,
and recognise their continuing connection to land, water and community. I pay
respect to elders past, present and emerging.

![](../../../_assets/ack_country.png)



# Today's Overview

- Introduction to Web Scraping
- Ethical Considerations
- Tools and Libraries
- HTML Basics
- Practical Implementation
- Best Practices and Additional Resources



::: {.notes}
**Aim**
The aim of this slide is to provide an overview of the key topics that will be covered in the presentation on web scraping using Python.

**Context**
Following the introductory slides on copyright information and acknowledgement of country, this slide outlines the main sections of the presentation. The subsequent slides will delve into each of these topics in greater detail, providing a comprehensive guide to web scraping using Python.

**Introduction to Web Scraping** This section will define web scraping, explain its purpose, and discuss the various applications of web scraping in different industries. It will also briefly touch on the types of data that can be extracted through web scraping.

**Ethical Considerations** Before diving into the technical aspects of web scraping, it is crucial to address the ethical considerations involved. This section will cover topics such as respecting website terms of service, avoiding excessive requests that may burden servers, and ensuring compliance with data privacy regulations.

**Tools and Libraries** This section will introduce the key tools and libraries used for web scraping in Python, such as requests for making HTTP requests, BeautifulSoup for parsing HTML, and pandas for data manipulation and analysis. It will also mention the need to install these libraries before proceeding with the practical implementation.

**HTML Basics** To effectively scrape data from websites, a basic understanding of HTML is necessary. This section will cover the fundamentals of HTML structure, tags, and attributes, which will be essential for locating and extracting desired data from web pages.

**Practical Implementation** This section will walk through the step-by-step process of web scraping using Python. It will demonstrate how to make HTTP requests, parse HTML using BeautifulSoup, extract specific data such as links and tables, and save the scraped data to a CSV file. Code examples and explanations will be provided to facilitate understanding.

**Best Practices and Additional Resources** The final section will discuss best practices for web scraping, such as rate limiting to avoid overloading servers and handling exceptions gracefully. It will also provide additional resources, including documentation, tutorials, and online communities, for further learning and troubleshooting.
:::

# Introduction to Web Scraping

- Definition: Automatically extracting data from websites
- Common Use Cases: Data gathering, price comparison, weather data aggregation

Example:
```python
import requests

# Simple example of fetching a weather page
url = "https://example.com/weather"
response = requests.get(url)
print(f"Status code: {response.status_code}")
print(f"Content: {response.text[:100]}...")  # Print first 100 characters
```



::: {.notes}
**Aim**
This slide aims to introduce the concept of web scraping, providing a definition and common use cases to set the foundation for the presentation.

**Context**
Following the overview slide, "Introduction to Web Scraping" is the first content slide of the presentation. It serves as a starting point for the audience to grasp the basic concept before delving into ethical considerations, tools, and techniques in the subsequent slides.

**Definition: Automatically extracting data from websites**
Web scraping is the process of automatically collecting data from websites using software or scripts. Instead of manually copying and pasting information, web scraping allows you to extract large amounts of data quickly and efficiently. This data can be text, images, links, or any other structured content available on the web pages.

**Common Use Cases: Data gathering, price comparison, weather data aggregation**
Web scraping has various applications across industries. It is commonly used for gathering data for research, analysis, or business intelligence purposes. For example, companies can scrape competitor websites to compare prices and monitor the market. Another use case is aggregating weather data from multiple sources to provide comprehensive forecasts. Web scraping enables the collection of data that may not be readily available through APIs or other means.
:::

# Ethical Considerations in Web Scraping

- Always check `robots.txt`
- Abide by the website's terms of service
- Avoid overwhelming the server (rate-limiting)
- Consider legal and ethical implications

Example of checking robots.txt:
```python
import requests

def check_robots_txt(url):
    robots_url = f"{url}/robots.txt"
    response = requests.get(robots_url)
    if response.status_code == 200:
        print(f"Robots.txt content:\n{response.text}")
    else:
        print(f"No robots.txt found at {robots_url}")

check_robots_txt("https://curtin.edu.au")
```



::: {.notes}
**Aim**
This slide aims to highlight the key ethical considerations that should be taken into account when performing web scraping to ensure responsible and respectful data collection practices.

**Context**
Having introduced the concept of web scraping and its applications, it is crucial to address the ethical implications before delving into the technical aspects and tools. This slide serves as a bridge between the introduction and the hands-on sections, emphasising the importance of ethical web scraping practices.

**Always check `robots.txt`**
The `robots.txt` file is a standard used by websites to communicate their crawling preferences to web scrapers. It is essential to respect the website's wishes by checking this file before scraping. The file specifies which pages or sections of the website are allowed or disallowed for scraping. Ignoring the `robots.txt` file can be considered unethical and may lead to legal consequences.

**Abide by the website's terms of service**
In addition to `robots.txt`, websites often have terms of service (TOS) or legal disclaimers that outline acceptable usage policies. These terms may explicitly prohibit web scraping or specify conditions under which scraping is permitted. It is crucial to thoroughly review and comply with the website's TOS to avoid violating their guidelines and potentially facing legal repercussions.

**Avoid overwhelming the server (rate-limiting)**
Web scraping can put a significant load on the target website's server, especially if the scraping is aggressive or poorly implemented. To prevent overwhelming the server and disrupting its normal functionality, it is important to incorporate rate-limiting techniques. This involves adding delays between requests, limiting the number of concurrent requests, and being mindful of the website's resources. Respectful web scraping practices help maintain a healthy internet ecosystem.

**Consider legal and ethical implications**
Web scraping can raise legal and ethical concerns, particularly when it involves sensitive or personal data. It is crucial to consider the purpose of scraping and assess whether it aligns with ethical principles. Scraping copyrighted material, personal information, or data protected by privacy laws should be approached with caution. Consulting with legal experts and staying informed about relevant regulations can help navigate potential legal and ethical pitfalls.
:::

# Tools for Web Scraping in Python

- `requests` for making HTTP requests
- `BeautifulSoup` for parsing HTML/XML documents
- `pandas` for data manipulation (especially tables)
- `scrapy` for large scale scraping
- `Selenium` for scraping dynamic content



::: {.notes}
**Aim**
This slide aims to introduce the key Python libraries and tools commonly used for web scraping tasks.

**Context**
Having discussed the ethical considerations in web scraping, we now move on to the practical tools and libraries available in Python for scraping web data. The slide sets the stage for subsequent slides that dive deeper into using these tools for various web scraping tasks.

**`requests` for making HTTP requests** The `requests` library simplifies the process of making HTTP requests to web servers from Python. It abstracts away the low-level details and provides a user-friendly interface for sending GET, POST, and other types of requests. With `requests`, you can easily fetch the HTML content of web pages, which is the first step in web scraping.

**`BeautifulSoup` for parsing HTML/XML documents** Once you have obtained the HTML content using `requests`, you need to parse and extract the desired data from it. `BeautifulSoup` is a powerful library that allows you to parse HTML and XML documents efficiently. It provides intuitive methods to navigate and search the parsed tree, making it convenient to locate and extract specific elements, such as tags, attributes, and text content.

**`pandas` for data manipulation (especially tables)** `pandas` is a data manipulation library that excels at handling structured data, particularly tabular data. In the context of web scraping, `pandas` is particularly useful when dealing with data in HTML tables. It provides functions to read HTML tables directly into `DataFrame` objects, allowing for easy data cleaning, transformation, and analysis using the rich functionalities of `pandas`.

**`scrapy` for large scale scraping** While `requests` and `BeautifulSoup` are great for small to medium-sized scraping tasks, `scrapy` is a framework designed for large-scale web scraping projects. It provides a complete ecosystem for building and managing web spiders, handling requests, parsing responses, and storing scraped data. `scrapy` offers features like concurrent requests, built-in caching, and support for various output formats, making it suitable for more complex and intensive scraping tasks.

**`Selenium` for scraping dynamic content** Some websites heavily rely on JavaScript to dynamically render content on the client-side. In such cases, using `requests` alone may not be sufficient as it cannot execute JavaScript. `Selenium` is a tool that automates web browsers, allowing you to interact with web pages as a user would. It can be used in combination with Python to scrape dynamic content by simulating user actions like clicking buttons, filling forms, and waiting for elements to load.
:::

# Installing the Necessary Libraries

Install the required libraries using pip:

```
pip install requests beautifulsoup4 pandas
```

Consider using a virtual environment for your project.



::: {.notes}
**Aim**
This slide aims to guide participants through the process of installing the required Python libraries for web scraping.

**Context**
Having discussed the ethical considerations and tools for web scraping in Python, this slide will provide practical instructions on setting up the necessary libraries. It acts as a foundation before delving into the technical aspects of web scraping in subsequent slides.
:::

# Understanding URLs

- Breakdown of a URL (scheme, domain, path, query parameters)
- Dynamic vs. Static URLs

Example:
```python
from urllib.parse import urlparse, parse_qs

url = "https://example.com/weather?city=New York&units=metric"
parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

print(f"Scheme: {parsed_url.scheme}")
print(f"Domain: {parsed_url.netloc}")
print(f"Path: {parsed_url.path}")
print(f"Query parameters: {query_params}")
```



::: {.notes}
**Aim**
The aim of this slide is to provide an overview of the structure and components of URLs and to explain the difference between dynamic and static URLs.

**Context**
This slide follows an introduction to web scraping and ethical considerations, and precedes slides on the basics of HTML and making HTTP requests. Understanding URLs is a fundamental concept for web scraping, as it allows us to locate and access specific web pages and resources.

**Breakdown of a URL (scheme, domain, path, query parameters)**
A URL (Uniform Resource Locator) is a standardised address used to locate and access resources on the internet. It consists of several components:
- Scheme: Specifies the protocol used to access the resource, such as HTTP or HTTPS.
- Domain: Identifies the web server hosting the resource, such as example.com.
- Path: Specifies the location of the resource within the website's directory structure, like /page.html.
- Query parameters: Optional key-value pairs appended to the URL after a question mark (?), used to pass data to the server, e.g., ?key1=value1&key2=value2.

**Dynamic vs. Static URLs**
URLs can be classified as either dynamic or static:
- Static URLs have fixed content that remains the same each time the page is accessed. They are typically used for pages that don't require server-side processing or user input.
- Dynamic URLs, on the other hand, generate content on-the-fly based on user input, database queries, or other server-side processes. They often include query parameters and may change each time the page is accessed.
:::

# Basics of HTML

Key HTML Elements: `<div>`, `<span>`, `<a>`, `<table>`, `<tr>`, etc.

Example:
```html
<div id="weather-container">
  <h1>Weather Forecast</h1>
  <table>
    <tr>
      <th>Day</th>
      <th>Temperature</th>
      <th>Condition</th>
    </tr>
    <tr>
      <td>Monday</td>
      <td>25°C</td>
      <td>Sunny</td>
    </tr>
    <!-- More rows... -->
  </table>
</div>
```



::: {.notes}
**Aim**
The aim of this slide is to provide a brief introduction to the basics of HTML.

**Context**
This slide follows on from the "Understanding URLs" slide, which focused on the structure and components of URLs. Understanding HTML is crucial for web scraping, as it forms the structure and content of web pages. The following slides will cover the tools and techniques for web scraping in Python, building on this foundational knowledge of HTML.
:::

# Making an HTTP Request with `requests`

Example:
```python
import requests

url = "https://wttr.in/perth"
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the weather page")
    print(f"Content: {response.text[:200]}...")  # Print first 200 characters
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
```



::: {.notes}
**Aim**
To demonstrate how to make an HTTP request using the `requests` library in Python.

**Context**
Having learned about the basics of HTML and URLs, we are now ready to start making HTTP requests to retrieve web pages. This slide focuses on using the `requests` library, which is a popular and user-friendly library for making HTTP requests in Python. The next slide will cover parsing the retrieved HTML using `BeautifulSoup`.
:::

# Parsing HTML with `BeautifulSoup`

Example:
```python
from bs4 import BeautifulSoup

html_content = """
<html>
  <body>
    <h1>Weather Forecast</h1>
    <p class="temperature">25°C</p>
    <p class="condition">Sunny</p>
  </body>
</html>
"""

soup = BeautifulSoup(html_content, 'html.parser')
temperature = soup.find('p', class_='temperature').text
condition = soup.find('p', class_='condition').text

print(f"Temperature: {temperature}")
print(f"Condition: {condition}")
```



::: {.notes}
**Aim**
This slide aims to introduce the BeautifulSoup library and demonstrate how it can be used to parse HTML content.

**Context**
After discussing the basics of HTML and making HTTP requests using the `requests` library, this slide focuses on parsing the retrieved HTML content using BeautifulSoup. The following slides will build upon this foundation, showing how to extract specific elements like links and tables from the parsed HTML.

**Parsing HTML with `BeautifulSoup`** BeautifulSoup is a popular Python library used for parsing HTML and XML documents. It provides a convenient way to extract data from web pages by allowing you to navigate the parsed tree structure using various methods and selectors. BeautifulSoup can handle imperfect or messy HTML and still extract the desired information effectively. To use BeautifulSoup, you first create a BeautifulSoup object by passing the HTML content and the parser to be used (e.g., 'html.parser'). Once the object is created, you can use methods like `find()`, `find_all()`, and CSS selectors to locate specific elements within the parsed HTML tree. BeautifulSoup's intuitive API makes it easy to extract text, attributes, and navigate between different elements in the document.
:::

# Extracting All Links from a Webpage

Example:
```python
import requests
from bs4 import BeautifulSoup

url = "https://curtin.edu.au"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    href = link.get('href')
    text = link.text
    print(f"Link: {text} -> {href}")
```



::: {.notes}
**Aim**
The aim of this slide is to demonstrate how to extract all hyperlinks from a webpage using Python and BeautifulSoup.

**Context**
After learning about making HTTP requests with `requests` and parsing HTML with `BeautifulSoup`, this slide builds on that knowledge to show a practical application. It leads into the next slides on extracting tables from webpages using `BeautifulSoup` and `pandas`.

**Bullet Point 1** To extract all links from a webpage, first make an HTTP request to the desired URL using the `requests` library. This will return the HTML content of the page.

**Bullet Point 2** Next, create a `BeautifulSoup` object by passing the HTML content and the parser type (e.g., 'html.parser') to the `BeautifulSoup` constructor. This allows you to parse and navigate the HTML structure.

**Bullet Point 3** Use the `find_all()` method of the `BeautifulSoup` object to locate all the `<a>` tags in the HTML, as these tags represent hyperlinks. You can pass the tag name 'a' as an argument to `find_all()`.

**Bullet Point 4** Iterate over the resulting list of `<a>` tags. For each tag, access the 'href' attribute using square bracket notation (e.g., `link['href']`). This attribute contains the URL of the hyperlink.

**Bullet Point 5** Append each extracted URL to a list to store all the links found on the webpage. You can then use this list for further analysis or processing as needed.

**Bullet Point 6** Remember to handle any relative URLs by joining them with the base URL of the webpage to create absolute URLs. You can use the `urljoin()` function from the `urllib.parse` module for this purpose.
:::

# Extracting Tables with `BeautifulSoup`

Example:
```python
html_content = """
<table id="weather-forecast">
  <tr>
    <th>Day</th>
    <th>Temperature</th>
    <th>Condition</th>
  </tr>
  <tr>
    <td>Monday</td>
    <td>25°C</td>
    <td>Sunny</td>
  </tr>
  <tr>
    <td>Tuesday</td>
    <td>22°C</td>
    <td>Cloudy</td>
  </tr>
</table>
"""

soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find('table', id='weather-forecast')

for row in table.find_all('tr')[1:]:  # Skip header row
    columns = row.find_all('td')
    day = columns[0].text
    temp = columns[1].text
    condition = columns[2].text
    print(f"{day}: {temp}, {condition}")
```



::: {.notes}
**Aim**
This slide aims to demonstrate how to extract tables from webpages using the `BeautifulSoup` library in Python.

**Context**
After covering the basics of HTML parsing with `BeautifulSoup`, this slide focuses on a specific use case: extracting tabular data. The following slide will explore an alternative approach using the `pandas` library, and subsequent slides will cover saving the extracted data and ethical considerations in web scraping.
:::

# Using `pandas` to Extract Tables

Example:
```python
import pandas as pd

url = "https://en.wikipedia.org/wiki/Global_surface_temperature#Global_temperature_record"
tables = pd.read_html(url)
weather_df = tables[0]  # Assuming the weather table is the first table on the page
print(weather_df.head())
```



::: {.notes}
**Aim**
The aim of this slide is to demonstrate how to use the `pandas` library to extract tables from web pages.

**Context**
This slide follows on from the previous slide about extracting tables using `BeautifulSoup`. It provides an alternative approach using the `pandas` library, which can simplify the process of extracting tabular data from HTML. The next slide will cover saving the extracted data to a CSV file.
:::

# Saving Data to a CSV File

Example:
```python
# Assuming we have a cleaned DataFrame 'weather_df'
weather_df.to_csv('weather_data.csv', index=False)
print("Data saved to weather_data.csv")
```



::: {.notes}
**Aim**
The purpose of this slide is to demonstrate how to save the data extracted from web scraping to a CSV file for further analysis or use.

**Context**
After learning how to extract data from webpages using `requests`, `BeautifulSoup`, and `pandas`, the next logical step is to save this data in a format that can be easily accessed and manipulated later. This slide will show how to save the scraped data to a CSV file, which is a common and versatile format for storing tabular data. The following slides will cover topics such as rate limiting and advanced web scraping techniques.
:::

# Rate Limiting: Being a Good Web Citizen

- Importance: Avoid overwhelming servers and getting blocked
- Simple implementation: Add delays between requests

Example:
```python
import time
import requests

def fetch_with_delay(url, delay=1):
    response = requests.get(url)
    print(f"Fetched {url}: Status {response.status_code}")
    time.sleep(delay)  # Wait for 1 second before next request
    return response

# Usage
urls = ["https://example.com/weather/day1", "https://example.com/weather/day2"]
for url in urls:
    fetch_with_delay(url)
```



::: {.notes}
**Aim**
The aim of this slide is to emphasise the importance of rate limiting when web scraping and provide guidance on how to implement it.

**Context**
This slide follows on from the discussion of ethical considerations in web scraping and the technical details of making HTTP requests and parsing HTML. It serves as a bridge to the more advanced topics that will be covered later in the presentation.

**Importance: Avoid overwhelming servers and getting blocked**
Rate limiting is crucial when web scraping to avoid placing excessive load on the servers you are scraping. Sending too many requests in a short period can overwhelm the server, potentially causing it to slow down or even crash. Moreover, many websites have mechanisms in place to detect and block suspicious activity, such as scraping without rate limiting. Ignoring rate limits can lead to your IP address being blocked, preventing further access to the site.

**Simple implementation: Add delays between requests**
One straightforward way to implement rate limiting is to add delays between your requests. After making a request and processing the response, your scraper should pause for a set amount of time before sending the next request. This delay helps mimic human browsing behaviour and reduces the burden on the server. The length of the delay can be adjusted based on the specific website's terms of service and the volume of data you need to scrape.
:::

# Advanced Topics

- `Scrapy` for large-scale scraping projects
- `Selinumn` for dynamic content
- Use of header (mimic a browser)
- Handling CAPTCHAs and IP Blocks
- APIs as an alternative to scraping (e.g., OpenWeatherMap API)
- Deep dive into robots.txt and terms of service
- Understanding and respecting website policies



::: {.notes}
**Aim**
This slide aims to introduce advanced topics in web scraping that go beyond the basics covered in previous slides.

**Context**
Having covered the fundamentals of web scraping, including tools, HTML parsing, and basic data extraction, this slide delves into more complex aspects of web scraping. It explores techniques for handling dynamic content, large-scale projects, and challenging scenarios like CAPTCHAs. The slide also discusses the importance of respecting website policies and suggests APIs as an alternative to scraping.

**Scrapy for large-scale scraping projects**
Scrapy is a powerful and popular Python framework designed for large-scale web scraping projects. It provides a high level of customisation and flexibility, allowing you to efficiently crawl and extract data from multiple pages and websites. Scrapy handles tasks such as request scheduling, parallel processing, and data pipeline management, making it an excellent choice for complex scraping tasks.

**Selenium for dynamic content**
Some websites heavily rely on JavaScript to render content dynamically, making it difficult to scrape using traditional methods. Selenium is a tool that automates web browsers, allowing you to interact with dynamic web pages as if you were a human user. With Selenium, you can load and navigate through dynamic content, click buttons, fill forms, and extract data that may not be immediately available in the HTML source code.

**Use of headers (mimic a browser)**
When sending HTTP requests to a website, it's sometimes necessary to mimic the behaviour of a browser to avoid being detected as a scraper. One way to achieve this is by setting appropriate headers in your requests. Headers such as "User-Agent", "Referer", and "Accept-Language" can be customised to resemble those sent by popular browsers, making your requests appear more legitimate to the target website.

**Handling CAPTCHAs and IP blocks**
Websites may employ various measures to prevent automated scraping, such as CAPTCHAs and IP blocking. CAPTCHAs are designed to distinguish human users from bots by presenting challenges that are difficult for computers to solve. To handle CAPTCHAs, you may need to use specialised libraries or services that can solve them automatically. IP blocking occurs when a website detects suspicious activity from an IP address and blocks it. To mitigate this, you can implement techniques like rotating IP addresses, using proxies, or introducing delays between requests.

**APIs as an alternative to scraping (e.g., OpenWeatherMap API)**
In some cases, websites offer APIs (Application Programming Interfaces) that provide structured access to their data. Using APIs can be a more reliable and efficient alternative to web scraping. APIs often have well-defined endpoints, authentication mechanisms, and documentation, making it easier to retrieve data in a structured format. For example, the OpenWeatherMap API allows you to access weather data for various locations without the need for scraping.

**Deep dive into robots.txt and terms of service**
Before scraping a website, it's crucial to familiarise yourself with its robots.txt file and terms of service. The robots.txt file is a standard used by websites to communicate their crawling policies to web robots. It specifies which pages or sections of the website are allowed or disallowed for scraping. The terms of service outline the legal guidelines and restrictions set by the website owner regarding the use of their content. Violating these guidelines can lead to legal consequences.

**Understanding and respecting website policies**
Web scraping should be conducted in an ethical and respectful manner. It's essential to understand and adhere to the website's policies regarding scraping. Some websites may explicitly prohibit scraping or have specific requirements for accessing their content. Respectful web scraping involves limiting the frequency of requests to avoid overloading the website's servers, properly identifying your scraper, and complying with any stated terms of service. Building a good reputation as a responsible scraper is important for long-term success in web scraping projects.
:::

# Conclusion

- Recap: Web scraping workflow, tools, and ethical practices
- Remember to always scrape responsibly
- Practice and explore different websites to improve your skills

Any questions?

::: {.notes}
**Aim**
The aim of this slide is to summarise the key points covered throughout the presentation and reinforce the importance of responsible web scraping practices.

**Context**
This final slide follows on from the "Advanced Topics" section and brings together all the concepts, tools, and techniques discussed in the presentation. It serves as a reminder of the main takeaways and encourages the audience to apply their newfound knowledge in a responsible and ethical manner.

**Recap: Web scraping workflow, tools, and ethical practices**
Throughout this presentation, we have covered the essential components of web scraping, including the basic workflow, the tools available in Python, such as `requests` and `BeautifulSoup`, and the ethical considerations one must keep in mind when scraping websites. By understanding the fundamentals of web scraping and the importance of adhering to ethical guidelines, you can effectively extract valuable data while respecting the rights of website owners and the integrity of the web.

**Remember to always scrape responsibly**
As emphasised in the "Ethical Considerations in Web Scraping" section, it is crucial to scrape responsibly and respect the terms of service, robots.txt files, and other guidelines set by website owners. Avoid overloading servers with excessive requests, cache data when possible, and be mindful of the impact your scraping activities may have on the target website. By being a responsible web scraper, you can maintain a positive relationship with website owners and ensure the sustainability of web scraping as a valuable data gathering technique.

**Practice and explore different websites to improve your skills**
To become proficient in web scraping, it is essential to practice and apply the concepts learned in this presentation to a variety of websites. Start with simple, static websites and gradually move on to more complex, dynamic ones. Experiment with different libraries and techniques, such as handling pagination, interacting with APIs, and scraping data from JavaScript-rendered pages. By exploring diverse websites and challenging yourself with new scraping scenarios, you will develop a strong foundation in web scraping and be well-equipped to tackle real-world data extraction tasks.
:::

