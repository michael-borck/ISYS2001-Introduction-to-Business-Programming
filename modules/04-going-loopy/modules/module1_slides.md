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
# Module 1: Why Programs Need to Repeat
*Week 4: Repetition & Patterns*

::: {.notes}
Module 1 introduces the fundamental concept of why programs need repetition. It explores the AI playlist problem, which illustrates the core truth that programs must be able to handle large amounts of data and perform tasks repeatedly to be useful and efficient. The module emphasises the importance of repetition in programming and how it enables programs to scale and tackle real-world problems effectively.

The module then presents the three fundamental patterns of repetition: counted repetition, conditional repetition, and collection processing. These patterns form the foundation for understanding how repetition is implemented in programming. The module includes practice exercises for pattern recognition and connects the concepts to real-world examples, such as a finance tracker application. The key takeaways reinforce the significance of repetition in programming and its role in enabling programs to handle large-scale tasks efficiently.
:::

# Learning Objectives
By the end of this module, you will:

- Recognise when programs need repetition
- Identify the three fundamental patterns of repetition
- Choose the right pattern for different scenarios
- Connect repetition to real-world applications

::: {.notes}
Learning objectives are the key outcomes participants should achieve by the end of this module. Recognise when programs require repetition to avoid code duplication and increase efficiency. Identify the three core repetition patterns: counted repetition for a known number of iterations, conditional repetition while a condition is met, and collection processing to iterate over data sets.

Choose the appropriate repetition pattern for different programming scenarios, considering factors like iteration count and termination conditions. Connect these patterns to real-world applications, such as looping through user input, processing data from files or databases, and implementing algorithms that require repetitive steps, to demonstrate the practical relevance of repetition in programming.
:::

# The AI Playlist Problem
What happens when we ask AI for a "music playlist manager"?

**AI might give us:**

```python
import random
import json
from datetime import datetime

class Song:
    def __init__(self, title, artist, duration, genre, year):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.play_count = 0
        self.last_played = None
        
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []
        self.shuffle_mode = False
        self.repeat_mode = 'none'
    # ... and much more!
```

::: {.notes}
The AI Playlist Problem is a classic example that demonstrates the need for repetition in programming. Imagine you have a large playlist of songs and want to count the number of songs by a specific artist. To solve this problem efficiently, you would need to process each song in the playlist one by one, keeping a running count of songs by the desired artist. This repetitive checking and counting process is a fundamental pattern in programming.

The AI Playlist Problem highlights the core truth that to solve many real-world problems, programs need to repeat actions. Whether it's processing a collection of items, performing a task a specific number of times, or repeating an action until a condition is met, repetition is a key concept in programming. By introducing this problem early, learners can grasp the importance of repetition and be better prepared to recognise and apply the three fundamental repetition patterns covered in the module.
:::

# The Core Truth

**A playlist really just needs to:**

1. 📀 Store multiple songs *(that's why we need lists!)*
2. 🔄 Play each song in order *(that's why we need loops!)*
3. ⏯️ Maybe let you skip or repeat *(basic control)*

**That's it!** Let's learn to build this simply.

::: {.notes}
The core truth about programming is that repetition is fundamental. All programs, regardless of their purpose or complexity, rely on repeating instructions to accomplish tasks efficiently and effectively.

By understanding and leveraging the three core patterns of repetition - counted repetition, conditional repetition, and collection processing - programmers can create powerful, flexible, and scalable solutions to a wide range of problems. Mastering these patterns is essential for writing code that is both concise and robust.
:::

# Why Programs Need Repetition

## Repetition is everywhere in computing:

**ATM Machine:**
```
REPEAT while PIN incorrect:
    Ask for PIN
    Check if valid
    IF incorrect: increment attempts
    IF attempts >= 3: keep card
```

**Music Player:**
```
FOR each song in playlist:
    Play current song
    Wait for it to finish
    Move to next song
```

::: {.notes}
Programs require repetition to efficiently handle tasks that involve performing the same or similar operations multiple times. Without repetition, code would become unnecessarily long, complex, and difficult to maintain as programmers would need to write out each individual step explicitly. Repetition allows us to express these repeated operations concisely and clearly.

There are three fundamental patterns of repetition in programming: counted repetition, where a block of code is repeated a specific number of times; conditional repetition, where code is repeated until a certain condition is met; and collection processing, where a set of operations is performed on each item in a collection of data. Recognising and applying these patterns is a key skill for writing effective and efficient code.
:::

# The Three Fundamental Patterns

All programming repetition falls into three patterns:

1. **🔢 Counted Repetition** - "Do something exactly N times"
2. **❓ Conditional Repetition** - "Keep doing while condition is true"  
3. **📋 Collection Processing** - "Do something for each item"

*Every loop you'll ever write fits one of these patterns!*

::: {.notes}
The three fundamental patterns of repetition in programming are counted repetition, conditional repetition, and collection processing. Counted repetition involves executing a block of code a fixed number of times, conditional repetition repeats code while a condition remains true, and collection processing iterates over the elements in a collection data structure.

Recognising these patterns is a critical skill for programmers. Being able to identify opportunities to use repetition and select the appropriate pattern simplifies code, reduces errors, and enables programs to scale gracefully to handle larger datasets. Repetition is a core programming concept that allows automation of repetitive tasks.
:::

# Pattern 1: Counted Repetition
## "Do something exactly N times"

**Real examples:**

- Print 10 labels
- Deal 5 cards to each player
- Show 20 search results
- Calculate 12 months of interest

**Programming tool:** FOR loops with `range()`

```python
# Print 5 stars
for i in range(5):
    print("⭐", end=" ")
```

::: {.notes}
Counted repetition is a fundamental programming pattern where a block of code is repeated a specific number of times. The examples on the slide illustrate practical applications of this pattern, such as printing a set number of labels, dealing a fixed number of cards to each player in a game, displaying a predetermined number of search results, or calculating interest for a given number of months.

By using counted repetition, programmers can efficiently handle tasks that require executing a block of code a known number of times. This pattern helps avoid redundant code and makes programs more concise and maintainable. Counted repetition is often implemented using loops, such as for loops in many programming languages, which allow developers to specify the number of iterations required to complete the task at hand.
:::

# Pattern 2: Conditional Repetition
## "Keep doing while condition is true"

**Real examples:**

- Keep asking for password until correct
- Keep playing game until lives = 0
- Process transactions until file ends
- Validate input until acceptable

**Programming tool:** WHILE loops

```python
# Keep asking until valid
password = ""
while password != "secret123":
    password = input("Enter password: ")
```

::: {.notes}
The slide titled "Pattern 2: Conditional Repetition" focuses on programs that repeatedly execute a block of code until a specific condition is met. The bullet points provide examples of this pattern, such as asking for a password until the correct one is entered, playing a game until the player's lives reach zero, processing transactions until the end of a file is reached, and validating input until it is acceptable.

Conditional repetition is a fundamental pattern in programming that allows programs to handle scenarios where the number of iterations required is unknown beforehand. By repeatedly executing a block of code until a condition is satisfied, programs can adapt to different inputs and situations dynamically. This pattern is essential for creating interactive and responsive programs that can handle user input, process data files, and implement game logic effectively.
:::

# Pattern 3: Collection Processing
## "Do something for each item"

**Real examples:**

- Send email to each subscriber
- Calculate grade for each student
- Display each photo in album
- Process each bank transaction

**Programming tool:** FOR loops with lists

```python
# Process each expense
for expense in expense_list:
    print(f"${expense:.2f}")
```

::: {.notes}
The slide titled "Pattern 3: Collection Processing" presents examples of processing each item in a collection, such as sending an email to each subscriber, calculating a grade for each student, displaying each photo in an album, and processing each bank transaction. This pattern involves iterating through a collection of items and performing a specific action or computation on each individual item.

Collection processing is a fundamental pattern in programming that enables working with sets of data efficiently and systematically. By applying an operation to each element in a collection, developers can automate repetitive tasks and handle large amounts of data with ease. This pattern is essential for various scenarios, from managing user interactions to analysing data sets and generating reports.
:::

# Pattern Recognition Practice

**Scenario:** You need to validate a user's PIN entry, giving them up to 3 attempts before locking the account.

**Which pattern fits?**

- A) Counted Repetition (FOR) - because we know exactly 3 attempts
- B) Conditional Repetition (WHILE) - because we keep asking until correct OR max attempts
- C) Collection Processing (FOR with list) - because we're processing PIN digits

*Think about it...*

::: {.notes}
The slide titled "Pattern Recognition Practice" presents three options for identifying the fundamental pattern in a given scenario. Option A suggests counted repetition using a FOR loop, as the number of attempts is known to be exactly three. Option B proposes conditional repetition with a WHILE loop, since the program keeps asking for input until the correct answer is provided or the maximum number of attempts is reached. Option C indicates collection processing using a FOR loop with a list, as the program processes the individual digits of the PIN.

This slide forms part of a larger presentation on the importance of repetition in programming. The presentation covers topics such as the three fundamental patterns of repetition (counted repetition, conditional repetition, and collection processing), real-world examples of these patterns, and how collections enable scalability in programming. The slide on pattern recognition practice aims to reinforce the learner's understanding of these concepts by presenting a practical scenario and asking them to identify the most appropriate repetition pattern to use in that context.
:::

# Pattern Recognition Practice - Answer

**Answer: B) Conditional Repetition (WHILE)**

**Why?** We need to check TWO conditions:

- Keep going until PIN is correct, OR
- Stop when we reach maximum attempts

We don't know how many attempts it will actually take!

```python
attempts = 0
while attempts < 3:
    pin = input("Enter PIN: ")
    if pin == correct_pin:
        break  # Success!
    attempts += 1
```

::: {.notes}
Here are the presenter notes for the "Pattern Recognition Practice - Answer" slide:

The first bullet point indicates that we should keep attempting to enter the PIN until it is correct. This represents the conditional repetition pattern, where we repeat an action until a specific condition is met. In this case, the condition is entering the correct PIN.

The second bullet point suggests that we should stop trying to enter the PIN if we reach the maximum number of allowed attempts. This is an additional condition that prevents an infinite loop if the correct PIN is never entered. It demonstrates how multiple conditions can be combined to control the repetition effectively.
:::

# Why Collections Enable Scale

**Without collections (lists):**
```python
expense1 = 25.50  # Groceries
expense2 = 45.00  # Gas  
expense3 = 12.99  # Coffee
expense4 = 89.99  # Utilities
# What if you have 100 expenses? 1000?
```

**With collections:**
```python
expenses = [25.50, 45.00, 12.99, 89.99]  # Can grow to any size!
# Process them all with a single loop
```

Collections + Loops = Processing any amount of data!

::: {.notes}
Collections enable programs to efficiently process large amounts of data without the need for repetitive code. By storing multiple values in a single variable, collections make it possible to write concise, scalable code that can handle datasets of any size with ease.

Whether working with a small set of values or processing millions of data points, collections provide a flexible and powerful tool for managing data at scale. From simple arrays and lists to more complex data structures like dictionaries and sets, collections are a fundamental building block for creating efficient, maintainable, and scalable software solutions.
:::

# Finance Tracker Connection

**Your finance tracker will need all three patterns:**

- **Counted:** Calculate interest for 12 months
- **Conditional:** Keep asking for valid expense amounts
- **Collection:** Process all transactions in a list

The same patterns work everywhere!

::: {.notes}
The Finance Tracker Connection slide demonstrates how the three fundamental patterns of repetition can be applied to a real-world problem. The first bullet point, "Counted: Calculate interest for 12 months", shows an example of counted repetition where a specific number of iterations is known in advance. The second bullet point, "Conditional: Keep asking for valid expense amounts", illustrates conditional repetition, which continues until a certain condition is met. Finally, the third bullet point, "Collection: Process all transactions in a list", exemplifies collection processing, where each item in a collection is processed one at a time.

By presenting these concrete examples, the slide helps learners connect the abstract concepts of repetition patterns to a practical, relatable scenario. This connection reinforces the importance and applicability of these patterns in solving real programming problems. The Finance Tracker example serves as a bridge between theory and practice, making the learning more meaningful and memorable for the audience.
:::

# Real-World Pattern Examples

## ATM System
```
WHILE user not authenticated AND attempts < 3:
    Request PIN
    Validate PIN
    Update attempt count
```

## Game Loop
```
WHILE player has lives:
    Display game world
    Get player input
    Update game state
    Check win/lose conditions
```

::: {.notes}
Real-world examples of the three fundamental patterns of repetition can be found in various domains, from finance and healthcare to education and entertainment. Counted repetition is exemplified by a fixed number of iterations, such as a workout routine with a set number of repetitions for each exercise. Conditional repetition is illustrated by processes that continue until a specific condition is met, like a thermostat controlling a heating system until the desired temperature is reached. Collection processing is demonstrated by tasks that involve iterating over a collection of items, such as a teacher grading a stack of student papers or a librarian cataloguing a shelf of books.

These real-world examples showcase the ubiquity and importance of repetition patterns in our daily lives. By recognising these patterns, we can better understand and analyse the processes around us, as well as design more efficient and effective solutions to problems. Whether it's automating repetitive tasks, optimising resource allocation, or streamlining data processing, the application of these fundamental patterns can lead to significant improvements in various fields. As we continue to explore the role of repetition in programming, it's essential to keep these real-world examples in mind and appreciate the practical implications of mastering these concepts.
:::

# Quick Check: Pattern Matching

**Match each scenario to its pattern:**

1. Calculate tax for each item in shopping cart
2. Roll dice until you get a 6
3. Display 10 most recent transactions

**Patterns:**

- A) Counted Repetition
- B) Conditional Repetition  
- C) Collection Processing

::: {.notes}
This slide, titled "Quick Check: Pattern Matching", presents three options labelled A, B, and C, which correspond to the three fundamental patterns of repetition discussed in the earlier slides. Option A refers to Counted Repetition, where a program repeats a specific number of times. Option B represents Conditional Repetition, in which a program repeats until a certain condition is met. Finally, Option C denotes Collection Processing, where a program iterates over a collection of items.

The purpose of this slide is to provide a quick assessment of the audience's understanding of the three repetition patterns covered in the presentation. By presenting these options, the presenter can gauge whether the participants have grasped the key concepts and can correctly identify each pattern. This quick check serves as a valuable opportunity for the presenter to reinforce the learning objectives and ensure that the audience is following along effectively.
:::

# Quick Check: Answers

1. Calculate tax for each item in shopping cart → **C) Collection Processing**
2. Roll dice until you get a 6 → **B) Conditional Repetition**
3. Display 10 most recent transactions → **A) Counted Repetition**

*Getting comfortable with pattern recognition is key!*

::: {.notes}
1. The "Quick Check: Answers" slide provides the solutions to the pattern matching questions posed in the previous slide. By revealing the correct answers, learners can assess their understanding of the three fundamental patterns of repetition covered in Module 1: counted repetition, conditional repetition, and collection processing. This self-assessment allows learners to identify areas where they may need further clarification or review.

2. Presenting the answers to the quick check questions serves as a checkpoint in the learning process, ensuring that learners have grasped the key concepts before moving on to the next module. It also provides an opportunity for the presenter to address any common misconceptions or questions that may have arisen during the pattern recognition practice. By reviewing the answers together, learners can solidify their understanding of the core truth that programs need repetition to solve complex problems efficiently.
:::

# Key Takeaways

✅ **All repetition fits three patterns** - learn to recognise them

✅ **Collections (lists) enable scale** - handle any amount of data

✅ **Choose the right tool** - FOR for counting/collections, WHILE for conditions

✅ **Real applications use all patterns** - your finance tracker will too!

::: {.notes}
Key Takeaways:

This module focused on why programs need repetition and introduced the three fundamental repetition patterns in programming: counted repetition, conditional repetition, and collection processing. These patterns enable programs to handle repetitive tasks efficiently and at scale, which is crucial for solving real-world problems like the AI playlist example.

Recognising these patterns in code and mapping them to appropriate problem scenarios is a valuable skill. The module provided practice identifying the patterns and connected the concepts to a real-world finance tracker application. Upcoming modules will explore each pattern in greater depth, building on this foundational understanding of why repetition is essential in programming.
:::

# Coming Next: Module 2

**Module 2: Counted Repetition - For Loops**

You'll learn:

- How `range()` works for precise counting
- Creating and using lists for data storage
- Processing collections with FOR loops
- Common patterns: accumulation, building, filtering

*Ready to write your first loops!*

::: {.notes}
Coming up in Module 2, we'll explore how the `range()` function works for precise counting in Python programs. We'll also learn about creating and using lists for efficient data storage and management.

In addition to these topics, Module 2 will cover processing collections with FOR loops, a powerful technique for automating repetitive tasks. We'll examine common patterns such as accumulation, building and filtering, which are essential skills for working with collections in Python.
:::

# Module 1 Complete! 🎉

**You now understand:**

- Why programs need repetition
- The three fundamental patterns
- How to recognise which pattern fits a scenario
- Why collections are essential for scale

**Next:** Let's implement these patterns in Python code!

::: {.notes}
In this module, we covered the fundamental concepts of repetition in programming. We explored why programs need repetition and introduced the three core patterns: counted repetition, conditional repetition, and collection processing. Learners practised recognising which pattern best fits different programming scenarios.

Furthermore, we emphasised the importance of collections in enabling programs to scale effectively. By leveraging collections, programmers can write code that processes large amounts of data without explicitly repeating instructions for each item. This module laid the groundwork for understanding these essential programming concepts.
:::

