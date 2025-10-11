---
title: "STAFF ANSWER: Web Scraping in Python: Beginner's Worksheet"
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

#### Part 1: Understanding Web Scraping

1. **Define web scraping**:  
   Web scraping is the automated process of extracting data from websites, typically by using code to gather and parse the data from the HTML of web pages.

2. **Common use cases for web scraping**:  
   a. Gathering pricing data from e-commerce websites for comparison.  
   b. Collecting information such as reviews or ratings from websites for sentiment analysis.  
   c. Extracting large datasets from government or academic websites for research purposes.

#### Part 2: Ethical Considerations

3. **Importance of checking robots.txt**:  
   The `robots.txt` file provides instructions about which parts of the website should or should not be accessed by automated scrapers. Respecting this file ensures compliance with the site's preferences and avoids legal or ethical violations.

4. **True or False**: Scraping a website as quickly as possible is okay.  
   Answer: **False**  
   Rapid scraping can overwhelm the server, leading to denial of service for other users or violating the terms of service of the website.

#### Part 3: Python Libraries

5. **Match the Python library to its primary use**:  
   a. `requests` — Making HTTP requests.  
   b. `BeautifulSoup` — Parsing HTML.  
   c. `pandas` — Data manipulation and analysis.

6. **Command to install libraries**:  
   ```bash
   pip install requests beautifulsoup4 pandas
   ```

#### Part 4: Basic HTML

7. **Identify HTML elements**:  
   a. `<div>` — A container or section in HTML often used to group elements together.  
   b. `<a href="...">` — A hyperlink element used to link to another webpage or resource.  
   c. `<table>` — An element used to define a table for displaying data in rows and columns.

#### Part 5: Practical Exercise

8. **Python code with BeautifulSoup to extract temperature**:
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

   # Extracting temperature
   temperature = soup.find('p', class_='temperature').text

   print(f"The temperature is: {temperature}")
   ```

   **Output**:  
   The temperature is: 25°C

#### Part 6: Data Cleaning and Storage

9. **Why you might need to clean data after scraping**:  
   Data scraped from websites may contain extra characters, formatting inconsistencies, or irrelevant information. Cleaning the data ensures it's structured and ready for analysis.

10. **Save DataFrame to CSV**:
    ```python
    weather_df.to_csv('weather_data.csv', index=False)
    ```

#### Part 7: Advanced Topics

11. **Scrapy usage**:  
    Scrapy is a powerful and efficient Python framework used for large-scale web scraping projects, allowing for the scraping, processing, and storing of large amounts of web data.

12. **Selenium usage**:  
    Selenium is a tool used for automating web browsers, and in web scraping, it is especially useful for scraping websites that rely on JavaScript to load content dynamically.

#### Advanced Practical Exercise

13. **Web Scraping and Data Visualization Project**:
   ```python
    import pandas as pd
    import matplotlib.pyplot as plt

    # Scrape the table
    url = "https://en.wikipedia.org/wiki/Global_surface_temperature#Global_temperature_record"
    tables = pd.read_html(url)
    df = tables[0]  # Assuming the first table contains the data we need

    # Clean the data (not really needed, but...)
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
    df = df.dropna(subset=['Year'])  # Drop rows where 'Year' couldn't be converted
    df = df.sort_values(by='Year')

    # Create a bar plot showing temperature trends over time
    plt.bar(df['Year'], df['Anomaly °C'])
    plt.xlabel('Year')
    plt.ylabel('Temperature Anomaly(°C)')
    plt.title('Global Surface Temperature Trend')
    plt.show()
   ```

   **Bonus (Trend Line)**:
   To add a trend line, you could use `numpy` to fit a line to the data:

   ```python
   import numpy as np

    # Fit a line to the data
    z = np.polyfit(df['Year'], df['Anomaly °C'], 1)
    p = np.poly1d(z)

    # Create a bar plot showing temperature trends over time
    plt.bar(df['Year'], df['Anomaly °C'])
    # Plot the trend line
    plt.plot(df['Year'], p(df['Year']), label='Trend Line', color='red')
    plt.xlabel('Year')
    plt.ylabel('Temperature Anomaly(°C)')
    plt.title('Global Surface Temperature Trend')
    plt.legend()
    plt.show()
   ```