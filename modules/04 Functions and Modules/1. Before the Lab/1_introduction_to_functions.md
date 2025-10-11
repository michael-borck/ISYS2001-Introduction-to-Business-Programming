---
title: "Unlock the Power of Functions"
subtitle: "Your First Step to Organised Python Code"
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
# Welcome to Functions in Python

Welcome to our introduction to functions! In this module, you'll learn how functions help make your Python code more organised and easier to manage.

::: {.notes}
Welcome to Functions in Python! Functions are a fundamental concept in programming that allow you to organise your code into reusable blocks. By defining a function, you can encapsulate a specific task or computation, making your code more modular, readable, and maintainable.

In this presentation, we will explore what functions are, why they are useful, and how to define and call them in Python. We will cover the syntax for defining a function, including the def keyword, function name, parameters, and return values. Additionally, we will discuss how to call a function and pass arguments to it. By the end of this presentation, you will have a solid foundation in working with functions in Python.
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

::: {.notes}
Functions are an essential tool for organising code into manageable pieces, making it more readable and understandable. By breaking down a programme into smaller, self-contained functions, each responsible for a specific task, the overall structure becomes clearer and easier to follow. This modular approach helps to reduce complexity and makes the code more maintainable, as changes can be made to individual functions without affecting the rest of the programme.

Functions also promote code reusability, allowing a piece of code to be written once and used multiple times throughout the programme. This eliminates the need for duplicating code, saving time and effort, and reducing the likelihood of errors. By encapsulating a specific task within a function, it can be called whenever that functionality is needed, leading to more efficient and streamlined code. Additionally, well-defined functions with clear input and output parameters make the code more self-explanatory and easier for other developers to understand and collaborate on.
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

# Activity: Create Your Own Greeting Function

Try writing your very own function! Remember our early "Personalise Greeting" from labs? Now, lets make it a function?.  

**Task:**  
- Write a function named `greet()` that:
  - Uses the `input()` function to ask the user for their name.
  - Prints a personalised greeting message (for example, "Hello, [name]!").

Take a few minutes to try it out!

::: {.notes}
In this activity, you will create your own personalised greeting function called `greet()`. The function will use the built-in `input()` function to prompt the user to enter their name. Once the user has provided their name, the function will store it in a variable for further use.

After obtaining the user's name, the `greet()` function will print a customised greeting message. The message will incorporate the user's name, creating a personalised experience. For instance, if the user enters "Alice" as their name, the function will output "Hello, Alice!" or a similar greeting tailored to the user.
:::

# Answer: A Personalised Greeting Function

Here's one way to write the `greet()` function using the `input()` function inside it:

```python
def greet():
    name = input("Enter your name: ")
    print("Hello, " + name + "!")
    
greet()  # Calling the function to see it in action
```

In this solution, when you call `greet()`, the programme asks for your name and then prints a greeting just for you. Enjoy experimenting with your own greetings!

::: {.notes}
To create a personalised greeting function, we can modify the simple greeting function to accept a name parameter. Inside the function, we concatenate the "Hello" string with the provided name to create a customised greeting message. Finally, we print this personalised message when the function is called.

When calling the personalised greeting function, we pass in the desired name as an argument. This allows us to reuse the function with different names, generating unique greetings for each person. By utilising parameters, we can create flexible and reusable functions that adapt their behaviour based on the input provided.
:::

