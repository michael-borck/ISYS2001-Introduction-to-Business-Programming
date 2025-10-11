---
title: "Module 1: Dictionary Fundamentals"
subtitle: "Part of Week 6: Organising Your Thoughts (with Dictionaries)"
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

# Module Overview
- **Duration:** 20 minutes
- **Position:** Module 1 of 3
- **Prerequisites:** Understanding of lists, basic Python syntax from previous weeks

# Learning Objectives
After this module, you will be able to:
- [ ] Explain what dictionaries are and how they differ from lists
- [ ] Identify when dictionaries are more appropriate than other data structures
- [ ] Create basic dictionaries using proper Python syntax
- [ ] Understand the key-value relationship concept

---

# What Are Dictionaries?

## Think of a Real Dictionary 📚

When you look up a word in a traditional dictionary, you:
1. Find the **word** (the key)
2. Read its **definition** (the value)

Python dictionaries work the same way! They store **key-value pairs** where:
- The **key** is like the word you're looking up
- The **value** is like the definition or information you get

## Dictionary vs. List: A Student Records Example

Let's say we want to store information about university students. We could use lists, but look at the problems:

### ❌ Using Lists (The Hard Way)
```python
# Storing student information with parallel lists
student_ids = ["S12345", "S67890", "S11111"]
student_names = ["Alice Chen", "Bob Smith", "Charlie Davis"]
student_majors = ["Information Systems", "Computer Science", "Business"]
student_gpas = [3.8, 3.2, 3.9]

# To find Alice's GPA, we need to:
alice_index = student_ids.index("S12345")  # Find her position
alice_gpa = student_gpas[alice_index]      # Use that position
print(f"Alice's GPA: {alice_gpa}")
```

**Problems with this approach:**
- Multiple lists to keep in sync
- Complex code to find related information
- Easy to make mistakes with indices
- Hard to add new student information

### ✅ Using Dictionaries (The Smart Way)
```python
# Storing the same information with a dictionary
students = {
    "S12345": {
        "name": "Alice Chen",
        "major": "Information Systems", 
        "gpa": 3.8
    },
    "S67890": {
        "name": "Bob Smith",
        "major": "Computer Science",
        "gpa": 3.2
    },
    "S11111": {
        "name": "Charlie Davis", 
        "major": "Business",
        "gpa": 3.9
    }
}

# To find Alice's GPA:
alice_gpa = students["S12345"]["gpa"]
print(f"Alice's GPA: {alice_gpa}")
```

**Benefits of this approach:**
- All related information grouped together
- Direct access using meaningful keys
- Much easier to read and understand
- Simple to add new student records

---

# When Should You Use Dictionaries?

## Perfect Scenarios for Dictionaries 🎯

### 1. **Looking Up Information**
When you need to find specific information quickly:
- Student records by ID
- Product details by barcode
- User preferences by username

### 2. **Grouping Related Data**
When multiple pieces of information belong together:
- A student has a name, major, and GPA
- A course has a title, instructor, and credits
- A book has an author, genre, and rating

### 3. **Counting and Categorising**
When you need to count occurrences or group items:
```python
# Count how many students are in each major
major_counts = {
    "Information Systems": 15,
    "Computer Science": 23, 
    "Business": 18,
    "Engineering": 12
}
```

## When Lists Are Still Better 📝

### Use Lists When:
- **Order matters**: Shopping lists, to-do lists, step-by-step instructions
- **Simple sequences**: A list of numbers, names without additional info
- **Mathematical operations**: Calculations, statistics on sequences

### Quick Decision Guide
Ask yourself: 
- **"Do I need to look things up by name/ID?"** → Use Dictionary
- **"Is this just a sequence of similar items?"** → Use List
- **"Do I need to group related information?"** → Use Dictionary

---

# Creating Your First Dictionaries

## Basic Dictionary Syntax

### Empty Dictionary
```python
# Create an empty dictionary
my_dict = {}
# or
my_dict = dict()
```

### Dictionary with Initial Data
```python
# A simple course information dictionary
course_info = {
    "code": "ISYS2001",
    "title": "Introduction to Business Programming", 
    "credits": 6,
    "semester": "Semester 2"
}
```

## Important Rules for Keys and Values

### Dictionary Keys Must Be:
- **Unique**: No duplicate keys allowed
- **Immutable**: Strings, numbers, tuples are OK. Lists are NOT allowed as keys

```python
# ✅ Good keys
valid_dict = {
    "student_id": "S12345",        # String key
    42: "The Answer",              # Number key  
    (2024, 2): "Semester 2 2024"  # Tuple key
}

# ❌ Bad keys (will cause errors)
# invalid_dict = {
#     ["first", "last"]: "John Doe"  # Lists can't be keys!
# }
```

### Dictionary Values Can Be:
- **Anything**: Strings, numbers, lists, even other dictionaries!

```python
flexible_dict = {
    "name": "Alice",                    # String value
    "age": 20,                         # Number value
    "courses": ["ISYS2001", "MATH101"], # List value
    "address": {                       # Dictionary value!
        "street": "123 University Ave",
        "city": "Sydney"
    }
}
```

---

# Try It Yourself! 🧪

## Exercise 1: Create a Personal Profile
Create a dictionary that represents you as a student:

```python
# Create your student profile dictionary
my_profile = {
    # Add your information here
    "student_id": "S??????",
    "name": "Your Name",
    "program": "Your Program", 
    "year": 1,
    "favourite_subject": "Your favourite subject"
}

print("My student profile:")
print(my_profile)
```

## Exercise 2: Course Catalog
Create a dictionary for a university course:

```python
# Create a course dictionary
course = {
    # Fill in realistic course information
}

print("Course details:")
print(course)
```

---

# Knowledge Check 🎯

Test your understanding before moving to the next module:

<details>
<summary><strong>Question 1:</strong> What's the main advantage of dictionaries over parallel lists?</summary>

**Answer:** Dictionaries group related information together and allow direct access using meaningful keys, eliminating the need to maintain multiple synchronized lists and complex index lookups.
</details>

<details>
<summary><strong>Question 2:</strong> Which of these would be better stored as a dictionary vs. a list?
<br>A) A shopping list of items to buy
<br>B) Student records with ID, name, and grades  
<br>C) A sequence of daily temperatures</summary>

**Answer:** B) Student records with ID, name, and grades - this involves looking up information by ID and grouping related data together. A) and C) are better as lists since they're simple sequences.
</details>

<details>
<summary><strong>Question 3:</strong> Can you use a list as a dictionary key? Why or why not?</summary>

**Answer:** No, you cannot use a list as a dictionary key because lists are mutable (can be changed). Dictionary keys must be immutable (unchangeable) like strings, numbers, or tuples.
</details>

<details>
<summary><strong>Question 4:</strong> What type of data can dictionary values contain?</summary>

**Answer:** Dictionary values can contain any type of data: strings, numbers, lists, other dictionaries, or any Python object. Values have no restrictions unlike keys.
</details>

---

# Module Summary 📋

**Key Takeaways:**
- **Dictionaries store key-value pairs** for efficient information lookup
- **Use dictionaries when** you need to group related data or look up information by name/ID  
- **Use lists when** you have simple sequences or order matters
- **Dictionary keys** must be unique and immutable (strings, numbers, tuples)
- **Dictionary values** can be any type of data, including other dictionaries

**Real-world Applications:**
- Student information systems
- Product catalogs
- User account management
- Configuration settings
- Data analysis and counting

---

# Preparation for Next Module 🚀

In **Module 2: Core Dictionary Operations**, you'll learn:
- How to access and modify dictionary data
- Essential dictionary methods like `.get()`, `.keys()`, and `.values()`
- How to safely work with dictionaries in your code
- Iterating through dictionaries effectively

**Before continuing:**
- [ ] Complete the "Try It Yourself" exercises
- [ ] Check your understanding with the Knowledge Check questions
- [ ] Think about where you might use dictionaries in a personal finance tracker

**Ready?** Let's move on to learning how to actually work with dictionary data!