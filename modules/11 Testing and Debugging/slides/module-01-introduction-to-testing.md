---
title: "Python Testing Frameworks: Your Quality Toolkit in the Age of AI"
subtitle: "Building Reliable Code with Human Insight and AI Assistance"
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

# Focus of Today's Presentation:
    * Core concepts of Python testing frameworks (`doctest`, `unittest`, `pytest`).
    * How to leverage AI as your testing assistant.
    * Building a foundation for writing reliable code.

::: {.notes}
Welcome! AI tools are becoming powerful assistants in software development, you might wonder about the role of traditional practices like testing. This session introduces Python testing frameworks, not just as historical tools, but as essential components of your modern development toolkit. We'll explore how these frameworks, combined with your critical thinking and AI assistance, help you build reliable, maintainable, and high-quality Python applications. Our focus will be on understanding foundational concepts and how they are *amplified*, not replaced, by AI.

Today, we'll explore foundational Python testing frameworks like `doctest` for simple, documentation-based tests, and the more structured `unittest` and `pytest`. Crucially, we'll discuss how you can intelligently partner with AI to make your testing efforts more effective and efficient.

:::



# The "Why Test?" in the Age of AI**

* AI generates code, but who verifies its correctness and intent? **You do, with tests!**
* Testing provides the "ground truth" for AI-assisted refactoring and modifications.
* AI can *help write tests faster*, increasing your ability to build a safety net.
* Understanding testing fundamentals makes you a better collaborator with AI tools.

::: {.notes}

You've probably seen AI tools that can write code, suggest bug fixes, and even explain complex algorithms. So, why dedicate time to learning about testing frameworks? The answer is crucial: AI is a powerful assistant, but it's not infallible.
* When AI generates code, tests are what confirm it actually does what's intended and doesn't have subtle bugs.
* If you ask AI to refactor code, how do you know the new code still works? A solid test suite provides that confidence.
* AI can significantly speed up the process of writing tests, but *you* still need to understand what makes a good test and what needs to be tested.
:::



# Why Testing *Still* Matters (Enhanced)**

  * **Ensures Reliability & Quality:** Catches bugs before users (or AI-generated code) introduce them widely.
  * **Facilitates Safer Changes:** Refactor code (yours or AI's) with confidence, knowing tests guard against regressions.
  * **Acts as Living Documentation:** Tests clearly show how code is intended to be used – invaluable for human and AI understanding.
  * **Provides a Safety Net:** AI-driven development can be fast; tests ensure speed doesn't compromise stability.
  * **Reduces Debugging Time:** Well-tested code leads to fewer, easier-to-diagnose bugs.

::: {.notes}

The fundamental benefits of testing haven't disappeared with AI; they've become even more pronounced.
* **Reliability and Quality:** Whether code is written by a human or an AI, it can have bugs. Tests are your first line of defense.
* **Safer Changes:** Imagine AI suggests a major refactor. Without tests, deploying that change is a high-risk gamble. With tests, it's a calculated, verifiable step.
* **Living Documentation:** Well-written tests, especially `doctests`, clearly demonstrate how your functions are supposed to work. This is vital for team members and even for AI tools trying to understand or modify your code later.
* **Safety Net:** As development cycles potentially speed up with AI assistance, having a robust test suite ensures you're not just moving fast but also maintaining stability. AI can even help *build* this safety net faster.
* **Reduced Debugging:** Fewer bugs make it into later stages, and when they do, tests often help pinpoint the cause much quicker.
:::



# Introduction to `doctest` – Simple, Integrated Testing**

* Write tests directly in your function's docstrings.
* Examples look like interactive Python sessions.
* Excellent for simple functions and ensuring documentation is accurate.
* **AI Assistance:**
    * Prompt AI: "Generate `doctest` examples for this Python function, including edge cases."
    * AI can help ensure your documented examples are also effective tests.

::: {.notes}

Our first stop is `doctest`, a wonderfully simple way to integrate tests directly into your code's documentation. The tests are written as if you're typing them into a Python interpreter right in the docstring. This not only tests your code but also provides clear, executable examples of how to use it.
:::

# Doctest Example:
    ```python
    def add(a, b):
        """
        Adds two numbers.
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        """
        return a + b

import doctest
doctest.testmod()
```

::: {.notes}
* **AI Power-Up:** If you have a function, you can ask an AI, "Can you write some `doctest` examples for this function that cover typical usage and a couple of edge cases?" The AI can help you quickly populate your docstrings with useful tests. Always review these suggestions to ensure they accurately reflect the function's intent and cover meaningful scenarios. This is a great way to ensure your documentation is always up-to-date and correct because it *is* the test!
:::



# Introduction to `unittest`**

* Part of Python's standard library.
* Organises tests into classes and methods.
* Supports test automation, setup/teardown for tests.
* Follows xUnit style (familiar if you've seen JUnit, NUnit).
* **AI Assistance:**
    * Prompt AI: "Write `unittest` test cases for this Python function."
    * AI can help generate the class structure and assertion methods.

::: {.notes}

Next is `unittest`, Python's built-in framework that provides a more formal structure for your tests. It's an "xUnit" style framework, meaning tests are organised into classes that inherit from `unittest.TestCase`, and individual test scenarios are methods within those classes that typically start with `test_`. This structure is great for managing larger test suites and for tests that require setup (e.g., creating a temporary database) or cleanup after they run.
:::

# unittest example
    ```python
    import unittest

    class TestSum(unittest.TestCase):
        def test_sum(self):
            self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    if __name__ == '__main__':
        unittest.main()
    ```

::: {.notes}
* **AI Power-Up:** Provide your function to an AI and ask, "Write `unittest` test cases for this function." AI can help generate the boilerplate `TestClass` structure, suggest appropriate `self.assert...` methods (like `assertEqual`, `assertTrue`, etc.), and even propose different test methods for various scenarios. Remember to critically review the generated tests: Do they cover the right conditions? Are the assertions meaningful?
:::



# Introduction to `pytest`**

* Popular third-party framework (install via `pip install pytest`).
* Simple, less verbose syntax (often just functions).
* Powerful features: fixtures, rich plugin ecosystem, detailed reporting.
* Easier to start with for many; scales well.
* **AI Assistance:**
    * Prompt AI: "Write `pytest` tests for this Python function."
    * AI can generate concise test functions and suggest fixture usage.

::: {.notes}
`pytest` is a widely adopted third-party testing framework loved for its simplicity and power. It often requires less boilerplate code than `unittest` – you can frequently write tests as simple functions. `pytest` has a very expressive way of handling test setup and dependencies using "fixtures," and its plugin architecture allows for extensive customisation and integration with other tools.

:::

# pytest example

    ```python
    # import pytest # Not needed if pytest runs the file

    def test_sum():
        assert sum([1, 2, 3]) == 6, "Should be 6"
    ```

::: {.notes}
* **AI Power-Up:** As with `unittest`, you can ask an AI, "Write `pytest` tests for this Python function." AI tools are generally good at generating the straightforward `assert` statements that `pytest` favors. You might also ask, "Can you show me how to use a `pytest` fixture to provide test data for this function?" This helps you learn more advanced features with AI guidance. Always ensure the AI-suggested tests align with your function's logic and cover necessary cases.
:::



# Comparing `doctest`, `unittest`, and `pytest` (AI Lens)**

* **`doctest`:**
    * Pros: Simple, in-documentation, great for examples.
    * Cons: Less suited for complex tests or setup/teardown.
    * *AI Fit:* Excellent for AI to quickly populate docstrings with verifiable examples.
* **`unittest`:**
    * Pros: Standard library, xUnit structure, good for complex scenarios.
    * Cons: Can be verbose.
    * *AI Fit:* AI can generate boilerplate, suggest assertion methods, and help structure test classes.
* **`pytest`:**
    * Pros: Concise, powerful fixtures, rich ecosystem, less boilerplate.
    * Cons: Third-party (needs install).
    * *AI Fit:* AI excels at generating simple `assert` style tests; can help introduce fixture concepts.
* **Your Choice:** Depends on project, team, and complexity. AI can help you get started with *any* of them.

::: {.notes}

So, `doctest`, `unittest`, or `pytest`?
* **`doctest`** is fantastic for simple functions where tests also serve as clear documentation. AI can rapidly generate these examples for you.
* **`unittest`** is robust, part of Python itself, and its structured approach is beneficial for larger projects or when you need sophisticated setup/teardown. AI can lessen the burden of its verbosity by generating initial test structures.
* **`pytest`** often hits a sweet spot with its concise syntax and powerful features like fixtures, making it a favorite for many. AI can easily generate basic `pytest` tests and help you explore more advanced features.
The choice often comes down to the project's needs and team preference. The good news is that AI can assist you in writing tests regardless of the framework, lowering the barrier to entry for all of them. You might even use `doctest` for simple examples and `pytest` or `unittest` for more complex integration tests within the same project.
:::



# Writing Effective Test Cases (AI-Enhanced)**

* **Keep Tests Small & Focused:** One distinct behavior or scenario per test.
    * *AI Assist:* "Break down testing for this complex function into smaller, focused test cases."
* **Use Descriptive Names:** Clearly state what's being tested and the expected outcome.
    * *AI Assist:* "Suggest descriptive names for these `pytest` test functions based on what they test."
* **Test Positive & Negative Scenarios:** Verify correct behavior with valid inputs AND graceful handling of invalid inputs/errors.
    * *AI Assist:* "For this function, suggest `doctest` examples for both valid inputs and common error-inducing inputs."
* **Focus on Behavior, Not Implementation:** Test *what* the code does, not *how* it internally does it (makes tests less brittle).
    * *AI Assist (with caution):* "Write tests for the public API of this class, focusing on its observable behavior." (Requires careful prompting).
* **Human Review is Crucial:** AI generates; you validate, refine, and ensure tests are meaningful.

::: {.notes}

Regardless of the framework, effective tests share common qualities. And AI can help achieve them!
* **Small & Focused:** Each test should ideally check one specific thing. If a test fails, you'll know exactly where the problem lies. You can ask AI to help decompose testing for a complex piece of code.
* **Descriptive Names:** Good names make your test suite readable. AI can suggest names if you provide the test code or its purpose.
* **Positive & Negative Tests:** Don't just test the "happy path." What happens with bad data? Or edge cases? AI is great at brainstorming these: "What are some edge cases or invalid inputs I should test for this login function?"
* **Behavior, Not Implementation:** Test the "contract" of your function – given these inputs, expect these outputs or side effects. Avoid testing internal private methods directly, as this makes your tests fragile if you refactor. Prompt AI carefully here.
* **Always, always review AI-generated tests.** Does it actually test what you intend? Is it clear? Is it robust? You are the final arbiter of test quality.
:::



# Navigating Pitfalls in Testing (Even with AI)
* **Testing Internal Implementation:** (As mentioned) Makes tests brittle.
    * *AI Risk:* AI might do this if not prompted to focus on public interfaces/behavior.
* **Skipping "Simple" Functions/Code:** "Obvious" code can still have bugs.
    * *AI Solution:* AI can generate tests for simple code so quickly, there's less reason to skip!
* **Non-Isolated Tests (Flaky Tests):** Tests that depend on each other or shared state.
    * *AI Risk:* AI might not automatically ensure isolation; human design of test structure and fixtures (for `pytest`/`unittest`) is key.
* **Ignoring Edge Cases:** Focusing only on typical inputs.
    * *AI Solution:* Actively prompt AI: "What are the edge cases for this function that I should test?"
* **Blindly Trusting AI Output:** Generated tests might be incomplete, incorrect, or test the wrong thing. **Critical human review is essential.**

::: {.notes}

While testing is powerful, there are common traps.
* **Testing Internals:** If you change how a function works internally (refactor) but its external behavior remains the same, tests focused on internals will break unnecessarily.
* **Skipping "Simple" Code:** Famous last words! AI can help by making it trivial to generate basic tests for these, removing the excuse.
* **Flaky Tests:** These are tests that sometimes pass and sometimes fail without code changes, often due to external dependencies or shared state. Designing for test isolation is a human skill, though AI might help refactor to improve it if asked specifically.
* **Ignoring Edge Cases:** These are the unusual inputs – empty lists, seros, maximum values – where bugs often hide. AI can be a great partner in brainstorming these.
* **The Biggest AI-Era Pitfall: Blind Trust.** Never assume AI-generated tests are perfect. They are a starting point. You must understand them, review them, and ensure they meet your quality standards and truly validate your code's intended behavior. Your critical thinking is the most important part of the process.
:::



# The Human-AI Partnership in Testing
* **You (the Developer):**
    * Understand requirements and intended behavior.
    * Design the overall testing strategy.
    * Critically evaluate and refine AI-generated tests.
    * Ensure tests are meaningful and maintainable.
    * Own the quality.
* **AI (the Assistant):**
    * Generates initial test code/examples rapidly.
    * Suggests edge cases and scenarios.
    * Helps explain framework syntax or concepts.
    * Can refactor tests for clarity (under your guidance).
    * Handles boilerplate.
* **Goal:** Leverage AI to do more thorough testing, faster, allowing you to focus on high-level design and critical thinking.

::: {.notes}

So, what does this all mean for you? Testing in the AI era is a partnership.
* You bring the deep understanding of what the software *should* do, the context, and the critical judgment. You design the strategy – what needs testing and how thoroughly.
* AI brings speed, the ability to handle repetitive tasks like generating boilerplate test code, and a knack for suggesting things (like edge cases) you might have overlooked.
When you effectively combine your strengths with AI's capabilities, you can achieve a higher level of software quality and a more efficient testing process. You're still in the driver's seat; AI is your co-pilot.
:::



# Conclusion: Embarking on Your AI-Assisted Testing Journey
* Testing is more crucial than ever for verifying human *and* AI-generated code.
* Mastering a testing framework (`doctest`, `unittest`, `pytest`) is a key skill.
* Learn to prompt AI effectively to assist in your testing workflow.
* **Practice is key:** Write tests for your projects, experiment with AI assistance, and critically review the results.
* Explore further: Test-Driven Development (TDD), Behavior-Driven Development (BDD), advanced fixture usage, coverage tools (topics for future learning!).
* **Call to Action:** Start integrating testing, with AI as your partner, *early and often* in your development.

::: {.notes}

To wrap up, the core message is this: in an era where AI can generate and modify code at an unprecedented rate, the ability to write and understand tests is not just relevant – it's a cornerstone of responsible and effective software development.
* Frameworks like `doctest`, `unittest`, and `pytest` provide the tools. Your intellect provides the strategy. AI provides the acceleration.
* The key is to practice. Take the functions you write and try to test them. Use `doctest` for simple cases. Experiment with `pytest` or `unittest`. Ask an AI to help you generate tests, then critically review and improve them.
* There's always more to learn – concepts like Test-Driven Development, where you write tests *before* code, or tools for measuring test coverage, are exciting next steps.
But for now, focus on integrating these foundational testing practices, augmented by thoughtful AI collaboration, into your work. This will make you a stronger, more confident Python developer.
:::
