---
title: "Building Reliable Data Tools"
subtitle: "A Conceptual Guide for Robust Applications"
format: 
  pptx:
    reference-doc: curtin_template.pptx
  html:
    theme: 
      - cosmo
    toc: true
    toc-expand: 2
    code-fold: true
    embed-resources: true
    fig-cap-location: bottom
    css: module-styles.css
  pdf:
    toc: false
    colorlinks: true
    geometry:
      - top=30mm
      - left=20mm
  docx:
    highlight-style: github
    toc: false
---

## The Goal: From Fragile Scripts to Robust Apps

* A **"Happy Path" script** works only when conditions are perfect.
* A **robust application** is designed to handle imperfections gracefully.
* **Our Goal:** Move beyond simple scripts to build reliable, user-friendly tools.
* **Key Concepts:**
    * **Robustness:** The ability of a system to cope with errors during execution.
    * **User Experience (UX):** Ensuring the user gets clear, helpful feedback, not cryptic errors.

::: {.notes}
Welcome! This week, we're shifting our focus from just writing code that works to writing code that *doesn't break*. A simple script might do the job when everything is perfect, but in the real world, data is messy and users make mistakes. We're going to learn how to build robust applications that can handle these issues gracefully. This is all about improving the user experience and building tools that people can trust.
:::

---

## The Gradio Connection

* A **fragile** Gradio app crashes and shows a generic "Error" message. This is confusing and unhelpful for the user.
* A **robust** Gradio app catches the problem and displays a custom, helpful message like, "Error: Please upload a valid CSV file."
* Good error handling is the difference between a frustrating prototype and a useful tool.

::: {.notes}
You were introduced to Gradio last week. Think about it from a user's perspective. If you upload a file to an app and it just shows a red "Error" message, what do you do next? You don't know what you did wrong. Our goal is to anticipate what might go wrong and give the user specific, helpful feedback. This is a core part of creating a professional-quality application.
:::

---

## Planning for Failure: The "What Ifs"

* Building robust software is like risk management for your code.
* We must anticipate the "What Ifs" of data handling:
    * What if the user uploads the **wrong file type** (e.g., a `.jpg`)?
    * What if the data inside the file is **messy or corrupt**? 
    * What if the file is **missing or can't be found**? 
    * What if the file is **empty**? 

::: {.notes}
So, how do we start? We start by thinking about what could possibly go wrong. This isn't pessimism; it's professional planning. In any data-handling task, there are a handful of common problems we can expect. The user might upload the wrong type of file, the file might have bad data, it might not exist where we expect it to be, or it might be completely empty. We need a plan for each of these scenarios.
:::

---

## Python's "Alarm System": Exceptions

* An **exception** is an event that occurs during program execution that disrupts the normal flow of instructions.
* Think of it as Python's built-in alarm system. When something goes wrong, an "alarm" (the exception) is raised.
* If we don't have a plan to handle the alarm, the program stops (crashes).
* Our job is to listen for specific alarms and execute a backup plan.

::: {.notes}
Luckily, Python has a system for telling us when these problems happen. It's called the exception handling system. When a risky operation fails, Python raises an exception. You've seen these before—`FileNotFoundError`, `ValueError`, etc. If we do nothing, this exception will halt our program. But we can write code to "catch" these exceptions and handle them without crashing.
:::

---

## The Safety Net: A Plan with `try` and `except`

* Python gives us a "safety net" to handle exceptions: the `try...except` block.
* It's a simple "Plan A / Plan B" structure:
    * **`try` block:** This is our **Plan A**. We optimistically *try* to run our risky code (e.g., loading a user's file).
    * **`except` block:** This is our **Plan B**. If a *specific* exception occurs during Plan A, the code in this block is executed instead of crashing.

::: {.notes}
The tool Python gives us for this is the `try...except` block. It’s one of the most important concepts for building reliable code. The logic is simple: you put your main, potentially risky code in the `try` block. Then you define one or more `except` blocks. Each one listens for a specific type of exception. If that exception occurs in the `try` block, the program immediately jumps to the corresponding `except` block and runs that code instead. Plan A fails, so we switch to Plan B.
:::

---

## Code Example: Graceful Handling in Gradio

```python
import pandas as pd

def process_file(uploaded_file):
    try:
        # Plan A: Try to read the uploaded file as a CSV
        df = pd.read_csv(uploaded_file.name)
        return f"Successfully loaded {len(df)} rows."
    except pd.errors.ParserError:
        # Plan B: If it's not a valid CSV, return a helpful message
        return "Error: Please upload a valid CSV file."
    except Exception as e:
        # Plan C: A catch-all for any other unexpected error
        return f"An unexpected error occurred: {e}"
```

---

## Prompting AI for Robust Code

* Now that you understand the concepts, you can guide AI to build robust applications.
* **Generic prompt (less effective):**
    * "Add error handling to my code"
* **Specific prompt (much better):**
    * "Add try/except blocks to handle these cases: file not found, invalid CSV format, empty files, and wrong file type. Provide user-friendly error messages for each."
* **Your role:** Know *what* can go wrong so you can tell AI *what* to handle.
* **AI's role:** Generate the correct Python syntax and exception types.

::: {.notes}
This is where everything comes together. You don't need to memorize exception names or syntax details—that's what AI is for. But you DO need to think through what could go wrong, because AI can't read your mind about your specific use case. When you prompt with specific failure scenarios, AI can generate comprehensive, robust code. Your conceptual understanding lets you evaluate whether AI's solution actually covers all the cases you care about. This is the power of AI-first learning: you focus on the thinking, AI handles the implementation details.
:::
