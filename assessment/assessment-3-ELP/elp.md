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

# Extended Learning Portfolio: Python and Data Analysis  

**Examination Instructions**  

- **Format:** Open-book exam. You may use textbooks, web content, and AI tools to complete the exam.  
- **Collaboration:** No collaboration allowed. For inquiries, contact the instructor directly.
- **GitHub Invites:**. PLease invite you tutor to you **private** GitHub repository.

  - Students from Monday's 11 AM class and Friday's 8 AM class, please invite to(Mandeep): isysprogram@gmail.com.
  - Students from Tuesday's 9 AM class and Friday's 10 AM class, please invite to(Suwe): suweslab.

- **Google Colab Notebooks:** All python code must run in the Google Colab
  Notebook environment.  You can use multiple notebooks or a single noteboook.
  Please make sure you save all notebooks to you github repository.
- **No Code Answers:** Please either include non code answers as a text cell
  within the notebook or as a separate document. PLease make sure you save or
  upload you non-code answers to your GitHub repository.  A copy of this
  repository is to be submitted.
- **Duration:** 48 hours. CAP adjustments will be applied accordingly.  
- **Questions:** Answer all questions. Each response should be submitted in a single Word document.  
- **Use of AI Tools:** Ethical use of AI tools is allowed. Provide copies or
  links to relevant AI conversations. Explain any AI-generated solutions that
  differ from the course material.  
- **Academic Integrity:** All work must be your own. Proper referencing in
  Chicago format is required.
- **Submission:** Please upload all relevant files to your Github repository.
  Then download the sip file of you repository, submit both the sip file and
  link to you private GitHub repository.


---

# **Question 1: Functions and Control Structures** *(15 marks)*  
Write a Python function that takes the current wind speed and returns a description of the wind condition as follows:  
- "Calm" if the wind speed is less than 5 km/h,  
- "Moderate" if the wind speed is between 5 and 20 km/h,  
- "Strong" if the wind speed is greater than 20 km/h.

- **Concepts Tested:** Function definition, conditional logic.  
- **What to Submit:** Python code and explanation of how functions help make your code reusable.

---

# **Question 2: Data Visualisation with Matplotlib** *(15 marks)*  
You are provided with a dataset containing daily precipitation levels for a month. Create the following visualisations using Matplotlib:  
- A bar plot showing daily precipitation levels.  
- A pie chart showing the proportion of days with "No rain" (precipitation = 0), "Light rain" (precipitation < 5 mm), and "Heavy rain" (precipitation ≥ 5 mm).  

- **Concepts Tested:** Data visualisation, Matplotlib, basic data analysis.  
- **What to Submit:** Python code, graphs, and a brief description of the weather patterns shown by the data.

---

# **Question 3: File Handling and Data Analysis with Pandas** *(20 marks)*  
Using Python’s Pandas library, load the file *seasonal_weather_data.csv* available on the unit's Blackboard site, containing weather data (temperature, humidity, and wind speed) for different days. Perform the following tasks:  
1. Display the last five rows of the dataset.  
2. Calculate the maximum temperature for the dataset.  
3. Create a new column that categorises each day as "Windy" if the wind speed is greater than 30 km/h and "Not Windy" otherwise.

- **Concepts Tested:** File handling, data manipulation with Pandas, working with DataFrames.  
- **What to Submit:** Python code and a screenshot of the dataset after adding the new column.

---

# **Question 4: Loops and Exception Handling** *(20 marks)*  
Write a Python program that monitors temperature readings every hour for 12 hours. If the temperature falls below 0°C, the program should raise an exception and stop further recordings.

- **Concepts Tested:** Loops, exception handling, program control flow.  
- **What to Submit:** Python code and a brief reflection on how you handled the exception scenario.

---

# **Question 5: Lists and Dictionaries** *(30 marks)*  
You are building a rainfall tracker that records precipitation levels for different cities. Create a Python program that stores precipitation data for 4 cities in a dictionary. Use a list to store the precipitation readings for each city. Then, implement the following:  
- Display the precipitation data for a specific city.  
- Calculate the total precipitation for all cities.

- **Concepts Tested:** Lists, dictionaries, data aggregation, iteration over collections.  
- **What to Submit:** Python code and output showing the results.

---

# **Question 6: Problem-Solving with Development Methodology** *(30 marks)*  
Using the first four steps of our six-step development methodology, solve the following problem:

**Problem:**  
Write a program that calculates the heat index (apparent temperature) based on the temperature and humidity using the formula:

\[
HI = c_1 + c_2T + c_3H + c_4TH
\]

Where:  
- **HI** = Heat Index (in degrees Celsius)  
- **T** = Temperature (in degrees Celsius)  
- **H** = Relative Humidity (percentage)

Constants:  
\[
c_1 = -8.78469475556,\ c_2 = 1.61139411,\ c_3 = 2.33854883889,\ c_4 = -0.14611605
\]

### Steps:
1. **Understand the Problem**: Rewrite the problem in your own words.
2. **Identify Inputs/Outputs**: Identify the necessary inputs and outputs for the problem.
3. **Work the Problem by Hand**: Perform a manual calculation of the heat index for a temperature of 30°C and relative humidity of 70%.
4. **Develop the Pseudocode**: Create pseudocode for solving this problem.

- **Concepts Tested:** Problem-solving, inputs/outputs, manual computation, pseudocode development.  
- **What to Submit:** Written answers for steps 1-4, including manual calculations and pseudocode.

---

### End of Exam  
Ensure all AI conversations used in your responses are included and referenced appropriately.

---