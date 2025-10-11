---
title: "Elif in Python"
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

- Understand the purpose and syntax of the elif statement in Python
- Learn how to create complex branching structures using if, elif, and else statements
- Recognize when to use elif statements to handle multiple conditions

**Introduction**

The elif statement builds upon the concepts of boolean expressions, if-then statements, and else statements covered in previous lessons. It allows for more sophisticated decision-making in Python programs and sets the stage for the weather condition checker example in the following lesson.

**[Bullet Point 1]** The elif keyword in Python is short for "else if" and is used in conjunction with if and else statements to create more complex branching structures. It allows you to specify additional conditions to check if the preceding if statement's condition is false. You can include multiple elif statements to handle different cases or scenarios.

**[Bullet Point 2]** The syntax for using elif is similar to if statements. After an initial if statement, you can add one or more elif statements, each followed by a condition and a colon. The code block under each elif statement is executed if its condition evaluates to True. You can optionally include an else statement at the end to handle the case when none of the conditions are met.

**[Bullet Point 3]** When Python encounters an if-elif-else structure, it evaluates the conditions in order from top to bottom. If the if statement's condition is True, its code block is executed, and the rest of the elif and else blocks are skipped. If the if condition is False, Python moves on to the first elif condition. If that condition is True, its code block is executed, and the remaining elif and else blocks are skipped. This process continues until a condition is met or until the else block is reached.

**[Bullet Point 4]** Elif statements are useful when you need to check multiple conditions and execute different code blocks based on those conditions. They provide a way to handle various scenarios or cases in your program logic. By using elif, you can create more precise control flow and make your code more readable and manageable.

**Key Takeaways**

- The elif keyword is used in combination with if and else to create complex branching structures
- Elif allows you to specify additional conditions to check if the preceding if statement's condition is false
- Python evaluates the conditions in an if-elif-else structure from top to bottom, executing the first code block whose condition is True
- Elif statements make code more readable and manageable when handling multiple conditions and scenarios

**Quick Quiz**

1. What is the purpose of the elif statement in Python?
   Answer: To specify additional conditions to check if the preceding if statement's condition is false

2. How does Python evaluate the conditions in an if-elif-else structure?
   Answer: Python evaluates the conditions from top to bottom, executing the first code block whose condition is True

**Additional Resources**

- Python if, elif, else Statements: https://www.programiz.com/python-programming/if-elif-else
- Python if...elif...else Statement: https://www.tutorialspoint.com/python/python_if_else.htm
- Python if, else, and elif Statements: https://realpython.com/python-conditional-statements/

*Created on: 2024-08-05*
