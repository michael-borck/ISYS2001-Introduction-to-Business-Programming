---
title: "Recognising Decisions"
subtitle: "When and Why Programs Make Choices"
format: 
  pptx: default
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
# When Programs Need to Think

## The Smart Home Dilemma (8 minutes)

### Let's Start with AI Overengineering

Watch what happens when I ask AI for a "smart thermostat controller":

**Me**: "Write a smart home thermostat controller"

::: {.notes}
When programs need to make decisions based on varying conditions or inputs, they require a way to evaluate those conditions and determine the appropriate course of action. This is where the concept of computational thinking comes into play, as it involves breaking down complex problems into smaller, more manageable components and applying logical reasoning to solve them.

In the realm of programming, there are three primary decision patterns that enable programs to "think" and make choices: single choice (if), either/or choice (if/else), and multiple options (if/elif/else). By incorporating these patterns into their code, developers can create programs that respond intelligently to different scenarios, allowing them to handle a wide range of tasks and adapt to changing circumstances.
:::

# AI might give you this:
```python
class SmartThermostat:
    def __init__(self):
        self.temp_history = []
        self.learning_mode = True
        self.eco_mode = False
        self.schedules = {}
        
    def control_temperature(self, current_temp, target_temp, 
                          outside_temp, humidity, time_of_day):
        if self.eco_mode and outside_temp < target_temp - 5:
            return self.open_windows()
        elif self.learning_mode:
            prediction = self.ml_predict_comfort(time_of_day, 
                                               self.temp_history)
            if prediction != target_temp:
                self.adjust_schedule(time_of_day, prediction)
        
        if current_temp < target_temp - 1:
            if humidity > 60:
                return self.heat_with_dehumidify()
            else:
                return self.heat()
        elif current_temp > target_temp + 1:
            return self.cool()
        else:
            return self.maintain()
```

::: {.notes}
AI-generated responses may seem plausible but could be inaccurate or nonsensical. They may sound authoritative and convincing, using correct grammar and structure, but the content itself might be made up, irrelevant or just plain wrong.

It's important to think critically about any AI-generated information. Don't just accept it at face value - analyse it carefully, fact-check key claims from reputable sources, and use your own judgement. AI can be a useful tool, but human discernment is essential.
:::

# **Now let me ask you**:

- What does a thermostat REALLY need to decide?
- How many of these features do you understand?
- Could you modify this to add a fan option?

::: {.notes}
Now let me ask you a few questions about the thermostat example we just discussed. What information does a thermostat actually need to make its decisions? How well do you understand the various features and inputs involved in a thermostat's operation? And finally, if given the chance, do you think you could modify the thermostat's programming to include an option for controlling a fan?

These questions are designed to get you thinking critically about the decision-making process in a real-world device. By considering what data is truly necessary for a thermostat to function, evaluating your own understanding of its features, and imagining how you might expand its capabilities, you're engaging in computational thinking. This thought process is essential for breaking down complex problems and designing effective solutions in programming and beyond.
:::

# The Core Truth

A thermostat makes ONE fundamental decision:

- Too cold? → Turn on heat
- Too hot? → Turn on cooling  
- Just right? → Do nothing

That's it. Everything else is extra.

::: {.notes}
The slide titled "The Core Truth" presents a simple decision-making process based on temperature. If it's too cold, the action is to turn on the heat. If it's too hot, the solution is to turn on cooling. However, if the temperature is just right, no action is required.

This slide is part of a larger presentation that covers various aspects of computational thinking and decision-making. The topics range from recognising when programs need to think, to exploring different decision patterns such as single choice, either/or choice, and multiple options. The presentation also includes practice activities on pattern recognition, flowchart design, and real-world scenarios like a grade calculator and a simple game health system.
:::

# Today's Mission

Learn to **recognise** when programs need decisions and map them out before we code.

::: {.notes}
Today's mission is to explore computational thinking and decision-making in programming. We'll examine how decisions are ubiquitous in the digital world, from traffic lights and vending machines to the apps on our phones. By understanding the core concepts of computational thinking, we can begin to break down complex problems into manageable steps.

We'll introduce the three main decision patterns used in programming: single choice (if), either/or choice (if/else), and multiple options (if/elif/else). Through hands-on practice activities, such as designing flowcharts for a grade calculator and a simple game health system, we'll apply these decision patterns to real-world scenarios. By the end of the session, you'll have a solid foundation in computational thinking and be ready to tackle the next step: learning Python syntax.
:::

# Computational Thinking: Decisions Everywhere (7 minutes)

### Decisions in Daily Life
Every interactive system makes decisions, often without us realising it. Let's explore some examples

::: {.notes}
Computational thinking is all around us, embedded in the everyday devices and systems we interact with. From traffic lights that regulate the flow of vehicles at intersections to vending machines that dispense snacks and drinks based on our selections, decision-making is a fundamental aspect of computational thinking. Even our smartphones, which we rely on for communication, entertainment and productivity, are constantly making decisions behind the scenes to provide us with the functionality we expect.

In this presentation, we'll explore three main decision patterns that form the building blocks of computational thinking: single choice (if), either/or choice (if/else) and multiple options (if/elif/else). By understanding these patterns and how they are applied in real-world scenarios, we can develop a deeper appreciation for the role of computational thinking in our daily lives. We'll also have the opportunity to practice recognising these patterns and applying them to solve problems through flowcharting and other activities.
:::

# **Traffic Light**:
```
IF pedestrian button pressed:
    Change to walk signal
ELSE:
    Continue normal cycle
```

::: {.notes}
Imagine a traffic light at a busy intersection. The traffic light needs to make decisions based on the current state of the traffic flow to ensure safe and efficient movement of vehicles. It must determine when to change the lights from green to yellow to red, and back to green again. This decision-making process is crucial for preventing accidents and managing traffic congestion.

The traffic light is a perfect example of how computational thinking and decision-making are applied in everyday life. By analysing the flow of traffic and making decisions based on predefined rules, the traffic light demonstrates the importance of logical thinking and problem-solving. As we explore the concept of computational thinking, the traffic light serves as a relatable and practical illustration of how decisions are made in programming and in the world around us.
:::

# **Vending Machine**:
```
IF money inserted >= item price:
    Dispense item
    Give change
ELSE:
    Show "Insert more money"
```

::: {.notes}
* A vending machine is a common everyday device that relies on computational thinking and decision-making to function correctly. The machine must be able to accept money, validate the amount, and dispense the correct product based on the user's selection. This process involves a series of decisions and conditions that the machine must evaluate to complete the transaction successfully.

* For example, the machine must first check if the correct amount of money has been inserted before allowing the user to make a selection. Once a selection is made, the machine must determine if the chosen product is in stock and if the user has entered enough money to purchase it. If these conditions are met, the machine will dispense the product and return any change owed. If not, the machine must display an appropriate error message and return the user's money. These decisions and actions are all controlled by the vending machine's internal programming, which relies on computational thinking principles to operate effectively.
:::

# **Your Phone**:
```
IF battery < 20%:
    Show low battery warning
IF screen timeout reached:
    Turn off display
```

::: {.notes}
Your phone is a powerful computational device that makes countless decisions every second. From managing battery life to prioritising tasks and processing user input, your phone is constantly evaluating conditions and choosing appropriate actions based on predefined rules and algorithms.

The decision-making processes in your phone follow the same fundamental patterns we've discussed: single choice (if statements), either/or choices (if/else statements), and multiple options (if/elif/else statements). By recognising these patterns, you can better understand how your phone operates and how its software is designed to handle various scenarios efficiently.
:::

# The Three Decision Patterns

Understanding these patterns helps you recognise when to use each:

::: {.notes}
The three main decision patterns in programming are single choice (if), either/or choice (if/else), and multiple options (if/elif/else). The single choice pattern uses an if statement to execute code only when a specific condition is met. The either/or choice pattern utilises an if/else statement to execute one block of code if a condition is true, and a different block if it is false.

The multiple options pattern extends the either/or choice by adding elif statements between the if and else. This allows for checking multiple conditions in sequence, executing the corresponding code block for the first condition that evaluates to true. By recognising and applying these three core decision patterns, programmers can effectively implement conditional logic in their programs.
:::

# 1. Single Choice (if)
"Do something special in one case"

```
IF it's raining:
    Take umbrella
(Otherwise, just continue normally)
```

**When to use**: Adding a special action for specific conditions

::: {.notes}
The single choice (if) decision pattern is used when a program needs to make a decision based on a single condition. If the condition is true, the program will execute a specific block of code; otherwise, it will skip that block and continue with the rest of the program. This pattern is the simplest of the three decision patterns and is often used for basic decision-making in programs.

Some common examples of the single choice (if) pattern include checking if a user has entered a valid input, determining if a number is positive or negative, or verifying if a file exists before attempting to read from it. By using this pattern, programmers can create programs that can adapt their behaviour based on specific conditions, allowing for more dynamic and responsive software.
:::

# 2. Either/Or Choice (if/else)
"Do one thing OR another"

```
IF homework is done:
    Play games
ELSE:
    Do homework first
```

**When to use**: Must choose between two different actions

::: {.notes}
The Either/Or Choice decision pattern, also known as if/else, allows a program to choose between two possible paths based on whether a condition is true or false. If the condition evaluates to true, the program executes the code block following the if statement; otherwise, it executes the code in the else block.

Real-world examples of the Either/Or Choice pattern include a traffic light deciding whether to display red or green based on sensor input, a vending machine determining if a product is available or sold out, and a phone deciding to ring or go to voicemail depending on user settings. Recognising this pattern in everyday scenarios helps develop computational thinking skills and prepares learners for implementing if/else statements in their code.
:::

# 3. Multiple Options (if/elif/else)
"Choose from several possibilities"

```
IF grade >= 90:
    Letter grade is A
ELIF grade >= 80:
    Letter grade is B  
ELIF grade >= 70:
    Letter grade is C
ELSE:
    Letter grade is F
```

**When to use**: Several distinct categories or ranges

::: {.notes}
The if/elif/else statement in Python allows for more than two possible outcomes based on multiple conditions. It starts with an if statement, followed by any number of elif (short for "else if") statements, and ends with an optional else statement. The conditions are evaluated in order until the first one that evaluates to True is found, and the corresponding code block is executed. If none of the conditions are True, the code in the else block (if present) is executed.

To visualise this, imagine a choose-your-own-adventure book where you make decisions at various points in the story. The if statement is like the first decision point, the elif statements are additional decision points, and the else statement is the default path if none of the other conditions are met. This allows for complex decision-making in your programs, enabling them to handle a variety of situations based on different input or computed values.
:::

# Practice: Pattern Recognition

For each scenario, identify the decision pattern:

1. **ATM Withdrawal**: Check balance, dispense money or show error
2. **Game Health**: Show different messages for high/medium/low/critical health
3. **Password Strength**: Add exclamation mark if password is weak
4. **Restaurant Menu**: Choose appetiser, main course, dessert categories

**Answers**: 

1. Either/Or (dispense OR error)
2. Multiple Options (4 health levels)  
3. Single Choice (add ! only if weak)
4. Multiple Options (3 menu categories)

## Visual Thinking: Flowcharts (5 minutes)

### Why Flowcharts Matter

Before writing code, **map out the logic visually**:

- Catches missing cases
- Shows the flow clearly
- Easier to explain to others
- Helps debug later

::: {.notes}
Practice: Pattern Recognition is an important skill in computational thinking. Recognising patterns in code catches missing cases, shows the flow clearly, and makes it easier to explain the logic to others. It also helps with debugging later on when issues arise.

The slide on Practice: Pattern Recognition is part of a larger presentation on computational thinking and decision-making in programs. The other slides cover topics such as the need for AI, the core truth of computational thinking, the three main decision patterns (single choice, either/or choice, and multiple options), flowchart symbols and best practices, and practice activities for designing programs before coding.
:::

# Basic Flowchart Symbols

```
[Rectangle] = Action/Process
<Diamond> = Decision
(Oval) = Start/End
Arrow → = Flow direction
```

::: {.notes}
This slide introduces the basic symbols used in flowcharts to represent different actions and decisions in a program's logic. These symbols include ovals for start and end points, rectangles for process steps, diamonds for decision points, and arrows for connecting the symbols and showing the flow of the program.

By learning and using these standard flowchart symbols, you can create clear visual diagrams of a program's structure and logic before writing any code. This helps break down the problem-solving process into discrete steps and decisions, making it easier to plan out a solution and identify any potential issues or edge cases to consider.
:::

# Simple Example: Password Checker

```
     Start
       ↓
   [Get Password]
       ↓
   <Length >= 8?>
    ↙         ↘
   Yes         No
    ↓           ↓
<Has number?>  [Show "Too short!"]
  ↙      ↘       ↓
Yes       No     ↓
 ↓         ↓      ↓
[Show     [Show   ↓
"Strong"] "Add    ↓
          number"]↓
    ↘      ↙      ↓
       ↓         ↙
      End ← ← ← 
```

::: {.notes}
Simple Example: Password Checker

This slide presents a simple example of a password checker program to illustrate the application of computational thinking and decision-making in code. The password checker likely involves a single choice or either/or choice decision pattern, where the program checks if the entered password matches the correct password and outputs a corresponding message based on the result.

The example aims to provide a concrete, relatable scenario for learners to understand how the decision patterns discussed in previous slides can be implemented in a real-world context. By walking through the logic and flowchart of the password checker, learners can solidify their understanding of computational thinking principles and see how they translate into functional code.
:::

# Flowchart Best Practices

1. **Start simple**: One decision at a time
2. **Be specific**: "Length >= 8" not "good length"
3. **Cover all paths**: Every diamond needs Yes/No exits
4. **Test by tracing**: Follow arrows with different inputs

::: {.notes}
When creating flowcharts, it's crucial to follow best practices to ensure clarity and effectiveness. Start by clearly defining the problem or process you're illustrating, and break it down into logical steps. Use consistent symbols and layouts, and keep the flowchart simple and easy to follow by avoiding unnecessary details or branching paths. Label each step concisely and accurately, and use arrows to indicate the flow of the process.

Test your flowchart thoroughly to ensure it accurately represents the intended process and produces the expected results. If necessary, iterate and refine the flowchart based on feedback and testing. Remember, a well-designed flowchart should be easily understood by anyone, even those unfamiliar with the process. By following these best practices, you'll create flowcharts that effectively communicate complex processes and help streamline problem-solving and decision-making.
:::

# Practice Activity: Design Before Code

Draw flowcharts for the following scenarios:

- **Grade Calculator**: Convert numeric score to letter grade
- **Game Health**: Show status messages based on health points
- **Thermostat Control**: Decide when to heat/cool/maintain
- **Password Strength Checker**: Check length, numbers, special characters

::: {.notes}
In this practice activity, you will have the opportunity to apply computational thinking and design skills before diving into coding. The slide presents four scenarios: a grade calculator that converts numeric scores to letter grades, a game health system that displays status messages based on the player's health points, a thermostat control that decides when to heat, cool, or maintain the temperature, and a password strength checker that evaluates the length, presence of numbers, and special characters.

For each scenario, create a flowchart or pseudocode to map out the logic and decision-making process before writing any actual code. This practice reinforces the importance of planning and designing solutions, helping you break down problems into manageable steps and visualise the flow of your program. By focusing on the design phase first, you'll be better prepared to write efficient and effective code when you start the implementation process.
:::

# Scenario: Grade Calculator

**Requirements**: 

- Get a numeric score (0-100)
- Convert to letter grade (A/B/C/D/F)
- Show encouraging message

**Your Task**: Draw the flowchart first!

**Consider**:

- What's the input?
- What decisions need to be made?
- What are all the possible outputs?
- Are there edge cases? (What if score is 89.9?)

::: {.notes}
This scenario challenges students to create a grade calculator program. The program should accept a numeric score between 0 and 100 as input, then convert it to a letter grade (A, B, C, D, or F). After determining the letter grade, the program displays an encouraging message to the user. To design the solution, students must identify the required input, the decisions the program needs to make based on the score ranges for each letter grade, and all the possible outputs, including any encouraging messages. They should also consider edge cases, such as how to handle a score like 89.9 that falls on the boundary between two letter grades.

Designing the grade calculator requires breaking down the problem into clear steps and decision points. Students can use a flowchart to visualise the program's logic before writing any code. This process of analysing the scenario, identifying the necessary input, outputs, and decisions, and planning the solution using a flowchart is an excellent example of computational thinking in action. By working through this scenario, students will gain experience in applying computational thinking to solve a real-world problem and translating their solution into a working program.
:::

# Scenario: Simple Game Health

**Requirements**:

- Player has health points (0-100)
- Show different status messages
- If health is 0, show "Game Over"

**Your Task**: 

1. Identify the decision pattern
2. Determine the health ranges  
3. Draw the flowchart

::: {.notes}
This slide presents a scenario for a simple game health system. The player's health points range from 0 to 100, and different status messages are displayed based on the player's current health. If the player's health reaches 0, the game displays a "Game Over" message, indicating that the player has lost the game.

Implementing this scenario requires decision-making and conditional statements in the code. The program must check the player's health points and determine which status message to display. If the health points reach 0, the program must trigger the "Game Over" state. This scenario demonstrates the practical application of decision-making patterns in game development.
:::

# Key Takeaways

1. **Decisions are everywhere** in interactive programs
2. **Three main patterns** handle most scenarios
3. **Flowcharts first** before coding
4. **Start simple** - you can always add complexity

::: {.notes}
Key takeaways from the presentation include the importance of computational thinking in modern programs, with a focus on decision-making and the three core decision patterns: single choice (if), either/or choice (if/else), and multiple options (if/elif/else). The presentation also covered the use of flowcharts to design programs before coding, including basic flowchart symbols and best practices.

The presentation provided practical examples and scenarios to reinforce the concepts, such as a password checker, grade calculator, and simple game health system. By understanding and applying these decision patterns and design techniques, learners can develop more effective and efficient programs in the next part of the course, which will cover Python syntax.
:::

# Next Up: Python Syntax

In next module you'll learn:

- How to write these decisions in Python
- The `if`, `elif`, `else` keywords
- Comparison operators (`==`, `<`, `>`)
- The critical difference between `=` and `==`

::: {.notes}
The slide "Next Up: Python Syntax" outlines the key elements of writing decision-making logic in Python code. It introduces the `if`, `elif`, and `else` keywords used to create conditional statements that execute different code blocks based on whether certain conditions are true or false. The slide also mentions comparison operators such as `==` for equality, `<` for less than, and `>` for greater than, which are used to evaluate conditions in decision statements.

One critical point emphasised on the slide is the difference between the assignment operator `=` and the equality comparison operator `==`. The single equals sign `=` is used to assign a value to a variable, while the double equals sign `==` is used to check if two values are equal. Confusing these two operators is a common mistake for beginners, so it's important to clarify the distinction. The upcoming slides will likely provide code examples demonstrating how to use these keywords and operators to implement different decision patterns in Python programs.
:::

# Preview Question

Looking at this flowchart:
```
<score >= 90?>
    ↙       ↘
   Yes       No
    ↓         ↓
[Grade = A] <score >= 80?>
              ↙       ↘
             Yes       No
              ↓         ↓
          [Grade = B] [Continue...]
```

Can you guess what the Python might look like?

---

::: {.notes}
The slide "When Programs Need to Think" explores the decision-making process in programming, using a thermostat as an example. It presents a series of questions to consider, such as understanding the features, modifying the code to add a fan option, and the different actions the thermostat should take based on temperature. The slide also highlights the benefits of using a clear decision-making structure, including easier debugging and explanation to others.

The slide then presents a grading system example, where a numeric score is converted to a letter grade and accompanied by an encouraging message. It prompts the audience to consider the input, decisions, possible outputs, and edge cases in this scenario. Another example involving a player's health points in a game is presented, showcasing different status messages and a "Game Over" screen when health reaches zero. Finally, the slide introduces the Python keywords (`if`, `elif`, `else`) and comparison operators (`==`, `<`, `>`) used to write these decisions, emphasising the importance of understanding the difference between assignment (`=`) and equality comparison (`==`).

Preview questions are an effective way to capture your audience's attention and prime them for the upcoming content. By posing a thought-provoking question related to the presentation topic, you can engage your listeners and encourage them to actively consider the material you're about to cover.

When crafting a preview question, aim for something that will pique curiosity and set the stage for the key points you plan to address. The question should be relevant, concise and open-ended enough to stimulate critical thinking without being overly complex or confusing. Ideally, the preview question will create a sense of anticipation and excitement for the information to come.
:::