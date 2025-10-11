---
title: "Variables in Python"
subtitle: "Understanding Named Storage for Data"
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

Variables are fundamental building blocks in Python programming. They allow you to store and manipulate data in your code. Here's what you need to know:

1. **Named Storage for Data**
   - Variables are like labeled containers for information
   - They can hold various types of data (numbers, text, etc.)
   - Example: `age = 25` stores the number 25 in a variable named 'age'

2. **Creation by Assignment**
   - Variables are created when you first assign them a value
   - Use the equals sign (=) for assignment
   - Example: `name = "Alice"` creates a variable 'name' with the value "Alice"

3. **Mutable Nature**
   - Variables can change value during program execution
   - Simply reassign a new value to update
   - Example:
     ```python
     x = 10
     x = 20  # x now holds the value 20
     ```

4. **Naming Conventions**
   - Use lowercase letters, numbers, and underscores
   - Start with a letter or underscore, not a number
   - Use descriptive names (e.g., `user_age` instead of `ua`)
   - Avoid Python keywords (like 'if', 'for', 'while')

5. **Case Sensitivity**
   - Python distinguishes between uppercase and lowercase
   - `name`, `Name`, and `NAME` are three different variables
   - Be consistent to avoid confusion

Remember, variables are essential for storing and manipulating data in your programs. They allow you to write flexible and reusable code. Practice creating and using variables to become comfortable with these concepts.

Pro Tip: Use meaningful variable names to make your code more readable and easier to understand, both for yourself and others who might read your code.