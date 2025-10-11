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

# Week 5 Key Takeaways: Functions & Modules for Tutors

## Quick Overview for Lab Preparation

**Theme:** Modularity in Python - Building reusable finance-focused functions and using external libraries

**Student Level:** Information Systems majors, intermediate Python (after loops and conditionals)

**Lab Focus:** Interactive practice with function design and module integration for business applications

---

## Core Learning Objectives

### 1. Functions Fundamentals
- **What:** Creating reusable code blocks that perform specific tasks
- **Why:** Essential for building professional business applications
- **Key Concept:** Functions are the building blocks of modular programming

### 2. Parameters & Arguments
- **What:** Passing data into functions to make them flexible
- **Business Example:** Loan calculator needs principal, rate, time as inputs
- **Key Distinction:** Parameters (in definition) vs Arguments (actual values passed)

### 3. Return Values vs Printing
- **Critical Concept:** Return values enable function composition
- **Business Impact:** Returned loan payment can feed into budget analysis
- **Professional Practice:** Functions should return values, not just print

### 4. Python Modules for Business
- **datetime:** Timestamping transactions, financial reporting
- **csv:** Data import/export for business applications  
- **math/decimal:** Precise financial calculations
- **Custom modules:** Student-created function libraries

---

## Lab Activity Suggestions

### Warm-up (10 minutes)
**Function Design Challenge:**
```python
# Ask students to design (not implement) a function for:
def calculate_tip(bill_amount, tip_percentage):
    # What should this return? Why not print?
    pass
```

### Main Activity (30 minutes)
**Modular Finance Toolkit:**
1. Students create 2-3 related functions (tip calculator, budget analyser)
2. Practice using returned values from one function in another
3. Add timestamp using datetime module
4. Save results using csv module

### Discussion Points (10 minutes)
- "When would you use return vs print in a business app?"
- "How do modules help you avoid 'reinventing the wheel'?"
- "What business problems could benefit from modular functions?"

---

## Common Student Struggles & Solutions

### Problem 1: "When to use return vs print?"
**Quick Rule:** If another function needs the result, return it. If humans need to see it, print the returned value.

### Problem 2: "Import errors with modules"
**Common Fix:** `import datetime` then `datetime.datetime.now()` vs `from datetime import datetime` then `datetime.now()`

### Problem 3: "Functions seem unnecessary for simple tasks"
**Reframe:** Show how loan payment function can be reused in multiple contexts (budget analysis, financial planning, reporting)

---

## Mini-Project Context

**Finance Toolkit Theme:** Students build a modular personal finance system
- Functions for calculations (tip, loan payments, ROI)
- Modules for data handling (datetime stamps, CSV export)
- Cell-based modularity in Google Colab (functions defined in one cell, used in others)

**AI Integration:** Students learn to describe function requirements to AI and evaluate generated code

---

## Questions to Engage Prepared Students

1. "What business processes in your family/work could benefit from modular functions?"
2. "How might AI tools help you discover relevant Python modules for business problems?"
3. "What's the difference between building everything from scratch vs using existing modules?"
4. "How do return values enable 'function composition' in business applications?"

---

## Quick Assessment Ideas

### Formative Check (during lab):
- "Sketch the parameters needed for a budget analysis function"
- "Explain why a loan calculator should return a value rather than print it"

### Exit Ticket:
- "Name two Python modules useful for business applications and explain why"
- "What's one way functions make code more professional?"

---

## Materials Status

✅ **Available Now:**

- 4 enhanced learning modules (markdown → slides)
- 2 enhanced worksheets with business examples
- Interactive quiz (10 questions)
- Interactive function builder tool
- Complete mini-project specification

✅ **Key Features:**

- Finance theme throughout (no more generic "hello world")
- AI collaboration context for modern development
- Google Colab compatibility (cell-based, no file imports)
- Progressive difficulty building to final project

---

## Emergency Backup Plan

**If students arrive unprepared:**

1. **5-minute concept intro:** "Functions are like business processes - they take inputs, do work, produce outputs"
2. **Live coding demo:** Create simple tip calculator showing parameters → processing → return value
3. **Pair programming:** One student describes business problem, other implements function
4. **Focus on practical value:** How this week's concepts apply to their future careers

---

**If Stuck:** Focus on the "why" - modularity enables the professional applications they'll build in later weeks.

---

*This week builds the foundation for Week 8's data visualisation and the final dashboard project. Functions become their business logic toolkit!*