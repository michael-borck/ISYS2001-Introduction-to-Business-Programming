---
title: "While Loops in Python"
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

- Understand the basic structure and functionality of while loops in Python
- Learn how to control the flow of while loops using appropriate conditions
- Recognize the potential for infinite loops and how to avoid them

**Introduction**

Having discussed for loops in the previous lesson, this lesson expands on another type of repetition structure in Python: while loops. It is followed by lessons that demonstrate practical applications of while loops, such as in a weekly forecast program and a weather station simulator.

**Repeat while condition is True** While loops in Python continue to execute a block of code as long as a specified condition evaluates to True. The loop body is repeated until the condition becomes False. This allows for dynamic control flow based on changing conditions.

**Useful for unknown iterations** While loops are particularly handy when the number of required iterations is not known in advance. They can keep running until a certain condition is met, making them flexible for scenarios where the loop's end point is determined by external factors or computed values.

**Requires careful condition management** To prevent while loops from running indefinitely, it's crucial to manage the loop condition carefully. The condition should eventually become False, either through changes made within the loop body or by external events. Forgetting to update the condition can lead to infinite loops.

**Can create infinite loops** If the condition in a while loop always remains True, the loop will continue to execute indefinitely, resulting in an infinite loop. This can cause the program to hang or crash. It's important to include appropriate termination conditions and test the loop to ensure it ends as expected.

**Example: continuous weather monitoring** A practical example of using a while loop is in a weather monitoring system. The loop can continuously check the current weather conditions and perform actions based on the readings. It can keep running until a specific condition is met, such as a certain temperature threshold or a user-initiated termination signal.

**Key Takeaways**

- While loops execute a block of code repeatedly as long as a specified condition evaluates to True
- While loops are useful when the number of required iterations is not known in advance
- Careful management of the loop condition is crucial to prevent infinite loops
- While loops can be used in scenarios where continuous monitoring or dynamic control flow is needed

**Quick Quiz**

1. What is the main difference between a while loop and a for loop in Python?
   Answer: While loops execute based on a condition, whereas for loops iterate over a sequence.

2. True or False: A while loop will always execute at least once.
   Answer: False. If the condition is initially False, the loop body will not execute.

3. What can happen if the condition in a while loop always remains True?
   Answer: The loop will run indefinitely, resulting in an infinite loop.

**Additional Resources**

- Python While Loops: https://www.w3schools.com/python/python_while_loops.asp
- Python While Loop: https://www.programiz.com/python-programming/while-loop
- while Loop Examples: https://www.geeksforgeeks.org/python-while-loop/

*Created on: 2024-08-05*
