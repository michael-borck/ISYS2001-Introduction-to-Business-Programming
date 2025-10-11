---
title: "Fetching Data from the OpenWeatherMap API"
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

## Objectives
- Understand what APIs are and why they're useful
- Learn how to fetch weather data using the OpenWeatherMap API
- Understand how to handle API responses and errors
- Save fetched data to a CSV file
- Perform basic data manipulation and visualisation with weather data
- Learn about API rate limits and best practices

## Introduction to APIs and OpenWeatherMap

### What are APIs?
API stands for Application Programming Interface. It's a set of rules and
protocols that allow different software applications to communicate with each
other. APIs enable developers to access specific features or data from other
services or applications without needing to understand their internal workings.

### Why are APIs useful?
1. **Data Access**: APIs allow access to valuable data from external sources.
2. **Functionality**: They enable the use of pre-built functionalities, saving
   development time.
3. **Integration**: APIs facilitate easy integration between different systems
   and services.
4. **Scalability**: They allow applications to scale by leveraging external
   services.

### Introduction to OpenWeatherMap API
The OpenWeatherMap API provides weather data for various locations worldwide.
It's a great example of how APIs can provide valuable data for applications.

## Introduction to OpenWeatherMap API
The OpenWeatherMap API provides weather data for various locations. You need to
sign up and get an API key to access the data.

### Steps to Get API Key
1. Go to [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and sign up for an account.
2. After signing up, navigate to the API keys section and generate a new API key.
3. Keep this API key safe, as you will need it to make API requests.

> Note: Once you have your API key, it can take between 15-20 mins to become active

## 2. Fetching Weather Data
We'll use the `requests` library to fetch weather data from the OpenWeatherMap API.

### Import Required Libraries
```python
import requests
import pandas as pd  # We needed this later, lets import it now
```


### Fetch some Data
Lets fetch some data..  Replace `'your_api_key_here'` with your actual API key and fetch data for a sample location.

```python
# Setup important variables
api_key = 'your_api_key_here'
location = 'Perth'

# Make request to website endpoint
url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
response = requests.get(url)

# Print response
response
```

> Note: A response code of 200 means the request was successful. Other codes, like 404 (not found) or 401 (unauthorised), indicate various errors.

What happens if the location does not exist, try a location that does not exist.  

Try:
```python
location='ABCDEFG'
```

```python
# Either modify the above cell or add code with incorrect location here
```


### Define Function to Fetch Weather Data
Let's create a function to fetch weather data for a specific location.

Why are we putting this into a function?

```python
def fetch_weather_data(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data: {response.status_code}")
        return None
```


Let us use the new function.  We will look at API key security soon, but for now lets replace `'your_api_key_here'` with your actual API key and fetch data for a sample location.

```python
api_key = 'your_api_key_here'
location = 'Perth'
data = fetch_weather_data(api_key, location)
data
```

## 3. Parsing and Displaying Data
The data returned form an API call is in JSON format.  The requests library will convert this to Python dictionary for us but
we don't need all the information.  The process of extracting just the relevant details, is often called parsing. We'll parse the JSON response and extract relevant information.  As we might want to do this often, lets put this into a function.

```python
def parse_weather_data(data):
    if data:
        weather = {
            "Location": data["name"],
            "Temperature (K)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"]
        }
        return weather
    else:
        return None

api_key = 'your_api_key_here'
location = 'Perth'
data = fetch_weather_data(api_key, location)
parsed_data = parse_weather_data(data)
parsed_data
```


## Saving Data to a CSV File
We use pandas library for most of of data handling. Lets save the fetched data to a CSV file using pandas.

### Convert Data to DataFrame
```python
def save_to_csv(data, filename):
    df = pd.DataFrame([data])
    df.to_csv(filename, index=False)

save_to_csv(parsed_data, 'data/raw/weather_data.csv')
```

# Read and Display the CSV File
```python
df = pd.read_csv('data/raw/weather_data.csv')
df
```

## 5. Error Handling
It's important to handle errors that may occur during API requests. We've
already added basic error handling in the `fetch_weather_data` function. Let's
test it with an invalid location.

### Test Error Handling
```python
invalid_location = 'InvalidCity'
invalid_data = fetch_weather_data(api_key, invalid_location)
invalid_data
```

## Data Manipulation and Visualisation

Let's perform some basic data manipulation and create a simple visualisation.

```python
# Fetch data for multiple cities
cities = ['New York', 'London', 'Tokyo', 'Sydney', 'Moscow']
weather_data = []

for city in cities:
    data = fetch_weather_data(api_key, city)
    if data:
        weather_data.append(parse_weather_data(data))

# Create a DataFrame
df = pd.DataFrame(weather_data)

# Convert temperature from Kelvin to Celsius
df['Temperature (C)'] = df['Temperature (K)'] - 273.15

# Create a bar plot of temperatures
plt.figure(figsize=(10, 6))
plt.bar(df['Location'], df['Temperature (C)'])
plt.title('Temperature Comparison Across Cities')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Display humidity levels
print(df[['Location', 'Humidity (%)']])
```

## API Rate Limits and Best Practices

When working with APIs, it's crucial to be aware of rate limits and follow best
practices:

1. **Check the documentation**: Always review the API documentation for rate
   limits. OpenWeatherMap has different limits based on your subscription level.

2. **Implement rate limiting**: In your code, implement delays between requests
   to avoid hitting rate limits.

3. **Cache responses**: For data that doesn't change frequently, consider
   caching responses to reduce the number of API calls.

4. **Use bulk requests when possible**: Some APIs offer bulk data retrieval. Use
   these features when available to minimise the number of requests.

5. **Handle errors gracefully**: Implement proper error handling, especially for
   rate limit errors (usually HTTP 429 status code).

Example of implementing a simple delay:

```python
import time

def fetch_weather_data_with_delay(api_key, location, delay=1):
    data = fetch_weather_data(api_key, location)
    time.sleep(delay)  # Wait for 1 second before the next request
    return data

# Usage
for city in cities:
    data = fetch_weather_data_with_delay(api_key, city)
    # Process data...
```

Remember, respecting API rate limits is not just about avoiding errors - it's
about being a good API citizen and ensuring fair usage for all users.

## Secure API Key Management

# Method 1: Using a Secrets File (`api_key.txt`)

- **Advantages:**
  - Keeps API keys separate from your code.
  - Easy to manage and update without altering the codebase.

- **Disadvantages:**
  - Requires handling the file securely.
  - Must ensure the file is not uploaded to public repositories.

```python
# Make sure you have upload api_key.txt to the Colab folder.
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()
```

# Method 2: Prompting the User to Enter the API Key

- **Advantages:**
  - No need to store the API key in a file.
  - Reduces the risk of accidental exposure through file sharing.

- **Disadvantages:**
  - Requires manual entry each time the notebook is run.
  - Less convenient for repetitive tasks.

```python
# Get the API key from user input
api_key = input("Enter your OpenWeatherMap API key: ")
```

Lets create a function to manage the API key, if the file exists, try to extract
the key, otherwise prompt the user for the key.

```python
# Function to get the API key securely
def get_api_key():
    """
    Reads the API key from a file or prompts the user to input it.
    """
    try:
        with open('api_key.txt', 'r') as file:
            api_key = file.read().strip()
    except FileNotFoundError:
        api_key = input("Enter your OpenWeatherMap API key: ")
    return api_key
```

## Building a Simple Weather App with Plot
Using the functions you have created above, code from the lecture notes, and
seek help from GenAI if needed implement the following program.

1. **Get API Key:** Use best practice for eky management
2. **Get User Input:** Ask for a city name
3. **Make API Request:** Fetch current weather forecast
4. **Extract Dates and Temps:** Extract 4-hourly temps for each day
5. **Calculate Average Temp:** For each day, find the average temp
6. **Display/Plot Results:** Show average temperature plot

```python
```