---
title: "Staff Answer Guide: Web Scraping Basics"
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
This guide provides instructors with expected answers, common student challenges, and grading guidance for the "Web Scraping Basics: A Friendly Introduction for Beginners" notebook. The notebook introduces students to web scraping concepts and techniques using Python, BeautifulSoup, requests, and pandas.

## Learning Objectives Assessment

Students should demonstrate the ability to:
1. Understand web scraping concepts and ethical considerations
2. Use requests library to download web page content
3. Parse HTML using BeautifulSoup to extract specific data elements
4. Organize and clean scraped data using pandas
5. Perform basic data analysis on the collected information

## Expected Code Outputs & Solutions

### Section: Downloading a Web Page

**Expected code execution:**
```python
# Define your headers to identify yourself
headers = {
    'User-Agent': 'Mozilla/5.0 (Educational purpose scraper)',
    'Accept': 'text/html,application/xhtml+xml'
}

# URL of the page we want to scrape
url = 'http://books.toscrape.com/'

# Make a request to the website
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    print(f"Successfully downloaded the page! Content length: {len(response.text)} characters")
else:
    print(f"Failed to download the page. Status code: {response.status_code}")

# Let's see what the raw HTML looks like (just the first 500 characters)
print(response.text[:500])
```

**Expected output:** 
- Success message showing content length (varies, typically 50,000+ characters)
- First 500 characters of HTML code from the page

**Grading notes:**
- Students should include proper headers with a user agent
- The request should be made correctly with `requests.get()`
- Response status code should be checked to verify successful download
- Raw HTML preview should be shown for inspection

### Section: Parsing HTML with BeautifulSoup

**Expected code execution:**
```python
# Create a BeautifulSoup object
soup = BeautifulSoup(response.text, 'html.parser')

# Let's check the title of the page
page_title = soup.title.text
print(f"Page title: {page_title}")
```

**Expected output:**
- Page title: "All products | Books to Scrape - Sandbox"

**Grading notes:**
- Students should correctly create a BeautifulSoup object with appropriate parser
- Page title should be extracted using `.title.text`
- Print statement should display formatted output

### Section: Extracting Book Information

**Expected code execution:**
```python
# Find all book containers on the page
book_containers = soup.find_all('article', class_='product_pod')
print(f"Found {len(book_containers)} books on this page")

# Lists to store our data
titles = []
prices = []
ratings = []

# Extract information from each book container
for book in book_containers:
    # Extract title
    title = book.h3.a['title']
    titles.append(title)

    # Extract price
    price = book.find('p', class_='price_color').text
    prices.append(price)

    # Extract star rating (contained in the class name)
    star_rating = book.find('p', class_='star-rating')['class'][1]
    ratings.append(star_rating)

# Display the first 5 items from each list
for i in range(5):
    print(f"Book {i+1}: {titles[i]}, Price: {prices[i]}, Rating: {ratings[i]}")
```

**Expected output:**
- Message showing number of books found (typically 20 on the first page)
- List of 5 books with their titles, prices, and ratings

**Grading notes:**
- Students should correctly select book containers using `find_all()`
- Book properties should be extracted using appropriate BeautifulSoup methods
- All three data points should be stored in separate lists
- The first 5 entries should be displayed properly

### Section: Converting to a DataFrame

**Expected code execution:**
```python
# Create a DataFrame from the scraped data
books_data = {
    'Title': titles,
    'Price': prices,
    'Rating': ratings
}

books_df = pd.DataFrame(books_data)

# Show the DataFrame
books_df
```

**Expected output:**
- A pandas DataFrame with three columns (Title, Price, Rating) and approximately 20 rows

**Grading notes:**
- Data should be correctly organized into a dictionary structure
- DataFrame should be created properly with all three columns
- DataFrame should be displayed (implicit or explicit)

### Section: Cleaning and Processing Data

**Expected code execution:**
```python
# Clean the price column (remove £ symbol and convert to float)
books_df['Price'] = books_df['Price'].str.replace('£', '').astype(float)

# Convert ratings to numeric values
rating_mapping = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
}
books_df['Rating'] = books_df['Rating'].map(rating_mapping)

# Show the updated DataFrame
books_df
```

**Expected output:**
- An updated DataFrame with:
  - Price column containing numeric values without £ symbol
  - Rating column converted to integers (1-5)

**Grading notes:**
- Price cleaning should use string replacement and type conversion
- Rating conversion should use a mapping dictionary
- Both columns should be properly overwritten in the DataFrame
- Updated DataFrame should be displayed

### Section: Analyzing the Scraped Data

**Expected code execution:**
```python
# Display basic statistics
books_df.describe()

# Calculate average price by rating
avg_price_by_rating = books_df.groupby('Rating')['Price'].mean().sort_index()
print("Average price by rating:")
avg_price_by_rating
```

**Expected output:**
- Statistical summary of the DataFrame columns
- Average price by rating level (grouped and sorted by rating)

**Grading notes:**
- Basic statistics should be displayed using `describe()`
- Groupby operation should be applied correctly
- Results should be sorted by rating index
- Output should be formatted with appropriate label

### Section: Challenge - Scrape Multiple Pages

**Expected code execution:** 
Students will implement their own solution to scrape multiple pages. A correct implementation should:

```python
all_titles = []
all_prices = []
all_ratings = []

# Loop through multiple pages
for page_num in range(1, 4):  # Pages 1, 2, and 3
    # Construct the URL for each page
    if page_num == 1:
        page_url = 'http://books.toscrape.com/'
    else:
        page_url = f'http://books.toscrape.com/catalogue/page-{page_num}.html'

    # Add a small delay to be polite
    time.sleep(1)

    # Make the request
    response = requests.get(page_url, headers=headers)

    # Check if successful
    if response.status_code == 200:
        print(f"Successfully scraped page {page_num}")

        # Parse the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all book containers on the page
        book_containers = soup.find_all('article', class_='product_pod')
        
        # Extract book information
        for book in book_containers:
            # Extract title
            title = book.h3.a['title']
            all_titles.append(title)

            # Extract price
            price = book.find('p', class_='price_color').text
            all_prices.append(price)

            # Extract star rating
            star_rating = book.find('p', class_='star-rating')['class'][1]
            all_ratings.append(star_rating)
    else:
        print(f"Failed to scrape page {page_num}")

# Create a DataFrame with all the collected data
all_books_df = pd.DataFrame({
    'Title': all_titles,
    'Price': all_prices,
    'Rating': all_ratings
})

# Clean the data
all_books_df['Price'] = all_books_df['Price'].str.replace('£', '').astype(float)
all_books_df['Rating'] = all_books_df['Rating'].map(rating_mapping)

# Display the result
print(f"Total books collected: {len(all_books_df)}")
all_books_df.head()
```

**Expected output:**
- Success messages for each page scraped
- DataFrame with approximately 60 books (20 from each page)
- Clean data with proper types

**Grading notes:**
- URL construction should handle the first page differently (base URL vs. pagination)
- Ethical scraping practices should be implemented (delay between requests)
- For loop should iterate through all three pages
- All data should be properly extracted and combined
- Final DataFrame should be created and data should be cleaned

### Section: Saving the Scraped Data

**Expected code execution:**
```python
# Save the DataFrame to a CSV file
books_df.to_csv('scraped_books.csv', index=False)
print("Data saved to 'scraped_books.csv'")
```

**Expected output:**
- Confirmation message that the file was saved

**Grading notes:**
- `.to_csv()` method should be used correctly
- `index=False` should be specified to avoid saving row numbers
- Appropriate filename should be used
- Success message should be displayed

## Common Student Mistakes and Troubleshooting

1. **Connection/HTTP errors**:
   - Problem: Website may block requests or connection issues may occur
   - Solution: Check headers, URL, and internet connection; try alternative sites if needed

2. **HTML structure misinterpretation**:
   - Problem: Students may misunderstand the structure of the HTML and use incorrect selectors
   - Solution: Encourage students to inspect the page source or use browser DevTools to verify selectors

3. **Missing error handling**:
   - Problem: Students often don't include checks for request success or error handling
   - Solution: Emphasize the importance of checking status codes and using try/except blocks

4. **Exceeding rate limits**:
   - Problem: Too many rapid requests without delays
   - Solution: Reinforce the ethical approach with time.sleep() between requests

5. **Incorrect data cleaning**:
   - Problem: Price conversion failures or rating mapping issues
   - Solution: Guide students to check data types and string formatting before conversion

6. **Challenge implementation issues**:
   - Problem: Pagination URLs constructed incorrectly
   - Solution: Provide hint about the different URL structure for page 1 vs. subsequent pages

## Additional Guidance Notes

### Ethical Web Scraping Emphasis

When reviewing student submissions, pay special attention to whether they've implemented ethical scraping practices:
- Appropriate delays between requests
- Proper headers identifying the purpose
- Checking robots.txt (mentioned in the notes)
- Only scraping necessary data

### Extension Ideas for Advanced Students

For students who complete the assignment early or are looking for more challenge:
1. Extract more detailed information (book descriptions, categories, availability)
2. Implement more robust error handling and retry mechanisms
3. Create data visualizations of the scraped information
4. Compare data across different book categories
5. Build a simple command-line interface for the scraper

### Assessment Rubric

| Criterion | Excellent (A) | Satisfactory (B-C) | Needs Improvement (D-F) |
|-----------|---------------|--------------------|-----------------------|
| Code Functionality | All sections work correctly, challenge implemented properly | Minor issues in implementation, challenge attempted | Major functionality issues, challenge not attempted |
| Web Scraping Technique | Correctly uses BeautifulSoup selectors, extracts all data properly | Basic extraction works, but some selectors could be improved | Incorrect selectors, fails to extract required information |
| Data Processing | Clean data transformation, proper handling of types | Basic cleaning implemented with minor issues | Missing or incorrect data cleaning |
| Ethical Practices | Implements all ethical considerations (headers, delays, etc.) | Basic ethical practices with some omissions | No consideration of ethical scraping practices |
| Code Quality | Well-organized, commented, efficient code | Functional code with minor inefficiencies | Poorly structured, inefficient, or uncommented code |

## Website Stability Note

The example website (books.toscrape.com) is a demonstration site designed for scraping practice. However, websites can change their structure or go offline. If students encounter issues with the site, here are some alternatives:
- quotes.toscrape.com (quotes and authors)
- www.scrapethissite.com (designed for practice)
- wikipedia.org (for stable, scrapable content)

## Resource Links for Students

Additional resources to share with students who need more help:
- BeautifulSoup documentation: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Web Scraping Ethics Guide: https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01
- Pandas Data Cleaning Tutorial: https://pandas.pydata.org/pandas-docs/stable/user_guide/text.html
- HTML/CSS Introduction: https://www.w3schools.com/html/
