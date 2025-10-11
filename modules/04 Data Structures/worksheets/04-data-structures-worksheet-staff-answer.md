---
title: "STAFF ANSWERS: Python Data Structures Worksheet: Weather Edition"
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

Here are the staff answers for the Python Data Structures Worksheet: Weather Edition:

## Section 1: Choosing the Right Data Structure

1. List
   ```python
   days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
   ```
   Explanation: A list is appropriate because the order of days is important, and the collection is fixed.

2. List of tuples
   ```python
   weekly_temps = [(25, 15), (27, 16), (26, 14), (28, 17), (30, 18), (29, 17), (26, 15)]
   ```
   Explanation: Each day's high and low temperatures form a pair, which is best represented as a tuple. The week's data is then stored in a list.

3. Dictionary
   ```python
   weather_event = {"date": "2024-08-12", "type": "hurricane", "severity": 4}
   ```
   Explanation: A dictionary allows us to store key-value pairs for different attributes of the weather event.

4. List of tuples
   ```python
   weather_stations = [(40.7128, -74.0060), (34.0522, -118.2437), (51.5074, -0.1278)]
   ```
   Explanation: Each coordinate pair is represented as a tuple, and multiple stations are stored in a list.

5. List
   ```python
   monthly_rainfall = [50, 45, 60, 55, 70, 65, 40, 35, 55, 75, 80, 70]
   ```
   Explanation: A list allows for easy indexing by month (assuming January is index 0) and maintains order.

6. Dictionary
   ```python
   city_weather = {"New York": "Sunny", "London": "Rainy", "Tokyo": "Cloudy"}
   ```
   Explanation: A dictionary allows for quick lookup of weather conditions by city name.

7. Dictionary
   ```python
   wind_direction = {"morning": "NE", "afternoon": "E", "evening": "SE", "night": "S"}
   ```
   Explanation: A dictionary allows for easy association of time periods with wind directions.

8. List of dictionaries
   ```python
   severe_weather_alerts = [
       {"type": "Tornado", "location": "Oklahoma City", "expiration": "2024-08-12 18:00"},
       {"type": "Flash Flood", "location": "Miami", "expiration": "2024-08-13 10:00"}
   ]
   ```
   Explanation: Each alert is represented as a dictionary, and multiple alerts are stored in a list.

9. Dictionary
   ```python
   monthly_avg_temp = {"January": 5, "February": 7, "March": 10, "April": 15, "May": 20, "June": 25, "July": 28, "August": 27, "September": 23, "October": 18, "November": 12, "December": 7}
   ```
   Explanation: A dictionary allows for quick lookup of average temperature by month name.

10. Dictionary
    ```python
    hourly_temps = {0: 20, 1: 19, 2: 18, 3: 17, 4: 16, 5: 15, 6: 16, 7: 18, 8: 20, 9: 22, 10: 24, 11: 26, 12: 28, 13: 29, 14: 30, 15: 30, 16: 29, 17: 28, 18: 26, 19: 24, 20: 23, 21: 22, 22: 21, 23: 20}
    ```
    Explanation: A dictionary allows for quick access to temperature by hour (0-23).

## Section 2: Implementing Data Structures in Python

1. ```python
   weekly_temperatures = [28, 30, 29, 31, 27, 26, 29]
   ```

2. a) ```python
      print(max(weekly_temperatures))
      ```
   b) ```python
      print(sum(weekly_temperatures) / len(weekly_temperatures))
      ```

3. ```python
   weather_station = ("Central Park", 40.7829, -73.9654)
   ```

4. ```python
   weather_forecast = {
       "Day 1": {"condition": "Sunny", "temperature": 28},
       "Day 2": {"condition": "Partly Cloudy", "temperature": 26},
       "Day 3": {"condition": "Cloudy", "temperature": 24}
   }
   ```

5. a) ```python
      print(weather_forecast["Day 2"]["temperature"])
      ```
   b) ```python
      weather_forecast["Day 3"]["condition"] = "Rainy"
      ```

6. ```python
   rainfall_data = [
       ("January", 50), ("February", 45), ("March", 60), ("April", 55),
       ("May", 70), ("June", 65), ("July", 40), ("August", 35),
       ("September", 55), ("October", 75), ("November", 80), ("December", 70)
   ]
   ```

7. ```python
   max_rainfall = max(rainfall_data, key=lambda x: x[1])
   print(f"The month with the highest rainfall is {max_rainfall[0]} with {max_rainfall[1]}mm")
   ```

8. ```python
   city_temperatures = {
       "New York": [28, 30, 29, 31, 27, 26, 29],
       "London": [20, 22, 21, 23, 19, 18, 20],
       "Tokyo": [31, 32, 33, 31, 30, 29, 32]
   }
   ```

9. ```python
   for city, temps in city_temperatures.items():
       avg_temp = sum(temps) / len(temps)
       print(f"Average temperature in {city}: {avg_temp:.1f}°C")
   ```

10. ```python
    weather_alerts = [
        {"type": "Thunderstorm", "location": "Chicago", "severity": 3},
        {"type": "Hurricane", "location": "Miami", "severity": 5},
        {"type": "Heatwave", "location": "Phoenix", "severity": 4}
    ]

    severe_alerts = [alert for alert in weather_alerts if alert["severity"] >= 4]
    for alert in severe_alerts:
        print(f"Severe alert: {alert['type']} in {alert['location']}")
    ```

*Advanced/Bonus Questions:*

11. ```python
    temperature_categories = []
    for temp in weekly_temperatures:
        if temp < 20:
            temperature_categories.append("Cool")
        elif 20 <= temp <= 25:
            temperature_categories.append("Mild")
        else:
            temperature_categories.append("Warm")
    ```

12. ```python
    seasons = {"Spring": 0, "Summer": 0, "Autumn": 0, "Winter": 0}
    for i, (month, rainfall) in enumerate(rainfall_data):
        season = ["Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Autumn", "Autumn", "Autumn", "Winter"][i]
        seasons[season] += rainfall
    ```

13. ```python
    most_consistent_city = min(city_temperatures, key=lambda city: max(city_temperatures[city]) - min(city_temperatures[city]))
    print(f"The city with the most consistent temperature is {most_consistent_city}")
    ```

14. ```python
    import random

    temperature = 20
    temperature_readings = [temperature]

    while 15 <= temperature <= 30:
        change = random.uniform(-3, 3)
        temperature += change
        temperature_readings.append(round(temperature, 1))

    print(f"Temperature readings: {temperature_readings}")
    print(f"Simulation ended after {len(temperature_readings)} days")
    ```

15. ```python
    location = input("Enter a location: ")
    location_alerts = [alert for alert in weather_alerts if alert["location"].lower() == location.lower()]
    sorted_alerts = sorted(location_alerts, key=lambda x: x["severity"], reverse=True)

    if sorted_alerts:
        print(f"Alerts for {location}:")
        for alert in sorted_alerts:
            print(f"Type: {alert['type']}, Severity: {alert['severity']}")
    else:
        print(f"No alerts found for {location}")
    ```

These answers demonstrate proper use of Python data structures and incorporate weather-related scenarios to make the exercises more engaging and practical.