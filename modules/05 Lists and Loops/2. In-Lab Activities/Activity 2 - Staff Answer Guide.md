---
title: "Staff Answer Guide: Build-A-Bot Worksheet"
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


## Setup Checklist

- Ensure the `simple_bot` package is properly installed and accessible to all students
- Verify that the local Ollama server is running and accessible
- Test the connection to ensure `get_response()` works correctly
- Have sample responses prepared in case the AI service is unavailable

## Expected Learning Outcomes

By the end of this worksheet, students should be able to:
1. Use loops to create continuous interactions with a chatbot
2. Create and manipulate lists to store conversation history
3. Implement basic command structures using conditionals and lists
4. Apply the concepts of loops and lists to a conversational interface
5. Understand how to provide context to an AI using previous messages

## Activity 1: One-Shot Bot Response

### Expected Output
Students should successfully import the `simple_bot` package and get a single response from the AI.

```
Ask the bot something: What is Python?
Bot: Python is a high-level, interpreted programming language known for its readability and simplicity. It supports multiple programming paradigms including procedural, object-oriented, and functional programming. Python is widely used for web development, data analysis, artificial intelligence, scientific computing, and automation.
```

### Common Issues
- **ImportError**: Student needs to check that `simple_bot` is correctly installed
- **No response from bot**: Check connection to Ollama server
- **Delayed response**: Reassure students that the first response might take longer as the model loads

### Teaching Notes
- Explain that `get_response()` sends the text to an AI model running locally on the Ollama server
- Point out that this is a simple sequential execution - one question, one answer
- Ask students to identify limitations of this approach (doesn't remember context, can't have a conversation)

## Activity 2: Creating a Looping Bot

### Expected Output
Students should see a continuous conversation loop that exits when they type 'bye', 'quit', or 'exit'.

```
Welcome to LoopBot! Ask me anything! Type 'bye' to quit.
You: Hello
Bot: Hello! How can I assist you today?
You: What can you do?
Bot: I'm a simple AI assistant trained to have conversations and answer questions. I can provide information, help with tasks, offer suggestions, and engage in casual discussion. Feel free to ask me anything!
You: bye
Bot: Goodbye! 👋
```

### Code Explanation
- The `while True:` creates an infinite loop that continues until explicitly broken
- The `if user_input.lower() in ["bye", "quit", "exit"]:` checks for exit commands
- The `break` statement exits the loop when an exit command is detected
- Each iteration of the loop gets new input and displays a response

### Teaching Notes
- Emphasize how the loop creates continuous interaction
- Discuss the importance of providing an exit condition to break out of infinite loops
- Ask students how this improves upon the one-shot approach from Activity 1

## Activity 3: Adding Memory with Lists

### Expected Output
Students should see a bot that remembers previous inputs and can report on its memory when asked.

```
Welcome to MemoryBot! I'll try to remember what you say.
You: Hello
Bot: Hello! How can I assist you today?
You: My name is Alex
Bot: Nice to meet you, Alex! How can I help you today?
You: what do you remember
Bot memory contains:
  1. Hello
  2. My name is Alex
  3. what do you remember
You: bye
Bot: Chat ended. I remembered 3 messages. Bye! 👋
```

### Code Explanation
- `memory = []` creates an empty list to store the conversation history
- `memory.append(user_input)` adds each new input to the memory list
- `len(memory)` returns the number of items stored in the list
- `for i, message in enumerate(memory):` loops through each item in the memory list with its position

### Common Questions
- **Why does the bot repeat my last message?** Because we're appending the message to memory before getting a response
- **What would happen if we store thousands of messages?** Memory usage would increase and could potentially slow down the program
- **Does the AI see all the remembered messages?** In this implementation, the AI only sees the current message, not the memory

## Activity 4: Enhanced Memory Bot Challenge

### Sample Solution
Here's a complete implementation that students might create:

```python
# Your enhanced memory bot implementation
print("\nYour Advanced MemoryBot! Type 'help' for commands.")

# Import the needed package
from simple_bot import get_response

# Create your lists and initialize variables here
memory = []
commands = ["help", "memory", "clear", "bye"]

# Write your loop here
while True:
    user_input = input("You: ")
    
    # Implement the command handling
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    elif user_input.lower() == "help":
        print("Available commands:", ", ".join(commands))
    elif user_input.lower() == "memory":
        if memory:
            print("I remember these messages:")
            for i, msg in enumerate(memory):
                print(f"  {i+1}. {msg}")
        else:
            print("My memory is empty!")
    elif user_input.lower() == "clear":
        memory = []
        print("Memory cleared!")
    else:
        # Add message to memory
        memory.append(user_input)
        
        # Keep only the last 3 items using list slicing
        if len(memory) > 3:
            memory = memory[-3:]
            
        # Join the memory items with newlines to create context
        context = "\n".join(memory)
        
        # Send the context to get a more informed response
        response = get_response(context)
        print("Bot:", response)
        print(f"(Memory size: {len(memory)} messages)")
```

### Alternative Approach
A different approach might use a dictionary to track both user inputs and bot responses:

```python
from simple_bot import get_response

print("\nDual Memory Bot! Type 'help' for commands.")

# Track both sides of the conversation
conversation = {
    "user": [],
    "bot": []
}
commands = ["help", "history", "clear", "bye"]

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "bye":
        print("Bot: Chat ended. Goodbye!")
        break
    elif user_input.lower() == "help":
        print("Available commands:", ", ".join(commands))
    elif user_input.lower() == "history":
        if conversation["user"]:
            print("Conversation history:")
            for i in range(len(conversation["user"])):
                print(f"  You: {conversation['user'][i]}")
                print(f"  Bot: {conversation['bot'][i]}")
        else:
            print("No conversation history yet!")
    elif user_input.lower() == "clear":
        conversation = {"user": [], "bot": []}
        print("History cleared!")
    else:
        # Add to user history
        conversation["user"].append(user_input)
        
        # Create context from the last 3 exchanges
        if len(conversation["user"]) > 3:
            conversation["user"] = conversation["user"][-3:]
            conversation["bot"] = conversation["bot"][-3:]
            
        # Create context string with both user and bot messages
        context = ""
        for i in range(len(conversation["user"])-1):
            context += f"User: {conversation['user'][i]}\n"
            context += f"Bot: {conversation['bot'][i]}\n"
        context += f"User: {conversation['user'][-1]}"
        
        # Get response
        response = get_response(context)
        print("Bot:", response)
        
        # Add to bot history
        conversation["bot"].append(response)
```

### Key Concepts to Look For
- Proper handling of commands using conditionals
- Use of list methods (append, slicing with [-3:])
- Properly joining messages into context
- Checking for empty lists before trying to display them
- Displaying relevant information to the user

## Extension: Personality Bot Challenge

### Expected Output
Students should be able to switch between different bot personalities.

```
Multi-Personality Bot! Type 'personalities' to see options.
You: personalities
Available personalities: regular, pirate, emoji, formal
To change, type 'switch to [personality]'
You: switch to pirate
Bot: Switched to pirate personality!
You: What is Python?
PirateBot: Arrr, matey! Python be a programmin' language that's easy to learn and powerful to use! Many a scallywag starts their codin' journey with it! Treasure be waitin'!
```

### Solution Explanation
- `personalities = ["regular", "pirate", "emoji", "formal"]` stores available options
- `current_personality = "regular"` tracks which personality is active
- `startswith()` checks if the input begins with "switch to"
- A conditional structure selects the right function based on the current personality

### Common Issues
- Forgetting to import the personality functions (`pirate_bot`, `emoji_bot`)
- Not checking if the requested personality exists in the list
- Confusion about string methods like `startswith()` and `replace()`

## Creating Custom Bot Personalities

### Sample Implementation
Here's how students might implement a custom bot personality:

```python
from simple_bot import get_response

# Define a custom personality
def wise_dragon_bot(message):
    return get_response(message, system="You are a wise old dragon who answers questions in riddles and ancient wisdom.")

print("\nWise Dragon Bot Test:")
print(wise_dragon_bot("How do I debug my code?"))
```

### Expected Output
```
Wise Dragon Bot Test:
To untangle the webs of code that confound thee, young seeker, first thou must observe with patience. Look for the tracks of thy prey—the elusive bug—in the sands of thy console output. Set traps with print statements to reveal its hiding place. Break thy journey into smaller quests, testing each portion of thy code in isolation. Remember, even the mightiest dragon must sometimes step back to see the entire mountain. In the ancient scrolls, it is written: "To understand the bug, one must become the bug." Walk through thy code as the machine would, one instruction at a time, and the truth shall reveal itself.
```

### Teaching Notes
- Explain that the `system` parameter gives instructions to the AI about how to respond
- Discuss the concept of "persona" in AI interactions
- Encourage creativity while keeping responses appropriate

## Assessment Criteria

To evaluate student understanding, look for:

1. **Basic Skills (C grade)**
   - Successfully implements the looping bot
   - Can add items to a list for memory
   - Uses basic conditionals for commands

2. **Intermediate Skills (B grade)**
   - Successfully implements the enhanced memory bot
   - Correctly uses list slicing to limit memory
   - Properly provides context to the AI
   - Implements multiple commands correctly

3. **Advanced Skills (A grade)**
   - Implements the personality switching functionality
   - Creates custom personalities with the system parameter
   - Adds creative extensions to the basic requirements
   - Code is well-organized and commented

## Common Student Mistakes

1. **Loop Control Flow Issues**
   - Forgetting to include a break statement for exit commands
   - Adding too many nested conditions making code difficult to follow
   - Not handling edge cases (empty input, unexpected commands)

2. **List Management Errors**
   - Attempting to access indexes that don't exist
   - Not checking if the list is empty before trying to display it
   - Incorrect use of slicing syntax to limit the memory size

3. **Context Building Problems**
   - Not properly joining the list items with newlines
   - Sending too much context to the AI (causing confusion)
   - Not providing enough context to maintain conversation flow

## Time Management

- Activity 1: ~5 minutes
- Activity 2: ~10 minutes
- Activity 3: ~15 minutes
- Activity 4: ~20 minutes
- Extension: ~10 minutes

If students are progressing rapidly, encourage them to implement additional features like:
- Error handling for API connection issues
- Saving conversation history to a file
- Loading different system prompts from a configuration file

## Connecting Back to Turtle Graphics

Help students see the parallels between the two worksheets:
- Both use loops to repeat actions (drawing shapes vs. continuing conversation)
- Both use lists to store collections (colors/coordinates vs. message history)
- Both combine loops and lists to create more complex behavior

## Stretch Goals for Advanced Students

If some students finish early, suggest these extensions:
- Implement a chat log feature that saves conversations to a file
- Create a menu of different personalities the bot can switch between
- Add a feature to summarize the conversation so far
- Create a "reset context" command that keeps the memory but starts a fresh conversation

## Troubleshooting the `simple_bot` Package

If students encounter issues with the `simple_bot` package:

1. **ImportError**
   - Verify the package is installed correctly
   - Check for typos in the import statement

2. **Connection Issues**
   - Ensure the Ollama server is running
   - Check for network connectivity issues

3. **Slow Responses**
   - Remind students the first response may be slow as the model loads
   - Suggest using shorter prompts for testing

4. **API-Related Errors**
   - Have a backup activity ready if the API service is down
   - Consider implementing a simple mock version of `get_response()` that returns fixed responses

## Final Project Ideas

To extend learning beyond the workshop, suggest these project ideas:
1. Create a specialized bot for a specific domain (sports, cooking, etc.)
2. Build a chatbot that can play a text-based game
3. Combine the turtle graphics with the chatbot to create a drawing assistant
4. Create a study helper bot that quizzes students on course material

## Reflection Questions for Wrap-up

End the session with these discussion questions:
1. How did using loops make your program more interactive?
2. How did lists help you create a more intelligent conversation?
3. What similarities did you notice between the two activities?
4. How might you use these concepts in other programming projects?
5. What was the most challenging part of building your chatbot?