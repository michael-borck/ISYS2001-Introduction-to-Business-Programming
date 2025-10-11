---
title: "Staff Answer Guide: Mastering OOP: Design Choices Unpacked"
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


**Date Prepared:** April 24, 2025

This guide provides sample solutions and evaluation points for the student worksheet focused on OOP design, justification, and ethical AI usage in Python.

## Introduction & Key Concepts
Ensure students understand the definitions provided, particularly:

* **Class:** The blueprint (`Book`, `Patron`).
* **Object:** An instance (`my_book`, `a_patron`).
* **Encapsulation:** Bundling data (attributes) and methods operating on that data within a class, controlling access to internal state (e.g., managing `is_checked_out` via methods).
* **(Inheritance/Polymorphism):** While not directly implemented in the core activities, these are background concepts. Polymorphism could be relevant if discussing how different item types (`Book`, `DVD`) might have different `check_out` logic but the same method name.

## Application Activities

### Activity 1: Designing a Simple Class (`Book`)

**Objective:** Define a `Book` class with relevant attributes and methods for basic library operations, including state management (availability).

**Expected Code Structure:**

```python
# Write your class definition here.
class Book:
    """
    Represents a book in a library system, managing its details and availability.
    """
    def __init__(self, title, author, year):
        """
        Initialises a new Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year of publication.
        """
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False # Attribute to track availability (state)

    def check_out(self):
        """
        Marks the book as checked out if it is currently available.
        Returns:
            bool: True if successfully checked out, False otherwise.
        """
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
            return True
        else:
            print(f"'{self.title}' is already checked out.")
            return False

    def check_in(self):
        """
        Marks the book as available (checked in) if it is currently checked out.
        Returns:
            bool: True if successfully checked in, False otherwise.
        """
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been checked in.")
            return True
        else:
            print(f"'{self.title}' is already checked in.")
            return False

    def display_details(self):
        """ Displays the book's details and availability status. """
        status = "Checked Out" if self.is_checked_out else "Available"
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {status}")

# --- Example Usage (Optional - for testing the class) ---
# book1 = Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)
# book1.display_details()
# book1.check_out()
# book1.display_details()
# book1.check_in()
# book1.display_details()
```

**Evaluation Notes:**

* Check for correct class and `__init__` syntax.
* Attributes `title`, `author`, `year` should be present.
* Crucially, there should be an attribute to track state (like `is_checked_out` or `is_available`), initialised appropriately.
* `check_out` and `check_in` methods should modify this state attribute *conditionally* (i.e., check the current state before changing).
* Methods should ideally provide feedback (print statements or return values) indicating success or failure. Returning a boolean is good practice for interaction (used in Extension).

### Activity 2: Justifying Your Design

**Objective:** Students should articulate the reasoning behind their `Book` class structure, linking it to OOP principles.

**Sample Justification:**

```
# Provide your justification here.
My design for the `Book` class encapsulates all relevant information (title, author, year) and behaviors (checking in, checking out) related to a single book within one structure. This follows the OOP principle of **Encapsulation**, keeping data and methods that operate on that data together.

The inclusion of the `is_checked_out` attribute is essential for managing the book's state internally. The `check_in` and `check_out` methods act as controlled interfaces to modify this state, preventing invalid operations (like checking out an already checked-out book) and hiding the direct manipulation of the `is_checked_out` variable from outside the class.

This design offers benefits like:
- **Modularity:** Each `Book` object is a self-contained unit.
- **Reusability:** The `Book` class can be used to create many book instances.
- **Maintainability:** If the logic for checking books in/out needs to change, modifications are localised to the `Book` class methods.

While Polymorphism isn't heavily demonstrated here, if we later added other item types (like `DVD` or `Magasine`) with their own `check_in`/`check_out` methods, we could potentially treat them interchangeably in parts of the system using polymorphic behavior.
```

**Evaluation Notes:**

* Look for a clear explanation of *why* specific attributes and methods were chosen.
* The justification *must* connect the design to **Encapsulation**. Does the student explain how data and methods are bundled? Do they mention controlled access to state via methods?
* Mentioning benefits like modularity, reusability, or maintainability shows a deeper understanding.
* Bonus points for correctly identifying that Polymorphism isn't the primary principle demonstrated here but explaining how it *could* apply in a broader context.

## Extension Challenge (`Patron` class)

**Objective:** Design a `Patron` class that interacts with the `Book` class, managing borrowing and returning actions.

**Expected Code Structure:**

```python
# (Assume the enhanced Book class from Activity 1 with boolean returns is available)

class Patron:
    """
    Represents a library patron who can borrow and return books.
    """
    def __init__(self, name, patron_id):
        """
        Initialises a new Patron object.

        Args:
            name (str): The name of the patron.
            patron_id (str): The unique ID of the patron.
        """
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = [] # List to hold references to borrowed Book objects

    def borrow_book(self, book):
        """
        Attempts to borrow a book. Checks availability via the book object.

        Args:
            book (Book): The Book object instance to borrow.
        """
        print(f"\nPatron '{self.name}' attempting to borrow '{book.title}'...")
        if isinstance(book, Book): # Basic type check
            if book.check_out(): # Call the book's method, which handles state change & returns status
                self.borrowed_books.append(book)
                print(f"'{book.title}' successfully borrowed by {self.name}.")
            else:
                # check_out method already printed the reason (e.g., "already checked out")
                print(f"Patron '{self.name}' could not borrow '{book.title}'.")
        else:
            print("Invalid item provided. Cannot borrow.")


    def return_book(self, book):
        """
        Attempts to return a book. Checks if the patron has borrowed it.

        Args:
            book (Book): The Book object instance to return.
        """
        print(f"\nPatron '{self.name}' attempting to return '{book.title}'...")
        if isinstance(book, Book) and book in self.borrowed_books:
            if book.check_in(): # Call the book's method, which handles state change & returns status
                self.borrowed_books.remove(book)
                print(f"'{book.title}' successfully returned by {self.name}.")
            else:
                # check_in method already printed the reason (e.g., "already checked in")
                 print(f"Patron '{self.name}' could not return '{book.title}' (state issue).")
        elif not isinstance(book, Book):
             print("Invalid item provided. Cannot return.")
        else: # Book object valid, but not found in borrowed list
            print(f"Patron '{self.name}' did not borrow '{book.title}'. Cannot return.")


    def display_borrowed_books(self):
        """ Displays the list of books currently borrowed by the patron. """
        print(f"\nBooks currently borrowed by {self.name} ({self.patron_id}):")
        if not self.borrowed_books:
            print("  None.")
        else:
            for book in self.borrowed_books:
                # Accessing attributes of the contained Book objects
                print(f"  - {book.title} by {book.author}")

# --- Example Usage (Showing Interaction) ---
# book_a = Book("Dune", "Frank Herbert", 1965)
# book_b = Book("Foundation", "Isaac Asimov", 1951)
# patron1 = Patron("Alice", "P101")

# patron1.display_borrowed_books()
# patron1.borrow_book(book_a) # Alice borrows Dune
# book_a.display_details()    # Show Dune is checked out
# patron1.borrow_book(book_a) # Alice tries to borrow Dune again (fails)
# patron1.borrow_book(book_b) # Alice borrows Foundation
# patron1.display_borrowed_books() # Show Alice has Dune and Foundation

# patron1.return_book(book_a) # Alice returns Dune
# book_a.display_details()    # Show Dune is available again
# patron1.display_borrowed_books() # Show Alice only has Foundation
# patron1.return_book(book_a) # Alice tries to return Dune again (fails)
```

**Evaluation Notes:**

* Check `Patron` class definition with `__init__` storing `name`, `patron_id`, and an empty list for `borrowed_books`.
* Verify `borrow_book` method:
    * Takes a `book` object as input.
    * Calls the `book` object's `check_out` method.
    * Adds the book to `borrowed_books` *only if* `check_out` succeeds.
    * Includes basic error handling/messaging.
* Verify `return_book` method:
    * Takes a `book` object as input.
    * Checks if the `book` is actually in the `borrowed_books` list.
    * Calls the `book` object's `check_in` method.
    * Removes the book from `borrowed_books` *only if* it was present and `check_in` succeeds.
    * Includes basic error handling/messaging.
* The interaction demonstrates how objects of different classes collaborate by calling each other's methods to manage state changes.

## Reflection

**Objective:** Assess the student's metacognition regarding their learning process and ethical use of AI in the context of OOP design.

**Evaluation Guidance:**

* **AI Helpfulness:** Ask for specifics. "Did AI help brainstorm attributes/methods?" "Did AI help structure the class interaction in the extension?" "Did AI help refine the justification paragraph?" Look for concrete examples of prompts used or suggestions received.
* **Integrity:** How did the student ensure they weren't just blindly copying AI output, especially for design choices? "Did you compare AI suggestions with OOP principles discussed in class?" "Did you consider *why* the AI suggested a certain structure?" "Did you modify or reject AI suggestions based on your own understanding or the project requirements?" "Did you test the AI-assisted code thoroughly?" Look for evidence of **Critical Evaluation** and treating the AI as a **Learning Partner**, not just an answer generator. Linking back to **Transparency** (acknowledging use) is also key.
