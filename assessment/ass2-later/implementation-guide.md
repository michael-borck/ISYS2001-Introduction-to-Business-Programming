# Implementation Guide: Weather Advisor Project

This guide provides implementation suggestions and prompting examples to help you get started with your Weather Advisor project.

## Getting Started

### Setting Up Your Repository

1. Create a new GitHub repository named `weather-advisor-project`
2. Create a new Google Colab notebook
3. Connect your Colab notebook to your GitHub repository
4. Create initial files:
   - `README.md`
   - `PROMPTING.md`

### Project Structure

Consider structuring your Colab notebook with these sections:

```
# Weather Advisor
## Setup & Configuration
## User Interface
## Weather Data Retrieval
## Data Processing & Analysis
## Visualization Functions
## Natural Language Processing
## Main Application Logic
```

## Step-by-Step Implementation Approach

### 1. Weather Data Component

Start by implementing basic weather data retrieval. Here's a sample intentional prompting sequence:

**Initial Prompt:**
```
I'm building a weather application in Python that needs to retrieve current weather and forecast data for a given city. I'd like to use the wttr.in API. Can you show me how to make a request and parse the JSON response?
```

**Evaluation:** The initial response might give you basic code but likely won't handle errors or edge cases.

**Refined Prompt:**
```
That's helpful, but I need to make my weather data retrieval more robust. Can you improve the function to:
1. Handle connection errors
2. Validate the city name input
3. Cache results to avoid excessive API calls
4. Return a structured dictionary with only the data I need (current temp, conditions, forecast)
```

As you implement this component, use the 6-step methodology:
1. Restate the problem (get weather data)
2. Identify input/output (city name → weather data)
3. Work a simple example manually
4. Request pseudocode
5. Convert to Python
6. Test with different inputs

### 2. Visualization Component

Once you have weather data, you'll need to visualize it.

**Sample Prompt:**
```
I have a Python dictionary containing weather forecast data for the next 5 days. Each day has temperature (high/low), precipitation chance, and weather condition. What are 3 different ways I could visualize this data using matplotlib that would be most helpful for users? For each visualization, explain why it would be useful.
```

**Follow-up Prompt:**
```
I like the temperature trend line chart idea. Can you provide code for this visualization? The dictionary structure is:
{
  'day1': {'date': '2025-04-11', 'temp_high': 72, 'temp_low': 58, 'precip': 20, 'condition': 'Partly Cloudy'},
  'day2': {'date': '2025-04-12', 'temp_high': 75, 'temp_low': 60, 'precip': 10, 'condition': 'Sunny'},
  ...and so on
}
```

### 3. Natural Language Interface

This is where you'll leverage the hands-on-ai package and your experience with chatbots.

**Initial Prompt:**
```
I want to create a function that takes a user's question about weather (e.g., "Will it rain tomorrow in Sydney?") and determines:
1. The location they're asking about
2. The time period (today, tomorrow, this weekend)
3. The weather condition they're interested in (rain, temperature, etc.)

Can you help me write a function that parses a question and extracts these elements?
```

**Refinement Prompt:**
```
That's a good start, but I want to improve the natural language understanding. Can you revise the function to:
1. Handle more variations of time expressions (e.g., "next Tuesday", "in 3 days")
2. Handle compound questions ("Will it be sunny and warm?")
3. Return default values when elements aren't specified
```

### 4. Integration and User Interface

Finally, you'll need to integrate all components and create a user interface.

**Sample Prompt:**
```
I want to create a menu-driven interface using pyinputplus that gives users these options:
1. Get current weather for a location
2. See 5-day forecast with visualizations
3. Ask a weather-related question in natural language
4. Exit

Can you provide the code structure for this menu system?
```

## Examples of Intentional Prompting

### Example 1: Requesting Logic Explanation

**Prompt:**
```
I notice your code uses list comprehension here instead of a for loop. Can you explain why that approach is better in this context?
```

### Example 2: Critiquing Implementation

**Prompt:**
```
Your solution for parsing the weather condition works, but I'm concerned it might break with unusual inputs. What edge cases should I be concerned about, and how would you modify the code to handle them?
```

### Example 3: Requesting Modular Design

**Prompt:**
```
I think this visualization code would be clearer if broken into smaller functions. Can you refactor it into a more modular design with separate functions for data preparation and plotting?
```

## Using hands-on-ai Package

The hands-on-ai package provides several components that could be useful for your project:

1. **Conversation Management**
   - Track conversation history
   - Maintain context across multiple user queries

2. **Natural Language Understanding**
   - Entity extraction (locations, dates, weather conditions)
   - Intent classification for weather questions

Here's a sample prompt for integrating hands-on-ai:

```
I want to use the hands-on-ai package to enhance my weather advisor's natural language capabilities. Specifically, I'd like to use its conversation management features to remember previous queries. Can you show me how to integrate it with my existing parse_question function?
```

## Documentation Requirements

Remember to document your AI interactions thoroughly in `PROMPTING.md`:

```markdown
## Weather Data Retrieval Component

### Initial Prompt
I asked the AI: "..."

### AI Response
The AI suggested: "..."

### My Evaluation
The response had these strengths and weaknesses:
- Strength: Good error handling
- Weakness: No caching to prevent excessive API calls

### Refined Prompt
I then asked: "..."

### Final Implementation
After several iterations, here's my final implementation with comments explaining my choices:

```python
def get_weather(city):
    # Code here
    # ...
```

## Common Pitfalls to Avoid

1. **Overly broad prompts** - Be specific about what you need
2. **Accepting first responses** - Always evaluate and refine
3. **Not testing edge cases** - Ask AI to help you identify boundary conditions
4. **Forgetting to document** - Update your prompting journal as you go

Good luck with your Weather Advisor project!
