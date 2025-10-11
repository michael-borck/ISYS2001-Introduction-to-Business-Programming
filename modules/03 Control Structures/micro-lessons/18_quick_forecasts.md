---
title: "Quick Forecasts"
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
This lesson introduces list comprehensions as a concise and efficient way to create lists in Python, combining looping and conditional logic.

**Context**
After covering branching (if-elif-else) and repetition (for and while loops) in Python, this lesson shows how these concepts can be combined using list comprehensions. It leads into the next lessons on reusable weather logic and applying functions with loops.

**Concise way to create lists** List comprehensions provide a compact syntax for creating lists based on existing lists or other iterable objects. They allow you to generate new lists in a single line of code, making your code more concise and readable.

**Combines loop and conditional logic** List comprehensions integrate the functionality of loops and conditional statements into a single expression. You can iterate over elements, apply transformations, and filter items based on specific conditions, all within the list comprehension itself.

**Readable for simple operations** For straightforward list creation tasks, list comprehensions offer a clear and intuitive way to express the desired operation. They eliminate the need for explicit loop and conditional constructs, making the code more readable and maintainable.

**Powerful for data transformations** List comprehensions shine when it comes to performing data transformations on lists. You can easily apply functions, mathematical operations, or string manipulations to each element of a list, creating a new list with the transformed values.

**Example: weekly temperature categorization** To illustrate the usage of list comprehensions, the lesson presents an example of categorizing weekly temperatures. By applying a list comprehension to a list of temperature values, you can create a new list that categorizes each temperature as "hot", "warm", or "cold" based on specific thresholds.