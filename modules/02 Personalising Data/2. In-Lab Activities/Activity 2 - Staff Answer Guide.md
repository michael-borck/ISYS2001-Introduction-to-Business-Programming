---
title: "STAFF ANSWER GUIDE: Activity 2: Ad-Hoc User Preferences Survey"
subtitle: "Explore and Experiment: Crafting Your Own User Preferences Survey"
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

# Staff Answer Guide: Activity 2 – Ad-Hoc User Preferences Survey

## Overview

This guide provides a sample solution and explanations for Activity 2. The goal is to create a Python script that gathers user preferences in an ad-hoc manner and then displays them. The exercise encourages experimentation with basic input/output functions in Python. In addition, mini-challenges are included to foster creative problem-solving and to hint at upcoming concepts such as basic calculations and alternative output formatting.

## Sample Solution

Below is one example of how a student might implement the activity. Note that there is no single correct solution—students are encouraged to be creative.

### Main Survey Implementation

```python
# Collect user input for various preferences
name = input("What is your name? ")
favourite_colour = input("What's your favourite colour? ")
favourite_food = input("What's your favourite food? ")
favourite_hobby = input("What's your favourite hobby? ")

# Option 1: Using string concatenation
print("Hello, " + name + "! Your favourite colour is " + favourite_colour +
      ", you love " + favourite_food + ", and you enjoy " + favourite_hobby + ".")

# Option 2: Using comma-separated arguments for automatic spacing
print("Hello,", name + "!", "Your favourite colour is", favourite_colour + ",",
      "you love", favourite_food + ", and you enjoy", favourite_hobby + ".")
```

## Mini-Challenges

These mini-challenges are designed to stimulate further creativity and introduce additional concepts:

### Challenge 1: Starred Preferences
Print each preference on a separate line with a star (`*`) at the beginning of each line.

```python
print("* Name:", name)
print("* Favourite Colour:", favourite_colour)
print("* Favourite Food:", favourite_food)
print("* Favourite Hobby:", favourite_hobby)
```

### Challenge 2: Age Calculator
Ask the user for their birth year and calculate how old they will be this year.  
*Hint: You may use the `datetime` module to get the current year.*

```python
import datetime

birth_year = int(input("What year were you born? "))
current_year = datetime.datetime.now().year
age = current_year - birth_year
print("You are", age, "years old!")
```

### Challenge 3 (Optional Advanced): F-String Formatting
Refactor the summary message to use Python's f-string formatting instead of string concatenation. (This is an optional advanced challenge intended for students who wish to explore newer formatting methods.)

```python
print(f"Hello, {name}! Your favourite colour is {favourite_colour}, you love {favourite_food}, and you enjoy {favourite_hobby}.")
```

## Explanation of the Code

- **Collecting Input:**  
  - The `input()` function is used to prompt the user for information.
  - Each response is stored in its own variable (e.g., `name`, `favourite_colour`) for later use.

- **Constructing the Output Message:**  
  - **Option 1 (String Concatenation):**  
    Combines strings using the `+` operator. Note that extra spaces and punctuation must be managed manually.
  - **Option 2 (Comma-Separated Arguments):**  
    When multiple arguments are passed to `print()`, Python automatically inserts spaces between them.

- **Mini-Challenges:**  
  - **Starred Preferences:**  
    This challenge reinforces printing multiple lines and adds a simple formatting twist.
  - **Age Calculator:**  
    Introduces the concept of using external modules (like `datetime`) and basic arithmetic operations to perform a calculation.
  - **F-String Formatting:**  
    Provides a glimpse into a modern way of formatting strings. This challenge is optional and can be attempted by more advanced students.

## Tutor Tips

- **Encourage Flexibility:**  
  Remind students that there are several ways to construct their output. The goal is to practice and understand basic input/output operations.
  
- **Address Common Issues:**  
  - Ensure students understand that the `input()` function always returns a string.
  - Clarify the differences between string concatenation and using commas in the `print()` function.
  
- **Mini-Challenges as Extensions:**  
  - Explain that the mini-challenges are optional but provide great opportunities to stretch their understanding.
  - For the f-string challenge, emphasize that it’s an introduction to a topic that will be covered in more detail later.

- **Discussion Points:**  
  - Ask students what other preferences they might add.
  - Discuss the benefits of clear output formatting.
  - Encourage students to share creative modifications they made to the program.

## Extension Ideas

- **Additional Preferences:**  
  Invite students to add more questions (e.g., favourite movie, book, travel destination) to further personalize the output.
  
- **Refactoring:**  
  Once students are comfortable, challenge them to refactor their code for improved readability or to implement functions to reuse code.
