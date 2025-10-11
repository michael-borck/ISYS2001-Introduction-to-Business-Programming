---
title: "Module 2: Core Dictionary Operations"
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
- **Position:** Module 2 of 3
- **Prerequisites:** Module 1 - Dictionary Fundamentals completed

# Learning Objectives
After this module, you will be able to:
- [ ] Access dictionary values using keys safely and efficiently
- [ ] Add, modify, and remove dictionary entries
- [ ] Use essential dictionary methods like `.get()`, `.keys()`, `.values()`, and `.items()`
- [ ] Iterate through dictionaries using different approaches

---

# Accessing Dictionary Data

## The Basic Way: Using Square Brackets

Just like with lists, you use square brackets `[]` to access dictionary values. But instead of using numbers (indices), you use keys:

```python
# University course information
course = {
    "code": "ISYS2001",
    "title": "Introduction to Business Programming",
    "instructor": "Dr. Smith",
    "credits": 6,
    "capacity": 120
}

# Access individual values
print(f"Course: {course['title']}")
print(f"Instructor: {course['instructor']}")  
print(f"Credits: {course['credits']}")
```

**Output:**
```
Course: Introduction to Business Programming
Instructor: Dr. Smith
Credits: 6
```

## ⚠️ The KeyError Problem

What happens if you try to access a key that doesn't exist?

```python
# This will cause an error!
try:
    prerequisites = course['prerequisites']  # This key doesn't exist!
except KeyError as e:
    print(f"Error: {e}")
```

**Output:**
```
Error: 'prerequisites'
```

The program crashes! This is where the `.get()` method saves the day.

## ✅ The Safe Way: Using `.get()`

The `.get()` method lets you access dictionary values safely:

```python
# Safe access with default value
prerequisites = course.get('prerequisites', 'None listed')
semester = course.get('semester', 'Not specified')

print(f"Prerequisites: {prerequisites}")
print(f"Semester: {semester}")
```

**Output:**
```
Prerequisites: None listed
Semester: Not specified
```

**Why `.get()` is better:**
- Never crashes your program
- Lets you provide a default value if the key doesn't exist
- Makes your code more robust and professional

---

# Modifying Dictionary Data

## Adding New Key-Value Pairs

Simply assign a value to a new key:

```python
# Start with basic student info
student = {
    "id": "S12345",
    "name": "Alice Chen",
    "program": "Information Systems"
}

# Add new information
student["email"] = "alice.chen@student.university.edu"
student["year"] = 2
student["gpa"] = 3.8

print("Updated student record:")
print(student)
```

## Modifying Existing Values

Use the same assignment syntax:

```python
# Update Alice's year and GPA
student["year"] = 3  # She advanced!
student["gpa"] = 3.9  # Improved grades!

print(f"{student['name']} is now in year {student['year']} with GPA {student['gpa']}")
```

## Removing Data

### Using `del` to Remove Key-Value Pairs
```python
# Remove a piece of information
del student["email"]  # No longer needed

print("After removing email:")
print(student)
```

### Using `.pop()` to Remove and Return Value
```python
# Remove and get the value at the same time
old_gpa = student.pop("gpa", 0.0)  # Default to 0.0 if key doesn't exist
print(f"Removed GPA: {old_gpa}")
print("Student without GPA:")
print(student)
```

---

# Essential Dictionary Methods

## Getting All Keys: `.keys()`

```python
# Create a grade book
grades = {
    "Alice": 85,
    "Bob": 92, 
    "Charlie": 78,
    "Diana": 96
}

# Get all student names
student_names = list(grades.keys())
print("Students in class:", student_names)
```

## Getting All Values: `.values()`

```python
# Get all grades
all_grades = list(grades.values())
print("All grades:", all_grades)

# Calculate class average
average_grade = sum(all_grades) / len(all_grades)
print(f"Class average: {average_grade:.1f}")
```

## Getting Key-Value Pairs: `.items()`

```python
# Get everything together
print("Grade report:")
for student, grade in grades.items():
    print(f"  {student}: {grade}")
```

**Output:**
```
Grade report:
  Alice: 85
  Bob: 92
  Charlie: 78
  Diana: 96
```

## Checking if Keys Exist: `in` keyword

```python
# Check if a student is in the class
if "Alice" in grades:
    print(f"Alice's grade: {grades['Alice']}")
else:
    print("Alice not found in gradebook")

# Check if a grade value exists
if 100 in grades.values():
    print("Someone got a perfect score!")
else:
    print("No perfect scores this time")
```

---

# Iterating Through Dictionaries

## Method 1: Iterate Through Keys (Default)

```python
print("Method 1 - Keys only:")
for student in grades:  # This loops through keys by default
    print(f"Student: {student}")
```

## Method 2: Iterate Through Values Only

```python
print("Method 2 - Values only:")
for grade in grades.values():
    print(f"Grade: {grade}")
```

## Method 3: Iterate Through Key-Value Pairs (Most Useful!)

```python
print("Method 3 - Key-value pairs:")
for student, grade in grades.items():
    status = "Pass" if grade >= 80 else "Need improvement"
    print(f"{student}: {grade} ({status})")
```

**Output:**
```
Method 3 - Key-value pairs:
Alice: 85 (Pass)
Bob: 92 (Pass)
Charlie: 78 (Need improvement)
Diana: 96 (Pass)
```

---

# Practical Examples

## Example 1: Student Record Management

```python
def update_student_record(student_dict, **updates):
    """Update student record with new information"""
    for key, value in updates.items():
        student_dict[key] = value
    return student_dict

# Create student record
student = {
    "id": "S67890", 
    "name": "Bob Smith",
    "program": "Computer Science"
}

# Update with new information
student = update_student_record(
    student, 
    email="bob.smith@university.edu",
    year=1,
    gpa=3.2,
    phone="04XX XXX XXX"
)

print("Complete student record:")
for key, value in student.items():
    print(f"  {key}: {value}")
```

## Example 2: Inventory Management

```python
# University bookshop inventory
inventory = {
    "ISYS2001 Textbook": 45,
    "Programming Guide": 23,
    "Calculator": 78,
    "USB Drive": 156
}

def check_stock(item_name):
    """Check if an item is in stock"""
    stock = inventory.get(item_name, 0)
    if stock > 0:
        return f"{item_name}: {stock} units available"
    else:
        return f"{item_name}: Out of stock"

def sell_item(item_name, quantity=1):
    """Sell an item and update inventory"""
    current_stock = inventory.get(item_name, 0)
    if current_stock >= quantity:
        inventory[item_name] = current_stock - quantity
        return f"Sold {quantity} {item_name}(s). Remaining: {inventory[item_name]}"
    else:
        return f"Cannot sell {quantity} {item_name}(s). Only {current_stock} available."

# Test the system
print(check_stock("ISYS2001 Textbook"))
print(sell_item("ISYS2001 Textbook", 3))
print(check_stock("ISYS2001 Textbook"))
```

---

# Try It Yourself! 🧪

## Exercise 1: Personal Gradebook

Create and manipulate a gradebook for yourself:

```python
# Create your personal gradebook
my_grades = {
    "ISYS2001": 0,  # We'll update this!
    "MATH101": 85,
    "ENGL102": 78
}

# TODO: Add your other subjects and grades
# TODO: Update your ISYS2001 grade to something optimistic!
# TODO: Calculate your average grade
# TODO: Print a nice report showing all subjects and grades

# Your code here:
```

## Exercise 2: Course Catalog Manager

```python
# Create a course catalog
courses = {}

# TODO: Add at least 3 courses with details like:
# - course code, title, credits, instructor, capacity

# TODO: Create functions to:
# - Add a new course
# - Update course information  
# - Display course details
# - List all available courses

# Your code here:
```

---

# Knowledge Check 🎯

<details>
<summary><strong>Question 1:</strong> What's the difference between <code>dict['key']</code> and <code>dict.get('key')</code>?</summary>

**Answer:** `dict['key']` will raise a KeyError if the key doesn't exist, potentially crashing your program. `dict.get('key')` returns `None` (or a default value) if the key doesn't exist, making your code safer.
</details>

<details>
<summary><strong>Question 2:</strong> How do you safely remove a key from a dictionary and get its value?</summary>

**Answer:** Use the `.pop()` method: `value = dict.pop('key', default_value)`. This removes the key and returns its value, or the default value if the key doesn't exist.
</details>

<details>
<summary><strong>Question 3:</strong> What's the best way to iterate through both keys and values of a dictionary?</summary>

**Answer:** Use the `.items()` method: `for key, value in dict.items():`. This gives you both the key and value in each iteration.
</details>

<details>
<summary><strong>Question 4:</strong> How can you check if a key exists in a dictionary before accessing it?</summary>

**Answer:** Use the `in` keyword: `if 'key' in dict:`. You can also use `.get()` method which handles missing keys gracefully.
</details>

---

# Common Patterns and Best Practices 💡

## Pattern 1: Safe Dictionary Access
```python
# ❌ Risky
value = my_dict[key]  # Could crash

# ✅ Safe
value = my_dict.get(key, default_value)
```

## Pattern 2: Dictionary Iteration
```python
# ✅ Most common and useful
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

## Pattern 3: Conditional Updates
```python
# Update only if key doesn't exist
if 'new_key' not in my_dict:
    my_dict['new_key'] = 'default_value'

# Or use setdefault
my_dict.setdefault('new_key', 'default_value')
```

## Pattern 4: Building Dictionaries Dynamically
```python
# Start empty and build up
result = {}
for item in data_list:
    key = process_item(item)
    result[key] = item
```

---

# Module Summary 📋

**Key Takeaways:**
- **Safe access:** Use `.get()` instead of `[]` when keys might not exist
- **Modification:** Direct assignment to add/update: `dict[key] = value`
- **Essential methods:** `.keys()`, `.values()`, `.items()` for accessing dictionary contents
- **Iteration:** Use `.items()` to loop through key-value pairs
- **Existence checking:** Use `in` keyword to check if keys exist

**Essential Dictionary Methods:**
- `.get(key, default)` - Safe value retrieval
- `.keys()` - All keys as a view
- `.values()` - All values as a view  
- `.items()` - Key-value pairs as a view
- `.pop(key, default)` - Remove and return value
- `key in dict` - Check if key exists

---

# Preparation for Next Module 🚀

In **Module 3: Dictionary Applications**, you'll learn:
- Working with nested dictionaries for complex data
- Real-world problem-solving patterns
- How to replace parallel lists with dictionary structures
- Preparing for the mini-project implementation

**Before continuing:**
- [ ] Complete both "Try It Yourself" exercises
- [ ] Test the knowledge check questions
- [ ] Practice the common patterns shown above
- [ ] Think about how these operations might help in managing finance data

**Ready for advanced applications?** Let's move to Module 3!