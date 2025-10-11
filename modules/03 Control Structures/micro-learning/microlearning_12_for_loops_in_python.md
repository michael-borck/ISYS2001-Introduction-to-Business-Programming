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


**Learning Objectives**

- Understand the purpose and usage of for loops in Python for iterating over sequences and repeating code blocks.
- Utilize the range() function to control the number of loop iterations.
- Recognize situations where for loops are appropriate, such as processing items in a collection or repeating a task a known number of times.

**Introduction**

This lesson follows on from discussing the concept of repetition in programming. It precedes a lesson on while loops, another type of repetition structure in Python.

**Iterate over a sequence** For loops in Python allow you to iterate over a sequence of items, such as a list, tuple, or string. This means the loop will execute once for each item in the sequence, with a loop variable taking on the value of the current item in each iteration. This is useful when you need to process each item in a collection individually.

**Repeat a specific number times** For loops can also be used to repeat a block of code a specific number of times. This is achieved using the range() function, which generates a sequence of numbers. By specifying the range, you can control exactly how many times the loop will execute.

**Useful for known iterations** For loops are particularly useful when you know in advance how many times you need to repeat a block of code. This could be based on the length of a sequence you're iterating over, or a fixed number of repetitions required for a specific task.

**Concise and readable** One advantage of for loops is their concise and readable syntax. The structure of a for loop clearly shows what sequence is being iterated over and what variable is being used for each item. This makes for loops easy to understand and maintain.

**Example: weekly weather forecast** To illustrate the usage of for loops, consider generating a weekly weather forecast. You could use a for loop to iterate over a list of the seven days of the week, executing the code to fetch and display the weather data for each day. This is a clear and efficient way to process the data for a known number of iterations.

**Key Takeaways**

- For loops allow iteration over sequences like lists, tuples, and strings.
- The range() function generates a sequence of numbers to control loop iterations.
- For loops are useful when the number of required iterations is known in advance.
- The concise and readable syntax of for loops makes them easy to understand and maintain.
- For loops are efficient for processing data in scenarios with a known number of iterations.

**Quick Quiz**

1. What is the primary purpose of for loops in Python?
   Answer: To iterate over a sequence of items or repeat a block of code a specific number of times.

2. How can you control the number of times a for loop executes?
   Answer: By using the range() function to generate a sequence of numbers specifying the desired number of iterations.

3. When are for loops particularly useful in Python?
   Answer: When you know in advance how many times you need to repeat a block of code, such as when processing items in a collection or repeating a task a fixed number of times.

**Additional Resources**

- Python For Loops Tutorial: https://www.w3schools.com/python/python_for_loops.asp
- Python range() Function: https://www.programiz.com/python-programming/methods/built-in/range
- Python For Loops Examples and Explanations: https://realpython.com/python-for-loop/

*Created on: 2024-08-05*
