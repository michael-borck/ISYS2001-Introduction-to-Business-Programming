---
title: "Web Scraping in Python: Beginner's Worksheet"
format:
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

## Part 1: Understanding Web Scraping

1. In your own words, define web scraping:
   _________________________________________________________________
   _________________________________________________________________

2. List three common use cases for web scraping:
   a. _____________________________________________________________
   b. _____________________________________________________________
   c. _____________________________________________________________

## Part 2: Ethical Considerations

3. Why is it important to check a website's robots.txt file before scraping?
   _________________________________________________________________
   _________________________________________________________________

4. True or False: It's okay to scrape a website as quickly as possible to get the data you need.
   Answer: ____________

## Part 3: Python Libraries

5. Match the Python library to its primary use in web scraping:
   a. requests     ___ Parsing HTML
   b. BeautifulSoup  ___ Making HTTP requests
   c. pandas       ___ Data manipulation and analysis

6. Install the necessary libraries using pip. Write the command you would use:
   _________________________________________________________________

## Part 4: Basic HTML

7. Identify the following HTML elements:
   a. <div> _______________________________________________________
   b. <a href="..."> ______________________________________________
   c. <table> ______________________________________________________

## Part 5: Practical Exercise

8. Using the following HTML snippet, write Python code with BeautifulSoup to extract the temperature:

```html
<div class="weather-info">
  <h2>Today's Weather</h2>
  <p class="temperature">25°C</p>
  <p class="condition">Sunny</p>
</div>
```

Your code:
```python
from bs4 import BeautifulSoup

html_content = """
<div class="weather-info">
  <h2>Today's Weather</h2>
  <p class="temperature">25°C</p>
  <p class="condition">Sunny</p>
</div>
"""

soup = BeautifulSoup(html_content, 'html.parser')

# Your code here to extract the temperature


print(f"The temperature is: {temperature}")
```

## Part 6: Data Cleaning and Storage

9. Why might you need to clean data after scraping a website?
   _________________________________________________________________
   _________________________________________________________________

10. Write a line of Python code to save a pandas DataFrame called 'weather_df' to a CSV file named 'weather_data.csv':
    _________________________________________________________________

## Part 7: Advanced Topics

11. Briefly explain what Scrapy is used for in web scraping:
    _________________________________________________________________
    _________________________________________________________________

12. What is Selenium used for in the context of web scraping?
    _________________________________________________________________
    _________________________________________________________________

## Advanced Practical Exercise

13. Web Scraping and Data Visualisation Project

Your task is to scrape the first table from the Wikipedia page on global surface temperature, process the data, and create a visualization of the temperature trend.

URL: https://en.wikipedia.org/wiki/Global_surface_temperature#Global_temperature_record

Steps:
a) Use pandas to scrape the first table from the webpage.
b) Clean and prepare the data (hint: you may need to handle the 'Year' column).
c) Create a bar plot showing the temperature trend over time.

Here's a template to get you started:

```python
import pandas as pd
import matplotlib.pyplot as plt. # Or use panadas plotting

# Scrape the table
url = "https://en.wikipedia.org/wiki/Global_surface_temperature#Global_temperature_record"

# Sort the dataframe by year
# Your code here

# Create a bar plot
# Your code here to create a bar plot using matplotlib

# Show the plot
plt.show()
```

Hints:
- Use `pd.read_html(url)` to scrape all tables from the webpage.
- You may need to clean the 'Year' column to remove any non-numeric characters.
- Consider using `df['Year'] = pd.to_numeric(df['Year'], errors='coerce')` to convert 'Year' to numeric values.
- For the bar plot, you can use `plt.bar(df['Year'], df['Temperature'])` as a starting point.
- Don't forget to add labels and a title to your plot!

Bonus: Can you add a trend line to your plot?