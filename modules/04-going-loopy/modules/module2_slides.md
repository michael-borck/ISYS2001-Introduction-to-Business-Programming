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
# Module 2: Counted Repetition - For Loops
*Week 3: Repetition & Patterns*

::: {.notes}
Module 2 introduces the concept of counted repetition using FOR loops in programming. It covers the fundamentals of FOR loops, including when to use them, understanding the range() function and its parameters, and common FOR loop patterns. The module also explores a finance example of calculating monthly interest to demonstrate the practical application of FOR loops.

The module then delves into lists as data collections, emphasising the critical concept of list indexing. It explains how to use FOR loops with lists and provides guidance on choosing the appropriate method. The module presents three common patterns: accumulation, list building, and filtering, along with a finance example of generating an expense report. It concludes with a practice challenge, discussion of common mistakes to avoid, a quick knowledge check, and integration with a finance tracker application.
:::

# Learning Objectives
By the end of this module, you will:

- Use `range()` for precise counting and repetition
- Create and manipulate lists to store collections of data
- Process lists with FOR loops effectively
- Apply common patterns: accumulation, building, and filtering

::: {.notes}
By the end of this module, you'll be able to use the `range()` function for precise counting and repetition in your Python programs. You'll also learn how to create and manipulate lists to store collections of data effectively.

We'll cover common patterns for processing lists with FOR loops, including accumulation (summing or aggregating values), building new lists, and filtering lists based on specific criteria. These techniques will allow you to tackle a wide range of programming tasks involving lists and loops.
:::

# Recap: When to Use FOR Loops

**FOR loops are perfect for:**
- **Counted Repetition:** "Do something exactly N times"

- **Collection Processing:** "Do something for each item"

**Today's focus:** Both patterns using Python's FOR loops

::: {.notes}
When deciding to use FOR loops in your code, there are two main scenarios to consider. The first is counted repetition, where you need to perform an action a specific number of times. FOR loops excel at executing a block of code exactly N times, making them perfect for tasks like generating sequences or repeating a process a set number of times.

The second scenario is collection processing, where you have a list or other iterable and need to do something with each item. FOR loops seamlessly iterate over the elements in a collection, allowing you to access and manipulate each item individually. This makes them ideal for tasks such as summing numbers, transforming data or filtering lists based on certain criteria.
:::

# Understanding range()

## Your counting companion for precise repetition

```python
# Count from 0 to 4 (5 numbers total)
for number in range(5):
    print(f"Count: {number}")  # Output: 0, 1, 2, 3, 4

# Count from 1 to 5  
for number in range(1, 6):
    print(f"Number: {number}")  # Output: 1, 2, 3, 4, 5

# Count by 2s from 0 to 8
for number in range(0, 10, 2):
    print(f"Even: {number}")  # Output: 0, 2, 4, 6, 8
```

::: {.notes}
range() is a built-in Python function that generates a sequence of numbers. It's commonly used in for loops to control the number of iterations. The basic syntax is range(start, stop, step), where start is the starting number (inclusive, defaults to 0), stop is the ending number (exclusive, required), and step is the increment between each number (defaults to 1).

Some examples of using range() include range(5) which generates numbers from 0 to 4, range(1, 6) which generates numbers from 1 to 5, and range(1, 10, 2) which generates odd numbers from 1 to 9. range() is efficient for generating large sequences as it doesn't create a list in memory but instead generates numbers on the fly. This makes it useful for controlling loop iterations without consuming extra memory.
:::

# range() Parameters

## Three ways to use range():

1. **`range(stop)`** → starts at 0, counts to stop-1
2. **`range(start, stop)`** → starts at start, counts to stop-1  
3. **`range(start, stop, step)`** → starts at start, counts by step

**Remember:** The stop value is NEVER included!

```python
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8
```

::: {.notes}
range() accepts up to three parameters: start, stop, and step. The start parameter specifies the starting value of the sequence (default is 0), stop specifies the value at which the sequence ends (exclusive), and step specifies the increment between each value in the sequence (default is 1). For example, range(1, 6, 2) generates the sequence [1, 3, 5].

If only one argument is provided to range(), it is treated as the stop value, and the sequence starts from 0. If two arguments are given, they represent the start and stop values respectively. The step parameter is optional and can be used to generate sequences with custom increments, such as even or odd numbers, or to generate sequences in reverse order using negative step values.
:::

# Common FOR Loop Pattern

## "Repeat N times" - the classic pattern

```python
# Ask user how many stars they want
how_many = int(input("How many stars? "))

# Print that many stars
for i in range(how_many):
    print("⭐", end=" ")  # end=" " keeps on same line
print()  # New line at the end
```

**Input:** `5`  
**Output:** `⭐ ⭐ ⭐ ⭐ ⭐`

::: {.notes}
Here are the presenter notes for the "Common FOR Loop Pattern" slide in two paragraphs, using Australian/British spelling:

The common FOR loop pattern involves iterating over a sequence of values, such as a range of numbers or a list, and performing a specific action for each value. This pattern is widely used in programming to repeat a block of code a specified number of times or to process each element in a collection.

When using the common FOR loop pattern, the loop variable takes on each value in the sequence one at a time, and the code inside the loop is executed for each iteration. This allows you to perform calculations, modify data, or carry out any desired operation on each value in the sequence. It's important to ensure that the loop condition is properly defined to avoid infinite loops and that the loop variable is used correctly within the loop body to achieve the intended result.
:::

# Finance Example: Monthly Interest

```python
# Calculate compound interest month by month
principal = 1000  # Starting amount
rate = 0.05       # 5% annual = 0.004167 monthly
monthly_rate = rate / 12

print("Month by month growth:")
for month in range(1, 13):  # 12 months
    principal = principal * (1 + monthly_rate)
    print(f"Month {month}: ${principal:.2f}")
```

*Perfect for time-based financial calculations!*

::: {.notes}
Here are the presenter notes for the "Finance Example: Monthly Interest" slide:

To illustrate how FOR loops can be applied in finance, let's look at calculating monthly interest. Suppose we have an initial investment amount and want to determine the value after earning interest each month for a year. We can use a FOR loop to iterate through the months, calculating and adding the interest to the running total.

The key steps are: 1) Initialize variables for the initial amount and monthly interest rate. 2) Use range(12) in the FOR loop to execute the code block 12 times, once for each month. 3) Inside the loop, calculate the monthly interest by multiplying the current amount by the monthly rate, then add it to the running total. 4) After the loop finishes, the final amount will reflect the value after a year of earning interest.
:::

# Lists: Your Data Collections

## Creating and using lists

```python
# Empty list
expenses = []

# List with initial values
monthly_expenses = [450.00, 32.50, 89.99, 12.75]

# Adding items
expenses.append(25.50)  # Add grocery expense
expenses.append(45.00)  # Add gas expense

print(expenses)  # [25.50, 45.00]
```

::: {.notes}
Lists are a fundamental data structure in Python that allow you to store and manage collections of related items. They provide a flexible and efficient way to organise your data, whether it's a sequence of numbers, strings, or even other objects. Lists are created using square brackets [], with individual elements separated by commas.

One of the key features of lists is their ability to be indexed, allowing you to access individual elements by their position within the list. Indexing starts at 0 for the first element and increases by 1 for each subsequent element. You can also use negative indexing to access elements from the end of the list, with -1 referring to the last element. Lists are mutable, meaning you can modify, add, or remove elements after the list has been created.
:::

# Critical: List Indexing

## Indices start at 0 (not 1!)

```python
expenses = [25.50, 45.00, 12.99]
#  Index:    0      1      2

print(expenses[0])   # First item: 25.50
print(expenses[1])   # Second item: 45.00
print(expenses[2])   # Third item: 12.99
print(expenses[3])   # ERROR! IndexError: list index out of range

# Useful shortcuts
print(expenses[-1])  # Last item: 12.99
print(len(expenses)) # Length: 3
```

::: {.notes}
List indexing is a fundamental concept in Python that allows you to access individual elements within a list. Each element in a list is assigned a unique index, starting from 0 for the first element and incrementing by 1 for each subsequent element. To access an element, you use square brackets [] and specify the index of the element you want to retrieve. For example, if you have a list called my_list, you can access the first element using my_list[0], the second element using my_list[1], and so on.

It's important to be aware of the bounds of the list when indexing. Attempting to access an index that is outside the range of valid indices for the list will result in an IndexError. For instance, if a list has 5 elements, the valid indices range from 0 to 4. Trying to access an index like my_list[5] or my_list[-6] will raise an error. Negative indices can also be used to access elements from the end of the list, with -1 referring to the last element, -2 referring to the second-to-last element, and so on.
:::

# FOR Loops with Lists

## Two ways to process lists:

**Method 1: Direct iteration** *(when you just need each item)*
```python
expenses = [25.50, 45.00, 12.99]

for expense in expenses:
    print(f"${expense:.2f}")
```

**Method 2: Index-based** *(when you need position/numbering)*
```python
for i in range(len(expenses)):
    print(f"{i+1}. ${expenses[i]:.2f}")
```

::: {.notes}
FOR loops are a powerful tool for working with lists in Python. They allow you to iterate over each element in a list, performing operations or calculations on each item. This makes FOR loops an essential concept to understand when processing and analysing list-based data.

When using FOR loops with lists, you can access individual elements using their index. This enables you to manipulate specific items, create new lists based on conditions, or accumulate values. Common patterns include accumulation (summing or counting elements), list building (creating new lists), and filtering (selecting elements that meet certain criteria). By mastering these patterns, you'll be able to efficiently process and transform list data in your Python programs.
:::

# Which Method to Choose?

## Direct iteration vs. Index-based

**Use Direct Iteration when:**

- You just need to process each item
- Position doesn't matter
- Simpler and more readable

**Use Index-based when:**

- You need to number items (1, 2, 3...)
- You need to modify the list
- You're working with multiple lists simultaneously

::: {.notes}
When deciding which method to use for processing items in a list, consider the specific requirements of your task. If you simply need to process each item individually and the position doesn't matter, a FOR loop is often the simpler and more readable choice. FOR loops are also useful when you need to number items or work with multiple lists simultaneously.

However, if you need to modify the list itself during processing, such as adding or removing elements, a WHILE loop may be more appropriate. WHILE loops provide greater flexibility and control over the list, allowing you to dynamically adjust the loop condition based on the current state of the list. Ultimately, the choice between a FOR loop and a WHILE loop depends on the specific needs of your program and the nature of the data you're working with.
:::

# Finance Example: Expense Report

```python
expenses = [25.50, 45.00, 12.99, 89.99, 33.25]

print("=== Expense Report ===")

# Simple listing
for expense in expenses:
    print(f"${expense:.2f}")

print("\n=== Numbered Report ===")

# Numbered listing  
for i in range(len(expenses)):
    print(f"{i+1}. ${expenses[i]:.2f}")
```

::: {.notes}
Here are the presenter notes for the "Finance Example: Expense Report" slide:

This slide demonstrates a practical application of FOR loops in a financial context. We'll analyse a list of expenses and calculate the total amount spent, showcasing how FOR loops can automate repetitive calculations.

By iterating through each expense in the list, we can add it to a running total variable. This accumulation pattern is commonly used with FOR loops to sum up values. The end result is the total expenses, calculated efficiently using a concise FOR loop.
:::

# Pattern 1: Accumulation

## Sum, count, or collect values as you loop

```python
expenses = [25.50, 45.00, 12.99, 89.99, 33.25]

# Calculate total
total = 0  # Start with 0
for expense in expenses:
    total = total + expense  # Add each expense

average = total / len(expenses)

print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")
```

**Key:** Initialise accumulator before the loop!

::: {.notes}
Pattern 1: Accumulation involves iterating through a list or sequence and accumulating a result, such as a sum or count, over each iteration. This pattern is useful for calculating totals, averages, or other aggregate values from a collection of data.

To implement the accumulation pattern, initialise an accumulator variable before the loop to store the running result. Inside the loop, update the accumulator by performing the desired operation (addition, multiplication, etc.) with the current element. After the loop completes, the final value of the accumulator represents the accumulated result over all iterations.
:::

# Pattern 2: List Building

## Create new lists from input or calculations

```python
# Build a list from user input
expenses = []  # Start empty

print("Enter 5 expenses:")
for i in range(5):
    expense = float(input(f"Expense {i+1}: $"))
    expenses.append(expense)

print(f"You entered: {expenses}")

# Build calculated list
tax_amounts = []
for expense in expenses:
    tax = expense * 0.08  # 8% tax
    tax_amounts.append(tax)
```

::: {.notes}
Pattern 2: List Building involves creating a new empty list before the loop begins, then appending elements to that list within the loop. This pattern is useful when you want to transform each element in the original list and store the results in a new list.

To implement List Building, initialise an empty list before the loop starts. Inside the loop, perform any necessary computations or transformations on each element, and append the result to the new list. After the loop finishes, the new list will contain all the transformed elements in the same order as the original list.
:::

# Pattern 3: Filtering

## Find items that meet specific criteria

```python
expenses = [25.50, 45.00, 12.99, 89.99, 33.25, 156.78]

# Count large expenses (over $50)
large_count = 0
for expense in expenses:
    if expense > 50:
        large_count = large_count + 1

print(f"Large expenses: {large_count}")

# Build list of small expenses
small_expenses = []
for expense in expenses:
    if expense < 20:
        small_expenses.append(expense)

print(f"Small expenses: {small_expenses}")
```

::: {.notes}
Filtering is a powerful technique used in programming to create new lists containing only elements that satisfy a certain condition. This pattern involves iterating through an existing list using a FOR loop and selectively adding elements to a new list based on a specified criteria or condition. Elements that meet the condition are included in the filtered list, while those that do not are omitted.

To implement the filtering pattern, start by creating an empty list to store the filtered elements. Then, use a FOR loop to iterate through each element in the original list. Within the loop, apply an IF statement to check if the current element satisfies the desired condition. If the condition is met, append the element to the filtered list. After the loop completes, the filtered list will contain only the elements that passed the condition, effectively filtering out unwanted elements from the original list.
:::

# Practice Challenge

## Modify this expense analyser:

```python
expenses = [450.00, 32.50, 89.99, 12.75, 156.30, 78.45]

# Basic analysis
total = 0
for expense in expenses:
    total = total + expense

average = total / len(expenses)
print(f"Total: ${total:.2f}")
print(f"Average: ${average:.2f}")

# TODO: Add these features:
# 1. Count expenses over $50
# 2. Find the highest expense  
# 3. List all expenses under $20
```

::: {.notes}
Here are the presenter notes for the "Practice Challenge" slide:

This slide provides an opportunity for learners to apply the concepts covered in Module 2 through a hands-on practice challenge. The challenge will likely involve writing code that incorporates FOR loops, lists, and the various patterns discussed, such as accumulation, list building, and filtering. Encourage learners to refer back to the examples and explanations provided throughout the module as they work on the challenge.

Depending on the complexity of the challenge, consider allotting sufficient time for learners to complete it independently or in small groups. Be available to answer questions and provide guidance as needed. Once the allotted time has elapsed, walk through the solution to the challenge, explaining each step and highlighting how the concepts from the module are applied in the code. This practice challenge serves as a valuable opportunity for learners to solidify their understanding of FOR loops and lists before moving on to the next module.
:::

# Challenge Solution

```python
expenses = [450.00, 32.50, 89.99, 12.75, 156.30, 78.45]

total = 0
large_count = 0
max_expense = 0
small_expenses = []

for expense in expenses:
    # Basic accumulation
    total += expense
    
    # Count large expenses
    if expense > 50:
        large_count += 1
    
    # Track maximum
    if expense > max_expense:
        max_expense = expense
    
    # Collect small expenses
    if expense < 20:
        small_expenses.append(expense)

print(f"Total: ${total:.2f}")
print(f"Large expenses: {large_count}")
print(f"Highest: ${max_expense:.2f}")
print(f"Small expenses: {small_expenses}")
```

::: {.notes}
Here are the presenter notes for the "Challenge Solution" slide in 2 paragraphs:

This slide presents the solution to the practice challenge exercise. The solution demonstrates how to apply the concepts and techniques covered in this module to solve a real-world problem. It showcases the effective use of FOR loops, lists, and the common patterns of accumulation, list building, and filtering.

By studying the challenge solution, learners can reinforce their understanding of the module's content and see how the different components work together in practice. Analysing the solution helps solidify the knowledge gained throughout the module and provides a concrete example of how to approach similar problems in the future.
:::

# Common Mistakes to Avoid

## 1. Off-by-one errors
```python
# WRONG: range(1, len(expenses)+1) for 0-based list
for i in range(1, len(expenses)+1):
    print(expenses[i])  # IndexError on last item!

# RIGHT: range(len(expenses)) for 0-based list
for i in range(len(expenses)):
    print(expenses[i])
```

## 2. Forgetting to initialise accumulators
```python
# WRONG: total not initialised
for expense in expenses:
    total = total + expense  # NameError!

# RIGHT: Initialise first
total = 0
for expense in expenses:
    total = total + expense
```

::: {.notes}
- Forgetting to initialise variables before using them in a loop
- Using the wrong comparison operator in loop conditions (e.g. using "=" instead of "==")
- Accidentally creating infinite loops by not updating the loop control variable properly
- Modifying a list while iterating over it, which can lead to unexpected behaviour
- Indexing out of bounds when accessing list elements inside a loop

When working with loops, it's crucial to double-check your initialisation, comparison operators, and control variable updates to prevent bugs. Be cautious when modifying lists during iteration, as this can cause skipped or repeated elements. Always ensure you're accessing valid indices to avoid IndexError exceptions. By being mindful of these pitfalls, you'll write more reliable and error-free loop code.
:::

# Quick Knowledge Check

## What will this code print?

```python
scores = [85, 90, 78]
for i in range(len(scores)):
    print(f"{i}: {scores[i]}")
```

**A)** `1: 85, 2: 90, 3: 78`  
**B)** `0: 85, 1: 90, 2: 78`  
**C)** `85: 0, 90: 1, 78: 2`

::: {.notes}
Here are the presenter notes for the "Quick Knowledge Check" slide:

This slide serves as a brief assessment to reinforce and test the audience's understanding of the key concepts covered in Module 2 on counted repetition using for loops. The slide should contain a few concise questions or problems that encapsulate the core ideas, such as the usage of range(), list indexing, and common for loop patterns like accumulation, list building, and filtering.

The questions should be designed to be quickly answerable, either through multiple choice or short fill-in-the-blank prompts, allowing the presenter to gauge the audience's comprehension and address any misconceptions or uncertainties before moving on to the next section of the presentation. The subsequent slide, "Quick Knowledge Check - Answer", should provide the correct answers and brief explanations to reinforce the learning objectives.
:::

# Quick Knowledge Check - Answer

**Answer: B) `0: 85, 1: 90, 2: 78`**

**Why?** 

- `range(len(scores))` gives us `range(3)` which is `0, 1, 2`
- Python lists use 0-based indexing
- So we get index: value pairs starting from 0

*Remember: Python always starts counting at 0!*

::: {.notes}
The slide "Quick Knowledge Check - Answer" explains the correct solution to the previous knowledge check question. It highlights that `range(len(scores))` evaluates to `range(3)`, which produces the values `0, 1, 2`. This is because Python lists use 0-based indexing, meaning the first element is at index 0, not 1.

Therefore, when using `range(len(scores))` in a FOR loop to iterate over a list, we get index-value pairs starting from index 0. This is a fundamental concept to understand when working with lists and FOR loops in Python, as it ensures we access the correct elements and avoid IndexError exceptions.
:::

# Finance Tracker Integration

## All patterns working together:

```python
print("=== Monthly Expense Tracker ===")
expenses = []

# Pattern 2: List Building
for i in range(5):
    expense = float(input(f"Enter expense {i+1}: $"))
    expenses.append(expense)

# Pattern 1: Accumulation  
total = 0
for expense in expenses:
    total += expense

# Pattern 3: Filtering
over_budget = []
for expense in expenses:
    if expense > 100:
        over_budget.append(expense)

print(f"Total spent: ${total:.2f}")
print(f"Over budget items: {len(over_budget)}")
```

::: {.notes}
Finance Tracker Integration:

Integrating a finance tracker into your personal finance management system can provide valuable insights and help you stay on top of your expenses, income, and overall financial health. By automating the tracking process, you can save time and reduce the risk of manual errors, ensuring your financial data is accurate and up to date.

When selecting a finance tracker, consider factors such as ease of use, compatibility with your existing systems, and the level of detail and customisation it offers. Look for features like transaction categorisation, budgeting tools, and reporting capabilities to maximise the benefits of the integration. With the right finance tracker in place, you'll be well-equipped to make informed financial decisions and achieve your personal finance goals.
:::

# Key Takeaways

✅ **`range()` is your counting tool** - master the three parameter forms

✅ **Lists store collections** - use 0-based indexing

✅ **Two ways to loop lists** - direct iteration vs. index-based

✅ **Three essential patterns** - accumulation, building, filtering

✅ **Always initialise accumulators** - start with appropriate values

::: {.notes}
Key Takeaways:

In this module, we explored the power of FOR loops in Python, which allow us to repeat a block of code a specified number of times. We learned about the range() function and its parameters, enabling us to control the start, stop and step of the loop. We also discovered how to use FOR loops with lists, a critical data structure in Python, and covered the basics of list indexing.

Throughout the module, we examined three common patterns: accumulation, list building and filtering. These patterns form the foundation for solving many programming problems efficiently. We applied these concepts to real-world examples, such as calculating monthly interest and processing expense reports. Finally, we highlighted some common mistakes to avoid when working with FOR loops and lists.
:::

# Coming Next: Module 3

**Module 3: Conditional Repetition - While Loops**

You'll learn:

- WHILE loop structure and safety
- Input validation patterns
- Sentinel value processing  
- Control flow with break/continue
- AI partnership strategies for debugging

*Ready to handle unknown repetition!*

::: {.notes}
Coming up in Module 3, we'll explore the powerful WHILE loop structure and learn strategies to ensure loop safety. We'll cover essential techniques for input validation to maintain program integrity. Additionally, we'll discover how to effectively handle sentinel values and control loop flow using the break and continue statements.

Throughout the module, we'll also discuss AI partnership strategies for debugging, empowering you to efficiently identify and resolve issues in your code. By mastering these concepts and techniques, you'll gain the skills to construct robust and reliable loops in your programs.
:::

# Module 2 Complete! 🎉

**You now know how to:**

- Count precisely with `range()`
- Store and process collections with lists
- Apply the three essential loop patterns
- Build real data processing programs

**Next:** WHILE loops for conditional repetition!

::: {.notes}
Module 2 covered essential concepts and techniques for precise counting and data processing using Python. Learners discovered how to use the `range()` function to generate sequences of numbers for precise counting in loops. They also learnt how to store and manipulate collections of data using lists, a fundamental data structure in Python. The module introduced the three critical loop patterns: accumulation, list building, and filtering, which form the foundation for processing data in many real-world scenarios.

Throughout the module, learners applied their newly acquired skills to solve practical problems, such as calculating monthly interest in a finance example and processing expense reports. They also gained awareness of common mistakes to avoid when working with loops and lists. The knowledge check and coding challenges provided opportunities to reinforce understanding and build confidence in applying these concepts independently. With the completion of Module 2, learners are now equipped with valuable tools and patterns for tackling a wide range of data processing tasks using Python.
:::

