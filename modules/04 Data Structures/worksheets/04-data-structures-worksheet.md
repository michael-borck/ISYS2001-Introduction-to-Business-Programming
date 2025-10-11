---
title: "Python Data Structures Worksheet: Weather Edition"
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

## Section 1: Choosing the Right Data Structure

For each scenario, choose the most appropriate data structure (list, tuple, or dictionary) and briefly explain why. If possible, write out how you would represent the data using the chosen structure.

1. You need to store the names of the seven days of the week for a weather forecast application.

2. A weather station needs to record the daily high and low temperatures for a week.

3. You want to store information about a specific weather event, including the date, type of event (e.g., "hurricane", "thunderstorm"), and severity rating.

4. An application needs to store the latitude and longitude coordinates of multiple weather stations.

5. You're creating a program to track monthly rainfall totals for a year.

6. A weather app needs to store city names and their corresponding weather conditions.

7. You want to keep track of the wind direction at different times of the day (morning, afternoon, evening, night).

8. An app needs to store a list of severe weather alerts, where each alert has a type, location, and expiration time.

9. You're developing a system to record the average temperature for each month of the year. The system should allow for easy retrieval of the average temperature for a specific month. 

10. A weather monitoring system needs to store hourly temperature readings for a day, with the ability to quickly access the temperature at a specific hour.

## Section 2: Implementing Data Structures in Python

Complete the following Python exercises to practice working with lists, tuples, and dictionaries in a weather context. The advanced/bonus questions are marked with an asterisk (*).

1. Create a list called `weekly_temperatures` with seven daily high temperatures.
   ```python
   weekly_temperatures = # Your code here
   ```

2. Using the `weekly_temperatures` list, write code to:
   a) Print the highest temperature of the week
   b) Print the average temperature for the week

3. Create a tuple called `weather_station` with the name, latitude, and longitude of a weather station.
   ```python
   weather_station = # Your code here
   ```

4. Create a dictionary called `weather_forecast` for a 3-day forecast. Each day should have a "condition" and "temperature" key.
   ```python
   weather_forecast = # Your code here
   ```

5. Using the `weather_forecast` dictionary:
   a) Print the temperature for the second day
   b) Change the condition of the third day to "Rainy"

6. Create a list of tuples called `rainfall_data`, where each tuple contains a month name and its rainfall amount.
   ```python
   rainfall_data = # Your code here
   ```

7. Using the `rainfall_data` list, write code to find and print the month with the highest rainfall.

8. Create a dictionary called `city_temperatures` where keys are city names and values are lists of daily temperatures for a week.
   ```python
   city_temperatures = # Your code here
   ```

9. Using the `city_temperatures` dictionary, calculate and print the average temperature for each city.

10. Create a list of dictionaries called `weather_alerts`, where each dictionary represents a weather alert with "type", "location", and "severity" keys.
    ```python
    weather_alerts = # Your code here
    ```

    Then, write code to print all "severe" weather alerts.

*Advanced/Bonus Questions:*

11. * Using a for loop and if statements, categorize each day in `weekly_temperatures` as "Cool" (below 20°C), "Mild" (20-25°C), or "Warm" (above 25°C). Store the results in a new list called `temperature_categories`.

12. * Using the `rainfall_data` list, create a new dictionary where keys are seasons ("Spring", "Summer", "Autumn", "Winter") and values are the total rainfall for that season. Assume the list starts with January.

13. * Using the `city_temperatures` dictionary, find and print the name of the city with the most consistent temperature (i.e., the smallest difference between its highest and lowest temperature).

14. * Create a while loop that simulates daily temperature readings. Start with a temperature of 20°C and randomly increase or decrease it by 0-3°C each day. Stop the loop when the temperature goes below 15°C or above 30°C. Store the temperatures in a list.

15. * Using the `weather_alerts` list, write code that asks the user to input a location and then prints all alerts for that location, sorted by severity (assume severity is a number from 1-5, with 5 being the most severe).
