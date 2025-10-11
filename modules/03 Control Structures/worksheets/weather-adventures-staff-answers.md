---
title: "Weather Adventures in Python Land: Staff Answers"
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


## Part 1: Basic Concepts in Pseudocode

1. Suggest clothing based on temperature:
```
Input temperature
If temperature > 25°C then
    Suggest light clothing
Else if temperature >= 15°C and temperature <= 25°C then
    Suggest a light jacket
Else
    Suggest warm clothing
```

2. Check if it's a good day for a picnic:
```
Input temperature
Input is_raining
If not is_raining AND temperature >= 20°C AND temperature <= 30°C then
    Print "It's a good day for a picnic!"
Else
    Print "Not an ideal day for a picnic."
```

3. Count rainy days in a week:
```
Set rainy_days = 0
For each day in week (7 times):
    Input weather_condition
    If weather_condition is "rainy" then
        Increment rainy_days by 1
Print rainy_days
```

4. Calculate average temperature for 5 days:
```
Set total_temperature = 0
For i = 1 to 5:
    Input daily_temperature
    Add daily_temperature to total_temperature
Set average_temperature = total_temperature / 5
Print average_temperature
```

5. Issue heat wave warning:
```
Set consecutive_hot_days = 0
For each day in forecast:
    Input temperature
    If temperature > 35°C then
        Increment consecutive_hot_days by 1
        If consecutive_hot_days >= 3 then
            Issue heat wave warning
            Exit loop
    Else
        Set consecutive_hot_days = 0
```

## Part 2: Structuring English Descriptions into Pseudocode

6. Air Quality Monitoring:
```
Set readings_count = 0
Set alert_triggered = False

While readings_count < 24 AND not alert_triggered:
    Measure AQI
    Increment readings_count by 1
    If AQI > 150 then
        Trigger alert
        Set alert_triggered = True
    Wait for 1 hour
```

7. Weather Forecasting Process:
```
For day = 1 to 7:
    Input today's temperature, humidity, wind_speed
    Input yesterday's temperature, humidity

    If today's temperature > yesterday's temperature AND today's humidity > yesterday's humidity then
        If wind_speed is increasing then
            Predict stormy weather
        Else
            Predict higher chance of rain
    Else if today's temperature ≈ yesterday's temperature AND today's humidity ≈ yesterday's humidity then
        Predict similar weather to today
    Else
        Predict based on other factors (not specified in the given process)

    Set yesterday's temperature = today's temperature
    Set yesterday's humidity = today's humidity
```

8. Severe Weather Alert System:
```
While True:
    Input temperature, wind_speed, precipitation
    
    Set alert_level = "None"
    
    If temperature > 40°C OR wind_speed > 100 km/h OR precipitation > 50 mm/hour then
        Set alert_level = "Red Alert"
    Else if temperature > 35°C AND wind_speed > 60 km/h AND precipitation > 30 mm/hour then
        Set alert_level = "Orange Alert"
    Else if (temperature > 35°C AND wind_speed > 60 km/h) OR
            (temperature > 35°C AND precipitation > 30 mm/hour) OR
            (wind_speed > 60 km/h AND precipitation > 30 mm/hour) then
        Set alert_level = "Yellow Alert"
    
    If alert_level != "None" then
        Issue alert_level
    
    Wait for 30 minutes
```

## Part 3: Reflection and Analysis

9. Challenging aspects of structuring pseudocode:
   - The weather forecasting process (Question 7) was challenging due to the need to compare current and previous day's data, requiring careful consideration of variable updates and logical flow.
   - The severe weather alert system (Question 8) was complex due to multiple nested conditions and the need to check for different combinations of factors.

10. Three questions for a GenAI tutor to refine the severe weather alert system pseudocode:
   a. How can I optimize the condition checks to make the code more efficient?
   b. What's the best way to implement the "maintains the highest level alert until conditions improve" requirement?
   c. How can I modify the pseudocode to allow for easy addition of new alert conditions in the future?

11. Extending the air quality monitoring pseudocode:
   To extend the air quality monitoring system, we could:
   - Add multiple pollutant measurements (e.g., PM2.5, ozone, nitrogen dioxide)
   - Implement different alert levels based on AQI ranges
   - Include a rolling average calculation for more stable readings
   - Add wind direction and speed to predict pollution spread
   - Implement a data logging system for historical analysis

This extended version might look like:

```
Initialize pollutants_list = [PM2.5, ozone, nitrogen_dioxide]
Initialize readings = empty dictionary
Initialize alert_levels = {
    "Green": 0-50,
    "Yellow": 51-100,
    "Orange": 101-150,
    "Red": 151-200,
    "Purple": 201+
}

While True:
    For each pollutant in pollutants_list:
        Measure pollutant level
        Add to readings[pollutant]
        If readings[pollutant] has 24 entries:
            Calculate 24-hour average
            Remove oldest reading
    
    Calculate overall AQI based on pollutant readings
    
    Determine alert_level based on AQI and alert_levels
    
    If alert_level changed:
        Issue new alert
    
    Measure wind_direction and wind_speed
    Predict pollution spread based on wind data
    
    Log all data to database
    
    Wait for 1 hour
```

This extended version provides a more comprehensive air quality monitoring system with multiple pollutants, rolling averages, multi-level alerts, and additional features like wind-based predictions and data logging.
