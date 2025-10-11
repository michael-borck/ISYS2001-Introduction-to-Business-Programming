---
title: "Unlocking Results with Returning Values"
subtitle: "How Your Functions Share Their Results with Your Code"
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

# Unlocking Results with Returning Values

Welcome to Module 3! In this module, you'll learn how functions process data and send results back to your programme using the `return` statement.

::: {.notes}
The "Unlocking Results with Returning Values" slide serves as an introduction to the concept of using return statements in functions to produce output. It sets the stage for the subsequent slides, which will delve into the specifics of how the return statement works and provide examples to illustrate its usage.

The slide is part of a larger presentation that covers the fundamentals of returning values from functions. The other slides in the presentation include "The return Statement", which explains the syntax and purpose of the return statement; "Simple Arithmetic Example", which demonstrates how to use the return statement in a basic arithmetic function; "Activity: Calculate the Area of a Circle", which provides a hands-on exercise for learners to practice using the return statement; and "Recap", which summarises the key points covered in the presentation.
:::

# The return Statement

- **Purpose:**  
  The `return` statement sends a value back to the part of your code that called the function.
- **Why use it?**  
  Instead of printing a result immediately, returning a value lets you store and use that result later.
- **Key Difference:**  
  - **Printing:** Displays a value on the screen.  
  - **Returning:** Provides a value that can be used elsewhere in your code.

::: {.notes}
The return statement serves two main purposes in programming. It allows you to exit a function and optionally send a value back to the caller. Using return is beneficial when you need to terminate a function's execution early or when you want to provide a result that can be utilised in other parts of your code.

It's important to distinguish between printing and returning values. Printing simply displays a value on the screen for informational purposes. In contrast, returning a value using the return statement makes it available for further use and processing within your program, enabling more flexible and modular code design.
:::

# Simple Arithmetic Example

Consider a function that adds two numbers:

```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print("The sum is", result)
```

- Here, `add_numbers` processes the numbers and returns the sum.
- We then store this result in the variable `result` and print it.

::: {.notes}
The slide "Simple Arithmetic Example" demonstrates how the `add_numbers` function processes the input numbers and returns their sum. This returned value is then assigned to the variable `result`, allowing us to store and utilise the computed sum for further operations or output.

By printing the `result` variable, we can display the sum of the numbers to the user, showcasing the successful execution of the `add_numbers` function and the returned value. This example highlights the importance of returning values from functions, enabling us to capture and work with the results of computations performed within the function's scope.
:::

# Activity: Calculate the Area of a Circle

**Your Task:**

- Create a function named `calculate_area` that:
  - Accepts one parameter: `radius`.
  - Calculates the area of a circle using the formula:  
    _Area = π × radius²_  
    (You can use 3.14 as an approximation for π.)
  - Returns the calculated area.
- Call your function and print the result.

**Example:**

```python
def calculate_area(radius):
    area = 3.14 * radius * radius
    return area

circle_area = calculate_area(5)
print("The area of the circle is", circle_area)
```

- Experiment with different radii to see how the area changes.

::: {.notes}
In this activity, you will create a function called `calculate_area` that takes the radius of a circle as a parameter. The function will use the well-known formula for calculating the area of a circle, which is πr², where π (pi) is approximately 3.14159 and r is the radius. Once the area is calculated, the function will return the result.

To test your function, call it with different radii and print the returned values. This will allow you to observe how the area changes as the radius is altered. By experimenting with various radii, you will gain a better understanding of the relationship between the radius and the area of a circle.
:::

# Recap

- The `return` statement lets a function send data back to the calling code.
- This technique allows you to use the results of a function in other parts of your programme.
- Practice writing functions that return values to become more confident in your coding skills.

Happy coding, and enjoy exploring the power of returning values from your functions!

::: {.notes}
In this slide, we recap the key points about returning values from functions. The `return` statement allows a function to send data back to the calling code, enabling you to use the results of the function in other parts of your programme. This is a powerful technique that can make your code more modular and reusable.

To become more confident in your coding skills, it's recommended that you practise writing functions that return values. By doing so, you'll gain a better grasp of how to structure your code and how to pass data between different parts of your programme. With time and practice, you'll find that using functions with return values becomes second nature and greatly improves the efficiency and readability of your code.
:::

