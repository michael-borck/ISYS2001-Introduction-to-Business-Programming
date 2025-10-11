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

# Tutor Facilitation Guide: Building with Digital Lego
*Week 8: Object-Oriented Programming for BIS Students*

---

## Overview & Teaching Philosophy

### Core Approach
- **Concepts over syntax** - Focus on business problem-solving, not Python details
- **AI-assisted discovery** - Students guide AI conversations, you facilitate understanding
- **Real-world connections** - Every concept ties to business systems students know
- **Hands-on exploration** - Learning through doing, not lecturing

### Your Role as Facilitator
- **Guide, don't lecture** - Students discover through AI interaction and peer discussion
- **Focus on understanding** - "Why does this solve business problems?" not "How does Python work?"
- **Encourage experimentation** - It's safe to try things and make mistakes
- **Connect to their experience** - Help them see OOP in apps they use daily

---

## Pre-Session Preparation

### What Students Should Have Done
✅ Completed Modules 1-3 (self-paced video content)  
✅ Tried the interactive quiz and flashcards  
✅ Brought questions about concepts they found unclear  

### What You Need to Prepare
- [ ] Test all notebooks work in your Colab environment
- [ ] Have the OOP Quick Reference handout ready (physical or digital)
- [ ] Prepare 2-3 real business examples relevant to your students
- [ ] Review common AI prompting pitfalls (see troubleshooting section)

### Room Setup
- Students in pairs or groups of 3
- Each group needs laptop access to Google Colab
- Ensure reliable internet for AI interactions
- Have backup: printed code examples if internet fails

---

## Session Structure (2-3 hours)

## Hour 1: Worksheet 1 - AI-Assisted Discovery

### Opening (10 minutes)
**Check Understanding:**
- "Who can give me an example of using objects in Python without realizing it?"
- "What business do you want to analyze today?" (for Part 1)

**Set Expectations:**
- "Today you're the project manager, AI is your developer"
- "Your job: guide AI with good business requirements"
- "My job: help you critique and improve AI suggestions"

### Part 1: Business Analysis (20 minutes)
**Facilitation Tips:**
- **Move between groups** - ensure they're getting good AI responses
- **If AI gives jargon:** Help them rephrase prompts more business-focused
- **Encourage specificity:** "Coffee shop" gets better responses than "business"
- **Look for patterns:** Groups should see similar object types emerging

**Common Issues & Solutions:**
| Problem | Student Says | Your Response |
|---------|--------------|---------------|
| AI too technical | "I don't understand 'instantiate'" | "Ask AI to explain using business forms instead of technical terms" |
| Vague responses | "AI just lists random things" | "Try: 'What daily tasks does a [business] need to track?'" |
| Analysis paralysis | "There are too many objects" | "Pick the 3 most important things customers interact with" |

### Part 2: Transaction Class Building (25 minutes)
**Key Teaching Moments:**
- **When AI gives perfect code:** "That's suspiciously perfect. What might go wrong?"
- **When students get errors:** "Great! Errors teach us. What is Python complaining about?"
- **Emphasize the business logic:** "Does this solve the CSV + manual entry problem?"

**Watch for:**
- Students copying AI code without understanding
- Groups not testing their code
- Focus on syntax instead of business problem

**Intervention Strategies:**
```
Instead of: "Your syntax is wrong"
Try: "Ask AI to explain what this line does for your business"

Instead of: "Use self.amount"  
Try: "How does each transaction remember its own amount?"
```

### Part 3: CSV Integration Challenge (20 minutes)
**This is where it clicks!** Students see OOP solving real problems.

**Facilitation Focus:**
- Emphasize the "aha moment" - same Transaction class works for both data sources
- Ask probing questions: "Why is this better than keeping CSV and manual data separate?"
- Connect to their experience: "How does your banking app handle transfers vs direct deposits?"

**Red Flags:**
- Group suggests different classes for different data sources (missed the point)
- AI solutions that are overly complex (guide toward simpler business logic)
- Students not seeing the scalability benefit

---

## Hour 2: Worksheet 2 - Gradio Integration

### Part 1: UI Object Discovery (15 minutes)
**Teaching Goal:** Students realize Gradio components are objects too

**Better Questions to Ask:**
- "What happens when you call gr.Textbox()?"
- "How is this like creating a customer form in a business?"
- "What's the connection between UI objects and your Transaction objects?"

### Part 2-3: Class Building Review (20 minutes)
**Quick Assessment:**
- Can groups explain their Transaction class in business terms?
- Do they understand how it works with both CSV and manual data?
- If not, use pair programming: stronger group helps weaker group

### Part 4: The Magic Connection (30 minutes)
**This is the climax!** Different object types working together.

**Scaffold the Understanding:**
1. "What does the textbox object do?" (collects user input)
2. "What does your Transaction class do?" (structures financial data)  
3. "What connects them?" (the function that bridges UI to business logic)

**Common Struggles:**
- **"It's too complex"** → Break it down: "Just focus on one textbox connecting to one Transaction"
- **"AI code doesn't work"** → Debug together: "Let's trace the data flow step by step"
- **"I don't see the point"** → Connect to experience: "How does your banking app work?"

### Part 5: Integration Testing (25 minutes)
**Make it real!** Students see their complete system working.

**Celebration Moments:**
- First successful transaction entry
- CSV data loading correctly
- Summary reports generating

**Teaching Opportunities:**
- "Why does this design scale to 1000 transactions?"
- "How would you add budgeting features?"
- "What other business systems work this way?"

---

## Troubleshooting Guide

### Common AI Prompt Problems

| Student Problem | Better Prompt Guidance |
|----------------|----------------------|
| Gets technical jargon | "Ask AI to explain like you're talking to your boss, not a programmer" |
| Code doesn't work | "Tell AI what error you got and ask for a business-focused fix" |
| Solution too complex | "Ask AI for the simplest version that solves the business problem" |
| Missing business logic | "Ask AI how this helps users, not just how the code works" |

### When to Provide the Quick Reference
- Student asks "What does `self` mean?"
- AI explanation gets too technical despite good prompts
- Group is stuck on syntax instead of concepts
- Advanced student wants deeper understanding

**How to Introduce It:**
> "Here's a reference sheet for when AI gets too technical. Your main job is still business problem-solving, but this explains the Python pieces if you need it."

### Debugging Student Understanding

| Warning Sign | Intervention |
|-------------|-------------|
| "I'll just copy the AI code" | "First, explain what business problem this solves" |
| "This is too hard" | "You already use objects every day. Tell me about your favorite app" |
| Focus only on making code work | "Great! Now why is this better for businesses than spreadsheets?" |
| Can't connect concepts | "Draw the data flow: user input → objects → business insights" |

---

## Assessment & Wrap-up

### Quick Understanding Checks
**Instead of:** "Do you understand classes?"  
**Try:** "Explain to me how Netflix uses objects to manage movies and users"

**Instead of:** "Can you write a method?"  
**Try:** "How would you add budget tracking to your finance app?"

### Wrap-up Questions (Last 15 minutes)
1. **Business Connection:** "Name an app you use that definitely uses the individual + system object pattern"
2. **Problem Solving:** "What business problem did OOP solve that spreadsheets couldn't?"
3. **AI Partnership:** "How did working with AI change how you approach coding?"
4. **Scalability:** "Why can Netflix handle millions of users with this approach?"

### Success Indicators
✅ Students can explain OOP benefits in business terms  
✅ Groups successfully connected different object types  
✅ Students guided AI effectively with business-focused prompts  
✅ Clear understanding of why this scales better than alternatives  

---

## Advanced Student Challenges

### For Students Who Finish Early
1. **Add budgeting logic** to their FinanceTracker
2. **Design a Customer class** for an e-commerce system  
3. **Extend Gradio interface** with charts/visualizations
4. **Help other groups** with their AI conversations

### Deeper Discussion Topics
- How do large systems like Amazon organize millions of objects?
- What happens when business requirements change?
- How does this approach support team development?
- Connection to database design and enterprise systems

---

## Common Misconceptions & Corrections

| Misconception | Reality | How to Address |
|--------------|---------|----------------|
| "OOP is just fancy syntax" | "OOP mirrors business organization" | Show real business examples |
| "Objects are hard" | "You use objects constantly" | Point out string.upper(), list.append() |
| "This is only for big systems" | "Scales from small to enterprise" | Start with simple examples, show growth |
| "AI will do everything" | "You provide business insight" | Emphasize human judgment in prompting |

---

## Post-Session Follow-up

### Encourage Students To:
- Try the interactive quiz/flashcards for reinforcement
- Experiment with their finance app design
- Look for object patterns in other apps they use
- Practice business-focused AI prompting

### Red Flags for Next Session:
- Students still thinking in procedural terms
- Confusion about individual vs system objects  
- Over-reliance on AI without understanding
- Missing the business problem-solving angle

### Success Stories to Celebrate:
- Groups that made creative business connections
- Effective AI collaboration and critiquing
- Students helping each other understand concepts
- Real "aha moments" about scalability and organization

---

## Key Phrases for Facilitation

### Redirect Technical Focus:
- "Let's think about the business problem first"
- "How does this help users accomplish their goals?"
- "What would happen if this was a real company?"

### Encourage AI Collaboration:
- "What would you ask AI to clarify that?"
- "How could you rephrase that prompt to get a better response?"
- "What business context is AI missing?"

### Build Confidence:
- "You're already thinking like a systems analyst"
- "That's exactly how real business systems work"
- "You've identified the core pattern that scales"

### Connect to Experience:
- "How does [app they know] handle this?"
- "What would your boss want to know about this?"
- "How is this like organizing a real business?"

---

## Remember: Your Success Metrics

✅ Students leave excited about building systems  
✅ Clear connection between OOP and business problem-solving  
✅ Confidence in guiding AI for development tasks  
✅ Understanding that scales beyond this course  

**You're not teaching Python syntax - you're teaching systems thinking that will serve them throughout their BIS careers!**