---
title: "Breaking the Loop"
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
The aim of this lesson is to introduce the concept of breaking out of loops in Python using the `break` statement.

**Context**
This lesson follows on from the previous lessons covering for loops and while loops in Python. It introduces a new concept that allows for more control over loop execution. The following lessons will apply this concept in practical examples like a quick weather forecast program.

**Breaking the Loop** 
In Python, the `break` statement provides a way to exit a loop prematurely. When `break` is encountered inside a loop, the program immediately exits the loop, regardless of the loop condition. This is useful in situations where you want to stop the loop based on a certain condition without waiting for the loop to complete all its iterations.

To use `break`, simply include the `break` statement at the point where you want the loop to exit. Any code after the `break` statement inside the loop will not be executed. Execution will continue with the first statement after the loop.

The `break` statement works with both for loops and while loops in Python. It provides an important control mechanism to prevent unnecessary iterations and to handle special conditions that require loop termination.

In the context of the weather station simulator example, `break` could be used to exit the loop if the user enters a specific input to quit the program. This allows for a graceful exit from the loop and the program.