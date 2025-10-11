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



# Great Habits for Testing and Debugging

- **Comments**: Describe what your code is doing.
- **Docstrings**: Add documentation to your functions (this will help with doctests!).
- **Use/Create functions**: Break tasks into reusable pieces.
- **Use/Create modules**: Organize your code.
- **Make small frequent commits**: Helps isolate where bugs come from.



# What is a Bug?

*A software bug is an error, flaw, or fault in computer software that causes it to produce an incorrect or unexpected result, or behave in unintended ways.*  
— Wikipedia



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



# Debugging Strategies

- **Step/Trace through code**: Use `print()` to trace how data flows.
- **Inspect Objects**: Use `type()` to check what kind of data your variables are holding.
- **Apply Trial and Error**: Try different values, step through your logic slowly.
- **Compare to similar code**: Use working code as a reference.
- **Ask for help**: Reach out to peers, forums, or Google.
- **Use an IDE**: Syntax highlighting and autocompletion can catch errors before you even run your code.



# Why Test?

- **Reliable**: Ensure the software behaves as expected.
- **Reproducible**: Others can verify your results.
- **Shareable**: Collaborators can see that your code works.

**_"Testing leads to failure, and failure leads to understanding."_**  
— Burt Rutan



# Testing: What Are We Testing?

1. **Requirements**: Does the weather prediction match the user’s needs?
2. **Design**: Does the code structure make sense?
3. **Code/Implementation**: Are the calculations and logic correct?
4. **Documentation**: Are there enough docstrings and comments?



# You Are Already Testing!

- Validating inputs:
  - Example: What if someone enters an invalid temperature like "hot" instead of a number?

- Testing a variety of inputs (data):
  - Example: What happens if today's temperature is -10°C vs. 40°C?

- Checking outputs to meet requirements:
  - Does the predicted weather make sense based on the input?

**We are just giving more structure to this process.**



# Types of Tests

1. **Unit Testing**: Test an individual, isolated function or module.
   - Example: Test if the `predict_weather()` function returns the correct output for different temperatures.

2. **Integration Testing**: Ensure multiple parts of the program work together.
   - Example: Test if weather prediction works when integrated with a larger weather dashboard application.

3. **End-to-End Testing**: Simulate a real user interacting with your program.
   - Example: Test the entire workflow of entering today's weather and predicting tomorrow's weather in your app.

4. **Acceptance Testing**: Ensure the program meets the user’s requirements.
   - Example: The program should correctly predict "Sunny" when the temperature is above 25°C.




Absolutely! Here's a slide reviewing REPL (Read-Eval-Print Loop) to provide context before introducing `doctest`:



# Review: What is the Python REPL?

The Python REPL stands for **Read-Eval-Print Loop** and is an interactive environment that lets you type and execute Python code line by line.

# How REPL Works:

1. **Read**: The REPL reads your input (Python code).
2. **Eval**: It evaluates or executes the code you entered.
3. **Print**: It displays the result of your code.
4. **Loop**: The process repeats, allowing you to try more code.

# Why Use REPL?

- **Instant Feedback**: You can quickly test and run small pieces of code.
- **Interactive Learning**: It’s great for experimenting with Python features.
- **Debugging**: Use it to test functions and explore data interactively.

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


# Doctests: Testing in Your Docstrings

Doctests allow you to write test cases directly in your function's docstring,
mimicking how you would test code in the Python shell. They are great for small
functions and help you document the expected behavior of your code.

# How Doctests Work

- Doctests simulate the Python shell (REPL) and check if the output matches the expected result written in the docstring.
- You write the function's input and output in a way that looks like a Python session, and `doctest` automatically checks if the function produces the correct result.

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

# Why Use Doctests?

- **Readable**: It combines documentation and testing in one place.
- **Simple**: You don't need separate testing files for small functions.
- **Automated**: Doctests verify that your code behaves as described.

# Running Doctests

To run doctests, include the following at the bottom of your Python file:
```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

This will run the tests inside your docstrings, checking if the actual outputs match the expected ones.



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



Here's a slide explaining how to use `doctest` in Jupyter notebooks, tailored for your audience:



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


# Building a Test Suite

1. **Build up a suite of tests**: Create a set of tests that cover different parts of your program.
2. **Run all tests in one go**: Use a script or notebook to run all tests automatically.
3. **Test sane cases, then edge cases**: Test common scenarios first, then unusual inputs.
   - Example: What happens when you input extreme temperatures like -100°C or 100°C?



# Review: Can you…

- Understand the difference between testing and debugging?
- Describe one approach to debugging?
- State why we test?
- List common testing strategies?

