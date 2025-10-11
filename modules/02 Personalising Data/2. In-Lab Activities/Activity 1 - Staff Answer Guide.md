---
title: "STAFF ANSWER GUIDE: Activity 1: Personalised Greeting & User Preferences"
subtitle: "From Input to Impact: Crafting Personalised Greetings in Python"
author: "Michael Borck"
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

# Staff Answer Guide for Activity 1

## Overview

This guide provides a sample solution and explanations for Activity 1: Personalized Greeting & User Preferences. The goal of this activity is to reinforce:
- How to collect user input with `input()`.
- Storing responses in variables.
- Producing personalised output using `print()`.

This resource is intended to assist tutors in guiding students through the exercise and addressing common pitfalls.

## Sample Solution

Below is a sample solution that demonstrates two acceptable approaches to constructing the output message.

```python
# Step 1: Collect user input and store responses in variables
name = input("What is your name? ")
favourite_colour = input("What is your favourite colour? ")
favourite_food = input("What is your favourite food? ")

# Step 2: Construct a personalised greeting using string concatenation
greeting = "Hello, " + name + "! Your favourite colour is " + favourite_colour + " and you love " + favourite_food + "."
print(greeting)

# Alternatively, using comma-separated arguments in print() for automatic spacing:
print("Hello,", name + "!", "Your favourite colour is", favourite_colour + ",", "and you love", favourite_food + ".")
```

## Explanation of the Code

- **Collecting Input:**  
  - The `input()` function prompts the user and returns their response as a string.
  - Each response is stored in a variable (`name`, `favourite_colour`, and `favourite_food`), which can be reused later in the programme.

- **Constructing the Output Message:**  
  There are two common methods shown:
  
  1. **String Concatenation using the `+` Operator:**  
     - Combines literal strings with variables.
     - Example: `"Hello, " + name + "!"`  
     - Tutors should remind students to manage spaces and punctuation carefully.
  
  2. **Using Comma-Separated Arguments in `print()`:**  
     - Multiple items passed to `print()` are automatically separated by a space.
     - Example: `print("Hello,", name + "!")`  
     - This method simplifies formatting by reducing the need to explicitly include spaces.

- **Output:**  
  - Both methods produce a personalised message that incorporates the user's inputs.
  - Encourage students to test with various inputs to ensure their programme works as intended.

## Tutor Tips

- **Common Pitfalls:**  
  - Students might forget that `input()` always returns a string, even if the user enters numbers.
  - Managing spaces correctly when using the `+` operator can be challenging. Encourage them to compare the two methods.
  
- **Discussion Points:**  
  - Ask students why it is useful to store user input in variables.
  - Discuss the readability benefits of each method and when one might be preferred over the other.
  
- **Further Exploration:**  
  - Once students are comfortable, mention that f-strings provide an even cleaner way to format output and will be introduced later.
  - Invite students to extend the programme by adding another preference (e.g., favourite hobby) to further personalise their greeting.
