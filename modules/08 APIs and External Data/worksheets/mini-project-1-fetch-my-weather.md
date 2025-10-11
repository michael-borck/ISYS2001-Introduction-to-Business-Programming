---
title: "Worksheet 1: Introduction to APIs with fetch-my-weather"
subtitle: Learning API Basics with a Beginner-Friendly Package
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

## Learning Objectives
By the end of this worksheet, you will be able to:
- Understand what APIs are and how they provide access to data
- Use the fetch-my-weather package to retrieve weather information
- Work with an LLM to learn a new Python package
- Create a simple weather dashboard using API data
- Understand the basics of pseudocode and program planning

## Introduction
Web APIs are a foundational element of modern applications, providing a pathway to access data programmatically. In this activity, you'll learn how to fetch and display weather data using a beginner-friendly package called fetch-my-weather.

This first worksheet focuses on the basics of working with APIs through a simplified interface. In a later worksheet, we'll explore more advanced API concepts like authentication and direct API requests.

## Key Concepts
- **API (Application Programming Interface):** A set of rules that allows one piece of software to interact with another.
- **Weather API:** A service that provides weather data through an API.
- **Python Package:** A collection of modules that simplifies certain tasks.
- **LLM (Large Language Model):** AI systems like ChatGPT or Claude that can help explain concepts and assist with coding.

## Using AI Tools Ethically & Effectively
**Transparency:** Always state the use of AI in your work, detailing how and when you used it.

**Critical Evaluation:** AI outputs need to be critically assessed. They are not always correct and may require contextual adjustments.

**Learning Partner:** Utilise AI to deepen your understanding. For instance, you can ask, "Explain the JSON data structure in simple terms" or "Provide an example of how an API might send data."

## Activities

### Activity 1: Teaching an LLM About fetch-my-weather

First, we'll teach an LLM about the package we'll be using, which is a powerful technique for working with new libraries.

**Step 1:** Choose your preferred LLM (Claude, ChatGPT, etc.) and start a new conversation.

**Step 2:** Upload the fetch-my-weather documentation guide to the LLM.

**Step 3:** Ask the LLM to confirm it understands the package by asking it to summarize the key features.

**Example prompt:**
```
I've just shared documentation about the fetch-my-weather package. Could you:
1. Summarize the key features of this package
2. Explain how error handling works in this package
3. Provide a simple example of how to get weather for London
```

### Activity 2: Using the fetch-my-weather Package

Now let's use the package to fetch some weather data!

**Step 1:** Install the fetch-my-weather package.

```python
# Install the package (uncomment and run this once)
# !pip install fetch-my-weather
```

**Step 2:** Get weather for a specific location.

```python
import fetch_my_weather

# Get weather for London
london_weather = fetch_my_weather.get_weather(location="London")
print(london_weather)
```

**Step 3:** Explore different options and parameters.

```python
# Get weather with compact view (fewer forecast days)
compact_weather = fetch_my_weather.get_weather(location="Paris", view_options="1")
print(compact_weather)

# Get weather in a different language
spanish_weather = fetch_my_weather.get_weather(location="Madrid", lang="es")
print(spanish_weather)

# Get moon phase information
moon_phase = fetch_my_weather.get_weather(is_moon=True)
print(moon_phase)
```

**Step 4:** Check for errors without exception handling.

```python
# Try getting weather for an invalid location
result = fetch_my_weather.get_weather(location="NonExistentPlace12345")

# fetch-my-weather returns error messages as strings instead of raising exceptions
if isinstance(result, str) and result.startswith("Error:"):
    print(f"Something went wrong: {result}")
else:
    print("Weather data retrieved successfully")
```

### Activity 3: Create a Weather Dashboard

Let's create a simple weather dashboard for displaying information about multiple cities.

**Step 1:** First, plan your dashboard using pseudocode. Pseudocode is a way to plan your code without worrying about exact syntax.

```
PSEUDOCODE FOR WEATHER DASHBOARD:

FUNCTION CreateWeatherDashboard:
    Initialize empty list called CityWeatherData
    
    FOR EACH city in CityList:
        Request weather data for city
        IF weather data retrieval successful THEN
            Add weather data to CityWeatherData list
        ELSE
            Display error message for this city
        END IF
    END FOR
    
    Display header "WEATHER DASHBOARD"
    Display current date and time
    
    FOR EACH city in CityWeatherData:
        Display city name and weather information
        Add separator line
    END FOR
END FUNCTION

FUNCTION Main:
    Ask user for cities to check
    Call CreateWeatherDashboard
END FUNCTION
```

**Step 2:** Now implement the dashboard based on your pseudocode.

```python
import fetch_my_weather
from datetime import datetime

def create_weather_dashboard(city_list):
    # Initialize empty list for storing weather data
    city_weather_data = []
    
    # Get weather data for each city
    for city in city_list:
        weather = fetch_my_weather.get_weather(location=city, view_options="0")
        
        # Check if we got valid weather data
        if isinstance(weather, str) and not weather.startswith("Error:"):
            city_weather_data.append({"city": city, "weather": weather})
        else:
            print(f"Could not get weather for {city}")
    
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
city_input = input("Enter cities to check (comma-separated): ")
cities = [city.strip() for city in city_input.split(",")]

# Create the dashboard
create_weather_dashboard(cities)
```

## 🧠 Intentional Prompting for Learning

If you're using an LLM to help with this worksheet, here are some tips for getting the most out of it:

### What Is Intentional Prompting?

**Intentional prompting** means you:
- Ask the AI to **explain** its reasoning, not just give solutions
- Ask questions that lead to deeper understanding of concepts
- Refine and adapt prompts when the first response isn't quite right
- Use the AI as a **thinking partner**, not just a code vending machine

### Examples of Good Prompts

**✅ Good prompt:** 
"I'm learning about the fetch-my-weather package. Could you explain how the caching feature works and why it's useful?"

**✅ Good prompt:** 
"I'm creating a weather dashboard using Python and the fetch-my-weather package. Could you help me understand how I might structure the code to display multiple cities and highlight the warmest one?"

### Your turn: Create an intentional prompt

Try writing your own intentional prompt to ask about something in this worksheet that you'd like to understand better.

*Your response:*
```
# Write your intentional prompt here
```

## Extension Activities

### Extension 1: Enhanced Weather Dashboard

Improve your weather dashboard to include more features:
- Add color coding for temperature ranges
- Display which city is warmest/coldest
- Allow the user to choose between different view options

```python
# Write your enhanced dashboard code here
```

### Extension 2: Weather-Based Recommendations

Create a simple program that recommends activities based on the weather:

```python
import fetch_my_weather

def suggest_activities(weather_data):
    # Add your recommendation logic here
    pass

# Get location from user
city = input("Enter your city: ")
weather = fetch_my_weather.get_weather(location=city)

# Get recommendations
suggest_activities(weather)
```

## Reflection
Consider how you might use what you've learned in your future projects:

- How did the fetch-my-weather package make it easier to work with weather data?
- What was the value of planning with pseudocode before writing the actual code?
- If you used an LLM, how did it help you understand the concepts better?
- What other types of APIs might you want to explore in the future?

*Your response:*
```markdown
# Your reflection here
- Experience with fetch-my-weather:
- Value of pseudocode planning:
- Learning with LLM assistance (if applicable):
- Future API interests:
```

This worksheet provides a gentle introduction to working with APIs through a beginner-friendly package. In the next worksheet, we'll explore making direct API requests and using authenticated APIs.
