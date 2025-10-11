---
title: "Unlocking the Digital Universe: APIs and Web Scraping"
subtitle: "A Beginner's Guide to Accessing Online Data Efficiently"
author: "Michael Borck"
format: 
  pptx:
    reference-doc: curtin_template.pptx
  html:
    theme: 
      - cosmo
      - custom.scss
    toc: true
    toc-expand: 2
    code-fold: true
    embed-resources: true
    fig-cap-location: bottom
    css: module-styles.css
  pdf:
    toc: false
    colorlinks: true
    geometry:
      - top=30mm
      - left=20mm
  docx:
    highlight-style: github
    toc: false
---


# Introduction to APIs and Web Scraping

* Understanding APIs and Web Scraping
* Importance in digital data retrieval
* Overview of today's session

::: {.notes}
Welcome to your introduction to APIs and Web Scraping! Today, we will explore how these tools allow us to harness vast amounts of data from the internet efficiently. APIs (Application Programming Interfaces) and web scraping are fundamental for anyone looking to retrieve, analyse, and use web data effectively. This session will cover the basics, setting the stage for more advanced topics.
:::

# What is an API?

* Definition: A set of rules that allows programs to communicate with each other
* Examples: Social media APIs, weather data APIs
* Uses: Data retrieval, automation, integration

::: {.notes}
An API, or Application Programming Interface, acts like a bridge between different software applications, allowing them to interact without user intervention. For instance, when you use a weather app, it retrieves data from a weather API to provide you with real-time updates. APIs are ubiquitous in software development, enabling functionalities such as pulling live data into applications or automating tasks.
:::

# Introduction to Web Scraping

* Definition: Extracting data from websites
* Tools: Python libraries like BeautifulSoup, Scrapy
* Legal and ethical considerations

::: {.notes}
Web scraping involves programmatically gathering data from the internet, specifically from web pages. Tools like BeautifulSoup and Scrapy in Python make this process accessible even for beginners. However, it's crucial to consider legal and ethical implications, such as respecting copyright and terms of service of websites, to avoid potential legal issues.
:::

# How APIs Work

* Sending requests from your application
* Receiving responses in formats like JSON, XML
* Common protocols: REST, SOAP

::: {.notes}
APIs work by processing requests and sending back responses. When you request data, such as the latest weather updates, the weather API processes this request and sends back data, often in JSON or XML format. Most modern APIs use the REST protocol due to its simplicity and effectiveness over the web.
:::

# Basic Web Scraping Example

* Python code to scrape data
* Simple example using BeautifulSoup

```python
from bs4 import BeautifulSoup
import requests

url = 'http://example.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.find('h1').text)
```

::: {.notes}
Here's a basic example of web scraping using Python. We use the BeautifulSoup library to parse HTML data. After sending a request to the website, we receive HTML content, which BeautifulSoup helps us navigate to extract specific pieces like headings, paragraphs, etc. This example simply prints the text inside the first heading tag (`<h1>`) of the webpage.
:::

# Comparing APIs and Web Scraping

* When to use each method
* Advantages and limitations
* Ethical considerations

::: {.notes}
Choosing between APIs and web scraping depends on your needs and the availability of data. APIs are preferred when available, as they are more stable and efficient. Web scraping is a good alternative when no API is available but requires careful handling to ensure it does not violate terms of service or copyright laws.
:::

# Practical Applications

* Real-time data integration in apps
* Automating repetitive tasks
* Enhancing data-driven decision making

::: {.notes}
Both APIs and web scraping have practical applications in various fields. For example, integrating real-time weather data into a travel app enhances user experience by providing current conditions. They also automate repetitive tasks, such as daily reports of stock prices, freeing up time for more complex analyses.
:::

# Conclusion

* Recap of key points
* Encouragement to explore further
* Resources for deeper learning

::: {.notes}
Today, we've covered the basics of APIs and web scraping, essential tools for modern data retrieval and application integration. I encourage you to explore these technologies further. Delve into the provided resources and experiment with building small projects to grasp their power and potential fully.
:::

# Further Resources

* [Python Requests Library Documentation](https://requests.readthedocs.io/en/latest/)
* [JSON Data in Python: A Practical Introduction](https://realpython.com/python-json/)
* [Understanding APIs for Beginners](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/)

::: {.notes}
For those eager to learn more, these resources are excellent starting points. They provide in-depth tutorials and explanations that can help reinforce today’s topics and expand your understanding and skills in working with APIs and web scraping.
:::