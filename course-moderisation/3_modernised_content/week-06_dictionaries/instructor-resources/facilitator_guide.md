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

# Week 6 Facilitator Guide: Dictionary Workshop

## 2-Hour Interactive Lab Session

**Course:** ISYS2001 Introduction to Business Programming  
**Week:** 6 - Dictionaries  
**Duration:** 2 hours (120 minutes)  
**Format:** Interactive lab with QMD notebook exercises  
**Pre-requisite:** Students complete 3 pre-class modules on dictionary fundamentals  
**Materials:** Students need access to warmup_recap_exercise.qmd, exercise1_dictionary_exploration.qmd, and exercise2_library_management_workshop.qmd

---

## 🎯 Session Overview

### Learning Objectives
By the end of this session, students will:
- Apply dictionary operations to solve real-world problems
- Compare and contrast dictionaries vs lists in practical scenarios
- Design appropriate dictionary structures for data management
- Transform existing list-based code to dictionary-based solutions

### Session Philosophy
- **Active Learning**: Students learn by doing, not listening
- **Peer Collaboration**: Encourage discussion and problem-solving together
- **Scaffolded Practice**: Build complexity gradually through guided exercises
- **Real Application**: Use library management as practical, relatable context

---

## ⏰ Session Timeline

| Time | Duration | Activity | Focus |
|------|----------|----------|--------|
| 0:00-0:15 | 15 min | Warm-up & Recap | Activate prior knowledge |
| 0:15-0:45 | 30 min | Dictionary Exploration Lab | Hands-on practice |
| 0:45-1:15 | 30 min | Library Management Workshop | Structured application |
| 1:15-1:25 | 10 min | Break | Rest and reset |
| 1:25-1:50 | 25 min | Mini-Project Introduction | Project launch |
| 1:50-2:00 | 10 min | Wrap-up & Next Steps | Consolidation |

---

## 📋 Detailed Activity Guide

### **Activity 1: Warm-up & Recap (15 minutes)**

**Objective:** Activate prior knowledge from pre-class modules and identify any gaps.

#### **Setup (2 minutes)**
```
"Welcome everyone! Please open warmup_recap_exercise.qmd in your Jupyter 
environment. Before we dive into hands-on practice, let's work through 
this warm-up exercise together. If anyone hasn't completed the three 
pre-class modules, please pair up with someone who has."
```

#### **Guided Warm-up Exercise (13 minutes)**

**Facilitator Script:**
```
"We'll work through the warm-up exercise together. This helps us activate 
your dictionary knowledge and identify any gaps before the main activities. 
Work in pairs and execute each cell as we go through it."
```

**Guide students through the QMD notebook:**

1. **Prediction Exercise (5 minutes)**: Have students predict outputs before running code
2. **Nested Dictionary Exploration (5 minutes)**: Work through safe access patterns  
3. **Quick Challenges (3 minutes)**: Let pairs attempt the mini-challenges

**Key Teaching Points:**
- Emphasize `.get()` vs direct access patterns
- Address any confusion about nested dictionary structures
- Note any areas where students struggle for follow-up

*Use the staff answer keys to verify student solutions and provide hints as needed.*

---

### **Activity 2: Dictionary Exploration Lab (30 minutes)**

**Objective:** Practice core dictionary operations through guided exploration using exercise1_dictionary_exploration.qmd.

#### **Setup & Context (3 minutes)**

**Facilitator Script:**
```
"Now please open exercise1_dictionary_exploration.qmd. Today we're working 
with a library management system - perfect for practicing dictionaries! 
This gives us a different context from your finance mini-project."
```

**Guide students to the starting data structure in the notebook:**
- Library catalog with nested book information
- Point out the structure: book_id as keys, book details as nested dictionaries

#### **Guided Exercises (22 minutes)**

**Exercise 1: Safe Access Practice (8 minutes)**

**Facilitator Instructions:**
```
"Work through Exercise 1.2 in your notebook. Focus on using the .get() 
method for safe access. I'll walk around to help with any issues."
```

**Circulate and observe:**
- Look for students using `book_id in library_catalog` vs `.get()`
- Help students who try unsafe access patterns
- Direct students to the solution in the notebook after they attempt it

**Exercise 2: Dictionary Methods Exploration (8 minutes)**

**Facilitator Script:**
```
"Move on to Exercise 2.2 - the challenge tasks. Work with your partner 
and attempt each challenge before looking at the solutions."
```

**Support students as they work through:**
- Challenge 1: Print all book titles
- Challenge 2: Count available books  
- Challenge 3: List unique categories
- Challenge 4: Find books by specific author

**Provide hints as needed, but encourage problem-solving first.**

**Exercise 3: Library Functions (6 minutes)**

**Facilitator Script:**
```
"Now tackle Exercise 3.3 - implementing checkout, return, and search 
functions. This is more challenging, so work together and don't hesitate 
to ask for help."
```

**Key teaching points while circulating:**
- Emphasize using `.get()` for safe access
- Help with function parameter understanding
- Point out the solutions are provided for comparison

#### **Wrap-up Discussion (5 minutes)**

**Facilitator Questions:**
```
"What patterns did you notice when working with nested dictionaries?
What was easier with dictionaries compared to if we used lists?
Which dictionary methods were most useful?"
```

**Key points to emphasize:**
- Dictionaries provide meaningful keys vs numeric indices
- `.get()` prevents crashes when keys might not exist
- Dictionary methods make iteration and analysis cleaner

*Refer to staff answer keys for complete solutions and teaching notes.*

---

### **Activity 3: Library Management Workshop (30 minutes)**

**Objective:** Apply dictionary skills to build a complete system using exercise2_library_management_workshop.qmd.

#### **Problem Introduction (5 minutes)**

**Facilitator Script:**
```
"Please open exercise2_library_management_workshop.qmd. Now we're building 
a complete library management system with CRUD operations. This directly 
prepares you for your mini-project where you'll do similar work with 
financial data."
```

**Review system requirements in the notebook:**
- Add new books to the catalog
- Check out books (mark as unavailable)  
- Return books (mark as available)
- Search for books by title or author
- Generate comprehensive reports

#### **Structured Implementation (20 minutes)**

**Phase 1: Book Management Functions (6 minutes)**

**Facilitator Instructions:**
```
"Start with Phase 1 in your notebook - the add_book function is provided, 
but work on implementing the remove_book function. Use the 'Your Turn' 
sections to practice before looking at solutions."
```

**Circulate and help:**
- Guide students through the remove_book implementation
- Emphasize safe dictionary access patterns
- Help debug any syntax issues

**Phase 2: Checkout/Return System (8 minutes)**

**Facilitator Script:**
```
"Move to Phase 2 - checkout and return functions. The checkout_book_enhanced 
function is provided as an example, but implement the return_book_enhanced 
function yourself."
```

**Key teaching points while circulating:**
- Emphasize using `.get()` to check if book exists
- Help students understand the enhanced version with borrower tracking
- Discuss error handling and user feedback patterns

**Phase 3: Search and Analysis (6 minutes)**

**Facilitator Script:**
```
"Work through Phase 3 - search and analysis functions. Try the 'Your Turn' 
exercises for books_by_category before checking the solution."
```

**Support students with:**
- Advanced search functionality
- Data aggregation patterns
- Dictionary comprehension techniques (if students are ready)

#### **Integration Testing (5 minutes)**

**Facilitator Instructions:**
```
"Complete Phase 5 - the integration test. This shows how all your functions 
work together in a real system. Run through the entire test sequence."
```

**Key observations while students work:**
- Are functions working together properly?
- Do students understand the data flow between operations?
- Can they debug integration issues?

*Use staff answer keys for complete solutions and extend with additional challenges for fast finishers.*

---

### **Break (10 minutes)**

```
"Great work everyone! Take a 10-minute break. When we return, we'll 
introduce your mini-project and see how these skills apply to your 
finance tracker assignment."
```

---

### **Activity 4: Mini-Project Introduction (25 minutes)**

**Objective:** Launch the mini-project with clear expectations and pathway choices.

#### **Project Overview (8 minutes)**

**Facilitator Script:**
```
"Your mini-project applies everything we've practiced today to personal 
finance management. Just like we organized books in a library, you'll 
organize financial information using dictionaries."
```

**Show the two pathways (display on screen):**

```
Pathway A: Extend Week 5 Project
- Transform your existing lists-based finance tracker
- Convert parallel lists to integrated dictionaries  
- See direct before/after improvement
- Perfect if you completed Week 5 successfully

Pathway B: Fresh Start
- Build a new dictionary-based finance tracker from scratch
- Professional-level system design
- More comprehensive feature set
- Perfect if Week 5 was challenging or you want a clean start
```

#### **Pathway Deep-Dive (12 minutes)**

**For Pathway A (6 minutes):**

**Facilitator Script:**
```
"If you choose Pathway A, you'll transform code like this:"
```

**Show before/after example:**
```python
# Before (Week 5 style)
expenses = [25.50, 12.00, 45.00]
categories = ['Food', 'Transport', 'Entertainment'] 
dates = ['2023-10-01', '2023-10-02', '2023-10-03']

# After (Week 6 style)
expenses = {
    'exp_001': {
        'amount': 25.50,
        'category': 'Food',
        'date': '2023-10-01'
    },
    'exp_002': {
        'amount': 12.00,
        'category': 'Transport', 
        'date': '2023-10-02'
    }
}
```

**Key benefits to highlight:**
- No more parallel list synchronization issues
- Meaningful IDs instead of array indices
- Easy to add new fields without breaking existing code
- Natural grouping of related information

**For Pathway B (6 minutes):**

**Facilitator Script:**
```
"If you choose Pathway B, you'll build a comprehensive system like this:"
```

**Show system structure:**
```python
finance_tracker = {
    'user_profile': {
        'name': 'John Doe',
        'monthly_income': 3000.00,
        'savings_goal': 500.00
    },
    'categories': {
        'Food': {'budget': 400.00, 'spent': 125.50},
        'Transport': {'budget': 200.00, 'spent': 45.00}
    },
    'expenses': {
        # Individual expense entries
    }
}
```

**Key advantages to highlight:**
- Professional system architecture
- Built-in budgeting and analysis features
- Scalable design for future enhancements
- Industry-standard data organization

#### **Requirements and Assessment Preview (5 minutes)**

**Facilitator Script:**
```
"Regardless of pathway, you'll be assessed on:
1. Dictionary structure design - logical organization
2. Dictionary operations mastery - safe access, methods
3. Problem-solving approach - clean, understandable code
4. Pathway-specific achievements - transformation or comprehensive build"
```

**Show assessment focus:**
```
This is FORMATIVE assessment - focus on learning, not grades!
- Demonstrate dictionary understanding
- Show improvement in code organization
- Use appropriate dictionary methods
- Handle edge cases safely
```

**Timeline and Support:**
```
- Project duration: 1-2 hours
- Advanced extensions available for fast finishers
- Sample solutions at different performance levels provided
- AI prompting guidance available to maintain appropriate complexity
```

---

### **Activity 5: Wrap-up & Next Steps (10 minutes)**

**Objective:** Consolidate learning and set expectations for project work.

#### **Learning Consolidation (5 minutes)**

**Facilitator Questions:**
```
"Before you start your projects, let's reflect:
1. What's the biggest advantage of dictionaries over lists for data management?
2. When would you use .get() instead of direct key access?
3. How do dictionaries make your code more readable and maintainable?"
```

**Expected responses to reinforce:**
- Meaningful keys vs numeric indices
- Grouped related data in one structure
- Safe access prevents crashes
- Self-documenting code through key names

#### **Project Launch Checklist (3 minutes)**

**Facilitator Script:**
```
"Before you start your project, make sure you have:
✓ Chosen your pathway (A or B)  
✓ Access to the project specification document
✓ Sample solutions for reference (don't peek too early!)
✓ AI prompting guidance if you need help
✓ Understanding of assessment criteria"
```

#### **Support Resources (2 minutes)**

**Available help:**
```
- Instructor office hours: [Insert times]
- Online discussion forum for peer help
- Sample solutions at beginner, intermediate, and advanced levels
- AI prompting templates for appropriate complexity level
- Assessment rubric for self-evaluation
- Complete staff answer keys for all exercises (instructor-resources/staff_answer_keys.qmd)
```

**Final encouragement:**
```
"Remember: This is about applying what you've learned, not perfect code. 
Focus on demonstrating your understanding of dictionaries through working 
solutions. The journey of building it is more important than the 
destination!"
```

---

## 🎯 Facilitator Success Tips

### **Managing the Room**

**Energy and Engagement:**
- Move around constantly during activities
- Ask pairs to share solutions, not just show answers
- Use "think-pair-share" for complex questions
- Celebrate good solutions publicly

**Handling Different Pace:**
```
Fast Finishers: "Try adding error handling or extra features"
Struggling Students: "Focus on getting basic functionality working first"
Mixed Pairs: "Stronger student explains approach to partner"
```

**Common Issues and Solutions:**

| Issue | Quick Fix |
|-------|-----------|
| "I don't understand dictionaries" | Pair with confident partner, start with simple examples |
| "This is too easy" | Provide extension challenges, ask them to help others |
| "I can't get it working" | Break down into smaller steps, focus on syntax errors first |
| "Why not just use lists?" | Show concrete examples of why dictionary keys are better |

### **Technical Troubleshooting**

**Common Code Issues:**
```python
# KeyError - remind about .get()
student['grade']  # ❌ 
student.get('grade', 'Unknown')  # ✅

# Wrong loop structure
for book in library_catalog:  # Gets keys only ❌
for book_id, book_info in library_catalog.items():  # ✅

# Forgetting nested structure
book['title']  # ❌ if book is None
library_catalog[book_id]['title']  # ❌ if book_id missing
library_catalog.get(book_id, {}).get('title', 'Unknown')  # ✅
```

### **Assessment Integration**

**Formative Assessment During Session:**
- Observe pair discussions for understanding
- Ask students to explain their approach, not just show code
- Note who uses safe access patterns vs risky ones
- Check if students understand when to use different dictionary methods

**Project Setup Success Indicators:**
- Students can articulate why they chose their pathway
- They understand the assessment criteria
- They know where to find help resources
- They're excited to start building

### **Differentiation Strategies**

**For Struggling Students:**
- Provide more scaffolded steps
- Pair with supportive partner
- Focus on basic operations before advanced features
- Use simpler example data

**For Advanced Students:**
- Provide extension challenges
- Ask them to mentor others
- Introduce more complex data structures
- Discuss performance implications

**For Mixed Groups:**
- Use peer teaching extensively
- Provide multiple solution approaches
- Offer choice in implementation details
- Create opportunities for different students to shine

---

## 📊 Session Evaluation

### **Student Feedback Questions (End of Session)**
```
1. How confident do you feel using dictionaries for data management? (1-5)
2. What was the most valuable part of today's session?
3. What topic needs more practice or explanation?
4. How well do you understand your mini-project requirements?
```

### **Instructor Self-Reflection**
```
- Did students actively engage throughout the session?
- Were the activities appropriately challenging?
- How well did the library theme work for dictionary concepts?
- What would you change for next time?
```

---

## 🔄 Follow-Up Actions

**Immediate (End of Session):**
- Share project specification documents
- Post session materials and solutions online
- Send reminder about project timeline

**Within 24 Hours:**
- Review student questions from session
- Prepare additional examples if common issues identified
- Update materials based on session feedback

**Ongoing Support:**
- Monitor project progress through office hours
- Share common questions and solutions with class
- Prepare for next week's content building on dictionary skills

---

**Remember: The goal is active learning through doing, not passive listening. Keep students engaged, celebrate their discoveries, and help them see the practical value of dictionaries in real programming scenarios.**