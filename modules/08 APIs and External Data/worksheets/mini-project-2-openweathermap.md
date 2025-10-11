---
title: "Worksheet 2: Advanced API Techniques and Authentication"
subtitle: Direct API Requests and Working with API Keys
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
- Make direct HTTP requests to web APIs using the requests library
- Understand and parse JSON data from API responses
- Implement basic error checking for API calls
- Work with authenticated APIs using API keys
- Apply security best practices for handling API credentials

## Introduction
In Worksheet 1, we used the fetch-my-weather package to simplify accessing weather data. Now, we'll go "under the hood" to understand how APIs work directly. We'll also learn how to use APIs that require authentication with API keys, a common requirement for many professional services.

This worksheet builds on the foundational knowledge from Worksheet 1, taking you from using a simplified package to understanding the underlying mechanics of API requests.

## Key Concepts
- **HTTP Request:** A message sent to a server to retrieve or send data.
- **JSON (JavaScript Object Notation):** A standard data format used by most modern APIs.
- **API Key:** A unique identifier used to authenticate requests to an API.
- **Environment Variables:** A secure way to store sensitive information like API keys.
- **Status Codes:** Numeric codes that indicate the result of an HTTP request (e.g., 200 for success, 404 for not found).

## Activities

### Activity 1: Direct API Requests to wttr.in

First, let's see what happens "under the hood" by using the requests library to directly access the wttr.in API that fetch-my-weather is built on.

**Step 1:** Make a direct request to the wttr.in API.

```python
import requests

def get_weather_direct(location):
    # Construct the URL for the wttr.in API
    url = f'https://wttr.in/{location}?format=3'
    
    # Make the request
    response = requests.get(url)
    
    # Check if the request was successful using status code
    if response.status_code == 200:
        # Return the text content of the response
        return response.text
    else:
        return f"Failed to fetch data: Status code {response.status_code}"

# Test the function
city = "London"
weather = get_weather_direct(city)
print(weather)
```

**Step 2:** Access the JSON format for more structured data.

```python
import requests

def get_weather_json(location):
    # Request the weather data in JSON format
    url = f'https://wttr.in/{location}?format=j1'
    
    # Make the request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        weather_data = response.json()
        
        # Check if the expected data is present
        if 'current_condition' in weather_data and weather_data['current_condition']:
            # Extract and display key information
            current = weather_data['current_condition'][0]
            current_temp = current['temp_C']
            weather_desc = current['weatherDesc'][0]['value']
            humidity = current['humidity']
            
            print(f"Weather in {location}:")
            print(f"Temperature: {current_temp}°C")
            print(f"Conditions: {weather_desc}")
            print(f"Humidity: {humidity}%")
            
            return weather_data
        else:
            print("Weather data has an unexpected format.")
            return None
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")
        return None

# Test the function
city = "Paris"
weather_data = get_weather_json(city)
```

**Step 3:** Adding basic error checking.

```python
import requests

def get_weather_with_error_checking(location):
    # Construct the URL for the wttr.in API
    url = f'https://wttr.in/{location}?format=j1'
    
    # Add a user agent to be respectful to the API provider
    headers = {
        'User-Agent': 'Learning Python Weather App'
    }
    
    # Make the request with headers
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful using status code
    if response.status_code == 200:
        # Try to parse the JSON response
        try:
            weather_data = response.json()
            
            # Check if the expected data is present
            if 'current_condition' in weather_data and weather_data['current_condition']:
                return weather_data
            else:
                return "Error: Weather data has an unexpected format."
        except ValueError:
            return "Error: Could not parse JSON response."
    else:
        return f"Error: Failed to fetch data. Status code {response.status_code}"

# Test with a valid location
valid_result = get_weather_with_error_checking("Tokyo")
if isinstance(valid_result, dict):
    print("Successfully retrieved weather data for Tokyo")
    
# Test with an invalid location
invalid_result = get_weather_with_error_checking("NonExistentPlace12345")
if isinstance(invalid_result, str) and invalid_result.startswith("Error:"):
    print(invalid_result)
```

::: {.callout-note}
**Looking Ahead:** In future modules, you'll learn about more advanced error handling using Python's try/except blocks. This approach allows for more robust handling of unexpected situations, including network errors, JSON parsing issues, and other exceptions that may occur. For advanced students interested in exploring this concept early, research "Python exception handling" and "try except blocks" to get a head start!
:::

### Activity 2: Compare Package vs. Direct Requests

Now that you've used both a third-party package (fetch-my-weather) and direct API requests, let's compare the two approaches:

```python
import time
import fetch_my_weather
import requests

def measure_performance():
    city = "London"
    
    # Measure time for fetch-my-weather
    start_time = time.time()
    fetch_my_weather.get_weather(location=city)
    package_time = time.time() - start_time
    
    # Measure time for direct request
    start_time = time.time()
    requests.get(f'https://wttr.in/{city}?format=j1')
    direct_request_time = time.time() - start_time
    
    print(f"Time with fetch-my-weather: {package_time:.4f} seconds")
    print(f"Time with direct requests: {direct_request_time:.4f} seconds")
    
    # Analyze the differences
    print("\nComparison of approaches:")
    print("1. fetch-my-weather advantages:")
    print("   - Easier to use with simpler function calls")
    print("   - Built-in error handling (no exceptions)")
    print("   - Includes automatic caching to reduce API calls")
    print("   - Provides consistent output format")
    
    print("\n2. Direct requests advantages:")
    print("   - More control over the exact request parameters")
    print("   - Access to raw response data")
    print("   - Better understanding of the underlying process")
    print("   - No additional dependencies beyond requests")

# Run the comparison
measure_performance()
```

### Activity 3: Understanding API Authentication

Many APIs require authentication to:
1. Identify who is making the request
2. Control access to data
3. Limit the number of requests (rate limiting)
4. Track usage for billing purposes

Let's learn about API keys and how to use them securely.

#### API Keys and Security Best Practices

API keys are sensitive credentials that should be protected:

- **Never hardcode API keys in your source code**
- **Never commit API keys to version control systems like Git**
- **Use environment variables** to store API keys
- Consider using dedicated secrets management tools for production systems

**Example of poor security practice:**
```python
# DON'T DO THIS
api_key = "1234567890abcdef"
response = requests.get(f"https://api.example.com/data?key={api_key}")
```

**Better approach:**
```python
# DO THIS INSTEAD
import os
from dotenv import load_dotenv

# Load API key from .env file (which is NOT committed to Git)
load_dotenv()
api_key = os.environ.get("WEATHER_API_KEY")

response = requests.get(f"https://api.example.com/data?key={api_key}")
```

#### Setting Up a `.env` File
1. Create a file named `.env` in your project directory
2. Add your API keys in the format: `VARIABLE_NAME=value`
3. Add `.env` to your `.gitignore` file to prevent it from being committed

**Example `.env` file:**
```
OPENWEATHERMAP_API_KEY=your_api_key_here
```

**Example `.gitignore` file:**
```
.env
__pycache__/
*.pyc
```

### Activity 4: Using OpenWeatherMap API with Authentication

Now let's apply what we've learned to access the OpenWeatherMap API, which requires an API key.

**Step 1:** Sign up for a free OpenWeatherMap API key:
1. Visit [OpenWeatherMap](https://openweathermap.org/api) and sign up for a free account
2. Retrieve your API key from your account dashboard

**Step 2:** Create a `.env` file to store your API key securely.

**Step 3:** Use the OpenWeatherMap API with your key:

```python
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
api_key = os.environ.get("OPENWEATHERMAP_API_KEY")

if not api_key:
    print("Error: No API key found. Please set the OPENWEATHERMAP_API_KEY environment variable.")
    exit(1)

def get_weather_openweathermap(city):
    # API endpoint for current weather
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    # Make the request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if the expected data is present
        if 'main' in data and 'weather' in data and data['weather']:
            # Extract relevant weather information
            temp = data['main']['temp']
            weather_desc = data['weather'][0]['description']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            
            print(f"Weather in {city}:")
            print(f"Temperature: {temp}°C")
            print(f"Conditions: {weather_desc}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            
            return data
        else:
            print("Weather data has an unexpected format.")
            return None
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")
        if response.status_code == 401:
            print("This might be due to an invalid API key.")
        elif response.status_code == 404:
            print(f"City '{city}' not found.")
        return None

# Get city from user
city = input("Enter a city name: ")
weather_data = get_weather_openweathermap(city)
```

**Step 4:** Explore the API documentation to find other endpoints and parameters:
1. Look at the [OpenWeatherMap API documentation](https://openweathermap.org/api)
2. Find at least one other endpoint or parameter you can add to your request
3. Modify your code to use this new feature

## Extension Activities

### Extension 1: Weather Forecast with OpenWeatherMap

Extend your code to fetch a 5-day forecast instead of just the current weather.

```python
# Write your forecast code here using the OpenWeatherMap forecast endpoint
```

### Extension 2: Compare Data from Multiple Weather APIs

Create a script that compares weather data from both wttr.in and OpenWeatherMap for the same location.

```python
# Write your comparison code here
```

### Extension 3: Create a Weather Dashboard with Data from OpenWeatherMap

Build a more detailed weather dashboard that uses data from OpenWeatherMap.

```python
# Write your dashboard code here
```

## Reflection
Consider how the direct API approach differs from using a package:

- What challenges did you encounter when working directly with APIs?
- How does the OpenWeatherMap API differ from wttr.in in terms of data structure?
- Why is it important to secure API keys, and what methods did you learn to do this?
- What advantages does each approach (package vs. direct) offer for different situations?

*Your response:*
```markdown
# Your reflection here
- Challenges of direct API work:
- Comparison of API data structures:
- Thoughts on API security practices:
- Advantages of different approaches:
```

This worksheet has introduced you to more advanced API concepts, including direct requests and authentication. These skills form the foundation for working with a wide range of APIs in your future projects.
