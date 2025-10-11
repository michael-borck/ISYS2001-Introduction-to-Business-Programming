---
title: "Weather Wizards: Crafting Interactive Dashboards"
subtitle: "Transform real-time weather data into captivating visuals with your programming magic"
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

#### **Assignment Overview**

In this assignment, you will create a Python-based weather dashboard using
Google Colab, integrating data from the OpenWeatherMap API. The dashboard will
feature weather data visualisations and will be developed using a
procedural/function-based approach. This project allows you to demonstrate the
skills and concepts covered in the unit, including data handling, API usage,
data visualisation, basic programming constructs, and good coding practices.

#### **Assignment Objectives**

- Apply Python programming concepts to create a functional weather dashboard.
- Utilise the OpenWeatherMap API to retrieve and display weather data.
- Develop visualisations using matplotlib or seaborn.
- Demonstrate effective use of AI tools (e.g., GitHub Copilot, ChatGPT) to aid
  coding, and document your interactions with these tools.
- Use version control effectively, making regular commits to a private GitHub
  repository, demonstrating a structured and iterative development process.
- Present your final work in a professional, well-documented Jupyter Notebook,
  including reflections on AI tool usage.

#### **Task Requirements**

1. **Data Collection and API Usage**:
   - Use the OpenWeatherMap API to fetch weather data for a location of your
     choice.
   - Implement basic error handling for API calls, such as handling invalid
     responses.
   - Securely manage your API key (instructions for obtaining an API key will be
     provided separately).

2. **Data Processing**:
   - Extract and process at least 2 weather parameters (e.g., temperature,
     humidity).
   - Use pandas for data manipulation if necessary.

3. **Dashboard Development**:
   - Create a weather dashboard using Google Colab.
   - Implement at least 1 type of visualisation using matplotlib or seaborn.
   - Include an interactive element (e.g., input field for city selection).

4. **Code Organisation and Documentation**:
   - Organise code into functions for data fetching, processing, and visualisation.
   - Provide comments and docstrings for your functions to explain their purpose
     and usage.
   - Use comments to explain complex logic and AI-assisted code sections.
   - Follow best coding practices for readability.

5. **AI Tools Usage**:
   - Use AI coding tools like GitHub Copilot or ChatGPT to assist in your
     development.
   - Briefly document your use of these tools in code comments and in a
     reflection section.

6. **Version Control and Development Process**:
   - Use version control by making regular commits to your GitHub repository
     after significant changes.
   - **Create a private GitHub repository** for your project.
   - **Invite your tutor to your private repository** to grant access for
     assessment. Failure to send an invite will result in a significant loss of
     marks because we cannot see the change and commit history.
   - Make at least **5 meaningful commits**, demonstrating the evolution of your
     project.
   - Use clear and descriptive commit messages that reflect the specific changes
     made.

7. **Professional Report**:
   - Structure your final notebook as a professional report, including:
     - **Introduction**: Project purpose and scope.
     - **Methods**: Description of data collection and processing steps.
     - **Results**: Visualisations and their interpretations.
     - **Discussion**: Reflection on the use of AI tools and any challenges faced.
     - **Conclusion**: Summary of what was achieved.
   - Include a brief discussion on data ethics and privacy considerations
     related to weather data usage.

#### **Required Libraries**

- `requests` (for API calls)
- `pandas` (for data manipulation)
- `matplotlib` or `seaborn` (for visualisation)

#### **Assessment Criteria**

Your project will be assessed based on:

- **Correct Application of Techniques (40%)**: Proper use of Python constructs,
  data handling, basic error checking, and visualisation techniques.
- **Code Quality and Documentation (15%)**: Good code quality, including
  comments, docstrings, adherence to coding standards, and code organisation.
- **Quality of Visualisations (15%)**: Clarity, relevance, and correctness of
  the visual representations.
- **Effective Use of AI (10%)**: Documented and ethical use of AI tools to
  enhance your coding process.
- **Effective Use of Version Control (10%)**: Demonstrated use of version
  control with regular commits and clear commit messages.
- **Overall Presentation (10%)**: Professionalism, clarity, and completeness of
  the final notebook report.

#### **Grading Rubric**

| Grade Level          | Functionality                                                                                                                                               |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pass (50-64%)        | Basic text output of weather data; Minimal error handling; Basic API integration; Basic comments.                                                           |
| Credit (65-74%)      | One type of visualisation; Proper data processing; Clear code organisation; Some error handling; Comments and docstrings; Basic use of version control.     |
| Distinction (75-84%) | Interactive element (e.g., input field for city selection); Multiple visualisations; Good error handling; Detailed comments and docstrings; Regular commits. |
| High Distinction (85-100%) | Advanced features (e.g., additional data parameters); Exceptional code quality and documentation; Comprehensive error checking; Creative use of libraries; Regular, detailed commits with descriptive messages. |

#### **Suggested Timeline**

- **Week 1**:
  - Set up the OpenWeatherMap API and securely manage your API key.
  - Begin data retrieval for a chosen location.
  - Initialise your private GitHub repository and invite your tutor.
  - Make initial commits with setup code.

- **Week 2**:
  - Implement data processing to extract required weather parameters.
  - Start developing visualisations.
  - Continue making regular commits with descriptive messages.

- **Week 3**:
  - Add an interactive element to your dashboard.
  - Refine visualisations and ensure they are informative.
  - Document your use of AI tools.
  - Enhance code with comments and docstrings.

- **Week 4**:
  - Finalise your code and ensure it runs without errors.
  - Complete your professional report within the notebook.
  - Make final commits and review your GitHub repository for completeness.

#### **Submission Details**

- **Due Date**: Friday, 18th October 2024, 23:59.
- **Submission Format**:
  - Submit your final Google Colab notebook as a `.ipynb` file.
  - Provide a **link to your private GitHub repository** containing your
    commits.
  - **Ensure you have invited your tutor to your private repository** to grant
    access for assessment. Failure to send an invite will result in a
    significant loss of marks because we cannot see the change and commit
    history.

- **Late Submission**: Penalties apply as outlined in the unit handbook.

#### **Additional Notes**

- **API Key Security**: Ensure your API key is not shared publicly in your code
  or repository. Use secure methods to handle the API key, such as environment
  variables or input prompts.

- **Data Ethics**: Consider the ethical implications of data usage and discuss
  this in your report. Even though weather data is public, responsible use and
  acknowledgment of data sources are important.

- **Version Control Best Practices**:
  - **Private Repository**: Create a private repository to protect your work.
  - **Inviting Your Tutor**: Invite your tutor to your private repository for
    assessment purposes.
  - **Regular Commits**: Commit after significant changes or feature additions.
    This helps in tracking changes, debugging, and collaborating.

- **Commenting and Documentation**: Write clear and concise docstrings for your
  functions. Follow standard documentation conventions to explain the purpose,
  parameters, return values, and any side effects.

- **Error Handling**: Implement basic error handling to manage issues such as
  invalid API responses.

- **Professionalism**: Ensure your final notebook is well-organised, free of
  errors, and professionally presented.
