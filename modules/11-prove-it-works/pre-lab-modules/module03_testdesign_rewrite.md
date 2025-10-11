---
title: "Strategic Test Design: Architecting Quality Assurance"
subtitle: "Specifying What to Test and Why - Your Role as Quality Architect"
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

# You Are the Test Architect

* **You decide** what needs testing
* **You specify** what "correct" looks like
* **You evaluate** if tests are adequate
* **AI assists** with implementation details

::: {.notes}
Welcome to Module 3, where we focus on strategic test design - the highest-level skill in quality assurance. This is where you truly step into the architect role.

In Module 1, you learned verification fundamentals - how to write simple assertions and understand testing concepts. In Module 2, you learned to investigate when verification fails. Now, in Module 3, we're zooming out to the strategic level: How do you decide what needs testing? How do you ensure your tests actually verify what matters?

This is a distinctly human skill. AI can help generate test cases once you've defined the strategy, but deciding what's important to test requires understanding of requirements, user needs, risk assessment, and business logic. These are things you bring to the table.

Think of it this way: AI can be an excellent construction crew, but you're the architect who decides what needs to be built and why. Today you'll learn how to create that blueprint for quality.
:::

# The Strategic Question: What Should I Test?

**Not:** "How do I write tests?"
**But:** "What behaviour matters most?"

**Your strategic decisions:**
- Which features are critical?
- What could go wrong?
- What do users actually need?
- Where are the risks?

::: {.notes}
The fundamental shift in test design is moving from "how" to "what." Beginners often focus on how to write test code. Architects focus on what needs to be tested and why.

Strategic test design starts with understanding what matters. Not every line of code needs equal testing. Some features are critical - if they fail, the whole application is useless. Others are nice-to-have. You need to prioritize.

Ask yourself: What could go wrong? What happens if this calculation is off? What if someone enters unexpected data? What if the system is under heavy load? Your tests should address realistic failure scenarios.

Think about users: What do they actually need this code to do? What would frustrate or harm them if it didn't work correctly? User needs drive testing priorities.

Consider risks: Where are the complex calculations? Where does data come from external sources? Where are there security implications? Risky areas need thorough testing.

These strategic questions guide your entire testing approach. AI can't answer them - they require human judgment about requirements, context, and priorities.
:::

# From Requirements to Test Strategy

**Requirement:** "Calculate employee discount based on years of service"

**Strategic breakdown:**
1. What's the core behaviour? (Discount calculation)
2. What are the input variations? (Different service years)
3. What are edge cases? (0 years, 50 years, negative?)
4. What could go wrong? (Wrong calculation, invalid input)
5. What's the expected output format? (Percentage? Dollar amount?)

::: {.notes}
Let's work through how you transform a requirement into a test strategy.

Start with a requirement - in this case, calculating discounts based on service years. Your first job is understanding what this really means.

Core behaviour: At the heart, this is a calculation. Years of service in, discount out. That's what we're fundamentally testing.

Input variations: Employees might have 0 years (brand new), 1 year, 5 years, 10 years, 25 years. Each might have different discount rules. You need to test representative values from each category.

Edge cases: What about exactly 0 years? What about someone with 50 years? What if the system somehow has negative years (data error)? Edge cases are where bugs hide.

Failure modes: What if the calculation formula is wrong? What if someone passes a string instead of a number? What if the database returns null? Your tests should verify the system handles these gracefully.

Output clarity: Is the discount 10% or 0.10? $10 or 10? Ambiguity in specifications leads to bugs. Clarify expected format before testing.

This analysis - breaking down requirements into testable components - is strategic thinking. Once you've done this analysis, you can specify tests clearly to AI.
:::

# The Three Levels of Test Specification

**Level 1: Plain Language**
"Test that new employees (0 years) get 0% discount"

**Level 2: Example-Based**
"Input: 0 years → Output: 0%"
"Input: 5 years → Output: 10%"

**Level 3: Executable Specification**
```python
assert calculate_discount(0) == 0.0
assert calculate_discount(5) == 0.10
```

::: {.notes}
When specifying what to test, you can work at three levels of detail. Each has its place.

Plain language specifications are great for initial thinking and communication: "We need to test that brand new employees get no discount." This is clear, understandable to non-programmers, and captures the intent.

Example-based specifications are more concrete: "When years is 0, discount should be 0%. When years is 5, discount should be 10%." These examples are unambiguous and can be given to AI.

Executable specifications are the assertions you actually run: `assert calculate_discount(0) == 0.0`. These are your verification mechanism.

You typically move through these levels. Start by thinking in plain language about what matters. Convert to concrete examples. Finally, express as executable assertions.

When working with AI, you can give it Level 1 or 2 specifications and ask it to generate Level 3. Or you write Level 3 yourself and ask AI to implement the function. The key is that you're doing the strategic thinking at Levels 1 and 2 - you're deciding what needs testing and what the expected results should be.
:::

# Identifying What to Test: A Framework

**Ask these questions for any feature:**

1. **Happy path:** What's the normal, expected use?
2. **Boundaries:** What are minimum/maximum valid values?
3. **Invalid input:** What shouldn't be accepted?
4. **Edge cases:** What unusual but valid scenarios exist?
5. **Error conditions:** What external failures could occur?

::: {.notes}
Here's a practical framework for identifying what to test. Apply these five questions to any feature.

Happy path: The normal case. User enters valid data, system processes it correctly, returns expected result. Example: User with 5 years gets 10% discount. This should always work.

Boundaries: The edges of valid ranges. If discount applies from 1-30 years of service, test 1 year (minimum), 30 years (maximum), 0 years (below minimum), 31 years (above maximum). Boundary conditions are bug-prone.

Invalid input: What shouldn't be accepted? Negative years? Non-numeric data? Null values? Your system should handle these gracefully - either with validation errors or sensible defaults. Test these explicitly.

Edge cases: Unusual but technically valid scenarios. What about exactly 0.5 years? What about someone with 100 years (data error but numerically valid)? What about decimal years if the system tracks months?

Error conditions: External dependencies can fail. Database might be down. Network might timeout. File might not exist. Your code should handle these without crashing. Test error handling.

This framework ensures comprehensive thinking about what to test. You're not just testing "does it work?" but "does it work in all the ways it might be used or misused?"
:::

# Using AI to Brainstorm Test Scenarios

**Effective prompt:**
```
"I have a function that calculates shipping costs
based on weight and distance.

What test scenarios should I consider?
Think about:

- Normal cases
- Edge cases
- Invalid inputs
- Boundary conditions"
```

**AI helps expand your thinking, you evaluate relevance.**

::: {.notes}
AI can be a powerful brainstorming partner for test scenarios. The key is asking the right questions.

Describe your function or feature clearly. Give AI context about what it does. Then explicitly ask for different categories of test scenarios - normal, edge, invalid, boundaries.

AI might suggest: "Test with zero weight, test with very heavy packages, test with negative weight (invalid), test with zero distance, test very long distances, test with non-numeric input, test weight at exact boundary between shipping tiers..."

This list expands your thinking. You might have thought of some of these, but AI often suggests scenarios you overlooked. The value is in the comprehensive exploration of possibilities.

However, you must evaluate relevance. AI doesn't know your specific business rules or constraints. If AI suggests testing with 10,000 kg packages but your system only handles up to 100 kg, that scenario might not be relevant. You filter AI's suggestions through your domain knowledge.

Use AI to ensure you've thought comprehensively, but you make the final decisions about what's actually worth testing based on priorities and risks.
:::

# Specifying Expected Results

**Weak specification:**
"Test the discount function"

**Strong specification:**
```
"Test discount calculation:

- 0 years service → 0% discount
- 1-5 years → 5% discount  
- 6-10 years → 10% discount
- 11+ years → 15% discount
- Invalid (negative, null) → error or 0%"
```

**The stronger your specification, the better AI can help.**

::: {.notes}
The quality of tests depends entirely on the quality of your specifications. Vague specifications lead to weak tests.

Compare these two approaches. "Test the discount function" tells AI almost nothing. What should it test? What are the correct results? AI will guess, but it might guess wrong.

The strong specification is precise. It defines the exact rules: what input ranges map to what outputs. It includes error cases. It's unambiguous.

With strong specification, you can hand this to AI and say "Write test cases that verify these rules." AI can generate:
```python
assert calculate_discount(0) == 0.0
assert calculate_discount(3) == 0.05
assert calculate_discount(8) == 0.10
assert calculate_discount(15) == 0.15
```

Or AI can implement the function to match your specification. Either way, the specification is your blueprint.

Developing clear specifications is a critical skill. It forces you to think precisely about requirements. Often, the act of writing specifications reveals ambiguities or gaps in your understanding. That's valuable - better to discover those before implementation.

Strong specifications are unambiguous, comprehensive, and include both normal and error cases.
:::

# The Specification-First Workflow

1. **Understand the requirement** (Read, ask questions)
2. **Write plain language specification** (What should happen?)
3. **Convert to examples** (Concrete input/output pairs)
4. **Identify edge cases** (Use framework, ask AI)
5. **Write assertions or give to AI** (Executable specification)
6. **Implement or have AI implement** (Code that meets spec)
7. **Verify** (Run tests, check they pass)
8. **Refine** (Add missed cases, simplify code)

::: {.notes}
This is your complete workflow for specification-driven development with AI. This is essentially a beginner-friendly Test-Driven Development approach.

Start by thoroughly understanding what's needed. If requirements are unclear, ask questions. Don't proceed with ambiguity.

Write a plain language description of what should happen. Use words, not code. This clarifies your thinking.

Convert to concrete examples. "When input is X, output should be Y." Be specific about data types, formats, ranges.

Identify edge cases systematically using the framework we discussed. Supplement your thinking by asking AI: "What edge cases should I consider for this feature?"

Create executable specifications - either as simple assertions you write yourself, or as detailed specifications you give to AI to convert to test code.

Implementation comes after specification. You might implement yourself, or more commonly, you give your specifications to AI: "Write a function that makes these assertions pass."

Verification confirms the implementation meets your specification. Run the assertions. Do they all pass? If not, either the implementation is wrong or your specification was unclear.

Refinement is the final step. Did you miss test cases? Is the code too complex? Iterate until you have simple, correct, well-tested code.

This specification-first approach ensures you always know what "correct" means before writing or generating code.
:::

# Evaluating Test Coverage

**Ask yourself:**
- Do my tests cover the happy path?
- Do they test boundaries and edge cases?
- Do they verify error handling?
- Would a bug in key logic be caught?
- Am I testing behavior, not implementation?

**You don't need 100% coverage, but you need strategic coverage.**

::: {.notes}
Test coverage is about ensuring you've tested what matters, not about hitting every line of code.

Happy path coverage: Does at least one test verify the normal, expected behavior? If this basic case doesn't work, nothing works.

Edge case coverage: Do you have tests for boundary conditions, unusual inputs, and special cases? This is where most bugs hide.

Error handling coverage: Do tests verify the system handles errors gracefully? What happens with invalid input, missing data, or external failures?

Bug detection: If someone introduced a bug in the core logic - wrong formula, off-by-one error, incorrect condition - would your tests catch it? Or would the tests still pass despite incorrect behavior?

Behavior vs implementation: Are you testing what the code does (behavior) or how it does it (implementation)? Test behavior. If you refactor how the code works but preserve what it does, tests should still pass.

Strategic coverage means prioritizing. Critical features need thorough testing. Simple utilities might need only basic tests. High-risk areas need edge case testing. Low-risk areas might be fine with happy path tests.

You make these priority decisions based on understanding of requirements and risks. AI can help generate tests, but you decide what level of coverage is appropriate for each component.
:::

# When Tests Reveal Missing Requirements

**Scenario:** Writing tests for "validate email address"

**Questions that arise:**
- Should spaces be allowed?
- What about plus signs (user+tag@domain.com)?
- How long can the domain be?
- Are uppercase letters OK?

**Tests help you discover requirements gaps.**

::: {.notes}
A wonderful thing about specification-first development: it reveals gaps and ambiguities in requirements.

Imagine you're testing email validation. You start writing test cases and realize you don't know the answers to several questions. Should the validator accept emails with spaces? Most email systems don't allow spaces, but did the requirement specify this?

What about plus signs? Gmail allows user+tag@gmail.com for filtering. Should your validator? The requirement didn't say.

Maximum lengths? Domain name rules? Case sensitivity? These aren't just implementation details - they're behavioral decisions that affect users.

When your test design reveals these gaps, that's valuable. Go back to requirements, ask stakeholders, research standards, make informed decisions. Then document those decisions in your tests.

Your tests become living documentation of these decisions: "Email validation accepts lowercase and uppercase, rejects spaces, allows plus signs, requires @ symbol and at least one dot in domain..."

This is why test design is strategic. It forces rigorous thinking about requirements and reveals assumptions before they become bugs.

When working with AI, if you discover requirement gaps, clarify them first, then update your specifications and give clearer instructions to AI.
:::

# Organizing Test Specifications

**Group by feature or scenario:**

```
User Authentication Tests:

- Valid login with correct credentials
- Invalid login with wrong password
- Invalid login with non-existent user
- Login attempt with empty fields
- Password reset flow

Discount Calculation Tests:
- New employee (0 years)
- Tier 1: 1-5 years
- Tier 2: 6-10 years
- Tier 3: 11+ years
- Invalid input handling
```

::: {.notes}
As your testing grows, organization becomes important. Group related test specifications together by feature or scenario.

This organization serves multiple purposes. First, it's easier to review and ensure completeness. Looking at "User Authentication Tests," you can quickly see if you're missing important scenarios.

Second, it communicates clearly to others (including AI). When you need to add functionality or fix a bug, you know exactly where the relevant tests are.

Third, it helps maintain consistency. All discount calculation tests should use the same input format, check the same edge cases, handle errors the same way.

When giving specifications to AI, this organization helps: "Here are my authentication test scenarios. Generate test code that verifies each one." The grouping makes it clear what should be tested together.

You might organize by user role ("Admin Tests," "Guest User Tests"), by feature ("Search Tests," "Checkout Tests"), or by component ("Database Tests," "API Tests"). Choose organization that makes sense for your project.

Good organization isn't busywork - it's strategic thinking about the structure of quality assurance.
:::

# AI Prompt Patterns for Test Design

**Pattern 1: Scenario Generation**
"What test scenarios should I create for [feature description]?"

**Pattern 2: Edge Case Discovery**
"What edge cases and boundary conditions should I test for [function]?"

**Pattern 3: Test Implementation**
"Create test assertions for these scenarios: [list specifications]"

**Pattern 4: Gap Analysis**
"Review these test cases: [list]. What important scenarios am I missing?"

::: {.notes}
Let's formalize effective AI prompting patterns for test design. These patterns help you get useful assistance at different stages.

Scenario generation is for brainstorming: "I'm testing a password strength validator. What scenarios should I consider?" AI generates a comprehensive list. You evaluate and prioritize.

Edge case discovery helps you think exhaustively: "My function calculates loan interest based on amount and duration. What edge cases should I test?" AI might suggest zero amounts, very long durations, negative values, etc.

Test implementation converts your specifications to code: "I have these requirements [list them]. Write test assertions that verify each one." You provide the strategy, AI provides the implementation.

Gap analysis is for quality checking: "Here are my current test cases [list them]. What am I missing?" AI might identify untested edge cases or missing error conditions.

The pattern across all these: You provide context and strategic direction, AI provides tactical assistance. You decide what's important, AI helps ensure thoroughness.

Always evaluate AI's suggestions against your domain knowledge and project priorities. AI provides possibilities, you make decisions.
:::

# Recognizing Weak vs Strong Test Specifications

**Weak:**
```python
def test_calculator():
    assert add(1, 1) == 2
```
*Only tests one trivial case*

**Strong:**
```python
def test_add_positive_numbers():
    assert add(2, 3) == 5
    
def test_add_negative_numbers():
    assert add(-1, -1) == -2
    
def test_add_mixed_signs():
    assert add(-5, 3) == -2
    
def test_add_with_zero():
    assert add(0, 5) == 5
```
*Tests multiple scenarios, clear purpose*

::: {.notes}
Learning to recognize test quality is crucial, whether you wrote the tests or AI generated them.

The weak test has several problems. It tests only one case - and a trivial one. If this passes, you know almost nothing about whether the function actually works. It doesn't test negative numbers, large numbers, edge cases, or error conditions. The test name is vague - "test calculator" could mean anything.

The strong tests are better on every dimension. Each test has a clear, specific purpose described in its name. Together, they cover multiple scenarios: positive numbers, negative numbers, mixed signs, zero. If all these pass, you have reasonable confidence the function works correctly.

When evaluating tests - whether yours or AI-generated - ask:
- Does each test have a clear, specific purpose?
- Do tests cover diverse scenarios?
- Are edge cases included?
- Would a bug in the core logic be caught?
- Are test names descriptive?

If you see weak tests, strengthen them. Don't accept quantity over quality. Five well-designed tests are worth more than twenty trivial ones.

This evaluation skill is what makes you an effective test architect, not just a test writer.
:::

# Simplicity in Test Design

**Complex test:**
```python
def test_complex():
    for i in range(10):
        result = calculate(i)
        if i < 5:
            assert result > 0
        else:
            assert result < 0
```

**Simpler tests:**
```python
def test_small_values_positive():
    assert calculate(2) > 0
    
def test_large_values_negative():
    assert calculate(7) < 0
```

::: {.notes}
Just as you should demand simplicity in implementation code, demand it in test code too.

The complex test has logic - loops, conditionals. This makes it harder to understand what's being tested. If it fails, you don't immediately know which case failed. The logic itself could have bugs.

The simpler tests are clear. Each tests one specific thing. Test names explicitly state what's being verified. If one fails, you know exactly what broke. There's no test logic to debug.

When AI generates complex test code - perhaps with loops, nested conditionals, or elaborate setup - ask yourself: "Could this be simpler?" Often the answer is yes.

Prompt AI: "These tests work but are too complex. Can you rewrite as separate, simple test functions, each testing one specific case?"

Simple tests are:
- Easy to understand
- Easy to debug when they fail
- Easy to maintain
- Less likely to have bugs themselves

Complexity in tests defeats their purpose. Tests should clarify what's correct, not obscure it behind complicated logic. Always prefer simple, explicit tests over clever, complex ones.
:::

# Practical Exercise: Design Test Strategy

**Requirement:**
"Create a function that grades students based on scores:

- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F"

**Your task:**
1. What are the happy path cases?
2. What are the boundary conditions?
3. What are invalid inputs?
4. Write specifications for each scenario

::: {.notes}
Let's practice strategic test design with a concrete example. Take a moment to think through this before reading the answer.

Happy path cases - normal scores within each range:
- 95 should give 'A'
- 85 should give 'B'
- 75 should give 'C'
- 65 should give 'D'
- 50 should give 'F'

Boundary conditions - edges of each range:
- 100 (maximum A)
- 90 (minimum A, one above B)
- 89 (maximum B, one below A)
- 80 (minimum B)
- And so on for each grade boundary...
- 60 (minimum D)
- 59 (maximum F)
- 0 (minimum valid score)

Invalid inputs:
- Negative scores (-10)
- Above maximum (110)
- Non-numeric input ("eighty")
- Null or undefined
- Decimal values (85.5) - should these round? Truncate? Be specified in requirements!

Notice how test design revealed a question: what about decimal scores? The requirement didn't specify. You'd need to clarify this before implementing.

Specifications:
```
assert grade(95) == 'A'
assert grade(90) == 'A'
assert grade(89) == 'B'
...
assert grade(-10) raises error or returns 'Invalid'
```

This systematic thinking is test design.
:::

# Test Design Checklist

**Before considering tests complete:**
- [ ] Happy path tested
- [ ] Boundary values tested
- [ ] Invalid inputs tested
- [ ] Edge cases identified and tested
- [ ] Error conditions tested
- [ ] Test names are clear and specific
- [ ] Tests are simple, not complex
- [ ] Tests verify behavior, not implementation
- [ ] Specifications match requirements
- [ ] You understand why each test exists

::: {.notes}
Use this checklist every time you design tests. It ensures systematic, comprehensive thinking.

Happy path: At minimum, verify normal usage works. This is your baseline.

Boundaries: Test the edges of valid ranges. Off-by-one errors lurk here.

Invalid inputs: Don't just test correct usage. Test what happens when someone uses the feature wrong.

Edge cases: Unusual but valid scenarios. Zero values, empty collections, very large numbers, special characters.

Error conditions: Network failures, file not found, database down. How does your code handle external problems?

Clear test names: Someone should understand what each test verifies just from its name.

Simple tests: No complex logic in tests. Each test should be obviously correct.

Behavior, not implementation: Tests should pass as long as behavior is correct, even if implementation changes.

Requirements match: Your specifications should trace back to actual requirements.

Understanding: Never have tests you don't understand. If AI generated complex tests, ask for simplification until you understand them.

This checklist is your quality gate. Tests that pass this checklist are well-designed.
:::

# Common Test Design Mistakes

**Mistake 1: Only testing happy path**
- Miss all the interesting bugs

**Mistake 2: Tests that can never fail**
- Provide false confidence

**Mistake 3: Testing implementation details**
- Tests break when you refactor

**Mistake 4: Vague test names**
- Can't tell what failed or why

**Mistake 5: Accepting AI tests without evaluation**
- AI might miss domain-specific requirements

::: {.notes}
Let's address common mistakes in test design so you can avoid them.

Testing only happy path is the most common beginner mistake. Yes, normal usage should work, but bugs hide in edge cases and error conditions. A function might work perfectly for typical inputs but crash on empty strings or null values.

Tests that can never fail are useless. Example: `assert True` or testing that a variable exists after you just created it. If the test can't fail, it's not testing anything meaningful. Every test should have realistic failure conditions.

Testing implementation details makes tests brittle. If you test that a function uses a specific algorithm or intermediate variable, the test breaks when you refactor. Test behavior instead: given these inputs, expect these outputs.

Vague test names hide information. "test_function1" tells you nothing. "test_discount_calculation_for_new_employee" tells you exactly what's being verified. When a test fails, the name should immediately tell you what broke.

Blindly accepting AI tests is dangerous. AI doesn't know your specific business rules, domain constraints, or regulatory requirements. It generates reasonable-looking tests based on code structure, but might miss crucial domain-specific scenarios. Always evaluate AI tests against your understanding of requirements.

Avoid these mistakes and your tests will actually improve code quality.
:::

# Building Confidence Through Testing

**Weak confidence:**
"I ran it once and it worked"

**Moderate confidence:**
"I tested it with several inputs manually"

**Strong confidence:**
"I have tests for normal cases, edge cases, and error conditions. They all pass."

**Strongest confidence:**
"I have comprehensive tests. I can refactor with confidence because tests verify behavior is preserved."

::: {.notes}
Different levels of testing provide different levels of confidence in your code.

Weak confidence comes from single-case manual testing. You ran the code once with one input. It worked. But does it work with different inputs? Edge cases? You don't know.

Moderate confidence comes from manual testing of several cases. You tried it with positive numbers, negative numbers, zero. Seems to work. But manual testing is time-consuming and easy to forget to repeat after changes.

Strong confidence comes from automated tests covering diverse scenarios. You've thought systematically about what could go wrong and verified it doesn't. Tests run quickly and can be repeated anytime.

Strongest confidence comes when you have tests comprehensive enough that you can refactor code without fear. You can change how the code works internally, and as long as tests still pass, you know behavior is preserved. This is transformative - you can improve code quality confidently.

The goal of test design is building this strong confidence. When you have it, you can work faster because you're not constantly worried about breaking things. You can experiment with AI-generated improvements because your tests will catch if something breaks.

Good test design is an investment that pays dividends in confidence and velocity.
:::

# Integrating All Three Modules

**Module 1:** Verification fundamentals (How to verify?)
**Module 2:** Debugging (What went wrong?)
**Module 3:** Test design (What to verify?)

**The complete cycle:**
1. Design tests (Module 3) - strategic thinking
2. Implement with AI - generate code
3. Verify (Module 1) - run tests
4. Debug if needed (Module 2) - investigate failures
5. Fix and refine - iterate
6. Achieve confidence - well-tested, working code

::: {.notes}
Let's see how all three modules work together in a complete development cycle.

Start with strategic test design (today's module). Understand requirements, identify test scenarios, write specifications. This is your architecture - what needs to be built and verified.

Implementation comes next, often with AI assistance. You give AI your specifications: "Write a function that makes these tests pass." AI generates code.

Verification uses skills from Module 1. Run your tests. Do assertions pass? You're verifying the implementation meets specifications.

If tests fail, debugging from Module 2 comes in. Investigate systematically. Understand why behavior doesn't match expectations. Fix the root cause.

Iteration continues. Maybe debugging revealed you missed a test case. Add it. Maybe the fix introduced a new bug. More verification and debugging. Maybe AI's code is too complex. Ask for simplification.

Eventually, all tests pass. You have confidence the code works. You understand what it does. It's simple enough to maintain. Tests document the behavior. You've achieved quality.

This cycle - design, implement, verify, debug, refine - is professional software development. Each module contributes essential skills. Together, they make you effective at guiding AI to produce quality code.
:::

# Looking Forward: Growing Your Skills

**Immediate practice:**
- Apply this framework to every feature
- Question your test coverage systematically
- Use AI to expand your thinking, not replace it
- Iterate on test design based on what you learn

**Longer term:**
- Study Test-Driven Development (TDD)
- Learn about different testing types (integration, system, etc.)
- Explore testing tools and frameworks more deeply
- Develop intuition for risk-based testing

::: {.notes}
You've now learned the fundamentals of strategic test design. Here's how to continue developing this skill.

Immediate practice: Apply this framework to every feature you build. For each requirement, systematically work through: happy path, boundaries, invalid inputs, edge cases, errors. Make it a habit.

Use the AI collaboration patterns we discussed. Ask AI to brainstorm scenarios, suggest edge cases, identify gaps. But always evaluate suggestions critically against your domain knowledge.

Iterate and learn. When bugs slip through, ask: "What test would have caught this?" Add that test. Over time, you'll develop intuition for what needs testing.

Longer term, explore Test-Driven Development more deeply. TDD is essentially what we've taught: write tests first (specifications), then implement. There's much more to learn about this discipline.

Study different testing levels. We've focused on unit testing (individual functions), but there are integration tests (components working together), system tests (whole application), performance tests, security tests. Each has its place.

Explore testing frameworks and tools beyond the basics. Learn continuous integration, test automation, coverage tools. These amplify effectiveness.

Develop risk-based testing intuition - knowing where to invest testing effort based on impact and likelihood of failure.

But for now, focus on the fundamentals: think strategically, specify clearly, verify thoroughly.
:::

# Key Takeaways

* **Test design is strategic thinking** - deciding what matters
* **You are the architect** - AI assists with implementation
* **Specifications drive quality** - clear specs → good tests
* **Think systematically** - happy path, boundaries, edge cases, errors
* **Evaluate comprehensively** - use checklists, ask AI for gaps
* **Simplicity matters** - in both tests and implementation
* **Tests build confidence** - enabling faster, safer development

::: {.notes}
Let's crystallize the essential lessons from this module.

Test design is fundamentally about strategic thinking. It's deciding what aspects of your software are important enough to verify and how thoroughly. This requires understanding requirements, assessing risks, and prioritizing. These are human judgment skills.

You are the architect in AI-assisted development. You make strategic decisions about what to test and why. AI can help with tactical implementation - generating test code, suggesting scenarios, identifying gaps - but you provide direction.

Clear specifications are the foundation of quality. When you specify precisely what should happen - with examples, edge cases, error conditions - you enable both effective implementation and thorough verification.

Systematic thinking prevents gaps. Use frameworks like the five questions (happy path, boundaries, invalid, edge, errors) to ensure you've thought comprehensively about what could happen.

Comprehensive evaluation catches what you missed. Use checklists. Ask AI to review your test strategy. Continuously question if coverage is adequate.

Simplicity in both tests and code makes everything maintainable. Complex tests are hard to understand and may have bugs. Complex implementation is hard to change safely. Demand simplicity from yourself and from AI.

Tests build confidence. When you have comprehensive, well-designed tests, you can develop faster because you're not afraid of breaking things. You can refactor, experiment, and improve with safety.

Master these concepts and you'll be an effective quality architect in AI-assisted development.
:::

# Final Practice Challenge

**Design a complete test strategy for:**
"A function that validates and formats phone numbers. It should accept various formats (with/without area code, with/without dashes or spaces) and return a standardized format: (XXX) XXX-XXXX. Invalid numbers should return an error message."

**Your deliverables:**
1. Plain language test scenarios
2. Example input/output pairs
3. Edge cases and boundaries
4. Invalid input handling
5. Simple assertions for key cases

::: {.notes}
Here's your final challenge to practice everything from this module. Phone number validation and formatting is a perfect real-world scenario.

Work through the strategic framework:

Plain language scenarios:
- Valid 10-digit number with area code
- Number with dashes
- Number with spaces
- Number with parentheses around area code
- Number without area code (7 digits)
- Invalid: too few digits
- Invalid: too many digits
- Invalid: contains letters
- Edge: empty string
- Edge: null input

Example input/output pairs:
- "1234567890" → "(123) 456-7890"
- "123-456-7890" → "(123) 456-7890"
- "123 456 7890" → "(123) 456-7890"
- "(123) 456-7890" → "(123) 456-7890" (already formatted)
- "456-7890" → Error or special handling
- "12345" → Error (too short)
- "12345678901" → Error (too long)
- "abc-defg-hijk" → Error (non-numeric)

Edge cases and boundaries:
- Exactly 10 digits (minimum valid)
- Exactly 7 digits (valid without area code?)
- Empty string
- Only spaces or dashes
- All zeros "0000000000"
- Mixed valid/invalid characters "123-abc-7890"

Invalid handling decisions needed:
- Should 7-digit numbers be accepted? (Requirement unclear!)
- Should international format be handled?
- What exact error message for each invalid case?

Simple assertions:
```python
assert format_phone("1234567890") == "(123) 456-7890"
assert format_phone("123-456-7890") == "(123) 456-7890"
assert format_phone("12345") == "Error: Invalid phone number"
```

Notice how working through test design revealed requirement gaps! You'd need to clarify the 7-digit number question before implementing.

This exercise demonstrates strategic test thinking. Work through it systematically and you'll have a comprehensive test strategy that can guide AI implementation or your own coding.
:::