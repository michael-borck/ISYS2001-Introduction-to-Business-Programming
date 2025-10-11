---
title: "Module 2: Using Input and Output in Python"
subtitle: "Speak and Listen: Empowering Your Programmes with Interactive Input and Output"
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

Welcome to Module 2. In this module, we explore how to interact with users through Python. We will learn how to capture user input using the `input()` function and display output with `print()`. These skills are essential for our User Preferences project.

::: {.notes}
This module introduces the fundamental concepts of input and output in Python programming. We will explore the `input()` function for capturing user input and the `print()` function for displaying output to the console. The module also covers techniques for formatting output using the `print()` function to create well-organised and visually appealing text.

Throughout the module, we will engage in hands-on activities to reinforce the concepts covered in each section. By the end of this module, you will have a solid understanding of how to interact with users through input and output operations in Python, enabling you to create more interactive and dynamic programs.
:::

# The `input()` Function: Overview

- The `input()` function allows you to receive user input as text.
- It displays a prompt message, pauses the programme, and waits for the user’s response.
- All input received is in the form of a string.
- Example:  
  ```python
  name = input("What is your name? ")
  ```

::: {.notes}
The `input()` function is a powerful tool in Python that enables developers to receive user input as text. When called, it displays a prompt message to the user, pauses the program execution, and waits for the user to enter a response. This function is particularly useful for creating interactive programs that require user participation.

It's important to note that all input received through the `input()` function is treated as a string, regardless of the type of data entered by the user. This means that if you require numerical input, you'll need to explicitly convert the received string to the appropriate data type, such as an integer or float, using functions like `int()` or `float()`. The slide also mentions that an example will be provided to demonstrate the usage of the `input()` function.
:::

# Capturing and Storing User Input

- Storing input in a variable lets you re-use the information.
- You can prompt the user with clear, concise messages.
- Consider the following example:  
  ```python
  favourite_colour = input("What is your favourite colour? ")
  ```
- This information will later be used to personalise outputs in our project.

::: {.notes}
Storing user input in a variable allows for reusability and flexibility in your program. By assigning the captured input to a variable, you can access and manipulate that information at any point in your code. This enables you to personalise outputs, perform calculations, or make decisions based on the user's input. It's important to provide clear and concise prompts to guide the user and ensure they understand what information is expected from them.

Let's consider an example where we prompt the user to enter their name and store it in a variable called `name`. We can then use that variable to display a personalised greeting, such as "Hello, [name]! Welcome to our program." This demonstrates how capturing and storing user input can enhance the interactivity and customisation of your program. Throughout our project, we will leverage this technique to create a more engaging and tailored experience for the user.
:::

# The `print()` Function: Displaying Output

- The `print()` function outputs information to the screen.
- It can display strings, variables, and results of operations.
- Example:  
  ```python
  print("Hello, " + name + "!")
  ```
- This helps to create personalised messages for the user.

::: {.notes}
The `print()` function is a fundamental tool in Python for displaying output to the user. It can handle a variety of data types, including strings, variables, and the results of operations, making it a versatile and essential part of any Python program. By using `print()`, developers can provide clear and informative messages to guide users through their applications.

One of the key benefits of the `print()` function is its ability to create personalised messages for the user. By incorporating variables and other dynamic content into the output, programs can generate tailored responses based on user input or other factors. This helps to make the user experience more engaging and interactive, encouraging users to continue interacting with the application.
:::

# Formatting Output with `print()`

- You can combine text and variables using:
  - String concatenation.
  - Comma-separated items (which adds spaces automatically).
- Example using commas:  
  ```python
  print("Hello,", name)
  ```
- These methods allow you to format your output neatly and clearly.

::: {.notes}
You can combine text and variables in `print()` statements using string concatenation or comma-separated items. String concatenation involves joining strings and variables using the `+` operator, while using commas automatically adds spaces between the items. For example, `print("Hello,", name)` would display "Hello, [name]" with a space after the comma.

Formatting your output with `print()` allows you to present information clearly and neatly. By combining text and variables effectively, you can create meaningful and readable output messages. This is particularly useful when displaying user-provided input, results from calculations, or any other dynamic content in your program.
:::

# Hands-On Activity: Basic Input and Output

**Task:** Create a simple programme that:
- Asks the user for their name.
- Asks for their favourite colour.
- Displays a personalised message that incorporates both inputs.

**Instructions:**
1. Use `input()` to capture the user's name and favourite colour.
2. Store the responses in variables.
3. Use `print()` to output a message, for example:  
   > "Hi [name], it's great to know your favourite colour is [colour]!"

::: {.notes}
This hands-on activity reinforces the concepts of basic input and output in Python. The activity involves asking the user for their name and favourite colour using the `input()` function, and then storing those values in variables.

The activity then demonstrates how to use the `print()` function to display a personalised message that incorporates both the user's name and favourite colour. This serves as a practical example of how to combine user input with output formatting to create a custom, interactive experience.
:::

# Additional Considerations

- Remember that every input is received as a string.  
- Think about how you might use this information in your User Preferences project.
- In future modules, we will explore converting input into other types and further refining output formatting.

::: {.notes}
When capturing user input with the `input()` function, it's important to remember that the entered data is always received as a string, regardless of whether the user enters text, numbers, or other characters. This means that if you require the input to be used as a different data type, such as an integer or float, you will need to explicitly convert it using functions like `int()` or `float()`.

In the upcoming User Preferences project, you may find yourself needing to store and manipulate user-entered data. By keeping in mind that input is received as strings, you can plan accordingly and incorporate the necessary type conversions to ensure your program processes the data correctly. As we progress through future modules, we will explore techniques for converting input into other data types and learn how to further customize the formatting of output using the `print()` function.
:::

# Summary

- You have learned how to capture user input using `input()` and display information with `print()`.
- These functions form the basis of interactive programmes.
- Apply these skills in your User Preferences project to create engaging, personalised user experiences.

::: {.notes}
In this slide, we summarise the key takeaways from the module on capturing user input with `input()` and displaying information using `print()`. These functions are fundamental building blocks for creating interactive programmes that engage users and provide personalised experiences. By mastering these skills, you'll be well-equipped to gather valuable data from users and present meaningful output.

As you work on your User Preferences project, apply the techniques covered in this module to craft programmes that dynamically respond to user input. Experiment with different prompts and formatting options to make your output more visually appealing and informative. Remember, effective communication between your programme and the user is crucial for creating successful applications that meet user needs and expectations.
:::

