---
title: "STAFF-ANSWER-GUIDE Activity 2: Exploring Python Mini-Projects"
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


## Overview for Tutors

This guide will help you support students as they explore and modify the example mini-projects from the "Beyond the Basics" lecture. In this activity, students will run pre-written code examples, understand their functionality, and make modifications to learn about different Python application domains. This is a bridge activity between following structured tutorials and creating original code, so students will need guidance in understanding existing code and making meaningful changes.

## Learning Objectives Assessment

Students should demonstrate the following by the end of this activity:

1. Successfully run at least one example project from the provided code pack
2. Demonstrate understanding of the code's structure and functionality
3. Make meaningful modifications to existing code
4. Document their changes and reflect on what they've learned
5. Identify areas of interest for future learning

## Expected Submission from Students

✅ Modified code files  
✅ Screenshots showing their modifications in action  
✅ Written answers to the reflection questions  
✅ Documentation of challenges or errors encountered  

## Example Project Guidelines and Common Issues

### Data Science Example (Weather Analysis)

#### Expected Understanding

Students should grasp:
- How to load data from CSV files using pandas
- Basic data cleaning operations
- Creating simple visualisations with matplotlib
- Performing data aggregation and calculations

#### Likely Modification Attempts

1. **Changing chart types**: Line to bar, scatter, etc.
2. **Altering colors or visual elements**
3. **Adding new calculations**: Averages, min/max, etc.
4. **Filtering data** based on different criteria

#### Common Issues and Solutions

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| "FileNotFoundError" | Incorrect path to CSV file | Check relative path; ensure file is in expected location |
| Empty or unexpected plots | Data filtering removed all points | Check filter conditions; print data before plotting |
| Type errors in calculations | Mixed data types in columns | Add explicit conversion: `df['column'] = df['column'].astype(float)` |
| Plots not showing | Missing `plt.show()` or incorrect environment | Ensure `plt.show()` is called; use `%matplotlib inline` in notebooks |
| SettingWithCopyWarning | Modifying a slice of a DataFrame | Use `df.loc[]` for assignment or create explicit copy with `df.copy()` |

#### Extension Guidance

For students who grasp the basics quickly, suggest:
- Combining multiple visualisations into subplots
- Implementing interactive widgets (if using notebooks)
- Conducting more complex statistical analysis
- Creating annotated plots with important data points highlighted

### Web Development Example (Flask App)

#### Expected Understanding

Students should grasp:
- Basic Flask application structure
- Routes and view functions
- Templates and passing data to HTML
- Handling basic form input (if implemented)

#### Likely Modification Attempts

1. **Adding new routes/pages**
2. **Modifying HTML templates**
3. **Adding form inputs**
4. **Changing display logic**

#### Common Issues and Solutions

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| "ModuleNotFoundError" for Flask | Flask not installed | Run `pip install flask` |
| App runs but shows "Not Found" | Incorrect route definition | Check route decorator matches URL being accessed |
| Template not found | Incorrect template folder structure | Ensure templates are in a folder named "templates" |
| Changes not appearing | Browser caching | Hard refresh (Ctrl+F5 or Cmd+Shift+R) |
| Permission denied on port | Port already in use | Change port number in `app.run(port=8080)` |
| Variables not appearing in template | Incorrect variable names | Match template variables to those passed in `render_template()` |

#### Extension Guidance

For students who grasp the basics quickly, suggest:
- Adding persistent data storage (simple file-based or SQLite)
- Implementing more complex form handling with validation
- Adding basic user authentication
- Styling the site with CSS (if they have web experience)

### GUI Application Example (Weather App)

#### Expected Understanding

Students should grasp:
- Tkinter window and widget creation
- Event handling with callbacks
- Layout management (grid, pack, or place)
- Updating UI elements dynamically

#### Likely Modification Attempts

1. **Changing colors or fonts**
2. **Adding new buttons or inputs**
3. **Modifying the layout**
4. **Extending functionality** with new features

#### Common Issues and Solutions

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Window appears briefly then closes | Main loop not called or error in code | Ensure `root.mainloop()` is at the end; check for runtime errors |
| Widgets not appearing | Layout manager not called | Check for `.pack()`, `.grid()`, or `.place()` on all widgets |
| Buttons don't do anything | Callback function not connected properly | Verify command parameter: `command=function_name` (no parentheses) |
| Layout looks different than expected | Mixed layout managers | Stick to one layout manager per container |
| Text not updating | StringVar not used correctly | Ensure `textvariable=var` and update with `var.set()` |
| "TclError" | Invalid widget operations | Check widget state before operations; handle errors with try/except |

#### Extension Guidance

For students who grasp the basics quickly, suggest:
- Implementing multiple frames or screens
- Adding data validation for inputs
- Creating custom styled widgets
- Connecting the UI to external data sources

### Automation Example (File Organisation)

#### Expected Understanding

Students should grasp:
- File system operations with `os` and `shutil`
- Working with file paths and extensions
- Conditional logic for file categorisation
- Basic automation workflow

#### Likely Modification Attempts

1. **Adding new file categories**
2. **Implementing file renaming**
3. **Adding logging functionality**
4. **Modifying organisation criteria**

#### Common Issues and Solutions

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| "PermissionError" | Files in use or insufficient permissions | Close open files; run with appropriate permissions |
| No files moved | Incorrect path or no matching files | Verify directory path; print files found before processing |
| Files moved to wrong location | Logic error in categorisation | Review conditional statements; print category before moving |
| Script runs but nothing happens | Silent failures | Add more print statements; implement error handling |
| Files unexpectedly overwritten | Destination file already exists | Add checks with `os.path.exists()` and handle duplicates |

#### Extension Guidance

For students who grasp the basics quickly, suggest:
- Implementing a scheduled task (basic cron-like functionality)
- Adding a simple configuration file to customise behavior
- Creating a basic undo functionality
- Building a log analyser to summarise operations

### Game Development Example (Pygame)

#### Expected Understanding

Students should grasp:
- Pygame initialisation and basic setup
- Game loop structure
- Drawing graphics to the screen
- Handling user input
- Basic collision detection

#### Likely Modification Attempts

1. **Changing colors or object sises**
2. **Adjusting game speed**
3. **Adding new game elements**
4. **Modifying game mechanics**

#### Common Issues and Solutions

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| "ModuleNotFoundError" for pygame | Pygame not installed | Run `pip install pygame` |
| Black window with no elements | Drawing code issue or timing problem | Check draw calls; verify screen update is called |
| Game runs too fast/slow | Frame rate not controlled | Use `clock.tick(FPS)` to regulate speed |
| Input not recognised | Event handling incomplete | Ensure all events processed with `for event in pygame.event.get()` |
| Objects don't move | Position not updated | Verify position variables change; check for logic errors |
| Collision not detected | Collision logic error | Print object positions; check collision detection math |

#### Extension Guidance

For students who grasp the basics quickly, suggest:
- Adding scoring and display elements
- Implementing game states (start, play, game over)
- Adding sound effects
- Creating multiple levels or difficulty settings

## Answering Reflection Questions: Guidance for Strong Responses

### 1. Which example(s) did you explore? Why did you choose these?

**Strong responses include:**
- Specific reasons related to interests or career goals
- Connections to prior programming experience
- Thoughtful consideration of which domains they wanted to learn more about
- Reflection on what seemed challenging or novel to them

**Encourage students to:** Explain not just what they chose, but their decision-making process and what they hoped to learn.

### 2. What modifications did you make to the code? Describe the before and after.

**Strong responses include:**
- Specific code changes with examples
- Clear explanation of how the original functionality worked
- Detailed description of the modified behavior
- Discussion of any challenges in implementing changes
- Screenshots or examples showing the changes in action

**Encourage students to:** Use technical language precisely and demonstrate understanding of why their changes had the effect they did.

### 3. What was the most challenging part of understanding the example code?

**Strong responses include:**
- Identification of specific complex concepts
- Reflection on their own knowledge gaps
- Description of their process for overcoming challenges
- Insights gained from working through difficulties

**Encourage students to:** Be specific about what confused them and how they resolved their confusion, not just stating that something was "hard."

### 4. What new Python features, libraries, or concepts did you learn from these examples?

**Strong responses include:**
- Specific language features, methods, or functions
- New libraries or modules they hadn't encountered before
- Concepts or patterns used in the code
- Comparisons to what they already knew

**Encourage students to:** Go beyond just naming libraries to discussing specific functions, methods, or patterns they learned.

### 5. Which area of Python programming most interests you for future learning? Why?

**Strong responses include:**
- Thoughtful reflection on their interests and strengths
- Connections to potential projects or applications
- Specific aspects of the area that appeal to them
- Consideration of learning resources or next steps

**Encourage students to:** Think about both what interests them and what would be valuable for their goals, not just what seemed easiest.

### 6. How could you apply what you learned to create a project of your own?

**Strong responses include:**
- Specific project ideas that build on the examples
- Realistic assessment of what they could implement now
- Identification of skills they would need to develop further
- Connections between multiple concepts or examples

**Encourage students to:** Be creative but realistic in their ideas, focusing on projects that would consolidate their learning.

## Common Conceptual Challenges and Teaching Strategies

### Challenge: Understanding Code Structure in Larger Programs

Many students are used to writing small programs and struggle to understand the organisation of larger codebases.

**Teaching strategies:**
- Encourage students to trace the execution flow on paper
- Suggest adding print statements to track program flow
- Help them identify the "entry point" and follow execution from there
- Demonstrate how to break down large functions into logical components

### Challenge: Making Meaningful vs. Superficial Changes

Students often default to changing colors or text rather than functional aspects.

**Teaching strategies:**
- Provide specific suggestions for more substantial changes
- Ask questions about how specific features work to guide deeper understanding
- Challenge students to extend functionality in specific ways
- Validate simple changes as a starting point, but push for more

### Challenge: Understanding Library Documentation

Many students struggle to find information in documentation for new libraries.

**Teaching strategies:**
- Demonstrate how to search for specific functions in documentation
- Show examples of reading function signatures to understand parameters
- Point out patterns common to many libraries (e.g., initialisation, cleanup)
- Encourage experimentation in the REPL or notebook to test assumptions

### Challenge: Connecting Theory to Implementation

Students sometimes understand concepts in theory but struggle to identify them in code.

**Teaching strategies:**
- Explicitly point out where theoretical concepts appear in the code
- Ask students to identify specific patterns or concepts in the examples
- Draw diagrams to connect abstract concepts to concrete implementation
- Use analogies that relate programming concepts to familiar ideas

## Differentiated Support Strategies

### For Struggling Students

1. **Simplify the task**: Suggest more straightforward modifications
2. **Provide scaffolding**: Give partially completed code for changes
3. **Break it down**: Divide modifications into smaller steps
4. **Pair programming**: Partner with another student or tutor
5. **Visual aids**: Draw diagrams of code structure and flow

### For Advanced Students

1. **Challenge extensions**: Suggest more complex modifications
2. **Integration projects**: Combine elements from multiple examples
3. **Research assignments**: Encourage deeper exploration of libraries
4. **Optimisation tasks**: Improve efficiency or organisation of code
5. **Mentoring opportunities**: Have them help explain concepts to peers

## Assessment Guidance

### Exemplary Work Should Show:

- Multiple successful modifications that change program functionality
- Evidence of deep code comprehension in explanations
- Creative extensions beyond suggested modifications
- Thoughtful reflection showing connections to programming concepts
- Clean, well-documented code with appropriate comments

### Satisfactory Work Should Show:

- At least one working modification per example
- Basic understanding of code structure and function
- Reasonable attempts at all reflection questions
- Evidence of problem-solving when faced with challenges
- Functional code that runs without significant errors

### Needs Improvement If:

- Unable to make working modifications
- Superficial understanding of code demonstrated in reflections
- Minimal effort in answering reflection questions
- No evidence of troubleshooting or problem-solving
- Submitted code has significant errors or doesn't run

## Tips for Specific Teaching Scenarios

### Remote/Online Sessions

- Have students share screens when troubleshooting
- Create breakout rooms for different project types
- Use collaborative coding tools if available
- Prepare screen recordings of common modifications as references
- Establish a chat/forum for asynchronous help

### Large Group Sessions

- Prepare handouts with common modifications for each project
- Group students by project choice for peer support
- Create a "help queue" system for efficient assistance
- Have example solutions ready to show intermediate steps
- Use "pair programming" approach to share knowledge

### Mixed-Ability Groups

- Create tiered modification suggestions (basic, intermediate, advanced)
- Establish "expert tables" where advanced students can support others
- Provide extended time for students who need it
- Prepare additional examples for students who finish early
- Design reflection questions that allow for different levels of insight

## Additional Resources for Tutors

### Data Science
- Common pandas operations cheat sheet
- Matplotlib gallery examples
- Data cleaning best practices

### Web Development
- Flask quick reference
- HTML/CSS basics refresher
- Common web application patterns

### GUI Applications
- Tkinter widget reference
- Layout manager comparison
- Event handling patterns

### Automation
- File system operations reference
- Error handling best practices
- Logging implementation examples

### Game Development
- Pygame function reference
- Game loop explanation
- Sprite and collision handling examples

## Final Notes for Tutors

- **Process over product**: This activity is about exploration and understanding, not creating perfect code
- **Encourage experimentation**: Validate attempts even if they don't work perfectly
- **Focus on transferable concepts**: Help students see how techniques apply across domains
- **Build confidence**: This is often students' first time modifying substantial existing code
- **Connect to next activity**: Highlight how these skills will help with building the Snake game

Remember that the goal is to bridge the gap between following tutorials and creating original code. Celebrate small wins and create a supportive environment for experimentation.
