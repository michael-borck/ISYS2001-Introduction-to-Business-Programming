---
title: "Module 1: Understanding Data, Values, and Data Types"
subtitle: "Data Demystified: Unlocking the Building Blocks of Your Digital World"
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
# Module Overview

In this module we will:
- Define what data is.
- Explore basic data types in Python.
- Understand how variables store data.
- Connect these ideas to our User Preferences project.

::: {.notes}
This slide provides an overview of the module, outlining the key topics that will be covered. We'll start by defining what data is and exploring some real-life examples to help contextualise the concept. Then, we'll dive into the basic data types in Python, such as integers, floats, strings, and booleans, and see how they're used in practice.

Next, we'll learn about variables and how they store data in Python programs. We'll discuss naming conventions, assignment, and reassignment of values. Finally, we'll connect these ideas to our User Preferences project, demonstrating how the concepts covered in this module are applied in a practical setting. Throughout the module, there will be hands-on activities to reinforce your understanding of the material.
:::

# What is Data?

- Data is information that is stored and processed by a computer.
- It can be numerical, textual, or a combination of both.
- In programming, data is the foundation on which our programmes operate.

::: {.notes}
Data is the foundation of all computer programs. It encompasses numerical values, text, or a combination of both, providing the raw material that software manipulates and processes. Without data, programs would have nothing to operate on, making it a crucial component in the field of programming.

In the context of Python programming, data is categorised into various types, each with its own characteristics and uses. These basic data types include integers for whole numbers, floats for decimal values, strings for textual information, and booleans for true/false values. Understanding these data types and how to work with them effectively is essential for writing functional and efficient Python code.
:::

# Real-Life Examples of Data

- Consider a student's details: name, age, and favourite colour.
- Everyday examples include shopping lists or contact records.
- In our User Preferences project, data represents the choices made by users.

::: {.notes}
This slide illustrates real-life examples of data to help students grasp the concept more tangibly. A student's details, such as their name, age, and favourite colour, serve as a relatable example. Similarly, everyday instances like shopping lists or contact records demonstrate how data is used in our daily lives.

In the context of our User Preferences project, data represents the choices made by users. This practical application highlights the relevance of data in real-world scenarios and reinforces the importance of understanding data for the students' future projects and endeavours.
:::

# Basic Data Types in Python

Python supports several basic data types:
- **Integers:** Whole numbers (e.g., 5, -3)
- **Floats:** Decimal numbers (e.g., 3.14, -0.001)
- **Strings:** Text (e.g., "hello", "favourite")
- **Booleans:** True or False values

::: {.notes}
In Python, there are four fundamental data types: integers, floats, strings, and booleans. Integers are whole numbers, both positive and negative, such as 5 or -3. Floats, on the other hand, are decimal numbers like 3.14 or -0.001. Strings represent text and are enclosed in double quotes, for example, "hello" or "favourite".

Booleans are a special data type that can only have two values: True or False. They are used to represent the truth or falsity of a condition or statement in Python. It's crucial to understand these basic data types as they form the building blocks for more complex data structures and algorithms in Python programming.

Integers are use to 'count', floats are used to 'measure', strings are used to 'label' and booleans are used to 'choose'.
:::

# Data Types in Context

- A student’s age as an integer.
- A rating or score as a float.
- A user’s name or favourite colour as a string.
- A confirmation (yes/no) as a Boolean.
- These examples are directly related to our User Preferences project.

::: {.notes}
In this slide, we explore how basic data types are applied in a real-world context, specifically within our User Preferences project. We see that an integer can be used to represent a student's age, while a float is suitable for storing a rating or score. When dealing with textual information, such as a user's name or favourite colour, we utilise strings. Lastly, Boolean values are employed to capture binary choices, like a yes/no confirmation.

These practical examples demonstrate the relevance and importance of selecting the appropriate data type for each piece of information we intend to work with. By understanding how to apply these data types in a meaningful way, we can ensure that our code is efficient, readable, and maintainable. As we progress through the User Preferences project, we will continue to encounter scenarios where choosing the correct data type is crucial for the success of our program.
:::

# Understanding Variables

- Variables are named containers that hold data.
- The value stored in a variable determines its data type.
- Variables allow us to refer to data by name, making our code clearer.
- They stand in for the data itself when performing operations.

::: {.notes}
Variables are named containers that store data, allowing us to refer to it by name and making our code more readable. The value held in a variable determines its data type, such as integers, floating-point numbers, or strings. By using variables, we can perform operations on the data without directly referencing the values themselves.

Variables play a crucial role in programming by providing a way to label and manipulate data effectively. They enable us to assign meaningful names to our data, making the code more self-explanatory and easier to understand. When we need to use or modify the data, we simply refer to the variable name instead of the actual value, which simplifies the coding process and reduces the likelihood of errors.
:::

# Hands-On Activity

**Task:**  
- Write a short Python programme to create and display variables.  
- For example:
  - `name = "Alice"`
  - `age = 25`
  - `favourite_colour = "blue"`
- Use `print()` to display each variable.
- Reflect on how the variable names clarify the type and purpose of the data.

::: {.notes}
In this hands-on activity, you will write a short Python programme to create and display variables. The example provided demonstrates how to assign values to variables with descriptive names such as 'name', 'age', and 'favourite_colour'. After assigning the values, you will use the print() function to display each variable.

As you work through this activity, reflect on how the variable names help clarify the type and purpose of the data they store. Well-chosen variable names make your code more readable and easier to understand, both for yourself and others who may work with your code in the future. This is an important practice to develop as you continue learning and writing Python programmes.
:::

