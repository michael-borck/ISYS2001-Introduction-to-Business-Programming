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
# In this module, you will learn

  - How to display output using print()
  - Common mistakes to avoid
  - Best practices for using print()

::: {.notes}
This module will cover the fundamentals of displaying output using the `print()` function in Python. You will learn how to effectively use `print()` to show results, messages, and other information to users, which is a critical skill for any Python programmer.

The module will also discuss common mistakes to avoid when working with `print()`, such as forgetting to include parentheses or quotation marks, or using incompatible data types. Additionally, you will learn best practices for using `print()`, including how to format output, use escape characters, and print multiple items efficiently.
:::

# Introduction to `print()`

- `print()` is used to display output on the screen.
- Basic syntax: `print("Hello, World!")`
- Always use **parentheses** with `print()`.
- **Strings** must be enclosed in quotation marks.

::: {.notes}
`print()` is a fundamental function in Python used to display output on the screen. Its basic syntax is `print("Hello, World!")`, where the desired output is enclosed in parentheses and surrounded by quotation marks if it is a string. It is crucial to always use parentheses with `print()`, as failing to do so will result in an error.

When working with `print()`, it is important to keep in mind that strings must be enclosed in either single or double quotation marks. Forgetting to include quotation marks or mismatching them is a common error that can prevent the code from running correctly. By following these basic guidelines and being mindful of syntax, you can effectively use `print()` to display output and communicate information to the user.
:::

# Why `print()` is Important

- Helps check if your code is working.
- Debugging tool: find mistakes and track errors.
- Outputs text to the screen for user interaction.

::: {.notes}
print() is a fundamental function in Python that helps developers check if their code is working as expected. It serves as a valuable debugging tool, allowing programmers to identify mistakes, track errors, and gain visibility into the execution flow of their programs. By strategically placing print() statements throughout the code, developers can output relevant information and variable values, making it easier to pinpoint issues and resolve them efficiently.

Moreover, print() plays a crucial role in facilitating user interaction by outputting text to the screen. Whether it's displaying prompts, results, or messages, print() enables effective communication between the program and the user. By leveraging print() to provide meaningful output, developers can create interactive and user-friendly applications that engage and inform users throughout the execution process.
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
This slide  highlights several mistakes that programmers often make when using the `print()` function in Python. These errors include forgetting to use parentheses, omitting quotation marks around string literals, capitalising the function name, misspelling `print()`, and adding extra spaces before the function call. Each incorrect example is marked with a cross emoji, while the correct usage is indicated with a tick emoji.

To avoid these common pitfalls, programmers should pay close attention to the syntax of the `print()` function. The function name should be written in lowercase letters, followed by a set of parentheses containing the value or variable to be printed. String literals must be enclosed in either single or double quotation marks. Proper indentation is also crucial in Python, so any leading spaces before the `print()` function call should be removed. By keeping these guidelines in mind, programmers can ensure that their `print()` statements work as intended and produce the desired output.
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
This slide, focuses on identifying and correcting common mistakes in the provided lines of code. The presenter should guide the audience through the process of analysing the code snippets, encouraging them to spot the errors independently before revealing the solutions.

After discussing the errors and their potential fixes, the presenter should demonstrate running the corrected code to showcase the expected output. This hands-on approach will help reinforce the importance of attention to detail and the impact of even small errors on the functionality of the code.
:::

# Best Practices for `print()`

- Always use **parentheses** with `print()`.
- Enclose text in **quotation marks**.
- Watch out for **indentation errors**.
- **Spell `print` correctly** (avoid typos like `pint`).
- Keep your code **clean and readable**.

::: {.notes}
Always use parentheses when calling the `print()` function in Python. This is the correct syntax and ensures your code will run without errors. Enclose the text you want to print in quotation marks, either single or double quotes. Be careful with indentation, as incorrect indentation can lead to errors in Python. Remember, consistent indentation is crucial for defining code blocks.

Watch out for common typos when writing `print()`, such as `pint()`. These mistakes can cause frustrating errors that are easily avoided by double-checking your code. Aim to write clean and readable code by using clear variable names, adding comments where necessary, and following Python's style guidelines (PEP 8). This will make your code easier to understand and maintain, both for yourself and others who may work with your code in the future.
:::

# Key Takeaways: Working with print()

**Remember These Core Points**:
- print() displays output on your screen
- Always use parentheses and correct quotation marks
- Case sensitivity matters: print(), not Print()

**Next Steps**:
- Practice identifying and fixing common errors
- Start using print() in your own code
- Build confidence with this fundamental command

::: {.notes}
print() is a fundamental command in Python that displays output on the screen. To use it effectively, always include parentheses and the correct quotation marks around the text or variables you want to display. Python is case-sensitive, so make sure to write print() and not Print(). As you start incorporating print() into your own code, take the time to practice identifying and fixing common errors, such as missing parentheses or quotation marks.

Building confidence with print() is key to progressing in Python. Once you understand how to use this command correctly, you'll be able to display useful information for debugging and communicating with users. Don't be afraid to experiment with print() in your code, as it's a valuable tool for understanding what your program is doing at each step. With practice, you'll soon be using print() with ease and reaping the benefits of this essential Python command.
:::

