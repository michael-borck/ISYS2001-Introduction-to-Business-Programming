---
title: "Introduction to Decision Making"
subtitle: "Conditionals and Logical Operators"
author: "Michael Borck"
format: 
  pptx:
    reference-doc: ../../../_assets/template.pptx
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
# Overview  
In this module, we'll introduce the fundamentals of decision making in Python.  
You'll learn how to use if-else statements and logical operators to make your programmes respond to different conditions.

::: {.notes}
The overview slide introduces the topic of conditionals in programming. It sets the stage for the rest of the presentation, which will cover what conditionals are, how they work, logical operators, visualising decision flow, an example of a simple weather decision, and an activity where participants can write their own conditionals.

This slide serves as a roadmap for the presentation, giving the audience a clear idea of what to expect in the coming slides. It's important to highlight the key points that will be covered and to emphasise the practical nature of the presentation, which includes an example and a hands-on activity.
:::

# What Are Conditionals?  
- Conditionals allow your programme to make decisions based on data.  
- They let you execute different code blocks depending on whether a condition is True or False.  
- Keywords include `if`, `elif`, and `else`.

::: {.notes}
Conditionals are a fundamental concept in programming that allow your code to make decisions based on specific conditions. By evaluating whether a condition is True or False, the programme can execute different blocks of code accordingly. This enables your programme to respond dynamically to various situations and inputs.

The key components of conditionals are the `if`, `elif` (else if), and `else` keywords. The `if` statement checks the initial condition, and if it evaluates to True, the corresponding code block is executed. If the condition is False, the programme moves on to the next `elif` statement, if present, and evaluates its condition. This process continues until a True condition is found or the `else` block is reached, which is executed if none of the previous conditions were True.
:::

# How Conditionals Work  
- The `if` statement checks a condition.  
- If the condition is True, the indented block of code runs.  
- Otherwise, the programme can either move to an `elif` (else if) or `else` block.  
- Example:
  
  ```python
  temperature = 18
  if temperature < 20:
      print("It's chilly!")
  else:
      print("It's warm!")
  ```

::: {.notes}
The `if` statement in programming checks a condition, and if that condition evaluates to True, the indented block of code following the `if` statement will execute. This allows the programme to make decisions based on certain criteria being met.

If the condition is not met (evaluates to False), the programme can either move to an `elif` (else if) statement to check additional conditions, or to an `else` block which will run if none of the previous conditions were True. This branching logic enables different code paths to be taken depending on the state of the programme at runtime.
:::

# Logical Operators  
- Logical operators combine multiple conditions:  
  - **and**: Both conditions must be True.  
  - **or**: At least one condition must be True.  
  - **not**: Reverses the truth value of a condition.
- Example:
  
  ```python
  temperature = 22
  is_raining = False
  if temperature > 20 and not is_raining:
      print("Great day for a picnic!")
  ```

::: {.notes}
Logical operators are used to combine multiple conditions in programming. The "and" operator requires both conditions to be true for the overall expression to be true. The "or" operator only needs at least one condition to be true for the overall expression to be true. The "not" operator reverses the truth value of a condition, so if a condition is true, "not" will make it false, and vice versa.

For example, consider the expression "if temperature > 20 and raining == False". This will only be true when the temperature is greater than 20 and it is not raining. If either the temperature is 20 or below, or it is raining, the expression will be false. Logical operators allow for more complex decision-making in programs by combining simple conditions.
:::

# Visualising Decision Flow  
Imagine your code as a flowchart:  
- **Start**  
  ↓  
- Evaluate condition (e.g., temperature)  
  ↓  
- **Yes:** Execute if-block  
  **No:** Move to else-block  
  ↓  
- **End**  
This diagram helps you understand how your programme chooses a path.

::: {.notes}
This slide visualises the flow of a simple conditional statement. It begins with a "Start" point, then evaluates a condition such as checking the temperature. If the condition is true, the flow moves to executing the code block associated with the "Yes" branch before reaching the "End" point.

By showing the decision flow as a linear sequence of steps, this diagram helps to break down the logic of a conditional into distinct stages. The "Yes" and "No" branches clearly illustrate the different paths the code may take depending on the outcome of the condition evaluation.
:::

# Example: A Simple Weather Decision  
Consider this code snippet:
  
```python
temperature = int(input("Enter the current temperature: "))
if temperature < 15:
    print("It's quite cold today.")
elif temperature < 25:
    print("It's a pleasant day.")
else:
    print("It's hot today!")
```
- This programme makes a decision based on the temperature entered by the user.

::: {.notes}
This example demonstrates how a simple program can make decisions based on user input. Here, the user enters a temperature value, and the program checks if it is above or below a certain threshold (in this case, 20 degrees Celsius). Depending on the result of this comparison, the program will print out a different message - either "It's warm outside" or "It's cold outside".

This is a very basic example of how conditionals can be used to create programs that respond differently based on certain conditions. By using logical operators and multiple conditional statements, much more complex decision-making processes can be implemented. However, this simple weather program serves as a good starting point for understanding the fundamental concepts behind conditionals in programming.
:::

# Activity: Write Your Own Conditionals  
- Practice writing a simple programme that:  
  1. Prompts the user for a number.  
  2. Uses an if-else structure to decide if the number is high or low.
- Experiment with different conditions to see how the flow changes.

::: {.notes}
In this activity, participants will have the opportunity to apply their knowledge of conditionals by writing a simple program. They should experiment with various conditions to observe how the program's flow changes based on the conditions they define.

Encourage participants to be creative and think of real-world scenarios where conditionals can be used to make decisions. Remind them to use the logical operators they've learned and to visualise the decision flow as they write their program. Offer assistance if needed, and allocate sufficient time for participants to complete the activity.
:::

# Summary and Next Steps  
- We explored how conditionals work with `if`, `elif`, and `else`.  
- We learned to use logical operators to combine conditions.  
- Understanding these concepts is vital for building interactive and responsive programmes.  
- In the next module, we'll apply these decision-making tools to create a simple weather forecaster.

::: {.notes}
In this module, we have explored the fundamental concepts of conditionals in programming using the `if`, `elif`, and `else` statements. These statements allow our programmes to make decisions based on specified conditions, enabling them to respond differently depending on the input or state of variables. We also learned how to combine multiple conditions using logical operators such as `and`, `or`, and `not`, which gives us even more control over the flow of our code.

As we move forward, it is crucial to recognise that a solid grasp of conditionals and logical operators is essential for creating interactive and responsive programmes. These concepts form the foundation of decision-making in programming, allowing us to build software that can adapt to various situations and user inputs. In the upcoming module, we will apply the knowledge gained here to develop a simple weather forecaster, demonstrating how these decision-making tools can be used to solve real-world problems.
:::

