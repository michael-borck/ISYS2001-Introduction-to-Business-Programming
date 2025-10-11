---
format:
  pdf:
    toc: true
    number-sections: false
    colorlinks: true
  docx:
    toc: true
    number-sections: false
    highlight-style: github
  html:
    toc: true
    toc-expand: 2
    embed-resources: true
---

# Introduction to Business Programming - Mock Extended Learning Portfolio

**Duration:** 3 hours  
**Allowed Resources:** Course materials, internet, any AI assistant  
**Practice Purpose:** Familiarize yourself with exam format, course constraints, and AI collaboration workflow

## COURSE CONSTRAINTS - PRACTICE APPLYING THESE
**All code must use ONLY techniques taught during this semester.**
**Any use of concepts not covered in our course will result in zero marks for that section.**
**All answers require a cross reference to materials from our course.**


**Practice Goal:** Learn to constrain AI responses to your actual course knowledge level.

## GOOGLE COLAB + GITHUB WORKFLOW PRACTICE
**Setup Practice:**
1. Create **private GitHub repository** named `mock-exam-[yourname]`
2. Work in **Google Colab** using our standard course setup
3. **Practice saving to GitHub** after each section
4. Include **doctest examples** for all functions (our standard testing approach)

## Time Management Guide
- **Section 1:** 45 minutes (Iterative Prompting)
- **Section 2:** 40 minutes (Debug & Correct)
- **Section 3:** 50 minutes (Debug & Refine)
- **Section 4:** 45 minutes (Implement & Reflect)

## Submission Requirements
**GitHub Repository Practice:**
1. Create **private repository**: `mock-exam-[yourname]`
2. Work in **Google Colab** with our standard course environment
3. **Repository structure practice:**
   ```
   mock-exam-[yourname]/
   ├── Mock_Exam.ipynb (main notebook)
   ├── conversation_log.txt
   ├── any-other-files (if created separately)
   └── README.md (practice summary)
   ```
4. **Practice saving to GitHub** after each major section
5. **Practice sharing:** Share with study partner for feedback
6. **Practice tagging** final version as `v1.0`

### Notebook Cell Practice (Follow Course Standard)
```python
# Section X.Y - [Description]
# Course constraint: [Week X concept being practiced]

def function_name(parameters):
    """
    Brief description
    
    >>> function_name(test_input)
    expected_output
    """
    # Your implementation
    
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

### Conversation Log Format (Practice)
```
SECTION X - KEY INTERACTION:
My prompt: [Your important prompts]
AI response: [Useful AI responses - summarize if long]
Course constraint applied: [How you modified AI suggestions]
---
```

## Mock Assessment Rubric

| Section | Component | Marks | Practice Focus |
|---------|-----------|-------|----------------|
| **1** | Initial Prompt & Response | 8 | Learn course-constrained prompting |
| | Two Refinements | 12 | Practice systematic improvement |
| | Critical Analysis + Course Refs | 10 | Connect to course learning |
| **2** | Error Identification | 10 | Debug within course knowledge |
| | Fix & Manual Rewrite | 15 | Code at appropriate skill level |
| **3** | Issue Analysis + Course Connection | 6 | Apply course debugging concepts |
| | Function Refinement | 10 | Use only Week 8 techniques |
| | Comparison Analysis | 4 | Evaluate using course criteria |
| **4** | Manual Implementation | 15 | Independent coding practice |
| | Course-Connected Reflection | 10 | Authentic learning connections |
| **Total** | | **100** | |

---

## Section 1: Iterative Prompt Engineering Practice (30 marks)
**Time: 45 minutes**

You're building a CLI **Quiz Generator** that loads question/answer pairs from a file, randomly selects N questions, quizzes the user, and reports their score.

### Course Constraint Practice
Your pseudocode must reflect **only techniques taught through Week 10:**
- File reading with basic error handling (Week 6)
- Lists for storing questions (Week 2)
- Simple random selection (Week 7)
- Basic user input validation (Week 6)

### 1.1 Initial Prompt & Pseudocode (8 marks)
**Task:** Write your first AI prompt requesting pseudocode using the planning methodology from our course.

**Required:**
- Your solution must only use techniques taught in this semester
- **Reference:** State which specific week/topic taught the planning approach you're using

**Deliverable:** 
- Quote your exact prompt and the AI's complete pseudocode response
- **Course Reference:** "I used the planning method from [specific week/topic]"

### 1.2 Two Prompt Refinements (12 marks)
**Task:** Improve your prompt twice by adding details that address overlooked requirements.

**Deliverable:** For each refinement:
- Quote your refined prompt
- Quote AI's updated pseudocode
- **Course reference:** "This refinement applied [concept] from [specific week/topic]"

### 1.3 Critical Analysis with Course References (10 marks)
**Task:** In ≤150 words, analyse your prompt evolution with **specific course connections**:

**Required references:**
- Reference specific weeks/topics that influenced your approach
- Explain how your refinements applied course concepts
- Connect your final pseudocode to specific course learning

---

## Section 2: Debug & Correct Practice (25 marks)
**Time: 40 minutes**

### The Buggy Chatbot (Designed with Week 6-level errors)
```python
# broken_chatbot.py
def simple_chatbot():
    """A basic chatbot that remembers conversation - Week 6 skill level"""
    memories = []
    print("Chatbot started! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Goodbye! Here's our conversation:")
            break
            
        # Generate response using basic if/elif (Week 3 style)
        if "hello" in user_input.lower():
            reply = "Hello there!"
        elif "how are you" in user_input.lower():
            reply = "I'm doing well, thanks!"
        elif "weather" in user_input.lower():
            reply = "I don't know about weather, sorry!"
        else:
            reply = "That's interesting! Tell me more."
            
        print(f"Bot: {reply}")
        memory.append(f"You: {user_input}")  # Error 1: wrong variable name
        memories.append(f"Bot: {reply}")
    
    # Show conversation history
    for m in memory:  # Error 2: wrong variable name again
        print(m)

# Test the chatbot  
if __name__ == "__main__":
    simple_chatbot()
```

### 2.1 Error Detection Practice (10 marks)
**Task:**
1. **Before using AI:** Scan the code yourself using systematic debugging approaches
2. **Then prompt AI:** Create your own prompt to analyse this chatbot code
3. **Compare:** How did your manual approach compare to AI's findings?

**Deliverable:** 
- Your initial error observations using systematic debugging
- Your AI prompt and AI's complete error analysis
- Brief comparison noting which **course approach** helped you identify errors

**Course Reference:** "I applied the debugging approach from [specific week/topic]"

### 2.2 Fix & Learn (15 marks)
**Task:**
1. Create your own prompt asking AI to provide corrected code
2. **Then manually rewrite** the entire corrected script in a **new Colab cell**
3. Add **doctest examples** and comments explaining your fixes

**Required:**
- Use only techniques taught in our course
- **Course Reference:** "My error handling approach comes from [specific week/topic]"
- **Course Reference:** "My testing approach follows [specific week/topic]"

---

## Section 3: Debug & Refine Practice (20 marks)
**Time: 50 minutes**

### Current Feedback Analyzer (Week 8 complexity level)
```python
import pandas as pd

def analyze_feedback(file_path):
    """Analyse customer feedback ratings from CSV file - Week 8 version"""
    # Basic file reading - Week 6 style
    try:
        df = pd.read_csv(file_path)
    except:
        return "File error"
    
    # Calculate statistics using basic operations
    avg_rating = df['rating'].mean()
    total_responses = len(df)
    
    # Categorise feedback using simple comparisons
    positive = df[df['rating'] >= 4]
    negative = df[df['rating'] <= 2]
    
    results = {
        'average_rating': avg_rating,
        'total_responses': total_responses,
        'positive_count': len(positive),
        'negative_count': len(negative)
    }
    
    return results

def ideal_analyze_feedback(file_path):
    """Improved version using Week 8 concepts only"""
    try:
        # Basic input validation - Week 6 approach
        if not file_path:
            print("Error: No file path provided")
            return None
            
        df = pd.read_csv(file_path)
        
        # Check for empty data - basic validation
        if len(df) == 0:
            print("Warning: File contains no data")
            return None
        
        # Check for required column using basic approach
        if 'rating' not in df.columns:
            print("Error: 'rating' column not found")
            return None
        
        # Calculate statistics with basic error checking
        try:
            avg_rating = df['rating'].mean()
            total_responses = len(df)
            
            # Simple categorization
            positive = df[df['rating'] >= 4]
            negative = df[df['rating'] <= 2]
            neutral = df[(df['rating'] > 2) & (df['rating'] < 4)]
            
            results = {
                'average_rating': round(avg_rating, 2),
                'total_responses': total_responses,
                'positive_count': len(positive),
                'negative_count': len(negative),
                'neutral_count': len(neutral)
            }
            
            return results
            
        except:
            print("Error: Could not calculate ratings")
            return None
            
    except:
        print("Error: Could not read file")
        return None
```

### 3.1 Issue Identification with Course Connection (6 marks)
**Task:**
1. **Manual review:** List ≥3 issues using systematic function review
2. **For each issue:** Note which **course concept** provides the solution approach
3. **AI code review:** Create your own prompt for AI to review this function

**Required Course Connections:**
- Reference specific weeks/topics that apply to each issue you identify

### 3.2 Function Improvement Practice (10 marks)
**Task:** Create `refined_analyze_feedback(file_path)` in a **new Colab cell** using **only techniques taught in our course**:

**Required:**
- Use only error handling techniques from our course
- Include **doctest examples** following our course approach
- **Save to GitHub** after completing this function

**Practice Strategy:** 
- Create your own prompts to get AI suggestions within course constraints
- Quote your constraint-setting prompts
- Include your final code that matches our course complexity level

**Course References:**
- "My error handling approach uses concepts from [specific week/topic]"
- "My testing follows the approach from [specific week/topic]"

### 3.3 Comparison Practice (4 marks)
**Task:** Compare your refined version with the ideal version:
- **2 Similarities:** Basic approaches both versions share
- **2 Differences:** How they handle complexity differently
- **1 Course Connection:** Which **course concept** your version demonstrates best
- **1 Learning Goal:** How this connects to **future course requirements**

---

## Section 4: Manual Implementation & Reflection Practice (25 marks)
**Time: 45 minutes**

### 4.1 Independent Coding Practice (15 marks)
**Task:** From your Section 1 pseudocode, implement these core functions **manually in Colab cells using only techniques taught in our course**:

```python
def load_quiz_questions(file_path):
    """
    Load questions from file - basic file handling
    
    >>> # Test with sample data
    >>> questions = load_quiz_questions("sample_quiz.txt")  # doctest: +SKIP
    >>> len(questions) > 0  # doctest: +SKIP
    True
    """
    # Your implementation here - basic file operations only
    pass

def select_random_questions(questions, num_questions):
    """
    Select N random questions - basic random selection
    
    >>> sample_questions = [("Q1", "A1"), ("Q2", "A2"), ("Q3", "A3")]
    >>> selected = select_random_questions(sample_questions, 2)
    >>> len(selected)
    2
    >>> isinstance(selected, list)
    True
    """
    # Your implementation here - simple random selection
    pass

def run_quiz_session(selected_questions):
    """
    Conduct quiz and return score - basic loops and user interaction
    
    >>> # This function requires user input, so we test the structure
    >>> test_questions = [("2+2?", "4")]
    >>> # run_quiz_session(test_questions)  # doctest: +SKIP
    """
    # Your implementation here - basic loops and user interaction
    pass
```

**Course Constraints:**
- File format assumption: "Question text|Answer text" per line
- Use basic file operations with simple error handling
- Use only basic random selection methods taught in our course
- User interaction with simple input() and print()
- **Include appropriate doctest** for each function
- Variable names and logic matching our course examples
- **Save to GitHub** after implementing each function

**Complexity Target:** Should look like our course exercise solutions - functional but straightforward.

### 4.2 Course-Connected Reflection Practice (10 marks)
Write exactly 200 words addressing these questions with **authentic course references**:

**1. Course Constraint Application (≈70 words):**
How did you apply our course AI partnership guidelines when constraining AI responses? Reference a specific moment where you had to modify an AI suggestion to match our course principles.

**2. Learning Connection (≈70 words):**
Describe how this exercise connected to your experience in previous coursework. Which course error handling concept did you find most useful, and how does it compare to your earlier debugging approach?

**3. Skill Development (≈60 words):**
Based on this practice, what will you focus on for the real exam? Reference one specific area from our course that you want to improve before future assignments.

**Required Authenticity Markers:**
- Reference specific course materials and assignment names
- Use our course terminology consistently
- Connect to your actual learning timeline and experience
- **Bold** all specific course references

---

## Mock Exam Learning Guide

### Course Integration Practice
This mock exam helps you practice:
- **Constraining AI to course knowledge level**
- **Referencing specific course materials authentically**
- **Writing code that matches your current skill progression**
- **Connecting learning across different course components**

### Course Constraint Strategy Practice
Learn to prompt AI with phrases like:
- "using only concepts from Week X"
- "suitable for our introductory Python course"
- "matching the complexity of our course exercises"
- "no advanced features beyond what we've learned"

### Authentic Reference Practice
Practice connecting your work to:
- **Specific week numbers and topics from our 12-week course**
- **Actual course content and methodologies**
- **Real learning experiences from each week**
- **Course terminology and frameworks we've used**

### Red Flags to Avoid
Code that would indicate AI over-reliance:
- Complexity beyond current course level (Week 1-12 progression)
- Advanced Python features not covered in our course
- Exception handling beyond Week 8's try-except basics
- Generic programming terminology instead of our course-specific language

### Self-Assessment Questions
After completing this mock:
1. Does my code look like it came from our Week 7-8 skill level?
2. Are my course references specific and match our 12-week outline?
3. Did I successfully constrain AI to appropriate complexity for our course?
4. Would my instructor recognise this as my typical work quality?

### Preparation for Real Exam
Use this practice to:
- **Identify your optimal AI collaboration workflow**
- **Practice authentic course material referencing**
- **Calibrate appropriate code complexity for Weeks 1-12 progression**
- **Develop confidence in manual implementation**

The real exam will be more challenging and require greater independence, but the course constraint and referencing requirements will be identical.