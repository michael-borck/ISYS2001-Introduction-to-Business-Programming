---
title: "First Command: print()"
subtitle: "Displaying Output on the Screen"
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

# Introduction to `print()`

- `print()` is used to display output on the screen.
- Basic syntax: `print("Hello, World!")`
- Always use **parentheses** with `print()`.
- **Strings** must be enclosed in quotation marks.

::: {.notes}
The `print()` function allows us to display text or messages on the screen. It’s one of the most fundamental commands in Python and helps us see what our code is doing.
:::


# Why `print()` is Important

- Helps check if your code is working.
- Debugging tool: find mistakes and track errors.
- Outputs text to the screen for user interaction.

::: {.notes}
When writing Python programs, `print()` is an essential tool to check outputs, track progress, and debug issues. If something isn't working as expected, adding a `print()` statement can help identify the problem.
:::


# Common Errors with `print()`

1. **Missing Parentheses**
   - ❌ `print "Hello"`
   - ✅ `print("Hello")`
2. **Missing Quotation Marks**
   - ❌ `print(Hello)`
   - ✅ `print("Hello")`
3. **Case Sensitivity**
   - ❌ `Print("hello")`
   - ✅ `print("hello")`
4. **Misspellings**
   - ❌ `pint("Hello")`
   - ✅ `print("Hello")`
5. **Indentation Errors**
   - ❌ `    print("Hello")` (extra spaces)
   - ✅ `print("Hello")` (no extra spaces)

::: {.notes}
Python is case-sensitive, meaning `print` must be lowercase. Also, **quotation marks are required** when printing text. Forgetting them will result in an error. Watch out for typos like `pint()` instead of `print()`!
:::


# Fix the Errors

- Identify and correct common mistakes in the following lines:
  ```python
  PRINT("Hello")
  print(Hello)
  pint("Hello")
  print("Missing parenthesis"
      print("Indentation error!")
  ```
- What errors do you see?
- Correct and run the fixed code.

::: {.notes}
This exercise will help you recognize and fix common mistakes when using `print()`. Run each line separately to see what kind of error Python gives you and learn how to debug your code.
:::


# Best Practices for `print()`

- Always use **parentheses** with `print()`.
- Enclose text in **quotation marks**.
- Watch out for **indentation errors**.
- **Spell `print` correctly** (avoid typos like `pint`).
- Keep your code **clean and readable**.

::: {.notes}
By following these best practices, you will avoid common errors and make your code easier to understand. Paying attention to these details early will make you a better coder in the long run!
:::