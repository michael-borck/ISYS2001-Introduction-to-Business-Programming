---
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

# Instructor Guide: Building a Robust CSV Processor
## Module: "Expecting the Unexpected"

---

## Table of Contents
1. [Workshop Overview](#workshop-overview)
2. [Learning Objectives](#learning-objectives)
3. [Timing & Session Flow](#timing--session-flow)
4. [Facilitation Strategies](#facilitation-strategies)
5. [Solution Key](#solution-key)
6. [Common Student Struggles](#common-student-struggles)
7. [AI Prompting Guidance](#ai-prompting-guidance)
8. [Assessment & Grading](#assessment--grading)
9. [Quick Troubleshooting Reference](#quick-troubleshooting-reference)

---

## Workshop Overview

### Context
This is Module 10 in an AI-first introductory programming course. Students have previously covered:

- Python basics (variables, data types, functions)
- Control flow (if-then, loops)
- Data structures (lists, dictionaries)
- Pandas for data analysis
- APIs and external modules
- Gradio for building UIs

### What's New This Week
- **Conceptual:** Robustness, edge cases, graceful degradation
- **Technical:** try-except blocks, exception types, error handling patterns
- **Applied:** Building professional-quality user-facing applications

### The AI-First Approach
Students use AI to generate code while focusing on:

1. **Conceptual understanding** - What can go wrong?
2. **Prompt engineering** - How to ask AI for robust solutions
3. **Code evaluation** - Does AI's solution handle all cases?
4. **Testing mindset** - Deliberately breaking things to verify robustness

---

## Learning Objectives

By the end of this workshop, students should be able to:

### Conceptual (Understand)
- [ ] Explain what robustness means in software development
- [ ] Identify common edge cases in file processing
- [ ] Describe the relationship between error handling and user experience
- [ ] Understand the "Plan A / Plan B" mental model of try-except

### Applied (Do)
- [ ] Use AI to generate exception handling code
- [ ] Test applications with deliberately problematic inputs
- [ ] Evaluate whether error messages are user-friendly
- [ ] Build a complete Gradio app with robust error handling

### Metacognitive (Reflect)
- [ ] Recognize when their prompts need to be more specific
- [ ] Critique AI-generated code for completeness
- [ ] Apply the "what if?" mindset to future projects

---

## Timing & Session Flow

### Flipped Classroom Model
**Pre-Class (30-45 min):**

- Students review slides on exception handling concepts
- Watch any supplementary videos (if provided)
- Come to class with conceptual understanding

**In-Class Workshop (90-120 min):**

| Time | Part | Activity | Tutor Role |
|------|------|----------|------------|
| 0-10 min | Setup | Install libraries, create test files | Circulate, help with setup issues |
| 10-30 min | Part 1 | Build basic Gradio app (happy path) | Monitor prompts, ensure everyone has working app |
| 30-50 min | Part 2 | Break the app, record observations | Encourage exploration, facilitate discussion |
| 50-55 min | — | **Break** | — |
| 55-85 min | Part 3 | Add exception handling | Help refine prompts, discuss AI output quality |
| 85-105 min | Part 4 | Add file download functionality | Support integration of new features |
| 105-120 min | Part 5 | Reflection & discussion | Facilitate group reflection |

**Post-Class:**
- Complete reflection questions
- Take quiz for self-assessment
- Review flashcards
- (Optional) Extend app with additional features

---

## Facilitation Strategies

### Part 1: The Happy Path

**Goal:** Everyone gets a working basic app quickly

**Key Teaching Moment:**
When reviewing working apps, ask: "What assumptions does this code make about the data?" Plant seeds for Part 2.

**Common Issue:** Students create apps that don't display output properly
- **Coaching:** "What type of output does your Gradio interface expect? Check if your function returns the right data type."

**Fast Finishers:**
- "Can you modify it to also show the number of products in the file?"
- "What happens if you add print statements to debug?"

**Teaching Tip:**
Emphasize that this code works perfectly... until it doesn't. The "happy path" is important but insufficient.

---

### Part 2: Breaking Things

**Goal:** Students experience failure viscerally to understand why robustness matters

**This is the MOST IMPORTANT part pedagogically!**

**Facilitation Strategy:**
1. **Let them struggle** - Don't jump in immediately when apps crash
2. **Encourage experimentation** - "Try uploading something really weird"
3. **Collect observations** - Use a shared document or whiteboard for patterns
4. **Build empathy** - "How would you feel as a user seeing this error?"

**Discussion Prompts (after testing):**
- "What patterns did you notice in the errors?"
- "Which error message was most confusing? Why?"
- "If you were building this for a real client, how would these crashes impact your reputation?"

**Key Insight to Surface:**
Python's default error messages are for *developers*, not *users*. Our job is to translate.

**Watch For:**
- Students who skip testing and move ahead → pull them back
- Students who only test one error type → encourage comprehensive testing
- Students who think errors mean they did something wrong → reframe as discovery

---

### Part 3: Making It Robust

**Goal:** Transform fragile code into professional-quality error handling

**This is the most technically demanding part**

**Scaffolding Approach:**
1. **Start with one exception** - Get everyone handling ParserError first
2. **Check for understanding** - "Why did we put this in an except block?"
3. **Expand systematically** - Add more exception types one at a time
4. **Test immediately** - After each addition, verify it works

**Common Prompt Issues:**

| Student Prompt | Problem | Better Approach |
|----------------|---------|-----------------|
| "Add error handling" | Too vague | "Add try-except blocks for FileNotFoundError, ParserError, and KeyError" |
| "Fix the errors" | AI doesn't know what's broken | "Handle the case when quantity column contains text instead of numbers" |
| "Make it robust" | AI might add unnecessary complexity | "Add specific error handling for [list 3-4 cases]" |

**When to Intervene:**
- ❌ **Don't:** Write code for students or give exact prompts
- ✅ **Do:** Ask guiding questions
  - "What specific error does Test 2 raise?"
  - "What do you want to tell the user when that happens?"
  - "Can you be more specific about which exceptions to catch?"

**AI Evaluation Exercise:**
This is crucial! Pause the class and facilitate discussion:

1. "Did anyone's AI put the general Exception before specific ones?"
2. "What problems could that cause?"
3. "How do you know if AI handled all five edge cases?"

**Teaching Moment - Exception Ordering:**
Draw on board or screen:
```
try:
    risky_code()
except Exception as e:        # ← Catches EVERYTHING
    return "Error"
except FileNotFoundError:     # ← Never reached!
    return "File not found"
```
vs.
```
try:
    risky_code()
except FileNotFoundError:     # ← Specific first
    return "File not found"
except Exception as e:        # ← Catch-all last
    return "Unexpected error"
```

---

### Part 4: Completing the Workflow

**Goal:** Add file output without breaking error handling

**Key Concepts:**
- File I/O (saving DataFrames)
- Changing Gradio output components
- Maintaining error handling through changes

**Common Challenge:**
Students forget to update error handling for the new return type (file path vs. text)

**Coaching Questions:**
- "Your function now returns a file path. Do your error messages need to change?"
- "What happens if saving the file fails? Should we handle that?"

**Watch For:**
- Students who lose their error handling when adding new features
- Confusion about returning file paths vs. DataFrames

**Extension Challenge Discussion:**
Use the extension challenges to discuss:

- "How would you handle a 5GB file?" (memory issues, streaming)
- "Why might negative prices be a problem?" (business logic validation)
- "What's the difference between empty cells and missing columns?" (data quality)

---

### Part 5: Reflection

**Goal:** Consolidate learning and develop metacognitive awareness

**Facilitation Style:** Discussion-based, not lecture

**Small Group Discussion (10 min):**
Put students in groups of 3-4 to discuss reflection questions. Rotate between groups.

**Large Group Synthesis (5-10 min):**
Bring insights to whole class:

- "What was the biggest 'aha' moment for you today?"
- "How did your prompting strategy change from Part 1 to Part 4?"
- "Where else in your projects could you apply this?"

**Real-World Connection:**
Share stories of:

- Apps that crash vs. apps that handle errors well
- How error handling impacts user trust
- Examples from industry (optional: show bad error message screenshots)

---

## Solution Key

### Part 1: Basic Gradio App (Happy Path)

```python
import gradio as gr
import pandas as pd

def calculate_revenue(file):
    """
    Basic CSV processor - no error handling (fragile)
    This will crash with any problematic input
    """
    # Read the CSV
    df = pd.read_csv(file.name)
    
    # Create revenue column
    df['revenue'] = df['quantity'] * df['price']
    
    # Calculate total
    total = df['revenue'].sum()
    
    return f"Total Revenue: ${total:,.2f}"

# Create Gradio interface
demo = gr.Interface(
    fn=calculate_revenue,
    inputs=gr.File(label="Upload CSV File"),
    outputs=gr.Text(label="Result"),
    title="CSV Revenue Calculator",
    description="Upload a CSV with product, quantity, and price columns"
)

demo.launch()
```

**Notes for Tutors:**
- Student solutions may vary slightly (different variable names, formatting)
- Key criteria: Does it work with valid data?
- Common variations: Some students might use `df['quantity'] * df['price']` inline
- This code SHOULD crash with bad inputs - that's the point!

---

### Part 3: Robust Version with Exception Handling

```python
import gradio as gr
import pandas as pd

def calculate_revenue_robust(file):
    """
    Robust CSV processor with comprehensive error handling
    Handles: None input, parser errors, missing columns, 
            invalid data types, empty files
    """
    
    # Check if file was uploaded
    if file is None:
        return "Error: Please upload a file before processing."
    
    try:
        # Attempt to read the CSV
        df = pd.read_csv(file.name)
        
        # Check if DataFrame is empty
        if df.empty:
            return "Error: The uploaded file contains no data."
        
        # Check for required columns
        if 'quantity' not in df.columns or 'price' not in df.columns:
            return "Error: CSV must contain 'quantity' and 'price' columns."
        
        # Create revenue column (this will raise TypeError/ValueError if data is invalid)
        df['revenue'] = df['quantity'] * df['price']
        
        # Calculate total
        total = df['revenue'].sum()
        
        return f"Total Revenue: ${total:,.2f}"
        
    except pd.errors.ParserError:
        return "Error: Please upload a valid CSV file."
        
    except KeyError as e:
        return f"Error: Missing required column: {e}"
        
    except (ValueError, TypeError):
        return "Error: Quantity and price must be numeric values."
        
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

# Create Gradio interface
demo = gr.Interface(
    fn=calculate_revenue_robust,
    inputs=gr.File(label="Upload CSV File"),
    outputs=gr.Text(label="Result"),
    title="CSV Revenue Calculator (Robust)",
    description="Upload a CSV with product, quantity, and price columns"
)

demo.launch()
```

**Alternative Acceptable Solutions:**

**Option A: Without explicit column check (relies on KeyError)**
```python
try:
    df = pd.read_csv(file.name)
    if df.empty:
        return "Error: The uploaded file contains no data."
    df['revenue'] = df['quantity'] * df['price']  # Will raise KeyError if columns missing
    total = df['revenue'].sum()
    return f"Total Revenue: ${total:,.2f}"
except KeyError:
    return "Error: CSV must contain 'quantity' and 'price' columns."
```

**Option B: More detailed empty check**
```python
if df.empty or len(df) == 0:
    return "Error: The uploaded file contains no data rows."
```

**Notes for Tutors:**
- Exception order MUST be specific → general
- All five edge cases should be handled (None, ParserError, KeyError, ValueError/TypeError, empty)
- Error messages should be user-friendly (no technical jargon)
- Some AI implementations might combine ValueError and TypeError into one except block - this is fine
- Watch for: Students who put `except Exception` first (will catch everything)

---

### Part 4: Complete Version with File Download

```python
import gradio as gr
import pandas as pd

def process_csv_complete(file):
    """
    Complete robust CSV processor that returns downloadable file
    """
    
    # Check if file was uploaded
    if file is None:
        return None  # Note: Return None for file output when error occurs
    
    try:
        # Read the CSV
        df = pd.read_csv(file.name)
        
        # Check if DataFrame is empty
        if df.empty:
            return None
        
        # Check for required columns
        if 'quantity' not in df.columns or 'price' not in df.columns:
            return None
        
        # Create revenue column
        df['revenue'] = df['quantity'] * df['price']
        
        # Save to new CSV
        output_path = 'processed_sales.csv'
        df.to_csv(output_path, index=False)
        
        return output_path
        
    except pd.errors.ParserError:
        return None
        
    except KeyError:
        return None
        
    except (ValueError, TypeError):
        return None
        
    except Exception as e:
        return None

# Create Gradio interface with File output
demo = gr.Interface(
    fn=process_csv_complete,
    inputs=gr.File(label="Upload CSV File"),
    outputs=gr.File(label="Download Processed CSV"),
    title="CSV Revenue Processor",
    description="Upload a CSV to add revenue calculations and download the result"
)

demo.launch()
```

**Important Notes:**
- When output is `gr.File`, errors should return `None` (not error message strings)
- For better UX, could use `gr.File` + `gr.Text` as outputs to show both file and messages
- The file path returned should be accessible to Gradio (typically current directory)

**Enhanced Version (Optional - for advanced students):**
```python
def process_csv_complete_enhanced(file):
    """Version with both file output AND status messages"""
    if file is None:
        return None, "Error: Please upload a file before processing."
    
    try:
        df = pd.read_csv(file.name)
        
        if df.empty:
            return None, "Error: The uploaded file contains no data."
        
        if 'quantity' not in df.columns or 'price' not in df.columns:
            return None, "Error: CSV must contain 'quantity' and 'price' columns."
        
        df['revenue'] = df['quantity'] * df['price']
        
        output_path = 'processed_sales.csv'
        df.to_csv(output_path, index=False)
        
        total = df['revenue'].sum()
        return output_path, f"✓ Success! Processed {len(df)} rows. Total Revenue: ${total:,.2f}"
        
    except pd.errors.ParserError:
        return None, "Error: Please upload a valid CSV file."
    except (ValueError, TypeError):
        return None, "Error: Quantity and price must be numeric values."
    except Exception as e:
        return None, f"An unexpected error occurred: {str(e)}"

# Interface with two outputs
demo = gr.Interface(
    fn=process_csv_complete_enhanced,
    inputs=gr.File(label="Upload CSV File"),
    outputs=[
        gr.File(label="Download Processed CSV"),
        gr.Text(label="Status")
    ],
    title="CSV Revenue Processor"
)
```

---

## Common Student Struggles

### 1. AI Generates Code That Doesn't Match the Prompt

**Symptoms:**
- Exception handling is incomplete
- Wrong exception types are caught
- Error messages are too technical

**Causes:**
- Vague prompts
- Not specifying all five edge cases
- Not requesting user-friendly messages

**Coaching Strategy:**
- Ask: "Did you tell AI about all five problems we found in Part 2?"
- Suggest: "Try listing each specific error type you want to handle"
- Remind: "Show AI the test cases that need to work"

**Example Improved Prompt:**
```
"Add exception handling for these specific cases:

1. User doesn't upload a file (check for None)
2. File isn't valid CSV (ParserError)
3. Missing quantity or price columns (KeyError)
4. Text in numeric columns (ValueError/TypeError)
5. File has only headers, no data (check df.empty)

For each case, return a clear error message like:
'Error: [what went wrong]. [how to fix it]'
```

---

### 2. Confusion About What to Test

**Symptoms:**
- Students test valid data repeatedly
- Skip testing some edge cases
- Don't understand why we're "trying to break it"

**Causes:**
- Haven't internalized the adversarial testing mindset
- Fear of breaking their working code

**Coaching Strategy:**
- Reframe: "Professional developers WANT to find bugs before users do"
- Analogy: "Like a crash test dummy - we break things on purpose to make them safer"
- Challenge: "Can you find a way to make it crash that we haven't thought of?"

---

### 3. Exception Order Problems

**Symptoms:**
- Specific exceptions never trigger
- General `Exception` catches everything

**Causes:**
- Don't understand that Python checks except blocks sequentially
- AI sometimes generates incorrect ordering

**Visual Teaching Aid:**
Draw a flowchart:
```
Exception raised
    ↓
Is it ParserError? → Yes → Run that block → Done
    ↓ No
Is it KeyError? → Yes → Run that block → Done
    ↓ No
Is it Exception? → Yes → Run that block → Done
    ↓ No
No handler found → Program crashes
```

**Coaching Questions:**
- "What happens if we put the general exception first?"
- "How can you test if your specific handlers are working?"

---

### 4. Unclear Error Messages

**Symptoms:**
- Messages like "Error: Invalid data"
- Messages include variable names or technical terms
- Messages don't tell users what to do

**Causes:**
- Copying Python's default error style
- Not thinking from user perspective

**Teaching Moment:**
Show two versions side-by-side:
```
❌ "Error: KeyError 'quantity'"
✓ "Error: CSV must contain 'quantity' and 'price' columns."

❌ "Error: Invalid input"
✓ "Error: Quantity and price must be numeric values. Please check your CSV for text in these columns."
```

Ask: "If you were the user, which would help you fix the problem?"

---

### 5. Lost Error Handling in Part 4

**Symptoms:**
- Part 3 works, but Part 4 doesn't handle errors
- Students rebuild from scratch instead of modifying

**Causes:**
- Starting over instead of modifying existing code
- Not explicitly telling AI to "keep all error handling"

**Prevention:**
Before Part 4, remind students: "You're adding features to your robust code, not replacing it"

**Recovery Strategy:**
- "Copy your Part 3 code into your Part 4 prompt"
- "Tell AI: 'Modify this code to add file download, keeping all existing error handling'"

---

### 6. File Path Confusion in Part 4

**Symptoms:**
- Returns DataFrame instead of file path
- File saves but doesn't appear in Gradio
- Error: "Cannot return DataFrame to File component"

**Causes:**
- Misunderstanding of gr.File output type
- Not knowing file must be saved to disk first

**Coaching:**
- "Gradio needs a filename as a string, not the DataFrame itself"
- "Two steps: First save with `to_csv()`, then return the filename"
- Show: `output_path = 'processed.csv'` → `df.to_csv(output_path)` → `return output_path`

---

## AI Prompting Guidance

### Teaching Students to Prompt Effectively

**The SCRAM Framework for Prompting:**

**S - Specific:** Name exact exception types, exact columns, exact messages
**C - Complete:** List ALL edge cases, not just one
**R - Readable:** Ask for user-friendly messages
**A - Actionable:** Request messages that tell users how to fix problems
**M - Maintainable:** Ask for clear code structure (specific exceptions before general)

### Progression of Prompt Quality

**Level 1 - Beginner (Vague):**
```
"Add error handling to my code"
```
**Problems:** AI doesn't know what errors to handle, may add unnecessary complexity

---

**Level 2 - Intermediate (Some Specificity):**
```
"Add try-except blocks to handle invalid CSV files"
```
**Problems:** Only addresses one type of error, unclear what "invalid" means

---

**Level 3 - Advanced (SCRAM Framework):**
```
"Add exception handling for these specific cases:

1. File parameter is None (user didn't upload): return 'Error: Please upload a file'
2. File isn't parseable CSV (ParserError): return 'Error: Please upload a valid CSV file'
3. Missing 'quantity' or 'price' columns (KeyError): return 'Error: CSV must contain quantity and price columns'
4. Non-numeric values in quantity/price (ValueError/TypeError): return 'Error: Quantity and price must be numeric'
5. Empty DataFrame (df.empty): return 'Error: File contains no data'

Put specific exceptions before the general Exception catch-all.
```

**Teaching Point:** Show these side-by-side and discuss why Level 3 gets better results

---

### When AI Gets It Wrong

**Common AI Mistakes:**

1. **Wrong exception order** → Student should recognize and fix
2. **Generic error messages** → Student should request more specific
3. **Missing edge cases** → Student should add to prompt
4. **Overly complex code** → Student should ask for simpler version

**This is PART OF THE LEARNING:**
Students need to:

- Recognize problems in AI output
- Iterate on prompts
- Understand that AI is a tool, not oracle

**Coaching Stance:**
- "What's wrong with this code AI generated?"
- "How could you improve your prompt to get better results?"
- "Does this handle all five cases? Which one is missing?"

---

### Prompt Templates for Common Issues

**Template: Adding to Existing Code**
```
"Here's my current code:
[paste code]

Modify it to also [new feature], while keeping all existing error handling."
```

**Template: Fixing Specific Problem**
```
"My code doesn't handle [specific scenario]. 
Add an except block that catches [exception type] and returns '[error message]'."
```

**Template: Making Messages Better**
```
"These error messages are too technical:
[list messages]

Rewrite them to be user-friendly and tell users how to fix the problem."
```

---

## Assessment & Grading

### Formative Assessment (During Workshop)

**Observe:**
- [ ] Can students identify edge cases in Part 2?
- [ ] Do they prompt AI with specificity in Part 3?
- [ ] Can they evaluate whether AI's output is complete?
- [ ] Do they test their error handling?

**Quick Checks:**
- Circulate during Part 2 - are students recording different error types?
- During Part 3 - ask students to explain one of their except blocks
- After Part 4 - ask "What happens if I upload [specific bad file]?"

---

### Summative Assessment Options

#### Option 1: Working App Submission (Recommended)
**Criteria:**

| Criterion | Excellent (4) | Good (3) | Satisfactory (2) | Needs Work (1) |
|-----------|---------------|----------|------------------|----------------|
| **Functionality** | Handles all 5+ edge cases correctly | Handles 4 edge cases | Handles 2-3 edge cases | Handles 0-1 edge cases |
| **Error Messages** | Clear, user-friendly, actionable | Clear but not always actionable | Present but technical | Generic or missing |
| **Code Structure** | Specific exceptions before general, well-organized | Mostly correct ordering | Some ordering issues | Incorrect exception order |
| **Testing** | Tested all edge cases, documented results | Tested most edge cases | Tested some edge cases | Minimal testing |
| **Completeness** | All parts complete + extensions | All required parts complete | Missing Part 4 | Missing multiple parts |

**Total: /20 points**

---

#### Option 2: Reflection + App (Holistic)

**Part A: Working Application (50%)**
- Demonstrates robust error handling
- Provides user-friendly feedback
- Completes the full workflow (upload → process → download)

**Part B: Reflection Essay (30%)**
Prompt: "Describe how your understanding of error handling evolved during this workshop. Include:

- What surprised you about testing edge cases
- How you improved your AI prompts through iteration
- Where you'll apply robustness principles in future projects"

**Part C: AI Prompting Evidence (20%)**
Submit:

- Initial prompt to AI for Part 3
- Refined prompt after testing
- Brief explanation of what you changed and why

---

#### Option 3: Peer Review Exercise

**Process:**
1. Students submit their Part 4 code
2. Exchange with partner
3. Each student tries to "break" partner's app
4. Document what worked and what didn't
5. Reflect on differences in approach

**Assessment:**
- Quality of testing (did they find real edge cases?)
- Feedback quality (constructive, specific)
- Reflection on learning

---

### Sample Rubric for Complete Project

```
FUNCTIONALITY (40 points)
□ Handles no file upload (8 pts)
□ Handles invalid CSV format (8 pts)
□ Handles missing columns (8 pts)
□ Handles invalid data types (8 pts)
□ Handles empty files (8 pts)

USER EXPERIENCE (20 points)
□ Error messages are clear (10 pts)
□ Error messages are actionable (10 pts)

CODE QUALITY (20 points)
□ Exception order correct (10 pts)
□ Code is well-structured (10 pts)

PROCESS (20 points)
□ Completed all reflection questions thoughtfully (10 pts)
□ Evidence of iterative testing (10 pts)

TOTAL: /100 points
```

---

### What "Good Enough" Looks Like

Given AI variations, here's what's acceptable:

**Must Have:**
- ✅ Handles at least 4 of 5 edge cases
- ✅ Error messages are understandable (even if not perfect)
- ✅ Specific exceptions come before general
- ✅ App doesn't crash on test files
- ✅ Part 4 returns downloadable file

**Nice to Have (but not required):**
- ⭐ Handles additional edge cases not in requirements
- ⭐ Error messages include suggestions for fixes
- ⭐ Code includes comments
- ⭐ Extensions implemented

**Red Flags (needs revision):**
- ❌ Crashes on standard test files
- ❌ No exception handling at all
- ❌ General Exception catches everything
- ❌ Error messages are cryptic or blame user

---

## Quick Troubleshooting Reference

### Problem: "My Gradio app won't launch"

**Check:**
1. Did you run the install cell? (`!pip install gradio pandas`)
2. Are you calling `demo.launch()` at the end?
3. Is the function name in `fn=` correct?
4. Try: Restart kernel and run all cells from top

---

### Problem: "AI generated code but it doesn't work"

**Diagnosis:**
- Does the error mention specific line numbers?
- Is it a syntax error (missing quotes, parentheses)?
- Is it a logic error (wrong exception type)?

**Steps:**
1. Read the error message carefully
2. Check the line it references
3. Try a more specific prompt to AI
4. If stuck, ask AI: "This code gives error [paste error]. How do I fix it?"

---

### Problem: "Error messages aren't showing in Gradio"

**Check:**
1. Is your function returning a string for text output?
2. For Part 4 (file output), are you returning None on errors?
3. Print debugging: Add `print()` statements before returns to verify code path

---

### Problem: "Test files not found"

**Check:**
1. Did you run the file creation cell?
2. Run the verification cell to check
3. Files must be in same directory as notebook
4. For Colab: Files might be in `/content/` directory

---

### Problem: "My exception isn't being caught"

**Check:**
1. Is it the right exception type? (Add `except Exception as e: print(e)` to debug)
2. Is general Exception before specific ones? (Re-order)
3. Is the error happening outside the try block?

---

### Problem: "Part 4 returns DataFrame not file"

**Fix:**
1. Save DataFrame: `df.to_csv('output.csv', index=False)`
2. Return the filename: `return 'output.csv'`
3. Make sure output component is `gr.File` not `gr.Dataframe`

---

## Tips for Different Student Levels

### Struggling Students

**Signs:**
- Can't get basic app working in Part 1
- Unclear what to test in Part 2
- Prompts are very vague

**Support Strategies:**
- Provide starter code for Part 1
- Work through one exception together as example
- Use step-by-step prompts from collapsible sections
- Pair with stronger student for Part 2 testing
- Focus on getting 3/5 edge cases working well

---

### Advanced Students

**Signs:**
- Finish early
- Add features not in requirements
- Ask "what about..." questions

**Extension Challenges:**
1. "Add validation for negative numbers"
2. "Handle multiple file uploads"
3. "Add a progress bar for large files"
4. "Log errors to a file for debugging"
5. "Create a custom exception class"
6. "Add unit tests for your error handling"

**Discussion Topics:**
- When is exception handling not the right tool?
- How would you handle errors in a production system?
- What's the difference between errors and warnings?

---

## Final Tips for Tutors

### Do's ✅
- Encourage experimentation and failure
- Celebrate when students find new edge cases
- Ask guiding questions rather than giving answers
- Recognize that AI output varies (multiple right answers)
- Make connections to real-world applications
- Emphasize the thinking process, not perfect code

### Don'ts ❌
- Don't write prompts for students
- Don't expect all students to use identical code
- Don't skip the "breaking things" phase
- Don't dismiss "weird" student questions about edge cases
- Don't prioritize speed over understanding
- Don't treat AI-generated code as gospel

---

## Additional Resources

### For Tutors:
- Python exception handling docs: https://docs.python.org/3/tutorial/errors.html
- Gradio documentation: https://gradio.app/docs/
- Common pandas errors: https://pandas.pydata.org/docs/reference/api/pandas.errors.html

### For Students:
- Quiz: `robustness-quiz.html`
- Flashcards: `robustness-flashcards.html`
- Python documentation on exceptions
- Gradio examples gallery

---

## Addressing the "AI Did It, Not Me" Concern

### The Fear
Some tutors worry: "If AI writes the code, what are students actually learning?"

### The Reality
Students ARE learning, just differently:

**Traditional Approach:**
- Student memorizes syntax
- Student types code character by character
- Student debugs syntax errors
- Learning = remembering how to write code

**AI-First Approach:**
- Student identifies problems conceptually
- Student articulates requirements clearly
- Student evaluates AI's solution
- Learning = critical thinking about what code should do

### What Students Actually Learn Here

**1. Problem Decomposition**
- Breaking "make it robust" into 5 specific edge cases
- Identifying what can go wrong before it does

**2. Requirements Specification**
- Translating fuzzy ideas into precise prompts
- Understanding that vague requirements → poor solutions

**3. Code Evaluation**
- Reading code to verify it handles all cases
- Recognizing when exception order is wrong
- Judging quality of error messages

**4. Testing Mindset**
- Adversarial testing (trying to break things)
- Systematic verification of edge cases
- Documentation of failure modes

**5. Iteration**
- Refining prompts when first attempt fails
- Debugging AI output
- Improving solutions incrementally

### Evidence of Learning

**Students demonstrate understanding when they:**
- Correctly identify edge cases without prompting (Part 2)
- Critique AI's code for missing exceptions (Part 3 evaluation)
- Refine prompts based on test results
- Explain WHY exception order matters
- Apply robustness thinking to new problems

**If a student can't do these things, they haven't learned—even if they have working code.**

---

## Discussion Prompts for Class Reflection

Use these to facilitate meaningful discussion:

### After Part 2 (Breaking Things):
1. "What surprised you most about how the app failed?"
2. "How did these error messages make you feel as a user?"
3. "What's the difference between a bug and an edge case?"
4. "Why do you think developers don't always handle these cases?"

### After Part 3 (Adding Error Handling):
1. "How did your prompting strategy evolve from first try to final version?"
2. "What made AI's code 'good enough' vs. 'not quite right'?"
3. "If you had to explain try-except to a friend, what analogy would you use?"
4. "What's harder: writing code or knowing what code to write?"

### After Part 4 (Complete Workflow):
1. "How is this different from projects you built in earlier weeks?"
2. "What would you need to add to deploy this app to real users?"
3. "Where in your other coursework could you apply robustness thinking?"
4. "What's one edge case we didn't cover that could still break this app?"

### Final Reflection:
1. "What does 'professional quality code' mean to you now?"
2. "How has AI changed your relationship with programming?"
3. "What's one robustness principle you'll take to your next project?"

---

## Week-Long Learning Arc

### Monday/Tuesday (Flipped Content):
**Student Does:**

- Watch concept videos
- Review slides on exception handling
- Read about try-except blocks
- Come to class with questions

**Tutor Prepares:**
- Review common misconceptions
- Prepare discussion prompts
- Test all code solutions
- Set up demo environment

### Wednesday/Thursday (Workshop):
**In Class:**

- Build and break apps together
- Practice prompting and iteration
- Facilitate testing and reflection
- Support struggling students
- Challenge advanced students

### Friday/Weekend (Consolidation):
**Student Does:**

- Complete reflection questions
- Take quiz for self-assessment
- Review flashcards
- (Optional) Extend app with new features
- Submit final project

**Tutor Does:**
- Grade submissions
- Provide personalized feedback
- Note common issues for next cohort
- Update materials as needed

---

## Measuring Success

### How do you know the workshop worked?

**Immediate Indicators (during class):**
- ✅ Students actively test edge cases in Part 2
- ✅ Prompts become more specific through Parts 3-4
- ✅ Students catch AI mistakes in evaluation exercise
- ✅ Discussions show conceptual understanding
- ✅ Students help each other debug prompts

**Post-Workshop Indicators:**
- ✅ Quiz scores show conceptual mastery
- ✅ Reflection essays demonstrate metacognition
- ✅ Students apply error handling to other projects
- ✅ Future projects show "what if?" thinking

**Long-Term Indicators:**
- ✅ Students build more robust apps in later modules
- ✅ Prompts in future weeks are more specific
- ✅ Code review discussions reference error handling
- ✅ Students catch edge cases peers miss

---

## Adapting for Different Contexts

### Online/Remote Workshop

**Challenges:**
- Harder to monitor individual progress
- Can't easily circulate between students
- Breakout rooms complicate Part 2 discussion

**Adaptations:**
- Use shared document for Part 2 observations
- Breakout rooms for Part 2 testing (3-4 students each)
- Use polls to check understanding at checkpoints
- Screen share for demonstration of key concepts
- Extended office hours for troubleshooting

### Large Class (>30 students)

**Challenges:**
- Can't help everyone individually
- Hard to facilitate whole-class discussion

**Adaptations:**
- Additional tutors/TAs assigned to sections
- Peer teaching: pair stronger/weaker students
- Designate "expert groups" for common issues
- Use online forum for async Q&A
- Pre-record common troubleshooting scenarios

### Accelerated Timeline (<90 min)

**Trim:**
- Combine Parts 3-4 (add error handling with download together)
- Reduce Part 2 testing to 3 core edge cases
- Move reflection to homework
- Provide pre-made test files (skip generation)

**Keep:**
- Part 2 breaking experience (essential!)
- AI evaluation exercise (crucial for learning)
- At least 3 exception types handled

### Extended Timeline (2+ sessions)

**Session 1:**
- Parts 1-3 (build → break → fix)
- End with working robust app

**Session 2:**
- Review Part 3 solutions
- Part 4 (add download)
- Extensions and advanced challenges
- Deeper discussion of robustness principles

**Between Sessions:**
- Students review exception types
- Complete quiz
- Study flashcards

---

## FAQ: Common Tutor Questions

### Q: "What if a student's AI generates completely wrong code?"

**A:** This is a learning opportunity!
- Don't fix it for them
- Ask: "What did you ask AI to do? What did it do instead?"
- Guide them to refine their prompt
- If truly stuck, suggest: "Try breaking your request into smaller steps"
- Last resort: Show example of good prompt (don't give exact prompt)

### Q: "Is it okay if students copy prompts from each other?"

**A:** Yes, with caveats:
- Sharing prompt strategies is fine (collaborative learning)
- Blindly copying without understanding is not
- Ask students who copied: "Can you explain what this prompt does?"
- Encourage: "How would you modify this prompt for a different problem?"

### Q: "What if AI generates code that works but is overly complex?"

**A:** Teachable moment!
- Discuss: "This works, but is it maintainable?"
- Ask: "Can you explain what each part does?"
- Challenge: "Can you prompt AI for a simpler version?"
- Introduce: "Sometimes simpler is better"

### Q: "Should I teach the syntax of try-except explicitly?"

**A:** Brief overview, not deep dive:
- Show structure once on board
- Emphasize concept (Plan A/Plan B)
- Students will learn syntax through use
- Focus on WHEN and WHY, not exact syntax

### Q: "How do I grade when everyone's code is different?"

**A:** Focus on outcomes, not code structure:
- Does it handle the edge cases? (functionality)
- Are error messages clear? (UX)
- Is exception order correct? (best practice)
- Did they test it? (process)
- Code differences are okay if criteria met

### Q: "What if students finish Part 4 with 30 minutes left?"

**A:** Extensions and deeper work:
- Implement extension challenges
- Help struggling students
- Lead advanced discussion on robustness
- Add additional edge cases
- Explore related topics (logging, custom exceptions)

### Q: "A student says 'AI makes programming too easy, why learn this?'"

**A:** Reframe what "learning programming" means:
- "Do architects need to know how to pour concrete?"
- Programming is problem-solving, not typing
- AI handles syntax; you handle strategy
- Ask: "Could you have built this without understanding exceptions?"
- The job market wants problem solvers who can leverage AI

### Q: "Should students be allowed to use ChatGPT/Claude during the workshop?"

**A:** Absolutely yes! That's the point:
- This is an AI-first course
- Real-world developers use AI assistants
- Skill is knowing HOW to use AI effectively
- Monitor for: understanding vs. blind copying

---

## Continuous Improvement

### After Each Workshop, Reflect On:

**What worked well?**
- Which explanations resonated?
- What discussions were most valuable?
- Where did students show "aha!" moments?

**What needs adjustment?**
- Where did students consistently struggle?
- Which parts took longer than expected?
- What questions came up repeatedly?

**What to change next time?**
- Add examples for common issues
- Adjust timing allocation
- Modify prompts for clarity
- Add/remove content

### Feedback Mechanisms:

**Quick Pulse Check (during workshop):**
- 👍/👎 hand signals at checkpoints
- "Red cup" system (red = need help, green = okay)
- Quick polls: "How confident do you feel?"

**End-of-Workshop Survey:**
- What was most valuable?
- What was most confusing?
- What would you change?
- Rate overall experience

**Follow-Up (next week):**
- "What from robustness workshop did you use?"
- "What questions do you still have?"
- Review quiz results for knowledge gaps

---

## Emergency Scenarios

### Scenario: "Nothing works for anyone"

**Likely Causes:**
- Library installation failed
- Gradio won't launch in environment
- File permissions issues

**Recovery Plan:**
1. Don't panic - stay calm
2. Switch to conceptual discussion of Parts 1-2
3. Demo working app from your screen
4. Assign troubleshooting as homework
5. Offer make-up session if needed
6. Focus on learning concepts even without running code

### Scenario: "Half the class is way behind"

**Likely Causes:**
- Part 2 testing took longer than expected
- Technical issues delayed some students
- Pace was too fast

**Recovery Plan:**
1. Pause for 5-10 min "catch-up time"
2. Fast finishers help those behind
3. Skip or shorten Part 5 reflection
4. Move some work to homework
5. Offer optional follow-up session

### Scenario: "Student says workshop is 'too easy' and is disruptive"

**Likely Cause:**
- Advanced student, already knows material
- Student isn't engaging deeply with concepts

**Response:**
1. Pull aside for 1-on-1 conversation
2. Challenge: "Have you implemented [extension challenges]?"
3. Assign: "Help three other students debug their code"
4. Deeper questions: "How would you handle [advanced edge case]?"
5. If truly ahead: Excuse to work on personal project

### Scenario: "AI keeps generating broken code for everyone"

**Likely Causes:**
- Service outage for AI provider
- Prompts are universally too vague
- Specific AI model struggling with task

**Recovery Plan:**
1. Provide working starter code
2. Focus on understanding existing code
3. Modify prompts to be more explicit
4. Use step-by-step approach instead of comprehensive
5. If persistent: Switch to manual coding session

---

## Success Stories to Share

Share these examples to motivate students:

### Real-World Impact of Good Error Handling:

**Example 1: E-commerce**
"A small online store lost $50,000 in sales because their checkout form crashed when users had apostrophes in their names (O'Brien, D'Angelo). One try-except block would have prevented this."

**Example 2: Healthcare**
"A hospital's patient portal showed cryptic errors when data was incomplete. After implementing better error handling with clear messages, patient satisfaction scores increased by 40%."

**Example 3: Student Project**
"A previous student built a grade calculator. Version 1 crashed if anyone uploaded the wrong file. After this workshop, they added error handling and won the showcase competition because their app was the most user-friendly."

---

## Closing Thoughts for Tutors

### Remember:

**This workshop is different.**
- It's not about memorizing syntax
- It's about developing professional judgment
- AI is a tool, not a crutch
- Struggle is part of learning

**Your role is:**
- Guide, not coder-in-chief
- Questioner, not answer-provider
- Facilitator, not lecturer
- Supporter, not rescuer

**Success looks like:**
- Students thinking critically about edge cases
- Students iterating on prompts independently
- Students testing comprehensively
- Students applying concepts to new contexts

**The bigger picture:**
You're teaching students to be **robust thinkers** who build **robust systems**. The try-except syntax is just a tool. The mindset—anticipating failure, planning for it, handling it gracefully—that's what will serve them throughout their careers.

### You've got this! 🎯

---

## Quick Start Checklist

**Before Workshop:**
- [ ] Review all solution code
- [ ] Test Gradio in your environment
- [ ] Prepare discussion prompts
- [ ] Have example AI prompts ready
- [ ] Create test files or test file creation script
- [ ] Review common student struggles section
- [ ] Prepare backup plan if technology fails

**During Workshop:**
- [ ] Set collaborative, experimental tone
- [ ] Emphasize Part 2 testing experience
- [ ] Monitor prompt quality in Part 3
- [ ] Facilitate AI evaluation discussion
- [ ] Support without solving
- [ ] Note issues for future improvement

**After Workshop:**
- [ ] Grade with rubric
- [ ] Provide specific feedback
- [ ] Collect student feedback
- [ ] Reflect on what to improve
- [ ] Celebrate successes!

---

**End of Instructor Guide**

*Good luck with the workshop! Remember: the goal isn't perfect code—it's robust thinking. Your students are learning to build systems that don't just work, but work well even when things go wrong. That's the mark of a professional developer.*

*Questions? Feedback? Please share with the teaching team so we can continuously improve these materials.*

---

## Appendix A: Glossary for Students

Provide this to students as reference:

**Exception:** An event during program execution that disrupts normal flow

**try block:** Code that might raise an exception (Plan A)

**except block:** Code that runs if specific exception occurs (Plan B)

**Robustness:** Ability to handle errors without crashing

**Edge case:** Unusual input that might break code

**Graceful degradation:** Handling errors with helpful feedback instead of crashing

**User-friendly error:** Clear message that tells users what went wrong and how to fix it

**ParserError:** Pandas can't read file as valid CSV

**KeyError:** Requested dictionary key/column doesn't exist

**ValueError:** Function receives wrong value type

**TypeError:** Operation used on wrong data type

**FileNotFoundError:** Requested file doesn't exist

---

## Appendix B: One-Page Student Handout

```
ROBUSTNESS CHECKLIST
====================

BEFORE BUILDING:
□ List 3-5 things that could go wrong
□ Plan what to tell users for each problem

WHILE BUILDING:
□ Put risky code in try blocks
□ Catch specific exceptions (not just Exception)
□ Order: specific exceptions → general Exception
□ Return clear, helpful error messages

AFTER BUILDING:
□ Test with valid data (happy path)
□ Test with each "what if?" scenario
□ Verify error messages make sense
□ Check that app never crashes

ERROR MESSAGE FORMULA:
"Error: [What went wrong]. [How to fix it]."

Example: "Error: CSV must contain 'quantity' and 'price' columns. Please check your file and try again."

AI PROMPTING TIPS:
✓ List ALL edge cases explicitly
✓ Specify exception types by name
✓ Request user-friendly messages
✓ Test and refine your prompt

REMEMBER:
Professional code doesn't just work—
it works even when things go wrong.
```

---

**Version:** 1.0  
**Last Updated:** 2025  
**Author:** Michael Borck  
**Course:** AI-First Programming - Module 10