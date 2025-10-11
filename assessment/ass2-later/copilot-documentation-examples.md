# Examples: Documenting GitHub Copilot Interactions

Below are examples showing how students might document their interactions with GitHub Copilot or similar inline coding assistants in a way that demonstrates intentional prompting.

## Example 1: Function Development with Comments as Prompts

```
# Interaction: Creating a Weather Data Retrieval Function
# Date: 2025-04-02

## My Initial Guidance to Copilot
I wrote the following comment to guide Copilot:

```python
# Function to retrieve weather data from wttr.in API
# Parameters:
#   location: string - name of city or location
#   forecast_days: int - number of days to forecast (1-5)
# Returns:
#   dictionary containing current weather and forecast
# Should handle connection errors and invalid inputs
def get_weather_data(
```

## Copilot's Suggestion
Copilot completed the function signature and provided this implementation:

```python
def get_weather_data(location, forecast_days=5):
    """
    Retrieve weather data for a location
    
    Args:
        location (str): City or location name
        forecast_days (int): Number of days to forecast (1-5)
        
    Returns:
        dict: Weather data including current conditions and forecast
    """
    import requests
    
    # Clean up the location string
    location = location.strip().replace(" ", "+")
    
    try:
        # Make request to wttr.in API
        url = f"https://wttr.in/{location}?format=j1"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        # Parse JSON response
        data = response.json()
        
        # Extract and structure the data
        result = {
            "location": location.replace("+", " "),
            "current": {
                "temperature": int(data["current_condition"][0]["temp_C"]),
                "condition": data["current_condition"][0]["weatherDesc"][0]["value"]
            },
            "forecast": []
        }
        
        # Add forecast data
        for i in range(min(forecast_days, len(data["weather"]))):
            day = data["weather"][i]
            result["forecast"].append({
                "date": day["date"],
                "max_temp": int(day["maxtempC"]),
                "min_temp": int(day["mintempC"]),
                "condition": day["hourly"][4]["weatherDesc"][0]["value"]
            })
        
        return result
        
    except Exception as e:
        print(f"Error retrieving weather data: {e}")
        return None
```

## My Evaluation and Refinement
I noticed several issues with the generated code:
1. The error handling just prints the error instead of allowing the caller to handle it
2. The data extraction was too simple and missed important fields
3. No validation of forecast_days parameter

I added this comment to guide refinement:

```python
# Need better error handling - should return error info in the result
# Also need to extract more weather data fields:
# - wind speed and direction
# - humidity
# - precipitation amount and chance
# - validate forecast_days is between 1-5
```

## Copilot's Refined Implementation
Based on my guidance, Copilot updated the function with these improvements:

[Content omitted for brevity - would include the improved function]

## My Final Implementation
After several iterations and testing, here's my final version with additional error handling and comprehensive data extraction:

[Final implementation code would be included here]
```

## Example 2: Manual Documentation of Multi-Step Development

```
# Interaction: Creating a Natural Language Parser for Weather Questions
# Date: 2025-04-03

This interaction happened over several steps as I refined the function with Copilot.

## Step 1: Function Definition

I started by defining the function purpose with a detailed comment:

```python
# Parse a weather question to extract:
# - location (city name)
# - time period (today, tomorrow, this weekend)
# - weather attribute (temperature, rain, clothing recommendation)
# Example inputs:
# - "Will it rain tomorrow in Sydney?"
# - "Do I need a jacket in Paris today?"
# - "What's the temperature in Tokyo this weekend?"
def parse_weather_question(
```

Copilot suggested a basic function structure with regex patterns for location extraction and simple keyword matching.

## Step 2: Improving Location Extraction

I wasn't satisfied with the location extraction, so I added:

```python
# The location extraction needs to be more robust
# Should find location names that follow prepositions like "in", "for", "at"
# Also handle when location is at the beginning: "Sydney weather tomorrow?"
```

Copilot suggested more complex regex patterns and a fallback mechanism.

## Step 3: Adding Time Period Extraction

After testing location extraction, I guided Copilot to improve time parsing:

```python
# Add support for more time expressions:
# - Next Monday, Tuesday, etc.
# - In two days
# - This evening/morning/afternoon
```

Copilot added a more comprehensive time expression detection system.

## Step 4: Final Integration

After several iterations, I integrated all the components and added my own improvements:

[Final code would be shown here]

## Design Decisions and AI Contribution

Throughout this process, I used Copilot as a pair programmer by:
1. Providing detailed comments that served as specifications
2. Breaking down the problem into manageable steps
3. Evaluating and refining each suggestion
4. Adding my own improvements when Copilot's suggestions weren't optimal

The most valuable aspect was how Copilot helped generate regex patterns and provided a starting structure, while I focused on the overall design and edge case handling.
```

## Example 3: Screen Recording Documentation Template

```
# Weather Visualization Development with Copilot
# Date: 2025-04-04

I've submitted a screen recording (visualization_development.mp4) showing my interaction with Copilot to develop the temperature visualization function. 

In the recording (timestamp references included):

## Initial Function Structure (0:00-1:15)
- I started by writing comments describing the visualization requirements
- Demonstrated how I used specific comments to guide Copilot's suggestions
- Showed my evaluation of the initial code suggestion

## Refining the Visualization (1:16-2:45)
- I identified issues with axis labels and color choices
- Added specific comments to guide improvements
- Showed how I merged Copilot's suggestions with my own ideas

## Testing and Final Implementation (2:46-4:30)
- Demonstrated testing with sample data
- Final adjustments to improve readability
- Explained my thought process throughout

## Key Takeaways
The recording demonstrates my intentional prompting approach by showing how I:
1. Used descriptive comments to guide Copilot's suggestions
2. Evaluated and refined suggestions rather than accepting them blindly
3. Broke down the problem into manageable parts
4. Maintained control of the design decisions while leveraging Copilot's coding assistance
```

# Guidance for Documentation Approaches

## Effective Comment-Based Prompting for Copilot

When using GitHub Copilot or similar tools, these strategies help document intentional prompting:

1. **Write descriptive comments before asking for code**:
   ```python
   # Function to parse user weather questions
   # Should extract: location, time period, and weather attribute
   # Handle questions like: "Will it rain in London tomorrow?"
   # Return a dictionary with the extracted information
   ```

2. **Create docstring templates**:
   ```python
   def process_weather_data(data, location):
       """
       Process raw weather data for a location
       
       Args:
           data: The raw weather data from the API
           location: The user's requested location
           
       Returns:
           Processed data with only the relevant information
       """
       # Copilot will suggest implementation here
   ```

3. **Use TODOs to guide implementation**:
   ```python
   def visualize_temperature(weather_data):
       # TODO: Create a line chart of 5-day temperature forecast
       # TODO: Show both high and low temperatures
       # TODO: Add proper labels and a title with the location
       # TODO: Use a color scheme that indicates temperature ranges
   ```

4. **Examples with expected outputs**:
   ```python
   # Example:
   # Input: "Will it rain tomorrow in Sydney?"
   # Output: {"location": "Sydney", "time": "tomorrow", "condition": "rain"}
   ```
