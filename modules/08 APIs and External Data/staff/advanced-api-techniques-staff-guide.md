---
title: "Staff Answer Guide: Worksheet 2 - Advanced API Techniques and Authentication"
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


This guide provides expected outcomes, common issues, and tips for supporting students as they work through Worksheet 2 on advanced API techniques and authentication with OpenWeatherMap.

## Key Concepts Review

- **HTTP Requests**: Messages sent to servers to retrieve or send data. Students will use the `requests` library to make these directly.
- **JSON**: A standard data format used by most modern APIs that provides structured data.
- **API Keys**: Unique identifiers used to authenticate requests to an API, controlling access and usage limits.
- **Environment Variables**: A secure method for storing sensitive information like API keys.
- **Status Codes**: Numeric codes that indicate the result of an HTTP request (e.g., 200 for success, 404 for not found).

## Activity 1: Direct API Requests to wttr.in

### Expected Code Output Examples

Basic direct request:
```python
import requests

def get_weather_direct(location):
    url = f'https://wttr.in/{location}?format=3'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        return f"Failed to fetch data: Status code {response.status_code}"

# Test output for London might look like:
# "London: ⛅️  +15°C"
```

JSON format request:
```python
def get_weather_json(location):
    url = f'https://wttr.in/{location}?format=j1'
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        
        if 'current_condition' in weather_data and weather_data['current_condition']:
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

# Expected terminal output for Paris:
# Weather in Paris:
# Temperature: 14°C
# Conditions: Partly cloudy
# Humidity: 76%
```

Error checking implementation:
```python
def get_weather_with_error_checking(location):
    url = f'https://wttr.in/{location}?format=j1'
    
    headers = {
        'User-Agent': 'Learning Python Weather App'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            try:
                weather_data = response.json()
                
                if 'current_condition' in weather_data and weather_data['current_condition']:
                    return weather_data
                else:
                    return "Error: Weather data has an unexpected format."
            except ValueError:
                return "Error: Could not parse JSON response."
        else:
            return f"Error: Failed to fetch data. Status code {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: Request failed. {str(e)}"

# Expected output for invalid location:
# "Error: Failed to fetch data. Status code 404"
```

### Common Issues
- **Network errors**: Students may encounter connection issues or timeouts.
- **JSON parsing**: Students might struggle with understanding nested JSON structure.
- **HTTP status codes**: Students may be unfamiliar with common status codes and their meanings.
- **Missing User-Agent header**: Some students might not add a User-Agent header, which can lead to rate limiting.

### Support Tips
- Emphasize the importance of checking `response.status_code` before trying to access response data.
- Recommend using `response.json()` for JSON responses instead of manual parsing.
- Suggest adding timeout parameters to prevent hanging on slow connections.
- Encourage exploring the response data structure with `print(json.dumps(data, indent=2))` for better visualization.
- Explain the purpose of headers, especially User-Agent, in making more professional API requests.

## Activity 2: Compare Package vs. Direct Requests

### Sample Performance Comparison Results
```
Time with fetch-my-weather: 0.7823 seconds
Time with direct requests: 0.6145 seconds

Comparison of approaches:
1. fetch-my-weather advantages:
   - Easier to use with simpler function calls
   - Built-in error handling (no exceptions)
   - Includes automatic caching to reduce API calls
   - Provides consistent output format

2. Direct requests advantages:
   - More control over the exact request parameters
   - Access to raw response data
   - Better understanding of the underlying process
   - No additional dependencies beyond requests
```

### Important Discussion Points
- The performance difference might vary depending on network conditions and whether caching is active.
- Trade-offs between ease-of-use (package) and flexibility/control (direct).
- The value of understanding what happens "under the hood," even when using convenience packages.

## Activity 3: Understanding API Authentication

### Key Teaching Points
- API keys should never be hardcoded in source code.
- API keys should never be committed to version control systems like Git.
- Environment variables provide a secure way to store and access sensitive information.
- The `.env` file should always be added to `.gitignore`.

### Sample `.env` File
```
OPENWEATHERMAP_API_KEY=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

### Sample `.gitignore` File
```
# Environment variables
.env
.env.*

# Python
__pycache__/
*.py[cod]
*$py.class
```

## Activity 4: Using OpenWeatherMap API with Authentication

### Expected Implementation

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
    
    try:
        # Make the request
        response = requests.get(url, timeout=5)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
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
            print(f"Failed to fetch data: Status code {response.status_code}")
            if response.status_code == 401:
                print("This might be due to an invalid API key.")
            elif response.status_code == 404:
                print(f"City '{city}' not found.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {str(e)}")
        return None

# Sample output for London:
# Weather in London:
# Temperature: 12.5°C
# Conditions: light rain
# Humidity: 82%
# Wind Speed: 4.12 m/s
```

### Common Issues
- **API key setup**: Students may struggle with creating and loading the `.env` file correctly.
- **OpenWeatherMap account creation**: Some students may have difficulties signing up or finding their API key.
- **API rate limits**: Students might hit rate limits if making too many requests.
- **Data structure differences**: OpenWeatherMap's JSON structure differs from wttr.in, causing confusion.

### Support Tips
- Provide step-by-step instructions for signing up for OpenWeatherMap and locating the API key.
- Emphasize the need to install the `python-dotenv` package (`pip install python-dotenv`).
- Help students understand the OpenWeatherMap response structure by printing it with `json.dumps(data, indent=2)`.
- Clarify common status codes they might encounter (401 for authentication issues, 404 for city not found).
- Remind students that free OpenWeatherMap accounts have rate limits (60 calls/minute).

## Extension Activities Guidance

### Extension 1: Weather Forecast with OpenWeatherMap

Key features to look for:
- Using the 5-day forecast endpoint (`/forecast`)
- Organizing forecast data by day or time periods
- Providing meaningful summary of forecast trends

Example implementation outline:
```python
def get_forecast_openweathermap(city):
    # 5-day forecast endpoint (returns forecast in 3-hour increments)
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    
    # Make request and check status
    response = requests.get(url)
    if response.status_code != 200:
        return f"Error: {response.status_code}"
    
    data = response.json()
    
    # Group forecast data by day
    forecasts_by_day = {}
    for forecast in data['list']:
        # Extract date from timestamp (format: "2025-04-14")
        date = forecast['dt_txt'].split(' ')[0]
        
        if date not in forecasts_by_day:
            forecasts_by_day[date] = []
        
        forecasts_by_day[date].append(forecast)
    
    # Display forecast by day
    for date, forecasts in forecasts_by_day.items():
        print(f"\nForecast for {date}:")
        
        # Calculate daily averages
        temps = [f['main']['temp'] for f in forecasts]
        avg_temp = sum(temps) / len(temps)
        
        # Get most common weather condition
        conditions = [f['weather'][0]['description'] for f in forecasts]
        # (Implementation of finding most common condition)
        
        print(f"  Average temperature: {avg_temp:.1f}°C")
        print(f"  Conditions: {most_common_condition}")
```

### Extension 2: Compare Data from Multiple Weather APIs

Implementation considerations:
- Creating a function that calls both APIs for the same location
- Highlighting differences in temperature, conditions, and other data points
- Calculating and displaying the variance between services

Example structure:
```python
def compare_weather_apis(city):
    # Get data from wttr.in
    wttr_data = get_weather_json(city)
    
    # Get data from OpenWeatherMap
    openweather_data = get_weather_openweathermap(city)
    
    if wttr_data and openweather_data:
        # Extract key metrics for comparison
        wttr_temp = float(wttr_data['current_condition'][0]['temp_C'])
        ow_temp = openweather_data['main']['temp']
        
        wttr_cond = wttr_data['current_condition'][0]['weatherDesc'][0]['value']
        ow_cond = openweather_data['weather'][0]['description']
        
        # Compare and display differences
        print(f"\nAPI Comparison for {city}:")
        print(f"Temperature:")
        print(f"  wttr.in: {wttr_temp}°C")
        print(f"  OpenWeatherMap: {ow_temp}°C")
        print(f"  Difference: {abs(wttr_temp - ow_temp):.1f}°C")
        
        print(f"Weather Condition:")
        print(f"  wttr.in: {wttr_cond}")
        print(f"  OpenWeatherMap: {ow_cond}")
```

### Extension 3: Create a Weather Dashboard with Data from OpenWeatherMap

Key elements to include:
- Multi-city data display
- Meaningful organization of weather information
- Visual elements (even simple ASCII art or formatting)
- Interactive components (e.g., user can refresh data)

Example dashboard structure:
```python
def create_openweather_dashboard(cities):
    # Display header
    print("\n" + "="*60)
    print(f"OPENWEATHERMAP DASHBOARD - {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*60)
    
    # Track temperature extremes
    warmest_city = {"name": "", "temp": -100}
    coldest_city = {"name": "", "temp": 100}
    
    # Get and display data for each city
    for city in cities:
        data = get_weather_openweathermap(city)
        
        if data:
            # Extract and format key information
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']
            condition = data['weather'][0]['description']
            
            # Update temperature extremes
            if temp > warmest_city["temp"]:
                warmest_city = {"name": city, "temp": temp}
            if temp < coldest_city["temp"]:
                coldest_city = {"name": city, "temp": temp}
            
            # Display city weather with formatting
            print(f"\n{city.upper()}")
            print(f"  Temperature: {temp}°C (Feels like: {feels_like}°C)")
            print(f"  Conditions: {condition}")
            print(f"  Humidity: {humidity}%")
            print(f"  Wind: {wind_speed} m/s")
    
    # Display temperature extremes
    print("\n" + "-"*60)
    print(f"Warmest city: {warmest_city['name']} ({warmest_city['temp']}°C)")
    print(f"Coldest city: {coldest_city['name']} ({coldest_city['temp']}°C)")
```

## Reflection Questions - Sample Responses

### Challenges of direct API work:
*Sample response:* "Working directly with APIs required more detailed understanding of HTTP requests, response handling, and JSON parsing. Error handling became more complex as I needed to account for network errors, invalid responses, and unexpected data structures."

### Comparison of API data structures:
*Sample response:* "The wttr.in API returns more detailed forecast data by default and has a different JSON structure than OpenWeatherMap. OpenWeatherMap separates current weather and forecast into different endpoints, while wttr.in includes both in a single response. OpenWeatherMap's response structure is somewhat simpler but may require more API calls to get the same information."

### Thoughts on API security practices:
*Sample response:* "Securing API keys is crucial to prevent unauthorized usage that could result in rate limiting, billing charges, or data breaches. Using environment variables and .env files provides a good balance of security and convenience, keeping sensitive information out of the codebase while still making it accessible to the application."

### Advantages of different approaches:
*Sample response:* "The package approach is ideal for beginners or when rapid development is needed, as it abstracts away complexity. The direct API approach provides more flexibility, control, and understanding of what's happening behind the scenes. For production applications, direct API requests with proper error handling and customization would be preferable, while for quick prototypes or educational purposes, a package might be more suitable."

## Additional Teaching Tips

1. **API Documentation Exploration**: Encourage students to read the OpenWeatherMap API documentation to discover additional endpoints and parameters they could use.

2. **Status Code Reference**: Provide a quick reference of common HTTP status codes (200, 400, 401, 403, 404, 429, 500) and what they indicate.

3. **JSON Visualization**: Recommend tools like [JSON Formatter & Validator](https://jsonformatter.curiousconcept.com/) for better visualization of API responses.

4. **API Testing Tools**: Introduce students to API testing tools like Postman or Insomnia for exploring APIs before coding.

5. **Rate Limiting Discussion**: Explain rate limiting concepts and how to implement backoff strategies for handling rate limits.

6. **Error Handling Progression**: Show the progression from basic status code checking to more robust try/except patterns for handling various error scenarios.

7. **Security Considerations**: Discuss real-world implications of API key leaks and show examples of automated bots that scan GitHub for exposed API keys.

8. **Advanced Authentication Methods**: For interested students, introduce the concept of OAuth and other more complex authentication methods used by APIs.
