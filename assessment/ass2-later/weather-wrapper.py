"""
WeatherWrapper - A simplified interface for weather data

This module provides easy access to weather data from various services
without requiring students to manage API keys or complex request handling.
"""

import os
import requests
import json
import time
from datetime import datetime, timedelta
from functools import lru_cache

class WeatherWrapper:
    """A wrapper class for weather data retrieval"""
    
    def __init__(self, cache_time=1800):
        """
        Initialize the WeatherWrapper
        
        Args:
            cache_time (int): Time in seconds to cache responses (default: 30 minutes)
        """
        self.cache_time = cache_time
        self._cache = {}
        self._last_error = None
        self._service = "wttr"  # Default to wttr.in as it doesn't require API keys
    
    @lru_cache(maxsize=32)
    def get_current_weather(self, location):
        """
        Get current weather conditions for a location
        
        Args:
            location (str): City name or location
            
        Returns:
            dict: Weather data including temperature, conditions, etc.
        """
        # Clean up location string
        location = self._sanitize_location(location)
        
        # Check cache first
        cache_key = f"current_{location}"
        cached = self._check_cache(cache_key)
        if cached:
            return cached
        
        # Retrieve from wttr.in
        try:
            url = f"https://wttr.in/{location}?format=j1"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract relevant information
            result = {
                "location": location,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "temperature": {
                    "current": self._extract_temp(data["current_condition"][0]["temp_C"]),
                    "feels_like": self._extract_temp(data["current_condition"][0]["FeelsLikeC"]),
                    "unit": "celsius"
                },
                "condition": {
                    "text": data["current_condition"][0]["weatherDesc"][0]["value"],
                    "code": data["current_condition"][0]["weatherCode"]
                },
                "wind": {
                    "speed": float(data["current_condition"][0]["windspeedKmph"]),
                    "direction": data["current_condition"][0]["winddir16Point"],
                    "unit": "kmh"
                },
                "humidity": int(data["current_condition"][0]["humidity"]),
                "precipitation": {
                    "value": float(data["current_condition"][0]["precipMM"]),
                    "unit": "mm"
                },
                "cloud_cover": int(data["current_condition"][0]["cloudcover"]),
                "is_day": data["current_condition"][0]["isdaytime"] == "yes"
            }
            
            # Store in cache
            self._update_cache(cache_key, result)
            self._last_error = None
            
            return result
            
        except Exception as e:
            self._last_error = str(e)
            return {"error": str(e), "location": location}
    
    @lru_cache(maxsize=32)
    def get_forecast(self, location, days=5):
        """
        Get weather forecast for a location
        
        Args:
            location (str): City name or location
            days (int): Number of days to forecast (1-5)
            
        Returns:
            dict: Forecast data for the specified number of days
        """
        # Clean up location string
        location = self._sanitize_location(location)
        days = min(5, max(1, days))  # Ensure days is between 1 and 5
        
        # Check cache first
        cache_key = f"forecast_{location}_{days}"
        cached = self._check_cache(cache_key)
        if cached:
            return cached
        
        # Retrieve from wttr.in
        try:
            url = f"https://wttr.in/{location}?format=j1"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            # Extract forecast data
            forecast_days = []
            for i in range(min(days, len(data["weather"]))):
                day_data = data["weather"][i]
                
                # Process each day
                day = {
                    "date": day_data["date"],
                    "astronomy": {
                        "sunrise": day_data["astronomy"][0]["sunrise"],
                        "sunset": day_data["astronomy"][0]["sunset"]
                    },
                    "temperature": {
                        "max": self._extract_temp(day_data["maxtempC"]),
                        "min": self._extract_temp(day_data["mintempC"]),
                        "unit": "celsius"
                    },
                    "condition": {
                        "text": day_data["hourly"][4]["weatherDesc"][0]["value"],  # Mid-day condition
                        "code": day_data["hourly"][4]["weatherCode"]
                    },
                    "wind": {
                        "max_speed": float(day_data["hourly"][4]["windspeedKmph"]),
                        "direction": day_data["hourly"][4]["winddir16Point"],
                        "unit": "kmh"
                    },
                    "humidity": int(day_data["hourly"][4]["humidity"]),
                    "precipitation": {
                        "chance": int(day_data["hourly"][4]["chanceofrain"]),
                        "amount": float(day_data["hourly"][4]["precipMM"]),
                        "unit": "mm"
                    },
                    "cloud_cover": int(day_data["hourly"][4]["cloudcover"]),
                    "hourly": self._extract_hourly(day_data["hourly"])
                }
                
                forecast_days.append(day)
            
            result = {
                "location": location,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "days": forecast_days
            }
            
            # Store in cache
            self._update_cache(cache_key, result)
            self._last_error = None
            
            return result
            
        except Exception as e:
            self._last_error = str(e)
            return {"error": str(e), "location": location}
    
    def convert_temperature(self, value, to_unit="C"):
        """
        Convert temperature between Celsius and Fahrenheit
        
        Args:
            value (float): Temperature value
            to_unit (str): Target unit ('C' or 'F')
            
        Returns:
            float: Converted temperature value
        """
        if to_unit.upper() == "F":
            return (value * 9/5) + 32
        else:
            return (value - 32) * 5/9
    
    def get_last_error(self):
        """Return the last error encountered"""
        return self._last_error
    
    def _sanitize_location(self, location):
        """Clean up location string for API request"""
        return location.strip().replace(" ", "+")
    
    def _extract_temp(self, temp_str):
        """Extract temperature as float from string"""
        try:
            return float(temp_str)
        except:
            return 0.0
    
    def _extract_hourly(self, hourly_data):
        """Extract simplified hourly forecast data"""
        hours = []
        
        for hour in hourly_data:
            # Convert wttr.in's format (3-hour blocks starting from 0) to hour of day
            hour_num = int(hour["time"]) // 100
            
            hour_info = {
                "hour": hour_num,
                "temperature": float(hour["tempC"]),
                "feels_like": float(hour["FeelsLikeC"]),
                "condition": hour["weatherDesc"][0]["value"],
                "precipitation": {
                    "chance": int(hour["chanceofrain"]),
                    "amount": float(hour["precipMM"])
                },
                "wind": {
                    "speed": float(hour["windspeedKmph"]),
                    "direction": hour["winddir16Point"]
                },
                "humidity": int(hour["humidity"])
            }
            
            hours.append(hour_info)
        
        return hours
    
    def _check_cache(self, key):
        """Check if valid data exists in cache"""
        if key in self._cache:
            timestamp, data = self._cache[key]
            if time.time() - timestamp < self.cache_time:
                return data
        return None
    
    def _update_cache(self, key, data):
        """Update cache with new data"""
        self._cache[key] = (time.time(), data)


# Example usage
if __name__ == "__main__":
    weather = WeatherWrapper()
    
    # Get current weather
    current = weather.get_current_weather("London")
    print(f"Current weather in {current['location']}:")
    print(f"Temperature: {current['temperature']['current']}°C")
    print(f"Condition: {current['condition']['text']}")
    
    # Get forecast
    forecast = weather.get_forecast("London", days=3)
    print("\nForecast:")
    for day in forecast["days"]:
        print(f"\n{day['date']}:")
        print(f"  High: {day['temperature']['max']}°C")
        print(f"  Low: {day['temperature']['min']}°C")
        print(f"  Condition: {day['condition']['text']}")
        print(f"  Rain chance: {day['precipitation']['chance']}%")