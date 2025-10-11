---
title: "STAFF ANSWER GUIDE: Activity 3: User Preferences with Simplified Methodology"
subtitle: "From Blueprint to Code: Building Your User Preferences Programme Step by Step"
author: "Michael Borck"
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

# Staff Answer Guide: Activity 3 – User Preferences with Simplified Methodology

## Overview

This guide provides a sample solution and detailed explanations for Activity 3. In this activity, students are guided through a structured problem-solving methodology to design and implement a User Preferences programme. Key steps include:

1. **State the Problem**
2. **Describe Input and Output**
3. **Work the Problem by Hand**
4. **Develop an Algorithm (Pseudocode)**
5. **Write the Code**
6. **Tackle Mini-Challenges**

In addition, students are encouraged to use AI tools to clarify their thought process and verify their work—while ensuring that all AI suggestions stay within the course scope (i.e., using only input(), print(), basic data types, and variables).



## Detailed Breakdown

### Step 1 – State the Problem

- **Student Task:**  
  Define the goal: build a programme that collects user preferences and displays them in a personalised summary.

- **Staff Explanation:**  
  Students should identify what information to gather (e.g., name, favourite colour, favourite food, and hobby) and decide how to present it. 

- **AI Usage Tip:**  
  Encourage students to ask an AI tool to rephrase their description. For example:  
  > "Can you restate my description of a user preferences programme to ensure I have captured the intent correctly?"  
  Remind them to verify that the AI’s response aligns with the topics covered so far.



### Step 2 – Describe Input and Output

- **Student Task:**  
  List the inputs (name, favourite colour, favourite food, favourite hobby) and define the expected output (e.g., a summary message).

- **Staff Explanation:**  
  Mapping the inputs to a clear output helps structure the programme. The expected output might be:  
  > "Hello, [name]! Your favourite colour is [colour], you love [food], and you enjoy [hobby]."

- **AI Usage Tip:**  
  Students can ask, "What are some creative ways to format a user preferences summary?" but must ensure the suggestions only use basic concepts.



### Step 3 – Work the Problem by Hand

- **Student Task:**  
  Use sample inputs (e.g., name = "Alice", favourite colour = "Blue", favourite food = "Pasta", favourite hobby = "Reading") to manually determine the expected output.

- **Staff Explanation:**  
  This step validates the student’s understanding. The manually written output should match what the code will generate.

- **AI Usage Tip:**  
  If unsure, students may ask, "Does this output message clearly reflect the provided inputs?" ensuring the feedback adheres to current learning.



### Step 4 – Develop an Algorithm (Pseudocode)

- **Student Task:**  
  Write pseudocode outlining the logical steps. An example might be:

  ```plain
  1. Start the programme.
  2. Prompt the user for their name and store the input.
  3. Prompt for favourite colour and store the input.
  4. Prompt for favourite food and store the input.
  5. Prompt for favourite hobby and store the input.
  6. Construct a summary message using the inputs.
  7. Print the summary message.
  8. End the programme.
  ```

- **Staff Explanation:**  
  Pseudocode helps bridge the planning phase with the coding phase. It doesn’t need to follow Python syntax.

- **AI Usage Tip:**  
  Students can ask an AI tool, "Can you review my pseudocode and suggest improvements?" Remind them to keep suggestions within the basics they have learned.



### Step 5 – Write the Code

- **Student Task:**  
  Translate the pseudocode into a Python script. A sample solution might be:

  ```python
  # Collect user input for various preferences
  name = input("What is your name? ")
  favourite_colour = input("What's your favourite colour? ")
  favourite_food = input("What's your favourite food? ")
  favourite_hobby = input("What's your favourite hobby? ")

  # Construct and display a personalised summary message
  print("\nHello, " + name + "!")
  print("Your favourite colour is " + favourite_colour + 
        ", you love " + favourite_food + 
        ", and you enjoy " + favourite_hobby + ".")
  ```

- **Staff Explanation:**  
  This code uses string concatenation and demonstrates the basic usage of input() and print() functions. Emphasize that this solution should not include advanced topics like functions, f-strings, or exception handling yet.

- **AI Usage Tip:**  
  In case of errors or confusion, students should ask follow-up questions like, "How can I improve this code using only input(), print(), and variables?" This ensures that AI feedback remains aligned with current topics.



### Mini-Challenges

The worksheet includes optional mini-challenges to encourage creative problem-solving:

1. **Starred Preferences:**  
   Print each preference on a separate line with a star at the beginning.

   ```python
   print("* Name:", name)
   print("* Favourite Colour:", favourite_colour)
   print("* Favourite Food:", favourite_food)
   print("* Favourite Hobby:", favourite_hobby)
   ```

2. **Age Calculator Challenge:**  
   Ask for the birth year, calculate the age, and print it.  
   *Note:* This may introduce the concept of basic arithmetic and importing modules, so students should verify with an AI tool if uncertain.
   
   ```python
   import datetime
   birth_year = int(input("What year were you born? "))
   current_year = datetime.datetime.now().year
   age = current_year - birth_year
   print("You are", age, "years old!")
   ```

3. **(Optional Advanced) F-String Formatting:**  
   Refactor the summary message using f-strings for cleaner syntax.  
   *Note:* This challenge is optional and should only be attempted if the student is comfortable with the material.
   
   ```python
   print(f"Hello, {name}! Your favourite colour is {favourite_colour}, you love {favourite_food}, and you enjoy {favourite_hobby}.")
   ```

- **Staff Explanation:**  
  These challenges reinforce the core concepts and gently introduce new ideas. Tutors should stress that students must use only what they've learned so far unless they explicitly choose to explore the advanced option.  

- **AI Usage Tip:**  
  Remind students to ask, "Can you explain how to complete this mini-challenge using only the topics we've covered?" if they receive suggestions that include more advanced content.



## Testing and Reflection

- **Testing:**  
  Students should test their programmes with various input scenarios. For example, when inputting "Alice" for the name, "blue" for the favourite colour, and so on, the output should match the expected result.

- **Reflection Questions:**  
  - How did planning (pseudocode) assist in coding the solution?
  - Which mini-challenge did you find most useful or interesting?
  - How did using AI tools enhance your understanding?  
    (Encourage them to verify and ask follow-up questions if any AI response uses concepts beyond input(), print(), and basic variables.)

- **Staff Explanation:**  
  Discuss the importance of systematic planning and how AI tools can be used to clarify and refine ideas—provided the student critically evaluates the output against what they’ve learned.



## Tutor Tips

- **Planning Emphasis:**  
  Encourage students to invest time in planning and pseudocoding before coding.

- **Comparative Discussion:**  
  Ask students to share both their pseudocode and final solutions. Compare the structured approach to earlier, less formal methods (like Activity 2).

- **Critical Evaluation of AI Outputs:**  
  Remind students that if any AI suggestion includes advanced topics (e.g., user-defined functions, exceptions, f-strings), they should ask follow-up questions to have the explanation tailored to the current level of learning.

- **Encourage Experimentation:**  
  Support creative extensions and mini-challenges as long as the core solution remains aligned with the course content.



## Conclusion

This staff guide is designed to help tutors support students through Activity 3. The guide includes a sample pseudocode, a basic Python solution, and mini-challenges—all supplemented with AI usage tips. These tips aim to encourage students to ask follow-up questions and critically evaluate AI outputs, ensuring that their solutions use only the concepts taught so far.

Happy tutoring!
