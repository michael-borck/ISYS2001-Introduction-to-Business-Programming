---
title: "Python Decision Syntax"
subtitle: "How to Write if/elif/else in Python"
format: 
  pptx: default
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
# From Flowcharts to Python Code

By the end of this module, you will be able to:

- ✅ Understand the basic structure of if/elif/else statements in Python
- ✅ Use comparison operators to create boolean conditions
- ✅ Write simple decision-making code using if statements
- ✅ Implement multiple choice decisions with elif
- ✅ Convert flowcharts into Python code
- ✅ Recognise common patterns and pitfalls in decision logic
- ✅ Prepare for more complex conditions in W3.3
  
Remember the three patterns from previous module? Here's how they look in Python:

::: {.notes}
The slide "From Flowcharts to Python Code" outlines the key learning objectives for converting decision logic flowcharts into Python code using if/elif/else statements. Students will gain an understanding of the basic structure and syntax of these statements, learn to use comparison operators to create boolean conditions, and write simple decision-making code. They will also learn to implement multiple choice decisions using elif and recognise common patterns and pitfalls in decision logic.

By the end of this lesson, students will be able to confidently convert flowcharts into functional Python code. They will have a solid foundation in the fundamentals of decision-making logic and be well-prepared for the more complex conditions covered in the upcoming W3.3 lesson. The slide serves as a roadmap for the topics covered in this lesson, ensuring students have a clear understanding of what they will learn and achieve.
:::

# **Pattern 1: Single Choice**
```python
if condition:
    # This code runs if condition is True
    # Notice the indentation!
```

::: {.notes}
The Single Choice pattern is used when there is only one condition to check in a decision. This pattern involves an if statement followed by a single action to perform if the condition is true. If the condition evaluates to false, the program simply skips the action and continues with the next line of code.

In Python, the syntax for the Single Choice pattern is straightforward. The if keyword is followed by the condition in parentheses, and the action to perform is indented on the next line. It's important to ensure proper indentation, as this is how Python determines which lines of code belong to the if statement.
:::

# **Pattern 2: Either/Or Choice**
```python
if condition:
    # Runs if condition is True
else:
    # Runs if condition is False
```

::: {.notes}
The Either/Or Choice pattern in Python allows for decision-making between two mutually exclusive options based on a single condition. It is represented in flowcharts by a decision diamond with two outgoing arrows, typically labelled "Yes" and "No". The code equivalent uses an if-else statement, where the if block executes when the condition is True, and the else block executes when it is False.

Proper indentation is crucial in Python to define the scope of the if and else blocks. The condition in the if statement must evaluate to a boolean value (True or False). Comparison operators like ==, !=, <, >, <=, and >= are commonly used to create conditions. It's important to use a colon (:) after the if and else keywords and to indent the code within each block consistently.
:::

# **Pattern 3: Multiple Options**
```python
if condition1:
    # Runs if condition1 is True
elif condition2:
    # Runs if condition1 is False AND condition2 is True
else:
    # Runs if all conditions are False
```

::: {.notes}
Multiple options patterns in flowcharts and code involve selecting from three or more choices based on certain criteria. This pattern is represented by a decision symbol with multiple branches, each leading to a different action or outcome depending on the specific conditions met.

In Python, multiple options are typically handled using an if-elif-else chain. The if statement checks the first condition, and if it's true, the corresponding code block is executed. If the condition is false, the program moves to the next elif (else if) statement to check another condition. This process continues until a condition is met or the final else block is reached, which handles any remaining cases not covered by the previous conditions.
:::

# Critical Python Rules

1. **Colon required**: Every `if`, `elif`, `else` needs a `:`
2. **Indentation matters**: Python uses spaces/tabs to group code
3. **Boolean result**: Conditions must evaluate to True or False

::: {.notes}
Critical Python rules form the foundation of writing effective and error-free code. These rules cover various aspects such as indentation, variable naming conventions, and proper use of data types. By adhering to these rules, Python programmers can ensure their code is readable, maintainable, and less prone to errors.

Mastering the critical Python rules is essential for beginners to avoid common mistakes and develop good coding practices. Consistent indentation, meaningful variable names, and appropriate use of data types are just a few examples of the rules that should be followed diligently. As programmers gain experience and tackle more complex projects, a solid understanding of these rules becomes even more crucial for writing clean and efficient code.
:::

# Understanding True and False

Recall data types from last week? There's a special type called **boolean** that can only be True or False. We call that a 'decision' or 'condition'.

::: {.notes}
Understanding True and False is a critical concept in programming. In Python, True and False are special keywords representing the truth values of logical expressions. These values are the basis for making decisions and controlling the flow of a program.

Boolean expressions, formed using comparison operators such as equality (==), inequality (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=), evaluate to either True or False. Mastering these comparison operators and their use in conditional statements like if, elif, and else is essential for writing effective Python code that can make decisions based on different conditions.
:::

# Boolean Basics

Every condition in Python becomes a boolean value:

```python
temperature = 75

# These create boolean values
is_hot = temperature > 80      # False
is_cold = temperature < 60     # False  
is_comfortable = True          # Directly set

# Using in decisions
if is_hot:
    print("Turn on AC")        # Won't run (is_hot is False)
```

::: {.notes}
Boolean values represent the fundamental concepts of true and false in programming. They are used to make decisions, control program flow, and evaluate conditions.

Python represents boolean values using the keywords True and False. These values can be assigned to variables, returned from functions, and used in logical expressions with operators such as and, or, and not to create more complex conditions.
:::

# Comparison Operators: The Building Blocks

These operators create boolean values by comparing things:

```python
age = 18

# Equality (TWO equals signs!)
age == 18        # True
age == 21        # False

# Inequality  
age != 21        # True (18 is not equal to 21)

# Ordering
age < 21         # True (18 is less than 21)
age > 21         # False
age <= 18        # True (less than OR equal)
age >= 18        # True (greater than OR equal)
```

::: {.notes}
Comparison operators are the fundamental building blocks used to create conditions in Python. These operators allow you to compare values and variables, resulting in either True or False. The comparison operators in Python include equal to (==), not equal to (!=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=).

By combining comparison operators with variables, constants, and other operators, you can construct expressions that evaluate to True or False. These expressions form the basis of conditions used in if statements and loops, enabling your program to make decisions and control its flow based on the comparison results. Mastering comparison operators is crucial for writing effective conditional logic in Python.
:::

# The Most Common Beginner Error

**CRITICAL WARNING**: `=` assigns, `==` compares!

```python
# WRONG - This assigns 5 to x!
if x = 5:        # SyntaxError!

# RIGHT - This compares x to 5
if x == 5:       # Checks if x equals 5
```

**Memory trick**: 
- `x = 5` → "x becomes 5" (assignment)
- `x == 5` → "x equals 5?" (question/comparison)

::: {.notes}
The most common beginner error when working with Python is confusing the assignment operator (`=`) with the equality comparison operator (`==`). The assignment operator is used to assign a value to a variable, such as `x = 5`, which means "x becomes 5". On the other hand, the equality comparison operator is used to compare two values and returns a Boolean result (True or False), such as `x == 5`, which means "x equals 5?".

It's crucial to understand the difference between these two operators to avoid logical errors in your code. Using the wrong operator can lead to unexpected behaviour and difficult-to-debug issues. Always double-check your code to ensure you're using the correct operator for the intended purpose, whether it's assigning a value to a variable or comparing two values for equality.
:::

# Testing Your Understanding

What do these expressions evaluate to if `score = 85`?

```python
score > 90       # ?
score == 85      # ?
score != 100     # ?
score <= 85      # ?
```

**Answers**: False, True, True, True

::: {.notes}
This slide aims to test the audience's understanding of the concepts covered in the previous slides. It serves as a checkpoint to ensure the participants have grasped the key points before moving on to more advanced topics.

The previous slides have covered topics such as flowcharts, Python code patterns for single choice, either/or choice, and multiple options, as well as critical Python rules, boolean basics, comparison operators, and common beginner errors. The upcoming slides will build upon this foundation, delving into practical applications such as building simple decisions, creating a grade calculator, handling multiple choices with elif chains, and converting flowcharts to code for various scenarios like a simple login system and temperature advice.
:::

# Building Simple Decisions: Single Choice Pattern

```python
temperature = 95

if temperature > 90:
    print("It's really hot today!")
    print("Stay hydrated!")

print("This always runs")
```

**Key point**: Code after the if block always runs

::: {.notes}
The Single Choice pattern is the simplest decision structure in programming. It executes a block of code only if a certain condition is true, otherwise it skips that block and continues with the rest of the program. This pattern is represented by the if statement in Python.

To implement the Single Choice pattern, first evaluate a condition that results in a boolean value (True or False). If the condition is true, the indented code block following the if statement will be executed. If the condition is false, the code block is skipped entirely and the program continues with the next line of code after the if block.
:::

# Building Simple Decisions: Either/Or Pattern

```python
age = 17

if age >= 18:
    print("You can vote!")
else:
    print("You'll be able to vote soon!")

print("Thanks for checking!")
```

**Key point**: Exactly one of the two branches runs

::: {.notes}
The Either/Or pattern is used when a decision has two possible outcomes based on a single condition. In Python, this pattern is implemented using an if-else statement, where the if block is executed if the condition evaluates to True, and the else block is executed if the condition evaluates to False.

To create an Either/Or decision in Python, first define the condition using comparison operators such as ==, !=, <, >, <=, or >=. Then, write the code for the actions to be taken when the condition is True in the if block, and the actions to be taken when the condition is False in the else block. It's important to ensure that the condition is well-defined and that the actions in each block are mutually exclusive to avoid unexpected behaviour.
:::

# Your First Grade Calculator

Let's convert this flowchart to code:

```
<score >= 90?>
    ↙       ↘
   Yes       No
    ↓         ↓
[Grade = A] [Grade = F]
```

```python
score = 92

if score >= 90:
    grade = "A"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

::: {.notes}
Your First Grade Calculator slide focuses on building a program that calculates grades based on user input. It likely demonstrates how to use elif statements to handle multiple possible input values, such as different letter grades or percentage ranges.

The slide is part of a larger presentation on decision-making in Python, covering topics like flowcharts, boolean logic, comparison operators, and common patterns for constructing decision structures. The slides following this one dive deeper into the elif chain pattern and discuss considerations like input order, handling edge cases, and avoiding redundancy in code.
:::

# Multiple Choice with elif: The elif Chain

For multiple categories, use `elif` (short for "else if"):

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:    # Only checked if score < 90
    grade = "B"
elif score >= 70:    # Only checked if score < 80
    grade = "C"
elif score >= 60:    # Only checked if score < 70
    grade = "D"
else:                # Only if all conditions false
    grade = "F"

print(f"Grade: {grade}")
```

::: {.notes}
The elif chain allows for multiple choices in a decision structure. It is used when there are more than two possible outcomes based on the value of a single variable. The conditions are checked in order from top to bottom, and the first condition that evaluates to True will have its associated code block executed. All remaining elif and else clauses are skipped.

It's critical to order the conditions carefully, as the first match will be executed even if a later condition would also evaluate to True. If none of the conditions are True, the else block is executed. This acts as a "catch-all" for any cases not covered by the if and elif conditions.
:::

# Why Order Matters

**WRONG** - Never reaches B or C!
```python
if score >= 70:      # Catches 85!
    grade = "C"
elif score >= 80:    # Never reached
    grade = "B"
elif score >= 90:    # Never reached
    grade = "A"
```

**RIGHT** - Check highest first:
```python
if score >= 90:      # Check A first
    grade = "A"
elif score >= 80:    # Then B
    grade = "B"
elif score >= 70:    # Then C
    grade = "C"
```

::: {.notes}
The order of conditions in an if/elif/else statement is critical. Python checks each condition sequentially until it finds one that evaluates to True, then executes the associated code block and skips the rest. If the conditions are in the wrong order, the code may produce unexpected results or even errors.

When crafting if/elif/else statements, put the most specific or restrictive conditions first, followed by more general ones. This ensures the code flows logically and handles all possible cases correctly. By carefully considering the order of conditions, you can create robust, error-free code that behaves as intended.
:::

# Complete Grade Calculator

```python
print("=== Grade Calculator ===")

score = float(input("Enter your score (0-100): "))

if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "Satisfactory"
elif score >= 60:
    grade = "D"
    message = "Needs improvement"
else:
    grade = "F"
    message = "Please see instructor"

print(f"Score: {score}")
print(f"Grade: {grade}")
print(message)
```

::: {.notes}
Complete Grade Calculator

This slide presents the final version of the grade calculator program, which incorporates all the concepts and patterns covered in the previous slides. The program takes user input for various grade components, such as assignments, quizzes, and exams, and calculates the overall grade based on the specified weights for each component.

The code for the complete grade calculator demonstrates the application of the single choice, either/or choice, and multiple options patterns, as well as the use of elif chains and range checking. It also showcases best practices for handling multiple valid inputs, avoiding redundancy, and addressing edge cases to ensure a robust and user-friendly program.
:::

# Common Patterns and Pitfalls

::: {.notes}
Common patterns in Python decision making include single choice, either/or choice, and multiple options using an elif chain. These patterns correspond to specific flowchart structures and can be implemented using if, if-else, and if-elif-else statements respectively. It's important to understand how to translate these flowchart patterns into Python code correctly.

There are also several pitfalls to watch out for when working with Python conditionals. These include forgetting to use colons at the end of if/elif/else lines, incorrect indentation, using the assignment operator (=) instead of the equality operator (==) in comparisons, and incorrect Boolean logic. Analysing your code carefully and testing thoroughly can help avoid these common errors.
:::

# Range Checking

```python
temperature = 72

# Check if temperature is in comfortable range (68-75)
if temperature >= 68 and temperature <= 75:
    print("Perfect temperature!")
```

::: {.notes}
Range checking is a technique used to validate whether a value falls within a specified range. It involves comparing the value against the lower and upper bounds of the acceptable range using comparison operators such as greater than or equal to (>=) and less than or equal to (<=). If the value satisfies both conditions, it is considered valid; otherwise, it is deemed invalid.

When implementing range checking in Python, it is crucial to use the appropriate comparison operators and logical operators (such as and) to combine the conditions. The if statement is employed to evaluate the range conditions and execute the corresponding code block based on the result. Range checking is commonly used in scenarios where input values need to be restricted to a specific range, such as validating ages, grades, or temperatures.
:::

# Multiple Valid Inputs

```python
answer = input("Continue? (Y/N): ")

# Accept multiple versions
if answer == "Y" or answer == "y" or answer == "yes":
    print("Continuing...")

# Simpler approach
if answer.upper() == "Y":
    print("Continuing...")
```

::: {.notes}
Multiple valid inputs can be handled using the or operator in Python. This allows you to check if a variable equals one value or another value, and execute the same code for either case.

For example, if you want to check if the user entered 'y' or 'Y' to indicate yes, you could write: if answer == 'y' or answer == 'Y'. This avoids needing to write the same code twice in separate if statements.
:::

# Avoiding Redundancy

```python
# Redundant - elif already means "else if previous was false"
if score >= 90:
    grade = "A"
elif score < 90 and score >= 80:  # Don't need score < 90
    grade = "B"

# Better - elif implies the previous was false
if score >= 90:
    grade = "A"
elif score >= 80:  # We only get here if score < 90
    grade = "B"
```

::: {.notes}
Avoiding redundancy is crucial when writing conditional statements in Python. Redundant code not only makes your program harder to read and maintain but can also introduce bugs. Look for opportunities to combine conditions using logical operators like 'and' and 'or' to simplify your code and reduce duplication.

When chaining multiple elif statements, be careful not to overlap conditions. Each elif condition should handle a distinct case not covered by the previous conditions. If you find yourself repeating the same action for multiple conditions, consider combining those conditions into a single branch to avoid redundancy and make your code more concise.
:::

# Edge Cases to Consider

```python
score = float(input("Enter score: "))

# What if user enters:
# - Exactly 90? (Should be A)
# - 89.9? (Should be B)  
# - -10? (Invalid!)
# - 150? (Invalid!)
# - "abc"? (ValueError!)

# We'll handle input validation in next module
```

::: {.notes}
Edge cases are important to consider when designing decision-making logic in code. These are situations that may not fit neatly into the main paths or patterns you've defined. Identifying and handling edge cases is crucial for creating robust, error-free programs.

Some common edge cases include invalid inputs, boundary values, and unexpected combinations of conditions. For example, when checking a grade, you might need to handle inputs that are outside the valid range, like negative numbers or values over 100. Thinking through these possibilities and adding appropriate checks can prevent your program from crashing or producing incorrect results.
:::

# Converting Flowcharts to Code: Simple Login

**Flowchart**:
```
<password == "secret123"?>
    ↙              ↘
   Yes              No
    ↓                ↓
[Welcome!]      [Access Denied]
```

**Your code**:
```python
password = input("Enter password: ")

if password == "secret123":
    print("Welcome!")
else:
    print("Access Denied")
```

::: {.notes}
This slide demonstrates how to convert a simple login flowchart into Python code. The flowchart depicts the logic for a basic username and password verification process, with a single choice pattern for checking if the entered credentials match the stored values. If the username and password are correct, the user is granted access; otherwise, an error message is displayed.

To implement this in Python, we start by prompting the user to enter their username and password. We then compare the entered values against the predefined correct credentials using an if statement. If the condition evaluates to True, meaning the username and password match, we print a success message. If the condition is False, we print an error message indicating invalid login details. This example showcases the direct translation of a flowchart's decision points and actions into executable Python code.
:::

# Converting Flowcharts to Code: Temperature Advice

**Requirements**: 

- Below 32°F: "Freezing! Bundle up!"
- 32-50°F: "Cold, wear a jacket"  
- 51-70°F: "Mild weather"
- Above 70°F: "Nice and warm!"

**Your turn**: Write the code!

::: {.notes}
This slide presents a temperature advice flowchart converted into Python code. The code uses multiple if-elif statements to check the temperature range and print the corresponding advice. Temperatures below 32°F print "Freezing! Bundle up!", between 32-50°F print "Cold, wear a jacket", 51-70°F print "Mild weather", and above 70°F print "Nice and warm!".

The slide is part of a larger presentation on converting flowcharts to Python code. It covers critical Python rules, boolean basics, comparison operators, common beginner errors, and different decision-making patterns like single choice, either/or choice, and multiple options using elif chains. The presentation also includes examples of grade calculators, login systems, and temperature advice, highlighting common patterns, pitfalls, and edge cases to consider when converting flowcharts to code.
:::

# Converting Flowcharts to Code: Temperature Advice **Solution**:

```python
temp = float(input("Temperature: "))

if temp < 32:
    print("Freezing! Bundle up!")
elif temp <= 50:
    print("Cold, wear a jacket")
elif temp <= 70:
    print("Mild weather")
else:
    print("Nice and warm!")
```

::: {.notes}
This slide presents the solution for converting the "Temperature Advice" flowchart into Python code. The code uses a series of if-elif statements to check the temperature range and print the appropriate advice based on the flowchart's logic.

The code demonstrates the use of comparison operators to create the temperature ranges and the elif chain to handle multiple options. It also showcases the importance of the order of conditions to ensure the correct advice is given for each temperature range.
:::

# What You've Mastered

- ✅ Basic if/elif/else syntax
- ✅ Comparison operators (==, !=, <, >, <=, >=)
- ✅ The critical = vs == distinction
- ✅ Proper indentation and structure
- ✅ Converting flowcharts to code

::: {.notes}
In this slide, we've summarised the key concepts and skills you've mastered so far in writing Python code for simple decision structures. You've grasped the basic if/elif/else syntax, comparison operators, the critical distinction between assignment (=) and equality testing (==), and the importance of proper indentation and structure in Python. Well done!

You've also learnt how to take a problem represented as a flowchart and translate that into working Python code. This is an essential skill as it allows you to take a visual representation of program logic and implement it in code. With practice, this process will become more natural and intuitive. Next, we'll look at some additional concepts to round out your understanding of Python conditionals.
:::

# Still to Learn

Next we will cover:

- Complex conditions with `and`, `or`, `not`
- Debugging decision logic with AI
- Input validation and error handling
- Testing edge cases systematically

::: {.notes}
Complex conditions involving `and`, `or`, and `not` operators, debugging decision logic with AI assistance, input validation, error handling, and systematically testing edge cases are advanced topics that build upon the foundations of decision making with Python. These skills enable you to create more sophisticated and robust programs that can handle a wide range of user inputs and exceptional situations.

Mastering these techniques will allow you to tackle more complex programming challenges and develop applications that provide a better user experience. By validating user input, handling errors gracefully, and thoroughly testing your code, you can ensure that your programs are reliable and function as intended, even in unexpected scenarios.
:::

# Quick Self-Check

Can you predict the output?

```python
x = 15

if x > 20:
    print("Big")
elif x > 10:
    print("Medium")
elif x > 5:
    print("Small")
else:
    print("Tiny")
```

**Answer**: "Medium" (x is 15, first true condition is x > 10)


::: {.notes}
From flowcharts to Python code, this slide covers the fundamentals of translating logic into functioning programs. Key concepts include the difference between assignment (x = 5) and comparison (x == 5), using if/elif/else statements to handle different temperature ranges, and the importance of proper indentation and structure.

The slide also highlights the mastery of comparison operators, the critical distinction between = and ==, and the process of converting flowcharts into code. Future topics will explore more advanced concepts such as complex conditions, debugging decision logic, input validation, error handling, and systematic testing of edge cases.

The quick self-check slide provides an opportunity for learners to reflect on their understanding of the key concepts covered throughout the presentation. This includes topics such as converting flowcharts to Python code, the three main decision-making patterns (single choice, either/or choice, and multiple options), and critical Python rules related to boolean logic, comparison operators, and common beginner errors.

The self-check also allows learners to assess their grasp of more advanced topics, such as building grade calculators using the elif chain, avoiding redundancy in code, handling edge cases, and converting complex flowcharts into functional Python code. By taking a moment to evaluate their comprehension, learners can identify areas where they may need further practice or clarification before moving on to new material.
:::
