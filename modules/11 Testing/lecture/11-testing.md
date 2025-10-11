---
title: "Debugging the Weather: Testing Your Code with Python"
subtitle: "From print statements to doctests—Master the basics of testing and debugging with a weather twist!"
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
# Copyright Information

![](../../../_assets/curtin-copy-right.png)

# Acknowledgement of Country

I acknowledge the traditional custodians of the land on which I work and live,
and recognise their continuing connection to land, water and community. I pay
respect to elders past, present and emerging.

![](../../../_assets/ack_country.png)

# Today’s Goals

- Understand the difference between testing and debugging
- Describe one approach to debugging
- State why we test
- List common testing strategies

::: {.notes}
**Aim**
The aim of this slide is to clearly outline the learning objectives for the session and set expectations for what participants will gain from the presentation.

**Context**
This slide follows the Acknowledgement of Country and copyright information. It sets the stage for the rest of the presentation, which covers debugging, testing strategies, and practical examples using Python REPL and Jupyter Notebooks. The topics mentioned in the goals will be explored in more detail throughout the subsequent slides.

**Understand the difference between testing and debugging**
Testing and debugging are often confused, but they serve distinct purposes. Testing involves validating that the code behaves as expected and produces the desired output. In contrast, debugging is the process of identifying and fixing issues or bugs in the code. Understanding this difference is crucial for developing a comprehensive approach to ensuring code quality and reliability.

**Describe one approach to debugging**
One common approach to debugging is using print statements strategically throughout the code to track the values of variables and identify where the issue might be occurring. By outputting the state of the program at different points, developers can narrow down the location of the bug and gain insights into what might be causing it. This technique, along with others, will be explored further in the presentation.

**State why we test**
Testing is an essential part of the software development process. It helps ensure that the code is functioning as intended, handles edge cases gracefully, and produces reliable results. By catching bugs and issues early, testing can save time and resources in the long run. Additionally, testing helps maintain code quality, improves reliability, and provides confidence in the software's behaviour.

**List common testing strategies**
There are various testing strategies that developers can employ, each with its own strengths and use cases. Some common testing strategies include unit testing, where individual components or functions are tested in isolation; integration testing, which verifies how different parts of the system work together; and end-to-end testing, which tests the entire application flow from start to finish. Other strategies, such as regression testing and acceptance testing, will also be discussed in the presentation.
:::

# Problem-Solving Methodology

1. **State the problem clearly**
   - Example: *Predict tomorrow’s weather based on today’s data.*

2. **Describe the input and output**
   - Input: Weather data (e.g., temperature, humidity, wind speed)
   - Output: Weather prediction (sunny, rainy, etc.)

3. **Work a simple example by hand**
   - If today’s temperature is 25°C and wind speed is 5 km/h, predict tomorrow’s temperature.

4. **Develop an algorithm (and convert to Python)**
   - Example algorithm: Use an average of the last 5 days' temperature to predict tomorrow’s.

5. **Test solution with a variety of data**
   - Test using multiple data points: What if it’s 35°C? Or 0°C?

6. **Feedback Loop(s)**
   - Test -> Debug -> Refine -> Retest

*"I'm not a great programmer, I'm just a good programmer with great habits"*  
— Kent Beck

::: {.notes}
**Aim**
This slide aims to introduce a simple problem-solving methodology using the example of predicting tomorrow's weather based on today's data.

**Context**
After setting the goals for the presentation, this slide provides a practical example of problem-solving in the context of AI and machine learning. It sets the stage for discussing good habits for testing and debugging, which will be covered in the following slides.

**Example: *Predict tomorrow's weather based on today's data.***
In this example, we will use a simple problem to demonstrate the problem-solving methodology in AI and machine learning. The goal is to predict tomorrow's weather based on the data available today, such as temperature, humidity, and wind speed.

**Input: Weather data (e.g., temperature, humidity, wind speed)**
The input for this problem is the weather data available today. This may include measurements such as temperature in degrees Celsius, relative humidity as a percentage, and wind speed in kilometres per hour. These input variables will be used to make predictions about tomorrow's weather.

**Output: Weather prediction (sunny, rainy, etc.)**
The output of the problem is the predicted weather for tomorrow. This could be a categorical variable, such as sunny, cloudy, or rainy, or it could be a numerical prediction, such as the expected temperature. The output depends on the specific problem and the approach used to solve it.

**If today's temperature is 25°C and wind speed is 5 km/h, predict tomorrow's temperature.**
To make the problem more concrete, let's consider a specific example. If today's temperature is 25°C and the wind speed is 5 km/h, we want to predict what the temperature will be tomorrow. This example helps to illustrate the type of input data and the desired output for the problem.

**Example algorithm: Use an average of the last 5 days' temperature to predict tomorrow's.**
One simple approach to solving this problem is to use the average temperature from the last five days as the prediction for tomorrow's temperature. This is just one example of an algorithm that could be used. In practice, more sophisticated algorithms and machine learning techniques would likely be employed.

**Test using multiple data points: What if it's 35°C? Or 0°C?**
To evaluate the effectiveness of the chosen algorithm, it's important to test it using multiple data points. For example, we should consider how well the algorithm performs when the input temperature is much higher, such as 35°C, or much lower, such as 0°C. Testing with a range of inputs helps to identify the strengths and weaknesses of the algorithm.

**Test -> Debug -> Refine -> Retest**
The problem-solving methodology in AI and machine learning involves an iterative process of testing, debugging, refining, and retesting. After testing the algorithm with multiple data points, any issues or bugs should be identified and fixed. The algorithm can then be refined based on the insights gained from testing. Finally, the refined algorithm should be retested to ensure that the changes have had the desired effect. This cycle continues until the algorithm performs satisfactorily.
:::

# Great Habits for Testing and Debugging

- **Comments**: Describe what your code is doing.
- **Docstrings**: Add documentation to your functions (this will help with doctests!).
- **Use/Create functions**: Break tasks into reusable pieces.
- **Use/Create modules**: Organize your code.
- **Make small frequent commits**: Helps isolate where bugs come from.

::: {.notes}
**Aim**
This slide aims to provide developers with a set of good coding habits that can make testing and debugging easier and more effective.

**Context**
Having discussed the problem-solving methodology, this slide focuses on specific habits developers should adopt to prevent bugs and streamline the debugging process. The subsequent slides will delve into the nature of bugs, debugging strategies, and various types of testing.

**Comments: Describe what your code is doing.** 
Adding comments to your code is crucial for clarity and maintainability. Comments should explain the purpose and functionality of code sections, making it easier for you and other developers to understand the code's intent. This is especially helpful when revisiting code after a long time or when collaborating with others.

**Docstrings: Add documentation to your functions (this will help with doctests!).** 
Docstrings are a way to document functions, classes, and modules in Python. They provide a brief description of the purpose, parameters, and return values of a function. By including docstrings, you not only make your code more readable and understandable but also enable the use of doctests, which allow you to write test cases within the docstrings themselves.

**Use/Create functions: Break tasks into reusable pieces.** 
Functions are a fundamental concept in programming that allow you to break down complex tasks into smaller, reusable pieces of code. By creating functions for specific tasks, you can improve code organization, reduce duplication, and make your code more modular and easier to test. Functions also promote code reuse, saving time and effort in the long run.

**Use/Create modules: Organize your code.** 
Modules are files containing Python code that can be imported and used in other Python programs. By organizing related functions, classes, and variables into modules, you can create a clear structure for your codebase. This makes it easier to navigate, maintain, and test your code. Modules also help avoid naming conflicts and allow for better code reusability across different projects.

**Make small frequent commits: Helps isolate where bugs come from.** 
Version control systems like Git are essential tools for managing and tracking changes in your codebase. By making small, frequent commits, you create a detailed history of your code's evolution. This practice helps isolate where bugs might have been introduced, as you can compare the code before and after a specific commit. Small commits also make it easier to revert changes if needed and facilitate collaboration with other developers.
:::

# What is a Bug?

*A software bug is an error, flaw, or fault in computer software that causes it to produce an incorrect or unexpected result, or behave in unintended ways.*  
— Wikipedia

::: {.notes}
**Aim**
This slide aims to explain what a bug is in the context of software development and programming.

**Context**
The slide "What is a Bug?" follows the "Problem-Solving Methodology" and precedes the slides on "Debugging: The Process of Fixing Bugs" and "Debugging Strategies". It provides a foundation for understanding the concept of bugs before delving into the process and strategies for debugging.
:::

# Debugging: The Process of Fixing Bugs

1. **Types of Errors**:
   - **Syntax Errors**: Mistakes in the code’s format.
   - **Run-Time Errors**: Errors that occur when the program is running (e.g., division by zero).
   - **Logic Errors**: The code runs but produces incorrect results (e.g., wrong weather prediction).

2. **Debugging with `print()`**:
   - Use `print()` to display variables and track how values change in your program.
   - Example:
     ```python
     def predict_weather(temp):
         print(f"Current temperature: {temp}")
         if temp > 25:
             return "Sunny"
         else:
             return "Cloudy"
     print(predict_weather(30))  # Should print "Sunny"
     ```

::: {.notes}
**Aim**
This slide aims to introduce the concept of debugging and explain the different types of bugs that can occur in code.

**Context**
Having covered problem-solving methodology and good habits for testing and debugging, this slide delves into the specifics of debugging, explaining what bugs are and the process of fixing them. It leads into the next slide which covers debugging strategies.

**Syntax Errors** Syntax errors occur when there are mistakes in the format of the code, such as missing brackets, incorrect indentation, or typos. These errors prevent the code from running at all, as the computer cannot interpret the instructions. Python will usually provide an error message indicating the line number and the nature of the syntax error, making them relatively easy to identify and fix.

**Run-Time Errors** Run-time errors happen when the program is executing and encounters an unexpected situation it cannot handle, such as dividing by zero, trying to access an index that doesn't exist, or running out of memory. These errors cause the program to crash or exit unexpectedly. Python will provide a traceback showing the line of code where the error occurred and the type of exception that was raised.

**Logic Errors** Logic errors are bugs where the code runs without crashing, but produces incorrect or unexpected results. These can be the most difficult to identify and fix, as there is no error message to point out the issue. Examples include using the wrong formula in a calculation, having incorrect conditionals in an if statement, or accidentally introducing an infinite loop. Careful testing with a variety of inputs is necessary to identify logic errors.

**Use `print()` to display variables and track how values change in your program.** One simple but effective debugging technique is to insert `print()` statements at key points in the code to display the values of variables. This allows you to track how the values change as the program runs and identify where unexpected behaviour is occurring. Remember to remove or comment out these `print()` statements once the bug is fixed.

**Example:** The slide includes an example demonstrating the use of `print()` statements for debugging. Walking through a concrete example helps solidify understanding of the concept and technique.
:::

# Debugging Strategies

- **Step/Trace through code**: Use `print()` to trace how data flows.
- **Inspect Objects**: Use `type()` to check what kind of data your variables are holding.
- **Apply Trial and Error**: Try different values, step through your logic slowly.
- **Compare to similar code**: Use working code as a reference.
- **Ask for help**: Reach out to peers, forums, or Google.
- **Use an IDE**: Syntax highlighting and autocompletion can catch errors before you even run your code.

::: {.notes}
**Aim**
This slide aims to provide students with practical strategies they can use to effectively debug their code when encountering issues or unexpected behaviour.

**Context**
The "Debugging Strategies" slide follows on from an introduction to the concept of bugs and the debugging process. It precedes slides on testing, which is another key aspect of ensuring code correctness. The strategies presented here are general techniques that can be applied in various contexts and languages.

**Step/Trace through code** When faced with unexpected behaviour, a powerful technique is to add `print()` statements at key points in your code. This allows you to see the exact values of variables at each step and trace the flow of execution. By comparing the actual output with your expected output, you can pinpoint where the issue lies.

**Inspect Objects** Python provides the `type()` function, which allows you to check the data type of a variable. This is particularly useful when working with complex data structures or when receiving unexpected errors related to data types. By inspecting your objects, you can ensure they are of the expected type and narrow down potential sources of bugs.

**Apply Trial and Error** Sometimes, the best way to understand a problem is to experiment. Try inputting different values, both valid and invalid, and observe how your code responds. Step through your logic one piece at a time, and verify that each part behaves as intended. This iterative process can help you isolate issues and better understand the boundaries of your code.

**Compare to similar code** When stuck, it can be helpful to refer to code that you know works correctly. This could be code you've written previously, examples from the course materials, or even snippets found online. By comparing your code to a working reference, you can often spot differences or missing pieces that are causing the issue.

**Ask for help** If you've tried debugging on your own but are still stuck, don't hesitate to reach out for help. Discuss the problem with your peers, as they may have encountered similar issues or can provide a fresh perspective. Online forums and communities are also great resources. If all else fails, a targeted Google search can often lead you to insights or solutions.

**Use an IDE** While not strictly a debugging technique, using an Integrated Development Environment (IDE) can prevent many common bugs in the first place. IDEs offer features like syntax highlighting, which makes spotting syntactical errors much easier. They also often provide autocompletion, which can prevent typos and help you use functions correctly. By catching these issues early, you can spend less time debugging and more time writing great code.
:::

# Why Test?

- **Reliable**: Ensure the software behaves as expected.
- **Reproducible**: Others can verify your results.
- **Shareable**: Collaborators can see that your code works.

**_"Testing leads to failure, and failure leads to understanding."_**  
— Burt Rutan

::: {.notes}
**Aim**
This slide aims to explain the importance of testing in software development, particularly in the context of AI and machine learning.

**Context**
The "Why Test?" slide follows the "Debugging Strategies" slide and precedes the "Testing: What Are We Testing?" slide. It builds upon the understanding of debugging and introduces the concept of testing as a proactive approach to ensuring software quality. The subsequent slides delve deeper into various testing methodologies and their applications.

**Reliable** Testing is crucial to ensure that the software behaves as expected under various conditions. By thoroughly testing the code, developers can identify and fix potential issues before they manifest in production environments. Reliable software instils confidence in users and stakeholders, as they can trust that the system will perform its intended functions consistently and accurately.

**Reproducible** Reproducibility is a fundamental aspect of scientific research, and it extends to software development as well. When tests are properly designed and documented, others can independently verify the results, ensuring that the software's behaviour is consistent across different environments and configurations. Reproducible tests contribute to the overall reliability and credibility of the software.

**Shareable** In collaborative software development, it is essential to have a means of demonstrating that the code works as intended. By sharing test results and test suites, collaborators can quickly assess the functionality and quality of the code. This fosters effective communication, enables faster iterations, and facilitates seamless integration of contributions from multiple developers.
:::

# Testing: What Are We Testing?

1. **Requirements**: Does the weather prediction match the user’s needs?
2. **Design**: Does the code structure make sense?
3. **Code/Implementation**: Are the calculations and logic correct?
4. **Documentation**: Are there enough docstrings and comments?

::: {.notes}
**Aim**
This slide aims to introduce the concept of testing in the context of AI and machine learning, and to explore the different aspects and components that are typically tested.

**Context**
Having discussed the importance and benefits of testing in the previous slide, this slide delves deeper into the specifics of what is actually being tested in AI and machine learning systems. The subsequent slides will cover different types of tests and provide practical examples of testing techniques.

**Bullet Point 1** 

**Bullet Point 2** 

**Bullet Point 3** 

**Bullet Point 4** 

**Bullet Point 5**
:::

# You Are Already Testing!

- Validating inputs:
  - Example: What if someone enters an invalid temperature like "hot" instead of a number?

- Testing a variety of inputs (data):
  - Example: What happens if today's temperature is -10°C vs. 40°C?

- Checking outputs to meet requirements:
  - Does the predicted weather make sense based on the input?

**We are just giving more structure to this process.**

::: {.notes}
**Aim**
The aim of this slide is to demonstrate that the audience is already familiar with the fundamentals of testing in their everyday interactions with AI and machine learning systems.

**Context**
This slide follows the "Why Test?" and "Testing: What Are We Testing?" slides, which introduce the importance and scope of testing. It precedes the "Types of Tests" slide, which delves into more formal testing methodologies. The slide helps bridge the gap between the audience's existing knowledge and the upcoming technical content.

**Validating inputs:** When interacting with AI systems, we instinctively validate the data we provide to ensure it is in the expected format and range. This validation is a form of testing that helps prevent errors and unexpected behaviour.

**Example: What if someone enters an invalid temperature like "hot" instead of a number?** This example illustrates the importance of input validation. If a weather prediction system accepts a non-numeric value like "hot" instead of a temperature, it may crash or produce nonsensical results. Testing the system with various inputs, including invalid ones, helps identify and fix such issues.

**Testing a variety of inputs (data):** We often test AI systems with a wide range of inputs to assess their robustness and performance under different conditions. This is similar to how we might check if a weather prediction system works well for different temperature ranges.

**Example: What happens if today's temperature is -10°C vs. 40°C?** Testing a weather prediction system with extreme temperatures helps ensure that it can handle a wide range of inputs and produce reasonable outputs. If the system fails or generates unusual predictions for certain temperatures, it indicates a need for improvement.

**Checking outputs to meet requirements:** When using AI systems, we naturally check if the outputs align with our expectations and requirements. This is a form of testing that helps verify the system's correctness and usefulness.

**Does the predicted weather make sense based on the input?** In the context of a weather prediction system, we would compare the predicted weather with the input temperature to see if it makes sense. For example, if the input is -10°C, we would expect the predicted weather to be cold and possibly snowy, not hot and sunny. Testing the system's outputs against our domain knowledge and common sense is crucial for ensuring its reliability.
:::

# Types of Tests

1. **Unit Testing**: Test an individual, isolated function or module.
   - Example: Test if the `predict_weather()` function returns the correct output for different temperatures.

2. **Integration Testing**: Ensure multiple parts of the program work together.
   - Example: Test if weather prediction works when integrated with a larger weather dashboard application.

3. **End-to-End Testing**: Simulate a real user interacting with your program.
   - Example: Test the entire workflow of entering today's weather and predicting tomorrow's weather in your app.

4. **Acceptance Testing**: Ensure the program meets the user’s requirements.
   - Example: The program should correctly predict "Sunny" when the temperature is above 25°C.


::: {.notes}
**Aim**
The aim of this slide is to introduce the different types of tests used in AI and machine learning development, with examples to illustrate each type.

**Context**
This slide follows on from discussing the importance and purpose of testing in AI and machine learning. It provides specific examples of different test types, before subsequent slides dive into more details on testing methodologies and tools.

**Example: Test if the `predict_weather()` function returns the correct output for different temperatures.** This is an example of a unit test, which focuses on testing an individual component or function in isolation. Here, we would pass different temperature inputs to the `predict_weather()` function and check that it returns the expected output for each case. Unit tests help verify the correctness of specific parts of the code.

**Example: Test if weather prediction works when integrated with a larger weather dashboard application.** This exemplifies an integration test, which checks how different components or modules work together. In this case, we would test if the weather prediction functionality integrates correctly with the broader weather dashboard application. Integration tests help identify issues that may arise when combining parts of the system.

**Example: Test the entire workflow of entering today's weather and predicting tomorrow's weather in your app.** This is a system or end-to-end test, which tests the complete functionality of the application from start to finish. It would involve entering today's weather data, running the prediction, and verifying that tomorrow's weather is correctly displayed. System tests ensure the application works as intended from a user's perspective.

**Example: The program should correctly predict "Sunny" when the temperature is above 25°C.** This is an example of a requirements-based or acceptance test. It checks that the application meets a specific requirement or criteria. In this case, we would test that the program outputs "Sunny" whenever the input temperature exceeds 25°C. Acceptance tests help validate that the software satisfies the specified requirements.
:::

# Review: What is the Python REPL?

The Python REPL stands for **Read-Eval-Print Loop** and is an interactive environment that lets you type and execute Python code line by line.

::: {.notes}
**Aim**
The aim of this slide is to review and refresh the audience's understanding of the Python REPL.

**Context**
This slide follows on from a discussion of testing and debugging strategies in Python. It serves as a refresher on the Python REPL before diving into practical examples of using the REPL for testing and debugging code, such as with doctests and in Jupyter notebooks.
:::

# How REPL Works:

1. **Read**: The REPL reads your input (Python code).
2. **Eval**: It evaluates or executes the code you entered.
3. **Print**: It displays the result of your code.
4. **Loop**: The process repeats, allowing you to try more code.

::: {.notes}
**Aim**
The aim of this slide is to explain how the Read-Eval-Print Loop (REPL) works in Python.

**Context**
This slide follows on from a review of what the Python REPL is. It provides more detail on the inner workings of the REPL before discussing why it is useful and showing it in action through examples.

**Bullet Point 1** [Read] In the first step, the REPL reads the Python expression or statement that you enter. It parses this input into a form that the Python interpreter can understand and execute.

**Bullet Point 2** [Eval] Next, the REPL evaluates the parsed expression or executes the parsed statement. This is where the actual Python code is run by the interpreter.

**Bullet Point 3** [Print] After the evaluation/execution step, the REPL prints the result of the expression or any output from the executed statement. This allows you to immediately see the outcome of your code.

**Bullet Point 4** [Loop] Finally, the REPL loops back to the beginning, ready to read the next input. This loop continues indefinitely, allowing you to keep entering and running Python code, until you signal to exit the REPL.
:::

# Why Use REPL?

- **Instant Feedback**: You can quickly test and run small pieces of code.
- **Interactive Learning**: It’s great for experimenting with Python features.
- **Debugging**: Use it to test functions and explore data interactively.

::: {.notes}
**Aim**
This slide aims to highlight the key benefits of using the Python REPL for coding and learning.

**Context**
After introducing the concept of the Python REPL in the previous slide, this slide delves into the practical advantages of using it. The following slides will provide specific examples and use cases to reinforce these benefits.

**Instant Feedback** The Python REPL allows you to enter code and see the results immediately, without the need to write a complete script or program. This instant feedback loop enables quick testing of ideas, syntax, and logic, making it an invaluable tool for iterative development and experimentation.

**Interactive Learning** The REPL provides an interactive environment that encourages hands-on learning and exploration of Python features. You can try out different commands, expressions, and libraries, and observe their behaviour in real-time. This interactive approach facilitates a deeper understanding of Python concepts and helps build confidence in using the language.

**Debugging** The REPL is a powerful tool for debugging and troubleshooting code. You can test individual functions, explore data structures, and inspect variables at runtime. By running code step-by-step and examining intermediate results, you can identify issues and fix bugs more efficiently. The REPL's interactive nature makes it easier to isolate problems and experiment with potential solutions.
:::

# Example: REPL in Action

```python
>>> temperature = 30
>>> if temperature > 25:
...     print("Sunny")
... else:
...     print("Cloudy")
...
Sunny
```

In this example:
- You entered a condition based on temperature.
- The REPL evaluated the condition and printed "Sunny" as the result.



### How REPL Connects to Doctests

- **Doctests** mimic the Python shell (REPL) experience inside your code.
- You can write your function's expected behaviour in a way that looks like what you'd do in the REPL.

::: {.notes}
**Aim**
This slide aims to demonstrate how the Python REPL works in practice, using a simple example to illustrate the process of entering code and seeing the evaluated result.

**Context**
After introducing the concept of the Python REPL and explaining how it works and why it's useful, this slide provides a concrete example of the REPL in action. It leads into the next section on testing, showing how the REPL experience can be mimicked within code using doctests.

**You entered a condition based on temperature.** In this example, you would have typed a line of code into the Python REPL that checks a condition based on the temperature. This could be something like `if temperature > 20: print("Sunny")`, which checks if the `temperature` variable is greater than 20 and prints "Sunny" if the condition is true.

**The REPL evaluated the condition and printed "Sunny" as the result.** After entering the code, the REPL immediately evaluated the condition. Assuming the `temperature` variable was set to a value greater than 20, the condition would be true, and the REPL would execute the `print` statement, displaying "Sunny" as the output.

**Doctests mimic the Python shell (REPL) experience inside your code.** Doctests are a way of writing tests directly in your code's docstrings. They are written in a format that looks like an interactive Python shell session, with lines of code followed by the expected output. This allows you to specify your function's expected behaviour in a way that resembles the REPL experience.

**You can write your function's expected behaviour in a way that looks like what you'd do in the REPL.** When writing doctests, you include example code snippets that demonstrate how your function should be used and what output it should produce. These code snippets are written just like you would enter them in the REPL, making it easy to understand and test your function's behaviour.
:::

# Simple Example: Testing with `doctest`

You can embed tests inside your function’s docstrings using `doctest`. Here's a weather example:

```python
def predict_weather(temp):
    """
    Predict tomorrow's weather based on today's temperature.

    >>> predict_weather(30)
    'Sunny'
    >>> predict_weather(20)
    'Cloudy'
    """
    if temp > 25:
        return "Sunny"
    else:
        return "Cloudy"
```

You can run `doctest` to check if the output matches the expected results. To run `doctest`, add this to the bottom of your script:
```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

::: {.notes}
**Aim**
Demonstrate how to write a simple test using Python's `doctest` module.

**Context**
Having introduced the concept of testing and the Python REPL, this slide provides a concrete example of how to write tests using `doctest`. It leads into the next few slides which explain doctests in more detail, including how they work, why they are useful, and how to run them.
:::

# Doctests: Testing in Your Docstrings

Doctests allow you to write test cases directly in your function's docstring,
mimicking how you would test code in the Python shell. They are great for small
functions and help you document the expected behavior of your code.

::: {.notes}
**Aim**
To introduce doctests as a way to write tests directly in the docstring of a function, and explain how they work.

**Context**
This slide builds on the previous discussion of testing by introducing a specific technique called doctests. It leads into the next few slides which provide examples of doctests in action and explain their benefits.
:::

# How Doctests Work

- Doctests simulate the Python shell (REPL) and check if the output matches the expected result written in the docstring.
- You write the function's input and output in a way that looks like a Python session, and `doctest` automatically checks if the function produces the correct result.

::: {.notes}
**Aim**
This slide aims to explain how doctests work by simulating a Python shell and automatically checking if a function's output matches the expected result.

**Context**
After introducing the concept of testing and different types of tests, the presentation dives into doctests as a specific testing method. This slide follows an example of using doctests and precedes slides on why and how to use doctests in practice.

**Doctests simulate the Python shell (REPL) and check if the output matches the expected result written in the docstring.** Doctests are a way to write tests directly in the docstring of a function. They mimic the interactive Python shell by including input and expected output as if you were typing commands and seeing the results in the shell. When you run the doctests, the testing framework automatically executes the function with the given input and compares the actual output to the expected output specified in the docstring. If they match, the test passes; if not, it fails.

**You write the function's input and output in a way that looks like a Python session, and `doctest` automatically checks if the function produces the correct result.** To create a doctest, you format the expected input and output in the docstring to resemble a Python interactive session. This includes the `>>>` prompt, function calls, and expected output. The `doctest` module then parses this information and runs the tests automatically, without the need for separate test files or special assert statements. This makes doctests a convenient way to include tests close to the source code and maintain them together with the function's documentation.
:::

# Doctest Example (Weather Prediction)

```python
def predict_weather(temp):
    """
    Predict tomorrow's weather based on today's temperature.
    
    This function returns 'Sunny' if the temperature is above 25°C, 
    otherwise it returns 'Cloudy'.
    
    Example usage in the Python shell:
    
    >>> predict_weather(30)
    'Sunny'
    >>> predict_weather(20)
    'Cloudy'
    """
    if temp > 25:
        return "Sunny"
    else:
        return "Cloudy"
```

::: {.notes}
**Aim**
This slide demonstrates how to use doctest to test a simple weather prediction function, showcasing the practical application of doctests in Python code.

**Context**
Having introduced the concept of doctests and how they work in the previous slides, this example builds on that foundation by presenting a concrete use case. The subsequent slides will discuss the benefits of using doctests and how to run them effectively.
:::

# Why Use Doctests?

- **Readable**: It combines documentation and testing in one place.
- **Simple**: You don't need separate testing files for small functions.
- **Automated**: Doctests verify that your code behaves as described.

::: {.notes}
**Aim**
This slide aims to explain the key benefits of using doctests for testing Python code.

**Context**
After introducing the concept of doctests and showing a simple example, this slide follows on to highlight the main advantages of using doctests. It leads into the next slides which cover running doctests and comparing them to using the Python shell.

**Readable** By including test cases directly in the docstring, doctests make it easy to see the expected behaviour of a function right next to its documentation. This keeps the tests closely tied to the code they are testing, making them more readable and maintainable. Having the tests and documentation in one place also makes it simpler for other developers to understand how the function is intended to be used.

**Simple** For small, focused functions, doctests provide a lightweight way to include tests without needing to create separate test files or use a full-featured testing framework. This reduces boilerplate and keeps the code concise. Doctests are ideal for unit testing individual functions in isolation.

**Automated** When doctests are run, they automatically compare the actual output of the code against the expected output written in the docstring. This verifies that the code behaves correctly according to its documentation. Having this automated testing helps catch regressions and ensures the code remains reliable as it is modified.
:::

# Running Doctests

To run doctests, include the following at the bottom of your Python file:
```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This will run the tests inside your docstrings, checking if the actual outputs match the expected ones.

::: {.notes}
**Aim**
The aim of this slide is to explain how to run doctests and demonstrate their practical application in testing code.

**Context**
This slide follows on from an introduction to doctests and examples of how they can be used for testing code. It precedes slides on testing strategies in Jupyter Notebooks and building a comprehensive test suite.

**Running Doctests**
To run doctests, you can use the `python -m doctest` command followed by the name of the Python file containing the doctests. This command searches for pieces of text that look like interactive Python sessions within the file's docstrings and runs them as tests. Any output produced by the code is compared to the expected output specified in the docstring. If they match, the test passes; if there are differences, the test fails and the differences are reported. Running doctests is a quick and easy way to check that your code is working as intended and to catch any regressions when making changes.
:::

# Doctest vs. Python Shell

When you run `doctest`, it behaves as if you are manually entering the input and checking the output in the Python shell (REPL):

**Python Shell Session**:
```python
>>> predict_weather(30)
'Sunny'
>>> predict_weather(20)
'Cloudy'
```

**Doctest in Docstring**:
```python
"""
>>> predict_weather(30)
'Sunny'
>>> predict_weather(20)
'Cloudy'
"""
```

Doctests save you time by automating these shell interactions and ensuring your code works as expected!

::: {.notes}
**Aim**
Compare and contrast the features and use cases of doctest and the Python shell for testing code.

**Context**
This slide builds on the previous content about using the Python REPL and doctest for testing. It aims to help learners understand when to choose one testing approach over the other by directly comparing them. The comparison provides a foundation for the subsequent slides on testing strategies and building test suites.

****
Doctest allows you to write tests directly in your docstrings, keeping the tests close to the code they are testing. This makes it easy to understand how a function is intended to be used and what its expected outputs are for given inputs. Doctest tests serve as executable documentation. In contrast, the Python shell is a more free-form environment for interactive testing where you manually enter expressions and check the output.

****
Running doctests is automated - you can run all tests in a file or module with a single command. This makes it easy to frequently re-run your test suite as you make changes. Testing in the Python shell is more manual - you need to re-enter expressions to re-run tests, and it's up to you to manually verify the output is as expected.

****
Doctest is best suited for testing pure functions that have well-defined inputs and outputs and don't depend on global state. The Python shell is more flexible and can be used for testing any kind of code, but is especially useful for exploratory testing and debugging where you want to inspect program state or try out different scenarios interactively. Using both together is often helpful.
:::

# Testing Strategy in Jupyter Notebooks

There are different ways to test notebooks:

- **Write python script to test notebook**: You can import your functions from the notebook and test them using a Python script.
- **Write test and code in one notebook**: You can use `assert()`, `doctest`, or other testing libraries directly in the notebook.
  
Example in a notebook:
```python
# Code cell:
def predict_weather(temp):
    return "Sunny" if temp > 25 else "Cloudy"

# Test cell:
assert predict_weather(30) == "Sunny"
assert predict_weather(20) == "Cloudy"
```

::: {.notes}
**Aim**
The aim of this slide is to introduce two strategies for testing code in Jupyter Notebooks.

**Context**
This slide is part of a section on testing strategies in a presentation about AI and machine learning. It follows slides explaining what testing is and why it's important. The next slide shows an example of using doctests in Jupyter Notebooks.

**Write python script to test notebook** You can write your functions in a Jupyter Notebook, then create a separate Python script that imports those functions and tests them. This allows you to keep your notebook focused on the main code while having a dedicated space for more comprehensive tests. The testing script can use Python's built-in unittest module or other testing frameworks.

**Write test and code in one notebook** Alternatively, you can include tests directly in the Jupyter Notebook alongside your code. Simple tests can be done using Python's assert() function, which raises an AssertionError if the condition is false. For more structured tests, the doctest module allows you to write tests in the docstrings of your functions. Other testing libraries like pytest can also be used directly in the notebook.
:::

# Using Doctests in Jupyter Notebooks

1. **Write Your Function with a Doctest**:
   Include the test cases directly in your function’s docstring.

   ```python
   def predict_weather(temp):
       """
       Predict tomorrow's weather based on today's temperature.

       >>> predict_weather(30)
       'Sunny'
       >>> predict_weather(20)
       'Cloudy'
       """
       if temp > 25:
           return "Sunny"
       else:
           return "Cloudy"
   ```

2. **Run Doctests with `doctest.testmod()`**:
   You can run your doctests in a Jupyter notebook using the `doctest` module.

   ```python
   import doctest
   doctest.testmod()
   ```

3. **View the Results**:
   If all tests pass, there will be no output.
   If any tests fail, `doctest` will show where the function’s output didn’t match the expected result.

::: {.notes}
**Aim**
This slide demonstrates how to use doctests within Jupyter Notebooks to test code and ensure it works as expected.

**Context**
The previous slides introduced doctests and explained how they work. This slide builds on that knowledge by showing how to apply doctests in the context of Jupyter Notebooks. The following slides will cover building a comprehensive test suite.

****
To use doctests in Jupyter Notebooks, simply include the doctests within the docstring of a function or class, just as you would in a regular Python script. When you run the cell containing the function or class definition, the doctests will be executed automatically.

****
If a doctest fails, an exception will be raised, and the notebook will display the traceback, indicating which test case failed and what the expected and actual outputs were. This allows you to quickly identify and fix any issues with your code.

****
It's good practice to include doctests for key functionality in your Jupyter Notebooks. This ensures that your code remains reliable and behaves as expected, even as you make changes and additions to your notebook over time.

****
Remember to strike a balance between thoroughness and brevity in your doctests. Focus on testing the most important aspects of your code, and use clear, concise test cases that cover a range of scenarios.

****
By incorporating doctests into your Jupyter Notebooks, you can create a self-documenting and self-testing codebase that is easier to maintain and less prone to errors. This is particularly valuable in the context of data analysis and machine learning projects, where accuracy and reproducibility are paramount.
:::

# Example in Jupyter Notebook

- First, define the function with doctests in the cell.
- Then, in a new cell, run the following code to check the tests:

```python
import doctest
doctest.testmod()
```

### Key Points:

- In Jupyter notebooks, `doctest` works just like in standard Python scripts.
- The tests will run, and you can verify that your function behaves as expected, just like in the Python shell.

::: {.notes}
**Aim**
This slide demonstrates how to use doctests within Jupyter Notebooks to test functions and ensure they behave as expected.

**Context**
After discussing the importance of testing and introducing doctests, this slide shows how to apply doctests in the context of Jupyter Notebooks. It is followed by a slide on building a comprehensive test suite.

**First, define the function with doctests in the cell.** Begin by writing your function in a Jupyter Notebook cell, including doctests within the function's docstring. These doctests serve as examples of how the function should behave given certain inputs, and they also act as a form of documentation for the function's expected behaviour.

**Then, in a new cell, run the following code to check the tests:** After defining your function with doctests, create a new cell below it. In this cell, use the `doctest.run_docstring_examples()` function, passing your function's name as an argument. This code will execute the doctests associated with your function.

**In Jupyter notebooks, `doctest` works just like in standard Python scripts.** The `doctest` module in Jupyter Notebooks functions identically to how it works in regular Python scripts. You can define your functions with doctests and run them using the same methods, making the testing process consistent across different environments.

**The tests will run, and you can verify that your function behaves as expected, just like in the Python shell.** When you run the cell containing the `doctest.run_docstring_examples()` function, the doctests associated with your function will execute. The output will indicate whether the tests passed or failed, allowing you to verify that your function behaves correctly based on the expected inputs and outputs defined in the doctests. This process is similar to testing your functions in the Python shell.
:::

# Building a Test Suite

1. **Build up a suite of tests**: Create a set of tests that cover different parts of your program.
2. **Run all tests in one go**: Use a script or notebook to run all tests automatically.
3. **Test sane cases, then edge cases**: Test common scenarios first, then unusual inputs.
   - Example: What happens when you input extreme temperatures like -100°C or 100°C?

::: {.notes}
**Aim**
This slide aims to demonstrate the importance of testing edge cases and extreme inputs when building a robust test suite.

**Context**
After discussing the basics of testing, types of tests, and using doctests in Python, this slide expands on the concept of building a comprehensive test suite. It encourages students to think critically about potential edge cases and boundary conditions that could break their code.

**Example: What happens when you input extreme temperatures like -100°C or 100°C?**
When building a test suite, it's crucial to consider not only the expected inputs but also extreme or unexpected ones. For example, if you're writing a function that processes temperature data, you should test how it handles inputs like -100°C or 100°C. These extreme values might be outside the normal operating range and could potentially cause your code to fail or produce incorrect results. By including such test cases, you can ensure your code is robust and can gracefully handle these edge cases, either by raising appropriate errors or returning sensible default values. This approach helps uncover hidden bugs and improves the overall reliability of your software.
:::

# Review: Can you…

- Understand the difference between testing and debugging?
- Describe one approach to debugging?
- State why we test?
- List common testing strategies?

::: {.notes}
**Aim**
This slide aims to review and reinforce key concepts and skills related to testing and debugging covered earlier in the presentation.

**Context**
The "Review: Can you..." slide is positioned towards the end of the presentation, following detailed coverage of debugging strategies, the importance of testing, types of tests, and practical examples using REPL and doctests. This review slide helps consolidate the knowledge gained and ensures students have grasped the fundamental concepts before concluding the lesson.

**Understand the difference between testing and debugging?**
Testing involves evaluating a program's behaviour and verifying that it produces the expected outputs for various inputs. In contrast, debugging is the process of identifying, locating, and fixing errors or bugs in the code that cause the program to behave incorrectly. Testing helps uncover bugs, while debugging is the systematic approach to resolving those issues.

**Describe one approach to debugging?**
One effective approach to debugging is the "divide and conquer" strategy. This involves narrowing down the problematic area of the code by systematically isolating smaller sections and testing them independently. By progressively eliminating code that works as expected, you can focus on the specific part causing the issue, making it easier to identify and fix the bug.

**State why we test?**
We test our code to ensure it functions as intended, producing the desired outputs for different input scenarios. Testing helps uncover bugs, edge cases, and unexpected behaviour early in the development process. By catching and fixing issues promptly, we improve the reliability, quality, and maintainability of our software, reducing the risk of errors in production and providing a better user experience.

**List common testing strategies?**
Some common testing strategies include unit testing, where individual components or functions are tested in isolation; integration testing, which verifies the interaction between different modules; and system testing, which evaluates the entire system's performance. Other strategies include regression testing to ensure new changes don't break existing functionality, acceptance testing to validate user requirements, and exploratory testing to uncover unforeseen issues.
:::

