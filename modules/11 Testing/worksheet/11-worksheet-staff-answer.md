---
title: "STAFF-ANSWER: Weathering the Bugs: A Hands-on Guide to Testing and Debugging in Python"
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
### **Exercise 1: Debugging with `print()`**

#### Code Setup:
The original function had an issue where temperatures between 15 and 25 returned
"Rainy" by default. However, the conditions weren’t structured properly to
handle this.

#### Debugging with `print()`:
We can insert `print()` statements to trace the value of `temp` and see how the logic flows.

```python
def predict_weather(temp):
    print(f"Current temperature: {temp}")
    if temp > 25:
        print("It's sunny!")
        return "Sunny"
    if temp < 15:
        print("It's cloudy!")
        return "Cloudy"
    print("It seems rainy.")
    return "Rainy"
```

#### Output after Debugging:
When testing the function with a value like `predict_weather(20)`, we noticed
that it directly jumped to "Rainy," even though we expected more conditions to
be checked.

#### Corrected Code:

```python
def predict_weather(temp):
    if temp > 25:
        return "Sunny"
    elif temp < 15:
        return "Cloudy"
    else:
        return "Rainy"
```

#### Expected Output:
```python
predict_weather(30)  # Sunny
predict_weather(10)  # Cloudy
predict_weather(20)  # Rainy
```

The issue was that the two `if` statements acted independently, so the second
condition (`if temp < 15`) wasn't executed properly. Changing the second `if` to
`elif` fixed this problem.



### **Exercise 2: Testing with `assert()`**

#### Code Setup:
We can now add `assert()` statements to test if the function behaves as expected.

```python
def predict_weather(temp):
    if temp > 25:
        return "Sunny"
    elif temp < 15:
        return "Cloudy"
    else:
        return "Rainy"
```

#### Testing with `assert()`:

```python
assert predict_weather(30) == 'Sunny'
assert predict_weather(10) == 'Cloudy'
assert predict_weather(20) == 'Rainy'
```

#### Output:
The code passes all the assertions, indicating that the function is working
correctly. If any of the conditions failed, `assert()` would raise an
`AssertionError`, helping us locate the issue.



### **Exercise 3: Writing and Running Doctests**

#### Code Setup:
Now we will add `doctest` cases inside the function's docstring.

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
    elif temp < 15:
        return "Cloudy"
    else:
        return "Rainy"
```

#### Running the Doctests:

```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

#### Output:
If all the doctests pass, there will be no output. If any of the tests fail,
`doctest` will provide a message showing where the actual output differed from
the expected result.



### **Optional Exercise: Debugging with `pdb`**

#### Code Setup with `pdb`:
Here’s how you can insert `breakpoint()` to step through the function using `pdb`.

```python
def predict_weather(temp):
    breakpoint()  # This will stop the execution and enter pdb mode
    if temp > 25:
        return "Sunny"
    elif temp < 15:
        return "Cloudy"
    else:
        return "Rainy"
```

#### Running the Code:
When you run the function in Jupyter or a Python shell, it will stop at the
`breakpoint()` and let you interact with the variables.

- Use `n` (next) to step through the code.
- Use `p temp` to print the value of `temp`.

Example:

```python
predict_weather(30)
```

You can then step through each line and check how the function is processing the input.

#### Output:
Using `pdb` allows you to inspect the state of the program at various stages,
making it easier to identify where things go wrong.

### **Summary of Results:**

- **Exercise 1**: Using `print()` helped us identify a logical error in the function.
- **Exercise 2**: We verified that our function passed a set of test cases using `assert()`.
- **Exercise 3**: We successfully wrote and executed `doctest` cases within the function's docstring.
- **Optional Exercise**: We explored using `pdb` to step through the code and interact with it line by line.
