---
author: Michael Borck
format:
  docx:
    highlight-style: github
    toc: false
  html:
    embed-resources: true
    toc: true
    toc-expand: 2
  pdf:
    colorlinks: true
    toc: false
  pptx:
    reference-doc: ../../../_assets/template.pptx
title: 'Introduction to Python''s Data Structures: Unleashing Weather Insights'
---

# Copyright
![](../../../_assets/curtin-copy-right.png)

# Acknowledgement of Country
I acknowledge the traditional custodians of the land on which I work and live,
and recognise their continuing connection to land, water and community. I pay
respect to Elders past, present and emerging.

![](../../../_assets/ack_country.png)

# Today

- Introduction to Data Structures
- Lists
- Dictionaries
- Tuples
- Weather Data Analysis Example

::: {.notes}
**Aim**
The purpose of this slide is to provide an overview of the key topics that will be covered in today's presentation on data structures in Python.

**Context**
After acknowledging the traditional owners of the land and covering copyright information, this slide sets the scene for the rest of the presentation. It outlines the main data structures that will be discussed in detail, before moving on to explain what data structures are and why they are important in the following slides.

**Introduction to Data Structures**
This presentation will introduce the fundamental concepts of data structures in Python programming. We will explore three essential built-in data structures: lists, dictionaries, and tuples. Understanding these data structures is crucial for organising and manipulating data effectively in Python programs.

**Lists**
Lists are one of the most versatile and commonly used data structures in Python. They are ordered, mutable, and allow duplicate elements. We will cover the key features of lists, how to create them, and perform basic operations such as accessing, modifying, and iterating over elements.

**Dictionaries**
Dictionaries are unordered collections of key-value pairs, providing a efficient way to store and retrieve data based on unique keys. We will explore the key features of dictionaries, how to create them, and perform common operations like accessing values, modifying entries, and checking for key existence.

**Tuples**
Tuples are ordered, immutable collections of elements, often used to group related data. We will discuss the key characteristics of tuples, how to create them, and perform basic operations such as accessing elements and determining the length of a tuple.

**Weather Data Analysis Example**
To demonstrate the practical application of data structures, we will walk through an example of analysing weather data using lists, dictionaries, and tuples. This example will showcase how these data structures can be used to store, organise, and extract meaningful information from real-world datasets.
:::

# What are Data Structures?

Data structures are ways to organise and store data in programming. They help us
manage information efficiently and are fundamental to solving problems with
code.

::: {.notes}
**Aim**
This slide aims to introduce the concept of data structures and provide an overview of their importance in programming and software development.

**Context**
The previous slides focused on the introduction, copyright information, and acknowledgement of country. This slide marks the beginning of the main content, starting with the fundamental concept of data structures. Subsequent slides will delve into specific data structures like lists, dictionaries, and tuples, along with their key features and basic operations.

**What are data structures?**
Data structures are fundamental building blocks in programming that allow efficient organisation, storage, and retrieval of data. They provide a way to structure and manage data within a program, enabling developers to write more organised and optimised code. Common examples of data structures include arrays, linked lists, stacks, queues, trees, and graphs. Each data structure has its own characteristics, strengths, and weaknesses, making them suitable for different scenarios and requirements.
:::

# Why are Data Structures Important?

- They help organise data effectively
- They make it easier to work with large amounts of information
- Different data structures are suited for different tasks

::: {.notes}
**Aim**
This slide aims to highlight the significance of data structures in AI and machine learning by outlining their key benefits and applications.

**Context**
Having introduced the concept of data structures in the previous slide, this slide delves deeper into their importance. It sets the stage for the following slides, which will explore specific data structures like lists, dictionaries, and tuples, and their roles in organising and manipulating data effectively.

**They help organise data effectively** Data structures provide a systematic way to arrange and store data in a computer's memory. By organising data in a logical and efficient manner, data structures enable quick access, retrieval, and modification of information. This is particularly crucial in AI and machine learning, where vast amounts of data need to be processed and analysed. Well-organised data facilitates faster algorithms, improves memory utilisation, and enhances overall performance.

**They make it easier to work with large amounts of information** AI and machine learning often involve dealing with massive datasets. Data structures offer a means to manage and manipulate these large volumes of data efficiently. They provide built-in methods and operations that simplify common tasks such as searching, sorting, inserting, and deleting elements. By leveraging appropriate data structures, developers can write cleaner, more concise code and focus on solving the core problems rather than getting bogged down in low-level details.

**Different data structures are suited for different tasks** No single data structure is optimal for all scenarios. Each data structure has its own strengths and weaknesses, making it suitable for specific tasks. For example, lists are ideal for storing and accessing ordered collections of elements, while dictionaries excel at fast key-value lookups. Tuples are useful for representing fixed-sise, immutable sequences of items. Choosing the right data structure based on the problem at hand is crucial for efficient and effective AI and machine learning implementations.
:::

# Lists: Versatile and Dynamic

Lists are ordered collections of items that can be of any type.

## Key Features of Lists

- Can contain different types of data (numbers, strings, etc.)
- Items are accessed by their position (index)
- Can be changed after creation (mutable)
- Created using square brackets
- Support various operations like adding, removing, and updating items
- Useful for storing and manipulating sequences of elements
  
::: {.notes}
**Aim**
To introduce lists as a versatile and dynamic data structure in Python, highlighting their key features and applications.

**Context**
This slide comes after an introduction to data structures and their importance in programming. It serves as the first in-depth exploration of a specific data structure, setting the stage for subsequent slides on dictionaries and tuples. The slide aims to provide a solid foundation for understanding lists before moving on to more complex data structures.

**Can contain different types of data (numbers, strings, etc.)**
Lists in Python are heterogeneous, meaning they can store elements of different data types within a single list. For example, a list can contain integers, floats, strings, and even other lists or complex objects. This flexibility allows lists to be used in a wide variety of scenarios, from simple collections of numbers to more complex data structures.

**Items are accessed by their position (index)**
Elements in a list are ordered and accessed by their position or index. In Python, indices start at 0 for the first element and increment by 1 for each subsequent element. This allows for efficient access to individual elements within the list using square bracket notation, such as my_list[0] to access the first element.

**Can be changed after creation (mutable)**
Lists in Python are mutable, which means they can be modified after they are created. Elements can be added, removed, or changed using various built-in methods and operations. This mutability allows for flexible manipulation of list contents, such as appending new elements, removing specific items, or updating values at particular indices. The ability to modify lists in-place is a powerful feature that distinguishes them from immutable data structures like tuples.
:::

# Creating a List

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14]
```

::: {.notes}
**Aim**
This slide aims to introduce the process of creating lists in Python, highlighting their simplicity and flexibility.

**Context**
After discussing the key features and importance of lists, this slide naturally follows by showing how to create lists in Python. It precedes slides on basic list operations, serving as a foundation for understanding list manipulation.

**Empty List**
To create an empty list, simply use square brackets with no elements inside:

my_list = []

This initialises a new, empty list that you can later populate with elements as needed.

**List with Initial Elements**
You can also create a list with initial elements by placing them inside the square brackets, separated by commas:

my_list = [1, 2, 3, 4, 5]

This creates a list containing the elements 1, 2, 3, 4, and 5 in that order. Lists can hold elements of different data types, such as integers, floats, strings, or even other lists.

**List Comprehension**
List comprehension provides a concise way to create lists based on existing lists or other iterable objects. It follows this syntax:

new_list = [expression for item in iterable if condition]

For example, to create a list of squares of numbers from 1 to 5:

squares = [x**2 for x in range(1, 6)]

This creates the list [1, 4, 9, 16, 25] by squaring each number in the range 1 to 5.
:::

# Basic List Operations

- Adding items: `fruits.append("orange")`
- Accessing items: `fruits` (gets the first item)
- Changing items: `fruits = "grape"`
- Removing items: `fruits.remove("cherry")`

::: {.notes}
**Aim**
This slide aims to introduce the fundamental operations that can be performed on lists in Python, enabling learners to manipulate and modify list elements effectively.

**Context**
After discussing the key features and creation of lists in the previous slides, this slide delves into the essential operations that can be performed on lists. The following slides will explore other data structures such as dictionaries and tuples, building upon the foundation established by this slide.

**Adding items: `fruits.append("orange")`**
The `append()` method is used to add an element to the end of a list. In the example provided, the string "orange" is appended to the `fruits` list. This operation modifies the list in-place, expanding its sise by one element. The `append()` method is useful when you need to dynamically add items to a list based on certain conditions or user input.

**Accessing items: `fruits[0]` (gets the first item)**
Lists in Python are sero-indexed, meaning the first element has an index of 0. To access an element in a list, you can use square brackets `[]` and provide the index of the desired element. In the example, `fruits[0]` retrieves the first item in the `fruits` list. You can access elements using positive indices (0 to len(fruits)-1) or negative indices (-1 to -len(fruits)).

**Changing items: `fruits[1] = "grape"`**
To modify an element in a list, you can assign a new value to a specific index using the square bracket notation. In the example, `fruits[1] = "grape"` assigns the string "grape" to the second element (index 1) of the `fruits` list, replacing the existing value at that position. This allows you to update or replace elements in a list as needed.

**Removing items: `fruits.remove("cherry")`**
The `remove()` method is used to remove the first occurrence of a specified element from a list. In the example, `fruits.remove("cherry")` removes the string "cherry" from the `fruits` list. If the element appears multiple times, only the first occurrence will be removed. If the element is not found, a `ValueError` will be raised. Alternatively, you can use the `del` statement with an index to remove an element at a specific position.
:::

# Dictionaries: Key-Value Pairs

Dictionaries store data in key-value pairs.

## Key Features of Dictionaries

- Unordered collection of key-value pairs
- Keys must be unique
- Fast for looking up values
- Can contain various data types as values
- Created using curly braces
- Keys and values are separated by colons

::: {.notes}
**Aim**
This slide aims to introduce dictionaries as a key-value pair data structure and explain their fundamental characteristics.

**Context**
After discussing lists and their features, this slide shifts the focus to dictionaries, another essential data structure in programming. The following slides will delve into creating dictionaries and performing basic operations on them.

**Key Features of Dictionaries**
Dictionaries are a powerful data structure that allows for efficient storage and retrieval of data using key-value pairs. Each entry in a dictionary consists of a unique key and its associated value. Keys are used to access and manipulate the corresponding values, providing a convenient way to organise and retrieve information. Dictionaries are unordered, meaning the elements are not stored in a specific sequence, and they can contain various data types as values.

**Creating a Dictionary**
To create a dictionary in Python, you can use curly braces {} or the dict() constructor. Keys and values are separated by colons, and each key-value pair is separated by commas. For example, you can create a dictionary of student grades like this: grades = {"Alice": 85, "Bob": 92, "Charlie": 78}. You can also create an empty dictionary and add key-value pairs later using square bracket notation or the update() method.

**Basic Dictionary Operations**
Dictionaries support various operations for accessing, modifying, and manipulating data. You can access values by their keys using square bracket notation, such as grades["Alice"] to retrieve Alice's grade. You can add new key-value pairs or update existing ones using the same notation. To remove a key-value pair, you can use the del statement or the pop() method. Other common operations include checking if a key exists using the in keyword, retrieving all keys or values using the keys() and values() methods, and iterating over key-value pairs using loops.

**Unordered collection of key-value pairs**
Unlike lists, which are ordered sequences, dictionaries store data as key-value pairs without any specific order. Each key in a dictionary is associated with a corresponding value, allowing for efficient retrieval of values based on their keys. This unordered nature means that the elements in a dictionary are not accessed by their position or index, but rather by their unique keys.

**Keys must be unique**
In a dictionary, each key must be unique within the dictionary. This uniqueness constraint ensures that there are no duplicate keys, and each key maps to a single value. If you attempt to add a key-value pair with a key that already exists in the dictionary, the previous value associated with that key will be overwritten by the new value. This property allows dictionaries to maintain a one-to-one mapping between keys and values.

**Fast for looking up values**
Dictionaries are optimised for fast value lookups based on keys. When you provide a key to access a value in a dictionary, Python uses a efficient hashing mechanism to quickly locate the corresponding value. This makes dictionaries highly efficient for retrieving values, especially when dealing with large amounts of data. The time complexity for accessing values in a dictionary is typically O(1) on average, making it a preferred choice when fast lookups are crucial.
:::

# Creating a Dictionary

```python
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
```

::: {.notes}
**Aim**
The aim of this slide is to introduce how to create a dictionary in Python.

**Context**
This slide follows on from the previous slide about the key features of dictionaries. It provides a practical example of creating a dictionary before moving on to basic dictionary operations in the next slide.

**Creating a Dictionary**
To create a dictionary in Python, we use curly braces {} and separate each key-value pair with a colon :. Multiple key-value pairs are separated by commas. For example:

my_dict = {"apple": 3, "banana": 5, "orange": 2}

This creates a dictionary called my_dict with three key-value pairs. The keys are strings ("apple", "banana", "orange") and the values are integers (3, 5, 2) representing the quantity of each fruit.

We can also create an empty dictionary using empty curly braces:

empty_dict = {}

This creates an empty dictionary called empty_dict which we can add key-value pairs to later.

Dictionaries are mutable, meaning we can change, add or remove key-value pairs after creation.
:::

# Basic Dictionary Operations

- Adding/updating items: `person["job"] = "Engineer"`
- Accessing values: `person["name"]`
- Removing items: `del person["age"]`

::: {.notes}
**Aim**
This slide aims to introduce the basic operations that can be performed on Python dictionaries, such as adding, accessing, and removing items.

**Context**
After discussing lists and their features, the presentation moves on to dictionaries, another essential data structure in Python. The previous slide covered the creation of dictionaries, and this slide builds upon that by explaining the fundamental operations that can be performed on dictionaries.

**Adding/updating items: `person["job"] = "Engineer"`**
To add a new key-value pair to a dictionary or update the value of an existing key, you can use the square bracket notation followed by the key and assign the desired value to it. In the example shown, we are adding or updating the "job" key in the "person" dictionary with the value "Engineer". If the key already exists, its corresponding value will be updated; otherwise, a new key-value pair will be added to the dictionary.

**Accessing values: `person["name"]`**
To retrieve the value associated with a specific key in a dictionary, you can use the square bracket notation followed by the key. In the given example, `person["name"]` will return the value associated with the "name" key in the "person" dictionary. It's important to note that if you try to access a key that doesn't exist in the dictionary, a `KeyError` will be raised.

**Removing items: `del person["age"]`**
To remove a key-value pair from a dictionary, you can use the `del` statement followed by the dictionary name and the key you want to remove within square brackets. In the example provided, `del person["age"]` will remove the key-value pair with the key "age" from the "person" dictionary. After this operation, the "age" key and its corresponding value will no longer exist in the dictionary.
:::

# Tuples: Immutable Collections

Tuples are similar to lists but cannot be changed after creation.

## Key Features of Tuples

- Ordered collection of items
- Cannot be modified after creation (immutable)
- Often used for fixed sets of data
- Created using parentheses
- Elements are separated by commas

::: {.notes}
**Aim**
The purpose of this slide is to introduce tuples as immutable collections in Python and highlight their key characteristics.

**Context**
Having covered lists and dictionaries, this slide shifts focus to tuples, another fundamental data structure in Python. The subsequent slides will delve into the key features of tuples, their creation, and basic operations.

**Key Features of Tuples**
Tuples are ordered, immutable sequences in Python. They allow you to store and group related items together. Once a tuple is created, its elements cannot be modified, added, or removed. This immutability makes tuples suitable for scenarios where data integrity and consistency are crucial. Tuples are defined using parentheses () and elements are separated by commas. They support indexing and slicing operations, allowing you to access individual elements or subsets of the tuple.

**Creating a Tuple**
To create a tuple in Python, you enclose a comma-separated sequence of elements within parentheses. For example, my_tuple = (1, 2, 3) creates a tuple with three integers. You can also create a tuple without parentheses by separating elements with commas, like my_tuple = 1, 2, 3. Tuples can hold elements of different data types, such as integers, floats, strings, or even other tuples. If you need to create a tuple with a single element, you must include a trailing comma after the element to differentiate it from an expression in parentheses.

**Basic Tuple Operations**
Tuples support various operations for accessing and manipulating their elements. You can use indexing to retrieve individual elements by their position, starting from 0 for the first element. For example, my_tuple[0] retrieves the first element. Slicing allows you to extract a portion of the tuple by specifying a range of indices. Tuples also support the + operator for concatenation, creating a new tuple by joining two or more tuples together. The * operator can be used to repeat a tuple a specified number of times. Additionally, you can use the len() function to determine the number of elements in a tuple and the in keyword to check if an element exists within the tuple.

**Ordered collection of items** Tuples are ordered sequences, meaning that the items in a tuple have a defined order. This order is determined when the tuple is created and remains fixed throughout its lifetime. Each item in a tuple can be accessed by its index, similar to lists.

**Cannot be modified after creation (immutable)** One of the defining features of tuples is their immutability. Once a tuple is created, its contents cannot be changed, added to, or removed. This immutability provides a level of data integrity and allows tuples to be used as keys in dictionaries or elements in sets.

**Often used for fixed sets of data** Tuples are commonly used to represent fixed collections of related data. Examples include representing coordinates (x, y), employee records (name, ID, department), or RGB colour values (red, green, blue). The immutability of tuples makes them suitable for scenarios where data should not be accidentally modified.
:::

# Creating a Tuple

```python
coordinates = (10, 20)
rgb_color = (255, 0, 0)
```

::: {.notes}
**Aim**
The aim of this slide is to explain how to create a tuple in Python.

**Context**
This slide is part of a larger presentation on data structures in Python, such as lists and dictionaries. Having covered lists and dictionaries, the presentation now moves on to tuples, which are another important data structure. The slide on creating a tuple follows the one on key features of tuples and precedes the slide on basic tuple operations.
:::

# Basic Tuple Operations

- Accessing items: `coordinates`
- Cannot add, remove, or change items

::: {.notes}
**Aim**
The purpose of this slide is to introduce the basic operations that can be performed on tuples in Python.

**Context**
This slide follows on from the previous slides introducing tuples and their key features. It provides more detail on how to work with tuples in practice. The next slide will give a practical example of using tuples to store weather data.

**Accessing items: `coordinates`**
To access individual elements within a tuple, you can use indexing. For example, if we have a tuple called `coordinates` storing latitude and longitude values like this: `coordinates = (-37.8136, 144.9631)`, we can access the latitude using `coordinates[0]` and the longitude using `coordinates[1]`. Indexing starts at 0 for the first element.

**Cannot add, remove, or change items**
One of the key features of tuples is that they are immutable, meaning their contents cannot be changed once the tuple is created. You cannot add new elements to a tuple, remove elements from a tuple, or modify the existing elements. If you need to update the values, you would have to create a new tuple. This immutability is useful when you want to ensure data remains constant throughout your program.
:::

# Weather Data Example

Let's use these data structures to store and analyse simple weather data.

```python
# List of daily temperatures
temperatures = [22, 24, 19, 21, 23, 25, 20]

# Dictionary of weather information
weather_station = {
    "city": "Sydney",
    # Tuple for fixed location data
    "location" = (-33.8688, 151.2093),  # Latitude and Longitude
    "temperatures": temperatures,
    "conditions": ["Sunny", "Cloudy", "Rainy", "Sunny", "Sunny", "Cloudy", "Rainy"]
}
```

::: {.notes}
**Aim**
This slide aims to illustrate how data structures can be applied to real-world data, using weather data as a practical example.

**Context**
After covering the key data structures of lists, dictionaries and tuples, this slide demonstrates their application to a real-world dataset. It leads into the next slide, which will explore some simple analysis that can be performed on the weather data using these data structures.
:::

# Simple Analysis

```python
# Average temperature
average_temp = sum(temperatures) / len(temperatures)
print(f"Average temperature: {average_temp:.1f}°C")

# Number of sunny days
sunny_days = weather_station["conditions"].count("Sunny")
print(f"Number of sunny days: {sunny_days}")

# Print location
location = weather_station["location"]
print(f"Weather station location: {location}")
```

::: {.notes}
**Aim**
The aim of this slide is to showcase how the weather data example can be used for simple analysis.

**Context**
The previous slide introduced a weather data example to illustrate how data structures like lists, dictionaries, and tuples can be used together to represent and organise real-world data. This slide builds on that example by demonstrating how the weather data can be analysed using simple techniques.
:::

# Summary

- Lists are versatile for storing collections of items
- Dictionaries are great for organising related data
- Tuples are useful for fixed sets of data

::: {.notes}
**Aim**
To summarise the key data structures covered in the presentation and highlight their main use cases.

**Context**
Having explored lists, dictionaries and tuples in detail, including their features, creation and basic operations, this final slide ties together the main points. It reminds the audience of the distinct strengths of each data structure, providing a concise overview to wrap up the presentation.

**Lists are versatile for storing collections of items**
Lists are highly flexible and can store a wide variety of data types, including numbers, strings and even other lists. Their ability to grow or shrink dynamically makes them suitable for scenarios where the number of items is not known in advance or may change over time. Lists provide convenient methods for adding, removing and modifying elements, making them a go-to choice for many programming tasks.

**Dictionaries are great for organising related data**
Dictionaries excel at storing and retrieving data in key-value pairs, allowing for efficient lookup and organisation of related information. By using meaningful keys, dictionaries provide a clear and intuitive way to structure and access data. They are particularly useful when working with data that has a natural mapping or association, such as user profiles, configuration settings or word counts in a text analysis task.

**Tuples are useful for fixed sets of data**
Tuples are immutable sequences, meaning their elements cannot be changed once created. This property makes them suitable for representing fixed collections of data, such as coordinates, database records or function return values. Tuples are generally faster than lists for accessing elements, as they are optimised for performance. They are commonly used to group related pieces of data together and can serve as keys in dictionaries.
:::

