---
title: "Weathering the Bugs: A Hands-on Guide to Testing and Debugging in Python"
subtitle: "Master the basics of debugging and testing with real-world weather data—one bug at a time!"
format:
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

## **Introduction and Background**

Testing and debugging are essential parts of software development. As a developer, you need to ensure that your code works as expected and handle errors efficiently. In this worksheet, you’ll practice using simple debugging tools like `print()`, `assert()`, and `doctest` to verify that your code functions correctly.

This worksheet will guide you through the process of creating a Jupyter notebook where you’ll implement and test Python code in the context of weather data, which fits our ongoing theme.

## **Learning Objectives**
By the end of this worksheet, you will:
- Understand how to use `print()` to debug code.
- Write simple tests using `assert()`.
- Create and run `doctest` to validate function behavior.
- (Optional) Explore how to use Python's built-in debugger, `pdb`, for step-by-step debugging.



## **Exercise 1: Debugging with `print()`**

In this exercise, you’ll debug a weather prediction function using `print()` statements to identify and fix an error.

1. **Code Setup**: 
   Below is a weather prediction function. There's an error in the function that causes it to return incorrect results for certain inputs. Use `print()` statements to trace the values of variables and debug the function.

```python
def predict_weather(temp):
    if temp > 25:
        return "Sunny"
    if temp < 15:
        return "Cloudy"
    return "Rainy"
```

2. **Task**: 
   Add `print()` statements inside the function to trace the value of `temp` and understand where the logic might be going wrong.

3. **Question**: 
   What was the bug? Fix the function so it works as intended.

4. **Expected Output**:
   - `predict_weather(30)` should return `'Sunny'`
   - `predict_weather(10)` should return `'Cloudy'`
   - `predict_weather(20)` should return `'Rainy'`



## **Exercise 2: Testing with `assert()`**

In this exercise, you’ll use `assert()` to test a function’s output. The `assert()` statement will raise an error if the condition is false, which helps to test the correctness of your code.

1. **Code Setup**:
   Modify the `predict_weather()` function from Exercise 1 to use `assert()` for testing.

```python
def predict_weather(temp):
    if temp > 25:
        return "Sunny"
    if temp < 15:
        return "Cloudy"
    return "Rainy"
```

2. **Task**: 
   Write `assert()` statements to test the function with different inputs. For example:

```python
assert predict_weather(30) == 'Sunny'
assert predict_weather(10) == 'Cloudy'
assert predict_weather(20) == 'Rainy'
```

3. **Question**: 
   Does your function pass all the tests? If not, fix it and re-run the tests.



## **Exercise 3: Writing and Running Doctests**

Now, you’ll use `doctest` to write test cases directly in the function’s docstring.

1. **Code Setup**: 
   Modify your `predict_weather()` function to include doctests.

```python
def predict_weather(temp):
    """
    Predict tomorrow's weather based on today's temperature.

    >>> predict_weather(30)
    'Sunny'
    >>> predict_weather(10)
    'Cloudy'
    >>> predict_weather(20)
    'Rainy'
    """
    if temp > 25:
        return "Sunny"
    if temp < 15:
        return "Cloudy"
    return "Rainy"
```

2. **Task**: 
   Add the `doctest` module to your code and run it. Example:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

3. **Question**: 
   Do your doctests pass? If not, fix the function and re-run the doctests.



## **Optional Exercise: Debugging with `pdb`**

If you're feeling adventurous, explore how to use the Python Debugger (`pdb`) to step through your code.

1. **Task**: 
   Add a `breakpoint()` in your `predict_weather()` function, and run the cell to step through the code.

```python
def predict_weather(temp):
    breakpoint()
    if temp > 25:
        return "Sunny"
    if temp < 15:
        return "Cloudy"
    return "Rainy"
```

2. **Steps**:
   - Run the code and use the `pdb` commands to navigate through the function.
   - Use `n` to step through the code and `p` to print variable values.

3. **Question**: 
   How did using `pdb` help you understand the behavior of the function?

