---
title: "STAFF ANSWER GUIDE: User Preferences Survey Project"
subtitle: "Applying Industry Best Practices in a Real-World Environment"
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

# Staff Answer Guide: User Preferences Survey Project

## Overview

This project collates several exercises from the week’s activities and requires students to build a simple User Preferences Survey using Python. The purpose is to practice fundamental concepts (variables, data types, input(), print(), and basic operations) while adhering to industry best practices. These best practices include using descriptive names, proper documentation, version control, and careful use of AI for guidance.

This guide provides sample answers and discussion points for tutors.



## Step 1 – State the Problem

**Expected Student Response:**  
Students should clearly articulate that the goal of the programme is to collect a user's preferences (such as name, favourite colour, favourite food, and favourite hobby) and then display a personalized summary message.

*Example Answer:*  
> "The programme is designed to ask the user for their name, favourite colour, favourite food, and favourite hobby. It will then use this data to generate a personalized greeting, such as 'Hello, Alice! Your favourite colour is blue, you love pizza, and you enjoy reading.'"

**Discussion Points:**  
- Verify that students have captured both the input data and the expected output.
- Emphasise that the problem statement must be clear and concise.

**AI Tip for Students:**  
Students are encouraged to ask an AI tool to rephrase their description. Tutors can suggest:  
> "Can you restate my description of a User Preferences Survey program using only input(), print(), and variables?"  
Ensure the AI’s response is in line with the basic concepts taught so far.



## Step 2 – Describe Input and Output

**Expected Student Response:**  
Students should list the inputs and clearly describe the expected output.

*Inputs:*  
- `user_name` (string)
- `fav_colour` (string)
- `fav_food` (string)
- `fav_hobby` (string)

*Expected Output:*  
A summary message formatted as:  
> "Hello, [user_name]! Your favourite colour is [fav_colour], you love [fav_food], and you enjoy [fav_hobby]."

**Discussion Points:**  
- Ensure that students understand the mapping between the inputs and the output.
- Discuss why a clear specification of inputs and outputs is important for planning.

**AI Tip for Students:**  
Ask an AI tool for creative formatting ideas, ensuring that suggestions remain within the basic techniques of input(), print(), and string concatenation.



## Step 3 – Work the Problem by Hand

**Expected Student Response:**  
Students should simulate the programme by writing sample inputs and manually determining the expected output.

*Sample Simulation:*  
- **Inputs:**  
  - `user_name`: "Alice"  
  - `fav_colour`: "blue"  
  - `fav_food`: "pizza"  
  - `fav_hobby`: "reading"
- **Expected Output:**  
  > "Hello, Alice! Your favourite colour is blue, you love pizza, and you enjoy reading."

**Discussion Points:**  
- Highlight that working the problem by hand helps to verify understanding before coding.
- Encourage students to try multiple scenarios.

**AI Tip for Students:**  
If uncertain, ask:  
> "Does this output message clearly reflect the provided inputs?"  
Review the AI feedback to ensure consistency.



## Step 4 – Develop an Algorithm (Pseudocode)

**Expected Student Response:**  
Students should produce pseudocode that outlines the logical steps of the programme. The pseudocode does not need to be written in Python syntax.

*Sample Pseudocode:*
```plain
1. Start the program.
2. Prompt the user for their name and store it in user_name.
3. Prompt the user for their favourite colour and store it in fav_colour.
4. Prompt the user for their favourite food and store it in fav_food.
5. Prompt the user for their favourite hobby and store it in fav_hobby.
6. Create a summary message using the stored inputs.
7. Print the summary message.
8. End the program.
```

**Discussion Points:**  
- Emphasize that pseudocode helps bridge planning and coding.
- Ask students to compare their pseudocode with a sample solution.

**AI Tip for Students:**  
Students can ask an AI tool:  
> "Can you review my pseudocode for a User Preferences Survey program and suggest improvements?"  
Ensure that the suggestions stay within the basic concepts taught.



## Step 5 – Write the Code

**Expected Student Response:**  
Students will translate their pseudocode into Python code using basic operations, input(), and print().

*Sample Python Code:*
```python
# Collect user input for preferences
user_name = input("What is your name? ")
fav_colour = input("What's your favourite colour? ")
fav_food = input("What's your favourite food? ")
fav_hobby = input("What's your favourite hobby? ")

# Construct the personalized summary message
summary = "Hello, " + user_name + "! Your favourite colour is " + fav_colour + \
          ", you love " + fav_food + ", and you enjoy " + fav_hobby + "."

# Display the summary message
print(summary)
```

**Discussion Points:**  
- Point out the importance of descriptive variable names.
- Discuss how comments and clear structure improve code readability.
- Verify that the solution uses only the concepts covered so far (no advanced topics).

**AI Tip for Students:**  
If any confusion arises, students can ask:  
> "Can you review my Python code for a User Preferences Survey and suggest improvements using only input(), print(), and basic variables?"  
This ensures that the solution remains aligned with course content.



## Reflection on Industry Best Practices

**Expected Reflection Points:**
- **Descriptive Names & Comments:**  
  How did using meaningful variable names and inline comments improve the clarity of the code?
- **Version Control:**  
  Emphasize the importance of frequent saves and using descriptive commit messages on GitHub.
- **Documentation:**  
  Reflect on how documenting the thought process in text cells helped understand and refine the solution.
- **Collation of Exercises:**  
  Note that this project collates several weekly activities. This approach is intentional and allows for reflection on whether students are improving in following industry best practices.

**Discussion Points:**  
- Discuss with students how this structured approach compares with more ad-hoc methods.
- Encourage them to critically evaluate any AI output they received and verify that it uses only the core topics covered so far.

**AI Tip for Students:**  
Ask an AI tool, "Can you suggest improvements to my project documentation and commit message examples based on industry best practices?" Ensure that any advice given adheres to the basic concepts learned.



## Final Reflection and Next Steps

**Expected Student Reflections:**
- How did following a structured methodology help in organizing the solution?
- Which aspects of industry best practices were most challenging to implement, and how can they be improved?
- How did the process of collating exercises help in understanding the overall project?

**Next Steps:**
- Experiment with adding new inputs or modifying the output format.
- Save your work frequently and use descriptive commit messages when uploading to GitHub.
- Share your completed project with peers and discuss possible improvements.

**Discussion Points for Tutors:**
- Encourage students to continue refining their code and documentation.
- Remind them that the best practices followed here are examples from the industry—useful habits to emulate as they grow in their careers.



## Tutor Tips

- **Encourage Reflection:**  
  Ask students to share what they learned about the importance of planning and documentation.
- **Emphasize Best Practices:**  
  Highlight the benefits of using descriptive names, version control, and proper commenting.
- **Foster Critical Use of AI:**  
  Remind students that AI is a tool to aid learning, but they should always verify that its suggestions are appropriate for their current level.



This staff answer guide is intended to provide a robust framework to support and evaluate student work on the User Preferences Survey Project. It emphasizes both the technical aspects and the industry best practices that are crucial for a successful software development career.

Happy tutoring!
