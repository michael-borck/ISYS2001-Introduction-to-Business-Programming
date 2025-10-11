---
format:
  pdf:
    toc: true
    number-sections: false
    colorlinks: true
  docx:
    toc: true
    number-sections: false
    highlight-style: github
  html:
    toc: true
    toc-expand: 2
    embed-resources: true
---

# ISYS2001 - AI-Assisted Python Programming - Final Exam Marking Guide

**Purpose:** This guide provides a consistent framework for remote lecturers and tutors to mark the final assessment, ensuring fairness and adherence to course objectives. It aligns directly with the provided assessment rubric and explicitly references course materials where applicable.

-----

## **General Marking Principles for Tutors**

* **Focus on Process over Product:** A significant portion of marks is allocated to the student's process of AI interaction, critical analysis, and adherence to course-taught techniques, not just the final working code.
* **Course Constraint Enforcement:** **Strictly enforce the "All code must use ONLY techniques taught during this semester."** Any use of concepts not covered in the specified weeks for each section **will result in zero marks for that specific section/component.**
* **Academic Integrity:** Pay close attention to the `conversation_log.txt`. It should demonstrate genuine iterative prompting, critical thinking, and modification of AI output to fit constraints. Look for instances where students *had* to modify AI suggestions.
* **Clarity and Citations:** Ensure all course references are explicit and correctly formatted. Misrepresenting or fabricating information from sources should be penalised.
* **GitHub Workflow:** Verify the private repository setup, naming convention, and regular commits. The commit history should reflect progressive work.
* **Doctests:** Check that doctest examples are included for all functions where specified, following the Week 9 format.

-----

## **Section 1: Iterative Prompt Engineering (30 marks)**

**Objective:** Assess the student's ability to use iterative prompting for planning and critical analysis with course references.

| Component | Marks | Criteria | Marking Guidance |
| :-------- | :---- | :------- | :--------------- |
| **1.1 Initial Prompt & Pseudocode** | 8 | Clear problem statement (3), Complete request (3), AI response quality (2) | **Prompt (6 marks):** Look for clear request for structured pseudocode for a CLI Task Manager. Problem statement is clear, includes Add, List, Remove tasks, and storage in memory. Mentions only course-taught techniques.<br>**AI Response (2 marks):** Does the pseudocode reflect a structured outline? Is it reasonably coherent based on the prompt?<br>**Course Reference:** Must state "I used the planning method from **Module 3: Computational Thinking and Algorithm Design / Simplified Development Methodology** " |
| **1.2 Two Prompt Refinements** | 12 | Meaningful improvements (6), Specific clarifications (6) | For *each* refinement (6 marks per refinement):<br>**Refined Prompt (3 marks):** Does it add specificity (e.g., error handling for invalid input, loop for menu, basic file persistence if mentioned)? Does it address overlooked requirements from initial prompt?<br>**AI's Updated Pseudocode (1.5 marks):** Does the AI's pseudocode reflect the refinement?<br>**Course Reference (1.5 marks):** Must explicitly state which concept from which week was applied (e.g., "This refinement applied **input validation** from **Week 6: Debug & Correct**"  or "This refinement applied **basic exception handling patterns** from **Week 8: Mastering Exception Management**"). |
| **1.3 Critical Analysis with Course References** | 10 | Analysis depth (5), Course material references (5) | **Analysis Depth (5 marks):** Is the analysis insightful? Does it explain *how* prompts evolved and *why* changes were made? Does it critically evaluate AI's strengths/weaknesses in this process?<br>**Course References (5 marks):**<br>- At least **3 specific references** to weeks/topics are required (e.g., "My approach was influenced by **Week 3: Computational Thinking and Algorithm Design**  on problem decomposition").<br>- Explains how refinements applied course concepts (e.g., "My second refinement to ensure valid user input applied the **input validation principles** from **Week 6: Debug & Correct** ").<br>- Connects final pseudocode to specific course learning (e.g., "The iterative menu system in my final pseudocode directly reflects the **'Repeat: Loops and Iteration' foundation** from **Week 5**  and the **menu design principles** from **Week 4: Designing a Simple Menu** "). |

-----

## **Section 2: Debug & Correct with AI (25 marks)**

**Objective:** Assess the student's ability to identify and fix errors using AI, and manually rewrite corrected code adhering to course constraints with doctests.

| Component | Marks | Criteria | Marking Guidance |
| :-------- | :---- | :------- | :--------------- |
| **2.1 Error Identification** | 10 | Completeness (6), AI interaction quality (4) | **Error Completeness (6 marks):** Student's prompt should ask AI to identify *all three* (or more) errors. Full marks for identifying all. Partial marks for identifying some.<br>- **Error 1: `tas` typo** in `remove_task` function.<br>- **Error 2: `task` variable** in `list_tasks` function.<br>- **Error 3: `list_task()` typo** in `main` function.<br>**AI Interaction Quality (4 marks):** Does the prompt clearly present the buggy code and ask for specific error identification? Is the AI's response quoted completely?<br>**Course Reference:** Must state "I applied the debugging approach from **Week 6: Debug & Correct / Debugging Prompts**  or **Module 12: Mastering Debugging** ". |
| **2.2 Fix & Manual Rewrite** | 15 | Correct fixes (8), Course-appropriate complexity (4), Hand-coding accuracy (3) | **Correct Fixes (8 marks):** All identified errors are correctly fixed in the rewritten code. (Each fix ~2.5 marks).<br>**Course-Appropriate Complexity (4 marks):** Code uses only Week 6 level concepts (lists, functions, `if`/`else`, `for` loops, `enumerate`). No advanced features like specific exception types, complex data structures, or OOP.<br>**Hand-coding Accuracy (3 marks):** The manually rewritten code is accurate and free of new typos or errors introduced during transcription.<br>**Doctest Examples (Mandatory - check each function):** Each function (`add_task`, `remove_task`, `list_tasks`) *must* have doctest examples following Week 9 format . Look for at least one positive and one negative test case for `remove_task`.<br>**Comments:** Comments explaining fixes.<br>**Course References:** "My error handling approach comes from **Week 8: Mastering Exception Management / Basic Exception Handling Syntax**  (though Week 6 context is simpler)." and "My testing approach follows **Week 9: Python Testing Frameworks / Introduction to Doctest** ". |

-----

## **Section 3: Debug & Refine WeatherWise API (20 marks)**

**Objective:** Assess the student's ability to analyse issues, refine code with specific error handling constraints, and compare implementations.

| Component | Marks | Criteria | Marking Guidance |
| :-------- | :---- | :------- | :--------------- |
| **3.1 Issue Analysis with Course Connection** | 6 | Identifies 3+ issues (3), Course concept application (3) | **Identifies 3+ problems (3 marks):**<br>1. Overly general `except:` block.<br>2. No specific exception types caught.<br>3. Lack of explicit input validation for `city`.<br>4. `print("Error occurred")` is uninformative.<br>5. Direct dictionary access without checking for key existence.<br>6. No handling for non-JSON responses.<br>**Course Concept Application (3 marks):** For each problem, correctly references a course week/concept that provides a solution approach (e.g., "Problem: Overly general `except:`. Solution concept: **Specific exception types** from **Week 8: Mastering Exception Management / Python's Exception Hierarchy** ").<br>**Prompt to AI (no marks, but required):** Ensure student quotes prompt "Review this function using only error handling techniques taught in an introductory programming course (basic try/except only)." |
| **3.2 Function Refinement with Course Constraints** | 10 | Working code (6), Week 8 error handling only (4) | **Working Code (6 marks):** The `refined_safe_weather_data_fetch` function should be functional and retrieve weather data when valid input is provided.<br>**Week 8 Error Handling (4 marks):**<br>- **Basic try/except blocks (no specific types):** Must adhere strictly to general `except:` blocks as per Week 8. No `ValueError`, `KeyError`, `requests.exceptions.RequestException` etc., in `except` clauses.<br>- **Simple input validation:** Uses `if not city:` for empty city name.<br>- **Print statements for errors:** Uses `print()` for all error messages.<br>- **Return None or dict:** Consistently returns `None` on failure or a dictionary on success.<br>**Doctest Examples (Mandatory - 2 marks):** Must include provided doctest examples for empty city and skipped invalid city, following Week 9 format . |
| **3.3 Comparison Analysis** | 4 | Similarities/differences (2), Pros/cons (2) | **2 Similarities (1 mark):**<br>- Both use `try/except` for error handling.<br>- Both attempt to fetch JSON data from `wttr.in`.<br>- Both return structured data or `None` on failure.<br>**2 Differences (1 mark):**<br>- Refined uses general `except:`, ideal uses specific exceptions.<br>- Refined uses simple validation, ideal has more robust data extraction with nested try.<br>- Ideal attempts to extract data more safely with explicit checks for `current_condition`.<br>**1 Course Connection (1 mark):** States how the student's version demonstrates a **Week 8 concept** (e.g., "My refined version best demonstrates **basic exception handling patterns** and **input validation** as taught in **Week 8: Mastering Exception Management**  and **Week 6: Debug & Correct** ").<br>**1 Improvement Area (1 mark):** Identifies one improvement for the refined version after reviewing **Textbook Chapter 6** (which corresponds to Week 8's "Mastering Exception Management" ). Example: "I would add specific exception types to handle different error scenarios more precisely, as discussed in **Week 8: Mastering Exception Management** ." |

-----

## **Section 4: Manual Implementation & Course Reflection (25 marks)**

**Objective:** Assess manual coding ability within strict constraints and the student's metacognitive reflection on the course.

| Component | Marks | Criteria | Marking Guidance |
| :-------- | :---- | :------- | :--------------- |
| **4.1 Manual Implementation with Course Constraints** | 15 | Functional code (8), Course constraints followed (4), Clear commenting (3) | **Functional Code (8 marks):**<br>- `display_menu()`: Prints the menu as specified.<br>- `get_user_choice()`: Prompts user, gets input, and validates it (e.g., checks if choice is within menu range).<br>- `main()`: Implements a basic loop structure that calls `display_menu` and `get_user_choice`, and simulates task manager operations based on choice.<br>**Course Constraints Followed (4 marks):**<br>- **ONLY Week 4-6 techniques:** Basic `input()`, `print()`, simple `while` loops, basic `if/else`.<br>- **No PyInputPlus**, no external libraries beyond `doctest` (for tests).<br>- **No complex data structures** (basic lists/dictionaries are okay for data storage).<br>- **No advanced error handling.**<br>**Clear Commenting (3 marks):** Code is well-commented, with references to specific course concepts used (e.g., "Uses `while True` for menu loop - **Week 5: The Power of Repetition** ").<br>**Doctest Examples (Mandatory - 3 marks for each testable function):** `display_menu()` (with `+SKIP`) and `get_user_choice()` (with `+SKIP`) must have doctests following Week 9 format . `main()` does not require a doctest. |
| **4.2 Course-Connected Reflection** | 10 | Workflow analysis (3), Course learning connections (4), Future application (3) | **Word Count:** Must be exactly 200 words (or very close). Penalise for significantly over/under.<br>**Workflow Balance (~70 words - 3 marks):** Discusses how human planning (e.g., **Week 3: Computational Thinking / Simplified Development Methodology** ) and AI assistance were balanced. Reference concepts like "iterative design" .<br>**Course Concept Application (~70 words - 4 marks):**<br>- Identifies one moment of **"Error Handling Mindset"** (from **Week 8: Mastering Exception Management** ) e.g., anticipating invalid user input, or dealing with API errors.<br>- Identifies one moment of **"Defensive Programming"** (from **Week 6: Debug & Correct** / **Week 8: Mastering Exception Management** ) e.g., validating input, checking if lists are empty before processing.<br>- Connects these to testing experience.<br>**Learning Transfer (~60 words - 3 marks):** Explains how **"iterative refinement process"**  will be applied to the final project (e.g., repeatedly refining AI prompts). References one specific technique from **Assignment 2 feedback** that will be improved using this approach (e.g., "breaking down complex problems into smaller, manageable parts" ).<br>**Format:** Bold specific week/document references. Uses course terminology. Connects to *actual* course experience. |

-----

## **Overall Feedback Suggestions**

### **Poor Assessment (Grade Fail):**

* **Code Issues:** Frequent syntax errors, logical errors, significant portions of code non-functional or missing.
* **Constraint Violation:** Clear use of advanced Python features not taught (e.g., specific exception types when only general `except` was allowed, PyInputPlus when forbidden). This is a critical fail.
* **AI Interaction:** Prompts are vague ("write the code for me"), no iterative refinement, AI responses are simply copied without modification. `conversation_log.txt` is sparse or shows little critical engagement.
* **Analysis/Reflection:** Lacks depth, generic statements, no specific course references, or misrepresents course content.
* **Submission Issues:** Repository not set up correctly, missing files, no doctests.

### **Good Assessment (Grade Pass/Credit):**

* **Code Issues:** Code is mostly functional with minor bugs. Adheres to most course constraints, but may have minor slips.
* **AI Interaction:** Shows attempt at iterative prompting, asks for clarification. AI responses are generally modified, but the `conversation_log.txt` might be less detailed or lack strong examples of critical evaluation.
* **Analysis/Reflection:** Attempts to connect to course materials but references might be a bit general or lack deep explanation. Reflections are present but could be more insightful.
* **Submission Issues:** Repository is mostly correct, doctests are present but might not be comprehensive.

### **Excellent Assessment (Grade Distinction):**

* **Code Issues:** All code is functional, clean, and strictly adheres to all specified course constraints. Displays a strong understanding of Python fundamentals.
* **AI Interaction:** Prompts are precise, demonstrates clear iterative refinement, and actively guides the AI. The `conversation_log.txt` clearly shows instances of critical evaluation, where the student identified AI's flaws or overly complex suggestions and directed the AI to correct them within course constraints.
* **Analysis/Reflection:** Deep, insightful analysis of the prompting process and code evolution. Explicitly references specific course concepts (week numbers, module names, exact techniques from handouts/lectures) and demonstrates sophisticated understanding of the iterative learning process.

-----

## **Process Over Product: A Key Assessment Philosophy**

This marking guide emphasises that assessment is fundamentally about evaluating how students learn and interact with AI tools, not just the final code output. This distinction is crucial for AI-assisted learning evaluation.

### **How the Rubric Differentiates Between "AI Answer" and "Student Work"**

The rubric is specifically designed to move beyond checking for correct code. It heavily weights components that require human critical thinking, iterative refinement, and understanding of course constraints, which AI cannot fully replicate without explicit, detailed human guidance.

#### **"AI-Answer" Indicators (Pass Level / Satisfactory):**
* Basic prompts that receive standard, generic responses
* Simple copying of AI-generated code with minimal modification
* Limited evidence of constraint enforcement or critical evaluation
* Generic analysis without specific course connections
* Sparse conversation logs showing minimal iterative refinement

#### **"Student Work" Indicators (High Excellent Level):**
* **Sophisticated prompting:** Demonstrates understanding of what AI needs and course constraints
* **Active constraint enforcement:** Clear evidence where student modified AI suggestions to fit course limitations
* **Iterative refinement:** Rich conversation logs showing problem identification, targeted follow-up prompts, and continuous improvement
* **Critical analysis:** Deep reflection on the prompting process with specific course concept applications
* **Metacognitive awareness:** Genuine personal reflection on learning journey and skill development

### **Key Marking Differentiators**

1. **Iterative Prompt Engineering (Section 1):** Look for evidence that students actively guided AI through multiple refinements, not just accepted first responses.

2. **Constraint Adherence (All Sections):** Students demonstrating high achievement will show clear instances where they rejected or modified AI suggestions that exceeded course boundaries.

3. **Course Integration:** Excellent work explicitly connects actions and decisions to specific weeks, concepts, and learning objectives rather than generic programming principles.

4. **Personal Reflection:** The best reflections demonstrate genuine metacognitive awareness about the student's own learning process and skill development.

### **For Tutors: Identifying Authentic Student Engagement**

**Red Flags (Lower Grades):**
* Conversation logs with only basic prompts and no follow-up questions
* Code that uses techniques clearly beyond the specified week constraints
* Analysis that could apply to any programming task (not course-specific)
* Reflections that sound generic rather than personally experienced

**Green Flags (Higher Grades):**
* Evidence of students "arguing" with AI to stay within constraints
* Multiple iterations showing progressive refinement
* Specific references to actual course materials and personal learning moments
* Code comments that reference exact course concepts and justify decisions

This philosophy ensures that students cannot achieve high marks simply by having AI complete their work, but must demonstrate genuine engagement with both the AI tool and the course learning objectives.