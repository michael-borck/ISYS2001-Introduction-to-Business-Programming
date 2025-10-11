---
title: "Staff Answer Guide: Introduction to Safe Utility Functions"
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

## Overview
This guide provides instructors with implementation answers, discussion points, and teaching tips for the "Introduction to Safe Utility Functions" worksheet. The activity introduces students to the concept of error-resistant wrapper functions that handle exceptions internally and return sensible default values.

## Implementation Solutions

### Task: Create a Safe Integer Conversion Function

```python
def safe_int(text, default=0):
    """
    Safely convert text to an integer.
    
    Args:
        text (str): The text to convert
        default (int): Value to return if conversion fails
        
    Returns:
        int: The converted integer or the default value
    """
    try:
        return int(text)
    except ValueError:
        return default
```

Expected outputs:
- `safe_int("123")` → 123
- `safe_int("abc")` → 0
- `safe_int("abc", -1)` → -1

### Extension Function Solutions

#### Option 1: safe_float()
```python
def safe_float(text, default=0.0):
    """
    Safely convert text to a floating-point number.
    
    Args:
        text (str or number): The value to convert
        default (float): Value to return if conversion fails
        
    Returns:
        float: The converted float or the default value
    """
    try:
        return float(text)
    except (ValueError, TypeError):
        return default
```

#### Option 2: safe_divide()
```python
def safe_divide(numerator, denominator, default=0.0):
    """
    Safely divide two numbers, handling division by zero.
    
    Args:
        numerator (number): The dividend
        denominator (number): The divisor
        default (number): Value to return if division fails
        
    Returns:
        number: The result of division or the default value
    """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return default
```

#### Option 3: safe_read_file()
```python
def safe_read_file(filename, default=""):
    """
    Safely read a file, returning a default value if the file doesn't exist.
    
    Args:
        filename (str): Path to the file
        default (str): Value to return if file reading fails
        
    Returns:
        str: The contents of the file or the default value
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except (FileNotFoundError, PermissionError, IOError):
        return default
```

## Teaching Notes

### Key Concepts to Emphasize
1. **Error Prevention vs. Error Handling**: Safe functions represent a proactive approach to dealing with potential errors.
2. **Abstraction of Error Handling**: Users of safe functions don't need to worry about try-except blocks in their code.
3. **Graceful Degradation**: Programs can continue functioning even when operations fail.

### Common Student Misconceptions
1. **All Errors Should Be Hidden**: Clarify that some errors should propagate (e.g., programming errors).
2. **Default Values Are Always Good**: Discuss how default values can sometimes mask real problems.
3. **Safe Functions Replace Exception Handling**: Explain that both approaches have their place.

### Discussion Question Guidance

#### Q1: How does your safe_int function compare to the built-in int() function?
**Key points to guide discussion:**
- The standard `int()` raises exceptions for invalid inputs
- `safe_int()` returns a default value instead of raising exceptions
- `safe_int()` has the same conversion behavior for valid inputs
- `safe_int()` may hide errors that could be important to know about

#### Q2: What are the advantages of returning a default value instead of raising an exception?
**Key points to guide discussion:**
- Simpler calling code without try-except blocks
- Programs continue running despite errors
- Reasonable fallback behavior for non-critical operations
- Better user experience for applications with casual users

#### Q3: Are there any disadvantages to hiding errors this way?
**Key points to guide discussion:**
- Errors might go unnoticed
- Debugging can become harder when errors are silently handled
- The program might continue with invalid data
- Default values might not be appropriate for all use cases

#### Q4: When might it be better to let exceptions propagate?
**Key points to guide discussion:**
- Critical operations where errors should not be ignored
- When detailed error information is needed
- During development and debugging
- When the calling code needs to handle the error specifically

### Reflection Question Guidance

#### How does creating "safe" versions of functions improve reliability?
**Key points to guide discussion:**
- Prevents crashes from unexpected inputs
- Allows for graceful degradation
- Simplifies error handling throughout the codebase
- Creates more predictable behavior

#### What considerations for choosing appropriate default values?
**Key points to guide discussion:**
- The default should be sensible within the domain context
- Ideally identifiable as a "default" and not a valid result
- Should not cause further errors down the line
- May need to be customizable for different contexts

#### How might students apply this concept to other operations?
**Key points to guide discussion:**
- Network operations that might time out
- Database queries that might fail
- User input validation
- JSON/data parsing functions

## Classroom Management Tips

1. **Live Coding**: Demonstrate the building of a safe function from scratch.
2. **Real-world Examples**: Show examples of safe functions in popular libraries.
3. **Pair Programming**: Have students work in pairs to implement different safe functions and then swap implementations.
4. **Error Challenge**: Create a challenge where students must identify scenarios where errors might occur in existing code.

## Assessment Guidelines

### What to Look For in Student Solutions

#### Correct Implementation (40%)
- Proper try-except structure
- Correct exception types being caught
- Appropriate use of the default parameter

#### Function Design (30%)
- Clear, descriptive function name
- Comprehensive docstring
- Sensible parameter names and default values

#### Error Handling Strategy (30%)
- Thoughtful consideration of which exceptions to catch
- Not catching overly broad exceptions without justification
- Appropriate error isolation

#### Bonus Points
- Additional error logging or reporting features
- Parameter validation
- Consideration of multiple error types

## Mini-Project Connection
Remind students that this activity is preparation for the Week 11 mini-project. You might want to have students start brainstorming what types of safe utility functions would be useful in their own programming projects.

## Conclusion
The concept of safe functions provides a powerful tool for creating more robust code. By learning to anticipate and handle errors gracefully, students are developing a key software engineering skill that will serve them throughout their programming careers.