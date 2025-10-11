"""
Sample code for using the hands-on-ai package in the Weather Advisor project
These examples show how to use key features of hands-on-ai for natural language
understanding and conversation management in your project.
"""

from hands_on_ai import nlp, conversation, response

# Example 1: Basic weather question parsing
def parse_weather_question(question):
    """
    Parse a natural language weather question to extract key information
    
    Args:
        question (str): User's weather-related question
        
    Returns:
        dict: Extracted location, time period, and weather attribute
    """
    # Use NLP to extract entities and intent
    analysis = nlp.analyze_text(question)
    
    # Default values
    result = {
        "location": None,
        "time_period": "today",  # Default to today
        "weather_attribute": "general"  # Default to general conditions
    }
    
    # Extract location (city, country, place name)
    locations = nlp.extract_entities(question, entity_type="LOCATION")
    if locations:
        result["location"] = locations[0]
    
    # Extract time expressions
    time_expressions = nlp.extract_time_expressions(question)
    if time_expressions:
        # Map time expressions to standardized periods
        time_mapping = {
            "today": ["today", "now", "current", "currently"],
            "tomorrow": ["tomorrow", "next day"],
            "this weekend": ["weekend", "this weekend", "coming weekend"],
            "this week": ["this week", "coming week"]
        }
        
        for period, keywords in time_mapping.items():
            if any(expr.lower() in keywords for expr in time_expressions):
                result["time_period"] = period
                break
            
        # Handle specific days
        days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
        for day in days:
            if any(day in expr.lower() for expr in time_expressions):
                result["time_period"] = day
                break
    
    # Extract weather attributes of interest
    weather_attributes = {
        "temperature": ["temperature", "temp", "hot", "cold", "warm", "cool", "heat", "degrees"],
        "rain": ["rain", "rainy", "raining", "precipitation", "wet", "umbrella", "downpour", "shower"],
        "wind": ["wind", "windy", "breeze", "gust", "blow"],
        "snow": ["snow", "snowy", "snowfall", "blizzard"],
        "cloud": ["cloud", "cloudy", "overcast", "clear", "sunny"],
        "humidity": ["humid", "humidity", "sticky", "muggy"],
        "storm": ["storm", "thunder", "lightning", "thunderstorm"],
        "clothing": ["jacket", "coat", "sweater", "jumper", "shorts", "t-shirt", "umbrella", "raincoat", "sunglasses"]
    }
    
    # Find which weather attributes are mentioned
    for attr, keywords in weather_attributes.items():
        if any(keyword in question.lower() for keyword in keywords):
            result["weather_attribute"] = attr
            break
    
    return result


# Example 2: Managing conversation context
class WeatherConversation:
    """Manage context for weather-related conversations"""
    
    def __init__(self):
        """Initialize conversation handler"""
        self.convo = conversation.ConversationManager()
        self.default_location = None
    
    def process_query(self, user_query):
        """
        Process a user query with conversation context
        
        Args:
            user_query (str): User's question or command
            
        Returns:
            dict: Processed query with context
        """
        # Add query to conversation history
        self.convo.add_user_message(user_query)
        
        # Parse the current query
        parsed = parse_weather_question(user_query)
        
        # If location is missing, check conversation context
        if not parsed["location"] and self.convo.message_count > 1:
            # Look for location in previous exchanges
            for msg in reversed(self.convo.get_history(limit=3)):
                if "location" in msg.get("metadata", {}) and msg["metadata"]["location"]:
                    parsed["location"] = msg["metadata"]["location"]
                    break
            
            # If still no location, use default
            if not parsed["location"]:
                parsed["location"] = self.default_location
        
        # Update conversation with this information
        self.convo.add_metadata_to_last_message({
            "location": parsed["location"],
            "time_period": parsed["time_period"],
            "weather_attribute": parsed["weather_attribute"]
        })
        
        return parsed
    
    def generate_response(self, weather_data):
        """
        Generate a natural language response based on weather data
        
        Args:
            weather_data (dict): Weather data to respond about
            
        Returns:
            str: Natural language response
        """
        # Get context from conversation
        last_msg = self.convo.get_last_message()
        metadata = last_msg.get("metadata", {})
        
        # Use response generator to create natural language
        template = self._select_response_template(
            metadata.get("weather_attribute", "general"),
            weather_data
        )
        
        response_text = response.fill_template(template, weather_data)
        
        # Add to conversation
        self.convo.add_assistant_message(response_text)
        
        return response_text
    
    def _select_response_template(self, attribute, weather_data):
        """Select appropriate response template based on weather attribute"""
        templates = {
            "temperature": [
                "The temperature in {location} {time_desc} is {temp}°C, feeling like {feels_like}°C.",
                "It's {temp}°C in {location} {time_desc}, but it feels like {feels_like}°C."
            ],
            "rain": [
                "For {location} {time_desc}, there's a {rain_chance}% chance of rain with expected precipitation of {rain_amount}mm.",
                "You can expect {rain_desc} in {location} {time_desc} ({rain_chance}% chance)."
            ],
            "clothing": [
                "For {location} {time_desc} with {temp}°C and {condition}, {clothing_advice}.",
                "{clothing_advice} for {location} {time_desc} as it will be {condition} with temperatures around {temp}°C."
            ],
            "general": [
                "The weather in {location} {time_desc} is {condition} with a temperature of {temp}°C.",
                "Expect {condition} conditions in {location} {time_desc}, with temperatures around {temp}°C."
            ]
        }
        
        # Return appropriate template or fall back to general
        return response.choose_template(templates.get(attribute, templates["general"]))


# Example 3: Generating clothing recommendations
def get_clothing_recommendation(weather_data):
    """
    Generate clothing recommendations based on weather conditions
    
    Args:
        weather_data (dict): Weather data including temperature, conditions, etc.
        
    Returns:
        str: Clothing recommendation
    """
    temp = weather_data.get("temperature", {}).get("current", 20)  # Default to 20°C if missing
    condition = weather_data.get("condition", {}).get("text", "").lower()
    is_raining = any(word in condition for word in ["rain", "shower", "drizzle"])
    is_snowing = any(word in condition for word in ["snow", "sleet", "blizzard"])
    is_windy = weather_data.get("wind", {}).get("speed", 0) > 20  # >20 kmh is windy
    
    advice = []
    
    # Temperature-based advice
    if temp <= 0:
        advice.append("you'll need a heavy winter coat")
        advice.append("wear multiple layers")
        advice.append("don't forget a hat and gloves")
    elif temp <= 10:
        advice.append("a warm coat is necessary")
        advice.append("you should wear layers")
    elif temp <= 16:
        advice.append("a light jacket or sweater is recommended")
    elif temp <= 22:
        advice.append("a light sweater might be good for comfort")
    elif temp <= 28:
        advice.append("short sleeves are fine")
    else:
        advice.append("wear light clothing")
        advice.append("you might want to have a hat for sun protection")
    
    # Condition-based advice
    if is_raining:
        advice.append("bring an umbrella")
        advice.append("waterproof shoes are a good idea")
    
    if is_snowing:
        advice.append("snow boots are recommended")
        advice.append("dress in waterproof layers")
    
    if is_windy:
        advice.append("a windbreaker would be helpful")
    
    if "sunny" in condition or "clear" in condition:
        advice.append("sunglasses would be useful")
        if temp > 22:
            advice.append("don't forget sunscreen")
    
    # Format response
    if len(advice) <= 2:
        return " and ".join(advice)
    else:
        formatted = ", ".join(advice[:-1]) + ", and " + advice[-1]
        return formatted


# Example usage
if __name__ == "__main__":
    # Example 1: Parse a weather question
    question = "Will it rain tomorrow in Sydney?"
    parsed = parse_weather_question(question)
    print(f"Parsed question: {parsed}")
    
    # Example 2: Use conversation context
    convo = WeatherConversation()
    query1 = "What's the weather like in Melbourne today?"
    result1 = convo.process_query(query1)
    print(f"Query 1 result: {result1}")
    
    # Follow-up question without specifying location
    query2 = "Will I need an umbrella tomorrow?"
    result2 = convo.process_query(query2)
    print(f"Query 2 result: {result2}")  # Should inherit Melbourne from context
    
    # Example 3: Clothing recommendation
    sample_weather = {
        "temperature": {"current": 12, "feels_like": 10},
        "condition": {"text": "Light rain shower"},
        "wind": {"speed": 25}
    }
    clothing_advice = get_clothing_recommendation(sample_weather)
    print(f"Clothing advice: {clothing_advice}")