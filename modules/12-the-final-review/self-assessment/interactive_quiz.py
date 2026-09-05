"""
Interactive Quiz Application for ISYS2001 Final Review
Self-assessment tool with randomized questions across four topic areas
"""

import random
import sys


# Question bank organized by topic area
QUESTION_BANK = {
    "fundamentals": [
        {
            "question": "What data type would you use to store a user's age?",
            "options": ["str (string)", "int (integer)", "float", "bool (boolean)"],
            "answer": 1,
            "explanation": "Age is a whole number, so int (integer) is the appropriate data type."
        },
        {
            "question": "What is the purpose of the 'elif' statement in Python?",
            "options": [
                "To check a new condition if all previous conditions were false",
                "To repeat code multiple times",
                "To define a function",
                "To handle errors"
            ],
            "answer": 0,
            "explanation": "elif allows you to check a new condition only if the previous if/elif conditions were false."
        },
        {
            "question": "Which loop would you use when you don't know how many times to repeat?",
            "options": ["for loop", "while loop", "if loop", "repeat loop"],
            "answer": 1,
            "explanation": "A while loop is used when the number of repetitions is unknown and depends on a condition."
        },
        {
            "question": "What does the 'range(5)' function generate?",
            "options": ["Numbers 1 to 5", "Numbers 0 to 4", "Numbers 0 to 5", "Numbers 1 to 4"],
            "answer": 1,
            "explanation": "range(5) generates numbers from 0 up to (but not including) 5: 0, 1, 2, 3, 4."
        },
        {
            "question": "What operator would you use to check if BOTH conditions are true?",
            "options": ["or", "and", "not", "xor"],
            "answer": 1,
            "explanation": "The 'and' operator requires all conditions to be true for the overall condition to be true."
        },
        {
            "question": "What is the correct way to store multiple expenses in Python?",
            "options": ["As separate variables", "In a list", "In a string", "In a boolean"],
            "answer": 1,
            "explanation": "A list is the appropriate data structure for storing multiple related items like expenses."
        },
        {
            "question": "In a grade calculator, why must you check from highest to lowest score?",
            "options": [
                "It runs faster",
                "To ensure the correct grade is assigned",
                "Python requires it",
                "It doesn't matter"
            ],
            "answer": 1,
            "explanation": "Checking from highest to lowest ensures the first matching condition gives the correct grade."
        },
        {
            "question": "What does 'len(expenses)' return?",
            "options": [
                "The sum of all expenses",
                "The largest expense",
                "The number of items in the list",
                "The average expense"
            ],
            "answer": 2,
            "explanation": "len() returns the count of items in a collection like a list."
        },
        {
            "question": "What is the purpose of the 'try' block in error handling?",
            "options": [
                "To try running risky code that might fail",
                "To repeat code multiple times",
                "To define a function",
                "To create a loop"
            ],
            "answer": 0,
            "explanation": "The try block contains code that might raise an exception, allowing you to handle errors gracefully."
        },
        {
            "question": "What type of value can a boolean variable store?",
            "options": ["Text only", "Numbers only", "True or False only", "Any value"],
            "answer": 2,
            "explanation": "Boolean variables can only store True or False values."
        }
    ],
    "structure_data": [
        {
            "question": "What is the main advantage of using functions in your code?",
            "options": [
                "They make code run faster",
                "They allow code reuse and better organization",
                "They reduce file size",
                "They prevent all errors"
            ],
            "answer": 1,
            "explanation": "Functions enable code reuse and modular organization, making programs easier to maintain."
        },
        {
            "question": "What is the difference between 'return' and 'print' in a function?",
            "options": [
                "They do the same thing",
                "return sends a value back to be used; print displays to screen",
                "print is faster",
                "return is only for numbers"
            ],
            "answer": 1,
            "explanation": "return provides a usable value that other code can work with, while print just displays information."
        },
        {
            "question": "What are parameters in a function?",
            "options": [
                "Errors in the code",
                "Data passed into the function to make it flexible",
                "The function's output",
                "Comments in the code"
            ],
            "answer": 1,
            "explanation": "Parameters are inputs that allow functions to work with different data each time they're called."
        },
        {
            "question": "What is the purpose of importing modules like 'datetime'?",
            "options": [
                "To make code run slower",
                "To access pre-built functionality",
                "To create errors",
                "To define variables"
            ],
            "answer": 1,
            "explanation": "Modules provide pre-built tools and functions so you don't have to build everything from scratch."
        },
        {
            "question": "How do you access a value in a dictionary?",
            "options": [
                "By position number",
                "By key name",
                "By random selection",
                "You can't access individual values"
            ],
            "answer": 1,
            "explanation": "Dictionaries use keys to access their associated values, like transaction['amount']."
        },
        {
            "question": "What does 'pd.read_csv()' do?",
            "options": [
                "Creates a new CSV file",
                "Deletes a CSV file",
                "Loads a CSV file into a pandas DataFrame",
                "Prints the CSV to screen"
            ],
            "answer": 2,
            "explanation": "pd.read_csv() reads a CSV file and loads it into a pandas DataFrame for data analysis."
        },
        {
            "question": "What structure is best for storing a single transaction with multiple details?",
            "options": ["A list", "A dictionary", "A string", "A boolean"],
            "answer": 1,
            "explanation": "A dictionary with key-value pairs is perfect for structured data like a transaction record."
        },
        {
            "question": "What does 'df.groupby('Category')['Amount'].sum()' do?",
            "options": [
                "Deletes categories",
                "Calculates total amounts for each category",
                "Sorts by category",
                "Creates new categories"
            ],
            "answer": 1,
            "explanation": "This pandas operation groups data by category and calculates the sum of amounts in each group."
        },
        {
            "question": "Why is returning values from functions important?",
            "options": [
                "It's not important",
                "So functions can work together and pass data",
                "To make code slower",
                "To create errors"
            ],
            "answer": 1,
            "explanation": "Returning values allows functions to collaborate - one function's output becomes another's input."
        },
        {
            "question": "What is a key-value pair in a dictionary?",
            "options": [
                "Two separate lists",
                "A name (key) associated with a value",
                "Two functions",
                "A type of loop"
            ],
            "answer": 1,
            "explanation": "A key-value pair stores data as a label (key) linked to its associated information (value)."
        }
    ],
    "robust_apps": [
        {
            "question": "What is the purpose of the 'except' block?",
            "options": [
                "To run when the try block succeeds",
                "To run when an error occurs in the try block",
                "To define variables",
                "To create loops"
            ],
            "answer": 1,
            "explanation": "The except block provides a Plan B that executes when an error occurs in the try block."
        },
        {
            "question": "What does API stand for?",
            "options": [
                "Application Programming Interface",
                "Automated Python Integration",
                "Advanced Programming Instructions",
                "Application Process Indicator"
            ],
            "answer": 0,
            "explanation": "API stands for Application Programming Interface - a way for programs to communicate with external services."
        },
        {
            "question": "What library do you use to make API requests in Python?",
            "options": ["pandas", "datetime", "requests", "json"],
            "answer": 2,
            "explanation": "The requests library is used to make HTTP requests to APIs and fetch data."
        },
        {
            "question": "What format do APIs commonly use to send data?",
            "options": ["CSV", "JSON", "TXT", "PDF"],
            "answer": 1,
            "explanation": "JSON (JavaScript Object Notation) is the standard format for API data exchange."
        },
        {
            "question": "In OOP, what is a class?",
            "options": [
                "A type of loop",
                "A blueprint for creating objects",
                "An error handling tool",
                "A database"
            ],
            "answer": 1,
            "explanation": "A class is a template that defines the structure and behavior for creating objects."
        },
        {
            "question": "What is an instance in OOP?",
            "options": [
                "A type of error",
                "A specific object created from a class blueprint",
                "A database query",
                "A loop counter"
            ],
            "answer": 1,
            "explanation": "An instance is an individual object created from a class, like a specific transaction."
        },
        {
            "question": "What does the __init__ method do in a class?",
            "options": [
                "Deletes the object",
                "Initializes a new object with starting values",
                "Prints the object",
                "Loops through the object"
            ],
            "answer": 1,
            "explanation": "__init__ is the constructor that sets up a new object with its initial properties."
        },
        {
            "question": "What is the purpose of an assertion in testing?",
            "options": [
                "To slow down code",
                "To declare what must be true and verify it",
                "To create errors",
                "To format output"
            ],
            "answer": 1,
            "explanation": "Assertions state expected conditions and stop the program if those conditions aren't met."
        },
        {
            "question": "What does 'response.json()' do when working with APIs?",
            "options": [
                "Deletes the response",
                "Converts JSON text to a Python dictionary",
                "Sends data to the API",
                "Creates an error"
            ],
            "answer": 1,
            "explanation": "response.json() parses JSON data and converts it into Python objects (dictionaries/lists)."
        },
        {
            "question": "Why is error handling important in applications?",
            "options": [
                "It makes code longer",
                "It prevents crashes and provides user-friendly error messages",
                "It's not important",
                "It makes code run faster"
            ],
            "answer": 1,
            "explanation": "Error handling creates robust applications that gracefully handle unexpected situations."
        }
    ],
    "ai_first": [
        {
            "question": "What is 'vibe programming'?",
            "options": [
                "Writing code very fast",
                "Describing desired outcomes to AI in natural language",
                "Playing music while coding",
                "Memorizing syntax"
            ],
            "answer": 1,
            "explanation": "Vibe programming is about being a 'code director' who describes goals rather than typing every line."
        },
        {
            "question": "What is the most important skill when working with AI-generated code?",
            "options": [
                "Typing speed",
                "The ability to critique and evaluate the code",
                "Memorizing Python syntax",
                "Using complex algorithms"
            ],
            "answer": 1,
            "explanation": "Critical evaluation of AI output ensures quality and correctness - never blindly trust AI code."
        },
        {
            "question": "What makes an effective AI prompt?",
            "options": [
                "Being as brief as possible",
                "Providing context, specifics, and format preferences",
                "Using technical jargon",
                "Asking multiple questions at once"
            ],
            "answer": 1,
            "explanation": "Good prompts include context about your data, specific task requirements, and desired output format."
        },
        {
            "question": "What is the first step in the Six-Step Methodology?",
            "options": [
                "Write Python code",
                "Understand the problem",
                "Test the solution",
                "Use AI to generate code"
            ],
            "answer": 1,
            "explanation": "Understanding the problem by restating it in your own words is the crucial first step."
        },
        {
            "question": "What is the purpose of the Developer's Diary?",
            "options": [
                "To store passwords",
                "To document learning and AI collaboration process",
                "To write personal thoughts",
                "To plan vacations"
            ],
            "answer": 1,
            "explanation": "The Developer's Diary demonstrates learning through documented AI interactions and reflections."
        },
        {
            "question": "What should an AI Evidence Package include?",
            "options": [
                "Only the final code",
                "Artifact, context, and reflection",
                "Just a screenshot",
                "Only errors encountered"
            ],
            "answer": 1,
            "explanation": "Each package needs the artifact (screenshot), context (what you were doing), and reflection (what you learned)."
        },
        {
            "question": "Why is version control with GitHub important?",
            "options": [
                "It's just for professional developers",
                "It provides history, safety, and demonstrates progress",
                "It makes code run faster",
                "It's not important for students"
            ],
            "answer": 1,
            "explanation": "Version control tracks changes, provides backup, and shows consistent effort over time."
        },
        {
            "question": "What is pseudocode?",
            "options": [
                "Fake code that doesn't work",
                "A human-readable blueprint of logic before coding",
                "Code with syntax errors",
                "Comments in Python"
            ],
            "answer": 1,
            "explanation": "Pseudocode is a plain-language outline of your solution's logic, written before actual coding."
        },
        {
            "question": "In the AI-First mindset, what is your primary role?",
            "options": [
                "Typing code as fast as possible",
                "Strategic thinking and quality control",
                "Memorizing algorithms",
                "Avoiding AI tools"
            ],
            "answer": 1,
            "explanation": "Your value comes from problem-solving strategy and ensuring quality, not typing speed."
        },
        {
            "question": "What should you ask when critiquing AI-generated code?",
            "options": [
                "Is it the longest solution possible?",
                "Is it too complex? Do I understand it? Does it handle real data?",
                "Does it use advanced features?",
                "Is it exactly like the example?"
            ],
            "answer": 1,
            "explanation": "Critique should focus on simplicity, understanding, robustness, and business relevance."
        }
    ]
}


def display_welcome():
    """Display welcome message and instructions"""
    print("\n" + "="*70)
    print(" "*15 + "ISYS2001 FINAL REVIEW QUIZ")
    print(" "*15 + "Self-Assessment Tool")
    print("="*70)
    print("\nWelcome! This interactive quiz will help you assess your understanding")
    print("of the course material. You can retake it multiple times - each time")
    print("you'll get a different random selection of questions.\n")


def display_menu():
    """Display topic selection menu"""
    print("\n" + "-"*70)
    print("SELECT A TOPIC AREA:")
    print("-"*70)
    print("1. Fundamentals (Variables, Logic, Loops)")
    print("2. Structure & Data (Functions, Dictionaries, Pandas)")
    print("3. Robust Apps (Error Handling, APIs, OOP, Testing)")
    print("4. AI-First (Strategy, Collaboration, Professional Practices)")
    print("5. Mixed Review (Random questions from all topics)")
    print("6. Exit Quiz")
    print("-"*70)


def get_topic_choice():
    """Get valid topic choice from user"""
    while True:
        choice = input("\nEnter your choice (1-6): ").strip()
        if choice in ['1', '2', '3', '4', '5', '6']:
            return choice
        print("Invalid choice. Please enter a number between 1 and 6.")


def get_num_questions():
    """Get number of questions from user"""
    while True:
        try:
            num = input("\nHow many questions would you like? (1-10, default 5): ").strip()
            if num == "":
                return 5
            num = int(num)
            if 1 <= num <= 10:
                return num
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")


def select_questions(topic_key, num_questions):
    """Randomly select questions from the chosen topic"""
    if topic_key == "mixed":
        # Combine all questions from all topics
        all_questions = []
        for questions in QUESTION_BANK.values():
            all_questions.extend(questions)
        available = all_questions
    else:
        available = QUESTION_BANK[topic_key]

    # Ensure we don't ask for more questions than available
    num_to_select = min(num_questions, len(available))
    return random.sample(available, num_to_select)


def run_quiz(questions):
    """Run the quiz with selected questions"""
    score = 0
    results = []

    print("\n" + "="*70)
    print("QUIZ START")
    print("="*70)

    for i, q in enumerate(questions, 1):
        print(f"\n--- Question {i} of {len(questions)} ---")
        print(f"\n{q['question']}\n")

        for idx, option in enumerate(q['options']):
            print(f"  {idx + 1}. {option}")

        # Get user answer
        while True:
            try:
                user_input = input("\nYour answer (1-4): ").strip()
                user_answer = int(user_input) - 1
                if 0 <= user_answer <= 3:
                    break
                print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Please enter a valid number.")

        # Check answer
        correct = user_answer == q['answer']
        if correct:
            score += 1
            print("\n✓ Correct!")
        else:
            print(f"\n✗ Incorrect. The correct answer was: {q['options'][q['answer']]}")

        print(f"\nExplanation: {q['explanation']}")

        results.append({
            'question': q['question'],
            'correct': correct,
            'user_answer': q['options'][user_answer],
            'correct_answer': q['options'][q['answer']]
        })

        # Pause before next question
        if i < len(questions):
            input("\nPress Enter to continue to next question...")

    return score, results


def display_results(score, total, results):
    """Display final quiz results"""
    percentage = (score / total) * 100

    print("\n" + "="*70)
    print("QUIZ COMPLETE - RESULTS")
    print("="*70)
    print(f"\nYou scored: {score}/{total} ({percentage:.1f}%)\n")

    # Performance feedback
    if percentage >= 90:
        print("Excellent work! You have a strong grasp of this material.")
    elif percentage >= 70:
        print("Good job! You understand most concepts. Review the areas you missed.")
    elif percentage >= 50:
        print("Fair effort. Consider reviewing the material and retaking the quiz.")
    else:
        print("You may need more practice. Review the course materials carefully.")

    # Show summary of incorrect answers
    incorrect = [r for r in results if not r['correct']]
    if incorrect:
        print(f"\n--- Questions to Review ({len(incorrect)}) ---")
        for i, r in enumerate(incorrect, 1):
            print(f"\n{i}. {r['question']}")
            print(f"   Your answer: {r['user_answer']}")
            print(f"   Correct answer: {r['correct_answer']}")

    print("\n" + "="*70)


def main():
    """Main quiz application loop"""
    display_welcome()

    while True:
        display_menu()
        choice = get_topic_choice()

        if choice == '6':
            print("\nThank you for using the ISYS2001 Quiz. Good luck with your studies!")
            sys.exit(0)

        # Map choice to topic
        topic_map = {
            '1': ('fundamentals', 'Fundamentals'),
            '2': ('structure_data', 'Structure & Data'),
            '3': ('robust_apps', 'Robust Apps'),
            '4': ('ai_first', 'AI-First'),
            '5': ('mixed', 'Mixed Review')
        }

        topic_key, topic_name = topic_map[choice]

        # Get number of questions
        num_questions = get_num_questions()

        # Select and run quiz
        questions = select_questions(topic_key, num_questions)
        score, results = run_quiz(questions)

        # Display results
        display_results(score, len(questions), results)

        # Ask if user wants to continue
        print("\nWould you like to:")
        print("1. Take another quiz")
        print("2. Exit")

        while True:
            continue_choice = input("\nEnter your choice (1-2): ").strip()
            if continue_choice in ['1', '2']:
                break
            print("Please enter 1 or 2.")

        if continue_choice == '2':
            print("\nThank you for using the ISYS2001 Quiz. Good luck with your studies!")
            break


if __name__ == "__main__":
    main()
