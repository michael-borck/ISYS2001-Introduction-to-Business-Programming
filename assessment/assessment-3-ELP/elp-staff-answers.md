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


# Final Exam: Python and Data Analysis  
**Staff Answers and Marking Guide**

---

**Question 1: Functions and Control Structures** *(15 marks)*  
Write a Python function that takes the current wind speed and returns a description of the wind condition.

**Answer:**
```python
def wind_condition(speed):
    if speed < 5:
        return "Calm"
    elif 5 <= speed <= 20:
        return "Moderate"
    else:
        return "Strong"
```

**Marking Guide:**
- **Function Definition (3 marks)**: Correctly defines a function.
- **Conditional Logic (8 marks)**: Proper use of if-elif-else structure, covering all cases.
- **Correctness (2 marks)**: The function returns correct output for given inputs.
- **Code Clarity (2 marks)**: Clear and readable code.

---

**Question 2: Data Visualisation with Matplotlib** *(15 marks)*  
Create a bar plot showing daily precipitation levels and a pie chart showing precipitation proportions.

**Answer:**
```python
import matplotlib.pyplot as plt

# Example data
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
precipitation = [0, 2.5, 5.0, 7.5, 0]

# Bar Plot
plt.figure(figsize=(10, 5))
plt.bar(days, precipitation, color='blue')
plt.xlabel('Day')
plt.ylabel('Precipitation (mm)')
plt.title('Daily Precipitation Levels')
plt.show()

# Pie Chart
no_rain = len([p for p in precipitation if p == 0])
light_rain = len([p for p in precipitation if 0 < p < 5])
heavy_rain = len([p for p in precipitation if p >= 5])

labels = ['No Rain', 'Light Rain', 'Heavy Rain']
sizes = [no_rain, light_rain, heavy_rain]

plt.figure(figsize=(7, 7))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Proportion of Precipitation Levels')
plt.show()
```

**Marking Guide:**
- **Bar Plot (7 marks)**: 
  - Correct plot generated (4 marks).
  - Correct labeling of axes and title (3 marks).
- **Pie Chart (6 marks)**:
  - Proper categorisation and proportions (3 marks).
  - Correct chart and labeling (3 marks).
- **Description of Trends (2 marks)**: Correctly describes patterns in precipitation data.

---

**Question 3: File Handling and Data Analysis with Pandas** *(20 marks)*  
Load a CSV file, calculate max temperature, and create a new column for windiness.

**Answer:**
```python
import pandas as pd

# Load data
df = pd.read_csv('weather_data.csv')

# Display last five rows
print(df.tail())

# Calculate max temperature
max_temp = df['Temperature'].max()
print(f'Maximum Temperature: {max_temp}°C')

# Create new column categorising "Windy" and "Not Windy"
df['Windy'] = df['Wind Speed'].apply(lambda x: 'Windy' if x > 30 else 'Not Windy')

# Display updated DataFrame
print(df.head())
```

**Marking Guide:**

- **File Loading (4 marks)**: Correct use of `pd.read_csv()` and `.tail()` (2 marks), file path and dataset structure (2 marks).
- **Max Calculation (6 marks)**: Proper calculation of maximum temperature using `.max()` (3 marks) and correct output (3 marks).
- **New Column Creation (10 marks)**: 
  - Correct use of `.apply()` function to categorise days (5 marks).
  - Correct output display with the new column (5 marks).

---

**Question 4: Loops and Exception Handling** *(20 marks)*  
Monitor temperature and raise an exception if it falls below 0°C.

**Answer:**
```python
import random

def monitor_temperature():
    for hour in range(12):
        temp = random.uniform(-5, 10)  # Simulating temperature
        print(f'Hour {hour}: Temperature = {temp}°C')
        if temp < 0:
            raise Exception(f"Alert! Temperature below freesing: {temp}°C")
    print("Monitoring completed.")

try:
    monitor_temperature()
except Exception as e:
    print(e)
```

**Marking Guide:**

- **Loop Structure (8 marks)**: Proper use of loops to monitor for 12 hours (5 marks), correct output display (3 marks).
- **Exception Handling (8 marks)**: Proper implementation of `try-except` block (5 marks), correct raising and handling of the exception (3 marks).
- **Reflection (4 marks)**: Clear explanation of handling exception scenarios.

---

**Question 5: Lists and Dictionaries** *(30 marks)*  
Track precipitation data for 4 cities and calculate total precipitation.

**Answer:**
```python
weather_data = {
    'City A': [2.0, 0, 5.0, 3.5],
    'City B': [1.0, 2.5, 0, 4.0],
    'City C': [3.0, 2.0, 1.5, 0],
    'City D': [0, 0, 1.0, 3.0]
}

# Display data for a specific city
city = 'City B'
print(f"Weather data for {city}: {weather_data[city]}")

# Calculate total precipitation for all cities
total_precipitation = sum([sum(weather_data[city]) for city in weather_data])
print(f"Total precipitation for all cities: {total_precipitation} mm")
```

**Marking Guide:**

- **Dictionary and List Creation (8 marks)**: 
  - Correct dictionary structure (4 marks).
  - Proper list usage for storing precipitation (4 marks).
- **Data Display (8 marks)**: 
  - Correct retrieval and display of data for a specific city (5 marks).
  - Accurate output display (3 marks).
- **Total Precipitation Calculation (10 marks)**: 
  - Correct loop and summation (7 marks).
  - Correct output of total precipitation (3 marks).
- **Code Clarity and Comments (4 marks)**: Clear and well-commented code.

---

**Question 6: Problem-Solving with Development Methodology** *(30 marks)*  
Calculate the heat index using a specific formula. Apply the first four steps of the development methodology.

**Step 1: Understand the Problem (5 marks)**  
In your own words: The heat index measures how hot it feels to the human body by considering temperature and humidity. We will use a formula with constants to calculate this based on given inputs.

**Step 2: Identify Inputs/Outputs (5 marks)**  

- **Inputs:** Temperature (T in degrees Celsius), Humidity (H in %).  
- **Outputs:** Heat Index (HI in degrees Celsius).

**Step 3: Work the Problem by Hand (10 marks)**  

For T = 30°C and H = 70%:  
\[
HI = -8.78469475556 + (1.61139411 \times 30) + (2.33854883889 \times 70) + (-0.14611605 \times 30 \times 70)
\]
\[
HI = -8.78469475556 + 48.3418233 + 163.6984187223 - 306.44535
\]
\[
HI = 34.81 \,°C
\]

**Step 4: Develop the Pseudocode (10 marks)**  

```
Pseudocode:
1. Start
2. Input temperature (T) and humidity (H)
3. Calculate HI using the given formula:
    HI = c1 + c2*T + c3*H + c4*T*H
4. Output the value of HI
5. End
```

**Marking Guide:**

- **Understanding (5 marks):** Clear understanding of the problem.
- **Inputs/Outputs (5 marks):** Correct identification of inputs and outputs.
- **Manual Calculation (10 marks):** Correct calculation and steps (10 marks).
- **Pseudocode (10 marks):** Proper structure and clarity of the pseudocode.
