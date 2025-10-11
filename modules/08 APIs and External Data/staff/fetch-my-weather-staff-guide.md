---
title: "Staff Answer Guide: Worksheet 1 - Introduction to APIs with fetch-my-weather"
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



This guide provides expected outcomes, common issues, and tips for supporting students as they work through Worksheet 1 on API basics with the fetch-my-weather package.

## Key Concepts Review

- **API (Application Programming Interface)**: A set of rules allowing different software applications to communicate with each other. In this worksheet, students use a simplified API to access weather data.
- **fetch-my-weather**: A beginner-friendly Python package that wraps around the wttr.in weather service, providing simplified access to weather data.
- **Pseudocode**: A method for planning code logic without worrying about exact syntax, helping students organize their thoughts before implementation.

## Activity 1: Teaching an LLM About fetch-my-weather

### Expected Outcomes
- Students should successfully upload the documentation to an LLM and receive a coherent summary of the package.
- A good LLM response will cover:
  - Main functionality (weather data retrieval)
  - Key features (caching, error handling, different formats)
  - Basic usage examples

### Common Issues
- **Document upload problems**: Some students may have difficulty uploading documents to LLMs, especially if using free tiers with limited upload capabilities.
- **Poorly formulated prompts**: Students might not get useful responses if their prompts are too vague.

### Support Tips
- Encourage students to be specific in their prompts, asking about particular aspects of the package they're confused about.
- If upload isn't working, suggest they copy key parts of the documentation directly into their prompt.
- Remind students that they can iterate on prompts to get more precise information.

## Activity 2: Using the fetch-my-weather Package

### Expected Code Output Examples

Basic weather retrieval:
```python
import fetch_my_weather

# Get weather for London
london_weather = fetch_my_weather.get_weather(location="London")
print(london_weather)

# Expected output: A WeatherResponse Pydantic model containing weather data for London
```

Compact view:
```python
# Get weather with compact view
compact_weather = fetch_my_weather.get_weather(location="Paris", view_options="1")
print(compact_weather)

# Expected output: A more condensed weather report with fewer forecast days
```

Language options:
```python
# Get weather in Spanish
spanish_weather = fetch_my_weather.get_weather(location="Madrid", lang="es")
print(spanish_weather)

# Expected output: Weather data with text elements in Spanish
```

Moon phase:
```python
# Get moon phase information
moon_phase = fetch_my_weather.get_weather(is_moon=True)
print(moon_phase)

# Expected output: Current moon phase information
```

Error handling example:
```python
# Trying invalid location
result = fetch_my_weather.get_weather(location="NonExistentPlace12345")

# Check for error
if isinstance(result, str) and result.startswith("Error:"):
    print(f"Something went wrong: {result}")
else:
    print("Weather data retrieved successfully")

# Expected output: "Something went wrong: Error: [error message]"
```

### Common Issues
- **Installation problems**: Students may encounter pip installation issues, especially if they have Python environment conflicts.
- **String vs object confusion**: Students might be confused by the return type (Pydantic model by default, string if format="text").
- **Error handling misunderstanding**: Students might expect exceptions rather than error strings.

### Support Tips
- For installation issues, check Python version compatibility and suggest using a virtual environment.
- Explain that `get_weather()` returns different types based on the `format` parameter (default is a Pydantic model).
- Emphasize the beginner-friendly error handling that returns strings instead of raising exceptions.
- Encourage students to explore the structure of the returned data using `print()` and `dir()`.

## Activity 3: Create a Weather Dashboard

### Pseudocode Guidance
Good pseudocode should:
- Be clear and concise
- Show the logical flow of the program
- Handle potential errors
- Include necessary loops and conditions

### Working Implementation Example

```python
import fetch_my_weather
from datetime import datetime

def create_weather_dashboard(city_list):
    # Initialize empty list for storing weather data
    city_weather_data = []
    
    # Get weather data for each city
    for city in city_list:
        weather = fetch_my_weather.get_weather(location=city, format="text")
        
        # Check if we got valid weather data
        if isinstance(weather, str) and not weather.startswith("Error:"):
            city_weather_data.append({"city": city, "weather": weather})
        else:
            print(f"Could not get weather for {city}: {weather}")
    
    # Display the dashboard header
    print("\n" + "="*50)
    print(f"WEATHER DASHBOARD - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*50)
    
    # Display weather for each city
    for city_data in city_weather_data:
        print(f"\n{city_data['city'].upper()}")
        print(city_data['weather'])
        print("-"*50)

# Get cities from user
def main():
    print("Welcome to the Weather Dashboard!")
    city_input = input("Enter cities to check (comma-separated): ")
    cities = [city.strip() for city in city_input.split(",")]
    
    # Create the dashboard
    create_weather_dashboard(cities)

if __name__ == "__main__":
    main()
```

### Common Issues
- **Format confusion**: Students might mix JSON and text formats, causing display issues.
- **Error handling**: Students may not properly check for error messages.
- **Input validation**: Poor handling of user input (empty strings, special characters).
- **Parsing text output**: If not using `format="text"`, students might struggle to display the weather data nicely.

### Support Tips
- Suggest using `format="text"` for easy display in a simple dashboard.
- Remind students to check if the result is an error message using `isinstance()` and `startswith()`.
- Encourage good input validation (removing extra spaces, handling empty input).
- For advanced students, suggest using JSON format and accessing specific weather properties.

## Extension Activities Guidance

### Enhanced Weather Dashboard

Key features to look for:
- Color coding (using ANSI color codes or a package like `colorama`)
- Comparison functionality to identify warmest/coldest cities
- Interactive elements (user choice of view options)

Example implementation highlights:
```python
# Color coding example
from colorama import Fore, Style

# Function to get color based on temperature
def get_temp_color(temp):
    if temp < 0:
        return Fore.BLUE
    elif temp < 10:
        return Fore.CYAN
    elif temp < 20:
        return Fore.GREEN
    elif temp < 30:
        return Fore.YELLOW
    else:
        return Fore.RED

# Extract temperature and add color
current_temp = int(current['temp_C'])
colored_temp = f"{get_temp_color(current_temp)}{current_temp}°C{Style.RESET_ALL}"
```

### Weather-Based Recommendations

Example implementation approach:
```python
def suggest_activities(weather_data):
    # Extract current conditions
    current = weather_data.current_condition[0]
    temp = float(current.temp_C)
    weather_desc = current.weatherDesc[0].value.lower()
    
    # Outdoor activities
    if temp > 20 and "sun" in weather_desc:
        print("Perfect day for a picnic or hiking!")
    elif "rain" in weather_desc or "shower" in weather_desc:
        print("Indoor day! How about visiting a museum or watching a movie?")
    elif temp < 5:
        print("Very cold today. Stay warm with some indoor activities.")
    # More conditions...
```

## Reflection Questions - Sample Responses

### How did fetch-my-weather make it easier to work with weather data?
*Sample response:* "The fetch-my-weather package simplified access to weather data by handling the complexities of API requests, error handling, and data formatting. It allows beginners to focus on using the data rather than worrying about HTTP requests, status codes, and JSON parsing."

### Value of pseudocode planning:
*Sample response:* "Pseudocode planning helped organize the logical flow of the program before implementation, making the actual coding process smoother. It forced me to think through the necessary steps and potential issues before encountering them in code."

### Learning with LLM assistance:
*Sample response:* "The LLM helped explain complex concepts in simpler terms and provided targeted examples for specific questions. It was particularly helpful in explaining the structure of the returned weather data and suggesting ways to handle different formats."

### Future API interests:
*Sample response:* "After working with weather data, I'm interested in exploring APIs for news, financial data, or social media. I'd also like to learn about APIs that require authentication to access more personalized or restricted data."

## Additional Teaching Tips

1. **Vocabulary Building**: Help students become comfortable with API terminology by consistently using terms like "endpoint," "request," "response," and "parameters."

2. **Visual Explanations**: Use diagrams to show how data flows from the API to their program. A simple flowchart can help visual learners understand the process.

3. **Real-World Connections**: Discuss how APIs are used in mobile apps, websites, and other software students use daily.

4. **Debugging Strategy**: Teach the strategy of printing intermediate results to understand what data is being returned at each step.

5. **Promote Exploration**: Encourage students to experiment with different parameters and locations to see how the output changes.

6. **Error Message Analysis**: Help students understand how to interpret error messages and use them to debug their code.
