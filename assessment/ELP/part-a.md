---
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

# Assessment 3: Part A: The Project Tour v2.1

## ISYS2001 Introduction to Business Programming

## Part A Screencast Component

**Duration:** 5-7 minutes  
**Format:** Video screencast with webcam overlay
**This is a required component of your video submission**

> This is a supporting document for Assessment 3. For the complete assessment overview, submission requirements, and marking criteria, see the **"Assessment 3: Master Specification"** document.

---

## Overview

Part A is a guided walkthrough of your final project. This is your opportunity to demonstrate what you built, explain how it works, and showcase your code in action. Think of this as giving a colleague or potential employer a tour of your work.

**This section is the same for all students.** Everyone completes Part A before moving on to answer their randomly assigned questions in Part B.

---

## How Part A Relates to Part B

Your Project Tour (Part A) introduces **what** you built and **how** it works. Some Part B questions will ask you to dive deeper into topics you introduce here.

**Think of it this way:**

- **Part A** = Show and tell: "Here's my code structure, here's why I organised it this way"
- **Part B** = Deep analysis: "What alternatives did I consider? What are the trade-offs? What would I change?"

**If you receive a Part B question related to something you covered in Part A:**

- Don't just repeat your Part A explanation
- Briefly acknowledge what you showed earlier: "As I demonstrated in my project tour..."
- Then go deeper: discuss alternatives, trade-offs, limitations, or technical details you didn't cover initially

**In Part A, aim for:**

- Clear overview of your architecture and key components
- Brief justification of major choices (1-2 sentences per decision)
- Focus on demonstrating working functionality

**Save for Part B:**

- Detailed comparison of alternative approaches
- Discussion of trade-offs and what you'd do differently
- Critical analysis of limitations and weaknesses
- Technical depth on algorithms and performance considerations

This separation ensures you don't run out of time in Part A, and it gives you room to show deeper analysis in Part B.

---

## What You Must Cover

Your Project Tour must include three distinct elements:

### 1. Introduction (30-60 seconds)

Briefly set the context for your project:

**What to include:**

- What does your project do? (One or two sentences)
- What problem does it solve or what purpose does it serve?
- What are the key features a user can expect?

**Example opening:**
*"This is a student grade tracking system for teachers. It allows teachers to import class lists, record assessment marks, calculate final grades, and generate progress reports. The three key features are CSV import, automatic grade calculation, and PDF report generation."*

**What to avoid:**

- ❌ Long backstory about why you chose this project
- ❌ Detailed explanation of assignment requirements
- ❌ Apologies or disclaimers ("This isn't perfect but...")

---

### 2. Code Structure Walkthrough (2-3 minutes)

This is the heart of Part A. Open your code and take us through its architecture.

**What to show and explain:**

#### **File/Module Organisation**

- Show your project file structure (in your IDE or file explorer)
- Explain how you organised your code (single file vs. multiple modules)
- Justify why you structured it this way

*Example: "I split my code into three main files. main.py handles the user interface and program flow, data_manager.py handles all file operations and data storage, and calculator.py contains all the grade calculation logic. This separation means I can test each component independently."*

#### **Key Functions or Classes (choose 2-3)**

- Open your main code file(s)
- Highlight 2-3 of your most important functions or classes
- For each one, briefly explain:
  - What it does
  - Why it's important to your program
  - Any interesting implementation details

*Example: "This is my calculate_final_grade function starting at line 87. It takes a student's assessment scores as a dictionary and returns their final weighted grade. The interesting part is how it handles missing assessments here on line 94—rather than crashing, it uses the average of their completed work."*

#### **Design Decisions**

- Discuss at least ONE significant design choice you made
- Explain what alternatives you considered
- Justify why you chose your approach

*Example: "I chose to store all student data in a dictionary with student ID as the key, rather than a list of objects. This gives me O(1) lookup when searching for students, which matters because teachers will be searching by ID frequently. The trade-off is that maintaining sorted order requires extra work."*

**What to avoid:**
- ❌ Reading code line-by-line without explaining the "why"
- ❌ Showing every single function (focus on the key ones)
- ❌ Getting lost in minor implementation details
- ❌ Static slides or diagrams instead of actual code

---

### 3. Live Demonstration (2-3 minutes)

Run your program and show it working with real input.

**What to demonstrate:**

#### **Core Functionality**

- Launch your program and show the main interface
- Walk through a typical user workflow
- Demonstrate your program's primary features working

*Example: "Let me run the program. Here's the main menu. I'll select option 2 to import a CSV file. I'm loading this sample class list with 15 students. You can see it's now displaying the student roster. Now I'll add some assessment marks... and here you can see the grades are automatically calculated and displayed."*

#### **Show, Don't Just Tell**

- Actually interact with your program on screen
- Show real inputs and outputs
- If your program produces files, show those files opening/being created
- If you have a GUI, click through the interface
- If it's command-line, type actual commands

#### **Highlight Key Features**

- Pick 2-3 features that best demonstrate your programming skills
- Show these working in real-time
- Briefly narrate what's happening behind the scenes

*Example: "When I click 'Generate Report', you can see the progress bar—this is because the PDF generation takes a few seconds. And here's the PDF that was just created. You can see it includes all the student data we entered, properly formatted with their final grades."*

**What to avoid:**

- ❌ Just describing what your program "would do"
- ❌ Showing fake/mock screens instead of the real program
- ❌ Saying "and it does this..." without actually showing it
- ❌ Getting stuck on bugs (if something breaks, acknowledge it briefly and move on)

---

## Success Criteria for Part A

Your Project Tour will be assessed on:

| Criterion | What We're Looking For |
|-----------|------------------------|
| **Clarity of Explanation** | Can we understand what your project does and how it works? Is your narration clear and well-organised? |
| **Code Understanding** | Do you demonstrate genuine understanding of your own code structure and design choices? |
| **Demonstration Quality** | Does your program actually work? Do you show real functionality rather than just describing it? |
| **Design Justification** | Can you explain *why* you made specific architectural or implementation choices? |

---

## Common Mistakes to Avoid

❌ **Starting with apologies:** "This probably isn't very good..." or "I ran out of time to..."  
✅ **Start confidently:** Present your work as-is and let it speak for itself

❌ **Reading code word-for-word:** Going through your code line-by-line without context  
✅ **Explain at the right level:** Focus on the logic and purpose, not every syntax detail

❌ **Hiding behind slides:** Using PowerPoint to describe your code instead of showing actual code  
✅ **Show real code:** Open your actual files in your IDE and walk through them

❌ **Static demo:** Just showing screenshots of your program  
✅ **Live interaction:** Actually run your program and interact with it

❌ **Excessive detail on trivial parts:** Spending a minute explaining how you formatted your print statements  
✅ **Focus on what matters:** Prioritize architectural decisions and core algorithms

❌ **Rushing the demo:** "And it works, moving on..."  
✅ **Actually demonstrate:** Take time to show your program functioning properly

---

## Time Management Tips

This is a 5-7 minute section, so manage your time wisely:

- **Introduction:** 30-60 seconds maximum
- **Code Walkthrough:** 2-3 minutes (this is where most time should be spent)
- **Live Demo:** 2-3 minutes (show it actually working)

**Practice tip:** Do a timed run-through before your final recording. Many students underestimate how long it takes to properly demonstrate their code.

---

## Preparing Your Project Tour

### Before Recording

1. **Clean up your code workspace**
   - Close unnecessary files/tabs
   - Have your main files ready to display
   - Test that your program runs without errors

2. **Plan your narrative**
   - Decide which 2-3 functions/classes you'll highlight
   - Identify 1-2 design decisions you'll discuss
   - Plan which features you'll demonstrate live

3. **Prepare test data**
   - Have sample input files ready if needed
   - Know what inputs you'll use in your demo
   - Make sure your demo will complete in 2-3 minutes

4. **Do a practice run**
   - Record a practice version
   - Check that you're staying within 5-7 minutes
   - Verify your screen and audio quality

### During Recording

- **Use your cursor** to point to specific lines of code
- **Speak naturally** as if explaining to a friend
- **Navigate confidently** through your files
- **Show enthusiasm** for what you built
- **Be authentic** about both strengths and limitations

---

## Examples of Effective Language

**When introducing your project:**

- ✅ "This program helps teachers track and analyse student performance."
- ❌ "For this assignment we had to make a program that..."

**When explaining code structure:**

- ✅ "I separated the data handling into its own module because it made testing easier and kept my main file cleaner."
- ❌ "I have some files and they do different things."

**When showing your code:**

- ✅ "This function on line 45 is critical because it validates all user input before processing. Without this, the program could crash on invalid data."
- ❌ "Here's a function I wrote."

**When demonstrating:**

- ✅ "I'm going to import this sample dataset. You can see the loading indicator, and now the data appears in the table. Let me show you what happens when I filter by grade..."
- ❌ "And when you run it, it works."

**When discussing design:**

- ✅ "I chose to use a dictionary here instead of a list because I needed fast lookups by student ID. With a list, I'd be doing linear search every time, but with a dictionary it's constant time."
- ❌ "I used a dictionary because it's better."

---

## Remember

Part A demonstrates **what you built and how it works**. Part B (the question bank responses) demonstrates **why you built it that way and what you understand**. Both parts together create a complete picture of your competence.

**Your Project Tour should make someone watching think:** *"This person clearly understands what they've built and can explain it professionally."*

---

## Checklist Before You Submit

Use this checklist to ensure your Part A is complete:

- [ ] My video is 5-7 minutes long (not too short, not too long)
- [ ] I introduced my project and explained its purpose
- [ ] I showed my actual code files on screen
- [ ] I explained my project's structure/organisation
- [ ] I walked through 2-3 key functions or classes
- [ ] I discussed at least one design decision I made
- [ ] I ran my program and demonstrated it working
- [ ] I showed real functionality, not just descriptions
- [ ] My face is visible via webcam throughout
- [ ] My audio is clear and understandable
- [ ] I spoke naturally and confidently about my work

---

**Next:** After completing Part A, proceed to Part B where you will answer your randomly assigned questions from the question bank.

Good luck with your Project Tour!

---

*Project Tour v2.1| Released Thursday 22 October 2025*

Change Log:

- v2.0 (15 Oct 2025): Initial release
- v2.1 (22 Oct 2025): Minor wording updates for clarity