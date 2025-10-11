---
title: "Verification Through Testing: Your Quality Control Toolkit"
subtitle: "Learning to Specify, Verify, and Guide AI-Generated Code"
author: "Michael Borck"
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

# Your New Role: Code Architect, Not Code Typist

* **You specify** what the code should do
* **AI implements** the solution
* **You verify** it works correctly
* **You guide** AI to simpler, better solutions

::: {.notes}
Welcome to a fundamentally different way of thinking about programming. In this course, you won't be spending most of your time typing code. Instead, you'll be learning the critical skills of specification and verification - the skills that matter most when working with AI assistants.

Think of yourself as an architect, not a construction worker. Architects don't build houses brick by brick; they specify what should be built, verify it meets requirements, and ensure quality. That's exactly what you'll be doing with code.

AI can generate code incredibly fast. Your job is to ensure that code actually does what you need, is simple enough to understand and maintain, and solves the right problem. Testing is your primary tool for verification.
:::

# Focus of Today's Module

* Understanding verification vs implementation
* Simple assertions: the foundation of testing
* Using docstrings to specify behaviour
* Reading and evaluating AI-generated tests
* Knowing when code is "good enough"

::: {.notes}
Today we focus on the fundamentals of verification. We'll start with the simplest possible way to verify code works: the assert statement. From there, we'll build up to understanding how specifications work, and how to evaluate whether AI-generated code and tests are actually doing what you need.

The goal isn't to make you expert test writers - it's to make you expert test evaluators and specification writers. These are the skills that amplify your effectiveness when working with AI.
:::

# Why Verification Matters More Than Ever

* AI generates code fast - but is it correct?
* Speed without verification = fast mistakes
* Tests are your "ground truth" specification
* Good tests let you confidently improve code
* You can't manage what you can't measure

::: {.notes}
Here's the reality: AI can write code much faster than humans. But speed means nothing if the code doesn't work correctly. In fact, speed without verification means you'll create a mess faster.

Think about it this way: if I give you a solution to a math problem, how do you know it's correct? You check it. You verify it. The same applies to code - except now, instead of checking your own work, you're checking AI's work.

Tests serve as your specification - they define what "correct" means. When you have good tests, you can confidently ask AI to refactor code, knowing that if the tests still pass, the functionality is preserved. Without tests, every change is a gamble.

The principle is simple: you can't manage what you can't measure. Tests are how you measure correctness.
:::

# The Simplest Test: An Assertion

```python
def add(a, b):
    return a + b

# Verify it works
assert add(2, 3) == 5
assert add(-1, 1) == 0
assert add(0, 0) == 0
```

This is verification at its most basic: "I claim this should be true."

::: {.notes}
Let's start with the absolute simplest form of verification: the assert statement. An assert is just a claim that something should be true. If it's true, nothing happens. If it's false, your program stops with an error.

Look at this example. We have a simple add function. Below it, we have three assertions. Each one is a claim: "When I add 2 and 3, I should get 5." "When I add -1 and 1, I should get 0."

This is verification in its purest form. You're stating what you expect to happen. Python checks if reality matches your expectation. This is the foundation of all testing.

Notice what you're NOT doing: you're not writing complex test frameworks or classes. You're simply stating facts about how your code should behave. This is the mental model we want you to develop.
:::

# Assertions as Specifications

```python
def calculate_discount(price, percent):
    return price * (percent / 100)

# These assertions SPECIFY the behavior
assert calculate_discount(100, 10) == 10
assert calculate_discount(50, 20) == 10
assert calculate_discount(200, 5) == 10
```

**Your assertions define what "correct" means.**

::: {.notes}
Here's a crucial insight: assertions aren't just checks - they're specifications. They define what "correct" means for your code.

Look at this discount calculation example. The assertions don't just verify the function works - they specify exactly how it should behave. "10% of 100 should give 10." "20% of 50 should give 10." These are requirements written in executable code.

This is key to working with AI: before you ask AI to write code, you should be able to write assertions that define what you want. These assertions become your requirements document. They're unambiguous, executable, and verifiable.

When you can write these specifications, you can hand them to AI and say "make this pass." Then you verify if the AI's solution actually makes your assertions true. This is the workflow we're teaching you.
:::

# Working with AI: Specify First, Implement Second

**Traditional approach:**
1. Write code
2. Hope it works
3. Test manually

**AI-assisted approach:**
1. Write simple assertions (your specification)
2. Ask AI to implement
3. Verify assertions pass
4. Check if code is simple enough

::: {.notes}
Let's contrast two workflows. The traditional approach many beginners use is: write some code, run it, manually check if it seems to work, and hope for the best. This is inefficient and error-prone.

The AI-assisted approach we're teaching reverses this. Start by writing simple assertions that specify what you want. These might be as simple as "assert calculate_discount(100, 10) == 10." 

Then, give these assertions to AI along with a description: "Write a function that calculates discounts and makes these assertions pass."

The AI generates code. You run it. Do the assertions pass? Good - the code meets your specification. But you're not done yet. Look at the code. Is it simple? Can you understand it? If it's too complex, ask AI to simplify it. This is your quality control role.

This workflow - specify, generate, verify, simplify - is the core pattern we want you to internalize.
:::

# Docstrings: Specifications Humans Can Read

```python
def calculate_discount(price, percent):
    """
    Calculate discount amount from price and percentage.
    
    Examples:
    - 10% of $100 = $10
    - 20% of $50 = $10
    - 5% of $200 = $10
    """
    return price * (percent / 100)
```

**Docstrings specify behavior in plain language.**

::: {.notes}
Assertions are great for verification, but they're not always easy to read. This is where docstrings come in. A docstring is just a description of what a function does, written as a string right after the function definition.

Look at this example. The docstring clearly states what the function does and gives concrete examples. Notice how the examples in the docstring match the assertions we wrote earlier? This is intentional.

Docstrings serve multiple purposes. First, they're documentation - they help humans understand what the code should do. Second, they're specifications you can give to AI. Third, with Python's doctest module, these examples can actually be run as tests - though we'll keep that simple for now.

The key point: when working with AI, you can write specifications in plain language using docstrings. "I need a function that calculates discounts. 10% of $100 should give $10." Give this to AI, and it will generate the implementation.

Good docstrings are clear, concrete, and example-based. They answer: "What does this do?" and "How do I use it?"
:::

# Doctest: When Examples Become Tests

```python
def add(a, b):
    """
    Add two numbers.
    
    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    >>> add(0, 0)
    0
    """
    return a + b
```

The `>>>` examples can be automatically verified using `python -m doctest filename.py`

::: {.notes}
There's a wonderful feature in Python called doctest that bridges specifications and verification. You write examples in your docstring using a special format that looks like the Python interactive prompt - the `>>>` symbol.

These examples serve three purposes at once: they document how to use the function, they specify what the correct behavior is, and they can be automatically run as tests.

You don't need to learn doctest syntax deeply right now. The important concept is this: examples in documentation can be executable specifications. When you write ">>> add(2, 3)" followed by "5", you're stating a fact: "when I call add with 2 and 3, I expect to get 5."

This is incredibly powerful when working with AI. You can write example-based specifications in plain language, and AI can generate code that makes those examples work. You can then actually run those examples to verify the AI's code is correct.

The pattern is always the same: specify what you want using examples, generate the implementation, verify it works.
:::

# What AI-Generated Tests Look Like

When you ask AI for tests, it might generate:

```python
import unittest

class TestDiscount(unittest.TestCase):
    def test_basic_discount(self):
        self.assertEqual(calculate_discount(100, 10), 10)
    
    def test_different_percentages(self):
        self.assertEqual(calculate_discount(50, 20), 10)
```

**You don't need to write this. You need to READ and EVALUATE it.**

::: {.notes}
When you ask AI to write tests, it will often generate code using frameworks like unittest or pytest. This code can look intimidating with classes, methods, and special assertion functions.

Here's the key insight: you don't need to write this code yourself. AI will generate it. Your job is to read it and evaluate whether it's actually testing the right things.

Look at this example. Strip away the framework boilerplate - the class definition, the unittest.TestCase inheritance, the method names starting with test_. What's the actual verification happening? It's just checking that calculate_discount(100, 10) equals 10. That's an assertion we already understand.

When evaluating AI-generated tests, ask yourself:
- What is actually being tested here?
- Are these the right test cases?
- Are important scenarios missing?
- Are the expected values correct?

You can understand tests without being able to write the framework code yourself. Focus on the logic, not the syntax.
:::

# Evaluating AI-Generated Tests: A Checklist

**Good tests:**
- Test the actual behavior you care about
- Include typical cases and edge cases
- Have clear, correct expected values
- Are simple enough to understand

**Warning signs:**
- Tests that always pass (meaningless)
- Missing important scenarios
- Wrong expected values
- Overly complex test logic

::: {.notes}
Let's develop your ability to evaluate tests. Whether you write simple assertions yourself or AI generates complex test suites, you need to judge if they're actually good tests.

Good tests verify real behavior. They should test both typical usage - the "happy path" - and edge cases like empty inputs, zero values, or boundary conditions. The expected values must be correct based on the requirements. And crucially, you should be able to understand what each test is checking.

Watch out for warning signs. Sometimes AI generates tests that look impressive but are meaningless - tests that can never fail, or tests that don't actually verify the important behavior. Sometimes AI misses critical scenarios. Sometimes it gets the expected values wrong based on a misunderstanding of the requirements.

Your job is to catch these issues. Read the tests. Ask yourself: "If this function was broken in some way, would these tests catch it?" If the answer is no, the tests aren't doing their job.

This evaluation skill is far more important than being able to write complex test code. It's the skill that lets you work effectively with AI-generated tests.
:::

# Practical Exercise: Specification to Verification

**Scenario:** You need a function to check if a password is strong.

**Your specification:**
```python
"""
A strong password must:

- Be at least 8 characters long
- Contain at least one number
- Contain at least one uppercase letter

Examples:
- "Pass123" is not strong (too short)
- "password1" is not strong (no uppercase)
- "Password1" is strong
"""
```

::: {.notes}
Let's practice the specification-to-verification workflow with a concrete example. Imagine you need a password strength checker.

Start by writing a clear specification. Not code - just requirements in plain language with examples. This specification tells you exactly what you need to verify.

From this specification, you can write simple assertions:
```python
assert is_strong_password("Pass123") == False
assert is_strong_password("password1") == False
assert is_strong_password("Password1") == True
```

These assertions are your ground truth. Now you can hand this to AI: "Write a function called is_strong_password that makes these assertions pass and meets these requirements."

AI generates the code. You run your assertions. Do they pass? Read the code - is it simple enough? Does it make sense? If it's overly complex, ask AI to simplify: "Can you make this simpler? Use basic Python and clear logic."

This is the workflow: specify, generate, verify, simplify. Practice this pattern and you'll be effective at guiding AI.
:::

# When to Accept vs Simplify AI Code

**Accept the code if:**
- Assertions pass
- Code is readable and uses basic concepts
- Logic is clear

**Ask AI to simplify if:**
- Uses advanced Python you don't understand
- Logic is convoluted or unclear
- Has unnecessary complexity

**Example prompt:** "This works but is too complex for a beginner. Can you rewrite using only basic Python features like if statements and simple string methods?"

::: {.notes}
One of your most important skills is knowing when code is "good enough" versus when to ask for improvements. Just because code works doesn't mean you should accept it.

AI sometimes generates overly clever solutions using advanced Python features, list comprehensions within comprehensions, or complex algorithms. If you can't understand the code, ask for simplification.

Your prompt is powerful here. Be explicit: "This works but uses features I haven't learned yet. Can you rewrite it using only basic if statements, for loops, and simple string methods?"

AI is very good at generating simpler versions when asked. But it won't do this unless you request it. Don't be intimidated by complex code - you're the architect, you set the standards.

The goal is code that works AND that you understand. Both criteria must be met. Working code you can't understand is not good code for your purposes. Always prioritize clarity and simplicity appropriate to your level.
:::

# Understanding Test Frameworks (Without Writing Them)

* **unittest**: Python's built-in framework (uses classes)
* **pytest**: Popular third-party framework (simpler syntax)
* **doctest**: Tests embedded in documentation

**You don't need to master these frameworks.**
**You need to recognize them and evaluate their output.**

::: {.notes}
You'll encounter three main testing frameworks when AI generates tests: unittest, pytest, and doctest. You don't need to become expert in writing these - AI will handle that. But you should recognize what you're looking at.

unittest uses classes that inherit from unittest.TestCase. Tests are methods that start with "test_". Assertions use self.assertEqual, self.assertTrue, etc. It's verbose but part of Python's standard library.

pytest is simpler - often just functions that start with "test_" and use regular assert statements. It's more beginner-friendly in its syntax.

doctest pulls examples directly from docstrings and runs them as tests. It's the most readable for beginners.

When AI generates tests, it might use any of these. Your job isn't to write in these frameworks from scratch - it's to read the generated tests and evaluate: Are these testing the right things? Are the assertions correct? Do they cover important scenarios?

Think of test frameworks like you think of different brands of measuring tape - they all measure, they just have different interfaces. Focus on what's being measured, not the mechanics of the measuring tool.
:::

# The Verification Mindset

**Key questions to always ask:**
1. What should this code do? (Specification)
2. How do I verify it works? (Test design)
3. Does it actually work? (Run tests)
4. Is it simple enough? (Code quality)
5. What could go wrong? (Edge cases)

::: {.notes}
Let's talk about developing a verification mindset. This is a way of thinking that will serve you throughout your programming career, especially when working with AI.

Always start with specification: What exactly should this code do? Be specific. Use examples.

Next, think about verification: How would I know if it works correctly? What assertions would prove it's working? Don't worry about test framework syntax - just think about what should be true if the code is correct.

Then verify: Run your tests or assertions. Do they pass? If not, the code doesn't meet your specification yet.

Evaluate quality: Even if tests pass, is the code simple enough for your needs? If AI generated something complex, ask for simplification.

Finally, think critically: What edge cases or unusual inputs might break this? Empty strings? Zero values? Negative numbers? Very large numbers? Ask AI to add tests for these scenarios.

This mindset - specify, verify, evaluate, think critically - is what separates someone who can work effectively with AI from someone who just copies and pastes code blindly.
:::

# Common Beginner Mistakes (And How to Avoid Them)

**Mistake 1:** Trusting AI code without verification
- **Fix:** Always write assertions first or verify AI's output

**Mistake 2:** Accepting complex code you don't understand
- **Fix:** Ask AI to simplify to your level

**Mistake 3:** Testing only the "happy path"
- **Fix:** Ask "What could go wrong?" Add edge cases

**Mistake 4:** Writing tests after the code
- **Fix:** Specify behavior first, implement second

::: {.notes}
Let's address common mistakes beginners make, especially when working with AI.

The biggest mistake is blind trust. AI generates code that looks professional, so beginners assume it must be correct. Always verify. Write your assertions or expected behavior first, then check if AI's code matches.

Second mistake: accepting complexity. If AI generates code using features you haven't learned, don't just copy it and move on. Ask AI to rewrite it more simply. You're in control - set your standards.

Third mistake: only testing obvious cases. Yes, your function works with normal inputs. But what about edge cases? Empty inputs? Boundary values? These are where bugs hide. Always ask "What could break this?"

Fourth mistake: writing tests after code is complete. This is backwards. Tests written after the fact tend to just confirm what the code already does, rather than specifying what it should do. Specify behavior first through examples or assertions, then implement.

Avoid these mistakes and you'll be far more effective than most beginners working with AI.
:::

# Practical Workflow Summary

1. **Understand the requirement** (What needs to be done?)
2. **Write simple specifications** (Examples or assertions)
3. **Give specifications to AI** (Describe what you need)
4. **Review generated code** (Does it make sense?)
5. **Run verifications** (Do assertions pass?)
6. **Request simplification if needed** (Make it beginner-friendly)
7. **Add edge case tests** (What could go wrong?)

::: {.notes}
Let's put it all together into a practical workflow you can follow for any coding task.

Start by understanding what you're trying to achieve. Be specific. Instead of "I need a calculator," say "I need a function that adds two numbers."

Write specifications. These might be simple assertions like "assert add(2, 3) == 5" or example-based docstrings showing input and expected output.

Give these to AI with clear instructions: "Write a function that makes these assertions pass" or "Implement this based on these examples."

When AI generates code, don't just run it - read it. Does the logic make sense? Can you follow what it's doing?

Run your verifications. Do your assertions pass? If yes, you've verified correctness. If no, either the code is wrong or your specifications need clarification.

If code is too complex, explicitly ask for simplification: "Rewrite this using only basic Python features I would learn in week 3 of a beginner course."

Finally, think about edge cases. What unusual inputs might break this? Ask AI to add tests for these scenarios, or write simple assertions yourself.

This workflow - understand, specify, generate, review, verify, simplify, extend - is your blueprint for working effectively with AI.
:::

# Looking Ahead: Building on Verification

* **Module 2:** Debugging - verifying what went wrong
* **Module 3:** Test design - systematic verification strategies
* **Throughout the course:** Specify → Generate → Verify → Simplify

**The foundation is always the same:**
You think, specify, and verify. AI generates and assists.

::: {.notes}
Today we've focused on the fundamental skill of verification through testing. This is your foundation.

In Module 2, we'll extend this to debugging - which is really about verifying what went wrong and why. Same mindset, different application.

Module 3 will teach you systematic test design strategies - how to think comprehensively about verification for larger projects.

But throughout this entire course, the pattern remains constant: You think strategically about what needs to happen, you specify it clearly (often with examples), you let AI generate implementation, and you verify the results. If the code is too complex, you guide AI toward simpler solutions.

This isn't just about testing - this is a fundamental working relationship with AI tools. You provide the intelligence, judgment, and strategic direction. AI provides speed and implementation. Verification ensures quality.

Master this mindset and you'll be effective not just in this course, but in any future work with AI development tools.
:::

# Practice Challenge

**Your task:**
Write specifications for a function that converts temperature from Celsius to Fahrenheit. Include:

- Plain language description
- At least 3 example inputs and outputs
- At least 2 edge cases

**Then:**
- Ask AI to implement it
- Verify with assertions
- If too complex, ask for simplification

::: {.notes}
Let's end with a practice challenge you can work on. This reinforces everything we've covered.

Start with specifications. Describe in plain language: "A function that converts Celsius to Fahrenheit using the formula F = (C × 9/5) + 32."

Provide examples:
- 0°C should give 32°F
- 100°C should give 212°F
- -40°C should give -40°F

Think about edge cases:
- What about 0°C?
- What about very large numbers?
- What about negative numbers?

Write these as simple assertions:
```python
assert celsius_to_fahrenheit(0) == 32
assert celsius_to_fahrenheit(100) == 212
assert celsius_to_fahrenheit(-40) == -40
```

Give these to AI with instructions: "Write a function that converts Celsius to Fahrenheit and makes these assertions pass."

Review the generated code. Run your assertions. If the code uses complex features, ask AI: "Can you make this simpler, using only basic arithmetic?"

This exercise practices the entire workflow. Work through it and you'll have internalized the key concepts of this module.
:::

# Key Takeaways

* **Verification** is more important than implementation
* **Assertions** are the simplest form of testing
* **Specifications** guide AI to correct solutions
* **You evaluate** AI-generated code and tests
* **Simplicity** is a requirement you enforce
* **The pattern:** Specify → Generate → Verify → Simplify

::: {.notes}
Let's crystallize the key takeaways from this module.

First and foremost: in the AI era, your value is in verification and specification, not in typing implementation code. This is a fundamental shift in how you should think about programming.

Assertions are your friend. They're simple, clear, and powerful. A well-placed assert statement is worth a thousand lines of complex test framework code.

Specifications - whether written as docstring examples, assertions, or plain language requirements - are how you communicate with AI. Clear specifications lead to correct implementations.

Your job is to evaluate what AI produces. Does it work? Is it simple enough? Does it test the right things? This evaluation skill is critical.

Never accept complexity you don't understand. You have the power to demand simplicity. Use it.

Finally, internalize the workflow: Specify what you want, generate implementation with AI's help, verify it works, simplify if needed. This pattern will serve you throughout the course and beyond.

Practice these concepts and you'll develop the mindset of an effective AI-assisted developer - someone who thinks strategically, specifies clearly, and verifies rigorously.
:::
