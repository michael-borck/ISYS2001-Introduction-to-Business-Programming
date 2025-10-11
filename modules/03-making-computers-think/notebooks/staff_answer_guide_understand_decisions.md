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

# Staff Answer Guide: Understanding Decisions with AI

## 🎯 Session Overview

**Duration**: 45 minutes  

**Learning Objectives**: Students will learn to analyze problems before coding, implement decision logic using if/elif/else statements, and collaborate effectively with AI tools.

**Key Pedagogical Approach**: Think-first programming - students must understand the problem and design logic before implementing code.

---

## 🚀 Opening Hook (5 minutes)

### Suggested Attention-Grabber Activity

**"The Human Decision Engine"**

Start with this interactive exercise:

1. **Ask students to stand up** and announce: "You are now human computers!"

2. **Give them a decision problem**: "If a student's GPA is above 3.5, clap once. If it's between 3.0-3.5, snap your fingers. If it's below 3.0, stomp your foot."

3. **Call out GPAs**: 3.8, 2.9, 3.2, 4.0, 2.1

4. **Observe the chaos**: Students will likely respond at different times, some will be confused about boundary cases (what about exactly 3.0?), and there will be inconsistency.

5. **Debrief**: "Why was that messy? What would we need to make it work perfectly every time?"

**Key Teaching Points**:

- Computers need **precise instructions**
- Humans naturally understand context; computers don't
- **Boundary cases** matter enormously
- **Order of checking conditions** affects outcomes

**Transition**: "Today we'll learn to think like computer scientists - breaking down decisions so clearly that even a computer can follow them perfectly."

---

## 📋 Activity 1: Problem Analysis Before Coding (15 minutes)

### Complete Answer Key

**Step 1: Understanding the Problem**

**Model Answers**:

- **Input needed**: Student's GPA (floating point number)
- **Output needed**: Academic status classification (string)
- **Decision points**: GPA thresholds that determine different status categories

**Step 2: Define the Logic**

**Sample Classification System** (students may vary):
```
If GPA is 3.5 or above, then status is "Dean's List"
If GPA is 3.0 to 3.49, then status is "Good Standing"  
If GPA is 2.0 to 2.99, then status is "Probation"
If GPA is below 2.0, then status is "Academic Warning"
```

**Teaching Note**: Accept different ranges, but ensure students address:
- **Boundary clarity**: What happens at exactly 3.0, 3.5?
- **Complete coverage**: Every possible GPA should have a classification
- **Logical progression**: Categories should make educational sense

**Step 3: Test Your Logic**

**Correct Predictions** (using sample system above):
- **Student A (3.7)**: "Dean's List"
- **Student B (2.9)**: "Probation"  
- **Student C (3.0)**: "Good Standing" (assuming inclusive lower bound)

### Common Pitfalls & Teaching Strategies

**Pitfall 1**: Students jump to coding without thinking
- **Strategy**: Physically cover their keyboards! "No typing until logic is clear."

**Pitfall 2**: Vague boundary definitions
- **Strategy**: Ask "What about exactly 3.0?" for every threshold they propose.

**Pitfall 3**: Missing edge cases
- **Strategy**: Always test with boundary values: 0.0, 4.0, exactly the thresholds.

### AI Collaboration Checkpoint 1

**Model AI Prompts** (show these as examples):

**✅ Good**: "I've designed a GPA classification system: Dean's List (3.5+), Good Standing (3.0-3.49), Probation (2.0-2.99), Academic Warning (<2.0). Can you help me implement this in Python using if/elif/else, making sure the boundaries work correctly?"

**❌ Less Helpful**: "Make a GPA thing"

**Sample Implementation**:
```python
def classify_student(gpa):
    if gpa >= 3.5:
        return "Dean's List"
    elif gpa >= 3.0:
        return "Good Standing"
    elif gpa >= 2.0:
        return "Probation"
    else:
        return "Academic Warning"

# Test cases
print(classify_student(3.7))  # Dean's List
print(classify_student(2.9))  # Probation
print(classify_student(3.0))  # Good Standing
```

**Tutor AI Guidance Strategy**:
- **Before students use AI**: Have them articulate their logic clearly
- **AI Prompt Template**: Teach students to include their specific requirements in prompts
- **After AI response**: Ask "Does this match your thinking? What's different?"

---

## 🎯 Activity 2: Independent Problem Solving (20 minutes)

### Complete Answer Key

**Step 1: Problem Definition (5 minutes)**

**Sample Factor Analysis**:
- **Hours studied today**: 0-2 (low), 3-5 (moderate), 6+ (high)
- **Stress level**: 1-3 (low), 4-6 (medium), 7-10 (high)
- **Days until exam**: 1 (urgent), 2-7 (soon), 8+ (distant)
- **Sleep hours**: <6 (poor), 6-8 (adequate), 8+ (good)

**Step 2: Sample Decision Logic**

```
IF hours_studied >= 6 AND stress_level >= 7 THEN recommend "Take a break - you've earned it!"

ELIF hours_studied < 2 AND days_until_exam <= 2 THEN recommend "Focus time! Start studying now."

ELIF stress_level >= 8 THEN recommend "Manage stress first - try meditation or light exercise"

ELIF sleep_hours < 6 THEN recommend "Prioritize sleep - you'll study better tomorrow"

ELSE recommend "Steady studying - keep up the good work!"
```

**Step 3: Sample Implementation**

```python
def study_recommendation(hours_studied, stress_level, days_until_exam, sleep_hours):
    """
    Provides personalized study recommendations based on multiple factors
    """
    if hours_studied >= 6 and stress_level >= 7:
        return "Take a break - you've earned it! High stress + lots of study = burnout risk."
    
    elif hours_studied < 2 and days_until_exam <= 2:
        return "Focus time! Start studying now - exam is soon and you're behind."
    
    elif stress_level >= 8:
        return "Manage stress first - try meditation, exercise, or talk to someone."
    
    elif sleep_hours < 6:
        return "Prioritize sleep - you'll study better with a rested brain."
    
    elif hours_studied >= 4 and stress_level <= 4:
        return "Great balance! Keep up the steady progress."
    
    else:
        return "Consider studying for 2-3 more hours, but monitor your stress level."

# Test cases
print(study_recommendation(6, 8, 5, 7))  # Take a break
print(study_recommendation(1, 3, 1, 8))  # Focus time
print(study_recommendation(0, 9, 7, 5))  # Manage stress
```

### Teaching Strategies

**Encourage Divergent Thinking**: Multiple correct approaches exist. Focus on:
- **Logic clarity**: Can they explain their reasoning?
- **Edge case handling**: What about extreme values?
- **User empathy**: Would this actually help a student?

**Common Student Struggles**:
1. **Analysis paralysis**: "I don't know what factors to pick"
   - **Strategy**: "Pick any 2-3 that matter to YOU as a student"

2. **Over-complication**: Trying to handle 8+ factors
   - **Strategy**: "Start simple, then add complexity"

3. **Vague recommendations**: "Study more"
   - **Strategy**: "Be specific - what should they do for the next hour?"

### AI Collaboration Checkpoint 2

**Effective Collaboration Sequence**:

1. **Problem Analysis**: "I want to build a study recommendation system. What factors beyond GPA might influence good study advice?"

2. **Logic Review**: "Here's my decision logic: [student's logic]. Does this make sense? What edge cases am I missing?"

3. **Implementation Help**: "Help me implement this logic in Python. I want to use if/elif/else statements."

4. **Testing Guidance**: "What test cases should I use to verify this recommends sensible advice?"

**Tutor Role**: Monitor AI conversations, intervene if AI is doing too much thinking for the student.

---

## 🐛 Activity 3: Debugging and Refinement (10 minutes)

### Complete Answer Analysis

**Step 1: Trace Through the Logic**

For `student_gpa = 3.2`:
- **Check 1**: `3.2 >= 2.0`? → **YES** (True)
- **What happens next**: Assigns `status = "Probation"` and **stops checking other conditions**

**Step 2: The Problem**

**The problem is**: The conditions are in the wrong order
**It happens because**: Python checks conditions **sequentially** and stops at the first true condition. Since 3.2 ≥ 2.0, it never checks the more specific conditions.

**Step 3: Fixed Version**

```python
student_gpa = 3.2

if student_gpa >= 3.5:
    status = "Dean's List"
elif student_gpa >= 3.0:
    status = "Good Standing"  
elif student_gpa >= 2.0:
    status = "Probation"
else:
    status = "Failing"

print(f"Status: {status}")  # Now correctly prints "Good Standing"
```

### Key Teaching Points

**Fundamental Concept**: `elif` chains execute **only the first true condition**

**Mental Model**: "It's like a waterfall - once water goes down one path, it doesn't check the others"

**Common Debugging Strategy**:
1. **Trace by hand**: Follow the logic step-by-step
2. **Order matters**: Most specific conditions first
3. **Test boundary cases**: Always check the threshold values

### AI Collaboration for Debugging

**Good Tutor-AI Prompt** (demonstrate this):
> "I have code that should classify GPA 3.2 as 'Good Standing' but it returns 'Probation' instead. Can you help me understand why the if/elif logic isn't working as expected?"

**Teaching Strategy**: Show students how this prompt:
- **States the expected behavior**
- **Describes the actual behavior** 
- **Asks for understanding**, not just a fix

---

## 🎭 Reflection Questions - Model Answers

### About Problem-Solving

1. **Was it harder to think through the logic first, or to jump straight into coding?**
   - **Sample Answer**: "Thinking first felt slower initially, but it made the coding much easier. When I jumped straight to code, I kept getting confused and making mistakes."

2. **How did breaking down the problem help (or not help) your understanding?**
   - **Sample Answer**: "It helped me realize I hadn't thought about edge cases. Breaking it down made me consider 'what if someone has exactly 3.0 GPA?' which I would have missed otherwise."

### About AI Collaboration

3. **When was AI most helpful - during problem analysis, coding, or debugging?**
   - **Sample Answer**: "AI was most helpful with coding syntax after I knew what I wanted to do. For problem analysis, I needed to think it through myself first."

4. **What's the difference between asking AI to solve a problem vs. asking AI to help you solve it?**
   - **Sample Answer**: "When I ask AI to solve it, I don't learn much. When I ask AI to help with my solution, I understand why it works."

### About Learning

5. **Do you understand why your code works, or just that it works?**
   - **Good Answer**: "I understand why - the order of conditions matters because Python stops at the first true condition."
   - **Concerning Answer**: "It just works" (needs follow-up)

6. **Could you explain your decision logic to someone else?**
   - **Teaching Note**: This is the ultimate test. If they can't explain it, they don't truly understand it.

---

## 🎯 Assessment Rubric

### Excellent (A)
- Clear problem analysis before coding
- Logical, well-ordered decision structure
- Handles edge cases appropriately
- Can explain reasoning clearly
- Uses AI strategically (for implementation, not thinking)

### Good (B)
- Some problem analysis, mostly correct logic
- Minor issues with boundary cases
- Can explain most decisions
- Some effective AI collaboration

### Needs Improvement (C)
- Jumps to coding without clear analysis
- Logic errors or missing cases
- Difficulty explaining reasoning
- Over-reliant on AI or not using AI effectively

---

## 💡 Extension Activities

**For Fast Finishers**:
1. **Add complexity**: Multiple input validation, error handling
2. **Create a GUI**: Simple input/output interface
3. **Data analysis**: Given a CSV of student GPAs, classify them all

**For Struggling Students**:
1. **Simplify**: Start with just two categories (pass/fail)
2. **Visual aids**: Draw flowcharts of their logic
3. **Pair programming**: Work with a partner

---

## 🤖 AI Tool Management Guidelines

### For Tutors Using AI During Session

**Do**: 
- Use AI to generate additional examples when students need them
- Ask AI for alternative explanations if your first approach doesn't work
- Use AI to quickly check your own code examples

**Don't**:
- Let students see you solving problems by just asking AI directly
- Use AI as a replacement for understanding the concepts yourself

### Recommended AI Prompts for Tutors

**For generating examples**: "Give me 3 more test cases for a GPA classification system that would help students understand boundary conditions"

**For explanations**: "Explain the concept of if/elif order in Python to a beginner using a real-world analogy"

**For debugging help**: "What are the most common mistakes students make when writing if/elif/else chains for classification problems?"

---

## 📚 Key Concepts Summary

**Computational Thinking Skills**:
- Problem decomposition
- Pattern recognition  
- Algorithm design
- Testing and debugging

**Python Concepts**:
- if/elif/else syntax and logic
- Condition ordering importance
- Boolean expressions
- Function design

**AI Collaboration**:
- Clear requirement specification
- Strategic tool usage
- Critical evaluation of AI output

**Success Indicator**: Students can analyze a new decision problem, design clear logic, implement it correctly, and explain their reasoning to others.
