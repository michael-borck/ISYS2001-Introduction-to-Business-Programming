---
title: "🌤️ Weather Question Parser Worksheet"
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

> A beginner-friendly guide to parsing weather questions using pseudocode and LLMs

## Introduction

Natural Language Processing (NLP) lets computers understand human language. In this worksheet, we'll design a system that can understand weather questions like "Will it rain tomorrow in Sydney?" by extracting:

- **Location**: Sydney
- **Time Period**: tomorrow
- **Weather Attribute**: rain

## What You'll Learn

In this worksheet, you will:
1. Understand different approaches to natural language parsing
2. Learn how to effectively use reference documentation with LLMs
3. Design a weather parser using pseudocode
4. Practice intentional prompting with LLMs to convert your design to Python
5. Learn how to use AI as a thinking partner in development

## Assessment Connection

**Important:** The skills you develop in this worksheet directly relate to your upcoming assessment. In this unit, your AI conversations with LLMs will be assessed and weighted more heavily than the resulting code. This is because the ability to effectively prompt, question, and collaborate with AI tools is becoming a critical skill for developers.

The weather parser you create here will not only help you understand NLP concepts but also provide a useful component you can apply in your assignment. Pay special attention to the intentional prompting techniques, follow-up questioning, and your approach to teaching the LLM about the hands-on-ai package—these are exactly the skills your assessment will evaluate.

## Different Approaches to NLP

There are several ways to solve this problem:

1. **Keyword Matching**: Using pattern recognition to find important words
2. **Template Matching**: Comparing questions to pre-defined templates
3. **Traditional NLP**: Using specialized linguistic analysis libraries
4. **LLM Integration**: Using AI language models

For beginners, the LLM approach can be surprisingly accessible while giving excellent results!

## Step 1: Introducing the hands-on-ai Package

The hands-on-ai package provides tools to work with language models easily. You should have access to a reference guide (`hands_on_ai_llm_guide.txt`) that explains the package's features.

### Teaching the LLM About hands-on-ai

Before asking the LLM to help you implement your parser, you need to teach it about the hands-on-ai package:

1. Upload the `hands_on_ai_llm_guide.txt` reference document to your chat with the LLM
2. Use an initial prompt like this to help the LLM understand the context:

```
I've uploaded a reference guide for the hands-on-ai package. Please review it to understand the package's capabilities, especially the chat module that we'll use for building a weather question parser. After reviewing, please confirm you understand how the package works.
```

## Step 2: Understanding the Problem

Before writing any code, let's break down what we're trying to accomplish:

1. Take a natural language question about weather
2. Extract structured information (location, time, weather attribute)
3. Return this information in a consistent format

## Step 3: Designing Our Weather Parser (Pseudocode)

Let's design our solution in pseudocode:

```
FUNCTION ParseWeatherQuestion(question)
    // Create a prompt for the language model
    prompt = "Extract location, time period, and weather attribute from: " + question
    
    // Send prompt to language model using hands-on-ai
    response = SendToLanguageModel(prompt)
    
    // Convert response to structured format
    result = ParseJsonResponse(response)
    
    // Set default values for missing information
    IF result does not have "location" OR result["location"] is empty THEN
        result["location"] = none
    END IF
    
    IF result does not have "time_period" OR result["time_period"] is empty THEN
        result["time_period"] = "today"
    END IF
    
    IF result does not have "weather_attribute" OR result["weather_attribute"] is empty THEN
        result["weather_attribute"] = "general"
    END IF
    
    RETURN result
END FUNCTION
```

## Step 4: Converting Pseudocode to Python with Intentional Prompting

Now that you've designed your parser in pseudocode and taught the LLM about the hands-on-ai package, it's time to convert this design to Python code.

### 🧠 What Is Intentional Prompting?

**Intentional prompting** means you:
- Ask the AI to **explain** its reasoning
- Ask questions that lead to deeper understanding of Python concepts
- Refine and adapt prompts when the first response isn't quite right
- Know when to question, correct, or reject AI-generated code
- Use the AI as a **thinking partner**, not just a code generator

### Example Intentional Prompt

Here's an example of how to intentionally prompt an LLM to help convert our pseudocode to Python:

```
Now that you understand the hands-on-ai package, I'd like your help implementing a weather question parser. I have the following pseudocode design:

FUNCTION ParseWeatherQuestion(question)
    // Create a prompt for the language model
    prompt = "Extract location, time period, and weather attribute from: " + question
    
    // Send prompt to language model using hands-on-ai
    response = SendToLanguageModel(prompt)
    
    // Convert response to structured format
    result = ParseJsonResponse(response)
    
    // Set default values for missing information
    IF result does not have "location" OR result["location"] is empty THEN
        result["location"] = none
    END IF
    
    IF result does not have "time_period" OR result["time_period"] is empty THEN
        result["time_period"] = "today"
    END IF
    
    IF result does not have "weather_attribute" OR result["weather_attribute"] is empty THEN
        result["weather_attribute"] = "general"
    END IF
    
    RETURN result
END FUNCTION

Please help me convert this to Python code using the hands-on-ai package. In your response:

1. First, explain which specific functions from the hands-on-ai.chat module would work best for parsing weather questions
2. Show me how to improve the prompt to get better structured data (JSON)
3. Write the Python implementation with comments explaining each step
4. Explain any potential errors and how to handle them
5. Suggest a simple way to test the function

After seeing your implementation, I want to understand WHY you made certain choices, not just copy the code.
```

## Step 5: Follow-up Questions for Deeper Understanding

After receiving the LLM's implementation, ask follow-up questions to deepen your understanding:

```
Thank you for the implementation. I have some follow-up questions:

1. I notice you used the get_response function from hands-on-ai.chat. Would using one of the personality bots like teacher_bot or coder_bot give better results for parsing? Why or why not?

2. Could we improve the error handling? What specific types of errors might occur when parsing JSON from an LLM response?

3. How would you modify this implementation to handle more complex weather questions like "Will I need sunscreen and a hat this weekend at the beach?" that contain multiple weather attributes?

4. If we wanted to make this part of a complete weather application, what would be the next step after parsing the question?
```

This type of follow-up demonstrates intentional prompting - you're asking "why" questions and exploring improvements rather than just accepting the first solution.

## Step 6: Experiments and Reflection

Once you have your implementation, test it with these questions:

- "Will it rain tomorrow in Sydney?"
- "What's the temperature in Tokyo today?"
- "Do I need an umbrella in London this weekend?"
- "Is it going to be windy in Chicago?"
- "How cold will it be in New York tomorrow?"

**Reflection Questions:**
1. How well did the LLM understand your pseudocode design?
2. What improvements did the LLM suggest to your original design?
3. What errors or edge cases did you encounter?
4. How could you further improve the prompt to get more accurate parsing?

## For Advanced Users: Exploring Advanced Techniques

If you're comfortable with the basic implementation, try exploring these advanced concepts:

### Using Custom Bots for Specialized Parsing

The hands-on-ai package allows creating custom bots with specific personalities and system prompts. Ask the LLM how you could create a specialized "weather parser bot" using code like this pseudocode:

```
FUNCTION CreateWeatherBot()
    // Create specialized bot for weather parsing
    SET system_prompt = "You are an expert at extracting structured data from weather questions."
    SET personality = "technical"
    
    RETURN CustomBot with system_prompt and personality
END FUNCTION
```

### Adding Schema Validation

For more reliable parsing, consider asking the LLM about adding schema validation to your implementation:

```
I'd like to ensure the parsed data always matches a specific structure. How could I use Python's data validation tools to ensure my weather query results always contain valid location, time_period, and weather_attribute fields? Please explain the concept and show me an example.
```

### Using the Agent Module for Complex Weather Questions

The hands-on-ai package includes an "agent" module with tools for multi-step reasoning. Ask the LLM how you might use this for more complex weather analysis:

```
Looking at the hands-on-ai reference guide, I see there's an "agent" module with tools for multi-step reasoning. How could I use this to handle more complex weather questions that might require calculations or conversions, like "Will it be warmer tomorrow in New York than it was yesterday in Boston?"
```

## Key Takeaways

1. LLMs make complex NLP tasks accessible to beginners
2. Pseudocode helps design solutions before jumping into implementation
3. Intentional prompting transforms AI from a code generator to a thinking partner
4. Reference documentation can be uploaded to LLMs to help them understand specific libraries
5. Follow-up questions deepen understanding and improve solutions

## Exercises

1. **Basic**: 
   - Upload the hands-on-ai reference guide and ask the LLM to explain which parts are most relevant for weather parsing
   - Create an intentional prompt to add one more field to extract from weather questions

2. **Intermediate**: 
   - Write pseudocode for a command-line interface for your parser
   - Ask the LLM to compare using the chat module versus the agent module for this task

3. **Challenge**: 
   - Design pseudocode for connecting your parser to a weather API
   - Ask the LLM to help implement a custom weather bot that can both parse questions and answer them using sample weather data

## Teaching LLMs About Domain-Specific Tools

This worksheet demonstrates a powerful approach to learning: using LLMs as collaborative learning partners by teaching them about specific tools and packages. You can apply this same approach to other domains by:

1. Finding or creating a reference document about your tool/library
2. Uploading it to the LLM
3. Using intentional prompting to ask the LLM to help you understand and use the tool
4. Following up with deeper questions to explore advanced features

## Resources

- Hands-On AI Documentation (from the reference guide you uploaded)
- [Effective Prompting Strategies for LLMs](https://example.com/prompting)
- [Python JSON and Error Handling](https://example.com/python-json)
