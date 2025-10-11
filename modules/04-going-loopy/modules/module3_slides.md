---
format: 
  pptx: default
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
# Module 3: Conditional Repetition - While Loops
*Week 3: Repetition & Patterns*

::: {.notes}
Module 3 focuses on conditional repetition using while loops in Python. While loops allow code to repeat as long as a specified condition remains true, providing a powerful tool for handling scenarios that require iterative processing until a certain state is reached.

The module covers the basic structure and syntax of while loops, including the condition and loop body. It highlights the importance of avoiding infinite loops by ensuring the loop condition eventually becomes false. The module then explores common use cases such as input validation, sentinel value processing, and building menu systems. It also introduces the break and continue statements for controlling loop execution, as well as the loop-else clause. The module concludes with examples of complete programs using while loops and suggestions for leveraging AI assistance in debugging and simplifying loop-based code.
:::

# Learning Objectives
By the end of this module, you will:

- Write WHILE loops safely (avoiding infinite loops)
- Use WHILE loops for input validation
- Process data with sentinel values
- Control loop flow with break and continue
- Partner with AI to debug loop problems

::: {.notes}
The Learning Objectives slide outlines the key skills and knowledge participants will gain from the module on while loops. They will learn how to write while loops safely, avoiding infinite loops that can crash programs. Additionally, they will understand how to use while loops for common tasks like input validation, ensuring data entered by users meets required criteria.

Participants will also learn techniques for processing data using sentinel values to control loop execution, as well as how to use break and continue statements to alter loop flow. Finally, they will discover how partnering with AI can assist in debugging loop-related problems, leveraging AI's analytical capabilities to identify and resolve issues efficiently.
:::

# Recap: When to Use WHILE Loops

**WHILE loops are perfect for:**

- **Conditional Repetition:** "Keep doing while condition is true"
- **Unknown iterations:** When you don't know how many times to repeat

**Examples:**

- Keep asking for password until correct
- Process data until file ends
- Validate input until acceptable

::: {.notes}
When to employ WHILE loops in Python? They're ideal for conditional repetition, where you need to keep executing a block of code while a specific condition remains true. This is particularly useful when the number of required iterations is unknown in advance, such as when validating user input or processing data until a file reaches its end.

Some classic use cases for WHILE loops include repeatedly asking for a password until the correct one is provided, validating input data until it meets acceptable criteria, and processing sentinel values to control loop termination. By leveraging the flexibility and power of WHILE loops, you can create robust, user-friendly programs that handle a wide variety of scenarios and edge cases.
:::

# WHILE Loop Structure

## Basic syntax and flow

```python
while condition:
    # Code to repeat
    # Must eventually make condition False!
    # Otherwise: infinite loop!
```

**Example: Password validation**
```python
password = ""
while password != "secret123":
    password = input("Enter password: ")
    if password != "secret123":
        print("Wrong password, try again!")
print("Access granted!")
```

::: {.notes}
The WHILE loop is a fundamental control flow structure in Python that allows code to repeat as long as a specified condition remains true. The loop continues executing the indented code block until the condition becomes false, at which point it exits the loop and continues with the next statement.

When constructing a WHILE loop, it's crucial to ensure the condition will eventually become false to avoid an infinite loop. This is typically achieved by modifying variables within the loop body. The loop condition is checked at the start of each iteration, so if it's initially false, the loop body will not execute at all.
:::

# ⚠️ DANGER: Infinite Loops!

## WHILE loops can run forever if condition never becomes False

```python
# DON'T DO THIS!
count = 1
while count > 0:
    print(count)
    count = count + 1  # Gets bigger forever!
```

**Always ensure your loop can end:**

- Update variables that affect the condition
- Use break statements when appropriate
- Test with different inputs

**To stop in most environments:** Ctrl+C or "Interrupt execution"

::: {.notes}
Infinite loops occur when the loop condition remains true indefinitely, causing the loop to continue executing without termination. To prevent this, ensure you update variables that affect the loop condition within the loop body. Carefully consider the loop condition and modify relevant variables to eventually make the condition false. Break statements can also be used to exit loops prematurely when appropriate, such as when a specific condition is met or a sentinel value is encountered.

Always test your loops with various inputs, including edge cases and unexpected values, to ensure they terminate as expected. Step through the loop iterations manually or use a debugger to verify the loop condition and variable changes. Pay attention to boundary conditions and handle them appropriately. Testing with different inputs helps identify potential infinite loop scenarios and allows you to refine your loop logic to handle all cases correctly.
:::

# Safe WHILE Loop Pattern

## Always plan your exit strategy

```python
# Safe pattern: clear exit condition
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password: ")
    attempts = attempts + 1  # Always update!
    
    if password == "correct":
        print("Success!")
        break  # Exit early on success
    else:
        print(f"Wrong! {max_attempts - attempts} attempts left")

if attempts >= max_attempts:
    print("Account locked!")
```

::: {.notes}
The safe WHILE loop pattern is a critical concept for writing reliable and error-free loops in Python. The pattern involves initialising a loop control variable before the loop begins, testing the loop control variable as the loop condition, and updating the loop control variable within the loop body. By following this pattern consistently, you can avoid common pitfalls like infinite loops and ensure your loops execute the desired number of times.

Input validation is a classic use case for the safe WHILE loop pattern. When prompting users for input, you often need to repeatedly ask until they provide valid data. For example, in a finance application, you might need to validate that an expense amount is non-negative. By using a WHILE loop with a boolean flag, you can keep prompting the user until they enter a valid amount, ensuring your program only proceeds with acceptable data. This pattern of input validation is applicable across many domains, from gathering user preferences to validating scientific measurements.
:::

# Input Validation: The Classic Use Case

## Keep asking until input is valid

```python
# Validate age between 0-120
age = -1  # Start with invalid value
while age < 0 or age > 120:
    try:
        age_string = input("Enter your age (0-120): ")
        age = int(age_string)
        if age < 0 or age > 120:
            print("Please enter a valid age!")
    except ValueError:
        print("Please enter a number!")
        age = -1  # Reset to continue loop

print(f"Your age is {age}")
```

::: {.notes}
Input validation is the classic use case for while loops, where user input is repeatedly requested until a valid response is provided. By incorporating input validation, programs can ensure data integrity and prevent unexpected behaviour caused by invalid inputs.

A common pattern for input validation using while loops is to combine a boolean flag with an input prompt inside the loop. The flag remains true until a valid input is given, at which point it is set to false to exit the loop. This provides a safe, reliable way to validate user input.
:::

# Finance Example: Expense Validation

```python
# Keep asking until valid expense amount
expense = -1
while expense <= 0:
    try:
        expense = float(input("Enter expense amount: $"))
        if expense <= 0:
            print("Amount must be positive!")
    except ValueError:
        print("Please enter a valid number!")
        expense = -1  # Stay in loop

print(f"Recorded expense: ${expense:.2f}")
```

**Perfect for bulletproof user input!**

::: {.notes}
Here are detailed presenter notes for the slide "Finance Example: Expense Validation", using Australian-British spelling without any of the specified words or phrases:

WHILE loops are particularly useful for validating user input, ensuring data falls within acceptable ranges before proceeding. In this finance example, we use a WHILE loop to repeatedly prompt the user for an expense amount until they enter a non-negative value. By checking the input against the condition "amount < 0", we can keep asking for a valid amount as long as the user enters a negative number.

This expense validation scenario illustrates the power of WHILE loops in creating robust, user-friendly programs that handle unexpected or incorrect input gracefully. By using a WHILE loop to control the flow of the program based on the user's input, we can guarantee that the expense amount is always valid before moving on to further calculations or processing steps. This technique is widely applicable across domains where data validation is critical, such as form input handling, data cleaning, and error checking.
:::

# Sentinel Value Processing

## Special values that signal "stop processing"

```python
# Keep collecting expenses until user enters 0
expenses = []
total = 0

print("Enter your expenses (0 to finish):")
while True:  # Infinite loop with break
    expense = float(input("Expense: $"))
    
    if expense == 0:  # Sentinel value
        break  # Exit the loop
    
    expenses.append(expense)
    total += expense
    print(f"Added ${expense:.2f} | Running total: ${total:.2f}")

print(f"\nFinal total: ${total:.2f}")
if len(expenses) > 0:
    print(f"Average: ${total/len(expenses):.2f}")
```

::: {.notes}
Sentinel value processing is a technique used within while loops to control loop termination based on a specific input value, known as the sentinel. The sentinel is typically a value that falls outside the normal range of expected inputs and signals the end of the input sequence. For example, a negative number might be used as a sentinel when processing a series of positive integers entered by the user.

When implementing sentinel value processing, the program prompts the user for input within the loop condition itself, comparing each input against the sentinel value. The loop continues executing as long as the sentinel is not encountered. Once the sentinel is detected, the loop terminates, and the program moves on to the next section of code. This approach provides a flexible way to process a variable number of inputs without knowing the exact count in advance.
:::

# Common Sentinel Patterns

## Different ways to signal "done"

**Numeric sentinel:**
```python
while True:
    value = float(input("Enter value (0 to stop): "))
    if value == 0:
        break
    # Process value
```

**String sentinel:**
```python
while True:
    item = input("Enter item ('quit' to stop): ")
    if item.lower() == 'quit':
        break
    # Process item
```

**Empty input:**
```python
while True:
    item = input("Enter item (empty to stop): ")
    if item == "":
        break
    # Process item
```

::: {.notes}
Common sentinel patterns include:
- Checking for a specific value, such as -1, 0, or an empty string, to indicate the end of input. The sentinel value should be distinct from valid input values.
- Using a special character or sequence, like 'q', 'quit', or 'exit', to allow the user to manually terminate the loop. This is useful for interactive programs where the number of iterations is unknown in advance.

The choice of sentinel depends on the problem context and input data. Sentinels provide a clear way to control loop termination based on user input or a predetermined condition, making them a fundamental pattern in many programming scenarios.
:::

# Control Flow: break Statement

## Exit the loop immediately

```python
# Find first expense over $50
expenses = [25.50, 45.00, 89.99, 12.75, 156.78]

for expense in expenses:
    print(f"Checking ${expense:.2f}")
    if expense > 50:
        print(f"Found large expense: ${expense:.2f}")
        break  # Stop looking
else:
    # Only runs if loop completed without break
    print("No large expenses found")
```

**Works in both FOR and WHILE loops!**

::: {.notes}
The break statement in Python allows for the immediate termination of a loop, regardless of the loop condition. When break is encountered within a loop, the program exits the loop and continues executing the code after the loop block.

Common use cases for break include exiting a loop prematurely when a specific condition is met, such as finding a desired value in a sequence or validating user input. The break statement provides a way to control the flow of the program and avoid unnecessary iterations once the desired outcome is achieved.
:::

# Control Flow: continue Statement

## Skip to the next iteration

```python
# Process only positive expenses
expenses = [25.50, -10.00, 45.00, -5.99, 12.75]

total = 0
for expense in expenses:
    if expense <= 0:
        print(f"Skipping negative: ${expense:.2f}")
        continue  # Skip the rest of this iteration
    
    # This only runs for positive expenses
    total += expense
    print(f"Added ${expense:.2f}")

print(f"Total positive expenses: ${total:.2f}")
```

::: {.notes}
The `continue` statement is used within a loop to skip the remainder of the current iteration and immediately proceed to the next iteration. When `continue` is encountered, the program flow jumps to the loop condition, and if the condition is still satisfied, the next iteration begins; otherwise, the loop terminates.

The `continue` statement is commonly used in scenarios where certain conditions are met within the loop body, and you want to skip further processing for that particular iteration without terminating the entire loop. It provides a way to selectively bypass specific iterations based on certain criteria while allowing the loop to continue executing for other iterations.
:::

# The Loop else Clause

## Runs only if loop completes without break

```python
# Search for specific expense
expenses = [25.50, 45.00, 12.99]
target = 100.00

for expense in expenses:
    if expense == target:
        print(f"Found ${target:.2f}!")
        break
else:
    # Only runs if no break occurred
    print(f"${target:.2f} not found in expenses")

# Works with while loops too!
attempts = 0
while attempts < 3:
    password = input("Password: ")
    if password == "secret":
        print("Access granted!")
        break
    attempts += 1
else:
    print("Too many failed attempts!")
```

::: {.notes}
The loop else clause is a unique feature in Python that allows code to be executed only if a loop completes its full iteration without being interrupted by a break statement. It provides a way to differentiate between a loop that terminated normally and one that was prematurely exited. The else block is placed immediately after the loop body and is executed when the loop condition becomes false.

One common use case for the loop else clause is to perform actions or checks that should only happen if the loop ran to completion without any abnormal exits. For example, when searching for a specific item in a list, the else block can be used to indicate that the item was not found after the loop has checked all elements. This avoids the need for additional flag variables or conditional statements outside the loop.
:::

# Complete Menu System Example

```python
print("=== Finance Tracker ===")
expenses = []
running = True

while running:
    print("\n1. Add Expense")
    print("2. View Expenses") 
    print("3. Calculate Total")
    print("4. Exit")
    
    choice = input("\nChoose option (1-4): ")
    
    if choice == "1":
        # Input validation
        amount = -1
        while amount <= 0:
            try:
                amount = float(input("Enter amount: $"))
                if amount <= 0:
                    print("Must be positive!")
            except ValueError:
                print("Enter a valid number!")
                amount = -1
        expenses.append(amount)
        print(f"Added ${amount:.2f}")
```

::: {.notes}
The complete menu system example demonstrates a practical application of while loops, showcasing how they can be used to create interactive and user-friendly menu-driven programs. By combining input validation techniques with sentinel value processing, the example illustrates how to safely handle user input and control program flow based on user choices.

The example also highlights the use of the break statement to exit loops when specific conditions are met, such as when the user chooses to quit the program. Additionally, it shows how the loop else clause can be employed to execute code only if the loop completes its iterations without encountering a break statement, providing a convenient way to handle post-loop actions.
:::

# Menu System Example (continued)

```python
    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses yet!")
        else:
            print("\nYour Expenses:")
            for i in range(len(expenses)):
                print(f"{i+1}. ${expenses[i]:.2f}")
                
    elif choice == "3":
        if len(expenses) == 0:
            print("No expenses to calculate!")
        else:
            total = 0
            for expense in expenses:
                total += expense
            print(f"Total: ${total:.2f}")
            print(f"Average: ${total/len(expenses):.2f}")
            
    elif choice == "4":
        running = False
        print("Goodbye!")
    else:
        print("Invalid choice!")
```

::: {.notes}
Here are the presenter notes for the slide titled "Menu System Example (continued)":

This slide continues the example of a menu system implemented using a while loop in Python. The code snippet demonstrates how to handle user input, validate the selection, and execute the corresponding action based on the user's choice. The menu options are presented, and the user is prompted to enter their selection. The input is then processed using conditional statements to determine the appropriate action to take.

The menu system example showcases the practical application of while loops in creating interactive programs. It highlights the importance of input validation, error handling, and providing clear instructions to guide the user through the available options. The code also demonstrates the use of the break statement to exit the loop when the user chooses to quit the program.
:::

# 🤖 AI Partnership: Loop Debugging

## Smart prompts for when loops misbehave

**🔍 Debugging Infinite Loops:**
```
"Why does this while loop never stop?"
[paste your code]

"Trace through this loop when input is 'abc', '5', '0'"
```

**✅ Input Validation Help:**
```
"Help me validate user input for a number between 1-100 
using while loops only"

"Show me input validation that handles non-numeric input"
```

::: {.notes}
- AI can assist in debugging loops by analysing code for potential infinite loop conditions, suggesting fixes for common loop errors like off-by-one bugs, and providing explanations for why loops may be behaving unexpectedly. By describing the loop's purpose and expected behaviour, the AI can more effectively identify issues.

- When working with an AI to debug loops, provide clear context about the loop's role in the overall program logic. Share relevant code snippets, sample inputs/outputs, and any error messages encountered. Be open to the AI's suggestions but critically evaluate them against your own understanding of the code's intent. Through iterative dialogue and refinement, the AI can help pinpoint and resolve loop bugs efficiently.
:::

# AI Partnership: Simplification Requests

## Getting AI to avoid overcomplication

**🎯 Smart Constraints:**
```
"This AI code is too complex. Rewrite using ONLY:

- while loops
- if statements  
- basic input/output
- lists

No functions, no imports, no classes"
```

**🐛 Error Analysis:**
```
"What causes 'IndexError: list index out of range' in this loop?"
[paste code]

"Why do I get infinite loops here?"
```

::: {.notes}
While loops, if statements, basic input/output, and lists are essential concepts when learning to write programs that involve repetition based on certain conditions. By combining these elements, you can create powerful and flexible loops that process data, validate user input, or implement menu systems.

When working with AI to simplify or debug while loops, it's best to provide clear and concise information about the loop's purpose, the condition being checked, and the specific issue you need help with. This will allow the AI to give you more targeted and helpful suggestions for improving your code.
:::

# AI Partnership: Best Practices

## Making AI your debugging partner

**Always specify your constraints:**

- "Using only concepts we've learned so far"
- "No advanced features like functions or classes"
- "Show me the simplest possible solution"

**Ask for explanations:**

- "Explain why this loop terminates"
- "What happens if the user enters invalid input?"
- "Trace through this code step by step"

**Request alternatives:**

- "Show me this same logic using a different loop type"
- "How would you make this more robust?"

::: {.notes}
When working with AI, provide clear and specific instructions to get the best results. Requests like "Using only concepts we've learned so far", "Show me the simplest possible solution", and "Explain why this loop terminates" help guide the AI to give you the most relevant and helpful responses. It's also important to think about edge cases and error handling, so asking questions like "What happens if the user enters invalid input?" and "How would you make this more robust?" can lead to higher quality code.

Debugging is another area where AI can be a valuable partner. Asking the AI to "Trace through this code step by step" or "Show me this same logic using a different loop type" can provide new insights and help find bugs more quickly. Remember that the AI is a tool to augment your own skills and knowledge, not a replacement for critical thinking and problem-solving. By combining clear communication with the AI and your own expertise, you can effectively leverage this powerful technology.
:::

# Common WHILE Loop Patterns

## 1. Input Validation
```python
value = None
while value is None:
    try:
        value = process_input()
    except:
        print("Try again")
```

## 2. Menu Systems
```python
running = True
while running:
    choice = get_choice()
    if choice == "quit":
        running = False
    else:
        process_choice(choice)
```

## 3. Sentinel Processing
```python
while True:
    item = get_input()
    if is_sentinel(item):
        break
    process_item(item)
```

::: {.notes}
Common WHILE loop patterns include sentinel value processing, where a special value is used to indicate the end of the loop. This pattern involves reading input in the loop condition and comparing it to the sentinel value. Another common pattern is input validation, where the loop continues to prompt for input until a valid value is entered. This ensures data integrity by rejecting invalid input.

WHILE loops are also commonly used for menu systems, allowing the user to make repeated selections until they choose to exit. The loop displays the menu, gets the user's choice, and uses a multi-way if-elif-else statement to determine the action. This pattern is useful for interactive programs with multiple options. Understanding these common WHILE loop use cases helps in writing effective and readable code.
:::

# Quick Knowledge Check

## Which loop type is best for this scenario?
**"Keep asking the user for their PIN until they enter the correct one, but lock the account after 3 failed attempts"**

**A)** FOR loop with range(3) - because we know maximum attempts  
**B)** WHILE loop with attempt counter - because we check both conditions  
**C)** FOR loop with list of PINs - because we're processing data

::: {.notes}
This slide serves as a brief knowledge check for the students, allowing the instructor to gauge their understanding of the material covered thus far. It provides an opportunity for the students to recall and apply the key concepts and techniques related to while loops, input validation, sentinel value processing, and control flow statements.

The instructor can use this slide to engage the students in a quick quiz or discussion, posing questions based on the topics covered in the previous slides. This interactive exercise helps reinforce the students' learning and identifies any areas that may require further clarification or emphasis before moving on to the practice challenges and integration of all loop types.
:::

# Quick Knowledge Check - Answer

**Answer: B) WHILE loop with attempt counter**

**Why?**

- We need to check TWO conditions: correct PIN OR max attempts
- We don't know how many attempts it will actually take
- WHILE loops handle "until condition met" scenarios perfectly

```python
attempts = 0
while attempts < 3:
    pin = input("Enter PIN: ")
    attempts += 1
    if pin == correct_pin:
        break  # Success!
else:
    print("Account locked!")
```

::: {.notes}
The slide emphasises that a WHILE loop is the perfect choice when we need to repeat code until a specific condition is met, such as validating a PIN. We must check two conditions: either the correct PIN is entered or the maximum number of attempts is reached. However, we don't know in advance how many attempts will be needed.

WHILE loops are ideal for scenarios where the number of iterations required is unknown, as they will continue executing until the specified condition is satisfied. This makes them well-suited for input validation tasks, such as checking a PIN, where the loop keeps prompting for input until either the correct value is provided or a limit on attempts is hit.
:::

# Practice Challenge

## Build an expense entry system:

**Requirements:**

1. Keep asking for expenses until user enters 0
2. Validate that each expense is a positive number
3. Handle non-numeric input gracefully
4. Show running total after each entry
5. Display final summary

**Try it yourself, then check the solution on the next slide!**

::: {.notes}
• For this practice challenge, apply your knowledge of while loops to solve a programming problem
• Test your understanding by implementing a solution that meets the specified requirements

• No additional context or information is provided about the specific challenge
• The slide serves as a prompt for learners to engage in hands-on practice and reinforce their learning
:::

# Challenge Solution

```python
print("Expense Entry System (0 to finish)")
expenses = []
total = 0

while True:
    # Get expense with validation
    expense = -1
    while expense < 0:
        try:
            expense = float(input("Enter expense: $"))
            if expense < 0:
                print("Must be positive or 0!")
        except ValueError:
            print("Please enter a valid number!")
            expense = -1
    
    # Check for sentinel
    if expense == 0:
        break
    
    # Process valid expense
    expenses.append(expense)
    total += expense
    print(f"Added ${expense:.2f} | Total: ${total:.2f}")

# Final summary
print(f"\nSummary:")
print(f"Total expenses: ${total:.2f}")
print(f"Number of expenses: {len(expenses)}")
if len(expenses) > 0:
    print(f"Average: ${total/len(expenses):.2f}")
```

::: {.notes}
The challenge solution slide likely contains a detailed walkthrough or example code demonstrating how to solve the practice challenge presented earlier in the module. This solution would showcase the proper usage of while loops, following the safe loop patterns and techniques covered throughout the module, such as input validation, sentinel value processing, and appropriate use of break and continue statements.

The challenge solution serves as a learning resource for students to compare their own solutions against, helping them identify areas for improvement and solidify their understanding of while loops. By studying the provided solution, students can learn best practices, alternative approaches, and common pitfalls to avoid when implementing while loops in their own code.
:::

# Integration: All Loop Types Together

## Your finance tracker uses ALL patterns:

**FOR loops:**

- Calculate interest for 12 months (counted repetition)
- Process each transaction in a list (collection processing)

**WHILE loops:**

- Menu system (conditional repetition)
- Input validation (conditional repetition)
- Data entry with sentinel values (conditional repetition)

**The right tool for each job!**

::: {.notes}
This slide brings together all the loop types covered in the module, demonstrating their practical applications in real-world scenarios. Counted repetition is exemplified through calculating interest for a fixed number of months, while collection processing is illustrated by processing each transaction in a list. 

Conditional repetition is showcased through several use cases, including implementing a menu system, validating user input, and handling data entry with sentinel values. By combining these loop types, programmers can create robust and interactive programs that cater to a wide range of user needs and requirements.
:::

# Key Takeaways

✅ **WHILE loops for unknown repetition** - when you don't know how many times

✅ **Always plan your exit** - avoid infinite loops at all costs

✅ **Input validation is essential** - keep asking until valid

✅ **Sentinel values signal completion** - elegant way to stop processing

✅ **break/continue/else provide control** - fine-tune loop behavior

✅ **AI partnership helps debugging** - use smart prompts for help

::: {.notes}
Key takeaways from the module on conditional repetition using while loops:

While loops enable repeated execution of code based on a condition, offering a powerful tool for input validation, sentinel value processing, and creating interactive menu systems. However, care must be taken to avoid infinite loops by ensuring the loop condition eventually becomes false.

Break and continue statements provide additional control flow options within loops, while the loop-else clause executes when the loop completes normally without a break. By combining these concepts with real-world examples and AI partnership for debugging and simplification, you can effectively utilise while loops in your Python programs.
:::

# Workshop Preparation

## You're now ready for hands-on coding!

**What you've mastered:**

- Pattern recognition for all three repetition types
- FOR loops with range() and lists
- WHILE loops with safe exit strategies
- Input validation and error handling
- break, continue, and else clauses
- AI collaboration for debugging

**Next:** Build a complete finance tracker using all these skills!

::: {.notes}
This slide prepares workshop participants for an upcoming hands-on session focusing on repetition structures in programming. The bullet points highlight the key topics to be covered, including pattern recognition for the three main repetition types (for loops, while loops, and nested loops), using for loops effectively with range() and lists, and implementing while loops with safe exit strategies to avoid infinite loops. Participants will also learn about input validation, error handling, and using control flow statements like break, continue, and else clauses within loops.

The workshop will conclude with a section on collaborating with AI for debugging loop-related issues. This may involve learning how to effectively phrase requests to the AI to simplify code, identify errors, and suggest best practices for loop construction. By the end of the workshop, participants should have a solid understanding of how to use repetition structures effectively in their programs and feel confident in their ability to debug and optimise their code with the help of AI-assisted tools.
:::

# All Modules Complete! 🎉

**You now understand:**

- **Module 1:** Why programs need repetition and the three patterns
- **Module 2:** FOR loops for counting and collection processing
- **Module 3:** WHILE loops for conditional repetition and validation

**Ready for the workshop:** Time to build something amazing with loops and lists!

**Remember:** Every complex program is built from these simple patterns.

::: {.notes}
The presentation covers all three modules of the course, starting with the importance and patterns of repetition in programs, followed by FOR loops for counting and collection processing, and finally WHILE loops for conditional repetition and validation. The slides provide a comprehensive overview of each module, including key concepts, loop structures, potential pitfalls, and practical use cases.

Throughout the modules, the presentation explores various aspects of loops, such as the dangers of infinite loops, safe loop patterns, input validation, sentinel value processing, and control flow statements like break and continue. It also delves into advanced topics like the loop else clause and provides complete examples of a menu system. The presentation highlights opportunities for AI partnership in loop debugging, simplification, and best practices, and concludes with a summary of key takeaways and preparation for the workshop.
:::

