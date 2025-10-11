---
title: STAFF ANSWER Weather Presenter Bot Mini-Project (Student Version)e
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
# Weather Forecast Analyzer: Staff Answer Guide

## Project Overview
This guide provides complete solutions and teaching notes for the Weather Forecast Analyzer mini-project. This project helps students practice working with lists, loops, conditionals, and basic calculations without requiring dictionaries, classes, or file I/O.

## Complete Solutions

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

**Key concepts**: Loops, list indexing, f-strings

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

**Key concepts**: Variables to track extremes, conditionals, nested lists, return values

### Task 3: Calculate Averages
```python
def calculate_averages(data):
    total_temp = 0
    total_humidity = 0
    total_wind = 0
    days = len(data)
    
    for day_data in data:
        total_temp += day_data[1]
        total_humidity += day_data[2]
        total_wind += day_data[3]
    
    avg_temp = round(total_temp / days, 1)
    avg_humidity = round(total_humidity / days, 1)
    avg_wind = round(total_wind / days, 1)
    
    return [avg_temp, avg_humidity, avg_wind]
```

**Key concepts**: Summation, division, rounding, lists as return values

### Task 4: Count Conditions
```python
def count_conditions(data):
    # Create a list of zeros with the same length as condition_names
    counts = [0] * len(condition_names)
    
    # Loop through the data and increment the count for each condition found
    for day_data in data:
        condition_code = day_data[4]
        counts[condition_code] += 1
    
    return counts
```

**Key concepts**: List creation with multiplication, using list indices as counters

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

**Key concepts**: String repetition, text-based visualization

### Task 6: Check Severe Weather
```python
def check_severe_weather(data):
    alerts = []
    
    for day_data in data:
        day = day_data[0]
        temp = day_data[1]
        humidity = day_data[2]
        wind = day_data[3]
        condition_code = day_data[4]
        
        # Check for severe conditions
        if condition_code == 4:  # Thunderstorm
            alerts.append(f"Thunderstorm expected on {day}")
        
        if wind > 20:
            alerts.append(f"High winds ({wind} km/h) expected on {day}")
        
        if humidity > 90:
            alerts.append(f"Very high humidity ({humidity}%) expected on {day}")
        
        if temp < 0:
            alerts.append(f"Freezing temperature ({temp}°C) expected on {day}")
        elif temp > 35:
            alerts.append(f"Extreme heat ({temp}°C) expected on {day}")
    
    return alerts
```

**Key concepts**: Multiple conditions, building lists dynamically, string formatting

### Task 7: Suggest Activities
```python
def suggest_activities(data):
    activities = []
    
    for day_data in data:
        day = day_data[0]
        temp = day_data[1]
        condition_code = day_data[4]
        
        # Choose an activity based on weather
        if condition_code == 0:  # Sunny
            if temp > 25:
                activity = "Go to the beach or pool"
            else:
                activity = "Go for a hike or picnic"
        elif condition_code == 1:  # Partly Cloudy
            activity = "Perfect for outdoor sports"
        elif condition_code == 2:  # Cloudy
            activity = "Visit a park or go for a walk"
        elif condition_code == 3:  # Rainy
            activity = "Visit a museum or watch a movie"
        elif condition_code == 4:  # Thunderstorm
            activity = "Stay indoors with a good book"
        elif condition_code == 5:  # Snowy
            activity = "Build a snowman or go sledding"
        else:
            activity = "Check weather again"
        
        activities.append((day, activity))
    
    return activities
```

**Key concepts**: Nested conditionals, tuples, complex decision-making

## Common Student Questions and Answers

### 1. "I'm confused about how to access the weather data. What does `day_data[1]` mean?"
**Answer**: The `weather_data` is a list of lists. Each inner list represents one day's data. When we loop through `weather_data`, each `day_data` is one of those inner lists. So `day_data[0]` is the day name, `day_data[1]` is the temperature, and so on. Think of it like a table where each row is a day, and each column is a different weather attribute.

### 2. "Why do we need to return a tuple with two lists in the `find_temperature_extremes` function?"
**Answer**: The function needs to return two pieces of information: the warmest day and the coldest day. Each of these needs both a day name and a temperature. We put each pair (day name, temperature) in its own list, and then return both lists inside a tuple. This way, when the main function calls it, it can easily unpack both pieces of information with: `warmest, coldest = find_temperature_extremes(weather_data)`.

### 3. "I don't understand the line `counts = [0] * len(condition_names)` in the count_conditions function."
**Answer**: This creates a new list filled with zeros. The `len(condition_names)` tells us how many different weather conditions we have, and the `* len(condition_names)` part repeats the `[0]` that many times. So if we have 6 possible conditions, this creates `[0, 0, 0, 0, 0, 0]`. Then we can use each position to count a specific condition.

### 4. "What does the `█` character do in the temperature chart function?"
**Answer**: That's a special character called a "block" that creates a solid bar when printed. By repeating it (using `"█" * temp`), we create a visual bar where each block represents one degree Celsius. This gives us a simple visual chart using just text.

### 5. "When I run my code, I get an error that says 'TypeError: can only concatenate str (not "int") to str'. What's wrong?"
**Answer**: This error happens when you try to combine a string and a number directly, like `"Temperature: " + temp`. You need to convert the number to a string first, like `"Temperature: " + str(temp)`. Alternatively, you can use an f-string like `f"Temperature: {temp}"`, which automatically handles the conversion.

### 6. "In the severe weather check, why do we have separate if statements instead of using elif?"
**Answer**: We use separate `if` statements because we want to check for multiple severe conditions that could happen on the same day. With `elif`, only one condition would be checked. For example, a day could be both very hot AND have high winds, and we want to report both of those alerts.

### 7. "Why do we use tuples in the activities list but not in other functions?"
**Answer**: In the `suggest_activities` function, we need to keep two pieces of information together for each day: the day name and the suggested activity. A tuple like `(day, activity)` is a good way to keep these paired. The main function then unpacks these pairs with `for day, activity in activities:`. In other functions, we use lists when we need to modify the data, and tuples when we just need to group related items.

### 8. "I'm having trouble with the for loops. How do I know when to use them?"
**Answer**: Generally, use a for loop when you need to:
- Process each item in a collection (like each day in `weather_data`)
- Perform the same operation multiple times
- Build a new collection based on an existing one
In this project, we often need to process each day's weather data, so we use `for day_data in data:` to go through each day one by one.

### 9. "What's the difference between `return` and `print`?"
**Answer**: `print` displays information to the console but doesn't save it for later use in your program. `return` sends data back from a function so it can be stored in a variable and used later. For example, the `calculate_averages` function returns a list of values that the main function can then use to print specific messages.

### 10. "My temperature chart looks weird. The bars are too long for some temperatures."
**Answer**: If you're testing with very high temperatures, the bars might be too long to display nicely. You could modify the function to scale the bars, for example by dividing the temperature by 2 or using a different character. For example: `temp_bar = "█" * (temp // 2)` would make each block represent 2 degrees.

## Teaching Tips

### Understanding List Structure
Draw a table representation of the weather data on the board:

| Index | Day       | Temp | Humidity | Wind | Condition |
|-------|-----------|------|----------|------|-----------|
| 0     | Monday    | 23   | 65       | 8    | 0 (Sunny) |
| 1     | Tuesday   | 21   | 70       | 10   | 1 (Partly)|
| ...   | ...       | ...  | ...      | ...  | ...       |

Explain that `weather_data[0]` gets the first row: `["Monday", 23, 65, 8, 0]`
And `weather_data[0][1]` gets the temperature (23) from that row.

### Demonstrating Loop Patterns
Show the common pattern for processing each day:
```python
for day_data in weather_data:
    # day_data is now each individual day's list
    day_name = day_data[0]
    temperature = day_data[1]
    # ... work with this data
```

### Introducing Testing Techniques
Encourage students to test each function individually:
```python
# Test the print_weather_report function
print_weather_report(weather_data)

# Test the calculate_averages function
averages = calculate_averages(weather_data)
print(f"Average temperature: {averages[0]}°C")
```

## Extension Implementation Ideas

### Random Weather Generation
```python
def generate_random_weather():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    new_data = []
    
    for day in days:
        temp = random.randint(0, 35)
        humidity = random.randint(30, 95)
        wind = random.randint(0, 30)
        condition = random.randint(0, 5)
        
        day_data = [day, temp, humidity, wind, condition]
        new_data.append(day_data)
    
    return new_data
```

### Temperature Trend Analysis
```python
def analyze_temperature_trend(data):
    temperatures = [day[1] for day in data]
    
    # Compare first half with second half
    first_half = sum(temperatures[:len(temperatures)//2]) / (len(temperatures)//2)
    second_half = sum(temperatures[len(temperatures)//2:]) / (len(temperatures) - len(temperatures)//2)
    
    if second_half > first_half:
        return "Getting warmer through the week"
    elif second_half < first_half:
        return "Getting cooler through the week"
    else:
        return "Temperatures are stable through the week"
```

## Assessment Rubric

| Criteria | Excellent (A) | Satisfactory (B/C) | Needs Improvement (D/F) |
|----------|---------------|--------------------|-----------------------|
| **Task Completion** | All 7 functions implemented correctly | 5-6 functions working correctly | Fewer than 5 functions working |
| **Code Logic** | Logic is sound with optimal solutions | Logic works but may not be optimal | Logic has significant flaws |
| **Lists Usage** | Effectively uses lists for all data | Generally uses lists appropriately | Struggles with list operations |
| **Loops** | Correctly implements all required loops | Most loops implemented correctly | Problems with loop implementation |
| **Conditionals** | Uses conditionals effectively and efficiently | Basic conditionals implemented correctly | Incorrect or missing conditions |
| **Creativity** | Highly creative activity suggestions or extensions | Standard activity suggestions | Minimal effort in suggestions |
| **Code Style** | Well-formatted, clear variable names | Generally readable code | Poor formatting, unclear naming |