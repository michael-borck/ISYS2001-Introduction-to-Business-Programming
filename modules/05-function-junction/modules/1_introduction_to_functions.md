---
title: "Unlock the Power of Functions"
subtitle: "Your First Step to Organised Python Code"
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
# Welcome to Functions in Python

Welcome to our introduction to functions! In this module, you'll learn how functions help make your Python code more organised and easier to manage. Functions are the building blocks of all professional applications—including the finance apps you'll build this semester.

::: {.notes}
Welcome to Functions in Python! Functions are a fundamental concept in programming that allow you to organise your code into reusable blocks. By defining a function, you can encapsulate a specific task or computation, making your code more modular, readable, and maintainable.

In this presentation, we will explore what functions are, why they are useful, and how to define and call them in Python. We will cover the syntax for defining a function, including the def keyword, function name, parameters, and return values. Additionally, we will discuss how to call a function and pass arguments to it. 

For Information Systems students, functions are particularly important because they mirror how business processes work—taking inputs, processing them, and producing outputs. Throughout this course, you'll use functions to build financial calculators, expense trackers, and eventually an interactive finance dashboard. By the end of this presentation, you will have a solid foundation in working with functions in Python.
:::

# What is a Function?

- A function is a reusable block of code that performs a specific task.
- Think of it like a mini-program that you can call whenever you need it.
- Using functions helps you avoid writing the same code over and over.

::: {.notes}
A function is a reusable block of code that performs a specific task, like a mini-program that you can call whenever you need it. By using functions, you can avoid writing the same code repeatedly, making your programs more efficient and easier to maintain.

Functions are a fundamental concept in programming and are essential for writing modular, reusable code. In this presentation, we'll explore why functions are useful, how to define and call them in Python, and see some examples of how they can be used to streamline your code.
:::

# Why Use Functions?

- **Organisation:** Break your code into manageable pieces.
- **Reusability:** Write a piece of code once and use it many times.
- **Clarity:** Make your programme easier to read and understand.
- **Business Logic:** Model real-world processes like calculating interest or categorising expenses.

::: {.notes}
Functions are an essential tool for organising code into manageable pieces, making it more readable and understandable. By breaking down a programme into smaller, self-contained functions, each responsible for a specific task, the overall structure becomes clearer and easier to follow. This modular approach helps to reduce complexity and makes the code more maintainable, as changes can be made to individual functions without affecting the rest of the programme.

Functions also promote code reusability, allowing a piece of code to be written once and used multiple times throughout the programme. This eliminates the need for duplicating code, saving time and effort, and reducing the likelihood of errors. By encapsulating a specific task within a function, it can be called whenever that functionality is needed, leading to more efficient and streamlined code.

For business applications, functions naturally mirror business processes. For example, a "calculate_monthly_payment" function takes loan details as input and returns a payment amount—just like a loan calculator would. A "categorise_expense" function takes an expense amount and returns whether it's a major, moderate, or minor expense—automating a decision process. This alignment between functions and business logic makes code easier for non-programmers to understand and maintain.
:::

# Defining a Function

- Functions are defined with the keyword `def`.
- The basic syntax is:
  ```python
  def function_name():
      # code goes here
  ```
- Remember: The code inside the function must be indented.

::: {.notes}
Here are the presenter notes for the "Defining a Function" slide:

To define a function in Python, we use the `def` keyword followed by the function name and parentheses. Inside the parentheses, we can specify parameters that the function accepts. After the parentheses, we add a colon to indicate the start of the function block. The basic syntax is shown on the slide, where `function_name` is a descriptive name for the function and `parameter1`, `parameter2`, etc. are optional parameters that the function can receive.

It's crucial to remember that the code inside the function must be indented. Python uses indentation to define code blocks, so all the statements that are part of the function must be indented consistently, typically with four spaces or a tab. This indentation distinguishes the function body from the rest of the code. Failing to indent properly will result in syntax errors.
:::

# Calling a Function

- After you define a function, you need to call it to make it run.
- Example:
  ```python
  def say_hello():
      print("Hello, everyone!")
  
  say_hello()  # This line calls the function
  ```
- **Note:** The function definition must appear before you call the function.

::: {.notes}
After defining a function in Python, you must call it to execute the code within the function. The function call instructs Python to run the code inside the function, allowing you to utilise the function's functionality. For example, if you have defined a function named `greet()`, you can call it by simply writing `greet()` in your Python script.

It is crucial to remember that the function definition must appear before the function call in your Python script. Python reads the script from top to bottom, so if you attempt to call a function before it has been defined, you will encounter an error. By ensuring that your functions are defined before they are called, your script will execute smoothly and without issues.
:::

# Recap

- A function is a way to bundle code that performs a task.
- Defining and calling functions makes your code less repetitive and more organised.
- In your upcoming lab, you'll get hands-on experience writing and using functions!

Take a moment to review these ideas, and get ready to explore functions in our lab session. Happy coding!

::: {.notes}
Here are the presenter notes for the "Recap" slide:

Functions are a fundamental concept in Python programming that allow you to encapsulate code performing a specific task into a reusable unit. By defining functions, you can avoid repetition in your code and improve its overall structure and readability. Functions also promote modular design, as you can break down complex problems into smaller, more manageable parts.

In the upcoming lab, you will gain practical experience in defining and invoking functions. This hands-on practice will reinforce your understanding of how functions work and how they can be effectively used to solve problems. By writing and using functions yourself, you will develop a deeper appreciation for their benefits and learn how to incorporate them into your own Python programs.
:::

# Functions in the AI Era

- **Why Functions Matter with AI:** AI tools work best when you understand code structure
- **Professional Reality:** Even with AI assistance, you need to understand what functions do
- **Learning Strategy:** Use AI to explain functions, not replace understanding them
- **Business Impact:** Functions help you direct AI to build the right solutions

::: {.notes}
In today's programming landscape, AI tools can generate function code quickly, but understanding function structure, purpose, and design principles becomes even more critical. Functions are the building blocks that AI uses to create larger programs, so understanding them helps you become a better AI collaborator.

When you understand functions, you can better evaluate AI-generated code, request specific functionality, and integrate AI solutions into larger systems. For Information Systems professionals, this means you can effectively bridge between business requirements and technical implementation, using AI as a powerful tool rather than a black box.

The most successful AI collaborations happen when humans understand the architectural patterns (like functions) and can guide AI tools to implement specific business logic within those patterns.
:::

# Activity: Create Your Own Finance Function

Try writing your very own function! Instead of a greeting, let's create something useful for your finance projects.

**Task:**  
- Write a function named `calculate_tip()` that:
  - Asks the user for a bill amount
  - Asks for the tip percentage they want to give
  - Calculates and prints the tip amount and total bill

Take a few minutes to try it out!

::: {.notes}
In this activity, you will create your own finance-related function called `calculate_tip()`. This function demonstrates how programming concepts apply to everyday financial calculations that Information Systems professionals might need to automate.

The function will use the built-in `input()` function to gather financial data from the user, perform calculations, and provide useful output. This mirrors the pattern you'll use throughout the course for building financial tools—get input, process it according to business rules, and provide meaningful results.

This type of function could be part of a larger expense tracking system, restaurant management application, or personal finance tool. By starting with simple, relatable financial calculations, you're building the foundation for more sophisticated business applications.
:::

# Answer: A Finance Calculation Function

Here's one way to write the `calculate_tip()` function:

```python
def calculate_tip():
    bill_amount = float(input("Enter the bill amount: $"))
    tip_percentage = float(input("Enter tip percentage (e.g., 18 for 18%): "))
    
    tip_amount = bill_amount * (tip_percentage / 100)
    total_bill = bill_amount + tip_amount
    
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total bill: ${total_bill:.2f}")
    
calculate_tip()  # Calling the function to see it in action
```

This function demonstrates key concepts you'll use throughout your finance projects: getting user input, performing calculations, and formatting financial output.

::: {.notes}
This finance-focused example demonstrates several important concepts for Information Systems students. First, it shows how functions can encapsulate business logic—in this case, the standard process of calculating tips and totals. The function uses float() to handle decimal numbers, which is essential for financial calculations.

The formatting with :.2f ensures that monetary amounts display with exactly two decimal places, following standard financial formatting conventions. This attention to proper formatting is crucial in business applications where precision and presentation matter.

This type of function illustrates how programming concepts directly apply to business processes. Students can see how the same pattern—input, process, output—will apply to more complex financial calculations like loan payments, investment returns, or budget analysis throughout the course.
:::

# From Simple Functions to Finance Apps

- **Week 5:** These functions become your finance calculator toolkit
- **Week 8:** Enhanced with data processing for comprehensive analysis
- **Final Project:** Interactive dashboard built from functions like these
- **Career Preparation:** Professional developers think in functions first

::: {.notes}
This progression shows students how their learning builds systematically toward practical applications. The simple tip calculator function they just wrote uses the same fundamental pattern as sophisticated financial software—it just operates on different data and implements different business rules.

By Week 5, students will create modular finance functions for expense categorisation, budget analysis, and financial projections. Week 8 introduces data processing libraries that make these functions more powerful. The final project brings everything together in an interactive dashboard that could genuinely be useful for personal finance management.

For Information Systems majors, this progression is particularly relevant because it mirrors how business software is actually built—starting with core business logic functions and gradually adding layers of sophistication, user interface, and data integration.
:::

