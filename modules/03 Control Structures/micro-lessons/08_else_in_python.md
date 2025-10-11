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

**Aim**
This lesson aims to explain the purpose and usage of the else statement in Python conditional logic.

**Context**
After introducing the concept of branching and if statements, this lesson covers the else statement as the next component in decision structures. It is followed by elif for more complex conditionals and practical examples applying these concepts.

**Provides alternative action** The else statement provides an alternative action to be executed when the condition in the preceding if statement evaluates to False. It allows you to specify a block of code that should run if none of the previous conditions were met.

**Executes when if is False** The code block under the else statement will only execute if the condition in the if statement is False. This ensures that either the if block or the else block will run, but never both for the same condition.

**Completes the decision structure** By including an else statement, you create a complete decision structure that covers all possible cases. This is useful when you need to ensure that some action is always taken, regardless of whether the if condition is True or False.

**Ensures code for all cases** Using an else statement guarantees that you have provided code to handle all possible cases in your conditional logic. This helps prevent gaps in your decision-making process and makes your code more robust.

**Use for binary decisions** The if-else structure is most commonly used for binary decisions, where there are only two possible outcomes. If you need to check for multiple conditions, you can use elif statements in between the if and else to handle additional cases.