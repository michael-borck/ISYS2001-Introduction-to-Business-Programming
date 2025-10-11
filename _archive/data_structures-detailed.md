---
author: Michael Borck
format:
  docx:
    highlight-style: github
    toc: false
  html:
    embed-resources: true
    toc: true
    toc-expand: 2
  pdf:
    colorlinks: true
    toc: false
  pptx:
    reference-doc: ../../_assets/template.pptx
title: 'Mastering Python''s Data Structures: Unleashing Weather Insights'
---

# Copyright
![](../../_assets/curtin-copy-right.png)

# Acknowledgement of Country
I acknowledge the traditional custodians of the land on which I work and live,
and recognise their continuing connection to land, water and community. I pay
respect to Elders past, present and emerging.

![](../../_assets/ack_country.png)

# Agenda

1. Introduction to Data Structures
2. Lists and Tuples
3. Dictionaries and Sets
4. Weather Data Analysis Example
5. Practical Applications
6. Summary and Conclusion

# Introduction to Data Structures

- What are data structures?
- Why are they important?
  - Efficient data organisation and manipulation
  - Fundamental in programming
- Python's built-in data structures
- Role in solving complex problems

# Lists: Dynamic and Versatile

- Ordered, mutable sequences
- Characteristics:
  - Store various data types
  - Accessed by index
  - Flexible sise
- Syntax: `[1, 'apple', 3.14]`

## List Operations

- Adding elements: `append()`, `insert()`
- Removing elements: `remove()`, `pop()`
- Slicing and indexing
- Sorting and reversing
- List comprehensions

# Tuples: Immutable Collections

- Ordered, immutable sequences
- Key features:
  - Similar to lists, but unchangeable
  - Defined using parentheses
  - Faster than lists for read-only operations
- Syntax: `(1, 'apple', 3.14)`

## Tuple Operations

- Accessing elements by index
- Slicing and concatenation
- Unpacking tuples
- Converting to/from lists
- Use cases: return values, dictionary keys

# Dictionaries: Key-Value Mappings

- Unordered, mutable mappings
- Structure:
  - Key-value pairs
  - Keys must be unique and immutable
- Fast value retrieval
- Syntax: `{'name': 'John', 'age': 30}`

## Dictionary Operations

- Adding and updating key-value pairs
- Accessing values by key
- `get()` method for safe access
- Iterating over keys, values, and items
- Dictionary comprehensions

# Sets: Unique Element Collections

- Unordered, mutable collections of unique elements
- Key features:
  - No duplicates allowed
  - Fast membership testing
  - Mathematical set operations
- Syntax: `{1, 2, 3}`

## Set Operations

- Adding and removing elements
- Union, intersection, difference
- Checking subset and superset relationships
- Eliminating duplicates from other collections
- Set comprehensions

# Weather Data Analysis Example

## Scenario
Analysing temperature data for a weather station

## Data Structure Choice
- Lists: Store daily temperature readings
- Dictionaries: Organise data by date and location
- Sets: Track unique observation dates

## Sample Data
```python
weather_data = {
    '2023-08-01': {'temp': [22.5, 23.1, 24.0, 23.8, 22.9], 'location': 'City A'},
    '2023-08-02': {'temp': [21.8, 22.7, 23.5, 23.1, 22.0], 'location': 'City A'},
    # ... more data ...
}
```

# Calculating Averages

```python
def calculate_average_temp(temperatures):
    return sum(temperatures) / len(temperatures) if temperatures else None

avg_temps = {date: calculate_average_temp(data['temp']) 
             for date, data in weather_data.items()}
```

- Demonstrates use of dictionaries and list operations
- Handles potential empty lists
- Uses dictionary comprehension for concise code

# Finding Extremes

```python
def find_temp_extremes(temperatures):
    return (min(temperatures), max(temperatures)) if temperatures else (None, None)

temp_extremes = {date: find_temp_extremes(data['temp']) 
                 for date, data in weather_data.items()}
```

- Shows tuple usage for returning multiple values
- Utilises min() and max() functions
- Demonstrates error handling for empty lists

# Extracting Specific Information

```python
hot_days = {date for date, data in weather_data.items() 
            if max(data['temp']) > 25}

city_a_data = {date: data for date, data in weather_data.items() 
               if data['location'] == 'City A'}
```

- Utilises set and dictionary comprehensions
- Demonstrates filtering data based on conditions
- Shows how to combine different data structures

# Practical Applications

1. Data Analysis and Visualisation
   - Pandas for data manipulation
   - Matplotlib/Seaborn for plotting

2. Database Management
   - Using dictionaries to represent database records
   - Lists for query results

3. Machine Learning and AI
   - NumPy arrays (built on lists) for efficient computations
   - Dictionaries for feature engineering

4. Web Development and APIs
   - JSON data (similar to dictionaries) for data exchange
   - Lists for handling multiple records

# Summary and Conclusion

- Explored Python's core data structures:
  - Lists: Dynamic, ordered collections
  - Tuples: Immutable, ordered collections
  - Dictionaries: Key-value mappings
  - Sets: Unique element collections
- Applied these structures to weather data analysis
- Demonstrated practical coding examples
- Discussed real-world applications

## Key Takeaway
Mastering these data structures is crucial for efficient and effective Python programming across various domains.

# Questions and Discussion

- What other data structures might be useful for weather analysis?
- How might we optimise our code for larger datasets?
- Any specific areas you'd like to explore further?

Thank you for your attention!