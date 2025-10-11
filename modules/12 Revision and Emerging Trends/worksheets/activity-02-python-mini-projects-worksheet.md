---
title: "Activity 2: Exploring Python Mini-Projects"
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


## Introduction

Now that you have set up your local Python environment with Anaconda, it's time to explore some exciting applications of Python beyond the basics we've covered in class. In this activity, you'll download a pack of example code, run different mini-projects, and make modifications to see how Python can be used in various domains.

## Objectives
- Run pre-written Python projects in different domains
- Understand code structure and functionality in real applications
- Make modifications to existing code to customise its behavior
- Explore areas of Python that interest you for future learning

## Getting Started

### Step 1: Download the Example Code Pack

1. Download the example code pack from our course repository:
   - Navigate to: [course-website.edu/resources/python-examples](https://course-website.edu/resources/python-examples)
   - Click on "Download sIP" and save to your computer
   - Extract/unsip the file to a location you can easily find (e.g., Documents folder)

2. Open Anaconda Navigator and launch Jupyter Notebook

3. In Jupyter, navigate to the folder where you extracted the example code pack

### Step 2: Review the Available Examples

The example code pack contains mini-projects in five different domains. Each folder contains a complete working example with detailed comments:

1. **Data Science**: Weather data analysis and visualisation
2. **Web Development**: Simple Flask website
3. **GUI Application**: Interactive desktop application
4. **Automation**: File organisation script
5. **Game Development**: Basic Pygame example

## Part 1: Choose Your First Project

Select at least ONE example that interests you the most (though feel free to explore more if time permits). Follow the specific instructions for your chosen example:

### Option A: Data Science Example

**File**: `data_science/weather_analysis.py`

This example demonstrates how to analyse weather data using pandas and create visualisations with matplotlib.

1. Open the file in Jupyter Notebook or your preferred Python editor

2. Review the code and comments to understand:
   - How data is loaded from a CSV file
   - How pandas is used to clean and analyse the data
   - How matplotlib creates different types of visualisations

3. Run the code to see the analysis and visualisations

4. Modification Tasks:
   - Change the chart type for one of the visualisations (e.g., from line to bar)
   - Add a new calculation (e.g., calculate the temperature range for each month)
   - Customise the appearance of one chart (colors, title, labels)

### Option B: Web Development Example

**File**: `web_dev/flask_app.py`

This example shows how to create a simple website using the Flask framework.

1. Open a terminal/command prompt:
   - Windows: Search for "Anaconda Prompt" in the Start menu
   - Mac/Linux: Open Terminal

2. Navigate to the web_dev directory:
   ```
   cd path/to/example_code_pack/web_dev
   ```

3. Install Flask if you haven't already:
   ```
   pip install flask
   ```

4. Run the Flask application:
   ```
   python flask_app.py
   ```

5. Open your web browser and navigate to: http://127.0.0.1:5000/

6. Review the code to understand:
   - How routes map to different web pages
   - How templates are used for HTML
   - How data is passed between Python and the web pages

7. Modification Tasks:
   - Add a new route and page (e.g., `/about`)
   - Modify the HTML template to change the appearance
   - Add a form that collects user input

### Option C: GUI Application Example

**File**: `gui/weather_app.py`

This example demonstrates a desktop application with a graphical user interface using Tkinter.

1. Open the file in your Python editor

2. Run the application:
   ```
   python weather_app.py
   ```

3. Review the code to understand:
   - How the GUI is structured with frames, labels, and buttons
   - How user input is processed
   - How the application responds to user actions

4. Modification Tasks:
   - Change the colors or font styles
   - Add a new button with a new function
   - Modify the layout of the elements

### Option D: Automation Example

**File**: `automation/organise_files.py`

This example shows how to automate file organisation using Python.

1. Open the file in your Python editor

2. Create a test directory with some sample files (or use the provided test files)

3. Review the code to understand:
   - How the script identifies different file types
   - How files are moved to appropriate folders
   - How the process is automated

4. Run the script on your test directory:
   ```
   python organise_files.py /path/to/test/directory
   ```

5. Modification Tasks:
   - Add a new category of files to organise
   - Modify the script to also rename files based on certain criteria
   - Add logging to record what files were moved

### Option E: Game Development Example

**File**: `games/pygame_example.py`

This example demonstrates basic game development with Pygame.

1. Install Pygame if you haven't already:
   ```
   pip install pygame
   ```

2. Run the game:
   ```
   python pygame_example.py
   ```

3. Play the game to understand its mechanics

4. Review the code to understand:
   - How the game loop works
   - How graphics are drawn to the screen
   - How user input is handled
   - How game physics and collision detection work

5. Modification Tasks:
   - Change the colors or sises of game elements
   - Adjust the speed or behavior of moving objects
   - Add a new game feature (e.g., sound effects, a new type of object)

## Part 2: Deeper Exploration and Modifications

After you've run your chosen example(s) and made basic modifications, select ONE of your examples for deeper exploration:

1. Review the code more carefully, making sure you understand:
   - The overall structure and flow
   - How different functions interact
   - How libraries and modules are used
   - Any advanced Python features being used

2. Complete at least TWO of the following advanced modifications:

   **For Data Science:**
   - Add a new type of analysis or calculation
   - Import a different dataset and adapt the code to work with it
   - Create a new type of visualisation not used in the original code

   **For Web Development:**
   - Add multiple new pages with navigation between them
   - Implement data persistence (store data between sessions)
   - Add dynamic content that changes based on user input

   **For GUI Applications:**
   - Add multiple screens or a tab interface
   - Connect the GUI to an external data source
   - Add data validation and error handling

   **For Automation:**
   - Extend the script to handle multiple directories
   - Add options to customise the organisation rules
   - Create a log file that records all actions taken

   **For Game Development:**
   - Add a scoring system
   - Create different levels or difficulties
   - Add new game mechanics or obstacles

3. Document the changes you've made:
   - What did you change?
   - Why did you make these changes?
   - What challenges did you encounter?
   - How did you solve any problems that came up?

## Part 3: Reflection and Questions

After exploring and modifying the examples, answer the following questions:

1. Which example(s) did you explore? Why did you choose these?

2. What modifications did you make to the code? Describe the before and after.

3. What was the most challenging part of understanding the example code?

4. What new Python features, libraries, or concepts did you learn from these examples?

5. Which area of Python programming (from the examples) most interests you for future learning? Why?

6. How could you apply what you learned from these examples to create a project of your own?

## Submission Guidelines

To complete this activity, submit:

1. Your modified code files (or links to them)
2. Screenshots showing your modified examples running
3. Your answers to the reflection questions
4. Any error messages or challenges you couldn't resolve (if applicable)

## Troubleshooting Tips

- **Missing libraries**: If you encounter "ImportError" or "ModuleNotFoundError", install the required library using pip:
  ```
  pip install library_name
  ```

- **File not found errors**: Check that you're in the correct directory and using the right file path

- **Permission errors**: Some automation scripts may require additional permissions

- **Game doesn't run**: Make sure Pygame is installed correctly and that your display supports the required resolution

If you get stuck, remember:
1. Read error messages carefully
2. Check the comments in the code for hints
3. Search online for specific error messages
4. Ask for help from classmates or the instructor

## Next Steps

After completing this activity, you'll have a better understanding of different Python applications and how to modify existing code. In the next activity, we'll apply these skills to build a complete game from scratch!
