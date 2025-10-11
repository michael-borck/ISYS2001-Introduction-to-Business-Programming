---
title: "Basic Python Data Types"
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

Python has several built-in data types that allow you to work with different kinds of data. Here are the fundamental ones you need to know:

1. **Integers (int)**
   - Whole numbers without decimal points
   - Examples: -3, 0, 42
   - Used for counting, indexing, etc.
   - Create with: `x = 5`

2. **Floats (float)**
   - Numbers with decimal points
   - Examples: 3.14, -0.001, 2.0
   - Used for precise calculations
   - Create with: `y = 3.14`

3. **Strings (str)**
   - Text data enclosed in quotes
   - Examples: "Hello", 'Python', "123"
   - Used for names, messages, etc.
   - Create with: `name = "Alice"`

4. **Booleans (bool)**
   - Represent True or False
   - Used for logical operations
   - Only two possible values: True, False
   - Create with: `is_valid = True`

5. **Lists**
   - Ordered collections of items
   - Can contain mixed data types
   - Created using square brackets []
   - Example: `numbers = [1, 2, 3, 4]`

Understanding these basic data types is crucial for effective Python programming. Each type has its own methods and operations. You can check the type of a variable using the `type()` function:

```python
x = 5
print(type(x))  # Output: <class 'int'>
```

Remember, Python is dynamically typed, meaning you don't need to declare the type of a variable explicitly. The interpreter infers the type based on the assigned value.

Pro Tip: Pay attention to data types when performing operations. Mixing types can lead to unexpected results or errors. For example, `"5" + 2` will cause an error because you can't add a string and an integer directly.