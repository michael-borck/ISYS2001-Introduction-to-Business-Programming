---
title: "Module 4: Variables and Operations"
subtitle: "Storing and Manipulating Data in Python: Turning Data into Action"
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
# Module 4: Variables and Operations

Welcome to Module 4. In this module, we learn how variables not only store data but also work with operations to manipulate that data. These skills are key to personalising our User Preferences project by performing calculations and customising outputs.

::: {.notes}
In this module, we will explore the fundamental concepts of variables and operations in programming. We will start by reviewing what variables are and how they are used to store and manipulate data. The assignment operator will be introduced, along with the concept of reassigning variables to new values. We will then dive into the basic arithmetic operations that can be performed on variables, such as addition, subtraction, multiplication, and division.

The order of precedence for these operations will be discussed, highlighting the importance of understanding how expressions are evaluated. We will look at examples using preference-related data to illustrate how variables and operations can be used in real-world scenarios. The module will include a hands-on activity to reinforce the concepts covered and provide an opportunity for practice. Finally, we will summarise the key points and reflect on the significance of variables and operations in programming.
:::

# Review of Variables

- Variables are named containers that hold data.
- They make it easier to reference and manipulate data in your code.
- A variable’s type is determined by the data it holds (e.g., integer, float, string, Boolean).

::: {.notes}
Variables are named containers that store data within a program, making it easier to reference and manipulate information throughout the code. The type of data a variable holds determines its classification, such as integer, float, string, or Boolean.

Understanding variables is essential for writing efficient and organised code. By assigning meaningful names to variables, programmers can create more readable and maintainable programs, reducing the likelihood of errors and making it simpler to modify the code in the future.
:::

# The Assignment Operator

- The assignment operator (`=`) is used to store a value in a variable.
- Example:
  ```python
  name = "Alice"
  age = 30
  ```
- It assigns the value on the right to the variable on the left.

::: {.notes}
The assignment operator (`=`) is used to store a value in a variable. For example, if we write `x = 5`, the value 5 is assigned to the variable `x`. The assignment operator always assigns the value on the right side of the equals sign to the variable on the left side.

It's crucial to understand how the assignment operator works, as it forms the basis for storing and manipulating data in variables. Throughout this module, we'll explore how to assign values to variables, reassign those values, and perform basic arithmetic operations using the variables. Mastering the assignment operator is a fundamental step in learning to program effectively.
:::

# Reassigning Variables

- Variables can be updated or reassigned.
- Example:
  ```python
  age = 30
  age = age + 1  # Now, age becomes 31
  ```
- This flexibility lets us perform calculations and update data as needed.

::: {.notes}
Variables in programming can be reassigned to new values as needed, providing flexibility for performing calculations and updating data. The example code snippet on the slide demonstrates this concept by initially assigning a value to a variable, then reassigning it to a new value later in the code.

Reassigning variables allows programmers to work with changing data throughout the execution of a program. By updating variables with new values, complex calculations can be performed, user input can be incorporated, and the program can respond to changing conditions dynamically.
:::

# Basic Arithmetic Operations

- Python supports several arithmetic operators:
  - Addition (`+`)
  - Subtraction (`-`)
  - Multiplication (`*`)
  - Division (`/`)
  - Floor Division (`//`)
  - Modulus (`%`)
  - Exponentiation (`**`)
- These operations let you perform calculations using variables.

::: {.notes}
Python supports several arithmetic operators for performing calculations using variables. These include addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), floor division (`//`), modulus (`%`), and exponentiation (`**`). By utilising these operators, you can manipulate numeric values stored in variables to carry out mathematical operations within your Python code.

The slide "Basic Arithmetic Operations" is part of Module 4, which focuses on variables and operations. This module covers topics such as reviewing variables, the assignment operator, reassigning variables, order of precedence, and examples using preference-related data. The slide itself is followed by a hands-on activity to reinforce the concepts and a summary and reflection section to consolidate the learnings from the module.
:::

# Order of Precedence

- Python evaluates expressions in a specific order:
  1. Parentheses `()`
  2. Exponentiation `**`
  3. Multiplication, Division, Floor Division, Modulus (`*`, `/`, `//`, `%`)
  4. Addition and Subtraction (`+`, `-`)
- For example:
  ```python
  result = 2 + 3 * 4  # Evaluates as 2 + (3 * 4) = 14
  ```

::: {.notes}
Python evaluates expressions in a specific order, known as the order of precedence or operator precedence. This order determines which operations are performed first when an expression contains multiple operators. For example, multiplication and division have higher precedence than addition and subtraction, so they are evaluated first in an expression like "2 + 3 * 4". Understanding the order of precedence is crucial for writing correct and efficient Python code.

The order of precedence in Python follows the common mathematical conventions, with parentheses having the highest precedence, followed by exponentiation, multiplication and division, and finally addition and subtraction. When operators have the same precedence, they are evaluated from left to right. It's important to use parentheses to explicitly specify the desired order of evaluation when multiple operators are involved, as this can make the code more readable and prevent unintended results.
:::

# Examples Using Preference-Related Data

- Suppose you want to calculate the total cost of a selected item including tax:
  ```python
  base_price = 20
  tax_rate = 0.1
  total_cost = base_price + (base_price * tax_rate)
  print("Total cost is", total_cost)
  ```
- Such examples show how arithmetic operations help personalise data based on user preferences.

::: {.notes}
The slide titled "Examples Using Preference-Related Data" demonstrates how arithmetic operations can be used to personalise data based on user preferences. The example provided calculates the total cost of a selected item, including tax, which showcases how basic math can be applied to real-world scenarios in programming.

This slide is part of the larger module on "Variables and Operations", which covers essential concepts such as the assignment operator, reassigning variables, basic arithmetic operations, and order of precedence. By presenting practical examples like calculating total cost with tax, the slide helps learners understand the relevance and utility of these fundamental programming concepts in creating dynamic, user-centric applications.
:::

# Hands-On Activity

**Task:**  
- Write a simple programme that:
  1. Asks the user for their current age and their birth year.
  2. Uses arithmetic operations to calculate the expected age by subtracting the birth year from the current year.
  3. Displays a confirmation message with the calculated age.
- This exercise will reinforce using variables, the assignment operator, and basic arithmetic in a real-world context.

::: {.notes}
In this hands-on activity, students will write a simple programme that reinforces the use of variables, the assignment operator, and basic arithmetic operations. The exercise will provide a real-world context for students to apply these fundamental programming concepts.

The activity will challenge students to create a programme that demonstrates their understanding of the topics covered in the previous slides, such as declaring and reassigning variables, using the assignment operator, and performing arithmetic operations while considering the order of precedence rules. By completing this practical exercise, students will gain hands-on experience and solidify their knowledge of these essential programming concepts.
:::

# Summary and Reflection

- We reviewed how variables store data and how the assignment operator works.
- We explored basic arithmetic operators and their order of precedence.
- These concepts empower you to perform dynamic calculations in your User Preferences project.
- Reflect on how these operations can be applied to personalise data in future projects.
```

::: {.notes}
In this presentation, we reviewed the fundamental concepts of variables and operations in programming. We started by discussing how variables store data and how the assignment operator is used to assign values to variables. We also explored the concept of reassigning variables, which allows us to update the value stored in a variable throughout the program's execution.

Next, we delved into the world of basic arithmetic operations, including addition, subtraction, multiplication, and division. We examined the order of precedence, which determines the sequence in which operations are performed in an expression. To solidify these concepts, we looked at examples using preference-related data, demonstrating how these operations can be applied to personalise data in real-world scenarios. Finally, we engaged in a hands-on activity to put our newfound knowledge into practice and reflect on how these concepts can be applied to future projects.
:::

