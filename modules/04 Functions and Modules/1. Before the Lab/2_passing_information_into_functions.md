---
title: "Supercharge Your Functions with Data"
subtitle: "Using Parameters, Arguments, and Defaults to Create Dynamic Code"
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
# Passing Information to Functions

Welcome to Module 2! In this module, we'll learn how to send data into your functions. This allows you to make your functions more dynamic and flexible.

::: {.notes}
Passing information to functions is a fundamental concept in programming. Functions can accept input values, known as arguments, which are used within the function to perform specific tasks or calculations. These arguments are defined as parameters in the function definition, specifying the expected input values.

When calling a function, you provide the necessary arguments, which can be literals, variables, or expressions. The arguments are passed to the corresponding parameters in the function, allowing the function to operate on the provided values. By utilising parameters and arguments effectively, you can create reusable and modular code that can be easily customised for different scenarios.
:::

# Objectives

- Understand the difference between parameters and arguments.
- Learn how positional arguments work.
- Discover how to assign default values to parameters.

::: {.notes}
Presenter notes for "Objectives" slide:

This slide outlines the key learning objectives for the section on passing information to functions. Firstly, we'll clarify the distinction between parameters and arguments, which are often used interchangeably but have different meanings. Parameters are the variables defined in a function's definition, whereas arguments are the actual values passed to the function when it's called. Understanding this difference is crucial for working effectively with functions.

Next, we'll explore how positional arguments work. In Python, the order in which arguments are passed matters, and this is determined by the position of the corresponding parameters in the function definition. We'll look at examples to illustrate this concept. Lastly, we'll learn how to assign default values to parameters, which allows us to provide a fallback value if an argument isn't passed. This can make our functions more flexible and easier to use in different contexts.
:::

# Parameters vs. Arguments

- **Parameters:**  
  These are placeholders in your function definition. They represent the data your function needs.
- **Arguments:**  
  These are the actual values you pass into your function when you call it.
  
For example, in:
  
```python
def add_numbers(a, b):
    result = a + b
    print("The sum is", result)
```

`a` and `b` are parameters. When you call `add_numbers(3, 4)`, 3 and 4 are arguments.

::: {.notes}
Parameters are variables defined in a function declaration that receive values when the function is called. They act as placeholders for the values that will be passed to the function, allowing it to work with different data each time it is invoked. Parameters are specified within the parentheses of the function declaration, and they can have default values assigned to them.

Arguments, on the other hand, are the actual values passed to a function when it is called. These values are supplied within the parentheses of the function call and are used to replace the corresponding parameters in the function definition. The number and order of arguments must match the number and order of parameters in the function declaration unless default values are provided for the parameters.
:::

# Positional Arguments

- Arguments are passed into functions based on their order.
- The first argument goes to the first parameter, the second to the second parameter, and so on.
- This is why it is important to keep the order consistent when calling your function.

::: {.notes}
Positional arguments are passed into functions based on their order. The first argument corresponds to the first parameter, the second argument to the second parameter, and so forth. It is crucial to maintain consistency in the order of arguments when calling a function to ensure the intended behaviour and avoid unexpected results.

When using positional arguments, the position of each argument determines which parameter it is assigned to within the function. This means that if the order of the arguments is changed when calling the function, the values will be assigned to different parameters, potentially leading to errors or incorrect outputs. Therefore, it is important to be mindful of the order and provide the arguments in the same sequence as the function's parameter list.
:::

# Default Parameter Values

- You can assign a default value to a parameter in your function definition.
- This allows the function to be called even if one or more arguments are missing.
- Example:
  
```python
def describe_person(name, age=18):
    print(name + " is " + str(age) + " years old.")
```

In this function, if you don't provide an age, it defaults to 18.

::: {.notes}
Default parameter values allow functions to be called even when one or more arguments are not provided. In the function definition, a default value can be assigned to a parameter, which will be used if the corresponding argument is missing when the function is called. This provides flexibility and convenience, as it eliminates the need to specify every argument if some have suitable default values.

Here's an example to illustrate the concept: def greet(name, greeting="Hello"): print(f"{greeting}, {name}!") In this function, the "greeting" parameter has a default value of "Hello". If the function is called with only one argument, like greet("Alice"), the default value will be used, and the output will be "Hello, Alice!". However, if both arguments are provided, such as greet("Bob", "Hi"), the specified value will override the default, resulting in "Hi, Bob!".
:::

# Activity: Create Your Own Function

**Task:**  
Create a function named `describe_person` that takes two parameters: `name` and `age`.  
- Set the default value of `age` to 18.
- Inside the function, print a message that says, for example, "Alice is 18 years old."  
- Experiment by calling the function with both one and two arguments.

Take a moment to write your own version of `describe_person`.

::: {.notes}
In this activity, you will create your own function and experiment with passing arguments to it. Set the default value of the `age` parameter to 18, so that if no age is provided when calling the function, it will use 18 as the default. Inside the function, print a message that includes the name and age, such as "Alice is 18 years old."

After creating your function, call it with both one and two arguments to observe the difference in behaviour. First, call the function with just a name argument, and notice that the default age of 18 is used. Then, call the function again with both a name and an age argument, and see how the function uses the provided age instead of the default value. This practice will help solidify your understanding of how default parameter values work in functions.
:::

# Example Answer

Here's one way to write the function:

```python
def describe_person(name, age=18):
    print(name + " is " + str(age) + " years old.")

# Calling the function with both arguments
describe_person("Alice", 25)

# Calling the function with just the name; age defaults to 18
describe_person("Bob")
```

When you run this code, you'll see personalised messages based on the arguments you provide.

Happy coding, and enjoy exploring how passing information to functions can make your code more powerful!

::: {.notes}
The example answer demonstrates a basic function that takes two parameters, num1 and num2, and returns their sum. The function uses positional arguments, where the order of the arguments matters when calling the function. To use the function, you simply call it with two numbers, like add_numbers(5, 3), and it will return the result 8.

The example also shows how to set default parameter values. In this case, num2 has a default value of 10. This means that if you call the function with only one argument, like add_numbers(7), it will assume num2 is 10 and return 17. Default parameter values provide flexibility and allow the function to be called with fewer arguments when needed.
:::

