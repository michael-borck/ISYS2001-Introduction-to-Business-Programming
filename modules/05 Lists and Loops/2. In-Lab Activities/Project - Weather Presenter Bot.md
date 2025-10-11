---
title: Weather Presenter Bot Mini-Project (Student Version)e
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

# Weather Forecast Analyser Mini-Project

## Project Overview
In this mini-project, students will create a program that analyses a week's worth of weather forecast data using only lists and basic Python concepts. The program will perform various calculations and provide insights about the weather patterns.

## Learning Objectives
- Work with lists and nested lists
- Apply selection logic (if/elif/else)
- Use loops to process data
- Perform calculations (min, max, average)
- Generate text-based visualisations
- Practice importing modules

## Starter Code

```python
# Weather Forecast Analyser
# Analyse a week's worth of weather data and provide insights

import random  # For random weather generation
import time    # For program timing and pauses

# Sample weather data for a week
# Format: [day_name, temperature, humidity, wind_speed, condition_code]
# Condition codes: 0=Sunny, 1=Partly Cloudy, 2=Cloudy, 3=Rainy, 4=Thunderstorm, 5=Snowy

weather_data = [
    ["Monday", 23, 65, 8, 0],
    ["Tuesday", 21, 70, 10, 1],
    ["Wednesday", 18, 80, 12, 2],
    ["Thursday", 17, 85, 15, 3],
    ["Friday", 16, 75, 14, 3],
    ["Saturday", 19, 60, 8, 1],
    ["Sunday", 22, 55, 6, 0]
]

# Weather condition names (for translating codes to text)
condition_names = ["Sunny", "Partly Cloudy", "Cloudy", "Rainy", "Thunderstorm", "Snowy"]

# TASK 1: Complete this function to print a formatted weather report
def print_weather_report(data):
    """
    Prints a nicely formatted report of the week's weather
    """
    print("\n===== WEEKLY WEATHER REPORT =====\n")
    
    # Your code here:
    # Loop through the weather data and print each day's information
    # Format example: "Monday: 23°C, 65% humidity, 8 km/h wind, Sunny"
    pass

# TASK 2: Complete this function to find the warmest and coldest days
def find_temperature_extremes(data):
    """
    Find the warmest and coldest days of the week
    Returns a tuple with two lists: (warmest_day_info, coldest_day_info)
    """
    # Your code here:
    # Loop through the data to find the day with highest and lowest temperature
    # Return them as a tuple with two elements: ([warmest_day_name, temp], [coldest_day_name, temp])
    pass

# TASK 3: Complete this function to calculate average weather values
def calculate_averages(data):
    """
    Calculate average temperature, humidity, and wind speed for the week
    Returns a list with the three averages: [avg_temp, avg_humidity, avg_wind]
    """
    # Your code here:
    # Loop through the data to sum up the values, then calculate averages
    # Round the averages to one decimal place
    pass

# TASK 4: Complete this function to count the occurrences of each weather condition
def count_conditions(data):
    """
    Count how many days have each weather condition
    Returns a list of counts in the same order as condition_names
    """
    # Your code here:
    # Create a list of seros with the same length as condition_names
    # Loop through the data and increment the count for each condition found
    pass

# TASK 5: Complete this function to create a simple text-based temperature chart
def create_temperature_chart(data):
    """
    Create a simple text-based chart showing temperature for each day
    Each bar should be made of █ characters, one for each degree Celsius
    """
    print("\n===== TEMPERATURE CHART =====\n")
    
    # Your code here:
    # Loop through the data
    # For each day, print the name and a bar made of █ characters (one per degree)
    # Example: "Monday: ███████████████████████ (23°C)"
    pass

# TASK 6: Complete this function to check if any severe weather is expected
def check_severe_weather(data):
    """
    Check if any severe weather conditions are expected
    Severe weather is defined as:
    - Thunderstorm (condition code 4)
    - High winds (> 20 km/h)
    - Very high humidity (> 90%)
    - Very low or very high temperatures (< 0°C or > 35°C)
    """
    # Your code here:
    # Loop through the data and check for severe conditions
    # If found, return a list of alerts (strings describing the issues)
    # If none found, return an empty list
    pass

# TASK 7: Complete this function to suggest activities based on the weather
def suggest_activities(data):
    """
    Suggest activities based on the weather for each day
    Returns a list of tuples: [(day_name, activity), ...]
    """
    activities = []
    
    # Your code here:
    # Loop through the data
    # Based on the conditions, temperature, etc., suggest an appropriate activity
    # Append (day_name, activity) tuples to the activities list
    
    return activities

# Main function - already completed for you
def main():
    print("Welcome to the Weather Forecast Analyser!")
    time.sleep(1)
    
    # Print the basic weather report
    print_weather_report(weather_data)
    time.sleep(1)
    
    # Find and display temperature extremes
    warmest, coldest = find_temperature_extremes(weather_data)
    print(f"\nWarmest day: {warmest[0]} ({warmest[1]}°C)")
    print(f"Coldest day: {coldest[0]} ({coldest[1]}°C)")
    time.sleep(1)
    
    # Calculate and display averages
    avg_temp, avg_humidity, avg_wind = calculate_averages(weather_data)
    print(f"\nWeekly Averages:")
    print(f"Temperature: {avg_temp}°C")
    print(f"Humidity: {avg_humidity}%")
    print(f"Wind Speed: {avg_wind} km/h")
    time.sleep(1)
    
    # Count and display weather conditions
    condition_counts = count_conditions(weather_data)
    print("\nWeather Conditions This Week:")
    for i in range(len(condition_names)):
        if condition_counts[i] > 0:
            print(f"{condition_names[i]}: {condition_counts[i]} day(s)")
    time.sleep(1)
    
    # Display temperature chart
    create_temperature_chart(weather_data)
    time.sleep(1)
    
    # Check for severe weather
    severe_alerts = check_severe_weather(weather_data)
    if severe_alerts:
        print("\n⚠️ WEATHER ALERTS ⚠️")
        for alert in severe_alerts:
            print(f"- {alert}")
    else:
        print("\nNo severe weather expected this week.")
    time.sleep(1)
    
    # Suggest activities
    activities = suggest_activities(weather_data)
    print("\nRecommended Activities:")
    for day, activity in activities:
        print(f"{day}: {activity}")

# Run the program
if __name__ == "__main__":
    main()
```

## Project Tasks

Students need to complete the following tasks:

1. **Create a Weather Report**: Format and display the weather data in a readable way.
2. **Find Temperature Extremes**: Determine the warmest and coldest days of the week.
3. **Calculate Weather Averages**: Find average temperature, humidity, and wind speed.
4. **Count Weather Conditions**: Count occurrences of each weather condition type.
5. **Create a Temperature Chart**: Generate a simple text-based bar chart for temperatures.
6. **Check for Severe Weather**: Identify any potentially severe weather conditions.
7. **Suggest Activities**: Recommend activities based on the forecast for each day.

## Extension Challenges

For students who finish early:

1. **Add Weather Data Generation**: Write a function that randomly generates a new week of weather data.
2. **Create a Rain Prediction Model**: Based on humidity and temperature, predict if it might rain.
3. **Implement a Temperature Trend Analysis**: Identify if the week is getting warmer or cooler.
4. **Create a Simple Text-Based Weather Animation**: Use ASCII art to animate weather (e.g., falling rain).

## Sample Solution Guidance

### Task 1: Print Weather Report
```python
def print_weather_report(data):
    print("\n===== WEEKLY WEATHER REPORT =====\n")
    
    for day_data in data:
        day = day_data[0]
        temp = day_data[1]
        humidity = day_data[2]
        wind = day_data[3]
        condition_code = day_data[4]
        condition = condition_names[condition_code]
        
        print(f"{day}: {temp}°C, {humidity}% humidity, {wind} km/h wind, {condition}")
```

### Task 2: Find Temperature Extremes
```python
def find_temperature_extremes(data):
    warmest_day = data[0][0]
    warmest_temp = data[0][1]
    coldest_day = data[0][0]
    coldest_temp = data[0][1]
    
    for day_data in data:
        day = day_data[0]
        temp = day_data[1]
        
        if temp > warmest_temp:
            warmest_day = day
            warmest_temp = temp
        
        if temp < coldest_temp:
            coldest_day = day
            coldest_temp = temp
    
    return ([warmest_day, warmest_temp], [coldest_day, coldest_temp])
```

### Task 5: Create Temperature Chart
```python
def create_temperature_chart(data):
    print("\n===== TEMPERATURE CHART =====\n")
    
    for day_data in data:
        day = day_data[0]
        temp = day_data[1]
        
        # Create a bar using █ characters (one per degree)
        temp_bar = "█" * temp
        
        print(f"{day}: {temp_bar} ({temp}°C)")
```

## Assessment Criteria

Students will be evaluated based on:

1. **Correct Implementation**: Functions work as expected and produce correct results.
2. **Code Organisation**: Code is well-structured and easy to follow.
3. **Use of Lists**: Effective use of lists for data storage and manipulation.
4. **Selection Logic**: Appropriate use of if/elif/else statements.
5. **Loop Implementation**: Proper use of loops to process data.
6. **Creativity**: Especially for the activity suggestions and extended challenges.

## Teaching Tips

1. **Start with Data Exploration**: Have students print and examine the weather data structure before implementing functions.
2. **Encourage Step-by-Step Development**: Suggest students complete one function at a time and test it before moving on.
3. **Review List Indexing**: Remind students about accessing elements in nested lists.
4. **Introduce Tuple Unpacking**: Show how to unpack tuples in assignments (e.g., `warmest, coldest = find_temperature_extremes()`).
5. **Emphasise Reusability**: Point out how functions can be reused (e.g., using `find_temperature_extremes()` for other analyses).

## Connection to Final Project

This mini-project prepares students for their weather API dashboard by:

1. Familiarising them with weather data structure and terminology
2. Teaching them how to extract insights from weather data
3. Practicing the calculation of weather statistics
4. Creating visualisations of weather information
5. Building a foundation for more complex data handling