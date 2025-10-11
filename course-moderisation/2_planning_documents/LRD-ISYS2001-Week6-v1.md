# Learning Requirements Document
## Version: 1.0 | Status: Draft | Last Updated: 26 August 2025

### 1. Topic
- **Week/Unit:** Week 6 - Organising Your Thoughts (with Dictionaries)
- **Main Theme:** Dictionaries as a structured approach to data organisation and management
- **Duration:** 3 hours total (1 hour pre-class, 2 hours in-class)

### 2. Learning Objectives
Upon completion, students will be able to:
- [ ] **Apply** dictionary operations to solve real-world data organisation problems [Application - Bloom's Level 3]
- [ ] **Create** dictionary-based solutions that replace less efficient data structures like parallel lists [Application - Bloom's Level 3]
- [ ] **Evaluate** when dictionaries are more appropriate than lists or other data structures for specific scenarios [Analysis - Bloom's Level 4]
- [ ] **Implement** nested dictionaries to represent hierarchical data relationships [Application - Bloom's Level 3]
- [ ] **Demonstrate** progressive enhancement by extending existing code with dictionary functionality [Application - Bloom's Level 3]

### 3. Target Audience
- **Course/Program:** ISYS2001 Introduction to Business Programming
- **Year Level:** 1st year Information Systems majors
- **Assumed Knowledge:** Functions, parameters, return values, loops, lists, input validation with pyinputplus
- **Class Size:** 25-30 students

### 4. Available Resources
#### Legacy Materials (Assessment: Needs Updating)
- **01_slide_introduction_to_python_data_structures.md**: Good foundation but uses generic examples - needs domain variety
- **02_slide_basics_of_python_dictionaries.md**: Solid technical content but examples need updating for theme differentiation
- **03_slide_dictionary_methods_and_operations.md**: Comprehensive coverage but needs non-finance examples
- **Activity 1, 2, 3**: Heavy focus on business data analysis - contradicts theme variety requirement, needs replacement
- **week5_finance_modularity_miniproject.qmd**: Excellent foundation for extension with dictionaries

#### New Resources Required
- **Student Record Management** examples for lectures (avoiding finance theme)
- **Library Management System** activities for worksheets (non-finance theme)
- **Interactive HTML exercises** for dictionary concept introduction
- **QMD notebook templates** for coding practice

### 5. Desired Structure
- **Pre-Class:** 60 minutes - Self-paced modules introducing dictionary concepts
  - **Module Breakdown:**
    - Module 1: Dictionary Fundamentals (20 minutes) - What are dictionaries, when to use them
    - Module 2: Core Dictionary Operations (20 minutes) - Create, access, modify, iterate
    - Module 3: Dictionary Applications (20 minutes) - Real-world use cases and problem-solving patterns
- **In-Class:** 120 minutes - Hands-on application and problem-solving
  - **Format:** Hybrid - 1-2 interactive HTML exercises + QMD notebook coding practice
  - **Facilitation Style:** Guided practice with student choice for mini-project approach
- **Post-Class:** Self-assessment quiz/flashcards for concept reinforcement

### 6. Key Activities & Deliverables

| Activity | Type | Format | Duration | Student Deliverable | Tutor Resources |
|----------|------|--------|----------|-------------------|-----------------|
| Dictionary Concept Explorer | Individual | Interactive HTML | 20 min | Completed exercises | Solution key |
| Library System Workshop | Individual/Pair | QMD Notebook | 45 min | Working code | Guide + solutions |
| Mini-Project: Finance Tracker Enhancement | Individual | QMD Notebook | 45 min | Enhanced tracker with dictionaries | Rubric + examples |
| Self-Assessment Quiz | Individual | Digital flashcards | 10 min | Quiz completion | Question bank |

### 7. Assessment
- **Type:** Formative assessment only
- **Method:** Self-assessment quiz/flashcards + in-class practical exercises
- **Weight:** Not graded (preparation for upcoming assignments)
- **Success Criteria:** 
  - Demonstrates understanding of when to use dictionaries vs. lists
  - Successfully implements dictionary operations in code
  - Shows progressive enhancement thinking in mini-project

### 8. Constraints & Assumptions
- **Time Limits:** Mini-project core features must be completable in 1-2 hours
- **Technical Requirements:** Google Colab environment, pyinputplus for input validation
- **Dependencies:** Successful completion of Week 5 (Functions and Modularity)
- **Simplicity Constraint:** Avoid exception handling - students should learn to prompt AI appropriately for their knowledge level
- **Accessibility:** Materials must work across devices, alternative formats for different learning styles

### 9. Integration Points
- **LMS Requirements:** QMD files convertible to .ipynb format via Quarto
- **Calendar Alignment:** Pre-class modules released 1 week prior, in-class activities ready for 2-hour lab session
- **Grade Book Mapping:** Formative only - no grade book entries required

### 10. Key Design Decisions

#### Theme Differentiation Strategy
- **Mini-project:** Finance domain (extending Week 5 tracker) - maintains progression toward smart finance app
- **Lecture examples:** Student records/academic management - provides variety while staying relevant
- **Workshop activities:** Library management system - different domain for transfer of learning
- **Rationale:** Variety prevents monotony while ensuring students apply concepts across different contexts

#### Student Choice Philosophy
- **Mini-project approach:** Students choose to extend Week 5 tracker OR start fresh finance project
- **Rationale:** Accommodates different student situations while maintaining learning objectives
- **Support:** Provide both pathways with equal scaffolding and examples

#### Scaffolded Complexity Progression
- **Level 1:** Basic dictionary operations (create, access, modify)
- **Level 2:** Dictionary iteration and methods
- **Level 3:** Nested dictionaries for hierarchical data
- **Advanced Extensions:** Optional for fast finishers - prepares for Pandas introduction
- **Rationale:** Progressive enhancement building toward data analysis tools

#### Application vs. Analysis Balance (70/30 Split)
- **70% Application Focus:** Hands-on problem-solving, building working solutions
- **30% Comparison/Analysis:** When to use dictionaries vs. other data structures
- **Rationale:** Prioritises practical skills while building critical thinking about data structure selection

### 11. Change Log
| Version | Date | Changes | Approved By |
|---------|------|---------|-------------|
| 1.0 | 26 Aug 2025 | Initial draft based on clarifying questions | Pending approval |

---

## Content Themes Summary

**Ensuring Variety Across Learning Components:**

| Component | Theme/Domain | Rationale |
|-----------|--------------|-----------|
| **Pre-class modules** | Student records, academic data | Relevant to student experience, avoids finance |
| **Lecture examples** | University systems, gaming leaderboards | Engaging variety, demonstrates broader application |
| **Workshop activities** | Library management, book catalogs | Clear hierarchical data, different from finance/academics |
| **Mini-project** | Personal finance tracker | Maintains progression toward final assignment |

**Result:** Students experience dictionary concepts across 4 different domains, ensuring transfer of learning while maintaining engagement through variety.

## Technical Implementation Notes

**QMD to Jupyter Workflow:**
- Primary development in .qmd format for Quarto compatibility
- Automatic conversion to .ipynb for Google Colab
- Maintains cell structure and markdown formatting

**Complexity Management:**
- Core concepts accessible to all students
- Optional advanced features clearly marked
- AI prompting guidance to maintain appropriate complexity level
- No exception handling until later weeks

**Assessment Philosophy:**
- Formative feedback emphasises growth over grades
- Self-assessment builds metacognitive skills
- Practical application demonstrates understanding better than theoretical tests