---
title: "Broaden Your Horizons with Modules"
subtitle: "Using External Libraries to Elevate Your Python Programmes"
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

# Expanding Your Code with Modules

Welcome to Module 4! In this module, you'll learn how to import and use external modules to extend the capabilities of your code. For business information students, using modules like `datetime` can be very practical.

::: {.notes}
Modules are an essential part of expanding your code in Python. They allow you to access pre-written code and functionality, saving you time and effort. By importing modules, you can leverage the work of other developers and avoid reinventing the wheel. Modules also help keep your code organised and maintainable, as you can separate different parts of your program into distinct modules.

In this slide, we'll explore the basics of importing modules and discuss why they are so useful. We'll also look at a simple demonstration using the datetime module to show how easy it is to start using modules in your own code. By the end of this section, you'll have a good understanding of how to use modules to expand the capabilities of your Python programs.
:::

# Objectives

- Understand what modules are and why they are useful.
- Learn the basics of import syntax.
- See how pre-written libraries can simplify your coding tasks.

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
  Modules like `datetime` are essential for tasks such as time-stamping transactions or scheduling.

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

# Activity: Explore a Module

**Your Task:**

- Write a small script that imports the `datetime` module.
- Use it to display:
  - The current date.
  - The current time.
- Experiment with formatting the output using the module's features (for example, displaying just the date or time).

Take some time to explore how modules can make your code more powerful and applicable to real-world business scenarios.

Happy coding, and enjoy expanding your Python skills with modules!

::: {.notes}
In this activity, you will explore the `datetime` module by writing a small script that imports it. The script should use the module to display the current date and time. Experiment with formatting the output using the module's features, such as displaying just the date or time.

The `datetime` module is a powerful tool for working with dates and times in Python. By learning how to use this module, you will be able to incorporate date and time functionality into your programs, which can be useful for a wide range of applications, such as scheduling, logging, and data analysis.
:::

