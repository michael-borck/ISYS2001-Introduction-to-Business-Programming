---
title: "Staff Facilitator Guide: Verification Through Testing Workshop"
subtitle: "AI-First Testing - Model Answers, Facilitation Tips, and Strategic Guidance"
format:
  pdf:
    toc: true
    colorlinks: true
    number-sections: true
  docx:
    toc: true
    highlight-style: github
  html:
    toc: true
    toc-expand: 2
    embed-resources: true
    number-sections: true
---

# Workshop Philosophy & Pedagogical Approach

## AI-First "Specify and Verify" Framework

This worksheet teaches students to be **strategic architects** rather than manual coders. The core workflow is:

```
Specify → Generate → Verify → Refine
```

**Student Role:**
- Decide WHAT needs testing (and what doesn't)
- Apply systematic frameworks for comprehensive coverage
- Make risk-based decisions about test adequacy
- Evaluate AI-generated code for simplicity and correctness
- Maintain strategic control throughout

**AI Role:**
- Suggest scenarios students might miss
- Implement code based on specifications
- Provide explanations
- Simplify overly complex solutions (when directed)

## Key Learning Objectives

Students should develop:

1. **Strategic thinking** - Risk assessment, test adequacy decisions
2. **Systematic frameworks** - Given/When/Then, Equivalence Partitioning, Boundary Analysis
3. **AI collaboration skills** - Clear specification, critical evaluation
4. **Quality judgment** - When code is "simple enough," when tests are "enough"

## Workshop Structure (3 hours)

| Part | Time | Focus | Key Skill |
|------|------|-------|-----------|
| 1 | 20 min | Understanding Assertions | Reading & writing specifications |
| 2 | 30 min | Specification Design | Systematic frameworks |
| 3 | 40 min | Specify→Generate→Verify | Complete AI workflow |
| 4 | 40 min | Test Design Practice | Risk-based strategy |
| 5 | 30 min | Bug Prevention | Specification-first fixing |
| 6 | 45 min | Integration Exercise | Applying complete framework |
| 7 | 15 min | Reflection | Metacognition |

---

# Part 1: Understanding Assertions (20 minutes)

## Exercise 1.1: Reading Assertions

### Model Answers

**1. What do these assertions tell you about what the function should do?**
- Multiplies amount by rate to calculate tax
- Returns a numeric result (float)
- Should handle different combinations of amounts and rates
- The calculation is straightforward multiplication (amount × rate = tax)

**2. What scenarios are being tested?**
- Normal case: $100 at 10% tax = $10
- Different amount/rate: $50 at 20% tax = $10
- Zero amount: $0 at 10% tax = $0 (boundary condition)

**3. What scenarios are NOT tested that probably should be?**
- **Negative amounts** (invalid input or refund scenario?)
- **Negative rates** (invalid input)
- **Zero rate** (tax-free)
- **Rates > 1.0** (like 1.5 = 150% tax)
- **Very large numbers** (overflow?)
- **Non-numeric inputs** (type validation)

### Strategic Teaching Points

**Focus on "What's Missing":**
- This exercise builds the mindset: *specifications are incomplete until proven comprehensive*
- Students often only see what IS tested, not what ISN'T
- Prompt: "What could go wrong with this function?"

### Common Student Issues

| Issue | Symptom | Intervention |
|-------|---------|--------------|
| Only see happy path | "All scenarios are tested" | "What if someone passes -100?" |
| Confuse specification with implementation | "It just multiplies" | "But what SHOULD happen with bad inputs?" |
| Accept incomplete specs | "These 3 tests are enough" | "How do you know? What's your criteria?" |

### Facilitation Strategy

**Opening prompt (2 min):**
"Look at these assertions. You're the quality engineer - is this product ready to ship?"

**Discussion prompts:**
- "Should the function validate inputs or assume they're valid?"
- "What business rules might apply to tax calculations?"
- "Who found a scenario that should be tested?"

**Mini-debrief (3 min):**
- Share diverse student answers
- Emphasize: no single "right" answer without a complete specification
- Preview: "In Part 2, we'll learn frameworks to find these gaps systematically"

---

## Exercise 1.2: Writing Your First Assertions

### Model Answers

```python
def is_even(n):
    """Return True if n is even, False if odd."""
    return n % 2 == 0

# Comprehensive test suite
assert is_even(2) == True      # Simple even
assert is_even(3) == False     # Simple odd
assert is_even(0) == True      # Zero (even by mathematical definition)
assert is_even(-2) == True     # Negative even
assert is_even(-3) == False    # Negative odd
assert is_even(100) == True    # Large even
assert is_even(1) == False     # Smallest positive odd
assert is_even(-1) == False    # Smallest negative odd
```

### Test Quality Assessment

**Minimal acceptable (4 tests):**
- One positive even
- One positive odd
- Zero
- One negative (even or odd)

**Good coverage (6-8 tests):**
- Multiple positive even/odd
- Zero
- Multiple negative even/odd
- At least one large number

**Excellent coverage (8+ tests):**
- All of above
- Explicit boundary cases (0, 1, -1)
- Systematic coverage of positive/negative × even/odd matrix

### Common Student Issues

| Issue | What you'll see | How to intervene |
|-------|----------------|------------------|
| Forgetting zero | Tests start at 1 | "What's the smallest integer?" |
| Only positives | No negative tests | "Do negative numbers have parity?" |
| Too few tests | 2-3 assertions only | "How do you know these are enough?" |
| Wrong expected values | `assert is_even(3) == True` | "Trace through the logic by hand" |

### Strategic Teaching Moment

**Risk-based thinking introduction:**

Ask: "How many tests do you need for this function?"

Expected student answers: "4? 6? 10?"

Your response: "It depends on the **risk**. For a homework exercise? 4 is fine. For banking software that calculates interest parity? Maybe 20+ with edge cases."

This plants the seed for Part 4's risk assessment framework.

### Facilitation Tips

**Scaffolding questions:**
1. "What categories of numbers exist?" (positive/negative/zero)
2. "Within each category, what types?" (even/odd)
3. "Draw a table - how many combinations?" (2×3 = 6 minimum)

**Check for understanding:**
- Ask a student to explain their test suite
- "Why did you choose these specific numbers?"
- "What scenarios did you decide NOT to test? Why?"

---

# Part 2: Specification Design (30 minutes)

## Exercise 2.1: Leap Year - Systematic Framework Application

This is the **core teaching moment** for systematic test design.

### Step 2: Systematic Framework Teaching

#### Framework 1: Equivalence Partitioning

**Teaching the concept:**

"Equivalence classes are groups of inputs that should behave identically. We test ONE representative from each class, not every possible value."

**Model Answer:**

```python
"""
Equivalence Classes for Leap Year:

Class 1: LEAP - Years divisible by 400
   Examples: 2000, 1600, 2400
   Test with: 2000

Class 2: NOT LEAP - Years divisible by 100 but not 400
   Examples: 1900, 1800, 1700, 2100
   Test with: 1900

Class 3: LEAP - Years divisible by 4 but not 100
   Examples: 2024, 2020, 2004, 1996
   Test with: 2024

Class 4: NOT LEAP - Years not divisible by 4
   Examples: 2023, 2021, 2019, 1999
   Test with: 2023
"""
```

**Teaching dialogue:**

> **You:** "Why test 2000 instead of testing 2000, 2400, 2800, 3200...?"
>
> **Student:** "They all do the same thing?"
>
> **You:** "Exactly! They're in the same equivalence class. One representative is sufficient for that class. We use our limited testing budget on DIFFERENT behaviors."

#### Framework 2: Given/When/Then

**Teaching the concept:**

"This structure forces clarity about test scenarios."

**Model Answer:**

```python
"""
Test Case 1:
Given: A year divisible by 400 (like 2000)
When: I check if it's a leap year
Then: Result should be True

Test Case 2:
Given: A year divisible by 100 but not 400 (like 1900)
When: I check if it's a leap year
Then: Result should be False

Test Case 3:
Given: A year divisible by 4 but not 100 (like 2024)
When: I check if it's a leap year
Then: Result should be True

Test Case 4:
Given: A year not divisible by 4 (like 2023)
When: I check if it's a leap year
Then: Result should be False
"""
```

#### Framework 3: Boundary Analysis

**Teaching the concept:**

"At the 'edges' between categories, test both sides of the boundary."

**Model Answer:**

```python
"""
Boundary at 100 divisibility:
- 1896: True (4-divisible, not 100-divisible)
- 1900: False (100-divisible, not 400-divisible) [BOUNDARY]
- 1904: True (4-divisible, not 100-divisible)

Boundary at 400 divisibility:
- 1600: True (400-divisible) [BOUNDARY]
- 1700: False (100-divisible, not 400-divisible)
- 2000: True (400-divisible) [BOUNDARY]
- 2100: False (100-divisible, not 400-divisible)

Critical boundaries: Years ending in 00
- Every 4th century year (1600, 2000, 2400): LEAP
- Other century years (1700, 1800, 1900): NOT LEAP
"""
```

### Step 3: Test Adequacy Evaluation

**Model Answer:**

```python
"""
Test Adequacy Check:

1. Have I covered all equivalence classes?
   ☑ Yes - 4 classes identified, 1 test each minimum

2. Have I tested boundaries between classes?
   ☑ Yes - Century years (1900, 2000)

3. What's the RISK if this function fails?
   Medium - Incorrect calendar calculations affect scheduling,
   but not life-critical

4. Based on risk, how many tests do I need?
   - Minimum: 4 (one per equivalence class)
   - Recommended: 8-10 (add boundary tests)
   - My decision: 8 tests
     * All 4 equivalence classes
     * Key boundaries (1900, 2000)
     * Recent year validation (2024)

5. Am I over-testing?
   - Testing 2000, 2400, 2800 would be over-testing (same class)
   - Testing 2024, 2020, 2016 would be over-testing (same class)
   - Current plan: appropriate coverage without redundancy
"""
```

### Step 4: Executable Specifications

**Model Answer:**

```python
def is_leap_year(year):
    """Determine if a year is a leap year."""
    pass  # To be implemented by AI

# Equivalence class representatives (minimum viable)
assert is_leap_year(2000) == True   # Class 1: divisible by 400
assert is_leap_year(1900) == False  # Class 2: divisible by 100 not 400
assert is_leap_year(2024) == True   # Class 3: divisible by 4 not 100
assert is_leap_year(2023) == False  # Class 4: not divisible by 4

# Boundary tests (risk-justified additions)
assert is_leap_year(1600) == True   # Boundary: 400-divisible
assert is_leap_year(1700) == False  # Boundary: 100-divisible
assert is_leap_year(1896) == True   # Just before 1900 boundary
assert is_leap_year(1904) == True   # Just after 1900 boundary
```

### Common Student Issues

| Issue | Symptom | Strategic Intervention |
|-------|---------|------------------------|
| Listing years without classes | "Test 2000, 2001, 2002..." | "Group these by behavior first" |
| Missing century boundaries | No 1900/2000 tests | "When does the 100-rule override the 4-rule?" |
| Can't articulate adequacy | "I just picked some years" | "Use the frameworks - classes + boundaries" |
| Over-testing same class | 10 tests all from Class 3 | "These all behave the same. What's different behavior?" |

### Facilitation Strategy

**Introduce frameworks (5 min):**
Use slides or board to show:
1. Equivalence Partitioning diagram
2. Given/When/Then template
3. Boundary analysis visualization

**Guided practice (10 min):**
- Work through Class 1 together as example
- Students complete Classes 2-4 independently
- Pair-share to compare

**Strategic discussion (5 min):**
- "How did frameworks change your thinking?"
- "Which framework felt most useful?"
- "How do you decide between 4 tests vs 40 tests?"

**Common teaching mistake to avoid:**
Don't give them the equivalence classes directly. Guide them to discover:
- "What makes 2000 different from 1900?"
- "What makes 2024 different from 2023?"
- "Can you group years by behavior?"

---

## Exercise 2.2: AI-Assisted Scenario Discovery

### Purpose

This exercise teaches critical AI collaboration: **using AI to brainstorm, but maintaining strategic judgment**.

### Model AI Prompt

```
I'm testing a leap year function with these rules:
- Divisible by 4: leap year
- Divisible by 100: NOT leap year
- Divisible by 400: leap year

What test scenarios should I consider? Include:
- Normal cases
- Edge cases
- Boundary conditions
- Any tricky scenarios I might miss

Organize your response by category and explain WHY each scenario matters.
```

### Typical Strong AI Response

```
Test Scenarios for Leap Year:

NORMAL CASES (Equivalence Classes):
1. Typical leap year (2024, 2020) - divisible by 4, not by 100
2. Typical non-leap year (2023, 2021) - not divisible by 4
3. Century leap year (2000, 1600) - divisible by 400
4. Century non-leap year (1900, 1800) - divisible by 100, not 400

WHY: These represent the four distinct logical paths through the rules.

BOUNDARY CONDITIONS:
5. Year exactly at century mark (1900, 2000, 2100)
6. Years adjacent to century marks (1899, 1901, 1999, 2001)

WHY: Century years are where the exception rules activate.

EDGE CASES:
7. Year 4 (earliest possible leap year)
8. Year 0 (undefined in Gregorian calendar)
9. Negative years (pre-1 CE - calendar system dependent)
10. Very large years (9999, 10000)

WHY: These test assumptions about valid input ranges.

TRICKY SCENARIOS:
11. Year 2100 (often mistaken as leap year)
12. Year 1900 (commonly fails in buggy implementations)

WHY: These frequently expose off-by-one errors in the logic.
```

### Evaluation Framework for Students

**Model Answer:**

```python
"""
AI suggested scenarios:

RELEVANT AND VALUABLE:
- Century years (1900, 2000) - I had these ✓
- Year 2100 test - I MISSED this, good catch
- Adjacent to boundaries (1899, 1901) - I didn't think of this

ALREADY HAD:
- Normal 4-divisible (2024) ✓
- Normal non-divisible (2023) ✓
- 400-divisible (2000) ✓

NEW AND VALUABLE:
- Year 2100 specifically called out as "tricky"
- Adjacent boundary years (1899, 1901)
- Explicit test of year 4

NOT APPLICABLE (for now):
- Year 0, negative years - outside spec scope
- Very large years - low priority for current risk level

DECISION: Add year 2100 test. Consider 1899/1901 if time permits.
"""
```

### Strategic Teaching Points

**Critical Evaluation, Not Blind Acceptance:**

This is where students learn their role as architect.

**Teaching dialogue:**

> **You:** "Did AI suggest everything?"
>
> **Students:** "Yes! So many scenarios!"
>
> **You:** "Should you test all of them?"
>
> **Students:** "I guess?"
>
> **You:** "Wrong. YOU decide. What's the risk? What's the value? AI suggests, YOU choose."

### Common Student Issues

| Issue | What you'll see | How to intervene |
|-------|---------|------------------|
| Accepting everything | "AI said test 20 scenarios, so I will" | "What's the value of testing year 9999?" |
| Ignoring AI completely | "I already did this, skip AI" | "Did AI notice something you missed?" |
| Not comparing | Paste AI response, no evaluation | "Which of these did YOU already have?" |
| Poor prompts | Vague: "give me tests" | "Show me your prompt. Is it specific?" |

### Facilitation Tips

**Before AI interaction (2 min):**
"AI is your brainstorming partner. But YOU are the engineer who decides what gets tested."

**During evaluation (5 min):**
Circulate and check student evaluations:
- "Did you add any AI suggestions? Why those specifically?"
- "Did you reject any AI suggestions? Why?"
- "Compare your evaluation with your neighbor"

**Share examples (3 min):**
- Show example where AI over-suggested (testing 2000, 2400, 2800)
- Show example where AI caught something important (2100)
- Show example of good vs. poor student evaluation

---

**Mini-Debrief for Part 2 (5 min before moving on):**

Gather class attention:

**Questions to ask:**
1. "Raise hand if AI suggested something you missed" (validate AI value)
2. "Raise hand if you rejected an AI suggestion" (validate strategic thinking)
3. "What was most useful: equivalence classes, boundaries, or AI brainstorming?"

**Key message:**
"You just practiced the core AI-first skill: **systematic specification + AI collaboration + strategic judgment**. That's the pattern for everything ahead."

---

# Part 3: The Specify → Generate → Verify Cycle (40 minutes)

## Exercise 3.1: Complete Implementation Workflow

This exercise brings together specification (Part 2) and AI code generation.

### Step 2: AI Implementation Request

**Model Prompt:**

```
Write a Python function is_leap_year(year) that implements these rules:

- Divisible by 4: leap year
- Divisible by 100: NOT leap year
- Divisible by 400: leap year

Make these assertions pass:
assert is_leap_year(2000) == True   # divisible by 400
assert is_leap_year(1900) == False  # divisible by 100 not 400
assert is_leap_year(2024) == True   # divisible by 4 not 100
assert is_leap_year(2023) == False  # not divisible by 4
assert is_leap_year(1600) == True   # divisible by 400
assert is_leap_year(1700) == False  # divisible by 100 not 400

Use only basic Python (if statements, boolean operators).
Keep it simple and readable for beginners.
```

### Typical AI Responses & Quality Evaluation

#### Version A: Boolean Expression (Common)

```python
def is_leap_year(year):
    """Determine if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```

**Quality Evaluation:**

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Correctness | ✓ Pass | All assertions pass |
| Simplicity | ✗ Fail | Complex boolean logic |
| Beginner-friendly | ✗ Fail | Requires understanding `and`/`or` precedence |
| Readable | ~ Partial | Concise but not self-documenting |

**Student Decision:** Request simplification

**Prompt for simplification:**
```
This works but uses complex boolean logic that's hard for beginners.
Can you rewrite using only simple if statements?
Make each rule check separate and clear.
```

#### Version B: If/Return Chain (Better)

```python
def is_leap_year(year):
    """Determine if a year is a leap year."""
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
```

**Quality Evaluation:**

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Correctness | ✓ Pass | All assertions pass |
| Simplicity | ✓ Pass | Only simple modulo and if |
| Beginner-friendly | ✓ Pass | Each rule is one line |
| Readable | ✓ Pass | Rules match spec order |

**Student Decision:** Accept - meets all criteria

#### Version C: If/Elif/Else (Common)

```python
def is_leap_year(year):
    """Determine if a year is a leap year."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
```

**Quality Evaluation:**

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Correctness | ✓ Pass | All assertions pass |
| Simplicity | ~ Partial | Uses `elif` (slightly advanced) |
| Beginner-friendly | ✓ Pass | Still readable |
| Readable | ✓ Pass | Clear structure |

**Student Decision:** Accept (slightly verbose but fine) OR Request simplification to Version B

### Step 4: Code Quality Evaluation

**Model Answers:**

```python
"""
1. Is the code simple enough for a beginner to understand?

   Version A (boolean): NO - requires understanding operator precedence
   Version B (if/return): YES - each line is self-contained
   Version C (elif): MOSTLY - elif is slightly advanced but readable

2. Does it use only basic Python features?

   Version A: NO - complex boolean expressions
   Version B: YES - only if, %, ==, return
   Version C: YES - if/elif/else are basic

3. Is the logic clear and correct?

   All versions: Correct
   Version B: Clearest - rules are visually separated
   Version A: Hardest to verify correctness by inspection

4. Would you have solved it differently? How?

   - I might add comments explaining each rule
   - I might use more descriptive variable names
   - I would prefer Version B for teaching
   - Version A is better for production (more compact)

DECISION: Version B is best for beginner context. Accept without changes.
         OR: If got Version A, request simplification to Version B.
"""
```

### Step 5: Request Simplification

**When to request:**
- Code uses advanced features (list comprehensions, ternary operators, complex boolean logic)
- Code is "clever" rather than clear
- Code would be hard to explain to a beginner
- Student can't trace through it by hand

**How to request:**

**Good simplification prompt:**
```
This works but is too complex for a beginner.
Can you rewrite it using only simple if statements?
Avoid combining conditions with 'and'/'or'.
Make each rule check one condition at a time.
Prioritize readability over brevity.
```

**Poor simplification prompt:**
```
Make it simpler.
```
*(Too vague - AI might make superficial changes)*

### Common Student Issues

| Issue | Symptom | Intervention |
|-------|---------|--------------|
| Accepting Version A without question | "It works!" | "Can YOU explain line 2 to a beginner?" |
| Not running tests | Assume correctness | "How do you know it works?" |
| Confusing concise with simple | "Short is better" | "Is short always clearer for learning?" |
| Missing rule order bug | Wrong 2000/1900 results | "Trace year 1900 by hand" |
| Not requesting simplification | Accepting complex code | "Is there a simpler way? Ask AI!" |

### Strategic Teaching Points

**Key Conceptual Shift:**

> "In traditional coding class, you'd be penalized for 'too simple' code.
>
> In AI-first coding, **simplicity is a strategic choice**.
>
> You CONTROL the complexity level by how you prompt AI."

**Teaching dialogue:**

> **You:** "Who got the boolean expression version?"
>
> *(Hands raise)*
>
> **You:** "Did you accept it?"
>
> **Student:** "Yes, it works."
>
> **You:** "Can you explain the `and`/`or` precedence to someone who's never coded?"
>
> **Student:** "Um... not really."
>
> **You:** "Then it's not simple enough. Ask AI to simplify. YOU set the quality bar."

### Facilitation Strategy

**Before AI generation (2 min):**
- "You're about to see AI's implementation"
- "Your job: verify correctness AND evaluate simplicity"
- "If too complex, request simpler version"

**During verification (10 min):**
Circulate and ask:
- "Did all assertions pass?" (correctness)
- "Can you explain each line?" (understanding)
- "Is this simple enough for a beginner?" (quality judgment)

**Group discussion (5 min):**
- "Show of hands: who got Version A?" *(boolean expression)*
- "Who requested simplification?" *(validate this choice)*
- Share simplified versions on screen
- Compare: which is clearest?

**Key teaching moment:**
Pull up two versions side-by-side:
```python
# Version A
return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Version B
if year % 400 == 0:
    return True
if year % 100 == 0:
    return False
if year % 4 == 0:
    return True
return False
```

Ask: "Which would YOU rather debug at 2am?"

---

# Part 4: Test Design Practice (40 minutes)

## Exercise 4.1: Strategic Test Design with Risk Analysis

This is where systematic frameworks from Part 2 are applied with **risk-based decision making**.

### Step 1: Risk Assessment

**Model Answer:**

```python
"""
Risk Analysis:

1. What happens if this function fails?

   Security implications:
   - Weak passwords accepted → user accounts vulnerable to attack
   - Strong passwords rejected → users frustrated, may bypass security
   - Inconsistent validation → unpredictable user experience

   User experience impact:
   - HIGH - users get locked out if false negative
   - HIGH - users' accounts hacked if false positive

   Business impact:
   - Reputational damage from security breach
   - Support costs from validation errors
   - Potential regulatory compliance issues (GDPR, etc.)

2. Risk level: ☑ High

3. Based on this risk, my testing strategy should be:
   ☑ Comprehensive - all edge cases, stress tests

   Justification:
   - Security-critical function
   - High cost of failure (both false positive and false negative)
   - Need confidence in all edge cases
   - Worth the investment in thorough testing
"""
```

**Teaching point:**

Students often default to "medium risk" for everything. Push them:

> "What if this password validator protects a banking app with 1 million users?"
>
> "What if it protects your personal blog?"
>
> Different contexts → different risk → different testing strategies.

### Step 2: Equivalence Partitioning

**Model Answer:**

```python
"""
Equivalence Classes:

VALID class (all requirements met):
- Example: "Pass123!"
  (8+ chars, has uppercase, has number, has special)

INVALID classes (each requirement violation):

Class 1: Too short (< 8 chars)
- Example: "Pas12!" (only 6 chars, otherwise valid)
- Why test: Length check is independent validation

Class 2: Missing uppercase
- Example: "pass123!" (8 chars, no uppercase, has number, has special)
- Why test: Case-sensitive validation different logic

Class 3: Missing number
- Example: "Password!" (8 chars, has uppercase, no number, has special)
- Why test: Digit check is separate logic

Class 4: Missing special character
- Example: "Password1" (8 chars, has uppercase, has number, no special)
- Why test: Special char validation likely separate

Class 5: Multiple violations
- Example: "pass" (too short, no uppercase, no number, no special)
- Why test: Ensure all validations run, not just first failure

Do I need to test EVERY invalid combination?
Decision: NO

Reasoning:
- 4 requirement violations
- Could test all combinations: 2^4 = 16 tests (overkill)
- Test ONE example per violation class (4 tests)
- Plus ONE example of multiple violations (1 test)
- Plus boundary cases
- Total: ~10-12 tests adequate for high risk
"""
```

**Strategic teaching point:**

> "You COULD test every combination of violations. That's 16 tests.
>
> Is it worth it? For high-risk, maybe. For medium-risk, probably not.
>
> **You** make that trade-off decision based on risk vs. effort."

### Step 3: Boundary Analysis

**Model Answer:**

```python
"""
Key boundaries:

Length boundary (8 characters):
- 7 chars (just under): "Pass12!" → False
- 8 chars (exactly at): "Pass123!" → True
- 9 chars (just over): "Pass1234!" → True

WHY CRITICAL: Off-by-one errors common in length checks
(< vs <=, > vs >=)

Other boundaries worth testing:

1. Empty string:
   - "" → False
   - WHY: Edge case, may cause crashes if not handled

2. Exactly minimum of each requirement:
   - "P1!aaaaa" (1 upper, 1 number, 1 special, 8 chars) → True
   - WHY: Tests "at least one" logic isn't "at least two"

3. Very long password:
   - "Pass123!" * 20 (160 chars) → True
   - DECISION: Low priority unless spec limits length

4. Only special characters:
   - "!@#$%^&*" → False (no uppercase, no number)
   - WHY: Edge case, tests multiple violations

5. Mixed requirements at boundary:
   - "Passwor!" (8 chars but no number) → False
   - WHY: Boundary + violation interaction
"""
```

### Step 4: Test Adequacy Decision

**Model Answer:**

```python
"""
How many tests is enough?

Minimum viable: 6 tests
- 1 valid (all requirements)
- 4 invalid (one per requirement violation)
- 1 boundary (exactly 8 chars)

My plan: 12 tests

Why this number?
- HIGH RISK security function justifies thoroughness
- 1 valid happy path
- 4 equivalence classes for invalid (one per violation)
- 3 boundary tests (7, 8, 9 chars)
- 2 edge cases (empty, multiple violations)
- 2 interaction tests (boundary + violation)

Could I get the same confidence with fewer tests?
- Possibly drop to 8-9 for MEDIUM risk
- Cannot drop below 6 (inadequate coverage)
- Current plan: appropriate for HIGH risk

What am I NOT testing, and why is that OK?
- NOT testing every password length 8-100 (same equivalence class)
- NOT testing all special char combinations (same logic)
- NOT testing very long passwords >100 chars (low probability)
- NOT testing Unicode/emoji (out of current spec scope)
- NOT testing all 16 combinations of violations (redundant)

These omissions are justified by:
- Equivalence class reasoning (representative examples)
- Risk vs. effort trade-off
- Spec scope boundaries
"""
```

**This is a critical metacognitive moment.**

Students must **justify** their testing decisions, not just make them.

### Step 5: Write Specifications

**Model Answer:**

```python
def is_strong_password(password):
    """Validate password strength."""
    pass  # To be implemented

# === VALID PASSWORDS (Equivalence Class: All requirements met) ===
assert is_strong_password("Pass123!") == True   # Canonical valid
assert is_strong_password("MyP@ssw0rd") == True # Different special char
assert is_strong_password("UPPER123!") == True  # All caps valid

# === INVALID - TOO SHORT ===
assert is_strong_password("Pass12!") == False   # 7 chars
assert is_strong_password("") == False          # Empty (edge case)

# === INVALID - MISSING UPPERCASE ===
assert is_strong_password("pass123!") == False  # All lowercase

# === INVALID - MISSING NUMBER ===
assert is_strong_password("Password!") == False # No digit

# === INVALID - MISSING SPECIAL CHARACTER ===
assert is_strong_password("Password1") == False # No special char

# === BOUNDARY - LENGTH ===
assert is_strong_password("Abcdef1!") == True   # Exactly 8 chars

# === EDGE CASE - MULTIPLE VIOLATIONS ===
assert is_strong_password("pass") == False      # Too short + missing all

# === EDGE CASE - MINIMUM REQUIREMENTS ===
assert is_strong_password("P1!aaaaa") == True   # Exactly 1 of each required

# === INTERACTION - BOUNDARY + VIOLATION ===
assert is_strong_password("Passwor!") == False  # 8 chars but no number
```

**Note comments group tests by purpose.** This is professional test organization.

---

## Exercise 4.2: AI Implementation and Evaluation

### Typical AI Implementation (Good Quality)

```python
def is_strong_password(password):
    """Validate password strength."""
    # Check length
    if len(password) < 8:
        return False

    # Check for at least one uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break

    # Check for at least one number
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
            break

    # Check for at least one special character
    has_special = False
    special_chars = "!@#$%^&*"
    for char in password:
        if char in special_chars:
            has_special = True
            break

    # All requirements must be met
    return has_upper and has_number and has_special
```

### Alternative AI Implementation (More Concise)

```python
def is_strong_password(password):
    """Validate password strength."""
    if len(password) < 8:
        return False

    has_upper = any(c.isupper() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)

    return has_upper and has_number and has_special
```

### Strategic Evaluation Framework

**Model Answer:**

```python
"""
Strategic Evaluation:

1. Does it pass all your assertions?

   ✓ YES - All 12 assertions pass

   Verified by running code and checking each assertion individually.

2. Code Simplicity:

   - Can a beginner understand this?
     First version: YES - explicit loops, clear logic
     Second version: MAYBE - requires understanding `any()` and generator expressions

   - Does it use only basic Python constructs?
     First version: YES - for loops, if statements, string methods
     Second version: NO - uses `any()` and generator expressions (advanced)

   - Is there a simpler approach?
     First version is already quite simple.
     Could be more concise but that's not our goal.

3. Did you find any bugs or issues?

   Potential issue: special_chars definition
   - "!@#$%^&*" is hardcoded
   - Should it be a constant?
   - Are these the ONLY valid special chars?
   - Spec says "!@#$%^&*" so this is correct per spec

   No actual bugs found after testing all assertions.

4. Test Coverage:

   - Are there scenarios you didn't test?
     * Password with multiple special chars ("Pass1@#!")
     * Password with spaces ("Pass 123!")
     * Unicode characters ("Pässw0rd!")

   - Are they worth testing (risk vs. effort)?
     * Multiple special chars: NO - same logic as one special char
     * Spaces: MAYBE - unclear if spaces count toward requirements
     * Unicode: NO - out of spec scope

   - Decision: Add tests / Leave as-is
     DECISION: Leave as-is
     JUSTIFICATION: Current coverage adequate for spec, no ambiguities found

5. Should you request simplification?

   First version: NO - already beginner-friendly
   Second version: YES - too advanced

   Prompt to use: "Make this simpler using only basic if statements and for loops.
                   Avoid any(), generator expressions, and other advanced features."

"""
```

### Common Student Issues

| Issue | Symptom | Intervention |
|-------|---------|--------------|
| Not running tests | "Looks correct" | "How do you KNOW without running?" |
| Accepting complex code | "It's shorter!" | "Can you explain `any()` to a beginner?" |
| No test gap analysis | "Tests are complete" | "What scenarios aren't tested?" |
| Can't justify adequacy | "Seems like enough" | "Use your frameworks - what's the risk?" |
| Finding issues but not acting | "Code has problems... but passes tests" | "What test would catch that problem?" |

### Facilitation Strategy

**Critical evaluation checkpoint (10 min):**

Walk around. For each student, ask ONE question:

- "Does it pass your tests?" (verification)
- "Can you explain line X to me?" (understanding)
- "Is this simple enough for your target audience?" (quality judgment)
- "What scenarios are you NOT testing?" (adequacy)
- "Should you request a simpler version?" (strategic decision)

**Group discussion (5 min):**

"Let's compare implementations. Who got a version using `any()`?"

*Show both versions side-by-side*

"Which is simpler for a beginner? Remember: YOU decide the quality bar."

**Key teaching moment:**

> "You all have working code. But 'working' isn't enough.
>
> As the architect, you must evaluate:
> - Correctness (tests)
> - Simplicity (readability)
> - Coverage (adequacy)
>
> This is strategic thinking, not just coding."

---

**Mini-Debrief for Part 4 (5 min before moving on):**

**Questions:**
1. "How many tests did you write? Raise hand: <8, 8-12, >12"
2. "Who made a conscious decision to STOP testing? Why?"
3. "Who requested AI to simplify code?"

**Key message:**
"You just practiced risk-based decision making. Some of you wrote 8 tests, some wrote 15. Both can be RIGHT if you can justify it based on risk. That's professional judgment."

---

# Part 5: Regression Testing & Bug Prevention (30 minutes)

## Paradigm Shift: Specification-First Bug Fixing

**Traditional debugging:**
1. See bug
2. Add print statements
3. Find root cause
4. Fix manually
5. Hope it works

**AI-first debugging:**
1. Write failing test that captures bug
2. Specify fix to AI
3. Verify fix passes test
4. Keep test for regression prevention

### Exercise 5.1: Specification-First Bug Fixing

**Teaching Setup (2 min):**

> "You're doing a code review. You discover this buggy code in production.
>
> Traditional approach: open IDE, add print statements, manually fix.
>
> AI-first approach: write test, specify fix, verify.
>
> Let's try the AI-first way."

### Step 1: Write Failing Test

**Model Answer:**

```python
# First, understand what SHOULD happen:
# Input: [2, -1, 4, -3]
# Positive numbers only: [2, 4]
# Sum: 2 + 4 = 6
# Count: 2
# Average: 6 / 2 = 3.0

def average_positive(numbers):
    """Calculate average of positive numbers only."""
    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
        count += 1  # BUG: increments for ALL numbers
    return total / count

# Write the assertion that DEMONSTRATES the bug:
result = average_positive([2, -1, 4, -3])
print(f"Expected: 3.0, Got: {result}")  # Got: 1.5

assert average_positive([2, -1, 4, -3]) == 3.0  # FAILS
```

**Strategic teaching point:**

> "Notice: we don't ADD print statements to find the bug.
>
> We SPECIFY the correct behavior as a test.
>
> The test documents the bug. Now we give it to AI to fix."

### Step 2: Specify the Bug to AI

**Model Prompt:**

```
The function average_positive should calculate the average of ONLY positive numbers,
ignoring negative numbers entirely.

Current behavior:
For input [2, -1, 4, -3], it returns 1.5

Expected behavior:
For input [2, -1, 4, -3], it should:
- Consider only positive numbers: [2, 4]
- Calculate average: (2 + 4) / 2 = 3.0
- Return 3.0

Here are the tests that should pass:
assert average_positive([2, -1, 4, -3]) == 3.0
assert average_positive([1, 2, 3]) == 2.0
assert average_positive([10, -5, 20, -10, 30]) == 20.0

Please fix the function to pass these tests.
Keep the solution simple - use only basic Python.
Explain what was wrong and how you fixed it.
```

**Teaching point on prompt quality:**

> "Notice what we included:
> - Current wrong behavior
> - Expected correct behavior
> - Multiple test cases
> - Simplicity constraint
>
> This is a COMPLETE specification. AI has everything it needs."

### Step 3: AI Fix & Verification

**Typical AI Response:**

```
The bug was in the count increment. It was counting ALL numbers, not just positive ones.

The count should only increment when we add a number to the total.

Fixed version:

def average_positive(numbers):
    """Calculate average of positive numbers only."""
    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
            count += 1  # Moved inside the if block

    # Handle edge case: no positive numbers
    if count == 0:
        return 0

    return total / count

Explanation:
- Original code: count incremented on every iteration (all numbers)
- Fixed code: count only increments when num > 0 (positive numbers only)
- Added edge case handling: if no positive numbers, return 0 instead of dividing by zero
```

**Verification:**

```python
# Paste AI's corrected version:
def average_positive(numbers):
    """Calculate average of positive numbers only."""
    total = 0
    count = 0
    for num in numbers:
        if num > 0:
            total += num
            count += 1
    if count == 0:
        return 0
    return total / count

# Run test assertions to verify:
assert average_positive([2, -1, 4, -3]) == 3.0  # PASSES ✓
assert average_positive([1, 2, 3]) == 2.0        # PASSES ✓
assert average_positive([10, -5, 20, -10, 30]) == 20.0  # PASSES ✓

print("All tests passed! Bug fixed.")
```

### Step 4: Add Edge Case Tests

**Model Answer:**

```python
"""
Additional scenarios to test:

1. All negative numbers: [-1, -2, -3]
   Expected behavior: No positive numbers
   Return: 0 (or could raise error - depends on spec)
   Rationale: Edge case, might cause division by zero

2. Empty list: []
   Expected behavior: No numbers at all
   Return: 0 (or could raise error)
   Rationale: Edge case, will definitely cause division by zero

3. Mix with zero: [0, 1, 2]
   Expected behavior: 0 is not positive, ignore it
   Return: (1 + 2) / 2 = 1.5
   Rationale: Boundary case, 0 is neither positive nor negative

4. Single positive: [5]
   Expected behavior: Average of one number is itself
   Return: 5.0
   Rationale: Minimum positive case

5. Very large numbers: [1000000, -999999, 2000000]
   Expected behavior: (1000000 + 2000000) / 2 = 1500000
   Rationale: Ensure no overflow issues
"""

# Write assertions for critical edge cases:
assert average_positive([-1, -2, -3]) == 0      # All negative
assert average_positive([]) == 0                # Empty
assert average_positive([0, 1, 2]) == 1.5       # With zero
assert average_positive([5]) == 5.0             # Single positive
```

**Strategic teaching point:**

> "The original bug fix passed our initial tests.
>
> But what about edge cases?
>
> ALWAYS ask: 'What weird inputs might break this?'
>
> That's defensive specification."

### Common Student Issues

| Issue | Symptom | Intervention |
|-------|---------|--------------|
| Trying to debug manually | Adding print statements | "Stop. Write the test FIRST." |
| Vague bug specification | "Fix the bug" prompt | "Be specific: what should happen?" |
| Not considering edge cases | Only testing original bug case | "What if all numbers are negative?" |
| Accepting fix without verification | Trust AI blindly | "How do you KNOW it's fixed?" |

---

## Exercise 5.2: AI-Driven Bug Investigation

### Step 1: Write Failing Test Specifications

**Model Answer:**

```python
"""
Test cases that should pass but currently fail:

1. All negative numbers:
   assert find_max([-5, -2, -8, -1]) == -1
   Currently returns: 0 ✗
   Should return: -1 ✓

2. Single negative number:
   assert find_max([-10]) == -10
   Currently returns: 0 ✗
   Should return: -10 ✓

3. Mix of negative and zero:
   assert find_max([-5, 0, -2]) == 0
   Currently returns: 0 ✓ (but for wrong reason!)
   Should return: 0 ✓

4. All zeros:
   assert find_max([0, 0, 0]) == 0
   Currently returns: 0 ✓
   Should return: 0 ✓

Critical test: #1 (all negative numbers)
This exposes the initialization bug most clearly.
"""
```

### Step 2: Prompt AI to Fix Based on Tests

**Model Prompt:**

```
This find_max function has a bug. It returns 0 for lists of all negative numbers
when it should return the largest (least negative) number.

Current broken behavior:
find_max([-5, -2, -8, -1]) returns 0 (wrong)

Expected behavior:
find_max([-5, -2, -8, -1]) should return -1 (the maximum)

Here's the current code:
def find_max(numbers):
    """Find the maximum number in a list."""
    max_num = 0
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

Make these assertions pass:
assert find_max([-5, -2, -8, -1]) == -1
assert find_max([3, 1, 4, 1, 5]) == 5
assert find_max([-10]) == -10

Explain:
1. What's wrong with the current code
2. Why it fails for all-negative lists
3. How to fix it

Then provide the corrected code using only basic Python.
Keep it simple for beginners.
```

### Step 3: AI Explanation & Fix

**Typical Good AI Response:**

```
What's wrong:
The bug is in the initialization: max_num = 0

Why it fails:
When all numbers are negative:
- We compare each number to max_num (which is 0)
- -5 > 0? No
- -2 > 0? No
- -8 > 0? No
- -1 > 0? No
- max_num never gets updated, stays 0
- We return 0, which isn't even in the list!

How to fix:
Initialize max_num to the first element of the list instead of 0.
This way, we're guaranteed to start with an actual value from the list.

Fixed code:

def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:  # Handle empty list
        return None  # or raise ValueError("Empty list")

    max_num = numbers[0]  # Start with first element
    for num in numbers[1:]:  # Start loop from second element
        if num > max_num:
            max_num = num
    return max_num

Alternative (still simple):

def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None

    max_num = numbers[0]
    for num in numbers:  # Can include numbers[0] in loop, won't matter
        if num > max_num:
            max_num = num
    return max_num
```

### Step 4: Verify and Reflect

**Model Answer:**

```python
# Paste the fixed function:
def find_max(numbers):
    """Find the maximum number in a list."""
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Run all test assertions:
assert find_max([-5, -2, -8, -1]) == -1  # PASSES ✓
assert find_max([3, 1, 4, 1, 5]) == 5    # PASSES ✓
assert find_max([-10]) == -10             # PASSES ✓

# Additional tests:
assert find_max([0, 0, 0]) == 0          # PASSES ✓
assert find_max([-5, 0, -2]) == 0        # PASSES ✓

# Reflection:
"""
How does the AI-first approach compare to manual debugging?

AI-FIRST APPROACH:
✓ Faster - wrote test, got explanation and fix in minutes
✓ Educational - AI explained WHY it failed
✓ Documented - test remains as regression prevention
✓ Systematic - forced me to think about test cases first
~ Required clear problem specification

MANUAL DEBUGGING:
~ Slower - would need to add prints, trace execution
~ Less learning - might fix without fully understanding
✗ No documentation - fix is done, move on
✗ Reactive - only fix the immediate bug

WHEN TO USE WHICH:
- AI-first: Most bugs, especially logic errors
- Manual: When you need to deeply understand code,
         or when bug is very subtle/context-specific

BIGGEST BENEFIT:
Writing the test FIRST forced me to think clearly about
what "correct" means. The test is now permanent documentation.

BIGGEST CHALLENGE:
Need to specify the bug clearly. Vague prompts get vague fixes.
"""
```

### Strategic Teaching Moment

**Pull the class back together for this (3 min):**

> "Show of hands:
> - Who wrote the failing test before asking AI? *(Should be everyone)*
> - Who asked AI to EXPLAIN before fixing? *(Validate this approach)*
>
> This is the key difference from traditional debugging:
> **Test first, specification-driven, AI-assisted.**
>
> You're not just fixing bugs, you're PREVENTING them from coming back."

### Common Student Issues

| Issue | Symptom | Intervention |
|-------|---------|--------------|
| Skipping test writing | Go straight to AI for fix | "Stop - write the test first" |
| Accepting code without explanation | Paste fix, move on | "Do you understand WHY it was wrong?" |
| Not testing edge cases | Only test the reported bug | "What about empty list?" |
| Can't articulate comparison | "AI is just faster" | "But what did YOU learn?" |

---

# Part 6: Integration Exercise (45 minutes)

This is the **capstone** where all frameworks come together.

## Exercise 6.1: Complete Feature Development

### Step 1: Apply Complete Testing Framework

Students should independently apply ALL frameworks learned:
1. Risk assessment
2. Equivalence partitioning
3. Boundary analysis
4. Test adequacy decisions

#### A. Risk Assessment - Model Answer

```python
"""
Risk Analysis:

1. What's the consequence if this function fails?

   Educational context:
   - Student gets wrong grade on transcript
   - Could affect GPA, scholarships, graduation

   Automated system:
   - Mass grading errors
   - Student appeals, administrative overhead
   - Institutional credibility damage

2. Risk level: ☑ High

   Justification:
   - Directly affects student outcomes
   - High visibility if wrong
   - Difficult to catch errors after deployment
   - Legal/policy implications

3. Testing approach based on risk: ☑ Comprehensive

   Strategy:
   - Test ALL boundaries (89/90, 79/80, etc.)
   - Test edge cases (0, 100, out of range)
   - Test invalid inputs
   - Test decimal scores if spec allows
"""
```

#### B. Equivalence Classes - Model Answer

```python
"""
Equivalence Classes:

Class 1: Grade A (90-100)
   Representative: 95
   Boundary representatives: 90, 100

Class 2: Grade B (80-89)
   Representative: 85
   Boundary representatives: 80, 89

Class 3: Grade C (70-79)
   Representative: 75
   Boundary representatives: 70, 79

Class 4: Grade D (60-69)
   Representative: 65
   Boundary representatives: 60, 69

Class 5: Grade F (<60)
   Representative: 50
   Boundary representatives: 0, 59

Invalid Classes:
Class 6: Out of range high (>100)
   Representative: 101, 150

Class 7: Out of range low (<0)
   Representative: -1, -50

Class 8: Invalid type
   Representative: "ninety", None, [90]
"""
```

#### C. Boundaries - Model Answer

```python
"""
Critical boundaries (where behavior changes):

Boundary between F and D (60):
- Test 59: expect F
- Test 60: expect D
- Test 61: expect D

Boundary between D and C (70):
- Test 69: expect D
- Test 70: expect C
- Test 71: expect C

Boundary between C and B (80):
- Test 79: expect C
- Test 80: expect B
- Test 81: expect B

Boundary between B and A (90):
- Test 89: expect B
- Test 90: expect A
- Test 91: expect A

Range boundaries (0-100):
- Test 0: expect F (minimum)
- Test 100: expect A (maximum)
- Test -1: expect error or invalid
- Test 101: expect error or invalid

WHY THESE ARE CRITICAL:
Off-by-one errors (> vs >=) would be caught by boundary tests.
This is the MOST COMMON bug in grading functions.
"""
```

#### D. Test Adequacy - Model Answer

```python
"""
Test Adequacy Decision:

Minimum tests needed: 5 (one per grade equivalence class)

Boundary tests needed: 10 (each grade boundary: just below, at, just above)
But actually: 8 boundary tests (at each boundary threshold)

Edge case tests: 4
- Minimum (0)
- Maximum (100)
- Out of range high (101)
- Out of range low (-1)

Total planned tests: 17

Breakdown:
- 5 equivalence class representatives (mid-range of each grade)
- 8 boundary tests (exact thresholds)
- 4 edge cases (range limits, out of range)

Justification:
HIGH RISK function requires comprehensive testing.
Boundaries are critical (most likely bugs).
Edge cases ensure robustness.

Could I reduce?
- For MEDIUM risk: could drop to 12 (skip some redundant boundaries)
- For LOW risk: could drop to 8 (one per class + critical boundaries)
- Current plan: appropriate for HIGH risk educational context
"""
```

### Step 2: Write Specifications - Model Answer

```python
def calculate_grade(score):
    """Convert numeric score to letter grade."""
    pass

# === EQUIVALENCE CLASS REPRESENTATIVES ===
assert calculate_grade(95) == "A"   # Mid-range A
assert calculate_grade(85) == "B"   # Mid-range B
assert calculate_grade(75) == "C"   # Mid-range C
assert calculate_grade(65) == "D"   # Mid-range D
assert calculate_grade(50) == "F"   # Mid-range F

# === CRITICAL BOUNDARIES (High Risk) ===
assert calculate_grade(90) == "A"   # A/B boundary (at)
assert calculate_grade(89) == "B"   # A/B boundary (just below)

assert calculate_grade(80) == "B"   # B/C boundary (at)
assert calculate_grade(79) == "C"   # B/C boundary (just below)

assert calculate_grade(70) == "C"   # C/D boundary (at)
assert calculate_grade(69) == "D"   # C/D boundary (just below)

assert calculate_grade(60) == "D"   # D/F boundary (at)
assert calculate_grade(59) == "F"   # D/F boundary (just below)

# === RANGE BOUNDARIES ===
assert calculate_grade(100) == "A"  # Maximum valid score
assert calculate_grade(0) == "F"    # Minimum valid score

# === EDGE CASES (depends on spec) ===
# Option 1: Raise exceptions for invalid
# assert calculate_grade(101) raises ValueError
# assert calculate_grade(-1) raises ValueError

# Option 2: Return error indicator
# assert calculate_grade(101) == "Invalid"
# assert calculate_grade(-1) == "Invalid"

# Decision needed: How to handle out-of-range scores?
```

**Teaching note:**

Students should recognize they need to make a SPECIFICATION DECISION about out-of-range scores. This is realistic - specs are often incomplete.

### Step 3: AI Implementation - Model Answer

**Good Prompt:**

```
Write a Python function calculate_grade(score) that converts a numeric score
to a letter grade using these rules:

- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: below 60

Make these assertions pass:
[paste all assertions here]

For scores outside 0-100 range, raise a ValueError with a descriptive message.

Use only basic Python (if statements, comparisons).
Keep it simple and readable for beginners.
No complex logic, no libraries.
```

**Typical Good AI Response:**

```python
def calculate_grade(score):
    """Convert numeric score to letter grade."""
    # Validate input range
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")

    # Determine grade
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
```

### Step 4: Strategic Evaluation - Model Answer

```python
"""
Strategic Evaluation:

1. Do all tests pass?

   ✓ YES - all 15 assertions pass

   Verification process:
   - Ran each assertion individually
   - Tested boundary cases carefully
   - Verified error handling for out-of-range

2. Simplicity check:

   - Could a beginner understand this without help?
     ✓ YES - straightforward if/elif chain

   - Explain to beginner test:
     "If score is 90 or higher, grade is A.
      If score is 80-89, grade is B.
      If score is 70-79, grade is C.
      If score is 60-69, grade is D.
      Otherwise, grade is F."

     ✓ Easy to explain, easy to understand

3. Test adequacy review:

   - Given HIGH risk level, are my tests sufficient?
     ✓ YES - all boundaries tested, edge cases covered

   - Am I over-testing (wasting effort on low-value tests)?
     ✗ NO - each test serves a distinct purpose
     All boundaries are critical for correctness
     Edge cases prevent crashes

   - Am I under-testing (missing critical scenarios)?
     Potential gap: decimal scores (89.5, 90.1)
     Decision: Add if spec requires precision
     Current spec says "numeric" so assume decimals possible

     Add tests:
     assert calculate_grade(89.5) == "B"  # Just below 90
     assert calculate_grade(90.0) == "A"  # Exactly 90.0
     assert calculate_grade(89.9) == "B"  # Very close to 90

4. What would you improve?

   In the code:
   - ✓ Already simple and clear
   - Could add type checking (isinstance(score, (int, float)))
   - Could add docstring examples

   In the tests:
   - Add decimal score tests (89.5, 79.9, etc.)
   - Add test for score = 100.0 (float)
   - Consider adding tests with named test cases for documentation

   In the process:
   - Document specification decision (how to handle out-of-range)
   - Create a test organization structure (group by category)
   - Consider using a testing framework (pytest) for better output
"""
```

### Step 5: Add a Bug Test - Model Answer

**Scenario: Discovered off-by-one error**

```python
"""
Bug Discovery Scenario:

During manual review, you notice the boundary logic.
You ask: "What if AI used > instead of >=?"

This would cause:
- Score of exactly 90 to return "B" instead of "A"
- Score of exactly 80 to return "C" instead of "B"
- etc.

Let's write a test that would catch this bug:
"""

# === REGRESSION TEST FOR OFF-BY-ONE BUG ===
def calculate_grade_buggy(score):
    """Buggy version with > instead of >="""
    if score < 0 or score > 100:
        raise ValueError(f"Score must be between 0 and 100, got {score}")

    if score > 90:  # BUG: should be >= 90
        return "A"
    elif score > 80:  # BUG: should be >= 80
        return "B"
    elif score > 70:  # BUG: should be >= 70
        return "C"
    elif score > 60:  # BUG: should be >= 60
        return "D"
    else:
        return "F"

# These tests would FAIL with buggy version:
try:
    assert calculate_grade_buggy(90) == "A"
    print("Test passed")
except AssertionError:
    print("BUG CAUGHT: calculate_grade_buggy(90) returned 'B', expected 'A'")

try:
    assert calculate_grade_buggy(80) == "B"
    print("Test passed")
except AssertionError:
    print("BUG CAUGHT: calculate_grade_buggy(80) returned 'C', expected 'B'")

"""
Key insight:
Boundary tests (exactly 90, exactly 80, etc.) are CRITICAL.
They catch the most common bug in grading logic.

This is why we spent so much time on boundary analysis!
"""

# Alternative: Write test FIRST, then it would prevent the bug
# This demonstrates Test-Driven Development (TDD) concept
```

**Strategic teaching moment:**

> "This exercise demonstrates why we emphasize boundaries.
>
> ONE character difference (> vs >=) breaks four test cases.
>
> Without boundary tests, this bug ships to production.
>
> This is the power of systematic test design."

### Common Student Issues

| Issue | Symptom | Intervention |
|-------|---------|--------------|
| Skipping risk assessment | Jump straight to tests | "Stop - assess the risk FIRST" |
| Missing boundaries | Only test mid-ranges | "Where does behavior CHANGE?" |
| Can't justify test count | "I wrote some tests" | "Use your frameworks - show me the analysis" |
| Accepting complex AI code | Advanced features used | "Can a beginner read this?" |
| No specification decisions | Unclear out-of-range handling | "What SHOULD happen for 101?" |

### Facilitation Strategy

**This is a long exercise (45 min) - structure it:**

**Phase 1: Planning (15 min)**
- Students work independently on Steps 1-2
- Circulate and check risk assessments
- Check equivalence class identification
- Verify test adequacy justifications

**Phase 2: Implementation (15 min)**
- Students prompt AI and verify
- Check code simplicity
- Check test passage

**Phase 3: Evaluation (10 min)**
- Students complete strategic evaluation
- Reflect on process

**Phase 4: Share & Debrief (5 min)**
- "How many tests did you write? Why that number?"
- "Who requested simplification? What was too complex?"
- "What specification decisions did you make?"

---

# Part 7: Reflection and Synthesis (15 minutes)

## Strategic Reflection - Model Answers

### Question 1: Strategic Thinking

**What was most challenging about deciding WHAT to test (vs. HOW to test)?**

**Strong answers include:**
- "Knowing when I had 'enough' tests - there's no obvious stopping point"
- "Deciding between testing every combination vs. representative examples"
- "Balancing thoroughness with practical constraints (time, effort)"
- "Making risk-based decisions - justifying why 10 tests, not 5 or 20"
- "Identifying equivalence classes - grouping inputs by behavior"

**Weak answers (redirect):**
- "Writing the test syntax" ← That's HOW, not WHAT
- "Understanding the function" ← Missing the strategic dimension

### Question 2: AI Collaboration

**How did your role as "architect" differ from traditional coding?**

**Strong answers include:**
- "I focused on WHAT needs to happen, not HOW to code it"
- "I spent more time thinking about specifications and less time debugging syntax"
- "I made decisions about simplicity and quality, AI just implemented"
- "I had to clearly communicate requirements - vague prompts failed"
- "I evaluated AI's work critically, didn't just accept it"

**What decisions did YOU make vs. what did AI do?**

**Strong answers include:**
```
MY DECISIONS:
- What to test (risk assessment, equivalence classes)
- How many tests (adequacy judgment)
- What's "simple enough" (complexity evaluation)
- When to request improvements (quality control)

AI'S ROLE:
- Suggest scenarios I might miss (brainstorming)
- Implement code from specifications (coding)
- Explain bugs and fixes (education)
- Simplify complex solutions (refactoring)
```

### Question 3: Test Design Frameworks

**Which framework was most useful?**

**Common valuable answers:**

**"Equivalence Partitioning"**
- "Helped me avoid redundant tests (testing 2000, 2400, 2800)"
- "Made me think about categories of behavior, not individual values"
- "Answered the question: which tests add VALUE vs. which are redundant"

**"Boundary Analysis"**
- "Caught bugs I wouldn't have thought of (89 vs 90)"
- "Made testing systematic - test both sides of each boundary"
- "This is where bugs actually hide"

**"Given/When/Then"**
- "Forced me to think clearly about each test scenario"
- "Made my test intentions explicit"
- "Helped me communicate test purpose to others"

**"Risk Assessment"**
- "Justified my testing decisions"
- "Helped me decide when to stop testing"
- "Made me think about real-world consequences"

### Question 4: Test Adequacy

**How did you decide when you had "enough" tests?**

**Strong answers demonstrate framework application:**
- "I covered all equivalence classes (one representative each)"
- "I tested all critical boundaries"
- "I based it on risk - high risk = more comprehensive testing"
- "I stopped when additional tests were redundant (same behavior)"
- "I asked: what's the cost of missing a bug vs. cost of another test"

**Weak answers (need growth):**
- "I felt like I had enough" ← Gut feeling, not systematic
- "I wrote until I got tired" ← No strategic thinking
- "I copied the example" ← Not applying frameworks independently

### Question 5: AI-First Approach

**Will you use "specify and verify" in future projects?**

**Strong affirmative answers:**
- "Yes - it's faster and forces me to think clearly about requirements"
- "Yes - writing tests first helped me understand the problem better"
- "Yes - AI handles syntax so I can focus on design and logic"
- "Yes - I caught bugs early instead of debugging for hours later"

**Honest hesitation (also valid):**
- "Maybe - depends on context. For learning syntax, I might still code manually"
- "Probably - but I need more practice writing good specifications"
- "Yes for features, maybe not for exploratory coding"

**What's the biggest benefit?**

**Common strong answers:**
- "Forces clear thinking - can't prompt AI if I don't understand requirements"
- "Faster feedback loop - test, generate, verify in minutes"
- "Better code quality - I focus on simplicity and correctness"
- "Documentation - tests remain as specification"
- "Confidence - comprehensive tests give me trust in the code"

**What's the biggest challenge?**

**Common honest answers:**
- "Writing clear, complete specifications is hard"
- "Knowing which tests to write (what to test, what to skip)"
- "Evaluating AI code for simplicity (I'm still learning what's 'simple')"
- "Breaking the habit of jumping straight to coding"
- "Trusting AI vs. wanting to code it myself"

---

## Key Takeaways Checklist - Evaluation Guidance

Students should check ALL items in each category if workshop was successful.

### Evaluation Strategy

**During workshop:**
- Circulate and check progress against checklist items
- Note which skills students struggle with
- Provide targeted interventions

**After workshop:**
- Students self-assess using checklist
- You review their work against checklist
- Identify common gaps for follow-up

### Common Gaps & Interventions

| Unchecked Item | Likely Cause | Follow-up Action |
|----------------|--------------|------------------|
| "Make risk-based decisions" | Skipped risk analysis | Require explicit risk assessment |
| "Apply systematic frameworks" | Used ad-hoc approach | Review framework examples |
| "Evaluate test adequacy" | Uncertainty about "enough" | Practice adequacy justification |
| "Identify what NOT to test" | Over-testing everything | Discuss redundant tests |
| "Prompt AI to simplify" | Accepting first answer | Require simplification example |
| "Understand architect role" | Still in coder mindset | Discuss strategic vs. tactical |
| "Specify bug fixes" | Manual debugging | Practice failing-test-first |

---

# Extension Challenges - Facilitation Notes

## Challenge 1: Roman Numerals

**Pedagogical value:**
- Complex rules require research
- Many equivalence classes (I, V, X, L, C, D, M)
- Subtractive notation (IV, IX, XL, XC, CD, CM)
- Good practice for systematic enumeration

**Key test scenarios guide:**

```python
# Single symbols
assert to_roman(1) == "I"
assert to_roman(5) == "V"
assert to_roman(10) == "X"
assert to_roman(50) == "L"

# Subtractive cases (most tricky)
assert to_roman(4) == "IV"   # Not IIII
assert to_roman(9) == "IX"   # Not VIIII
assert to_roman(40) == "XL"
assert to_roman(90) == "XC"
assert to_roman(400) == "CD"
assert to_roman(900) == "CM"

# Boundaries
assert to_roman(1) == "I"     # Min
assert to_roman(3999) == "MMMCMXCIX"  # Max

# Complex examples
assert to_roman(1994) == "MCMXCIV"  # M + CM + XC + IV
assert to_roman(2024) == "MMXXIV"   # MM + XX + IV
```

**Facilitation tips:**
- Students often forget subtractive cases
- Boundary at 3999 (Roman numerals traditionally don't go higher)
- Good opportunity to discuss research as part of specification

## Challenge 2: Email Validator

**Pedagogical value:**
- Deliberately ambiguous specification (real-world problem!)
- Forces students to MAKE specification decisions
- Many edge cases, no "perfect" solution

**Key teaching moment:**

> "There's no single correct test suite for email validation.
>
> YOU must decide:
> - Do you allow multiple @ signs? (technically invalid, but...)
> - Do you allow special characters? Which ones?
> - International domains (.co.uk, .com.au)?
> - IP address domains? (user@[192.168.1.1])
>
> This is specification work - making decisions under ambiguity."

**Minimal test scenarios:**

```python
# Obvious valid
assert is_valid_email("user@example.com") == True
assert is_valid_email("first.last@company.co.uk") == True

# Obvious invalid
assert is_valid_email("no-at-sign.com") == False
assert is_valid_email("@example.com") == False
assert is_valid_email("user@") == False
assert is_valid_email("") == False

# Decisions needed:
# user+tag@example.com - valid? (Gmail uses this)
# user@localhost - valid? (no TLD)
# user@192.168.1.1 - valid? (IP address)
```

**Facilitation focus:**
- Document specification decisions
- Justify why certain patterns are included/excluded
- Discuss trade-offs (strict vs. permissive validation)

## Challenge 3: Shopping Cart

**Pedagogical value:**
- **Stateful** testing (different from pure functions)
- Multiple interacting features
- Real-world complexity

**Key concepts:**

**State management testing:**
```python
# Order matters
cart = ShoppingCart()
assert cart.total() == 0  # Empty state

cart.add_item("apple", 1.00, 3)
assert cart.total() == 3.00  # After adding

cart.remove_item("apple", 1)
assert cart.total() == 2.00  # After removing

cart.clear()
assert cart.total() == 0  # After clearing
```

**Interaction testing:**
```python
# Discount + quantity interaction
cart = ShoppingCart()
cart.add_item("apple", 1.00, 10)  # $10.00
cart.apply_discount(0.10)  # 10% off
assert cart.total() == 9.00  # Discount applied to total
```

**Edge cases:**
```python
# Remove more than exists
cart.add_item("apple", 1.00, 3)
cart.remove_item("apple", 5)  # Remove 5, only 3 exist
assert cart.item_count("apple") == 0  # Or raise error?

# Negative quantity
cart.add_item("apple", 1.00, -3)  # Should raise error

# Zero price
cart.add_item("free_sample", 0.00, 1)
assert cart.total() == 0
```

**Facilitation tips:**
- Emphasize state initialization for each test
- Discuss: should tests be independent or sequential?
- Good transition to unit testing frameworks (setUp/tearDown)

---

# Assessment Rubric (Detailed Scoring Guide)

## Specifications (30 points)

### Comprehensive test scenarios identified (10 points)

**10 points:**
- All equivalence classes identified
- Boundaries systematically analyzed
- Edge cases considered
- Justification provided for each scenario

**7-9 points:**
- Most equivalence classes identified
- Some boundary analysis
- Limited edge case consideration
- Some justification

**4-6 points:**
- Basic scenarios only
- Missing boundaries or edge cases
- Minimal justification

**1-3 points:**
- Incomplete scenarios
- No systematic approach
- No justification

**0 points:**
- No scenario identification

### Clear assertions written (10 points)

**10 points:**
- All assertions executable and correct
- Well-organized (commented by category)
- Covers all identified scenarios
- Proper syntax and expected values

**7-9 points:**
- Most assertions correct
- Some organization
- Covers most scenarios
- Minor syntax issues

**4-6 points:**
- Some assertions correct
- Poor organization
- Gaps in coverage
- Syntax errors

**1-3 points:**
- Few assertions
- Major errors
- No organization

**0 points:**
- No assertions written

### Boundary conditions included (10 points)

**10 points:**
- ALL critical boundaries tested
- Both sides of each boundary
- Justification for boundary selection
- Edge cases at extremes

**7-9 points:**
- Most boundaries tested
- Some both-sided testing
- Limited justification

**4-6 points:**
- Some boundaries tested
- One-sided only
- No justification

**1-3 points:**
- Few boundaries
- Missing critical boundaries

**0 points:**
- No boundary testing

## AI Interaction (25 points)

### Effective prompts crafted (10 points)

**10 points:**
- Prompts are specific and complete
- Include requirements and constraints
- Include test cases
- Specify simplicity level

**7-9 points:**
- Prompts are mostly clear
- Include main requirements
- Some constraints specified

**4-6 points:**
- Prompts are vague
- Missing key information
- No constraints

**1-3 points:**
- Very poor prompts
- Minimal information

**0 points:**
- No prompts documented

### Critical evaluation of AI responses (10 points)

**10 points:**
- Detailed evaluation of correctness and simplicity
- Comparison to requirements
- Identification of improvements
- Justification of decisions (accept/reject/simplify)

**7-9 points:**
- Basic evaluation
- Some comparison
- Limited justification

**4-6 points:**
- Superficial evaluation
- Acceptance without analysis
- No justification

**1-3 points:**
- No real evaluation
- Blind acceptance

**0 points:**
- No evaluation

### Requested simplifications when needed (5 points)

**5 points:**
- At least one simplification requested with good justification
- Clear simplification prompt
- Evaluation of simplified version

**3-4 points:**
- Simplification requested but weak justification

**1-2 points:**
- Should have requested but didn't

**0 points:**
- No simplification attempted

## Implementation & Verification (30 points)

### Code runs and passes tests (15 points)

**15 points:**
- All code executes without errors
- All assertions pass
- Proper verification documented

**11-14 points:**
- Most code works
- Most tests pass
- Some verification

**6-10 points:**
- Some code works
- Some tests pass
- Minimal verification

**1-5 points:**
- Code has errors
- Few tests pass

**0 points:**
- Code doesn't run

### Debugging process documented (10 points)

**10 points:**
- Failing test written first
- Bug clearly specified to AI
- Fix verified
- Edge cases added
- Reflection on process

**7-9 points:**
- Some process documentation
- Fix verified
- Limited reflection

**4-6 points:**
- Minimal process
- Weak documentation

**1-3 points:**
- Almost no process documentation

**0 points:**
- No process

### Code quality evaluated (5 points)

**5 points:**
- Thorough evaluation (simplicity, correctness, readability)
- Comparison to requirements
- Justification of quality decisions

**3-4 points:**
- Basic evaluation

**1-2 points:**
- Superficial evaluation

**0 points:**
- No evaluation

## Reflection (15 points)

### Thoughtful answers to reflection questions (10 points)

**10 points:**
- All questions answered
- Specific examples from exercises
- Demonstrates understanding of strategic role
- Shows metacognitive awareness

**7-9 points:**
- Most questions answered
- Some specifics
- Basic understanding

**4-6 points:**
- Brief answers
- Generic responses
- Limited understanding

**1-3 points:**
- Minimal answers
- No depth

**0 points:**
- No reflection

### Evidence of learning/growth (5 points)

**5 points:**
- Clear articulation of what was learned
- Specific examples of "aha moments"
- Plan for applying skills

**3-4 points:**
- Some learning articulated
- Limited examples

**1-2 points:**
- Vague learning claims

**0 points:**
- No evidence of learning

---

# Common Student Mistakes & How to Address

## 1. Only Testing Happy Paths

**Symptom:** 2-3 assertions, all normal successful cases, no edge cases or boundaries

**Example:**
```python
# Student writes only:
assert calculate_grade(95) == "A"
assert calculate_grade(85) == "B"
assert calculate_grade(75) == "C"
# Missing boundaries, edge cases, invalid inputs
```

**Root cause:**
- Natural bias toward thinking about "how it should work"
- Not thinking adversarially ("how could this break?")
- Lack of systematic framework

**Intervention:**

**In the moment:**
> "These tests show the function works when everything is normal.
>
> But what if someone passes 89.9? Or 101? Or -5?
>
> Use the frameworks: where are your boundaries? Edge cases?"

**Probing questions:**
- "What's the smallest valid input? Largest?"
- "What happens at the exact boundary points?"
- "What could go wrong?"

**Teaching moment:**
- Show a buggy implementation that passes their tests but fails on boundaries
- Demonstrate how inadequate testing lets bugs through

## 2. Accepting AI Code Without Evaluation

**Symptom:** Pasting AI code directly without running, understanding, or evaluating

**Example:**
```python
# Student gets this from AI:
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Student pastes it, marks exercise complete, moves on
# No verification, no evaluation, no simplification request
```

**Root cause:**
- Misunderstanding of role (consumer vs. architect)
- Trust in AI without verification
- Not recognizing complexity

**Intervention:**

**In the moment:**
> "Can you explain this line to me as if I'm a beginner?"
>
> *(Student struggles)*
>
> "Then it's not simple enough. You're the architect - request a simpler version."

**Probing questions:**
- "Did you run this code?"
- "Do all your tests pass?"
- "Can you trace through this by hand for year 1900?"
- "Is this the simplest possible solution?"

**Teaching moment:**
- Show side-by-side: complex boolean logic vs. simple if statements
- "Both work. YOU decide which is better for your context."

## 3. Writing Tests After Implementation

**Symptom:** Tests match code exactly, don't find any bugs, written retroactively

**Example:**
```python
# Student implements first:
def calculate_grade(score):
    if score > 90:  # BUG: should be >=
        return "A"
    # ...

# Then writes tests that match the (buggy) code:
assert calculate_grade(91) == "A"  # Passes (but should test 90)
assert calculate_grade(81) == "B"  # Passes (but should test 80)
```

**Root cause:**
- Traditional coding habit (code first, test later)
- Not understanding specification-first approach
- Tests become "code descriptions" not "requirements"

**Intervention:**

**In the moment:**
> "Did you write these tests before or after seeing the code?"
>
> *(After)*
>
> "Then they're confirming what the code DOES, not what it SHOULD do.
>
> Start over: write tests from the specification first."

**Probing questions:**
- "Did your tests find any bugs?"
- "How would you test this if you didn't know the implementation?"
- "What does the specification say should happen?"

**Teaching moment:**
- Show example where tests-after-code miss a bug
- Demonstrate specification-first catching the bug

## 4. Poor Test Organization

**Symptom:** Random test order, no comments, no grouping, unclear purpose

**Example:**
```python
assert is_leap_year(2024) == True
assert is_leap_year(1900) == False
assert is_leap_year(2023) == False
assert is_leap_year(2000) == True
assert is_leap_year(2020) == True
# No organization, hard to see what's being tested
```

**Root cause:**
- Writing tests as they think of them
- Not planning test strategy first
- Not seeing tests as documentation

**Intervention:**

**Better organization:**
```python
# === EQUIVALENCE CLASS: Divisible by 400 ===
assert is_leap_year(2000) == True
assert is_leap_year(1600) == True

# === EQUIVALENCE CLASS: Divisible by 100 but not 400 ===
assert is_leap_year(1900) == False
assert is_leap_year(1800) == False

# === EQUIVALENCE CLASS: Divisible by 4 but not 100 ===
assert is_leap_year(2024) == True
assert is_leap_year(2020) == True

# === EQUIVALENCE CLASS: Not divisible by 4 ===
assert is_leap_year(2023) == False
assert is_leap_year(2021) == False
```

**Teaching:**
> "Tests are documentation. A future developer should be able to understand
> your testing strategy just by reading your test file."

## 5. Vague AI Prompts

**Symptom:** Getting generic, wrong, or overly complex responses from AI

**Example:**

**Poor prompt:**
```
Write a password validator.
```

**Result:** AI makes up its own requirements, uses complex regex, etc.

**Good prompt:**
```
Write a Python function is_strong_password(password) that validates:
- At least 8 characters
- At least one uppercase letter
- At least one number
- At least one special character from "!@#$%^&*"

Make these assertions pass:
[paste assertions]

Use only basic Python (for loops, if statements).
No regex, no advanced features.
Keep it simple for beginners.
```

**Result:** Clear, simple, correct implementation

**Root cause:**
- Not understanding importance of precise specification
- Assuming AI "knows what you mean"
- Not including constraints

**Intervention:**

**Show comparison:**
- Display poor prompt and resulting code
- Display good prompt and resulting code
- Discuss difference

**Template for good prompts:**
```
1. Function signature (name, parameters)
2. Requirements (numbered list)
3. Test cases (assertions)
4. Constraints (simplicity, features to use/avoid)
5. Context (beginner, production, etc.)
```

## 6. Can't Justify Test Adequacy

**Symptom:** "I don't know" or "seems like enough" when asked why N tests

**Example:**

> **You:** "Why did you write 10 tests instead of 5 or 20?"
>
> **Student:** "I don't know... it seemed like enough?"

**Root cause:**
- Not using systematic frameworks
- No risk assessment performed
- Gut feeling instead of reasoning

**Intervention:**

**Scaffolding:**
> "Let's work through this:
>
> 1. How many equivalence classes? (Count them)
> 2. How many boundaries? (Count them)
> 3. What's the risk level? (Assess it)
> 4. Now, how many tests minimum? (Equivalence classes)
> 5. Add boundaries? (Based on risk)
> 6. That's your number. Can you justify it?"

**Framework application:**
```python
"""
Justification for 12 tests:

Equivalence classes: 4
- One test each = 4 tests minimum

Critical boundaries: 6
- Risk level: HIGH
- Add boundary tests = 6 more tests

Edge cases: 2
- Empty input, out of range
- Add edge tests = 2 more tests

Total: 4 + 6 + 2 = 12 tests

This is appropriate for HIGH RISK function.
For LOW RISK, could reduce to 6 (classes + critical boundaries only).
"""
```

## 7. Over-Testing Same Equivalence Class

**Symptom:** 10+ tests that all test the same behavior

**Example:**
```python
# Testing same equivalence class repeatedly:
assert is_leap_year(2024) == True
assert is_leap_year(2020) == True
assert is_leap_year(2016) == True
assert is_leap_year(2012) == True
assert is_leap_year(2008) == True
assert is_leap_year(2004) == True
# All are "divisible by 4, not by 100" - same class!
```

**Root cause:**
- Not understanding equivalence classes
- Thinking "more tests = better"
- Not recognizing redundancy

**Intervention:**

**Teaching moment:**
> "These six tests all check the same logic path.
>
> If one passes, they all pass.
> If one fails, they all fail.
>
> That's an equivalence class - pick ONE representative."

**Exercise:**
- Ask student to identify which tests could be removed
- Show that code passing 1 test from class passes all
- Demonstrate value of testing DIFFERENT classes instead

## 8. Missing Strategic Reflection

**Symptom:** Reflection answers are superficial, generic, or missing

**Example:**

**Poor reflection:**
```
1. What was most challenging?
   "Everything was hard."

2. How did AI help?
   "It wrote code for me."

3. What did you learn?
   "How to test."
```

**Good reflection:**
```
1. What was most challenging?
   "Deciding when I had 'enough' tests. I could keep writing tests forever,
    but using the risk framework helped me make a justified decision."

2. How did AI help?
   "AI suggested test scenarios I missed (like year 2100 for leap year).
    But I had to evaluate which suggestions were valuable vs. redundant.
    I'm now more aware of my role as architect vs. AI as implementation assistant."

3. What did you learn?
   "Systematic frameworks (equivalence partitioning, boundaries) transform
    testing from guessing to engineering. I can now justify my test strategy
    instead of just 'testing some stuff.'"
```

**Root cause:**
- Rushing through reflection
- Not understanding metacognitive value
- Treating it as busywork

**Intervention:**

**In the moment:**
> "This reflection isn't busywork. It's where learning happens.
>
> Go back to Exercise 2. What specific insight did you gain?
> What moment made you think differently?"

**Prompts for deeper reflection:**
- "Give me a specific example from today"
- "What surprised you? Why?"
- "Compare your approach now vs. beginning of workshop"
- "What will you do differently next week?"

---

# Facilitation Best Practices

## Time Management Strategies

### Set Clear Time Boxes

**Use visible timer:**
- Project countdown on screen
- Announce time remaining
- Give 5-min and 1-min warnings

**Example script:**
> "You have 20 minutes for Part 1. I'll give you a 5-minute warning,
> then we'll pause for discussion whether you're done or not."

### Be Flexible But Bounded

**If students need more time:**
- Extend by 5-10 minutes max
- Identify which exercises can be shortened
- Move less critical content to homework

**If students finish early:**
- Have extension challenges ready
- Ask early finishers to help peers
- Start mini-debrief early with fast group

### Structured Breaks

**After Part 3 (about 90 min in):**
- 10-minute break
- Students return refreshed for Part 4

**After Part 5 (about 2.5 hours in):**
- 5-minute break or stretch
- Re-energize before capstone

## Engagement Strategies

### Constant Circulation

**Walk around continuously:**
- Monitor screens (are they stuck?)
- Read over shoulders (are they on task?)
- Check facial expressions (confusion? frustration?)

**Don't sit at front desk** - be mobile

### Ask Probing Questions, Don't Give Answers

**Instead of:**
> "The bug is that count increments outside the if statement."

**Ask:**
> "Walk me through what happens to count when num is negative."
>
> *(Student traces through)*
>
> "Ah! Count still increments even though we didn't add to total!"

**Socratic method** builds understanding

### Highlight Interesting Solutions

**Public recognition:**
> "I just saw a really clever test case over here - testing exactly 8 characters
> for the password validator. Why is that important?"

**Validation** - students feel seen, others learn

### Create "Aha Moments"

**Deliberately reveal bugs:**

Show this code:
```python
def calculate_grade(score):
    if score > 90:
        return "A"
    # ...
```

Ask: "Will this work?"

Students: "Yes!"

Test: `calculate_grade(90)` returns "B" (not "A")

Students: "Oh! >= not >"

**Concrete demonstration** more powerful than explanation

## Common Debrief Questions

### After Part 2 (Specification Design)

1. **"Who found a scenario they initially missed?"**
   - Validates using frameworks
   - Shows value of systematic thinking

2. **"Why are the century years so important to test?"**
   - Reinforces boundary analysis
   - Connects to real bugs

3. **"How did you decide what counts as 'enough' tests?"**
   - Surfaces strategic thinking
   - Introduces risk-based decisions

### After Part 4 (Test Design Practice)

1. **"How many tests did you write?"**
   - Show diversity of answers (8, 12, 15...)
   - Point out: multiple right answers exist
   - What matters: justification

2. **"What's harder - thinking of tests or writing them?"**
   - Most will say "thinking of tests"
   - Validates importance of frameworks
   - Shows AI helps with implementation, not strategy

3. **"Did anyone find a case that broke your intuition?"**
   - Surfaces interesting edge cases
   - Builds shared knowledge

### After Part 5 (Bug Prevention)

1. **"Who wrote the failing test BEFORE asking AI for the fix?"**
   - Reinforce specification-first approach
   - Distinguish from traditional debugging

2. **"How did AI explain the bug?"**
   - Compare explanations
   - Evaluate quality of AI reasoning
   - Discuss: does explanation help understanding?

3. **"How is this different from manual debugging?"**
   - Test-first vs. print-statement debugging
   - Documentation value
   - Regression prevention

### After Part 6 (Integration Exercise)

1. **"What was your risk assessment and how did it affect your testing?"**
   - Validate risk-based thinking
   - Show different justifications

2. **"Who made a specification decision (like how to handle out-of-range scores)?"**
   - Highlight realistic ambiguity
   - Discuss how different decisions are valid if justified

3. **"Did your tests catch the boundary bug (> vs >=)?"**
   - Most critical teaching moment
   - Shows value of systematic boundary testing

## Managing Difficulty Levels

### For Students Who Finish Early

**Extension challenges** (already provided in worksheet):
- Roman numerals
- Email validator
- Shopping cart

**Peer teaching:**
> "You're done? Great! Can you help explain equivalence partitioning to
> your neighbor?"

**Depth over breadth:**
> "Add one more scenario you DIDN'T test and explain why you chose not to."

### For Struggling Students

**Identify common struggles:**
- Can't identify equivalence classes → work through together
- Can't write assertions → provide template
- Confused by AI responses → help interpret

**Scaffolding:**
- Pair struggling students with stronger ones
- Provide partially completed examples
- Break down exercises into smaller steps

**One-on-one intervention:**
- Sit with student for 2-3 minutes
- Walk through one complete example together
- Check understanding, then let them continue

### For Mixed-Pace Classes

**Tier activities:**
1. **Core exercises** (everyone must complete)
2. **Extension exercises** (for fast finishers)
3. **Reflection questions** (buffer time, everyone can work on)

**Flexible grouping:**
- Fast finishers pair up for extensions
- Slower students get more individual attention
- Avoid making pace differences obvious/stigmatizing

## Technical Issues Management

### Before Workshop

**Test environment:**
- All code cells execute
- AI access works
- No library dependency issues

**Have backups:**
- Printed copies of worksheet
- Alternative exercises if tech fails
- Offline activities

### During Workshop

**Common issues:**

**"AI isn't responding"**
- Have backup prompts/responses ready
- Can share example AI response if needed
- Worst case: skip AI part, focus on frameworks

**"My code won't run"**
- Check for: missing colons, indentation, quote matching
- Have TA or peer help debug
- Don't let one student monopolize your time

**"I lost my work"**
- Encourage frequent saves
- Use version control if possible
- Have auto-save enabled

### Recovery Strategies

**If major tech failure:**
- Pivot to whiteboard discussion
- Focus on planning/frameworks (can code later)
- Use paper and pseudocode
- Extend worksheet as homework

**If isolated student issues:**
- Pair them with working student to share screen
- Provide completed sections to catch up
- Focus their time on key learning objectives

---

# Post-Workshop Follow-Up

## Suggested Homework

**Completion:**
> Complete any unfinished exercises from today's workshop.
> Submit your completed worksheet with all code running.

**Application:**
> Apply the testing frameworks to your current project:
> 1. Choose one function from your project
> 2. Perform risk assessment
> 3. Identify equivalence classes and boundaries
> 4. Write comprehensive test assertions
> 5. If bugs found, specify fixes to AI
>
> Submit: Your test suite with justification of adequacy

**Existing Code Testing:**
> Find a function you've already written:
> 1. Write tests for it using today's frameworks
> 2. Did you find any bugs?
> 3. Reflect: Would test-first have prevented these bugs?

**Extension Challenges:**
> Complete at least one extension challenge (Roman numerals, email, shopping cart)
>
> Submit with:
> - Risk assessment
> - Equivalence class analysis
> - Comprehensive test suite
> - AI collaboration documentation

## Next Class Connection

### Review Session (10-15 min next class)

**Share common findings:**
> "Many of you found boundary bugs in the grading function.
> This is the most common type of bug in decision logic.
> Remember: test at boundaries, not just in ranges."

**Gallery walk:**
- Post interesting test strategies
- Students walk around, compare approaches
- Discuss differences

**Common bugs collection:**
- Create shared list of bugs found
- Discuss how they were caught (or missed)

### Preview Next Module

**If next: Automated Testing with pytest:**
> "Today you wrote assertions directly in code.
> Next week: pytest framework for professional test organization.
>
> You'll learn:
> - Test organization (test files, test classes)
> - Running test suites
> - Test fixtures (setup/teardown)
> - Parameterized tests (run same test with multiple inputs)
>
> Today's strategic thinking transfers directly."

**If next: Test-Driven Development (TDD):**
> "Today you practiced specification-first testing.
> Next week: Full TDD workflow: Red-Green-Refactor
>
> You'll learn:
> - Write failing test (Red)
> - Make it pass (Green)
> - Improve code (Refactor)
> - Repeat
>
> Today's frameworks are foundation for TDD."

**Connection to AI-TDD:**
> "Today: You specified, AI implemented.
> Next week: You'll drive AI through the full TDD cycle.
>
> This is the future of software development:
> Strategic human + implementation AI = rapid, quality software."

---

# Assessment Examples

## Example 1: Excellent Submission

**Student work on leap year:**

```python
"""
RISK ASSESSMENT:
Risk level: Medium
- Incorrect calendar logic affects scheduling
- Not life-critical, but user-facing
- Moderate testing investment justified

EQUIVALENCE CLASSES:
1. Divisible by 400 → LEAP (e.g., 2000, 1600)
2. Divisible by 100 not 400 → NOT LEAP (e.g., 1900, 1800)
3. Divisible by 4 not 100 → LEAP (e.g., 2024, 2020)
4. Not divisible by 4 → NOT LEAP (e.g., 2023, 2021)

BOUNDARY ANALYSIS:
- Century years (1900, 2000) - where 100/400 rules apply
- Adjacent to centuries (1899, 1901) - verify rule transitions

TEST ADEQUACY:
Minimum: 4 tests (one per class)
My plan: 8 tests (classes + key boundaries)
Justification: Medium risk warrants boundary testing.
         Not going further because diminishing returns.
"""

def is_leap_year(year):
    pass

# === CLASS 1: Divisible by 400 ===
assert is_leap_year(2000) == True
assert is_leap_year(1600) == True

# === CLASS 2: Divisible by 100 not 400 ===
assert is_leap_year(1900) == False
assert is_leap_year(2100) == False  # AI suggested this

# === CLASS 3: Divisible by 4 not 100 ===
assert is_leap_year(2024) == True

# === CLASS 4: Not divisible by 4 ===
assert is_leap_year(2023) == False

# === BOUNDARY: Adjacent to century ===
assert is_leap_year(1899) == False  # Before 1900
assert is_leap_year(1901) == False  # After 1900

"""
AI COLLABORATION:
Prompt: [Well-structured prompt with requirements, tests, constraints]

AI Response: [Boolean expression version]

Evaluation:
- Correctness: PASS (all assertions pass)
- Simplicity: FAIL (complex boolean logic)
- Decision: Request simplification

Simplification prompt: [Clear request for simpler version]

AI Simplified: [If/return chain version]

Final evaluation:
- Much clearer for beginners
- Each rule is one line
- Accepted this version
"""
```

**What makes this excellent:**
✓ Systematic framework application
✓ Clear risk assessment with justification
✓ Complete equivalence class identification
✓ Boundary analysis
✓ Test adequacy justified
✓ AI collaboration documented
✓ Simplification requested and evaluated
✓ Strategic decisions explained

**Score: 28-30/30**

---

## Example 2: Good Submission (Needs Improvement)

**Student work on leap year:**

```python
def is_leap_year(year):
    pass

# Tests:
assert is_leap_year(2024) == True
assert is_leap_year(2023) == False
assert is_leap_year(2000) == True
assert is_leap_year(1900) == False
assert is_leap_year(2020) == True
assert is_leap_year(2021) == False

"""
AI gave me this code:
[working implementation]

It works and all tests pass.
"""
```

**Issues:**
✗ No risk assessment
✗ No equivalence class analysis
✗ Tests written but not categorized
✗ Some redundancy (2024/2020, 2023/2021 same classes)
✗ No boundary analysis
✗ No test adequacy justification
✗ Minimal AI collaboration documentation
✗ No evaluation of simplicity

**Feedback:**
> "Your tests work, but I can't see your strategic thinking.
>
> Add:
> 1. Risk assessment - why this testing level?
> 2. Equivalence classes - what does each test represent?
> 3. Boundary analysis - where are the critical boundaries?
> 4. Test adequacy - why 6 tests, not 3 or 12?
> 5. AI evaluation - is the code simple enough? Did you request simplification?"

**Score: 18-22/30**

---

## Example 3: Poor Submission (Major Revision Needed)

**Student work:**

```python
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert is_leap_year(2024) == True
assert is_leap_year(2000) == True
```

**Issues:**
✗ Only 2 tests (inadequate coverage)
✗ No failing test cases
✗ No risk assessment
✗ No framework application
✗ No AI collaboration documented
✗ Complex code not evaluated or simplified
✗ No reflection

**Feedback:**
> "This needs major revision. You've completed the mechanical steps but missed
> the strategic thinking that's the core learning objective.
>
> Start over with:
> 1. Risk assessment
> 2. Equivalence class identification
> 3. Boundary analysis
> 4. Complete test suite
> 5. AI collaboration with evaluation
> 6. Code simplicity assessment
>
> See me in office hours if you need help with the frameworks."

**Score: 8-12/30**

---

**End of Staff Facilitator Guide**
