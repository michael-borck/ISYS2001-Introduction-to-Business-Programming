---
title: "Python Input Validation"
subtitle: "Python Essentials"
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
## Introduction

Input validation is a crucial aspect of programming that ensures the data
entered by users meets specific criteria before it's processed. This worksheet
will guide you through understanding and implementing input validation using the
PyInputPlus module in Python.

## Aim

To understand the importance of input validation and practice implementing it
using PyInputPlus in a weather utility application.

## Questions

1. In your own words, what is input validation?

2. Why do we need to validate input?

3. Why are we using the PyInputPlus module instead of the built-in input() function?

## Hands-on Exercise: Enhancing Our Weather Utility

Let's enhance our weather utility functions from Lecture 1 with PyInputPlus for input and proper exception handling:

### Task 1: Setting Up

First, install PyInputPlus using pip:

```
pip install pyinputplus
```

Then, import the module in your Python script:

```python
import pyinputplus as pyip
```

### Task 2: Implementing Input Validation

Create a function called `get_weather_data()` that:

1. Uses `pyip.inputStr()` to get the city name
2. Uses `pyip.inputFloat()` to get the temperature
3. Implements exception handling for potential errors
4. Uses `pyip.inputFloat()` with a minimum value for wind speed
5. Uses `pyip.inputChoice()` for wind direction

```python
def get_weather_data():
    try:
        city = pyip.inputStr("Enter city name: ")
        temp = pyip.inputFloat("Enter temperature in Celsius: ")
        wind_speed = pyip.inputFloat("Enter wind speed (km/h): ", min=0)
        wind_direction = pyip.inputChoice(["N", "S", "E", "W"], prompt="Enter wind direction (N/S/E/W): ")
        return city, temp, wind_speed, wind_direction
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None, None, None
```

### Task 3: Using the Function

Use the `get_weather_data()` function and print the results:

```python
city, temp, wind_speed, wind_direction = get_weather_data()
if city:
    print(f"Weather in {city}: {temp}°C, Wind: {wind_speed} km/h {wind_direction}")
else:
    print("Failed to get weather data.")
```

### Task 4: Celsius to Fahrenheit Conversion

Create a function to convert Celsius to Fahrenheit using PyInputPlus:

```python
def celsius_to_fahrenheit():
    celsius = pyip.inputFloat("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
```

### Task 5: Testing

Run your script and test it with various inputs, including:
- Valid inputs
- Invalid inputs (e.g., non-numeric temperature)
- Edge cases (e.g., very high or low temperatures)

## Reflection

After completing the tasks, answer the following questions:

1. How does PyInputPlus simplify input validation compared to using the built-in
   input() function?

2. What challenges did you face while implementing input validation?

3. Can you think of any other weather-related data that could benefit from input
   validation? How would you implement it?