---
title: "Comparison operators"
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

- Understand the functionality and syntax of the AND, OR, and NOT Boolean operators in Python
- Apply Boolean operators to create logical expressions for conditional statements and loops
- Evaluate the outcome of logical expressions involving multiple Boolean operators

**Introduction**

Boolean operators are a fundamental concept in programming, and understanding them is essential for implementing branching and repetition in Python. This lesson follows the introduction to Boolean expressions and precedes the lessons on logical operators and their practical applications in if-then statements, loops, and the weather condition checker example.

**AND** The AND operator returns True if both operands are True, and False otherwise. It is denoted by the keyword "and" in Python. For example, the expression "x > 0 and x < 10" will evaluate to True only if the value of x is between 0 and 10 (excluding 0 and 10).

**OR** The OR operator returns True if at least one of the operands is True, and False if both operands are False. It is denoted by the keyword "or" in Python. For example, the expression "x < 0 or x > 10" will evaluate to True if the value of x is less than 0 or greater than 10.

**NOT** The NOT operator returns the opposite Boolean value of its operand. It is denoted by the keyword "not" in Python. For example, if x is True, then "not x" will evaluate to False, and if x is False, then "not x" will evaluate to True.

**Key Takeaways**

- The AND operator returns True only if both operands are True, and False otherwise
- The OR operator returns True if at least one of the operands is True, and False if both operands are False
- The NOT operator returns the opposite Boolean value of its operand
- Boolean operators are essential for implementing branching and repetition in Python programs
- Logical expressions involving multiple Boolean operators can be used to create complex conditions

**Quick Quiz**

1. What is the result of the expression 'True and False'?
   Answer: False

2. What is the result of the expression 'not (x < 5 or x > 10)' if x is 7?
   Answer: False

3. Which Boolean operator returns True if at least one of the operands is True?
   Answer: OR

**Additional Resources**

- Python Documentation - Boolean Operations: https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not
- Real Python - Python Boolean Operators: https://realpython.com/python-boolean-operators/
- W3Schools - Python Booleans: https://www.w3schools.com/python/python_booleans.asp

*Created on: 2024-08-05*
