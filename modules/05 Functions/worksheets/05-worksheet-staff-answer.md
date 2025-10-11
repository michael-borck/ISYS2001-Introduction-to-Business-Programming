---
title: "STAFF ANSWER: Python Functions Worksheet"
subtitle: "Python Essentials"
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

This worksheet is designed to introduce students to Python functions within the
context of weather data analysis. It covers key concepts including function
definition, use of built-in functions, creation of custom functions, and
introduction to NumPy for more advanced data manipulation.

## Key learning objectives:

- Understanding and implementing Python functions
- Applying built-in Python functions to real-world data
- Creating custom functions for specific tasks
- Using NumPy for efficient data manipulation and analysis
- Critically thinking about how to use AI tools in the learning process

## Worksheet structure:

The worksheet is structured to progressively build skills:

- It starts with guidance on using AI tools responsibly, encouraging students to
  think critically and use AI as a learning aid rather than a solution provider.
- Basic function concepts are introduced, allowing students to explain functions
  in their own words and understand the syntax.
- Built-in functions are explored using weather data, introducing practical
  applications.
- Students then create custom weather-related functions, applying their
  understanding to solve specific problems.
- NumPy is introduced for more advanced data manipulation, showing how libraries
  can enhance data analysis capabilities.
- The conclusion and additional exercises encourage reflection and provide
  opportunities for further exploration.

## Expected outcomes:

- Students should be able to define and use functions in Python.
- They should understand how to manipulate lists using built-in functions.
- Students should be able to create custom functions for specific tasks related
  to weather data.
- They should have a basic understanding of NumPy and its capabilities for data
  analysis.
- Students should develop critical thinking skills about using AI in their
  learning process.

## Areas of Student Difficulty:

Potential areas for student difficulty:

- Understanding the concept of functions and their syntax
- Translating mathematical formulas into Python code (e.g., Celsius to
  Fahrenheit conversion)
- Grasping the more complex concepts in NumPy

Instructors should be prepared to provide additional explanation and examples
for these areas. Encouraging pair programming or group discussions can also help
students work through challenging concepts.

The optional exercises provide opportunities for more advanced students to
explore further or for assignment extensions. They introduce more complex
calculations (heat index) and additional libraries (pandas and matplotlib),
which can serve as a bridge to more advanced data analysis topics.

## 1. GenAI Exercise

Question 1: Think of a weather-related programming task you're unsure how to approach. Write a strategic question you could ask an AI assistant to help you learn without directly solving the problem for you.

Answer: A good strategic question could be: "What are the key steps and considerations I should keep in mind when designing a function to calculate the 'feels like' temperature based on actual temperature and wind speed? Can you explain the general approach without providing the actual code?"

## 2. Introduction to Functions

Question 2: Explain in your own words what a function is in Python and why we use them.

Answer: A function in Python is a reusable block of code that performs a specific task. We use functions to:
1. Organise code into manageable, logical units
2. Avoid repetition by allowing code reuse
3. Make programs more readable and easier to maintain
4. Break down complex problems into smaller, more manageable parts
5. Enable easier testing and debugging of individual components

Question 3: Write the general syntax for defining a function in Python. Use comments to explain each part.

Answer:
```python
def function_name(parameter1, parameter2):  # Function signature
    """
    Docstring: Briefly describe what the function does,
    its parameters, and what it returns.
    """
    # Function body: code that performs the task
    # ...
    
    return result  # Optional: return a value
```

## 3. Using Built-in Functions

Question 4: How would you calculate the number of days in the dataset using a built-in function?

Answer: 
```python
num_days = len(temperatures)
```

Question 5: Write a line of code to calculate the total temperature for the week.

Answer:
```python
total_temperature = sum(temperatures)
```

Question 6: Calculate the average humidity. (Hint: You'll need to use two built-in functions)

Answer:
```python
average_humidity = sum(humidity) / len(humidity)
```

## 4. Creating Weather-related Functions

Question 7: Write a function called `celsius_to_fahrenheit` that converts a temperature from Celsius to Fahrenheit.

Answer:
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
```

Question 8: Create a function named `average_temperature` that takes a list of temperatures and returns the average.

Answer:
```python
def average_temperature(temp_list):
    return sum(temp_list) / len(temp_list)
```

Question 9: Define a function called `weather_description` that takes temperature and humidity as parameters and returns a description based on the given criteria.

Answer:
```python
def weather_description(temperature, humidity):
    if temperature > 25 and humidity < 60:
        return "Hot and Dry"
    elif temperature > 25 and humidity >= 60:
        return "Hot and Humid"
    elif 15 <= temperature <= 25 and humidity < 60:
        return "Pleasant"
    elif 15 <= temperature <= 25 and humidity >= 60:
        return "Comfortable but Humid"
    else:
        return "Cool"
```

## 5. Using Third-party Libraries: NumPy

Question 10: Using NumPy, create an array called `temp_array` from the `temperatures` list.

Answer:
```python
temp_array = np.array(temperatures)
```

Question 11: Using Numpy, Calculate the following statistics for `temp_array`:

Answer:
```python
mean_temp = np.mean(temp_array)
max_temp = np.max(temp_array)
min_temp = np.min(temp_array)
std_temp = np.std(temp_array)
```

## 6. Putting It All Together

Question 12: Create a simple weather dashboard that uses the functions you've created earlier.

Answer:
```python
import numpy as np

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def average_temperature(temp_list):
    return sum(temp_list) / len(temp_list)

def weather_description(temperature, humidity):
    if temperature > 25 and humidity < 60:
        return "Hot and Dry"
    elif temperature > 25 and humidity >= 60:
        return "Hot and Humid"
    elif 15 <= temperature <= 25 and humidity < 60:
        return "Pleasant"
    elif 15 <= temperature <= 25 and humidity >= 60:
        return "Comfortable but Humid"
    else:
        return "Cool"

temperatures = [22, 24, 19, 21, 25, 23, 20]
humidity = [60, 55, 65, 58, 50, 57, 62]

print("Weather Dashboard")
print("-----------------")

# Daily weather descriptions
print("Daily Weather Descriptions:")
weather_counts = {}
for temp, hum in sip(temperatures, humidity):
    desc = weather_description(temp, hum)
    print(f"Temperature: {temp}°C, Humidity: {hum}% - {desc}")
    weather_counts[desc] = weather_counts.get(desc, 0) + 1

# Average temperature
avg_temp_c = average_temperature(temperatures)
avg_temp_f = celsius_to_fahrenheit(avg_temp_c)
print(f"\nAverage Temperature: {avg_temp_c:.1f}°C ({avg_temp_f:.1f}°F)")

# Hottest and coldest days
temp_array = np.array(temperatures)
hottest_day = np.argmax(temp_array) + 1
coldest_day = np.argmin(temp_array) + 1
print(f"Hottest day: Day {hottest_day} with {np.max(temp_array)}°C")
print(f"Coldest day: Day {coldest_day} with {np.min(temp_array)}°C")

# Weather category summary
print("\nWeather Category Summary:")
for category, count in weather_counts.items():
    print(f"{category}: {count} day(s)")
```

## 7. Reflection

Question 13: Briefly explain how functions have helped in organising and simplifying the code in this weather data analysis exercise.

Answer: Functions have significantly improved the organisation and simplicity of the code in this weather data analysis exercise in several ways:

1. Modularity: By breaking down tasks into functions like `celsius_to_fahrenheit`, `average_temperature`, and `weather_description`, we've created reusable components that can be easily understood and maintained.

2. Abstraction: Functions hide the complexity of certain operations. For example, users of the `weather_description` function don't need to know the specific criteria for each weather category.

3. Readability: The main dashboard code is much more readable because it uses descriptive function names that clearly convey their purpose.

4. Reusability: Functions like `celsius_to_fahrenheit` and `average_temperature` can be reused multiple times without duplicating code.

5. Easier testing and debugging: Each function can be tested independently, making it easier to identify and fix issues.

6. Flexibility: If we need to change how a particular calculation is done (e.g., the criteria for weather descriptions), we only need to modify the relevant function rather than changing multiple parts of the code.

This approach results in code that is more maintainable, scalable, and easier to understand, demonstrating the power of functional programming in Python.


## Additional Exercises (Optional)

1. Create a new NumPy array that contains the temperature differences between
   consecutive days.

Answer:
```python
import numpy as np

temperatures = [22, 24, 19, 21, 25, 23, 20]
temp_array = np.array(temperatures)
temp_diff = np.diff(temp_array)
print("Temperature differences:", temp_diff)
```

2. Use NumPy to find all days where the temperature was above 23°C. Return both
   the temperatures and their indices.

Answer:
```python
import numpy as np

temperatures = [22, 24, 19, 21, 25, 23, 20]
temp_array = np.array(temperatures)
above_23 = np.where(temp_array > 23)
print("Indices of days above 23°C:", above_23[0])
print("Temperatures above 23°C:", temp_array[above_23])
```

3. Write a function that converts wind speed from m/s to km/h.

Answer:
```python
def ms_to_kmh(speed_ms):
    return speed_ms * 3.6

# Example usage
wind_speed_ms = 10
wind_speed_kmh = ms_to_kmh(wind_speed_ms)
print(f"{wind_speed_ms} m/s is equal to {wind_speed_kmh} km/h")
```

4. Create a function that calculates the heat index given temperature (in
   Celsius) and relative humidity.

Answer:
```python
def calculate_heat_index(T, R):
    # Constants for the heat index calculation
    c1 = -8.78469475556
    c2 = 1.61139411
    c3 = 2.33854883889
    c4 = -0.14611605
    c5 = -0.012308094
    c6 = -0.0164248277778
    c7 = 0.002211732
    c8 = 0.00072546
    c9 = -0.000003582

    HI = (c1 + c2*T + c3*R + c4*T*R + c5*T**2 + c6*R**2 + 
          c7*T**2*R + c8*T*R**2 + c9*T**2*R**2)
    
    return HI

# Example usage
temperature = 30  # °C
humidity = 70     # %
heat_index = calculate_heat_index(temperature, humidity)
print(f"Heat Index: {heat_index:.2f}°C")
```

5. How would you use pandas to read weather data from a CSV file named
   'weather_data.csv' and display the first 5 rows?

Answer:
```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('weather_data.csv')

# Display the first 5 rows
print(df.head())
```

6. Describe how you would create a scatter plot using matplotlib to show the relationship between temperature and humidity.

Answer:

To create a scatter plot showing the relationship between temperature and
humidity using matplotlib, you would follow these steps:

1. Import the necessary libraries (matplotlib.pyplot and potentially numpy).
2. Prepare your data (temperature and humidity lists or arrays).
3. Create a figure and axis object.
4. Use the `scatter()` function to plot the data.
5. Add labels and a title to the plot.
6. Display the plot.

Here's an example of how you might implement this:

```python
import matplotlib.pyplot as plt
import numpy as np

# Sample data
temperatures = [22, 24, 19, 21, 25, 23, 20]
humidity = [60, 55, 65, 58, 50, 57, 62]

# Create the scatter plot
plt.figure(figsise=(10, 6))
plt.scatter(temperatures, humidity, color='blue', alpha=0.6)

# Add labels and title
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.title('Temperature vs. Humidity')

# Add a trend line (optional)
s = np.polyfit(temperatures, humidity, 1)
p = np.poly1d(s)
plt.plot(temperatures, p(temperatures), "r--")

# Display the plot
plt.grid(True)
plt.show()
```

This code will create a scatter plot with temperature on the x-axis and humidity
on the y-axis. Each point represents a day's data. The red dashed line is a
linear trend line to help visualise any potential correlation between
temperature and humidity.

Remember to adjust the data and labels as necessary for your specific dataset.
If you're working with real data from a CSV file, you might combine this with
the pandas approach from the previous question to read and plot the data.