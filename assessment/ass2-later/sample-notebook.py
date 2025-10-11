def generate_weather_response(parsed_question, weather_data):
    """
    Generate a natural language response to a weather question
    
    Args:
        parsed_question (dict): Parsed question data
        weather_data (dict): Weather data
        
    Returns:
        str: Natural language response
    """
    if not weather_data:
        return f"I'm sorry, I couldn't retrieve weather data for {parsed_question.get('location', 'that location')}."
    
    # Extract relevant information
    location = weather_data['location']
    attribute = parsed_question['weather_attribute']
    time_period = parsed_question['time_period']
    
    # Get appropriate weather data based on time period
    if time_period == "today":
        # Current conditions
        temp = weather_data['current']['temperature']['current']
        condition = weather_data['current']['condition']['text']
        feels_like = weather_data['current']['temperature']['feels_like']
        
        # Generate response based on attribute
        if attribute == "temperature":
            return f"The current temperature in {location} is {temp}°C, but it feels like {feels_like}°C."
        
        elif attribute == "rain":
            if "rain" in condition.lower():
                return f"Yes, it's currently raining in {location}. The condition is {condition}."
            else:
                return f"No, it's not currently raining in {location}. The condition is {condition}."
        
        elif attribute == "clothing":
            if temp < 10:
                return f"In {location} it's quite cold at {temp}°C. You should wear a warm coat and layers."
            elif temp < 18:
                return f"It's {temp}°C in {location}, so I'd recommend a jacket or sweater."
            elif temp < 25:
                return f"The weather is pleasant in {location} at {temp}°C. A light sweater might be good if it gets cooler."
            else:
                return f"It's warm in {location} at {temp}°C. Light clothing should be fine."
        
        else:  # general
            return f"Currently in {location}, it's {temp}°C with {condition}."
    
    elif time_period == "tomorrow":
        # Tomorrow's forecast
        if len(weather_data['forecast']) > 0:
            forecast = weather_data['forecast'][0]
            max_temp = forecast['temperature']['max']
            min_temp = forecast['temperature']['min']
            condition = forecast['condition']['text']
            rain_chance = forecast['precipitation']['chance']
            
            if attribute == "temperature":
                return f"Tomorrow in {location}, expect temperatures between {min_temp}°C and {max_temp}°C."
            
            elif attribute == "rain":
                if rain_chance > 50:
                    return f"Yes, there's a good chance of rain tomorrow in {location} ({rain_chance}% probability)."
                elif rain_chance > 20:
                    return f"There's a slight chance of rain tomorrow in {location} ({rain_chance}% probability)."
                else:
                    return f"Rain is unlikely in {location} tomorrow (only {rain_chance}% chance)."
            
            elif attribute == "clothing":
                avg_temp = (max_temp + min_temp) / 2
                if avg_temp < 10:
                    advice = "a warm coat and layers"
                elif avg_temp < 18:
                    advice = "a jacket or sweater"
                elif avg_temp < 25:
                    advice = "light layers that you can adjust throughout the day"
                else:
                    advice = "light clothing"
                
                if rain_chance > 30:
                    advice += " and you might want an umbrella as there's a chance of rain"
                
                return f"For tomorrow in {location}, I'd recommend {advice}."
            
            else:  # general
                return f"Tomorrow in {location}, expect {condition} with temperatures between {min_temp}°C and {max_temp}°C."
        else:
            return f"I don't have tomorrow's forecast for {location}."
    
    else:  # other time periods
        return f"I can tell you about the weather in {location} today or tomorrow, but not for {time_period} yet."

# Test response generation
test_question = "Will it rain tomorrow in Sydney?"
parsed = parse_weather_question(test_question)
response = generate_weather_response(parsed, test_weather)
print(f"Question: {test_question}")
print(f"Response: {response}")

# Another test
test_question2 = "Should I wear a jacket in Sydney today?"
parsed2 = parse_weather_question(test_question2)
response2 = generate_weather_response(parsed2, test_weather)
print(f"\nQuestion: {test_question2}")
print(f"Response: {response2}")

## User Interface

# @title Main Application Interface
def weather_advisor():
    """Main function for the Weather Advisor application"""
    # Clear output and show welcome message
    clear_output()
    print("=" * 50)
    print("Welcome to the Weather Advisor!")
    print("=" * 50)
    print("This application can provide weather information and answer")
    print("your weather-related questions in natural language.")
    print()
    
    # Initialize application state
    current_location = None
    weather_data = None
    
    while True:
        # Main menu
        print("\nWhat would you like to do?")
        choice = pyip.inputMenu([
            "Get current weather",
            "View weather forecast",
            "Ask a weather question",
            "Change location",
            "Exit"
        ], numbered=True)
        
        # Process choice
        if choice == "Exit":
            print("\nThank you for using Weather Advisor. Goodbye!")
            break
            
        elif choice == "Change location":
            current_location = pyip.inputStr("Enter a city or location: ")
            print(f"Fetching weather data for {current_location}...")
            weather_data = get_weather_data(current_location)
            
            if weather_data:
                print(f"Weather data updated for {weather_data['location']}.")
            else:
                print(f"Could not retrieve weather data for {current_location}.")
                current_location = None
        
        elif choice == "Get current weather":
            # Make sure we have a location
            if not current_location:
                current_location = pyip.inputStr("Enter a city or location: ")
                print(f"Fetching weather data for {current_location}...")
                weather_data = get_weather_data(current_location)
            
            # Display current weather
            if weather_data:
                display_current_weather(weather_data)
            else:
                print(f"Could not retrieve weather data for {current_location}.")
        
        elif choice == "View weather forecast":
            # Make sure we have a location
            if not current_location:
                current_location = pyip.inputStr("Enter a city or location: ")
                print(f"Fetching weather data for {current_location}...")
                weather_data = get_weather_data(current_location)
            
            # Display forecast
            if weather_data:
                display_forecast(weather_data)
            else:
                print(f"Could not retrieve weather data for {current_location}.")
        
        elif choice == "Ask a weather question":
            # Get the question
            question = pyip.inputStr("What would you like to know about the weather? ")
            
            # Parse the question
            parsed = parse_weather_question(question)
            
            # If no location in question, use current or ask
            if not parsed["location"]:
                if current_location:
                    parsed["location"] = current_location
                else:
                    parsed["location"] = pyip.inputStr("For which city or location? ")
                    current_location = parsed["location"]
            else:
                current_location = parsed["location"]
            
            # Get weather data if needed
            if not weather_data or weather_data["location"].lower() != parsed["location"].lower():
                print(f"Fetching weather data for {parsed['location']}...")
                weather_data = get_weather_data(parsed["location"])
            
            # Generate and display response
            if weather_data:
                response = generate_weather_response(parsed, weather_data)
                print(f"\nAnswer: {response}")
            else:
                print(f"Could not retrieve weather data for {parsed['location']}.")

def display_current_weather(weather_data):
    """Display current weather conditions nicely"""
    current = weather_data["current"]
    
    # Create a nicely formatted display
    print("\n" + "=" * 50)
    print(f"Current Weather for {weather_data['location']}")
    print("=" * 50)
    print(f"Temperature: {current['temperature']['current']}°C (Feels like: {current['temperature']['feels_like']}°C)")
    print(f"Condition: {current['condition']['text']}")
    print(f"Wind: {current['wind']['speed']} km/h from {current['wind']['direction']}")
    print(f"Humidity: {current['humidity']}%")
    print(f"Precipitation: {current['precipitation']['value']} mm")
    print("=" * 50)

def display_forecast(weather_data):
    """Display weather forecast with visualizations"""
    print("\n" + "=" * 50)
    print(f"Weather Forecast for {weather_data['location']}")
    print("=" * 50)
    
    # Show text forecast
    for i, day in enumerate(weather_data["forecast"]):
        if i == 0:
            day_name = "Tomorrow"
        else:
            day_name = day["date"]
        
        print(f"\n{day_name}:")
        print(f"  Temperature: {day['temperature']['min']}°C to {day['temperature']['max']}°C")
        print(f"  Condition: {day['condition']['text']}")
        print(f"  Rain Chance: {day['precipitation']['chance']}%")
    
    print("\nGenerating visualizations...")
    
    # Show visualizations
    plot_temperature_forecast(weather_data)
    plot_precipitation_chance(weather_data)

# Run the main application
# Uncomment the line below to run the application
# weather_advisor()

## Putting It All Together

# @title Run the Weather Advisor Application
# Execute this cell to run the application
weather_advisor()# Weather Advisor: AI-Assisted Python Project

This notebook implements a weather advisor application that combines weather data retrieval with natural language processing to answer weather-related questions.

## Setup and Configuration

# @title Setup and Imports
# Import necessary libraries
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import pyinputplus as pyip
from datetime import datetime, timedelta
import json
import re
from IPython.display import display, HTML, clear_output

# Optional: Install any required packages (uncomment if needed)
# !pip install pyinputplus
# !pip install hands-on-ai

# Set up plotting
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

print("Setup complete!")

## Weather Data Retrieval

# @title Weather Data Functions
def get_weather_data(location, forecast_days=5):
    """
    Retrieve weather data for a location
    
    Args:
        location (str): City or location name
        forecast_days (int): Number of days to forecast (1-5)
        
    Returns:
        dict: Weather data including current conditions and forecast
    """
    # Clean up the location string
    location = location.strip().replace(" ", "+")
    
    try:
        # Make request to wttr.in API
        url = f"https://wttr.in/{location}?format=j1"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract and structure the data
        result = {
            "location": location.replace("+", " "),
            "current": extract_current_weather(data),
            "forecast": extract_forecast(data, forecast_days)
        }
        
        return result
        
    except Exception as e:
        # Handle errors
        print(f"Error retrieving weather data: {e}")
        return None

def extract_current_weather(data):
    """Extract current weather from API response"""
    current = data["current_condition"][0]
    
    return {
        "temperature": {
            "current": int(current["temp_C"]),
            "feels_like": int(current["FeelsLikeC"]),
            "unit": "celsius"
        },
        "condition": {
            "text": current["weatherDesc"][0]["value"],
            "code": current["weatherCode"]
        },
        "wind": {
            "speed": int(current["windspeedKmph"]),
            "direction": current["winddir16Point"],
            "unit": "kmh"
        },
        "humidity": int(current["humidity"]),
        "precipitation": {
            "value": float(current["precipMM"]),
            "unit": "mm"
        },
        "cloud_cover": int(current["cloudcover"])
    }

def extract_forecast(data, days=5):
    """Extract forecast data from API response"""
    forecast_days = []
    
    for i in range(min(days, len(data["weather"]))):
        day_data = data["weather"][i]
        
        # Process each day
        day = {
            "date": day_data["date"],
            "temperature": {
                "max": int(day_data["maxtempC"]),
                "min": int(day_data["mintempC"]),
                "unit": "celsius"
            },
            "condition": {
                "text": day_data["hourly"][4]["weatherDesc"][0]["value"],  # Mid-day condition
                "code": day_data["hourly"][4]["weatherCode"]
            },
            "precipitation": {
                "chance": int(day_data["hourly"][4]["chanceofrain"]),
                "amount": float(day_data["hourly"][4]["precipMM"]),
                "unit": "mm"
            }
        }
        
        forecast_days.append(day)
    
    return forecast_days

# Test weather retrieval
test_weather = get_weather_data("Sydney")
if test_weather:
    print(f"Retrieved weather data for {test_weather['location']}")
    print(f"Current temperature: {test_weather['current']['temperature']['current']}°C")
    print(f"Current conditions: {test_weather['current']['condition']['text']}")
else:
    print("Unable to retrieve weather data for testing.")

## Data Visualization

# @title Weather Visualization Functions
def plot_temperature_forecast(weather_data):
    """Create a line plot of temperature forecast"""
    if not weather_data or "forecast" not in weather_data:
        print("No forecast data available")
        return
    
    # Extract data
    dates = [day["date"] for day in weather_data["forecast"]]
    max_temps = [day["temperature"]["max"] for day in weather_data["forecast"]]
    min_temps = [day["temperature"]["min"] for day in weather_data["forecast"]]
    
    # Create DataFrame
    df = pd.DataFrame({
        "Date": dates,
        "Maximum": max_temps,
        "Minimum": min_temps
    })
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(df["Date"], df["Maximum"], marker='o', linewidth=2, label="Maximum", color="#FF5733")
    plt.plot(df["Date"], df["Minimum"], marker='o', linewidth=2, label="Minimum", color="#33A1FF")
    
    # Add labels and title
    plt.title(f"Temperature Forecast for {weather_data['location']}", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Temperature (°C)", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Customize appearance
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Display
    plt.show()

def plot_precipitation_chance(weather_data):
    """Create a bar chart of precipitation chance"""
    if not weather_data or "forecast" not in weather_data:
        print("No forecast data available")
        return
    
    # Extract data
    dates = [day["date"] for day in weather_data["forecast"]]
    precip_chance = [day["precipitation"]["chance"] for day in weather_data["forecast"]]
    
    # Create DataFrame
    df = pd.DataFrame({
        "Date": dates,
        "Precipitation Chance": precip_chance
    })
    
    # Plot
    plt.figure(figsize=(10, 6))
    bars = plt.bar(df["Date"], df["Precipitation Chance"], color="#3498DB")
    
    # Add data labels
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 1,
                 f'{height}%', ha='center', va='bottom')
    
    # Add labels and title
    plt.title(f"Chance of Precipitation for {weather_data['location']}", fontsize=16)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Chance (%)", fontsize=12)
    plt.ylim(0, 100)
    
    # Customize appearance
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Display
    plt.show()

# Test visualization
if test_weather:
    plot_temperature_forecast(test_weather)
    plot_precipitation_chance(test_weather)

## Natural Language Processing

# @title Natural Language Functions
def parse_weather_question(question):
    """
    Parse a weather-related question to extract location, time, and weather attribute
    
    Args:
        question (str): User's weather question
        
    Returns:
        dict: Extracted information
    """
    # Default values
    result = {
        "location": None,
        "time_period": "today",
        "weather_attribute": "general"
    }
    
    # Location extraction (simple approach)
    # Look for location after "in" or "for"
    in_pattern = r'(?:in|for|at)\s+([A-Za-z\s]+)(?:\?|$|\s)'
    in_match = re.search(in_pattern, question)
    if in_match:
        result["location"] = in_match.group(1).strip()
    
    # Time period extraction
    time_mapping = {
        "today": ["today", "now", "current", "currently"],
        "tomorrow": ["tomorrow", "next day"],
        "this weekend": ["weekend", "this weekend", "coming weekend"],
        "this week": ["this week", "coming week"]
    }
    
    for period, keywords in time_mapping.items():
        if any(keyword in question.lower() for keyword in keywords):
            result["time_period"] = period
            break
    
    # Weather attribute extraction
    weather_attributes = {
        "temperature": ["temperature", "temp", "hot", "cold", "warm", "cool", "heat", "degrees"],
        "rain": ["rain", "rainy", "raining", "precipitation", "wet", "umbrella", "downpour", "shower"],
        "wind": ["wind", "windy", "breeze", "gust", "blow"],
        "snow": ["snow", "snowy", "snowfall", "blizzard"],
        "cloud": ["cloud", "cloudy", "overcast", "clear", "sunny"],
        "humidity": ["humid", "humidity", "sticky", "muggy"],
        "clothing": ["wear", "jacket", "coat", "sweater", "umbrella", "raincoat", "sunglasses", "hat", "jumper"]
    }
    
    # Find which weather attributes are mentioned
    for attr, keywords in weather_attributes.items():
        if any(keyword in question.lower() for keyword in keywords):
            result["weather_attribute"] = attr
            break
    
    return result