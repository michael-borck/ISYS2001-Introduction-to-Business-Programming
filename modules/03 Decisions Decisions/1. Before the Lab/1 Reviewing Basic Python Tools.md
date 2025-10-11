---
title: "Reviewing Basic Python Tools"
subtitle: "Basic Python Tools"
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

# Overview
In this module we will review the essential Python tools you need to get started with programming.  
We'll explore how to display messages with `print()`, capture user input with `input()`, and work with variables and basic data types.  
Let’s begin our journey into Python!

::: {.notes}
Welcome to the exciting world of Python programming! In this introductory workshop, we'll explore the fundamentals of Python and equip you with the knowledge and skills to start your programming journey.

Throughout the session, we'll cover essential topics such as using the `print()` function to display output, interacting with users through the `input()` function, working with variables to store and manipulate data, and introducing the basic primitive data types in Python. By the end of the workshop, you'll have a solid foundation to build upon as you continue learning and practising Python programming.
:::

# Understanding `print()`
- The `print()` function is used to display information on the screen.
- It is a fundamental tool for debugging and communicating with the user.
- Example:
  
  ```python
  print("Hello, world!")
  ```
  
- Notice how the text is enclosed in quotes.

::: {.notes}
The `print()` function displays information on the screen and is enclosed in parentheses. Text to be printed must be enclosed in quotes, either single ('') or double (""). The `print()` function is a fundamental tool for debugging code and communicating with the user, as it allows the programmer to display messages or values at specific points in the program's execution.

In this slide, we introduce the basic syntax and usage of the `print()` function. We highlight the importance of enclosing the text to be printed in quotes, which is a common mistake made by beginners. We also discuss the role of `print()` in debugging and interacting with users, setting the stage for more advanced topics in future slides.
:::

# Exploring `input()`
- The `input()` function allows your programme to receive data from the user.
- It pauses programme execution until the user enters some text.
- Example:
  
  ```python
  name = input("What is your name? ")
  print("Hello, " + name + "!")
  ```
  
- This is the first step to making your programme interactive.

::: {.notes}
The `input()` function is a powerful tool in Python that enables your programme to accept user input, making it interactive and dynamic. When `input()` is called, the programme pauses execution and waits for the user to enter some text, which can then be stored in a variable for further processing.

To demonstrate the usage of `input()`, consider the following example code: `name = input("Please enter your name: ")`. In this case, the programme will display the prompt "Please enter your name: " and wait for the user to type in their name, which will be assigned to the variable `name`. This basic example illustrates how `input()` can be used to create engaging and responsive programmes that adapt to user input.
:::

# Working with Variables
- Variables are used to store data values.
- A variable is created the moment you assign it a value using the equals sign (`=`).
- Example:
  
  ```python
  age = 25
  print("Age:", age)
  ```
  
- Variables can hold different types of data, such as numbers or text.

::: {.notes}
Variables are fundamental building blocks in programming, allowing you to store and manipulate data values. To create a variable, you simply assign it a value using the equals sign (`=`). For example, `x = 5` creates a variable named `x` and assigns it the value of 5. Variables can hold various types of data, such as numbers (integers or floats) and text (strings).

It's crucial to choose meaningful variable names that reflect the purpose or content of the data they hold. This enhances code readability and makes it easier to understand and maintain your programs. As you progress in your programming journey, you'll encounter more complex data types and learn how to perform operations and calculations using variables. Mastering the concept of variables is a key step in becoming a proficient programmer.
:::

# Introduction to Primitive Data Types
- **Strings:** Text enclosed in quotes (e.g., `"sunny"`).
- **Integers:** Whole numbers (e.g., `10`).
- **Floats:** Numbers with decimal points (e.g., `3.14`).
- **Booleans:** `True` or `False` values.
- Example:
  
  ```python
  temperature = 20.5   # Float
  weather = "cloudy"   # String
  is_raining = False   # Boolean
  ```

::: {.notes}
In this slide, we introduce the four primitive data types in programming: strings, integers, floats, and booleans. Strings are used to represent text and are enclosed in quotes, such as "sunny". Integers are whole numbers like 10, while floats are numbers with decimal points, such as 3.14. Booleans, on the other hand, represent true or false values.

By understanding these primitive data types, you'll be able to effectively store and manipulate different kinds of data in your programs. Whether you're working with text, whole numbers, decimal numbers, or true/false values, these data types form the foundation of your programming toolkit. We'll explore an example that demonstrates how these data types can be used in practice.
:::

# Putting It All Together
- Let’s combine what we’ve learnt:
  1. Display a message with `print()`.
  2. Capture user input using `input()`.
  3. Store the input in a variable.
- Example programme:
  
  ```python
  print("Welcome to the weather programme!")
  temp = input("Enter the current temperature: ")
  print("You entered", temp, "degrees.")
  ```
  
- This simple code snippet demonstrates how our tools work in harmony.

::: {.notes}
Let's take a moment to consolidate our newfound knowledge by examining a concise code example that seamlessly integrates the concepts we've covered. This example will showcase the interplay between `print()`, `input()`, variables, and primitive data types, providing a clear demonstration of how these fundamental building blocks come together to create a functional program.

By dissecting this code snippet, we'll gain a deeper appreciation for the way these elements interact and contribute to the overall functionality of the program. This hands-on approach will reinforce our understanding of the core concepts and serve as a foundation for tackling more complex programming challenges in the future.
:::

# Summary and Next Steps
- In this module we reviewed:
  - The `print()` function for output.
  - The `input()` function for gathering user input.
  - How to create and use variables.
  - Basic data types in Python.
- With these fundamentals in place, you’re well-prepared to tackle more complex projects.
- Up next, we will begin exploring decision making with conditionals in our weather forecasting project.

::: {.notes}
In this module, we reviewed the fundamental concepts of Python programming, including the `print()` function for displaying output, the `input()` function for gathering user input, and the creation and use of variables. We also introduced the basic data types in Python, such as integers, floats, and strings, which form the building blocks of more complex programs.

With a solid grasp of these essential concepts, you are now well-equipped to take on more challenging projects and explore the vast possibilities that Python offers. In the upcoming module, we will delve into decision making using conditionals, which will allow you to create more dynamic and interactive programs. This knowledge will be applied to our exciting weather forecasting project, where you will have the opportunity to put your newfound skills into practice.
:::

