
## Pre-Lab Modules

1. **Reviewing Basic Python Tools**  
   - **Objective:** Refresh the fundamentals: using `print()`, `input()`, and working with variables.  
   - **Content:**  
     - Quick refresher video or reading on Python syntax.  
     - Interactive notebook examples that illustrate assigning and printing variables.  
     - Mini-exercises: Write simple programs to display messages and capture user input.

2. **Introduction to Decision Making**  
   - **Objective:** Introduce if-else statements and logical operators.  
   - **Content:**  
     - Explanation of how conditionals work (e.g., “if”, “else”).  
     - Diagrams showing the flow of decisions.  
     - Example code snippets that compare values and print different outputs.

3. **Exploring the Weather Context**  
   - **Objective:** Connect programming logic to real-world weather scenarios.  
   - **Content:**  
     - Overview of common weather conditions (cold, warm, rainy, etc.) and simple metrics (temperature thresholds).  
     - Discussion on how a program might “decide” a weather message based on a number (temperature) provided by the user.

4. **Designing a Simple Menu**  
   - **Objective:** Learn how to build a text-based menu interface using basic output and input.  
   - **Content:**  
     - Steps to display a menu with numbered options using `print()`.  
     - How to prompt the user for a choice and capture that choice with `input()`.  
     - Practice exercises: Create a menu that lets a user choose between two simple messages.

---

## In-Lab Activities

1. **Activity 1: Crafting the Weather Menu**  
   - **Task:** Create a menu that presents options like:  
     1. Check Temperature  
     2. Check Humidity  
     3. Check Wind Speed  
     4. Exit  
   - **Focus:** Use `print()` to display the menu and `input()` to capture the user’s selection.  
   - **Discussion:** Explain how each option might trigger a different response in the code.

2. **Activity 2: Writing Weather Decision Logic**  
   - **Task:** Based on the menu selection, write code using if-else statements to provide a weather forecast.  
     - For example, if the user selects “Check Temperature,” prompt them to enter the current temperature, then use conditionals to output messages like “It’s cold – wear a jacket” or “It’s warm – enjoy the day!”  
   - **Focus:** Practice writing nested if-else statements and understanding logical comparisons.  
   - **Guidance:** Encourage students to trace through their code with sample inputs.

3. **Activity 3: Testing and Refining the Weather Forecaster**
    - **Task:** Test the weather forecaster with different inputs to see how the program responds.  
    - **Focus:** Debugging and refining the code based on the output.  
    - **Discussion:** Discuss how to handle unexpected inputs and improve the user experience.
  - **Focus:** Debugging and refining the code based on the output.
  - **Guidance:** Encourage students to experiment with various inputs to see how the program reacts. Discuss how to handle edge cases and improve the user experience.
---

## Weekly Project: "Simple Weather Forecaster"

**Project Description:**  
Students will create a basic weather forecasting script that:
- **Displays a Menu:**  
  Presents options such as:  
  1. Check Temperature  
  2. Check Humidity  
  3. Check Wind Speed  
  4. Exit

- **Handles User Input:**  
  Based on the selected option, the script will ask for a related input. For example, if “Check Temperature” is selected, the program prompts the user to input the current temperature.

- **Implements Decision Logic:**  
  Uses if-else statements to analyze the input. For instance:  
  - If temperature is below a certain threshold, print “It’s cold – expect a chilly day.”  
  - If temperature is moderate, print “It’s a pleasant day.”  
  - (Similar simple logic can be applied for humidity and wind speed.)

- **Integration and Reflection:**  
  Emphasize that the focus is on understanding how conditionals make decisions.  
  Explain that next week the code will be refactored to use functions, but for now, all logic is written directly in the main block.

**Project Requirements:**
- Must use only `print()`, `input()`, variables, and basic data types.  
- Encourage creativity in designing simple weather messages.  
- Save the project in a Google Colab Notebook and push the final version to GitHub.

**Project Tips:**
- Remind students that clarity of logic is more important than complex features.
- Suggest that they use AI tools (e.g., ChatGPT) to get hints on improving readability, but they must write and understand the code themselves.
- Emphasize careful planning: drawing out the decision tree before coding can help organize the logic.

