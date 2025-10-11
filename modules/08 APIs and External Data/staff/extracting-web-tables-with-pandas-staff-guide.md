---
title: "Staff Answer Guide: Extracting Web Tables with Pandas"
author: "Michael Borck"
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

## Overview

This guide provides instructors with expected answers, common student challenges, and grading guidance for the notebook "Extracting Web Tables with Pandas: A Simple Introduction." The notebook teaches students how to use pandas to extract and analyze tabular data from websites.

## Learning Objectives Assessment

Students should demonstrate the ability to:
1. Use `pd.read_html()` to extract HTML tables from web pages
2. Process and clean the extracted data appropriately
3. Perform basic data analysis on the extracted tables
4. Export the cleaned data to a CSV file

## Expected Code Outputs & Solutions

### Section: Using pandas.read_html()

**Expected code execution:**
```python
# URL of a Wikipedia page with tables
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'

# Extract all tables from the web page
tables = pd.read_html(url)

# Check how many tables were found
print(f"Number of tables found on the page: {len(tables)}")
```

**Expected output:** The number of tables will vary based on the current Wikipedia page structure, but typically between 2-4 tables will be found.

**Grading notes:** 
- Students should correctly import pandas and use the `read_html()` function
- The URL should be properly formatted and enclosed in quotes
- They should store the result in a variable and check the number of tables found

### Section: Exploring the Extracted Tables

**Expected code execution:**
```python
# Let's look at the first table (index 0)
first_table = tables[0]

# Show the first few rows
first_table.head()
```

**Expected output:** A DataFrame display showing the first 5 rows of the first table from the Wikipedia page.

**Grading notes:**
- Students should correctly access the first element of the tables list
- They should use the `.head()` method to preview the data

### Section: Selecting the Right Table

**Expected code execution:**
```python
# Loop through all tables and print their shape (rows x columns)
for i, table in enumerate(tables):
    print(f"Table {i}: Shape = {table.shape} (rows × columns)")
    # Optional: display a small preview of each table
    print(f"Preview of columns: {table.columns.tolist()[:3]}...")
    print("-" * 50)
```

**Expected output:** For each table, information about its dimensions and a preview of column names.

**Grading notes:**
- Students should use enumeration to loop through the tables list
- They should correctly print the shape of each table
- Bonus points if they include additional information like column previews

### Section: Cleaning the Data

**Expected code execution:**
```python
# Make a copy to avoid changing the original
df = population_table.copy()

# Convert population to numeric (removing commas and other characters)
population_column = 'Population'  # Column name might vary
if population_column in df.columns:
    df[population_column] = df[population_column].astype(str).str.replace(',', '').str.extract('(\\d+)').astype(float)

# Show the cleaned table
df.head()
```

**Expected output:** A clean DataFrame with the population column converted to numeric values.

**Grading notes:**
- Students should create a copy of the DataFrame before modifying it
- They should correctly identify and clean the population column
- The cleaning should involve removing commas and converting to numeric data type
- They should handle the case where the expected column might not exist

### Section: Analyzing the Data

**Expected code execution:**
```python
# Get basic statistics
df.describe()

# Find the top 10 countries by population
top_10 = df.head(10)
print("Top 10 countries by population:")
top_10
```

**Expected output:** 
1. Statistical summary of the numeric columns
2. A DataFrame showing the top 10 countries by population

**Grading notes:**
- Students should use the `.describe()` method to generate summary statistics
- They should correctly extract the top 10 countries
- Note: If the table was already sorted by population, using `.head(10)` is sufficient; otherwise students should sort the data first

### Section: Saving the Results

**Expected code execution:**
```python
# Save the DataFrame to a CSV file
df.to_csv('country_populations.csv', index=False)
print("Data saved to 'country_populations.csv'")
```

**Expected output:** A confirmation message that the file was saved.

**Grading notes:**
- Students should use the `.to_csv()` method with the correct filename
- They should set `index=False` to avoid saving the DataFrame index
- No actual file will be created in most online notebook environments, so focus on correct syntax

## Challenge Section Assessment

For the challenge to extract a different table, assess:

1. **Table Selection:** Did the student choose an appropriate Wikipedia page with tabular data?
2. **Extraction Code:** Did they correctly implement `pd.read_html()`?
3. **Processing:** Did they identify and select the correct table from those extracted?
4. **Analysis:** Did they perform any meaningful analysis on the extracted data?

## Common Student Mistakes and Troubleshooting

1. **HTTP errors**: Students may encounter connection issues when accessing URLs
   - Suggestion: Verify the URL is accessible and correctly formatted

2. **Incorrect table indexing**: Students may select the wrong table from the extracted list
   - Suggestion: Emphasize the importance of exploring all tables before selecting one

3. **Data type conversion issues**: Problems with cleaning string-formatted numbers
   - Suggestion: Show examples of step-by-step conversion and error handling

4. **Column naming/access issues**: Wikipedia tables may have multi-level column headers
   - Suggestion: Demonstrate how to flatten or rename complex column structures

5. **Empty tables**: Some webpages may block automated scraping
   - Suggestion: Provide alternative URLs that are known to work with `read_html()`

## Additional Guidance Notes

### Ethical Considerations

Remind students about web scraping ethics:
- Check website's terms of service and robots.txt
- Implement reasonable request rates to avoid overloading servers
- Use data responsibly and cite sources

### Advanced Extensions

For students who finish early:
1. Suggest they try extracting tables from non-Wikipedia sources
2. Encourage them to create visualizations of the extracted data
3. Challenge them to automate the extraction of multiple tables from different pages

### Assessment Rubric

| Criterion | Excellent (A) | Satisfactory (B-C) | Needs Improvement (D-F) |
|-----------|---------------|--------------------|-----------------------|
| Table Extraction | Correctly extracts tables and selects appropriate ones | Extracts tables but may select wrong one | Unable to extract tables |
| Data Cleaning | Thoroughly cleans data, handles edge cases | Basic cleaning but misses some issues | Little/no data cleaning |
| Analysis | Performs meaningful analysis with insights | Basic analysis without deeper insights | Minimal or incorrect analysis |
| Code Quality | Well-organized, commented, efficient code | Functional code with minor inefficiencies | Poorly structured code with errors |
| Documentation | Clear explanation of process and findings | Basic documentation of steps | Little/no documentation |

## Support Resources for Students

Recommend these resources for students who need additional help:
- Pandas documentation on `read_html()`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_html.html
- Data cleaning tutorials with pandas
- Web scraping ethics guidelines
