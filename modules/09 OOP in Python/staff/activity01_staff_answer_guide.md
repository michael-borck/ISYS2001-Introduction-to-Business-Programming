---
title: "Staff Answer Guide: First Steps in Python: Crafting Your First Class"
author: "Michael Borck"
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

This guide provides the solutions and evaluation points for the student worksheet focused on introducing Python classes and ethical AI usage.

## Introduction & Key Concepts
Ensure students have grasped the basic definitions:

* **Class:** Blueprint (e.g., the `Book` definition).
* **Object:** Instance created from the blueprint (e.g., specific book instances like `book1`, `book2`).
* **Attribute:** Variable associated with an object (e.g., `title`, `author`).
* **Method:** Function associated with an object (e.g., `display_info`).

## Application Activities

### Activity 1: Design a Simple Class

**Objective:** Students should define a class `Book` with an initialiser (`__init__`) to set `title` and `author` attributes, and a method (`display_info`) to print these attributes.

**Expected Code Structure:**

```python
# Define the Book class here
class Book:
    """
    Represents a book with a title and author.
    """
    def __init__(self, title, author):
        """
        Initialises a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title  # Assign the title argument to the instance attribute 'title'
        self.author = author # Assign the author argument to the instance attribute 'author'

    def display_info(self):
        """
        Prints the book's title and author.
        """
        print(f"Title: {self.title}, Author: {self.author}")

# Note: No output is expected from just defining the class.
```

**Evaluation Notes:**

* Check for correct class definition syntax (`class Book:`).
* Verify the `__init__` method (constructor) is defined correctly with `self`, `title`, and `author` parameters.
* Ensure attributes are assigned using `self.attribute_name = parameter_name`.
* Check for the `display_info` method definition, taking `self` as the parameter.
* The method should correctly access and print the instance attributes (`self.title`, `self.author`). F-strings are common, but other printing methods are acceptable.

### Activity 2: Implement and Test Your Class

**Objective:** Students should use the `Book` class definition from Activity 1 to create two distinct book objects and call their `display_info` method.

**Expected Code:**

```python
# Implement the Book class and create instances here

# (Include the class definition from Activity 1 here or assume it's already executed)
class Book:
    """
    Represents a book with a title and author.
    """
    def __init__(self, title, author):
        """
        Initialises a new Book object.
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def display_info(self):
        """
        Prints the book's title and author.
        """
        print(f"Title: {self.title}, Author: {self.author}")

# Create instances (objects) of the Book class
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams")
book2 = Book("Pride and Prejudice", "Jane Austen")

# Display information for each book
print("Book 1 Info:")
book1.display_info()

print("\nBook 2 Info:")
book2.display_info()
```

**Expected Output:**

```
Book 1 Info:
Title: The Hitchhiker's Guide to the Galaxy, Author: Douglas Adams

Book 2 Info:
Title: Pride and Prejudice, Author: Jane Austen
```

**Evaluation Notes:**

* Verify the class definition is present or correctly referenced.
* Check that at least two instances are created using `ClassName(arguments)`.
* Ensure the `display_info` method is called correctly on each instance (`instance_name.method_name()`).
* The output should reflect the data provided when creating the instances.

### Extension Challenge: Enhance Your Class

**Objective:** Students should modify the `Book` class to include `year_published`, update the display method, add an `update_author` method, and test these changes.

**Expected Code:**

```python
# Enhance and test the Book class here

class Book:
    """
    Represents a book with a title, author, and publication year.
    Includes methods to display info and update the author.
    """
    def __init__(self, title, author, year_published):
        """
        Initialises a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year_published (int): The year the book was published.
        """
        self.title = title
        self.author = author
        self.year_published = year_published # Added attribute

    def display_info(self):
        """
        Prints the book's title, author, and publication year.
        """
        # Updated to include year_published
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year_published}")

    def update_author(self, new_author):
        """
        Updates the author of the book.

        Args:
            new_author (str): The new author's name.
        """
        print(f"Updating author for '{self.title}' from '{self.author}' to '{new_author}'...")
        self.author = new_author # Modify the instance attribute

# --- Testing the Enhanced Class ---

# Create an instance of the enhanced class
book3 = Book("1984", "George Orwell", 1949)

print("Original Info:")
book3.display_info()

# Update the author (Example scenario: Correcting a typo or pseudonym)
book3.update_author("Eric Arthur Blair (George Orwell)") # Using the author's real name as an example update

print("\nUpdated Info:")
book3.display_info()

```

**Expected Output:**

```
Original Info:
Title: 1984, Author: George Orwell, Year: 1949
Updating author for '1984' from 'George Orwell' to 'Eric Arthur Blair (George Orwell)'...

Updated Info:
Title: 1984, Author: Eric Arthur Blair (George Orwell), Year: 1949
```

**Evaluation Notes:**

* Check the `__init__` method signature and body include `year_published`.
* Verify `display_info` is updated to show the new attribute.
* Ensure the `update_author` method is defined correctly, taking `self` and `new_author`, and that it modifies `self.author`.
* Check that the test code creates an instance of the *enhanced* class, calls `display_info`, calls `update_author`, and calls `display_info` again to show the change.

## Reflection

**Objective:** Assess the student's understanding of the learning process, potential applications, and their approach to using AI tools ethically.

**Evaluation Guidance:**
There are no single "right" answers here. Look for thoughtful and specific responses.

* **How might you use this new knowledge in future projects?**
    * Look for connections to real-world scenarios or other programming concepts. Examples: Managing user data, creating game elements (characters, items), organising data records, building simple simulations, structuring larger applications. Vague answers like "to write code" are less insightful.
* **Reflect on how you used AI tools during this activity.**
    * Encourage honesty and specificity, referencing the AI Tips or other uses. Examples: "I asked ChatGPT for the basic syntax of a Python class as suggested," "I used GitHub Copilot to auto-complete method names," "I asked Bard to explain `self`," "I pasted my code and asked an AI to check for errors or suggest improvements." This relates to the **Transparency** guideline.
* **Describe how you ensured the integrity of your work when using AI assistance.**
    * Look for evidence of critical engagement with AI suggestions. Examples: "I compared the AI's suggestion with the lecture notes/documentation," "The AI gave me code, but I rewrote it to make sure I understood it," "I tested the AI's code to see if it actually worked as expected," "I didn't just copy-paste; I used it to understand the concept and then wrote my own version." This relates to the **Critical Evaluation** and **Learning Partner** guidelines. Assess if the student treated the AI as a tool to *aid* understanding, not just a source of answers.

