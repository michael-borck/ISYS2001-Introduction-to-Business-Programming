---
title: "Boolean Expressions"
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


**Learning Objectives**

- Understand the concept of boolean expressions and their role in decision making within Python programs.
- Learn how to compare values using operators like ==, !=, <, and > to create boolean expressions.
- Gain knowledge of logical operators (and, or, not) and how they can be used to combine boolean expressions.

**Introduction**

Following an introduction to branching, this lesson delves into boolean expressions as the foundation for conditional statements. It prepares the audience for upcoming lessons that demonstrate the use of if-then, else, and elif statements in Python.

**Evaluate to True or False** Boolean expressions are fundamental constructs in programming that evaluate to either True or False. They form the basis for decision making in code, allowing programs to execute different blocks of code depending on whether a condition is met or not. Boolean expressions are essential for creating logical flow and controlling program behaviour based on specific criteria.

**Compare values (==, !=, <, >)** Boolean expressions often involve comparing values using operators such as equal to (==), not equal to (!=), less than (<), and greater than (>). These operators allow programmers to check if two values are equal, unequal, or if one value is greater or less than another. By comparing values, boolean expressions can determine the relationship between variables or constants and make decisions accordingly.

**Combine with and, or, not** Boolean expressions can be combined using logical operators like and, or, and not. The 'and' operator returns True if both expressions are True, while the 'or' operator returns True if at least one expression is True. The 'not' operator negates a boolean expression, returning the opposite value. These operators enable the creation of more complex conditions by combining multiple boolean expressions.

**Essential for decision making** Boolean expressions are crucial for decision making in programming. They allow programs to evaluate conditions and execute different code blocks based on the results. Decision making is a fundamental aspect of programming, enabling programs to respond to different scenarios, handle user input, and control the flow of execution. Without boolean expressions, programs would be limited to linear execution and lack the ability to adapt to varying conditions.

**Examples: is_raining, temp > 30** The lesson provides two examples of boolean expressions: 'is_raining' and 'temp > 30'. 'is_raining' is a boolean variable that could represent whether it is currently raining or not. 'temp > 30' is a boolean expression that compares the value of the 'temp' variable to the constant value 30, evaluating to True if the temperature is greater than 30 and False otherwise. These examples demonstrate how boolean expressions can represent real-world conditions and make decisions based on them.

**Key Takeaways**

- Boolean expressions evaluate to either True or False and form the basis for decision making in code.
- Comparison operators (==, !=, <, >) allow programmers to check the relationship between values.
- Logical operators (and, or, not) enable the creation of more complex conditions by combining boolean expressions.
- Boolean expressions are essential for controlling program flow and executing different code blocks based on specific criteria.

**Quick Quiz**

1. What are the two possible values that a boolean expression can evaluate to?
   Answer: True or False

2. Which logical operator returns True if both expressions are True?
   Answer: and

3. Given the expression: x > 10 and x < 20, what can you conclude about the value of x when the expression evaluates to True?
   Answer: x is greater than 10 and less than 20

**Additional Resources**

- Python Boolean Expressions: https://realpython.com/python-boolean/
- Logical Operators in Python: https://www.w3schools.com/python/python_operators.asp
- Python Decision Making: https://www.geeksforgeeks.org/decision-making-in-python/

*Created on: 2024-08-05*
