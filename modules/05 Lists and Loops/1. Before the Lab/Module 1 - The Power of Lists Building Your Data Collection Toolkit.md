---
title: "The Power of Lists: Building Your Data Collection Toolkit"
subtitle: "Mastering the Fundamentals of Creating and Accessing Data Collections"
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

# The Power of Lists

* Lists are ordered collections of items
* One of the most versatile data structures in programming
* Foundation for many applications
* Essential skill for any programmer

::: {.notes}
Welcome to our presentation on list fundamentals! Lists are one of the most powerful tools in programming, allowing us to store and organise multiple items in a single variable. Whether you're building a simple to-do application or analysing complex datasets, understanding lists is essential.

Today, we'll explore how to create and access data within lists. We won't be covering loops yet—that's coming in the next module—but you'll learn everything you need to start working with collections of data effectively. These skills form the foundation for more advanced programming concepts we'll explore later.
:::

# Creating Lists

* Lists can contain multiple values in a single variable
* Created using square brackets `[]`
* Can contain any data type (numbers, strings, etc.)
* Elements are separated by commas

```python
# Empty list
my_list = []

# List of numbers
numbers = [1, 2, 3, 4, 5]

# List of strings
colours = ["red", "green", "blue"]

# Mixed data types
mixed = [42, "hello", True, 3.14]
```

::: {.notes}
Creating lists in Python is straightforward. You simply use square brackets and separate individual items with commas. What makes lists particularly flexible is their ability to hold different types of data—you can store numbers, strings, booleans, or even other lists within a list.

Think of a list like a shopping list, where each item is stored in sequence. This ordering is important, as we'll see when we discuss accessing list elements. When you're just starting out, experiment with creating different types of lists to get comfortable with the syntax. Try making lists of your favourite foods, films, or any collection of items that interests you.
:::

# List Indexing

* Accessing individual elements using indices
* Indices start at 0 (first element is at position 0)
* Use square brackets with the index number
* Negative indices count from the end (-1 for last element)

```python
fruits = ["apple", "banana", "cherry", "date"]

# Accessing elements
first_fruit = fruits[0]  # "apple"
second_fruit = fruits[1]  # "banana"
last_fruit = fruits[-1]  # "date"
```

::: {.notes}
Understanding list indexing is crucial when working with lists. In Python (and most programming languages), we count positions starting from 0, not 1. This means the first element is at index 0, the second at index 1, and so on. This zero-based indexing can be confusing at first, but it quickly becomes second nature.

A helpful feature in Python is the ability to use negative indices to access elements from the end of the list. For example, -1 refers to the last element, -2 to the second-last, and so forth. This is particularly useful when you don't know the exact length of a list but need to access its final elements. When teaching beginners about indexing, I often recommend visualising the list with position numbers written above each element to reinforce this concept.
:::

# List Slicing

* Extract multiple elements from a list
* Syntax: `list_name[start:end]`
* Returns elements from `start` up to (but not including) `end`
* Omitting `start` begins from index 0
* Omitting `end` goes until the end of the list

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

first_three = numbers[0:3]  # [0, 1, 2]
middle = numbers[3:7]      # [3, 4, 5, 6]
last_four = numbers[-4:]    # [6, 7, 8, 9]
every_second = numbers[::2] # [0, 2, 4, 6, 8]
```

::: {.notes}
List slicing extends the concept of indexing to allow us to access a range of elements at once. The syntax `list_name[start:end]` creates a new list containing elements from the start index up to, but not including, the end index. This "up to but not including" pattern is common in programming and takes some getting used to.

Slicing offers incredible flexibility. You can omit the start index to slice from the beginning, omit the end index to slice until the end, or even use a third parameter (as in `numbers[::2]`) to specify a step value, which lets you take every nth element. Think of slicing as cutting pieces from a loaf of bread—you specify where to start cutting and where to stop, and you get everything in between.
:::

# List Methods

* Functions built into lists
* Common methods for adding items:
  * `append()` - adds an item to the end
  * `insert()` - adds an item at a specific position
* Common methods for removing items:
  * `remove()` - removes a specific value
  * `pop()` - removes and returns an item at a specific index

```python
shopping = ["bread", "milk"]

# Adding items
shopping.append("eggs")        # ["bread", "milk", "eggs"]
shopping.insert(0, "butter")   # ["butter", "bread", "milk", "eggs"]

# Removing items
shopping.remove("milk")        # ["butter", "bread", "eggs"]
last_item = shopping.pop()     # ["butter", "bread"], last_item = "eggs"
```

::: {.notes}
List methods provide powerful tools for manipulating lists. These built-in functions let you modify lists in various ways without having to write complex code. Understanding these methods is essential for effective list manipulation.

The append and insert methods allow you to add items to a list. Append is simpler, always adding to the end, while insert gives you more control by specifying the exact position. For removing items, remove lets you specify the value to remove, while pop removes an item at a specific position and returns it, which can be useful when you need to use the removed value. Think of these methods as different ways to modify your shopping list—adding forgotten items or crossing off items you've already purchased.
:::

# List Properties

* Lists are mutable (can be changed after creation)
* Lists maintain order of elements
* Lists can contain duplicate values
* Finding the length with `len()`
* Checking for values with `in`

```python
numbers = [3, 1, 4, 1, 5, 9]

# Modifying elements
numbers[0] = 10          # [10, 1, 4, 1, 5, 9]

# Length of list
length = len(numbers)    # 6

# Checking membership
has_five = 5 in numbers  # True
has_seven = 7 in numbers # False
```

::: {.notes}
Understanding list properties helps you work with them effectively. Unlike some data structures, lists are mutable, meaning you can change their contents after creating them. This makes them incredibly flexible for storing data that might need to change.

Lists also maintain the order of elements, which is crucial for many applications. The `len()` function tells you how many elements are in a list, while the `in` operator lets you check if a specific value exists in the list. These features are particularly useful when validating data or implementing search functionality. Whenever you're working with collections of data that need to maintain order and might require modifications, lists are often the go-to data structure.
:::

# Lists vs Other Data Types

* String: ordered collection of characters (immutable)
* Tuple: ordered collection like lists (immutable)
* Dictionary: key-value pairs (unordered in older Python versions)
* Set: unordered collection of unique elements

```python
# Comparison
my_list = [1, 2, 3]           # Mutable, ordered
my_tuple = (1, 2, 3)          # Immutable, ordered
my_dict = {"a": 1, "b": 2}    # Key-value pairs
my_set = {1, 2, 3}            # Unique elements only
```

::: {.notes}
While lists are incredibly versatile, they're just one of several collection types in Python. Understanding the differences between these types helps you choose the right tool for specific tasks. Strings, like lists, are ordered collections, but they're specifically for text and are immutable (cannot be changed after creation). Tuples are similar to lists but immutable, making them useful when you want to ensure data doesn't change.

Dictionaries use key-value pairs instead of indices, allowing you to access elements by name rather than position. Sets are collections of unique elements with no duplicates allowed. Each type has its strengths—lists excel when you need an ordered collection that can change, tuples when order matters but immutability is required, dictionaries when you need named access, and sets when you only care about unique membership. In real-world programming, you'll often use multiple types together to solve complex problems.
:::

# Common List Operations

* Joining two lists with `+`
* Repeating lists with `*`
* Finding an item's index with `index()`
* Counting occurrences with `count()`
* Sorting lists with `sort()` or `sorted()`

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Combine lists
combined = list1 + list2      # [1, 2, 3, 4, 5, 6]

# Repeat lists
repeated = list1 * 3          # [1, 2, 3, 1, 2, 3, 1, 2, 3]

numbers = [3, 1, 4, 1, 5]
position = numbers.index(4)   # 2
occurrences = numbers.count(1) # 2
numbers.sort()                # [1, 1, 3, 4, 5]
```

::: {.notes}
Beyond basic creation and access, Python provides many powerful operations for working with lists. The `+` operator joins lists together, while `*` lets you repeat a list multiple times. The `index()` method finds the position of an item (returning the first occurrence if duplicates exist), and `count()` tells you how many times an item appears in a list.

Sorting is another common operation, with two main approaches: `sort()` modifies the original list in place, while `sorted()` returns a new sorted list without changing the original. These operations give you tremendous flexibility when manipulating collections of data. For instance, when building a playlist app, you might use `+` to combine genre-specific lists, `index()` to find a specific song, and `sort()` to arrange songs alphabetically.
:::

# Practical Applications of Lists

* Storing collections of related items
* Building data-driven applications
* Managing user inputs
* Implementing data structures (stacks, queues)
* Foundation for data analysis

```python
# Example: Simple to-do list application
todo_list = []

# Add tasks
todo_list.append("Complete assignment")
todo_list.append("Read chapter 5")
todo_list.append("Prepare for quiz")

# Mark a task as complete (remove it)
todo_list.remove("Read chapter 5")

# Current tasks: ["Complete assignment", "Prepare for quiz"]
```

::: {.notes}
Lists have countless practical applications in real-world programming. In fact, they're so fundamental that it's hard to imagine building modern applications without them. From simple to-do lists to complex data analysis, lists provide the structure needed to organise and manipulate collections of data.

As a beginner, implementing a basic to-do list application is an excellent way to practise list operations. You can add tasks with `append()`, remove completed tasks with `remove()`, and display the current list to the user. This simple example demonstrates how lists facilitate data management in applications. As you advance, you'll use lists as building blocks for more complex data structures like stacks (last-in, first-out) and queues (first-in, first-out), which have applications in everything from browser history management to printer job scheduling.
:::

# Next Steps

* In the next module: loops for iterating through lists
* Future topics:
  * List comprehensions
  * Nested lists (lists within lists)
  * Advanced list operations
  * Working with libraries that use lists (NumPy, Pandas)
* Practice is key to mastery!

::: {.notes}
Today we've covered the fundamentals of creating and accessing lists, but this is just the beginning of your journey. In the next module, we'll explore loops, which will allow you to process every element in a list automatically—a crucial skill for working with larger collections of data.

As you continue learning, you'll encounter more advanced list concepts like list comprehensions (a concise way to create lists), nested lists (lists containing other lists), and powerful libraries built around list-like structures. The skills you've learned today form the foundation for all of this future learning. I encourage you to practice regularly by creating small programs that use lists—perhaps a contact list, a music playlist, or a collection of your favourite quotes. Remember, programming is like learning an instrument: regular practice leads to mastery.
:::