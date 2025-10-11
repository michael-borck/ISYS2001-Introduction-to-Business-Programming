---
format: 
  pptx: default
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
# Week 6 Mini-Project Assessment Rubric
## Dictionary-Enhanced Finance Tracker

**Assessment Type:** Formative Assessment  
**Duration:** 1-2 hours  
**Focus:** Application of dictionary concepts to financial data management

---

## Overview

This rubric assesses student mastery of dictionary concepts through practical application in a finance tracker project. Students choose between two pathways (Extend Week 5 or Fresh Start) and demonstrate dictionary usage in real-world scenarios.

### Assessment Philosophy
- **Formative Focus**: Emphasises learning and improvement over grading
- **Application-Based**: Students demonstrate understanding through working code
- **Choice-Driven**: Multiple pathways accommodate different student situations
- **Dictionary-Centric**: Specifically evaluates dictionary concept mastery

---

## Core Assessment Criteria

### **Criterion 1: Dictionary Structure Design (25 points)**

| Performance Level | Points | Description | Evidence to Look For |
|-------------------|--------|-------------|---------------------|
| **Excellent (23-25)** | A+ | Creates logical, well-organised nested dictionary structures that clearly group related data | • Uses meaningful key names<br>• Logical hierarchy (user_profile, expenses, categories, etc.)<br>• Consistent structure throughout<br>• Easy to understand and maintain |
| **Proficient (20-22)** | A | Creates functional dictionary structures with minor organisational issues | • Most keys are meaningful<br>• Generally logical grouping<br>• Some minor inconsistencies<br>• Structure supports required functionality |
| **Developing (17-19)** | B | Creates basic dictionary structures but with unclear organisation or poor key choices | • Some unclear or poorly named keys<br>• Basic functionality works<br>• Structure could be more logical<br>• Shows understanding but needs refinement |
| **Beginning (10-16)** | C | Creates dictionaries but structure is confusing or overly complex | • Confusing key names<br>• Poor data organisation<br>• Structure makes code harder to understand<br>• Basic dictionary creation attempted |
| **Incomplete (0-9)** | F | No clear dictionary structure or major structural problems | • No coherent structure<br>• Major errors in dictionary creation<br>• Cannot demonstrate basic organisation |

**Assessment Notes:**
- Look for logical grouping of related data (expenses with expense details, categories with budget info)
- Check if structure supports the required functionality without unnecessary complexity
- Evaluate whether another programmer could easily understand the data organisation

---

### **Criterion 2: Dictionary Operations Mastery (25 points)**

| Performance Level | Points | Description | Evidence to Look For |
|-------------------|--------|-------------|---------------------|
| **Excellent (23-25)** | A+ | Demonstrates sophisticated use of dictionary operations including safe access, dynamic updates, and complex manipulations | • Consistent use of `.get()` for safe access<br>• Dynamic key creation and management<br>• Complex operations like filtering and aggregation<br>• Error handling for missing keys |
| **Proficient (20-22)** | A | Uses core dictionary operations correctly with occasional advanced techniques | • Uses `.get()` method appropriately<br>• Can add, update, and delete entries<br>• Some advanced operations attempted<br>• Generally safe coding practices |
| **Developing (17-19)** | B | Uses basic dictionary operations but may lack safe access patterns or advanced techniques | • Basic access using `dict[key]` mostly works<br>• Can perform simple add/update operations<br>• Limited use of `.get()` or other safe methods<br>• Some operations may be risky |
| **Beginning (10-16)** | C | Attempts dictionary operations but with errors or unsafe practices | • Frequent use of unsafe access patterns<br>• Basic operations work but with potential errors<br>• Limited understanding of dictionary methods<br>• May cause KeyError exceptions |
| **Incomplete (0-9)** | F | Cannot demonstrate basic dictionary operations or frequent errors | • Cannot perform basic access or updates<br>• Major errors in dictionary manipulation<br>• No evidence of understanding dictionary methods |

**Assessment Notes:**
- Pay attention to safe access patterns (`.get()` vs direct access)
- Look for appropriate use of `.keys()`, `.values()`, `.items()` methods
- Check if student can handle missing keys gracefully
- Evaluate dynamic dictionary manipulation (adding/removing entries during runtime)

---

### **Criterion 3: Application of Dictionary Methods (20 points)**

| Performance Level | Points | Description | Evidence to Look For |
|-------------------|--------|-------------|---------------------|
| **Excellent (18-20)** | A+ | Uses dictionary methods effectively for complex data analysis and manipulation | • Effective use of `.items()` for iteration<br>• Uses `.keys()` and `.values()` appropriately<br>• Dictionary comprehensions or advanced filtering<br>• Methods used for analysis and reporting |
| **Proficient (16-17)** | A | Uses dictionary methods correctly for most operations | • Good use of `.items()` for key-value iteration<br>• Appropriate use of `.keys()` and `.values()`<br>• Methods support the required functionality<br>• Some analysis or aggregation using methods |
| **Developing (14-15)** | B | Uses some dictionary methods but may miss opportunities for more efficient solutions | • Basic use of `.items()` or similar methods<br>• Some methods used correctly<br>• Could use methods more effectively<br>• Shows awareness but limited application |
| **Beginning (10-13)** | C | Limited use of dictionary methods, relies mainly on basic operations | • Minimal use of dictionary methods<br>• Prefers basic access over methods<br>• Methods used incorrectly or inappropriately<br>• Shows little awareness of method benefits |
| **Incomplete (0-9)** | F | No use of dictionary methods or incorrect usage | • No evidence of using dictionary methods<br>• All operations use basic access patterns<br>• Major errors when attempting to use methods |

**Assessment Notes:**
- Look for appropriate iteration patterns using `.items()`
- Check if methods are used for data analysis (finding totals, filtering, etc.)
- Evaluate whether student understands when to use different methods
- Consider if dictionary comprehensions are used where appropriate

---

### **Criterion 4: Problem-Solving and Code Organisation (15 points)**

| Performance Level | Points | Description | Evidence to Look For |
|-------------------|--------|-------------|---------------------|
| **Excellent (14-15)** | A+ | Code is well-organised, functions are logical, and solutions demonstrate clear problem-solving approach | • Functions have clear purposes and good naming<br>• Code is modular and reusable<br>• Solutions show logical thinking<br>• Easy to follow and understand |
| **Proficient (12-13)** | A | Code is generally well-organised with clear problem-solving approach | • Most functions are well-designed<br>• Generally good code organisation<br>• Solutions work effectively<br>• Some minor organisational issues |
| **Developing (10-11)** | B | Code works but could be better organised or show clearer problem-solving | • Functions work but may lack clarity<br>• Some organisational issues<br>• Solutions work but approach unclear<br>• Could be more logical or efficient |
| **Beginning (7-9)** | C | Code is poorly organised or problem-solving approach is unclear | • Functions are unclear or poorly designed<br>• Poor code organisation<br>• Solutions work but approach is confusing<br>• Hard to follow logic |
| **Incomplete (0-6)** | F | Code is disorganised and shows no clear problem-solving approach | • No clear function design<br>• Very poor organisation<br>• No clear solution approach<br>• Code is difficult to understand |

**Assessment Notes:**
- Look for logical function design and clear naming
- Check if code is organised in a way that makes sense
- Evaluate whether the approach to solving problems is clear and effective
- Consider maintainability and readability of the code

---

### **Criterion 5: Pathway-Specific Demonstration (15 points)**

#### For Pathway A (Extend Week 5):
| Performance Level | Points | Description | Evidence to Look For |
|-------------------|--------|-------------|---------------------|
| **Excellent (14-15)** | A+ | Successfully transforms existing list-based code to elegant dictionary structures, showing clear improvement | • Clear transformation from lists to dictionaries<br>• Shows understanding of improvements gained<br>• Enhanced functionality using dictionary advantages<br>• Reflects on transformation benefits |
| **Proficient (12-13)** | A | Transforms existing code to use dictionaries with good results | • Successful transformation completed<br>• Most functionality converted to dictionaries<br>• Shows improvement over original approach<br>• Generally good conversion |
| **Developing (10-11)** | B | Attempts transformation but may not fully utilise dictionary advantages | • Basic transformation attempted<br>• Some functions converted<br>• Limited use of dictionary advantages<br>• Partial improvement shown |

#### For Pathway B (Fresh Start):
| Performance Level | Points | Description | Evidence to Look For |
|-------------------|--------|-------------|---------------------|
| **Excellent (14-15)** | A+ | Creates comprehensive dictionary-based system from scratch with sophisticated features | • Complete system built from scratch<br>• Sophisticated dictionary usage<br>• All required functionality implemented<br>• Shows mastery of dictionary concepts |
| **Proficient (12-13)** | A | Creates functional dictionary-based system with good design | • Functional system created<br>• Good dictionary usage throughout<br>• Most required functionality implemented<br>• Shows good understanding |
| **Developing (10-11)** | B | Creates basic dictionary-based system but may lack some features or sophistication | • Basic system created<br>• Simple dictionary usage<br>• Some required functionality missing<br>• Shows basic understanding |

---

## Detailed Assessment Guidelines

### **Dictionary-Specific Learning Indicators**

**Excellent Performance Indicators:**
- [ ] Creates nested dictionaries with logical hierarchy
- [ ] Uses `.get()` method consistently for safe access
- [ ] Applies dictionary methods (`.keys()`, `.values()`, `.items()`) effectively
- [ ] Demonstrates understanding of when dictionaries are better than lists
- [ ] Can filter and analyse dictionary data using comprehensions or methods
- [ ] Handles missing keys gracefully without errors
- [ ] Uses meaningful key names that make the code self-documenting

**Common Issues to Watch For:**
- [ ] Using `dict[key]` instead of `dict.get(key)` for potentially missing keys
- [ ] Poor key naming (single letters, unclear abbreviations)
- [ ] Overly complex or unnecessarily nested structures
- [ ] Not taking advantage of dictionary benefits (still thinking in list terms)
- [ ] Inconsistent data structures across similar operations

### **Pathway-Specific Assessment Notes**

**Pathway A (Extend Week 5) - Look For:**
- Evidence of before/after comparison showing improvements
- Clear transformation from parallel lists to integrated dictionaries
- Understanding of why dictionaries are better for this use case
- Enhanced functionality that wasn't possible with lists
- Reflection on the transformation process

**Pathway B (Fresh Start) - Look For:**
- Comprehensive system design using dictionary principles
- Professional-level code organisation
- Full implementation of required features
- Creative use of advanced dictionary features
- Evidence of thinking in dictionary-first terms

---

## Advanced Student Assessment (Extensions)

**For students who complete extensions:**

| Extension | Assessment Focus | Points Available |
|-----------|------------------|------------------|
| **Data Persistence** | JSON serialisation, file handling, backup systems | +5 points |
| **Advanced Analytics** | Complex data analysis using dictionary aggregation | +5 points |
| **Multi-User System** | Sophisticated nested dictionary architectures | +5 points |
| **API Integration** | External data integration and caching | +5 points |
| **AI Insights** | Creative application of dictionary data analysis | +3 points |
| **Export Features** | Data transformation and export capabilities | +3 points |

**Extension Assessment Criteria:**
- **Implementation Quality**: Does the extension work correctly?
- **Dictionary Usage**: Does it demonstrate advanced dictionary concepts?
- **Innovation**: Does it show creative problem-solving?
- **Integration**: Does it integrate well with the core project?

---

## Assessment Workflow

### **Step 1: Initial Review (5 minutes)**
- [ ] Determine which pathway student chose
- [ ] Check if code runs without major errors
- [ ] Identify core features implemented
- [ ] Note any extensions attempted

### **Step 2: Dictionary Structure Assessment (10 minutes)**
- [ ] Examine main data structure design
- [ ] Check for logical organisation and naming
- [ ] Evaluate nesting and hierarchy decisions
- [ ] Assess consistency across the codebase

### **Step 3: Operations and Methods Assessment (10 minutes)**
- [ ] Test key operations (add, find, update, delete)
- [ ] Check for safe access patterns
- [ ] Verify correct use of dictionary methods
- [ ] Look for error handling and robustness

### **Step 4: Problem-Solving Assessment (10 minutes)**
- [ ] Evaluate overall approach and design decisions
- [ ] Check code organisation and function design
- [ ] Assess whether solutions are logical and efficient
- [ ] Review comments and documentation

### **Step 5: Pathway-Specific Assessment (5 minutes)**
- [ ] For Pathway A: Check transformation quality and improvements
- [ ] For Pathway B: Evaluate completeness and sophistication
- [ ] Look for pathway-specific requirements
- [ ] Assess demonstration of learning objectives

### **Step 6: Extension Review (if applicable) (5-10 minutes)**
- [ ] Test extension functionality
- [ ] Evaluate complexity and implementation quality
- [ ] Check integration with core project
- [ ] Assess learning demonstrated

---

## Feedback Templates

### **Excellent Performance Feedback:**
*"Outstanding work on your dictionary-based finance tracker! Your code demonstrates sophisticated understanding of dictionary concepts with excellent structure design and consistent use of safe access patterns. [Specific examples]. Your [pathway choice] shows clear mastery of dictionary advantages. This foundation will serve you well in advanced programming challenges."*

### **Proficient Performance Feedback:**
*"Great job implementing a functional dictionary-based finance tracker! Your code shows solid understanding of core dictionary concepts with good use of methods and operations. [Specific strengths]. Consider improving [specific areas] to make your code even more robust. You're well-prepared for more advanced dictionary applications."*

### **Developing Performance Feedback:**
*"Good effort on your finance tracker project! You've successfully implemented basic dictionary functionality. [Acknowledge what works]. To strengthen your dictionary skills, focus on [specific improvements like safe access patterns, better organisation, etc.]. I recommend [specific next steps] to build on this foundation."*

### **Areas for Improvement Feedback:**
*"I can see you're working hard on understanding dictionaries. [Acknowledge effort]. Your project shows [positive aspects], but there are some areas where we can improve your dictionary skills. Let's focus on [specific concepts] and practice [specific techniques]. Would you like to schedule time to go through these concepts together?"*

---

## Grade Mapping

| Total Points | Letter Grade | Percentage | Performance Level |
|-------------|--------------|------------|------------------|
| 90-100 | A+ | 90-100% | Excellent - Mastery demonstrated |
| 85-89 | A | 85-89% | Excellent - Strong performance |
| 80-84 | A- | 80-84% | Proficient - Good understanding |
| 75-79 | B+ | 75-79% | Proficient - Above average |
| 70-74 | B | 70-74% | Proficient - Meets expectations |
| 65-69 | B- | 65-69% | Developing - Needs some improvement |
| 60-64 | C+ | 60-64% | Developing - Significant gaps |
| 55-59 | C | 55-59% | Beginning - Major concerns |
| 50-54 | C- | 50-54% | Beginning - Needs substantial work |
| <50 | D/F | <50% | Incomplete - Requires remediation |

---

## Success Indicators Summary

**Student has successfully mastered Week 6 dictionary concepts if they demonstrate:**

✅ **Dictionary Design**: Creates logical, well-organised dictionary structures  
✅ **Safe Operations**: Uses `.get()` and handles missing keys appropriately  
✅ **Method Application**: Applies dictionary methods for iteration and analysis  
✅ **Problem Solving**: Shows clear thinking in approaching dictionary-based solutions  
✅ **Pathway Achievement**: Successfully completes chosen pathway requirements  

**This assessment focuses on understanding and application rather than perfect code, encouraging students to demonstrate their learning while building confidence with dictionary concepts.**