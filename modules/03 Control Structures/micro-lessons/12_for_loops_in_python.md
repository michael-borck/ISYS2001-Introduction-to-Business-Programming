---
title: "For Loops in Python"
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
The aim of this lesson is to introduce for loops in Python and explain their purpose and usage.

**Context**
This lesson follows on from discussing the concept of repetition in programming. It precedes a lesson on while loops, another type of repetition structure in Python.

**Iterate over a sequence** For loops in Python allow you to iterate over a sequence of items, such as a list, tuple, or string. This means the loop will execute once for each item in the sequence, with a loop variable taking on the value of the current item in each iteration. This is useful when you need to process each item in a collection individually.

**Repeat a specific number times** For loops can also be used to repeat a block of code a specific number of times. This is achieved using the range() function, which generates a sequence of numbers. By specifying the range, you can control exactly how many times the loop will execute.

**Useful for known iterations** For loops are particularly useful when you know in advance how many times you need to repeat a block of code. This could be based on the length of a sequence you're iterating over, or a fixed number of repetitions required for a specific task.

**Concise and readable** One advantage of for loops is their concise and readable syntax. The structure of a for loop clearly shows what sequence is being iterated over and what variable is being used for each item. This makes for loops easy to understand and maintain.

**Example: weekly weather forecast** To illustrate the usage of for loops, consider generating a weekly weather forecast. You could use a for loop to iterate over a list of the seven days of the week, executing the code to fetch and display the weather data for each day. This is a clear and efficient way to process the data for a known number of iterations.