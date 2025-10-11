# 🗣️ Understanding Weather Questions: NLP Strategies

> This handout explores different approaches to parsing natural language weather questions in Python, from beginner-friendly techniques to more advanced solutions.

## The Challenge

Converting questions like "Will it rain tomorrow in Sydney?" into structured data that identifies:
- **Location**: Sydney
- **Time Period**: tomorrow
- **Weather Attribute**: rain

## Strategy 1: Keyword Matching with Regular Expressions

Perfect for beginners with no external dependencies.

```python
import re

def parse_weather_question(question):
    """Extract location, time, and weather attribute from a question."""
    result = {
        "location": None,
        "time_period": "today",  # Default
        "weather_attribute": "general"  # Default
    }
    
    # Extract location (look for words after "in" or "for")
    location_pattern = r'(?:in|for|at)\s+([A-Za-z\s]+)(?:\?|$|\s)'
    location_match = re.search(location_pattern, question)
    if location_match:
        result["location"] = location_match.group(1).strip()
    
    # Extract time period
    time_keywords = {
        "today": ["today", "now", "current"],
        "tomorrow": ["tomorrow", "next day"],
        "weekend": ["weekend", "this weekend"]
    }
    
    for period, keywords in time_keywords.items():
        if any(keyword in question.lower() for keyword in keywords):
            result["time_period"] = period
            break
    
    # Extract weather attribute
    weather_attributes = {
        "rain": ["rain", "raining", "rainy", "umbrella", "wet"],
        "temperature": ["temperature", "hot", "cold", "warm", "cool"],
        "wind": ["wind", "windy", "breeze", "gust"],
        "sunshine": ["sun", "sunny", "sunshine", "bright", "clear"]
    }
    
    for attr, keywords in weather_attributes.items():
        if any(keyword in question.lower() for keyword in keywords):
            result["weather_attribute"] = attr
            break
            
    return result

# Example usage
question = "Will it rain tomorrow in Sydney?"
result = parse_weather_question(question)
print(f"Location: {result['location']}")
print(f"Time: {result['time_period']}")
print(f"Weather attribute: {result['weather_attribute']}")
```

**Pros**: Simple, no dependencies, easy to understand and extend  
**Cons**: Limited accuracy, struggles with complex phrasing

## Strategy 2: Template Matching

Good for beginners who want more structure.

```python
def parse_with_templates(question):
    """Match question against common templates to extract information."""
    # Define templates with placeholders
    templates = [
        {"template": "Will it [WEATHER] in [LOCATION] [TIME]?",
         "weather_index": 2, "location_index": 4, "time_index": 5},
        {"template": "Is it going to [WEATHER] in [LOCATION]?",
         "weather_index": 3, "location_index": 5, "time_index": None},
        {"template": "Do I need [ITEM] in [LOCATION] [TIME]?",
         "item_index": 3, "location_index": 5, "time_index": 6}
    ]
    
    # Normalize question
    question = question.lower().strip()
    if not question.endswith("?"):
        question += "?"
    
    # Try to match against templates
    words = question.split()
    
    for template in templates:
        template_parts = template["template"].lower().split()
        
        # Simple template matching (could be improved)
        if len(words) == len(template_parts):
            match = True
            for i, part in enumerate(template_parts):
                if part.startswith("[") and part.endswith("]"):
                    # This is a placeholder, no need to match exactly
                    continue
                if words[i] != part:
                    match = False
                    break
            
            if match:
                # Extract information based on template
                result = {"location": None, "time_period": "today", "weather_attribute": "general"}
                
                if "location_index" in template and template["location_index"] is not None:
                    result["location"] = words[template["location_index"]]
                
                if "time_index" in template and template["time_index"] is not None:
                    time_word = words[template["time_index"]]
                    # Map time word to period
                    if time_word in ["tomorrow"]:
                        result["time_period"] = "tomorrow"
                    elif time_word in ["weekend", "saturday", "sunday"]:
                        result["time_period"] = "weekend"
                
                if "weather_index" in template and template["weather_index"] is not None:
                    weather_word = words[template["weather_index"]]
                    # Map weather word to attribute
                    weather_mapping = {
                        "rain": "rain", "raining": "rain", "rainy": "rain",
                        "snow": "snow", "snowing": "snow", "snowy": "snow",
                        "hot": "temperature", "cold": "temperature", "warm": "temperature"
                    }
                    result["weather_attribute"] = weather_mapping.get(weather_word, "general")
                    
                if "item_index" in template and template["item_index"] is not None:
                    item_word = words[template["item_index"]]
                    # Map items to weather attributes
                    item_mapping = {
                        "umbrella": "rain", "jacket": "temperature", 
                        "sunglasses": "sunshine", "coat": "temperature"
                    }
                    result["weather_attribute"] = item_mapping.get(item_word, "general")
                
                return result
    
    # If no template matches, fall back to regex approach
    return parse_weather_question(question)
```

**Pros**: More structured, handles common patterns well  
**Cons**: Less flexible with varied phrasing, requires manual template creation

## Strategy 3: External LLM Integration

Great for intermediate students comfortable with APIs.

```python
import requests
import json
import os

def parse_with_llm(question):
    """Use an external LLM to parse the weather question."""
    # For demonstration - you would use your actual API endpoint
    # This example uses a simplified approach
    
    API_KEY = os.environ.get("LLM_API_KEY")  # Never hardcode API keys
    
    # Construct the prompt
    prompt = f"""
    Extract the following information from this weather-related question:
    Question: "{question}"
    
    Please respond with a JSON object containing:
    - location: The city or place being asked about (null if not specified)
    - time_period: When they're asking about (today, tomorrow, weekend, etc.)
    - weather_attribute: What aspect of weather they're asking about (rain, temperature, etc.)
    
    Return ONLY the JSON object without any explanation.
    """
    
    # Make the API request
    try:
        response = requests.post(
            "https://api.example.com/v1/completions",  # Replace with actual API endpoint
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": prompt,
                "max_tokens": 150,
                "temperature": 0.1  # Low temperature for more predictable outputs
            }
        )
        
        # Parse the JSON response
        result = json.loads(response.json()["choices"][0]["text"])
        
        # Validate and provide defaults
        if "location" not in result or result["location"] is None:
            result["location"] = None
        if "time_period" not in result or result["time_period"] is None:
            result["time_period"] = "today"
        if "weather_attribute" not in result or result["weather_attribute"] is None:
            result["weather_attribute"] = "general"
            
        return result
        
    except Exception as e:
        print(f"Error using LLM API: {e}")
        # Fall back to regex approach if API fails
        return parse_weather_question(question)
```

**Pros**: High accuracy, handles complex phrasing, minimal code  
**Cons**: Requires API key, external dependency, potential cost

## Strategy 4: NLTK Named Entity Recognition

Good for intermediate students interested in traditional NLP.

```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import ne_chunk

# Uncomment these lines the first time you run this
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

def parse_with_nltk(question):
    """Use NLTK to extract named entities and analyze the question."""
    result = {
        "location": None,
        "time_period": "today",  # Default
        "weather_attribute": "general"  # Default
    }
    
    # Tokenize and tag parts of speech
    tokens = word_tokenize(question)
    pos_tags = pos_tag(tokens)
    
    # Extract named entities
    named_entities = ne_chunk(pos_tags)
    
    # Find locations (GPE = Geo-Political Entity)
    for entity in named_entities:
        if hasattr(entity, 'label') and entity.label() == 'GPE':
            result["location"] = ' '.join([word for word, tag in entity.leaves()])
            break
    
    # Check for time expressions
    time_mapping = {
        "today": ["today", "now", "current", "currently"],
        "tomorrow": ["tomorrow", "next day"],
        "weekend": ["weekend", "this weekend", "saturday", "sunday"]
    }
    
    for time_period, keywords in time_mapping.items():
        if any(keyword in [word.lower() for word, _ in pos_tags] for keyword in keywords):
            result["time_period"] = time_period
            break
    
    # Check for weather attributes
    weather_attributes = {
        "rain": ["rain", "raining", "rainy", "umbrella", "wet", "precipitation"],
        "temperature": ["temperature", "temp", "hot", "cold", "warm", "cool", "degrees"],
        "wind": ["wind", "windy", "breeze", "gust", "breezy"],
        "snow": ["snow", "snowy", "snowing", "snowfall"]
    }
    
    for attr, keywords in weather_attributes.items():
        if any(keyword in [word.lower() for word, _ in pos_tags] for keyword in keywords):
            result["weather_attribute"] = attr
            break
    
    return result
```

**Pros**: More accurate than regex, no external API needed, good learning experience  
**Cons**: Requires installing NLTK and models, more complex to understand

## Strategy 5: Pydantic Models with LLM (Advanced)

For students with more programming experience.

```python
from pydantic import BaseModel, Field
from typing import Optional
import requests
import json
import os

class WeatherQuery(BaseModel):
    """Model for structured weather query information."""
    location: Optional[str] = Field(None, description="The city or place being asked about")
    time_period: str = Field("today", description="When they're asking about (today, tomorrow, weekend)")
    weather_attribute: str = Field("general", description="Weather aspect (rain, temperature, wind, etc.)")

def parse_with_pydantic_llm(question):
    """Use an LLM with Pydantic validation to parse the weather question."""
    
    API_KEY = os.environ.get("LLM_API_KEY")  # Never hardcode API keys
    
    # Schema description
    schema = {
        "type": "object",
        "properties": {
            "location": {"type": ["string", "null"], "description": "City or place name"},
            "time_period": {"type": "string", "description": "Time period (today, tomorrow, weekend)"},
            "weather_attribute": {"type": "string", "description": "Weather aspect (rain, temperature, etc.)"}
        },
        "required": ["time_period", "weather_attribute"]
    }
    
    # Construct the prompt
    prompt = f"""
    Extract structured information from this weather question: "{question}"
    
    Follow this JSON schema exactly:
    {json.dumps(schema, indent=2)}
    
    Return ONLY the JSON object without any explanation.
    """
    
    try:
        # Make the API request
        response = requests.post(
            "https://api.example.com/v1/completions",  # Replace with actual API endpoint
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "prompt": prompt,
                "max_tokens": 150,
                "temperature": 0.1
            }
        )
        
        # Parse the JSON response
        llm_result = json.loads(response.json()["choices"][0]["text"])
        
        # Validate with Pydantic
        query = WeatherQuery(**llm_result)
        
        # Return as dictionary
        return query.dict()
        
    except Exception as e:
        print(f"Error using LLM with Pydantic: {e}")
        # Fall back to simpler approach
        return parse_weather_question(question)
```

**Pros**: Structured output, validation, handles complex queries, modern approach  
**Cons**: More complex, requires understanding of Pydantic, external API dependency

## Choosing the Right Approach

| Strategy | Complexity | Dependencies | Accuracy | Good For |
|----------|------------|--------------|----------|----------|
| Regex | Low | None | Moderate | Beginners focusing on Python basics |
| Templates | Low-Medium | None | Moderate | Those who want more structure |
| External LLM | Medium | API access | High | Students comfortable with APIs |
| NLTK | Medium-High | NLTK package | Good | NLP enthusiasts |
| Pydantic+LLM | High | Pydantic, API | Excellent | Advanced programmers |

---

## Mini-Project: Build a Weather Question Parser

### Task
Create a function that extracts location, time period, and weather attribute from natural language questions about weather.

### Steps
1. Choose one of the strategies above based on your comfort level
2. Implement the parsing function
3. Test with at least 5 different weather questions
4. Add error handling for unexpected inputs
5. (Optional) Implement a fallback strategy if your primary method fails

### Example Questions for Testing
- "Will it rain tomorrow in Sydney?"
- "What's the temperature in Tokyo today?"
- "Do I need an umbrella in London this weekend?"
- "Is it going to be windy in Chicago?"
- "How cold will it be in New York tomorrow?"

### Extension
Combine your parser with a weather data API to create a complete system that can answer weather questions in natural language!
