---
title: "Broaden Your Horizons with Modules"
subtitle: "Using External Libraries to Elevate Your Python Programmes"
author: "Michael Borck"
format: 
  pptx: default
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

# Expanding Your Code with Modules

Welcome to Module 4! In this module, you'll learn how to import and use external modules to extend the capabilities of your code. For Information Systems students, understanding the Python ecosystem of business-relevant libraries is essential for building professional applications.

::: {.notes}
Modules are an essential part of expanding your code in Python. They allow you to access pre-written code and functionality, saving you time and effort. By importing modules, you can leverage the work of other developers and avoid reinventing the wheel. Modules also help keep your code organised and maintainable, as you can separate different parts of your program into distinct modules.

For Information Systems students, modules are particularly important because they provide access to the vast ecosystem of business-focused Python libraries. Whether you need to process CSV files, perform financial calculations, create user interfaces, or integrate with web services, there's likely a module that provides the functionality you need.

Understanding how to discover, evaluate, and integrate modules is a crucial skill for modern business application development. This becomes even more important when working with AI tools, which can help you find and implement appropriate modules for your specific business requirements.
:::

# Objectives

- Understand what modules are and why they are useful.
- Learn the basics of import syntax.
- See how pre-written libraries can simplify your coding tasks.
- Explore the Python ecosystem for business applications.
- Practice AI-assisted module discovery and evaluation.

::: {.notes}
Modules are self-contained units of code that can be imported into your Python programs to provide additional functionality. By breaking code into modules, you can make your programs more organised, easier to understand, and simpler to maintain. Modules also allow you to reuse code across multiple projects, saving time and effort.

In this presentation, we will cover the basics of import syntax, which is how you bring modules into your code. We will also explore how using pre-written libraries can simplify coding tasks and help you avoid reinventing the wheel. By the end of this presentation, you should have a solid understanding of what modules are, how to import them, and why they are such a valuable tool for Python programmers.
:::

# Import Syntax Basics

- **Using `import module`:**  
  This imports the entire module.  
  Example:
  ```python
  import datetime
  now = datetime.datetime.now()
  print("Current date and time:", now)
  ```
- **Using `from module import function`:**  
  This imports only the specific function you need.  
  Example:
  ```python
  from datetime import datetime
  now = datetime.now()
  print("Current date and time:", now)
  ```
- Choose the method based on your needs and the size of the module.

::: {.notes}
There are two main methods for importing modules in Python. The first method is using the `import module` syntax, which imports the entire module and requires you to prefix each function or variable with the module name when using them. The second method is using the `from module import function` syntax, which allows you to import specific functions or variables from a module directly into your namespace, so you can use them without the module prefix.

When deciding which method to use, consider the size of the module and your specific needs. If you only require a few functions from a large module, it may be more efficient to import them individually using the `from module import function` syntax. However, if you need to use many functions or variables from a module, or if you want to avoid potential naming conflicts, it may be better to use the `import module` syntax and prefix each function or variable with the module name.
:::

# Why Import Modules?

- **Reusability:**  
  Use pre-written, well-tested code to perform common tasks.
- **Organisation:**  
  Keep your code clean by separating functionality into different modules.
- **Efficiency:**  
  Save time by leveraging libraries that handle complex tasks for you.
- **Business Relevance:**  
  Modules like `datetime`, `csv`, and `pandas` are essential for business applications.
- **Professional Development:**  
  Understanding modules is crucial for modern software development workflows.

::: {.notes}
Importing modules in Python allows for reusability of code, enabling developers to leverage pre-existing functions and classes without having to write everything from scratch. This promotes organisation by keeping code modular and easy to maintain, as related functionality can be grouped together in separate modules. Efficiency is also improved, as importing modules reduces development time and allows for the use of optimised code written by experienced programmers.

From a business perspective, importing modules is highly relevant as it enables rapid development of robust, maintainable applications. By leveraging existing code, businesses can save time and resources, allowing them to focus on their core competencies and deliver value to their customers more quickly. Additionally, using well-established modules can help ensure the reliability and security of the application, which is crucial for businesses operating in today's digital landscape.
:::

# Simple Demonstration with the Datetime Module

Let's see a simple example using the `datetime` module:

```python
from datetime import datetime

# Get the current date and time
current_time = datetime.now()
print("Current date and time:", current_time)
```

This code snippet imports the `datetime` function from the datetime module, gets the current date and time, and prints it out. This can be very useful in business applications where tracking the current time is essential.

::: {.notes}
This slide demonstrates how to use the datetime module in Python to work with dates and times. The datetime module provides classes for manipulating dates and times, allowing you to perform operations such as formatting dates, calculating time differences, and handling time zones.

By importing the datetime module, you can easily create datetime objects representing specific dates and times. You can then use the various methods and attributes provided by the datetime classes to extract information like the year, month, day, hour, minute, and second from these objects. The datetime module also supports arithmetic operations on dates and times, enabling you to add or subtract time intervals and compare dates.
:::

# The Python Ecosystem for Business

**Essential Categories for Information Systems:**

**Data Processing:** `csv`, `pandas`, `openpyxl`  
**Financial Calculations:** `math`, `decimal`, `numpy`  
**User Interfaces:** `tkinter`, `streamlit`  
**Web Applications:** `flask`, `requests`  
**Date/Time:** `datetime`, `calendar`

::: {.notes}
Python's strength lies in its vast ecosystem of libraries designed for business applications. For Information Systems students, understanding which libraries solve common business problems can dramatically accelerate development and improve the quality of applications.

The data processing category becomes crucial as students work with CSV files, Excel spreadsheets, and eventually databases. Financial calculation libraries provide precision and advanced mathematical functions needed for business calculations. User interface libraries enable the creation of professional-looking applications.

As students progress through the course, they'll encounter many of these libraries. Week 8 will introduce data visualization libraries for their dashboard project, and the final project will bring together multiple libraries to create a comprehensive business application.
:::

# AI-Assisted Module Discovery

**Modern Development Workflow:**
1. Identify the business problem you're solving
2. Describe the problem to AI: "I need to work with CSV files in Python"  
3. Ask AI to compare options and recommend libraries
4. Request implementation examples and best practices
5. Evaluate AI's suggestions based on your requirements

**Example AI Prompt:**
"I'm building a finance application that needs to import transaction data from CSV files and calculate summary statistics. What Python libraries should I consider, and which would you recommend for a beginner?"

::: {.notes}
This workflow reflects how modern developers actually discover and evaluate libraries. AI tools excel at providing current information about the Python ecosystem, comparing library options, and suggesting implementations tailored to specific use cases.

For Information Systems students, this AI-assisted approach is particularly valuable because AI can bridge the gap between business requirements and technical implementation. Students can describe their business needs in natural language and get specific technical recommendations.

The key skill is learning to ask good questions and evaluate AI's suggestions based on factors like project requirements, learning curve, and long-term maintainability.
:::

# Activity: Explore Business-Relevant Modules

**Your Task:**

- Choose a business scenario: expense tracking, inventory management, or sales analysis
- Use AI to research relevant Python modules for your chosen scenario
- Write a small script that demonstrates 2-3 modules working together
- For example: use `datetime` to timestamp transactions and `csv` to save data

**Example Finance Script:**
```python
import datetime
import csv

def log_expense(amount, category, description):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Append to CSV file
    with open('expenses.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, amount, category, description])
    
    print(f"Logged: ${amount:.2f} for {category} at {timestamp}")

# Test the function
log_expense(45.50, "Food", "Lunch at restaurant")
```

Explore how combining modules creates powerful business functionality!

::: {.notes}
This activity combines multiple modules to solve a realistic business problem, demonstrating how individual modules work together to create useful applications. The expense logging example shows students how simple modules can be combined to create genuinely useful business functionality.

Students practice the complete workflow: identifying business requirements, researching appropriate modules, and implementing a solution. This mirrors the development process they'll use in more complex projects throughout the course.

The activity also introduces file I/O concepts that will be important in later weeks when students work with larger datasets and need to persist information between program runs.
:::

# Module Journey in Your Finance App

- **datetime:** Timestamp transactions and track spending patterns over time
- **csv:** Import/export financial data and create reports  
- **math/decimal:** Perform precise financial calculations
- **Your custom modules:** Week 5 finance toolkit functions

**Looking Ahead:** Week 8 will introduce data visualization libraries (`matplotlib`, `plotly`) for your interactive dashboard project.

::: {.notes}
This progression shows students how module usage builds throughout the course, with each week adding new capabilities to their growing finance application. The datetime module they learn about here becomes essential for time-based analysis in later projects.

Students can see how modules aren't just isolated tools—they work together to create comprehensive business applications. The custom modules they'll create in Week 5 (their own finance functions) will work alongside these standard library modules.

This forward-looking perspective helps students understand that they're building toward something substantial and professional, where multiple libraries combine to create powerful business applications.
:::

