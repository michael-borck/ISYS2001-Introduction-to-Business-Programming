---
title: "Else in Python"
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

- Understand the purpose and functionality of the else statement in Python conditional logic.
- Apply the else statement to provide an alternative action when the if condition is False.
- Create complete decision structures using if-else statements for binary decisions.

**Introduction**

After introducing the concept of branching and if statements, this lesson covers the else statement as the next component in decision structures. It is followed by elif for more complex conditionals and practical examples applying these concepts.

**Provides alternative action** The else statement provides an alternative action to be executed when the condition in the preceding if statement evaluates to False. It allows you to specify a block of code that should run if none of the previous conditions were met.

**Executes when if is False** The code block under the else statement will only execute if the condition in the if statement is False. This ensures that either the if block or the else block will run, but never both for the same condition.

**Completes the decision structure** By including an else statement, you create a complete decision structure that covers all possible cases. This is useful when you need to ensure that some action is always taken, regardless of whether the if condition is True or False.

**Ensures code for all cases** Using an else statement guarantees that you have provided code to handle all possible cases in your conditional logic. This helps prevent gaps in your decision-making process and makes your code more robust.

**Use for binary decisions** The if-else structure is most commonly used for binary decisions, where there are only two possible outcomes. If you need to check for multiple conditions, you can use elif statements in between the if and else to handle additional cases.

**Key Takeaways**

- The else statement provides an alternative action to be executed when the if condition is False.
- The code block under the else statement only runs if the if condition evaluates to False.
- Using an else statement ensures that your decision structure covers all possible cases.
- The if-else structure is most suitable for binary decisions with only two possible outcomes.
- For multiple conditions, use elif statements between the if and else to handle additional cases.

**Quick Quiz**

1. What is the purpose of the else statement in Python?
   Answer: To provide an alternative action when the if condition evaluates to False.

2. When does the code block under the else statement execute?
   Answer: Only when the if condition is False.

3. True or False: The if-else structure is suitable for handling multiple conditions.
   Answer: False. For multiple conditions, you should use elif statements between the if and else.

**Additional Resources**

- Python if...else Statement: https://www.w3schools.com/python/python_conditions.asp
- Conditional Execution in Python: https://realpython.com/python-conditional-statements/
- Python Decision Making: if, else, and elif Statements: https://www.programiz.com/python-programming/if-elif-else

*Created on: 2024-08-05*
