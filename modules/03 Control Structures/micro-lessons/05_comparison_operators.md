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

**Aim**
This lesson aims to introduce the common Boolean operators used in Python programming to create logical expressions for conditional statements and loops.

**Context**
Boolean operators are a fundamental concept in programming, and understanding them is essential for implementing branching and repetition in Python. This lesson follows the introduction to Boolean expressions and precedes the lessons on logical operators and their practical applications in if-then statements, loops, and the weather condition checker example.

**AND** The AND operator returns True if both operands are True, and False otherwise. It is denoted by the keyword "and" in Python. For example, the expression "x > 0 and x < 10" will evaluate to True only if the value of x is between 0 and 10 (excluding 0 and 10).

**OR** The OR operator returns True if at least one of the operands is True, and False if both operands are False. It is denoted by the keyword "or" in Python. For example, the expression "x < 0 or x > 10" will evaluate to True if the value of x is less than 0 or greater than 10.

**NOT** The NOT operator returns the opposite Boolean value of its operand. It is denoted by the keyword "not" in Python. For example, if x is True, then "not x" will evaluate to False, and if x is False, then "not x" will evaluate to True.