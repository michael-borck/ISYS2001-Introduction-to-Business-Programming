---
title: "Forecasting Functions: Python's Weather Wizardry"
subtitle: "Coding up a storm with Python's powerful function features"
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

# Today's Learning Outcomes
- Why we need functions
- Function syntax in Python
- Defining and calling functions
- Parameters and return values
- Creating functions
- What are modules and why use them?
- The import statement and its variations

::: {.notes}
**Aim**
The aim of this slide is to clearly outline the key learning objectives for the session, providing students with a roadmap of what they will learn about functions and modules in Python.

**Context**
This slide follows the Acknowledgement of Country and sets the stage for the rest of the presentation. The topics covered in the learning outcomes will be expanded upon in subsequent slides, such as "Why Functions?", "Function Syntax", and "What are modules and why use them?".

**Why we need functions**
Functions are a fundamental concept in programming that allow us to break down complex problems into smaller, more manageable tasks. They help us avoid repetition, make our code more readable and maintainable, and enable us to reuse code across different parts of a program or even across different projects.

**Function syntax in Python**
To define a function in Python, we use the `def` keyword followed by the function name, parentheses containing any parameters the function accepts, and a colon. The body of the function is indented below the definition line. To call a function, we simply write its name followed by parentheses containing any required arguments.

**Defining and calling functions**
When defining a function, we specify its name, parameters (if any), and the code that should be executed when the function is called. To call a function, we use its name followed by parentheses and provide any necessary arguments. This invokes the function and executes the code within its body.

**Parameters and return values**
Functions can accept parameters, which are values passed into the function when it is called. These parameters allow us to provide different data to the function each time it is called, making it more flexible and reusable. Functions can also return values using the `return` keyword, allowing them to pass data back to the caller.

**Creating functions**
To create a function, we start with the `def` keyword, followed by the function name and parentheses containing any parameters. We then write the code that the function should execute when called, indenting it below the definition line. It's important to choose descriptive names for functions and parameters to make the code more readable and self-explanatory.

**What are modules and why use them?**
Modules are files containing Python code that define functions, classes, and variables. They allow us to organize our code into logical, reusable units and help keep our main program files clean and concise. By using modules, we can break down complex programs into smaller, more manageable parts and easily import and reuse code across different projects.

**The import statement and its variations**
To use functions, classes, or variables defined in a module, we need to import the module into our main program. We do this using the `import` statement followed by the name of the module. There are several variations of the `import` statement, such as importing specific items from a module or renaming a module with an alias, which can help make our code more concise and avoid naming conflicts.
:::

# Why Functions?
- Reusability: Write once, reuse everywhere.
- Modularity: Break tasks into smaller parts.
- Abstraction: Simplify complex tasks easily.
- Organisation: Keep code clean and structured.
- Scalability: Grow programs with ease.
- Testing: Easier to test and fix..

#
![](images/Slide1.jpeg)

#
![](images/Slide2.jpeg)

#
![](images/Slide3.jpeg)

#
![](images/Slide4.jpeg)

#
![](images/Slide5.jpeg)

::: {.notes}
**Aim**
This slide aims to introduce the key benefits of using functions in programming, highlighting their importance in writing efficient, maintainable, and scalable code.

**Context**
After presenting the learning outcomes, this slide delves into the first major topic: functions. It sets the foundation for understanding functions before discussing their syntax and common built-in functions in Python. The slide also relates to the upcoming topic of modules, as functions are essential building blocks for creating and using modules effectively.

**Reusability: Write once, reuse everywhere.**
Functions allow you to write a block of code once and reuse it multiple times throughout your program. By encapsulating a specific task or operation into a function, you can call it whenever needed, saving time and effort in writing repetitive code. This reusability promotes code efficiency and maintainability, as you can make changes to the function in one place and have those changes propagate to all instances where the function is used.

**Modularity: Break tasks into smaller parts.**
Functions enable you to break down complex tasks into smaller, more manageable parts. By dividing a program into logical functions, each responsible for a specific subtask, you can improve the overall structure and readability of your code. Modular code is easier to understand, debug, and maintain, as you can focus on one function at a time without being overwhelmed by the entire program's complexity.

**Abstraction: Simplify complex tasks easily.**
Functions provide a level of abstraction by hiding the internal details of how a task is accomplished. When you use a function, you only need to know its purpose, input parameters, and expected output, without worrying about the underlying implementation. This abstraction simplifies the usage of complex operations, making your code more readable and allowing you to focus on the higher-level logic of your program.

**Organisation: Keep code clean and structured.**
Functions contribute to better code organisation by grouping related code together. By encapsulating specific tasks into functions, you can keep your main program clean and structured, with a clear flow of execution. Well-organised code is easier to navigate, understand, and maintain, especially as your programs grow in size and complexity.

**Scalability: Grow programs with ease.**
As your programs expand and evolve, functions facilitate scalability. You can easily add new features or modify existing functionality by creating new functions or updating existing ones, without disrupting the overall structure of your code. Functions allow you to build upon existing code, promoting code reuse and reducing duplication, making your programs more scalable and adaptable to changing requirements.

**Testing: Easier to test and fix.**
Functions make testing and debugging more manageable. By isolating specific tasks into functions, you can test each function independently, ensuring that it produces the expected output for various inputs. If a bug is identified, you can focus on fixing the specific function rather than searching through the entire codebase. This targeted testing and debugging approach saves time and effort in maintaining and improving the quality of your code.
:::

# Common Builtin Functions

| **Function** | **Purpose**                                              | **Example**                  |
|--------------|----------------------------------------------------------|------------------------------|
| `print()`    | Outputs data to the console                              | `print("Hello, World!")`     |
| `len()`      | Returns the length of an object                          | `len([1, 2, 3])`             |
| `int()`      | Converts a value to an integer                           | `int("42")`                  |
| `str()`      | Converts a value to a string                             | `str(42)`                    |
| `sum()`      | Returns the sum of all items               | `sum([1, 2, 3])`             |
| `range()`    | Generates a sequence of numbers                          | `range(5)`                   |
| `max()`      | Returns the largest item                  | `max(1, 2, 3)`               |
| `min()`      | Returns the smallest item                 | `min(1, 2, 3)`               |
| `input()`    | Reads a string from user input                           | `name = input("Enter your name: ")` |

::: {.notes}
**Aim**
The aim of this slide is to introduce students to some commonly used built-in functions in Python.

**Context**
After discussing the importance and benefits of functions, this slide highlights specific built-in functions that are readily available in Python. The following slides will cover function syntax and how to create reusable logic with functions.
:::

# Function Syntax
```python
def function_name(parameters):
    # Function body
    return value
```

::: {.notes}
**Aim**
Introduce the syntax for defining functions in Python.

**Context**
This slide follows the "Why Functions?" slide, which explains the benefits of using functions. It precedes the "Consider" slide, which likely provides examples or considerations for writing functions. The slide is part of a larger presentation on AI and machine learning that also covers topics like built-in functions and Python modules.

**Bullet Point 1**
The `def` keyword is used to define a function in Python. It is followed by the function name and parentheses `()`, which may contain parameters if the function accepts input values. After the parentheses, a colon `:` is used to indicate the start of the function block. The function body, which contains the code to be executed when the function is called, is indented below the function definition line.

**Bullet Point 2**
Function parameters are optional input values that can be passed to a function when it is called. They are defined within the parentheses `()` in the function definition. When a function is called with arguments, the values of the arguments are assigned to the corresponding parameters in the function definition. This allows functions to perform operations on different input values each time they are called.

**Bullet Point 3**
The `return` statement is used to specify the value that a function should output or "return" when it is finished executing. When a `return` statement is encountered in a function, the function execution stops, and the specified value is sent back to the point where the function was called. If no `return` statement is used, the function will return `None` by default. A function can have multiple `return` statements, but only one will be executed, depending on the conditions met within the function.
:::

# Consider
```python
temp = 25
humidity = 80

if temp > 30 and humidity > 70:
    print('Hot and humid')
elif temp < 0:
    print('Freezing')
else:
    print('Moderate')
```

::: {.notes}
**Aim**
To prompt the audience to consider the importance of refactoring repetitive code into reusable functions.

**Context**
This slide follows the introduction of functions and common built-in functions in Python. It sets the stage for discussing a specific example of refactoring weather-related logic into a reusable function, which leads into the topic of modules and their benefits.
:::

# Reusable Weather Logic

```python
def categorise_weather(temp, humidity):
    if temp > 30 and humidity > 70:
        return 'Hot and humid'
    elif temp < 0:
        return 'Freezing'
    else:
        return 'Moderate'
```
#
![](images/Slide18.jpeg)

#
![](images/Slide19.jpeg)

#
![](images/Slide20.jpeg)

#
![](images/Slide21.jpeg)

#
![](images/Slide22.jpeg)

#
![](images/Slide23.jpeg)

#
![](images/Slide24.jpeg)

#
![](images/Slide25.jpeg)

::: {.notes}
**Aim**
Explain the concept of reusable weather logic and how it can be implemented in Python code.

**Context**
Having covered the basics of functions and modules, this slide builds on that knowledge to show how those concepts can be applied to create reusable logic for a specific task, in this example, weather-related functionality. The next slides will cover common Python modules and how to import them using aliases.
:::

# What are modules and why use them?
- Modules are just Python files
- Modules help organize code
- Modules let you use code that others have written
- Python comes with useful modules
- You can also import specific functions or classes from a module using the `from` statement.
- Aliases can be used to refer to modules with a shorter name.
- Modules can be installed using package managers like `pip`.

::: {.notes}
**Aim**
The aim of this slide is to introduce the concept of modules in Python and explain their benefits for code organisation and reuse.

**Context**
This slide follows on from the discussion of functions in Python, building on the idea of code reuse and organisation. It leads into the next slide which covers some commonly used Python modules.

**Modules are just Python files** Modules in Python are simply regular Python files containing Python code. Any Python file can be treated as a module and imported into another Python program or script. This allows you to break up your code into smaller, more manageable pieces.

**Modules help organize code** As your Python projects grow larger, it becomes increasingly important to keep your code organised and maintainable. By splitting your code into separate modules based on functionality or purpose, you can make your codebase easier to navigate and understand. Each module can encapsulate related functions, classes, and variables.

**Modules let you use code that others have written** One of the great advantages of modules is the ability to leverage code written by other developers. You can import modules created by the Python community or your colleagues, saving time and effort by not having to write everything from scratch. This promotes code reuse and allows you to benefit from the expertise of others.

**Python comes with useful modules** Python comes with a rich standard library that includes a wide range of built-in modules. These modules provide functionality for common tasks such as file I/O, networking, string manipulation, and more. By using these built-in modules, you can quickly add powerful capabilities to your Python programs without the need for external dependencies.

**You can also import specific functions or classes from a module using the `from` statement.** In addition to importing an entire module, you can also import specific functions, classes, or variables from a module using the `from` keyword. This allows you to selectively import only the parts of a module that you need, which can help avoid naming conflicts and make your code more concise.

**Aliases can be used to refer to modules with a shorter name.** When importing modules, you can assign an alias to the module name using the `as` keyword. This is useful when dealing with modules that have long or cumbersome names. By assigning a shorter alias, you can refer to the module more conveniently throughout your code.

**Modules can be installed using package managers like `pip`.** While Python comes with a standard library, there are countless third-party modules available that extend Python's functionality. These modules can be easily installed using package managers like `pip`. With `pip`, you can quickly install, upgrade, and manage external modules, making it simple to expand your Python capabilities as needed.
:::

# Common Python Modules

| **Module**     | **Purpose**                                                                 | **Example**                              |
|----------------|-----------------------------------------------------------------------------|------------------------------------------|
| `os`           | Interacts with the operating system, file and directory operations          | `os.listdir()` lists files in a directory |
| `sys`          | Interacting with the Python runtime        | `sys.argv` retrieves command-line arguments |
| `math`         | Provides mathematical functions like trigonometry and logarithms            | `math.sqrt(16)` calculates square root    |
| `random`       | Implements pseudo-random number generators                                  | `random.randint(1, 10)` generates random integer |
| `pandas`       | Data manipulation and analysis      | `pandas.DataFrame()` creates a data table |
| `matplotlib`   | Generates plots and graphs for data visualisation                           | `matplotlib.pyplot.plot()` creates a line plot |
| `numpy`        | Large, multi-dimensional arrays and matrices, and mathematical functions | `numpy.array()` creates an array |

#
![](images/Slide8.jpeg)

#
![](images/Slide9.jpeg)

#
![](images/Slide10.jpeg)

#
![](images/Slide11.jpeg)

# What is an Alias?

An alias in Python is like a nickname for a module or library. It allows you to
use a shorter, more convenient name when referring to that module in your code.

Some of the most frequently used aliases in Python are:

- `import pandas as pd`
- `import numpy as np`
- `import matplotlib.pyplot as plt`

::: {.notes}
**Aim**
The aim of this slide is to introduce the concept of aliases in Python and demonstrate their usage with common module imports.

**Context**
This slide follows on from an introduction to Python modules and the `import` statement. It provides concrete examples of using aliases with popular Python modules before moving on to the learning outcomes for the session.

**`import pandas as pd`**
When importing the `pandas` module, it is common convention to alias it as `pd`. This allows you to reference the module using the shorter alias throughout your code. For example, instead of writing `pandas.DataFrame()`, you can simply use `pd.DataFrame()`. Using the `pd` alias for `pandas` is a widely adopted practice in the Python data science community.

**`import numpy as np`**
Similar to `pandas`, the `numpy` module is frequently aliased as `np`. This abbreviation makes it more convenient to work with `numpy` functionalities in your Python scripts. By importing `numpy` as `np`, you can access its functions and classes using the concise `np.` prefix. For instance, `np.array()` creates a new `numpy` array object.

**`import matplotlib.pyplot as plt`**
When working with the `matplotlib` library for data visualization, it is customary to import the `pyplot` module as `plt`. This alias allows you to easily create and customize plots using functions like `plt.plot()`, `plt.xlabel()`, and `plt.title()`. The `plt` alias is a well-established convention within the Python data visualization community.
:::

# Recall `import` Statement
![](images/Slide13.jpeg)

#
![](images/Slide14.jpeg)

#
![](images/Slide15.jpeg)

#
![](images/Slide16.jpeg)

::: {.notes}
**Aim**
Refresh understanding of the `import` statement and its role in accessing modules and functions.

**Context**
This slide follows the introduction to modules and common Python modules. It provides a quick review of the `import` statement syntax before moving on to learning outcomes and the next lecture.
:::

# Today's Learning Outcomes
- Why we need functions
- Function syntax in Python
- Defining and calling functions
- Parameters and return values
- Creating functions
- What are modules and why use them?
- The import statement and its variations

::: {.notes}
**Aim**
The aim of this slide is to outline the key learning objectives for the session, focusing on functions and modules in Python.

**Context**
This slide comes early in the presentation, following the "Acknowledgement of Country" and copyright information. It sets the stage for the subsequent slides that delve into the specifics of functions and modules, providing examples and demonstrations.

**Why we need functions** Functions allow us to break down complex tasks into smaller, more manageable pieces of code. By encapsulating a specific set of instructions within a function, we can reuse that code throughout our program without having to rewrite it each time. This promotes code reusability, modularity, and maintainability, making our programs more efficient and easier to understand.

**Function syntax in Python** In Python, a function is defined using the `def` keyword, followed by the function name and a set of parentheses containing any parameters the function may take. The function body is indented and contains the code that will be executed when the function is called. Functions can optionally return a value using the `return` statement.

**Defining and calling functions** To define a function, we use the `def` keyword, specify the function name, and include any necessary parameters. Once defined, we can call the function by its name followed by parentheses, passing in any required arguments. This allows us to execute the code within the function whenever needed.

**Parameters and return values** Functions can accept input values, known as parameters, which allow us to pass data into the function for processing. These parameters are specified within the parentheses in the function definition. Functions can also return values using the `return` statement, allowing us to pass data back to the calling code. This enables functions to perform calculations or operations and provide the results to other parts of the program.

**Creating functions** When creating functions, it's important to choose descriptive names that clearly indicate the purpose of the function. Functions should typically perform a single, well-defined task, following the principle of "separation of concerns." By keeping functions focused and modular, we can improve code readability, maintainability, and reusability.

**What are modules and why use them?** Modules in Python are files containing Python code that can be imported and used in other Python programs. They provide a way to organize related functions, classes, and variables into separate namespaces, promoting code modularity and reusability. By using modules, we can break down large programs into smaller, more manageable files, making the codebase easier to navigate and maintain.

**The import statement and its variations** To use functions or classes from a module, we need to import the module into our Python script. The `import` statement allows us to bring the contents of a module into our current namespace. We can import the entire module, specific functions or classes from the module, or use an alias to provide a different name for the imported module. This flexibility enables us to access the desired functionality from modules while avoiding naming conflicts.
:::

# Next time
- Input validation
- Exception handling

::: {.notes}
**Aim**
To preview upcoming topics in this AI and machine learning course, specifically input validation and exception handling.

**Context**
After covering many core concepts such as functions, modules, and aliasing, this final slide looks ahead to the next session. It introduces two important programming practices to make code more robust and reliable.

**Input Validation** Input validation involves checking data from external sources to ensure it is of the expected type and format before using it. This prevents errors caused by invalid or malicious inputs. Validation can check data type, length, range, format, or presence of required values. Proper validation makes programs more secure and less prone to crashing or misbehaving due to bad data.

**Exception Handling** Exceptions are errors that occur during program execution. Exception handling uses try/except blocks to gracefully manage these runtime errors without abruptly terminating the program. The code to handle expected exceptions is placed in the try block. If an exception occurs, control transfers to the except block to run appropriate error-handling code. This allows logging errors, alerting the user, retrying operations or safely shutting down instead of crashing.
:::

