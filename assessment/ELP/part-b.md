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

# Assessment 3: Viva Question Bank v2.1

## ISYS2001 Introduction to Business Programming

**Purpose:** This question bank contains all possible questions for Part B of your screencast assessment. You will be randomly assigned questions from different categories to ensure a balanced assessment of your knowledge and analytical skills.

**Important:** This question bank covers Part B of your screencast. Remember that your full video submission must also include Part A: The Project Tour.

> This is a supporting document for Assessment 3. For the complete assessment overview, submission requirements, and marking criteria, see the **"Assessment 3: Master Specification"** document.

---

## How to Use This Question Bank

**For Revision:**

- Review every question in all three categories
- Practice explaining each concept using examples from your own project
- Focus on the "why" behind your decisions, not just the "what"
- Think about how you would demonstrate your answers on screen

**Assignment Structure:**
You will receive **one question from Category A** (Core Concepts), **one question from Category B** (Design & Justification), and **one question from Category C** (Critical Analysis). This ensures you demonstrate both foundational knowledge and higher-order thinking.

**Important Notes:**

- You cannot choose your questions—they are randomly assigned
- All questions are weighted equally within the "Analytical Response" marking criterion
- Each answer should be approximately 2 minutes (total 4-6 minutes for both/all questions)
- Generic textbook answers will receive low marks—we want to see YOUR code and YOUR thinking

---

## Relationship Between Part A and Part B

**Important Context:** Your Part A (Project Tour) already covers several topics at an introductory level. Some Part B questions will ask you to expand on these topics with deeper analysis.

### If Your Question Overlaps with Part A

Don't worry about repetition—this is expected and intentional. However, your approach should differ:

**What you did in Part A:**

- Showed your code structure and organisation
- Demonstrated key features working
- Briefly explained major design choices
- Provided overview-level justification

**What Part B expects:**

- Deeper technical analysis and critical thinking
- Discussion of alternatives you considered
- Explicit trade-off analysis
- Honest evaluation of limitations
- Connection to broader programming principles from the unit

**Handling overlap effectively:**

✅ **Good approach:**
> "In my project tour, I showed how I structured my code into three modules. Now I'll explain why this was better than a single-file approach, and discuss the trade-offs. A single file would have been simpler to deploy but harder to test. I chose modularity because... [deeper analysis]. If I were building this for production, I'd also consider..."

❌ **Weak approach:**
> "As I said before, I organised my code into modules because it's better organised. It works well and is easy to understand."

### Expected Depth by Part

| Aspect | Part A (Project Tour) | Part B (Analytical Response) |
|--------|----------------------|------------------------------|
| **Code Structure** | "Here's how I organised it" | "Why this organisation vs. alternatives; trade-offs" |
| **Key Functions** | "This function does X" | "Why this approach vs. other algorithms; complexity" |
| **Design Choice** | "I chose approach X" | "I chose X over Y because... Under Z conditions, Y would be better..." |
| **Demonstration** | "Here it is working" | "Here's why it works this way; here's where it would break" |

**Bottom line:** If you get a Part B question about something from Part A, you should:

1. Briefly reference your Part A explanation (5-10 seconds)
2. Spend the remaining ~110 seconds on deeper analysis, alternatives, and critical evaluation

---

## Category A: Core Concepts in Practice

*Focus: Testing foundational knowledge by using your project as the primary example. These questions assess your understanding of fundamental programming concepts as implemented in your own work.*

### A1. Data Structures

**Question:** Select the most important data structure (e.g., list, dictionary, set, class, tuple) in your project. Show us where it appears in your code and justify why it was the right choice over at least one alternative for its specific purpose. Discuss the trade-offs of your choice.

---

### A2. Functions & Modularity

**Question:** Choose one of your key functions or methods. Show us the code, explain its purpose, walk through its parameters and return value, and explain how it contributes to the overall program logic. Discuss why you structured it this way rather than implementing the logic differently.

---

### A3. Control Flow

**Question:** Find a complex conditional (`if/elif/else`) block or loop in your code. Display it on screen and walk through its logic step-by-step. Explain why it is structured the way it is to handle different cases, and discuss what would happen if the logic were simplified or changed.

---

### A4. Error Handling

**Question:** Identify a specific part of your code where errors could occur (e.g., user input, file reading, data processing, calculations). Show us the relevant code and demonstrate how your program anticipates and handles these potential errors. If you didn't implement error handling in a particular area, explain what could go wrong and how you would address it.

---

### A5. Code Reuse & Libraries

**Question:** Identify an instance where you utilised code reuse—whether through an external library, a built-in module, a helper function you wrote, or importing your own code. Show the specific code that demonstrates this and explain why reusing or importing code was better than writing everything from scratch. Discuss what you gained (or lost) through this choice.

---

### A6. Iteration & Recursion

**Question:** Identify a place in your project where you use iteration (loops) to solve a problem. Explain how your loop works and why you chose iteration for this task. Then discuss whether recursion could have been used instead—if yes, explain why you didn't use it; if no, explain why recursion wouldn't work for this particular problem.

---

### A7. String or Data Processing

**Question:** Find a part of your code that manipulates, processes, or transforms data (this could be string operations, list comprehensions, data parsing, calculations, etc.). Show the specific code and explain step-by-step what transformations occur. Justify why you chose this particular approach to processing the data.

---

## Category B: Design Choices & Justification

*Focus: Testing the "why" behind your code's architecture and decisions. These questions assess your ability to articulate and defend the design decisions you made.*

**Note:** While some Category B questions may relate to topics introduced in Part A, these questions require deeper justification, discussion of alternatives, and analysis of trade-offs. You should go significantly beyond what you covered in your Project Tour.

---

> 📘 **Note for Questions B1-B6:**
>
> These questions may overlap with content from your Project Tour (Part A). This is intentional and expected.
>
> **Your task:** Don't just repeat what you said in Part A. Instead:
>
> - Acknowledge briefly what you already showed
> - Then provide NEW analysis: alternatives considered, trade-offs, what you'd change, why other approaches might work better in different contexts
>
> **Example:**
> "In my project tour, I showed my three-module structure. Now let me explain why I didn't use a class-based architecture instead. Classes would have provided... but for this project's scope... The trade-off is..."

### B1. Code Structure & Architecture

**Question:** Provide a high-level overview of your project's architecture. Show us your file structure or main modules and justify why you organized your code this way. Specifically, explain why you split (or didn't split) your code into different files, modules, or classes, and discuss the benefits of your organizational approach.

---

### B2. Key Algorithm or Logic

**Question:** Identify the most important algorithm or core piece of logic you implemented or used in your project. Show the specific code and explain how it works step-by-step, referencing the actual lines in your implementation. Discuss why this particular approach was appropriate for your problem.

---

### B3. Data Flow

**Question:** Trace the complete path of a key piece of data through your program. Show us where it originates (user input, file, hardcoded, etc.), how it is processed or transformed through different parts of your code, and what its final output or use is. Use your actual code to illustrate each stage of this journey.

---

### B4. Most Challenging Problem

**Question:** What was the most difficult technical problem you solved in this project? Show the exact code that implements your solution and walk us through your thought process. Explain what made it challenging and why your solution works. Discuss any alternative approaches you considered.

---

### B5. User Interaction Design

**Question:** Demonstrate how a user interacts with your program (whether through a GUI, command-line interface, web forms, or other means). Show the relevant code that handles this interaction and justify the design choices you made for accepting input and presenting output. Discuss what makes this approach user-friendly or what you'd improve.

---

### B6. File Operations or Data Persistence

**Question:** If your project reads from or writes to files (or uses any form of data persistence), show us the specific code that handles this. Explain your choice of file format or storage method, and demonstrate what happens during a read or write operation. If your project doesn't use files, explain how you would implement data persistence if it were required and why you'd choose that particular approach.

---

## Category C: Critical Analysis & Reflection

*Focus: Testing your ability to evaluate your own work and consider alternatives. These questions assess higher-order thinking—analysis, evaluation, and metacognition.*

### C1. Limitations & Weaknesses

**Question:** What is the single biggest limitation or weakness of your project in its current state? Be specific and show us the code that demonstrates or causes this limitation. Explain why it's a problem and discuss how you would begin to address it if you had more time or resources.

---

### C2. Scalability & Performance

**Question:** Imagine your project needed to handle 100 times more data, users, or transactions. Identify the part of your code that would become the biggest performance bottleneck. Show us this code and explain why it would struggle with scale. Discuss what changes you would need to make to improve its scalability.

---

### C3. Refactoring & Code Quality

**Question:** Select a function or section of code you are least satisfied with—perhaps it's messy, repetitive, poorly organised, or harder to understand than it should be. Show us this code and explain specifically what's wrong with it. Describe how you would refactor it for better readability, efficiency, or maintainability, and explain why you made the pragmatic choice to leave it as-is (if you did).

---

### C4. Testing & Validation

**Question:** How did you verify that your code works correctly and reliably? Show us a specific test case or scenario you used (whether formal unit tests, manual testing, or debugging examples). Walk through how you tested this aspect and explain how you know your program handles it correctly. If you didn't implement systematic testing, describe what testing approach would be most appropriate for your project and why.

---

### C5. Future Feature or Extension

**Question:** Propose one significant new feature or capability you would add to your project if you continued working on it. Explain what this feature would do, why it would be valuable, and discuss what specific changes or additions you would need to make to your current codebase to implement it. Show us the parts of your existing code that would need to be modified or extended.

---

### C6. Alternative Approaches

**Question:** Choose one major component or feature of your project. Explain how you implemented it, then describe at least one completely different way you could have achieved the same result (different algorithm, different data structure, different library, different design pattern). Compare the two approaches objectively—what are the trade-offs? Why did you choose your approach, and under what circumstances would the alternative be better?

---

## What Makes a Strong Answer?

Don't memorise scripts or try to sound overly formal. The goal is to naturally demonstrate that you understand your own code. Focus on these principles:

**Strong answers:**

- Start by immediately showing your code on screen (don't talk about it abstractly first)
- Use specific file names, function names, and line numbers from YOUR project
- Explain your reasoning process: "I chose X because Y, and the alternative Z wouldn't work because..."
- Use your cursor to point and guide attention to specific parts of your code
- Run your code to demonstrate concepts when relevant
- Sound natural and conversational, not rehearsed
- Admit limitations honestly: "Looking back, I should have..." is often better than claiming perfection
- Connect your specific code to broader programming concepts from the unit

**Weak answers:**

- Could apply to anyone's project (too generic)
- Use vague language: "it's better", "more efficient", "it works well" without explaining why
- Never show actual code running or point to specific lines
- Sound like you're reading a script you don't fully understand
- Make claims you can't back up with evidence from your code
- Spend most of the time on background and little time on your actual implementation
- Use circular reasoning: "It's complex because it does many things"

**Remember:** We can tell the difference between someone who built and understands their code versus someone who is trying to sound like they do. Be authentic, be specific, and show us your work.

---

## Tips for Preparing Strong Answers

### Do

✅ Reference your Part A tour when relevant, but don't just repeat it
✅ Open your actual code files and point to specific lines  
✅ Run your program to demonstrate concepts  
✅ Use your mouse/cursor to guide the viewer's attention  
✅ Explain the "why" behind your choices, not just the "what"  
✅ Be honest about limitations or what you'd do differently  
✅ Connect your answer to concepts learned in the unit  
✅ Practice explaining out loud before recording  
✅ Think about trade-offs and alternatives

### Don't

❌ Read generic definitions from slides or notes  
❌ Provide answers that could apply to any project  
❌ Ignore the specific requirements of the question  
❌ Claim your code is perfect when it isn't  
❌ Spend all your time on background and not enough on your actual code  
❌ Forget to show your face on camera  
❌ Exceed the 2 minute allocation per question  
❌ Make vague claims without evidence from your code

---

## Understanding the Categories

**Category A (Core Concepts):** These questions test whether you understand fundamental programming concepts. You should be able to identify these concepts in your own code and explain them clearly. Even if you didn't use a particular concept (like recursion), you should be able to discuss why you didn't and what you used instead.

**Category B (Design & Justification):** These questions test whether you can articulate the reasoning behind your code's structure and implementation. The key word is "why"—not just what your code does, but why you built it that way. Every design choice has trade-offs; strong answers acknowledge this.

**Category C (Critical Analysis):** These questions test your ability to think critically about your own work. They require you to step back and evaluate your project objectively—what worked well, what didn't, what would you change? There's no shame in identifying limitations; in fact, recognising them demonstrates maturity and understanding.

---

## Final Reminders

- **You will receive questions from multiple categories to balance different types of thinking**
- **You cannot predict which questions you'll get—prepare for all of them**
- **Your answers must reference YOUR specific project code**
- **Generic, memorised answers will receive low marks**
- **Demonstration and justification are more important than claiming perfection**
- **Honest, thoughtful analysis of your work is valued highly**

Good luck with your preparation!

---

*Question Bank v2.1 | Released Thursday 22 October 2025*

Change Log:

- v2.0 (15 Oct 2025): Initial release for ISYS2001 S2 2025
- v2.1 (22 Oct 2025): Minor wording adjustments for clarity