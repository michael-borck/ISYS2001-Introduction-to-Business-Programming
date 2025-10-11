---
title: "Mini-Project: Building Your Own Snake Game"
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

## Introduction

Now that you've set up your local Python environment and explored various Python mini-projects, it's time to apply what you've learned by building a classic game from scratch! In this activity, you'll create your own version of the Snake game using Pygame. This project will reinforce programming concepts like loops, conditionals, and functions while introducing you to game development principles.

## Objectives
- Build a complete, playable game from starter code
- Apply programming fundamentals in a game development context
- Learn basic game development concepts (game loop, rendering, input handling)
- Customize and extend a project based on your own creative ideas

## Prerequisites
- Completed Activity 1 (Anaconda installation)
- Python and Pygame installed on your computer
- Basic understanding of Python concepts (variables, loops, conditionals, functions)

If you haven't installed Pygame yet, run this command in your Anaconda Prompt or terminal:
```
pip install pygame
```

## Project Overview: Snake Game

The Snake game is a classic arcade game where you control a snake that moves around the screen. The basic gameplay includes:

1. The snake moves continuously in one direction
2. The player changes the snake's direction using arrow keys
3. The snake grows longer when it eats food
4. The game ends if the snake hits the wall or itself
5. The score increases each time the snake eats food

## Getting Started

### Step 1: Download the Starter Code

Download the starter code from our course repository:
- Navigate to: [course-website.edu/resources/snake-game-starter](https://course-website.edu/resources/snake-game-starter)
- Download the `snake_starter.py` file
- Save it to a location you can easily access

The starter code provides the basic structure and some helper functions to get you started.

### Step 2: Understand the Starter Code

Open the starter code in your preferred editor and review it. The code includes:

- Import statements for required libraries
- Game constants (screen size, colors, etc.)
- Basic initialization of Pygame
- A game loop structure
- Comment placeholders for code you'll need to add

```python
# Sections of the starter code:

# 1. Imports and initialization
import pygame
import random
pygame.init()

# 2. Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
GAME_SPEED = 15

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 3. Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

# 4. Game loop structure
def game_loop():
    # Game variables will go here
    
    # Main game loop
    game_over = False
    while not game_over:
        # Event handling will go here
        
        # Game logic will go here
        
        # Drawing code will go here
        
        # Update display
        pygame.display.update()
        clock.tick(GAME_SPEED)
    
    pygame.quit()
    quit()

# 5. Start the game
game_loop()
```

## Part 1: Implementing Core Game Functionality

Follow these steps to implement the essential components of the Snake game:

### Step 1: Set Up the Snake and Food

Add the following to your `game_loop()` function:

```python
def game_loop():
    # Game variables
    game_over = False
    
    # Initial snake position (middle of screen)
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2
    
    # Initial movement direction
    x_change = 0
    y_change = 0
    
    # Snake body (list of segments)
    snake_segments = []
    snake_length = 1
    
    # Generate initial food position
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    
    # Main game loop
    while not game_over:
        # Rest of the code goes here
```

### Step 2: Handle User Input

Add the following inside your main game loop:

```python
# Event handling
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        game_over = True
    
    # Handle key presses
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            x_change = -BLOCK_SIZE
            y_change = 0
        elif event.key == pygame.K_RIGHT:
            x_change = BLOCK_SIZE
            y_change = 0
        elif event.key == pygame.K_UP:
            y_change = -BLOCK_SIZE
            x_change = 0
        elif event.key == pygame.K_DOWN:
            y_change = BLOCK_SIZE
            x_change = 0
```

### Step 3: Update Snake Position

Add this code after the event handling:

```python
# Update snake position
x += x_change
y += y_change

# Check for boundary collisions
if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
    game_over = True
```

### Step 4: Draw Game Elements

Add this code to draw the snake, food, and clear the screen:

```python
# Clear the screen
screen.fill(BLACK)

# Draw food
pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

# Draw snake
snake_head = []
snake_head.append(x)
snake_head.append(y)
snake_segments.append(snake_head)

# Remove extra segments if snake is too long
if len(snake_segments) > snake_length:
    del snake_segments[0]

# Check if snake hits itself
for segment in snake_segments[:-1]:
    if segment == snake_head:
        game_over = True

# Draw each segment of the snake
for segment in snake_segments:
    pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])
```

### Step 5: Handle Food Collision and Growth

Add this code to handle when the snake eats food:

```python
# Check if snake eats food
if x == food_x and y == food_y:
    # Generate new food
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    # Increase snake length
    snake_length += 1
```

### Step 6: Test Your Game

Run your game to make sure the basic functionality works:
- The snake should move with arrow keys
- The snake should grow when it eats food
- The game should end when the snake hits the wall or itself

## Part 2: Adding Game Enhancements

Now that you have a working basic game, let's enhance it with additional features. Choose at least TWO of these enhancements to implement:

### Enhancement 1: Add a Score Display

```python
# Add at the beginning of game_loop()
score = 0
font = pygame.font.SysFont(None, 25)

# Add inside your game loop after clearing the screen
def display_score(score):
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])

# Update when the snake eats food
if x == food_x and y == food_y:
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    snake_length += 1
    score += 10  # Increase score

# Call in your drawing section
display_score(score)
```

### Enhancement 2: Add a Game Over Screen

```python
# Add at the beginning of game_loop()
def display_message(msg, color):
    font = pygame.font.SysFont(None, 50)
    message = font.render(msg, True, color)
    message_rect = message.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(message, message_rect)

# Replace the end of your game loop with this
# Outside the main game loop
screen.fill(BLACK)
display_message("Game Over! Press Q to Quit or C to Play Again", RED)
pygame.display.update()

# Wait for user to quit or restart
end_game = False
while not end_game:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                end_game = True
                game_over = True
            if event.key == pygame.K_c:
                game_loop()  # Restart the game
        if event.type == pygame.QUIT:
            end_game = True
            game_over = True
```

### Enhancement 3: Add Speed Progression

```python
# Add inside your game loop where the snake eats food
if x == food_x and y == food_y:
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    snake_length += 1
    score += 10
    
    # Increase game speed every 5 food items
    if snake_length % 5 == 0 and GAME_SPEED < 30:
        GAME_SPEED += 2
```

### Enhancement 4: Add Different Types of Food

```python
# Add at the beginning of game_loop()
food_types = [
    {"color": RED, "points": 10, "probability": 0.7},
    {"color": (255, 255, 0), "points": 20, "probability": 0.3}  # Yellow food worth more points
]
current_food_type = random.choices(food_types, 
                                  weights=[f["probability"] for f in food_types])[0]

# Change the food generation code
def generate_food():
    fx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    fy = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_type = random.choices(food_types, 
                              weights=[f["probability"] for f in food_types])[0]
    return fx, fy, food_type

# Initialize food
food_x, food_y, current_food_type = generate_food()

# Update drawing code
pygame.draw.rect(screen, current_food_type["color"], [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

# Update eating code
if x == food_x and y == food_y:
    food_x, food_y, current_food_type = generate_food()
    snake_length += 1
    score += current_food_type["points"]
```

### Enhancement 5: Add Wall Obstacles

```python
# Add after initializing the snake
obstacles = []
for _ in range(5):  # Create 5 random obstacles
    obs_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    obs_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    # Make sure obstacles don't overlap with snake's starting position
    if (obs_x != x or obs_y != y):
        obstacles.append([obs_x, obs_y])

# Add to your drawing code
for obs in obstacles:
    pygame.draw.rect(screen, (0, 0, 255), [obs[0], obs[1], BLOCK_SIZE, BLOCK_SIZE])

# Add to collision detection
# Check for obstacle collisions
for obs in obstacles:
    if x == obs[0] and y == obs[1]:
        game_over = True
```

## Part 3: Creative Customization

Now it's time to make the game your own! Add at least TWO personal touches to your game. Here are some ideas:

1. **Customize the appearance**:
   - Change colors or add a background image
   - Make the snake segments a different shape
   - Add a custom icon or title screen

2. **Add sound effects**:
   - Play a sound when the snake eats food
   - Add background music
   - Play a sound when the game ends

3. **Add gameplay features**:
   - Create power-ups that temporarily make the snake faster or slower
   - Add a "portal" that teleports the snake from one side to the other
   - Create a "time-limited" mode where players must reach a certain score before time runs out

4. **Add difficulty levels**:
   - Create an easy, medium, and hard mode with different speeds
   - Add more obstacles at higher difficulties
   - Make the play area smaller at higher difficulties

## Part 4: Debugging and Testing

As you develop your game, you'll likely encounter bugs or unexpected behavior. Here are some common issues and how to fix them:

1. **Snake doesn't move**:
   - Check that you're updating the snake's position with `x_change` and `y_change`
   - Make sure your game loop is running and updating the display

2. **Snake moves too fast or too slow**:
   - Adjust the `GAME_SPEED` constant
   - Make sure you're calling `clock.tick(GAME_SPEED)` in your game loop

3. **Snake can move backwards into itself**:
   - Add logic to prevent the snake from moving directly opposite its current direction

4. **Food appears inside the snake**:
   - Add a check to make sure new food doesn't spawn on top of the snake

## Submission Guidelines

To complete this activity, submit:

1. Your complete Python code file
2. A short video or screenshots showing your game in action
3. A brief description of:
   - Which enhancements you added
   - What personal touches you added
   - What challenges you faced and how you overcame them

## Extension Challenges (Optional)

If you finish early or want to continue developing your game, here are some advanced challenges:

1. **Two-player mode**: Allow two players to control different snakes on the same screen

2. **High score system**: Save and display the highest scores across game sessions

3. **Custom levels**: Create predefined levels with specific obstacle arrangements

4. **Animation effects**: Add visual effects for eating food, game over, etc.

5. **AI opponent**: Create a computer-controlled snake that tries to get food

Remember, the goal is to have fun while applying what you've learned about Python programming. Don't be afraid to experiment and make the game your own!
