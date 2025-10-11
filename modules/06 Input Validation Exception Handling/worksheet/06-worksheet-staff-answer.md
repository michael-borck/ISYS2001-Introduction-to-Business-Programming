---
title: "Python Input Validation: Staff Answer Key and Instructor Guide"
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

### Introduction

This guide provides answers to the questions and tasks in the student worksheet,
along with additional notes for instructors to facilitate discussion and
learning.

### Questions

1. What is input validation?

**Answer:** Input validation is the process of checking and ensuring that data
entered by users meets specific criteria or constraints before it's processed by
a program. It helps maintain data integrity and prevent errors or security
vulnerabilities.

**Instructor Note:** Encourage students to discuss different types of validation
(e.g., type checking, range checking, format validation) and their importance in
various applications.

2. Why do we need to validate input?

**Answer:** We validate input to:
- Prevent errors and crashes in our program
- Ensure data integrity and consistency
- Enhance security by preventing malicious inputs
- Improve user experience by providing immediate feedback

**Instructor Note:** Discuss real-world examples of input validation failures
and their consequences.

3. Why are we using the PyInputPlus module instead of the built-in input() function?

**Answer:** PyInputPlus offers several advantages over the built-in input() function:
- Built-in input validation features
- Automatic re-prompting for invalid inputs
- Type-specific input functions (e.g., inputStr(), inputFloat())
- Easy implementation of complex validation rules

**Instructor Note:** Demonstrate the difference between using input() and
PyInputPlus functions to highlight the benefits.

### Hands-on Exercise: Enhancing Our Weather Utility

#### Task 1: Setting Up

**Instructor Note:** Ensure all students have successfully installed
PyInputPlus. Address any installation issues.

#### Task 2: Implementing Input Validation

**Sample Solution:**

```python
import pyinputplus as pyip

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

**Instructor Note:** Explain the purpose of each PyInputPlus function used and
how they contribute to input validation. Discuss the importance of exception
handling.

#### Task 3: Using the Function

**Sample Solution:**

```python
city, temp, wind_speed, wind_direction = get_weather_data()
if city:
    print(f"Weather in {city}: {temp}°C, Wind: {wind_speed} km/h {wind_direction}")
else:
    print("Failed to get weather data.")
```

**Instructor Note:** Demonstrate how the function handles both valid and invalid
inputs.

#### Task 4: Celsius to Fahrenheit Conversion

**Sample Solution:**

```python
def celsius_to_fahrenheit():
    celsius = pyip.inputFloat("Enter temperature in Celsius: ")
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
```

**Instructor Note:** Discuss the importance of formatting output (e.g., rounding
to two decimal places) and how it relates to data presentation.

#### Task 5: Testing

**Instructor Note:** Guide students through testing various scenarios:
- Valid inputs: e.g., "London", 20.5, 10, "N"
- Invalid inputs: e.g., "123" for city name, "abc" for temperature
- Edge cases: e.g., -273.15°C (absolute zero), 1000 km/h wind speed

### Reflection

1. How does PyInputPlus simplify input validation compared to using the built-in
   input() function?

**Sample Answer:** PyInputPlus simplifies input validation by providing built-in
functions for different data types, automatic re-prompting for invalid inputs,
and easy implementation of validation rules. This reduces the amount of code
needed for input validation and makes the process more robust and user-friendly.

2. What challenges did you face while implementing input validation?

**Sample Answer:** Challenges might include:
- Understanding the different PyInputPlus functions and their parameters
- Deciding on appropriate validation rules for each input
- Handling unexpected exceptions

3. Can you think of any other weather-related data that could benefit from input
   validation? How would you implement it?

**Sample Answer:** Additional weather data could include:
- Humidity (percentage): `pyip.inputInt("Enter humidity (%): ", min=0, max=100)`
- Precipitation (mm): `pyip.inputFloat("Enter precipitation (mm): ", min=0)`
- Cloud cover (oktas): `pyip.inputInt("Enter cloud cover (0-8 oktas): ", min=0, max=8)`

**Instructor Note:** Encourage students to think about real-world applications
of their weather utility and how input validation contributes to its reliability
and usability.

### Additional Discussion Points

- The balance between strict validation and user experience
- The role of input validation in data science and machine learning pipelines
- Security implications of input validation in web applications
- Best practices for error messages and user feedback in input validation