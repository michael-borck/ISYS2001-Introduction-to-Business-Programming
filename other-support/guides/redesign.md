# ISYS2001: Introduction to Business Programming - Course Redesign

## Course Philosophy

This redesigned unit embraces a modern, AI-assisted approach to programming. The central philosophy moves beyond simply writing code to focus on developing well-rounded software developers who can think critically, solve problems creatively, and effectively leverage modern tools like Generative AI. 

The learning journey is built around a semester-long project, the "Personal Finance Assistant," where students learn programming fundamentals through a hands-on, iterative process. This new theme prevents code sharing between semesters while maintaining strong engagement with fundamental concepts: sequence, selection, and repetition.

## Technology Stack (Zero-Install Approach)

- **Google Colab** (with built-in Gemini): Primary development environment
- **GitHub**: Version control and portfolio repository
- **NotebookLM**: Personal research and reflection assistant
- **Microsoft Teams**: Platform for final oral defense

This zero-install approach prioritizes accessibility and reduces technical overhead, ideal for beginners while introducing industry-standard tools.

## Weekly Schedule & "Stealth Blueprint" Tasks

The weekly labs form the core learning experience. Each lab concludes with a low-stakes "Lab Exit Ticket" - a short, creative task that reinforces the week's topic while secretly building fragments of the final project plan.

| Week | Begin Date | Topic | Lab Project | "Stealth" Lab Exit Ticket (Blueprint Fragment) |
|------|------------|-------|-------------|------------------------------------------------|
| 1 | 24 Feb | Intro to Python & "Vibe" Programming | "Prompt a Simple Budget Tracker" | "User Story Brainstorm": Write two 'user stories' for a simple budget app |
| 2 | 3 Mar | Variables & Data Types | "Categorize Your Spending" | "Data Requirements": List data needed and types (text, number, etc.) |
| 3 | 10 Mar | Conditionals & Decision Making (TDD Focus) | "Budget Alerts" (Write tests first) | "Define a Business Rule": Write one 'if-then' rule (e.g., "IF spending > $200, THEN alert") |
| 4 | 17 Mar | Functions | "Refactor with Functions" | "Identify Reusable Actions": Name three actions that could become functions |
| 5 | 24 Mar | Lists & Loops | "Transaction History" | "Describe a Collection": What data to store in a list? How would loops help? |
| 6 | 31 Mar | Dictionaries & Data Structures | "Spending Analysis" | "Structure Your Data": Sketch app data using a dictionary |
| 7 | 7 Apr | Business Data Processing | "Import/Export Transactions (CSV)" | "Plan Your Report": Design a simple text-based weekly report |
| 8 | 14 Apr | APIs & External Data | "Stock Portfolio Tracker" | "External Feature Idea": How to use external API (stocks, currency) |
| 9 | 21 Apr | | Tuition Free Week | |
| 10 | 28 Apr | Object-Oriented Programming (OOP) | "The Transaction and Budget Classes" | |
| 11 | 5 May | Files & Exception Handling | "Save and Load Your Budget" | |
| 12 | 12 May | Testing & Debugging (TDD Focus) | "Unit Testing Your Finance App" | |
| 13 | 19 May | Final Project Implementation & Review | "Finalizing Your Personal Finance Assistant" | |
| 14 | 26 May | | Study Week | |
| 15 | 2 Jun | | Examinations | |
| 16 | 9 Jun | | Examinations | |

## Assessment Strategy

### 1. Lab Exit Tickets (20%)

**Task**: Weekly "Stealth Blueprint" tasks

**Assessment Method**: 
- Previous week's task marked pass/fail at the beginning of each lab
- Encourages routine attendance and habit formation
- In-person verification through brief conversation with tutor

**Policy**: 
- Students must have 6 out of 8 tasks successfully marked for full credit
- One-week grace period: absent students can have two tasks marked at next attendance
- Reduces administrative overhead while maintaining flexibility

### 2. Programming Project (40%)

**Task**: "Personal Finance Assistant" application - a portfolio demonstrating the entire development process

**Required Deliverables**:

1. **Python Application Code**: 
   - Stored in GitHub repository
   - Clear commit history showing consistent work over time (not last-minute commits)

2. **Developer's Diary** (Markdown file in repository):
   - **Annotated AI Interactions**: Document key AI collaborations as "Evidence Packages":
     - **The Artifact**: 30-90 second screen recording/GIF showing the interaction
     - **The Context**: One-sentence description of the goal
     - **The Reflection**: Analysis covering:
       - What happened?
       - What did you do in response?
       - What did you learn?
   - **AI Critique**: Mandatory section showing function critiqued by a second AI
   - Supports various AI tools (ChatGPT, Gemini, Copilot, Cursor, etc.)

### 3. Final Exam: "Structured Defense & Live Refactoring" (40%)

**Format**: 15-minute one-on-one viva via Microsoft Teams during examination period

**Structure**:

**Part 1: Structured Defense (5 minutes)**
- Questions specific to student's submitted project and Developer's Diary
- Verifies authorship and understanding
- Examples:
  - "Walk me through your calculate_total_spending function"
  - "Why did you choose a dictionary instead of a list here?"
  - "Explain how you simplified the AI's file error handling suggestion"

**Part 2: Randomized Live Challenge (10 minutes)**
- New, unseen problem from secret question bank
- Student solves live while sharing screen
- Can use AI assistants but must narrate process
- Three challenge categories:
  - **Tier 1 - Refactoring (Easy)**: Improve poorly written but functional code
  - **Tier 2 - Debugging (Medium)**: Find and fix 2-3 bugs in provided function
  - **Tier 3 - Feature Extension (Hard)**: Add new feature using AI assistance

**Preparation**: 
- Practice examples published for each category
- Actual assessment questions remain secret
- Tests applied skills, not memorization

## Key Features of the Redesign

### 1. Test-Driven Development (TDD) Integration
- Introduced early (Week 3) to build good habits
- Becomes essential with AI-generated code verification
- Students write tests that define correctness; AI generates code to pass tests
- Creates framework for safely experimenting with AI suggestions

### 2. AI as Core Development Tool
- "Vibe programming" approach using LLMs as the IDE
- Students learn to:
  - Write effective prompts
  - Critically evaluate AI suggestions
  - Refactor and simplify AI-generated code
  - Use multiple AIs for code critique

### 3. Process Over Product
- GitHub commit history demonstrates consistent effort
- Developer's Diary shows thinking and learning journey
- Screen recordings provide authentic evidence of understanding
- Oral defense ensures students can explain and extend their work

### 4. Scalability Considerations
- 60 students with 1 instructor + 1 tutor
- 15 hours total assessment time (7.5 hours each)
- Can be completed over 3-4 days during exam period
- Teams recordings enable moderation and appeals process

## Benefits of This Approach

1. **Prevents Code Sharing**: New theme each semester makes reusing previous code ineffective
2. **Industry-Relevant Skills**: Students learn modern development practices with AI tools
3. **Authentic Assessment**: Oral defense with live coding accurately measures understanding
4. **Reduced Tech Support**: Zero-install approach eliminates installation issues
5. **Flexible Learning**: Accommodates different paces while maintaining standards
6. **Built-in Scaffolding**: Weekly tasks organically prepare students for final project

This redesign creates a modern, engaging, and pedagogically sound approach to teaching introductory programming that prepares students for the AI-augmented future of software development.