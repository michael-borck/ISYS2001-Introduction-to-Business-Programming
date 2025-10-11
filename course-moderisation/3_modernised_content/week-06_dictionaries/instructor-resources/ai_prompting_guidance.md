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

# AI Prompting Guidance for Week 6: Dictionary Projects
## Helping Students Use AI Appropriately for Their Learning Level

---

## 🎯 Overview

This guide helps instructors teach students how to use AI tools effectively while maintaining appropriate complexity for their current learning level (Week 6 - first encounter with dictionaries). Students should learn to prompt AI as a learning partner, not a solution generator.

### Key Principles
- **AI as Learning Partner**: Help understand concepts, don't just generate code
- **Appropriate Complexity**: Keep AI responses at student learning level
- **Constraint-Based Prompting**: Use specific constraints to guide AI responses
- **Learning-Focused**: Emphasise understanding over completion

---

## 🚫 Common AI Prompting Problems

### **❌ Poor Student Prompts**

**Problem: Vague, Solution-Seeking Prompts**
```
Student: "Write a finance tracker using dictionaries"
Student: "Fix my code"
Student: "Make this better"
```

**Why These Are Problematic:**
- Generate complex code beyond student level
- Skip learning process and conceptual understanding
- Often include advanced concepts not yet covered
- Don't help student understand the "why" behind solutions

**AI Response Issues:**
- Uses exception handling (not covered until later)
- Includes complex patterns like list comprehensions
- Implements object-oriented design (not yet covered)
- Uses libraries or concepts beyond current scope

---

## ✅ Effective AI Prompting Strategies

### **🎯 Constraint-Based Prompting**

**✅ Good Student Prompts:**
```
Student: "I'm a first-year student learning dictionaries for the first time. 
I need to store expense information but I'm not sure if I should use a list 
or dictionary. Can you explain when to use each one with a simple example? 
Please don't use any advanced Python features I haven't learned yet."
```

**✅ Even Better - Specific Learning Context:**
```
Student: "I'm working on Week 6 of my programming course. We just learned 
about dictionary basics like creating them, using .get(), and .items(). 
I have expenses stored in parallel lists and want to understand how 
dictionaries would be better. Can you show me a simple before/after 
comparison using only basic dictionary operations?"
```

### **🔍 Concept-Focused Prompting**

**✅ Understanding-Focused Prompts:**
```
Student: "I keep getting KeyError when accessing dictionary keys. Can you 
explain why this happens and show me the safe way to access dictionary 
values? Please use simple examples."

Student: "What's the difference between dict[key] and dict.get(key)? 
When should I use each one?"

Student: "I have this dictionary structure [shows code]. Can you explain 
what .items() does and why I would use it instead of just looping through 
the dictionary normally?"
```

### **🛠️ Debugging-Focused Prompting**

**✅ Learning-Oriented Debugging:**
```
Student: "My code has an error [shows specific error]. I think it's related 
to how I'm accessing the dictionary. Can you help me understand what went 
wrong and how to fix it? Please explain why the error happened."

Student: "This function isn't working as expected [shows code]. I'm trying 
to add expenses to a dictionary but something's wrong. Can you help me 
trace through what happens step by step?"
```

---

## 🎓 Teaching Students to Prompt Effectively

### **Lesson: How to Ask AI for Help**

**Step 1: Set Learning Context**
Teach students to always start prompts with:
```
"I'm a first-year programming student in Week 6, learning dictionaries 
for the first time. I understand [list what they know] but I'm confused 
about [specific concept]."
```

**Step 2: Specify Constraints**
```
"Please use only basic Python features like:
- Simple dictionary creation {}
- Basic access with dict[key] and dict.get(key)
- Simple loops with for/while
- Basic if/else statements
- No exception handling (we haven't learned that yet)
- No advanced features like list comprehensions"
```

**Step 3: Ask for Understanding, Not Just Code**
```
"Instead of just giving me the code, can you:
- Explain why this approach is better
- Show me what happens step by step
- Help me understand the concept behind it
- Give me a simple example I can understand"
```

### **Example Teaching Session**

**Instructor Demo:**
```
"Let me show you two ways to ask AI for help with the same problem:

❌ Poor prompt: 'Write a function to add expenses to my finance tracker'

✅ Good prompt: 'I'm learning dictionaries and have a basic finance tracker 
structure like this: {expenses: {}, total: 0}. I want to add a new expense 
but I'm not sure how to create a good key for each expense. Can you show me 
a simple approach and explain why it works? Please use only basic dictionary 
operations we've covered in class.'

Notice how the good prompt:
- Sets context (learning level)
- Shows current understanding
- Asks for explanation, not just code
- Specifies appropriate complexity level"
```

---

## 📋 Instructor Guidelines for AI Discussion

### **When Students Show AI-Generated Code**

**🔍 Assessment Questions to Ask:**
1. "Can you explain how this code works line by line?"
2. "What parts of this code are new to you?"
3. "How did you prompt the AI to get this result?"
4. "What constraints did you give the AI about your learning level?"

**🚨 Red Flags to Watch For:**
- Exception handling (try/except blocks)
- List comprehensions or complex expressions
- Object-oriented design patterns
- Advanced libraries or imports
- Complex nested structures beyond course level
- Lambda functions or advanced Python features

**✅ Appropriate AI-Assisted Code Characteristics:**
- Uses only concepts covered in class
- Clear, simple variable names
- Basic dictionary operations (.get(), .items(), etc.)
- Simple control structures (if/else, for loops)
- Comments explaining each step
- Readable, beginner-friendly structure

### **Guiding Students to Better Prompts**

**When Students Show Poor AI Results:**
```
Instructor: "I see this code uses exception handling that we haven't 
covered yet. How did you ask the AI for help?"

Student: "I just said 'write a finance tracker'"

Instructor: "Let's try a better prompt together. What if you told the AI: 
'I'm a beginner learning dictionaries. Can you show me how to safely 
access a dictionary value that might not exist, using only basic 
dictionary methods we've learned in class?' What do you think that 
would give you?"
```

### **Encouraging Learning-Focused AI Use**

**✅ Praise Learning-Focused AI Use:**
```
"Great job asking the AI to explain the difference between dict[key] and 
dict.get(key)! I can see from your code that you understood the explanation 
and applied it correctly. That's exactly how AI should help your learning."
```

**🔄 Redirect Solution-Focused AI Use:**
```
"I see you got working code from AI, but let's make sure you understand it. 
Can you walk me through what each line does? If there's something unclear, 
let's ask the AI to explain that specific part."
```

---

## 🎯 Week 6 Specific AI Prompting Templates

### **Dictionary Fundamentals**
```
Template: "I'm learning dictionaries for the first time. I understand that 
they store key-value pairs, but I'm confused about [specific concept]. 
Can you explain this with a simple example using basic dictionary operations 
only?"

Examples:
- "...confused about when to use dictionaries instead of lists"
- "...confused about how .get() is different from using []"
- "...confused about how to iterate through key-value pairs"
```

### **Finance Tracker Context**
```
Template: "I'm building a personal finance tracker for a school project. 
I'm a beginner and we've only learned basic dictionaries. I need to 
[specific task] but I'm not sure [specific question]. Can you show me 
a simple approach using only basic Python and dictionary operations?"

Examples:
- "...need to store expense information but I'm not sure how to structure the dictionary"
- "...need to find all expenses in a category but I'm not sure how to search through the dictionary"
- "...need to calculate totals but I'm not sure how to add up values from the dictionary"
```

### **Debugging Help**
```
Template: "I'm a beginner working on a dictionary-based finance tracker. 
I'm getting this error: [error message]. Here's my code: [code]. I think 
the problem is [what they think] but I'm not sure. Can you help me understand 
what's wrong and how to fix it using concepts I should know at my level?"
```

### **Concept Clarification**
```
Template: "I'm learning about [specific dictionary concept] in class. I 
understand the basic idea but I'm confused about [specific aspect]. Can you 
give me a simple example and explain when I would use this in real programming?"

Examples:
- "...learning about dictionary methods like .keys() and .values()...confused about when to use each one"
- "...learning about nested dictionaries...confused about how to access values inside"
- "...learning about dictionary iteration...confused about the difference between different loop approaches"
```

---

## 📊 Assessment: Evaluating AI-Assisted Work

### **Appropriate AI Assistance Indicators**

**✅ Student Likely Used AI Well If:**
- Code matches current learning level complexity
- Student can explain all code components
- Comments show understanding of each step
- Student mentions specific prompting approach
- Code follows class patterns and conventions
- Evidence of iteration and refinement

**🔍 Questions to Verify Understanding:**
1. "Walk me through how this function works"
2. "What would happen if you changed this part?"
3. "How did you decide on this dictionary structure?"
4. "What other approaches did you consider?"
5. "How did the AI help you learn this concept?"

### **Inappropriate AI Assistance Indicators**

**⚠️ Student Likely Used AI Poorly If:**
- Code includes concepts not yet covered
- Student can't explain code components
- Solution is overly complex for the problem
- No evidence of understanding process
- Generic variable names or structure
- Perfect code with no iteration/refinement

**🔄 Remediation Approach:**
1. Don't penalise - use as teaching opportunity
2. Ask student to re-prompt AI with better constraints
3. Work together to simplify the solution
4. Focus on understanding over perfection
5. Praise learning-focused approach

---

## 🎪 Interactive AI Prompting Exercise

### **Classroom Activity: "Prompt the AI Right"**

**Setup (10 minutes):**
Present students with a common problem:
> "You want to find all expenses in the 'Food' category from your dictionary, but you're not sure how to search through it efficiently."

**Part 1: Bad Prompt Examples (5 minutes)**
Show poor prompts and their problematic results:
```
Bad: "Find food expenses in dictionary"
Result: Complex code with list comprehensions, exception handling, etc.
```

**Part 2: Good Prompt Development (10 minutes)**
Guide students to develop better prompts:
```
Step 1: Set context - "I'm a beginner learning dictionaries..."
Step 2: Specify constraints - "...using only basic operations like..."
Step 3: Ask for understanding - "...can you explain why this approach..."
```

**Part 3: Test and Compare (10 minutes)**
Have students try their improved prompts and compare results.

### **Take-Home Message**
*"AI is like a knowledgeable tutor - the better your questions, the better it can help you learn. Always ask for understanding, not just answers."*

---

## 🔄 Ongoing Support Strategies

### **Regular Check-ins**
- **Weekly prompt review**: Ask students to share one good AI prompt they used
- **Concept verification**: Quick questions about AI-assisted code
- **Peer learning**: Students share effective prompting strategies

### **Resource Creation**
- **Prompt bank**: Collect effective student prompts as examples
- **Common issues**: Document frequent AI-related problems and solutions
- **Success stories**: Share examples of effective AI-assisted learning

### **Integration with Assessment**
- **Prompt submission**: Ask students to submit their AI prompts with assignments
- **Reflection component**: "How did AI help your understanding this week?"
- **Process focus**: Assess learning process, not just final product

---

## 💡 Key Takeaways for Instructors

### **Foster Learning Partnership with AI**
- ✅ Encourage constraint-based prompting
- ✅ Emphasise understanding over completion
- ✅ Model effective AI interaction
- ✅ Celebrate learning-focused AI use

### **Monitor for Appropriate Complexity**
- 🔍 Check for concepts beyond current level
- 🔍 Verify student understanding of AI-generated code
- 🔍 Guide students to simpler, more appropriate solutions
- 🔍 Use AI assistance as teaching opportunity

### **Build AI Literacy Skills**
- 📚 Teach prompt engineering as core skill
- 📚 Show how AI can enhance (not replace) learning
- 📚 Develop critical evaluation of AI responses
- 📚 Integrate AI use into assessment process

**Remember: The goal is not to eliminate AI use, but to help students use it as an effective learning partner that supports their conceptual understanding at their current level.**

---

```markdown
## 🎯 Quick Reference: Good vs. Poor AI Prompts for Week 6

### ❌ POOR PROMPTS
- "Write my finance tracker"
- "Fix this code"
- "Make this work"
- "Create a dictionary program"

### ✅ GOOD PROMPTS
- "I'm learning dictionaries. Can you explain when to use dict.get() vs dict[key]?"
- "I'm confused about dictionary iteration. Can you show me the difference between these approaches?"
- "I have this error [shows error]. Can you help me understand what went wrong?"
- "I'm building a simple finance tracker. How would I structure a dictionary to store expense information?"

### 🎓 LEARNING-FOCUSED PHRASES TO TEACH
- "I'm a beginner learning..."
- "Can you explain why..."
- "Please use only basic features like..."
- "Help me understand..."
- "What's the difference between..."
- "Can you show me step by step..."
```