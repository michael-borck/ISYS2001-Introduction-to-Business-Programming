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

# ANSWERS: Introduction to Business Programming - Mock Extended Learning Portfolio

**Note to Students:** This staff answer demonstrates one possible approach to each section. Your solutions may differ while still being excellent. Pay particular attention to the **iterative prompting process** and **reflection quality** rather than trying to copy exact code.

---

## Section 1: Iterative Prompt Engineering (30 marks)

### 1.1 Initial Prompt & Pseudocode (8 marks)

**My Initial Prompt:**
```
I need to create a command-line quiz generator programme in Python for my programming course. The programme should load question/answer pairs from a text file, allow the user to specify how many questions they want, randomly select that many questions, present questions one by one and collect user answers, then calculate and display a final score.

Please provide pseudocode that only uses basic Python concepts suitable for our introductory course - no advanced features. Follow a structured planning approach with clear steps.
```

**AI's Pseudocode Response:**
```
PROBLEM RESTATEMENT:
Create an interactive CLI quiz system that reads questions from a file, randomly selects a subset, administers the quiz, and reports results.

INPUTS/OUTPUTS:
- Input: filename (string), number of questions (integer), user answers (strings)
- Output: questions presented to user, final score and percentage

EXAMPLE WALKTHROUGH:
File contains: "What is 2+2?|4", "Capital of France?|Paris", "Python creator?|Guido"
User wants 2 questions
System randomly picks questions 1 and 3
User answers "4" and "Guido" 
Score: 2/2 = 100%

PSEUDOCODE:
FUNCTION load_questions(filename):
    CREATE empty list questions
    OPEN file for reading
    FOR each line in file:
        SPLIT line by "|" to get question and answer
        ADD (question, answer) tuple to questions list
    RETURN questions

FUNCTION select_random_questions(questions, count):
    IF count > length of questions:
        SET count to length of questions
    RETURN random sample of 'count' questions from questions list

FUNCTION run_quiz(selected_questions):
    SET score to 0
    FOR each (question, correct_answer) in selected_questions:
        DISPLAY question to user
        GET user_answer from input
        IF user_answer equals correct_answer (case-insensitive):
            INCREMENT score
            DISPLAY "Correct!"
        ELSE:
            DISPLAY "Incorrect. Answer was: " + correct_answer
    RETURN score

MAIN PROGRAMME:
    GET filename from user
    GET number_of_questions from user
    SET questions = load_questions(filename)
    SET selected = select_random_questions(questions, number_of_questions)
    SET final_score = run_quiz(selected)
    CALCULATE percentage = (final_score / length of selected) * 100
    DISPLAY final results
```

**Course Reference:** "I used the 6-step problem-solving methodology from Week 2: Computational Thinking & Building Simple Interfaces"

### 1.2 Two Prompt Refinements (12 marks)

**First Refinement:**
```
Please refine the pseudocode to handle file validation and user input errors. Add specific error handling for when files don't exist, when the file format is incorrect, and when users enter invalid numbers for question count.
```

**AI's Updated Pseudocode:**
```
[Previous pseudocode enhanced with:]

FUNCTION load_questions(filename):
    IF filename does not exist:
        DISPLAY "Error: File not found"
        RETURN empty list
    
    CREATE empty list questions
    TRY:
        OPEN file for reading
        FOR each line in file:
            STRIP whitespace from line
            IF line is empty: CONTINUE
            IF "|" not in line:
                DISPLAY "Warning: Invalid format on this line, skipping"
                CONTINUE
            SPLIT line by "|" 
            ADD cleaned question/answer tuple to questions list
    EXCEPT file reading error:
        DISPLAY "Error: Could not read file"
        RETURN empty list
    RETURN questions

FUNCTION get_valid_number_input(prompt, max_value):
    WHILE True:
        TRY:
            GET user_input
            CONVERT to integer
            IF integer <= 0:
                DISPLAY "Please enter a positive number"
                CONTINUE
            IF integer > max_value:
                DISPLAY "Using maximum available: " + max_value
                RETURN max_value
            RETURN integer
        EXCEPT conversion error:
            DISPLAY "Please enter a valid number"
```

**Course Reference:** "This refinement applied basic file operations and error handling concepts from Week 7: Object-Oriented Programming (OOP) Fundamentals & File Operations"

**Second Refinement:**
```
Further enhance the pseudocode to include user experience improvements: add a main menu system, option to see score statistics, and better file format handling that can detect different delimiters automatically.
```

**AI's Final Pseudocode:**
```
[Previous pseudocode plus:]

FUNCTION detect_delimiter(sample_line):
    FOR delimiter in ["|", ",", "\t"]:
        IF delimiter in sample_line AND sample_line.count(delimiter) == 1:
            RETURN delimiter
    RETURN None

FUNCTION display_main_menu():
    DISPLAY menu options:
    1. Take Quiz
    2. View Statistics
    3. Exit

FUNCTION main_program():
    WHILE True:
        CALL display_main_menu()
        GET user_choice
        IF choice is 1:
            RUN quiz workflow
        ELIF choice is 2:
            DISPLAY previous scores if available
        ELIF choice is 3:
            EXIT
        ELSE:
            DISPLAY "Invalid choice"
```

**Course Reference:** "This refinement applied text-based menu design concepts from Week 2: Computational Thinking & Building Simple Interfaces"

### 1.3 Critical Analysis (10 marks)

**My Analysis (148 words):**

Each refinement significantly improved the robustness and user experience of the pseudocode. The first refinement addressed critical error handling that was completely missing from the initial version - file validation, input sanitization, and graceful degradation when users request more questions than available. This moved the code from a "happy path only" solution to something that could handle real-world usage scenarios.

The second refinement elevated the programme from basic functionality to a more polished application. The menu system and delimiter auto-detection make it more user-friendly, while the statistics feature adds value for repeat users.

The most impactful refinement was the first one, as it addressed fundamental reliability issues. Without proper error handling, the initial pseudocode would crash on common scenarios like missing files or malformed data. This connects directly to concepts from Week 7 about file operations and the importance of anticipating what could go wrong rather than assuming perfect inputs.

**Course References:** "My refinements applied the 6-step problem-solving methodology from Week 2: Computational Thinking, file operations concepts from Week 7: OOP Fundamentals & File Operations, and text-based interface design from Week 2: Building Simple Interfaces"

---

## Section 2: Debug & Correct Practice (25 marks)

### 2.1 Error Detection Practice (10 marks)

**My Initial Error Observations:**
- `memory` is used but `memories` is defined (line 23)
- Variable scope issue with `memory` in the final loop
- The conversation history logic seems incomplete

**My AI Prompt:**
```
Please analyse this chatbot code for a beginner programming student. Identify errors that a student would typically make, focusing on variable names, basic logic flow, and simple programming mistakes.
```

**AI's Complete Error Analysis:**
```
I found several errors in this chatbot code:

1. VARIABLE NAME ERROR (Line 23):
   - Uses `memory.append()` but the variable is named `memories`
   - This will cause a NameError at runtime

2. VARIABLE SCOPE ERROR (Line 28):
   - The for loop references `memory` but only `memories` exists
   - This will cause a NameError when trying to display conversation history

3. LOGIC ERROR:
   - Only bot responses are being stored in some places, not user inputs
   - The conversation history will be incomplete

4. POTENTIAL RUNTIME ERROR:
   - If the user types "quit" immediately, `memories` will be empty
   - The final loop will run but display nothing
```

**Comparison of Findings:**
I caught the main variable naming error by carefully reading through the code using systematic debugging approaches. The AI provided more comprehensive analysis including edge cases I hadn't considered, but my manual review using basic debugging helped me spot the core issues.

**Course Reference:** "I applied the debugging approach from Week 1: Introduction to AI-First Python & Python Fundamentals - identifying and fixing basic errors"

### 2.2 Fix & Learn (15 marks)

**My AI Prompt:**
```
Please provide the corrected version of this code using only basic Python techniques suitable for our introductory course. Include simple error fixes and make sure the conversation history works properly.
```

**My Hand-Written Corrected Version:**
```python
def simple_chatbot():
    """
    A basic chatbot that remembers conversation
    
    >>> # Test conversation memory structure
    >>> conversation_history = []
    >>> conversation_history.append("You: hello")
    >>> len(conversation_history)
    1
    """
    conversation_history = []  # Fixed: clearer variable name, consistent throughout
    print("Chatbot started! Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == "quit":
            print("Goodbye! Here's our conversation:")
            break
            
        # Store user input first - Fixed: was missing from original
        conversation_history.append(f"You: {user_input}")
            
        # Generate response using basic conditional logic
        if "hello" in user_input.lower():
            reply = "Hello there!"
        elif "how are you" in user_input.lower():
            reply = "I'm doing well, thanks!"
        elif "weather" in user_input.lower():
            reply = "I don't know about weather, sorry!"
        else:
            reply = "That's interesting! Tell me more."
            
        print(f"Bot: {reply}")
        # Fixed: store bot response with consistent variable name
        conversation_history.append(f"Bot: {reply}")
    
    # Show conversation history - Fixed: use correct variable name
    if conversation_history:  # Fixed: check if history exists before displaying
        for message in conversation_history:  # Fixed: use consistent variable name
            print(message)
    else:
        print("No conversation to display.")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    simple_chatbot()
```

**Course References:** 
- "My error handling approach comes from Week 1: Introduction to AI-First Python & Python Fundamentals - identifying and fixing basic errors"
- "My testing approach follows basic testing concepts that will be expanded in later weeks"

---

## Section 3: Debug & Refine Practice (20 marks)

### 3.1 Issue Identification Practice (6 marks)

**My Manual Review - Issues Found:**
1. No file existence checking - will crash if file doesn't exist
2. No validation that 'rating' column exists in the CSV
3. Generic exception handling masks specific errors
4. No handling of empty datasets or invalid rating values
5. Function doesn't handle file permission errors

**My AI Prompt:**
```
Please review this feedback analysis function for a beginner programming course. Identify potential problems with file handling, data validation, and error handling using only basic programming concepts.
```

**AI's Analysis:**
```
Several robustness issues identified:

1. FILE HANDLING ISSUES:
   - No check if file exists before reading
   - No handling of file permission errors
   - Assumes CSV format without validation

2. DATA VALIDATION PROBLEMS:
   - Assumes 'rating' column exists
   - No validation of rating data types
   - Could crash on non-numeric ratings
   - No handling of empty datasets

3. ERROR HANDLING DEFICIENCIES:
   - Generic try/except masks all errors
   - No informative error messages for users
   - Silent failures could be confusing
```

**Course References:**
- Applied file handling concepts from Week 7: Object-Oriented Programming (OOP) Fundamentals & File Operations
- Used error analysis approach from Week 8: Advanced OOP & Exception Handling
- Referenced data validation patterns from understanding CSV data structures (Week 6: Advanced Data Structures)

### 3.2 Function Improvement Practice (10 marks)

**My AI Prompts Used:**
```
Prompt 1: "Help me improve error handling for a CSV analysis function using only basic try/except blocks suitable for a beginner course."

Prompt 2: "What's the simplest way to check if a file exists and if a pandas DataFrame has the expected columns?"

Prompt 3: "Show me how to provide clear error messages that help users understand what went wrong."
```

**My Refined Function:**
```python
def refined_analyze_feedback(file_path):
    """
    Analyse customer feedback ratings from CSV file with basic error handling
    
    >>> refined_analyze_feedback("")
    Error: No file path provided
    >>> refined_analyze_feedback("nonexistent.csv")  # doctest: +SKIP
    Error: Could not read file
    """
    import os
    import pandas as pd
    
    try:
        # Basic input validation - check for empty file path
        if not file_path:
            print("Error: No file path provided")
            return None
        
        # Check if file exists before trying to read it
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' not found. Please check the file path.")
            return None
        
        # Attempt to read CSV with basic error handling
        try:
            df = pd.read_csv(file_path)
        except:
            print("Error: Could not read file. Check if it's a valid CSV.")
            return None
        
        # Check if dataset is empty
        if len(df) == 0:
            print("Warning: CSV file contains no data rows.")
            return {'message': 'No data to analyse', 'total_responses': 0}
        
        # Check for required 'rating' column
        if 'rating' not in df.columns:
            available_columns = ', '.join(df.columns.tolist())
            print(f"Error: Required 'rating' column not found.")
            print(f"Available columns: {available_columns}")
            return None
        
        # Basic data cleaning and validation
        original_count = len(df)
        # Remove rows with non-numeric ratings
        df = df[pd.to_numeric(df['rating'], errors='coerce').notna()]
        
        if len(df) == 0:
            print("Error: No valid numeric rating data found in 'rating' column.")
            return None
        
        # Calculate basic statistics
        avg_rating = round(df['rating'].mean(), 2)
        total_responses = len(df)
        
        # Simple categorization
        positive = df[df['rating'] >= 4]  # 4-5 stars
        negative = df[df['rating'] <= 2]  # 1-2 stars
        neutral = df[(df['rating'] > 2) & (df['rating'] < 4)]  # 3 stars
        
        # Build results dictionary
        results = {
            'average_rating': avg_rating,
            'total_responses': total_responses,
            'positive_count': len(positive),
            'negative_count': len(negative),
            'neutral_count': len(neutral),
            'positive_percentage': round((len(positive) / total_responses) * 100, 1)
        }
        
        return results
        
    except:
        print("Unexpected error occurred while analyzing feedback")
        return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

**Course References:**
- Error handling approach from Week 8: Advanced OOP & Exception Handling
- File validation techniques from Week 7: Object-Oriented Programming (OOP) Fundamentals & File Operations
- Testing approach follows concepts that will be reinforced in later course work
            'negative_count': len(negative),
            'neutral_count': len(neutral),
            'positive_percentage': round((len(positive) / total_responses) * 100, 1),
            'negative_percentage': round((len(negative) / total_responses) * 100, 1),
            'data_quality_note': 'Good sample size' if total_responses >= 30 else 'Limited sample size'
        }
        
        return results
        
    except Exception as e:
        print(f"Unexpected error occurred while analyzing feedback: {e}")
        return None
```

### 3.3 Comparison Practice (4 marks)

**2 Similarities:**
1. Both use basic file validation and check for the 'rating' column before processing
2. Both clean invalid rating data and provide clear categorization of positive/negative feedback

**2 Differences:**
1. The ideal version uses more detailed pandas exception handling; mine uses simpler generic try/except blocks suitable for our course level
2. The ideal version includes more comprehensive data quality reporting; mine focuses on essential validation only

**1 Course Connection:**
My version demonstrates basic exception handling patterns from Week 8: Advanced OOP & Exception Handling, using simple try/except blocks and clear user feedback messages.

**1 Learning Goal:**
This exercise connects to future work with data processing and web applications - I need to improve my approach to validating data before processing it in real-world scenarios.

---

## Section 4: Manual Implementation & Reflection Practice (25 marks)

### 4.1 Independent Coding Practice (15 marks)

**AI Syntax Help Used:**
```
Prompt: "What's the correct syntax for randomly sampling from a list in Python?"
AI Response: "Use random.sample(list, k) for sampling without replacement"
```

**My Manual Implementation:**
```python
import random
import os

def load_quiz_questions(file_path):
    """
    Load questions from file - basic file handling
    
    >>> # Test with sample data structure
    >>> questions = [("2+2?", "4"), ("Capital of France?", "Paris")]
    >>> len(questions)
    2
    >>> isinstance(questions[0], tuple)
    True
    """
    questions = []
    
    # Basic file validation
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return questions
    
    try:
        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                
                if '|' not in line:
                    print(f"Warning: Line {line_num} missing delimiter, skipping.")
                    continue
                
                parts = line.split('|', 1)  # Split on first | only
                if len(parts) == 2:
                    question = parts[0].strip()
                    answer = parts[1].strip()
                    if question and answer:  # Both must be non-empty
                        questions.append((question, answer))
                        
    except:
        print("Error: Could not read file")
    
    return questions

def select_random_questions(questions, num_questions):
    """
    Select N random questions from the list
    
    >>> sample_questions = [("Q1", "A1"), ("Q2", "A2"), ("Q3", "A3")]
    >>> selected = select_random_questions(sample_questions, 2)
    >>> len(selected)
    2
    >>> isinstance(selected, list)
    True
    """
    if not questions:
        print("No questions available to select from.")
        return []
    
    # Ensure we don't request more questions than available
    actual_num = min(num_questions, len(questions))
    
    if actual_num < num_questions:
        print(f"Only {len(questions)} questions available, selecting all.")
    
    # Use random.sample for sampling without replacement
    return random.sample(questions, actual_num)

def run_quiz_session(selected_questions):
    """
    Conduct quiz and return score
    
    >>> # This function requires user input, so we test the structure
    >>> test_questions = [("2+2?", "4")]
    >>> # run_quiz_session(test_questions)  # doctest: +SKIP
    """
    if not selected_questions:
        print("No questions to quiz on.")
        return 0
    
    score = 0
    total_questions = len(selected_questions)
    
    print(f"\n--- Starting Quiz: {total_questions} Questions ---")
    
    for i, (question, correct_answer) in enumerate(selected_questions, 1):
        print(f"\nQuestion {i}/{total_questions}: {question}")
        user_answer = input("Your answer: ").strip()
        
        # Case-insensitive comparison
        if user_answer.lower() == correct_answer.lower():
            print("✓ Correct!")
            score += 1
        else:
            print(f"✗ Incorrect. The answer was: {correct_answer}")
    
    # Display final results
    percentage = round((score / total_questions) * 100, 1)
    print(f"\n--- Quiz Complete ---")
    print(f"Final Score: {score}/{total_questions} ({percentage}%)")
    
    return score

if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

**Course References:**
- File handling techniques from Week 7: Object-Oriented Programming (OOP) Fundamentals & File Operations
- List operations and iteration from Week 4: Repetition & Fundamental Data Structures (Lists)
- Basic testing approach that prepares for future advanced testing concepts

### 4.2 Reflection Practice (10 marks)

**Workflow Balance (70 words):**
I used AI primarily for syntax verification and brainstorming error-handling approaches, but kept all architectural decisions and logic design as my own work. My strategy was to design the function structure first, implement the core logic manually, then consult AI for specific Python idioms I was uncertain about. This balance let me maintain ownership of the problem-solving while leveraging AI for efficiency in implementation details.

**AI Partnership Insights (70 words):**
AI exceeded expectations when I asked for comprehensive error-handling strategies - it suggested edge cases I hadn't considered, like file permissions and encoding issues. However, I had to override AI's suggestion to use a simple try-catch-all approach, instead implementing specific exception handling for different error types. This taught me that AI is excellent for brainstorming but I need to critically evaluate its suggestions against best practices.

**Skill Development (60 words):**
I'll improve my prompting by being more specific about context and constraints. Instead of asking "how do I handle errors?", I'll ask "what specific exceptions should I catch when reading CSV files in a user-facing application?" This iterative refinement approach will transfer directly to real projects where I need to research unfamiliar libraries or design patterns systematically.

---

## Conversation Log (Abbreviated)

```
SECTION 1 - INITIAL PROMPT:
I need to create a command-line quiz generator programme in Python...

AI RESPONSE:
[Comprehensive pseudocode with 6-step structure as shown above]

---

SECTION 1 - FIRST REFINEMENT:
Please refine the pseudocode to handle these additional requirements: file validation...

AI RESPONSE:
[Enhanced pseudocode with error handling as shown above]

---

SECTION 2 - ERROR ANALYSIS:
Please analyse this chatbot code and identify all errors, including syntax errors...

AI RESPONSE:
I found several errors: 1. SYNTAX/NAMING ERROR (Line 23): Uses memory.append()...

---

SECTION 3 - BRAINSTORMING:
Help me brainstorm comprehensive error handling for a CSV analysis function...

AI RESPONSE:
Consider these error scenarios: file not found, permission errors, malformed CSV...

---

SECTION 4 - SYNTAX CHECK:
What's the correct syntax for randomly sampling from a list in Python?

AI RESPONSE:
Use random.sample(list, k) for sampling without replacement

---
```

**Staff Notes for Students:**

1. **This is one approach among many valid solutions** - your code structure, variable names, and error handling strategies may differ while being equally correct.

2. **Focus on the process** - notice how the iterative prompting in Section 1 builds complexity gradually, and how AI is used strategically rather than for everything.

3. **Quality markers to emulate:**
   - Specific, detailed prompts that give AI context
   - Manual implementation that shows independent thinking  
   - Reflections that demonstrate metacognitive awareness
   - Comprehensive error handling in practical code

4. **Common student mistakes this avoids:**
   - Vague initial prompts that produce generic responses
   - Over-reliance on AI for basic programming logic
   - Shallow reflections that don't show real learning
   - Code that works for happy path but crashes on edge cases

Use this as a calibration tool, not a template to copy!