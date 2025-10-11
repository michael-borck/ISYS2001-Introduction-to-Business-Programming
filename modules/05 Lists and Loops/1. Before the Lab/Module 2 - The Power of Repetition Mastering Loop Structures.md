---
title: "The Power of Repetition: Mastering Loop Structures"
subtitle: "Understanding For and While Loops in Programming"
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

# Introduction to Loop Structures

* Programming often requires repeating actions
* Loops are control structures that automate repetition
* Two primary loop types: For loops and While loops
* Essential for efficient, scalable code
* Foundational concept for all programming languages

::: {.notes}
Welcome to our presentation on loop structures! When writing programs, we frequently encounter situations where we need to perform the same action multiple times. Rather than writing the same code over and over, programming languages provide loop structures to handle repetition efficiently. 

In this presentation, we'll focus on the two most common loop types: For loops and While loops. Understanding these structures is fundamental to programming as they appear in virtually every programming language and are used in countless applications, from simple counters to complex data processing algorithms. Mastering loops will significantly enhance your ability to write clean, efficient code.
:::

# The Problem: Why We Need Loops

* Manual repetition is tedious and error-prone
* Consider checking 1,000 numbers for even/odd status
* Without loops:
  * Write the same code 1,000 times
  * Hard to maintain and update
* With loops:
  * Write the logic once
  * Let the computer handle repetition

::: {.notes}
Imagine you need to check whether each number in a list of 1,000 numbers is even or odd. Without loops, you would need to write the same checking code 1,000 times—a tedious and error-prone approach. If you later discovered a bug in your logic, you'd need to fix it in all 1,000 places!

Loops solve this problem elegantly by allowing you to write the logic once and then instruct the computer to repeat it as many times as needed. This not only makes your code more concise and readable but also much easier to maintain. When your requirements change, you only need to update the logic in one place, and the loop will apply that updated logic to all iterations.
:::

# For Loops: Concept and Structure

* Used when the number of iterations is known beforehand
* Components of a For loop:
  * Initialisation (starting value)
  * Condition (when to stop)
  * Update statement (how to change the counter)
* Executes a specific number of times
* Common uses: iterating over collections, counting

::: {.notes}
For loops are the perfect choice when you know exactly how many times you need to repeat an action. They follow a clear structure with three key components: initialisation (where we set our starting point), a condition (that determines when to stop), and an update statement (that changes our counter with each iteration).

Think of a For loop like a recipe that says "stir the mixture 20 times." You know exactly how many stirs to perform before you start. For loops are commonly used to process elements in a collection (like items in a list), perform actions a set number of times, or count up or down between specific values. Their predictable nature makes them easy to understand and reason about.
:::

# For Loop: Python Example

* Basic syntax in Python:

```python
for variable in sequence:
    # Code to repeat
```

* Example: Printing numbers 1 through 5

```python
for i in range(1, 6):
    print(i)
# Output: 1 2 3 4 5
```

* Example: Iterating through a list

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like " + fruit)
```

::: {.notes}
The Python For loop has a straightforward syntax that makes it particularly readable. The loop variable (often named 'i' for 'index', or something more descriptive like 'fruit') takes on each value in the specified sequence, one at a time, and the indented code block executes once for each value.

The `range()` function is frequently used with For loops to generate a sequence of numbers. In our first example, `range(1, 6)` creates a sequence from 1 up to (but not including) 6, so the loop prints numbers 1 through 5. In the second example, we iterate directly through a list of fruits, demonstrating how loops can work with different data types. This flexibility makes For loops incredibly versatile for all kinds of repetitive tasks.
:::

# While Loops: Concept and Structure

* Used when the number of iterations is unknown beforehand
* Continues as long as a specified condition is true
* Components:
  * Initialisation (before the loop)
  * Condition (when to continue)
  * Update statement (inside the loop)
* May execute zero or many times
* Requires careful condition design to avoid infinite loops

::: {.notes}
While loops are fundamentally different from For loops because they're designed for scenarios where you don't know in advance how many iterations you'll need. Instead of counting, a While loop continues executing as long as its specified condition remains true. This makes While loops particularly useful for situations that depend on user input, external data, or complex conditions.

The structure of a While loop requires careful attention. You typically initialise variables before the loop begins, check a condition at the start of each iteration, and include statements inside the loop that eventually change the condition to false. If you forget to update the condition, you might create an "infinite loop" that never ends—a common beginner mistake. While loops give you more flexibility but also require more responsibility to ensure they terminate properly.
:::

# While Loop: Python Example

* Basic syntax in Python:

```python
while condition:
    # Code to repeat
    # Update condition
```

* Example: Counting to 5

```python
count = 1
while count <= 5:
    print(count)
    count += 1
# Output: 1 2 3 4 5
```

* Example: User input validation

```python
password = ""
while password != "secret":
    password = input("Enter password: ")
print("Access granted")
```

::: {.notes}
In Python, While loops begin with the keyword "while" followed by a condition that evaluates to either True or False. As long as the condition is True, the indented code block continues to execute. Notice that in our counting example, we need to manually initialise the counter before the loop and increment it inside the loop—steps that For loops handle automatically.

The second example demonstrates a practical application of While loops: validating user input. The loop continues asking for a password until the user enters the correct one. This kind of interaction couldn't easily be handled with a For loop because we don't know how many attempts the user will need. While loops excel at these open-ended scenarios where the number of iterations depends on dynamic conditions.
:::

# Choosing the Right Loop

* For loops: Best when you know the number of iterations
  * Iterating through collections
  * Counting a specific number of times
  * Processing sequences

* While loops: Best for conditional repetition
  * User input validation
  * Waiting for a condition to be met
  * Unknown number of iterations

* Both can often solve the same problem in different ways

::: {.notes}
Choosing between For and While loops is an important skill that improves with practice. Generally, if you can answer the question "How many times will this loop run?" before the loop starts, a For loop is probably the better choice. For loops are typically more concise and less prone to errors since they handle the initialisation and incrementation automatically.

While loops shine in situations where the termination depends on a condition that can't be predicted in advance. They're perfect for scenarios like processing input until the user enters a specific value, or running a simulation until a certain state is reached. Remember that most problems can be solved with either type of loop, but choosing the appropriate one will make your code clearer and more maintainable.
:::

# Common Loop Patterns

* Loop control statements:
  * `break`: Exit the loop immediately
  * `continue`: Skip to the next iteration
  
* Nested loops: Loops within loops
  * Useful for working with multi-dimensional data
  
* Accumulators: Building results during iteration
  * Summing values, collecting results

* Loop and a half: Checking conditions mid-loop

::: {.notes}
Beyond the basic loop structures, several common patterns appear frequently in programming. The `break` statement allows you to exit a loop immediately when a certain condition is met, while `continue` lets you skip the rest of the current iteration and move to the next one. These control statements are powerful tools for making your loops more efficient.

Nested loops—placing one loop inside another—are essential for working with multi-dimensional data structures like matrices or tables. Accumulators are variables that collect or combine results during iteration, such as summing numbers or building a list of results. The "loop and a half" pattern addresses situations where you need to check conditions in the middle of processing each item. These patterns build on the basic loop structures to solve more complex problems elegantly.
:::

# Loop Pitfalls and Best Practices

* Common mistakes to avoid:
  * Infinite loops (forgetting to update condition)
  * Off-by-one errors (including or excluding endpoints)
  * Inefficient loop designs

* Best practices:
  * Keep loops simple and focused
  * Use meaningful variable names
  * Consider performance for large datasets
  * Test boundary conditions (first/last iterations)

::: {.notes}
Loops can be tricky, especially for beginners. Infinite loops occur when the termination condition is never met, causing your program to hang indefinitely. Off-by-one errors happen when you mistakenly include or exclude an element at the boundaries of your iteration range—for example, iterating from 0 to 9 when you meant 1 to 10. These bugs can be subtle and frustrating to track down.

Following best practices can help you avoid these pitfalls. Keep your loops focused on a single task, use variable names that clearly indicate their purpose (e.g., `student_index` rather than just `i`), and consider the performance implications when working with large datasets. Always test your loops with attention to the boundary conditions—what happens on the first and last iterations? Taking these precautions will help you write more reliable loop structures.
:::

# Summary and Further Practice

* Loops are essential programming constructs
* For loops: Use when the iteration count is known
* While loops: Use for condition-based repetition
* Practice is key to mastery
* Next steps:
  * Experiment with different loop types
  * Solve problems using loops
  * Learn about loop variants in different languages

::: {.notes}
We've covered the fundamental concepts of For and While loops, examining their structures, use cases, and some common patterns and pitfalls. Remember that For loops are best when you know the number of iterations in advance, while While loops excel when the repetition depends on a condition that may change dynamically.

To truly master loops, there's no substitute for practice. Try rewriting While loops as For loops and vice versa to understand their differences and similarities. Tackle programming challenges that involve repetition, such as processing lists, validating input, or implementing algorithms. As you progress, you'll also encounter variations of these basic loop structures in different programming languages, but the core concepts you've learned today will remain relevant regardless of the language you use.
:::