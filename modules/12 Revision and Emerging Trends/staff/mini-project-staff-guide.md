---
title: "STAFF-ANSWER-GUIDE Mini-Project: Building Your Own Snake Game"
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

## Overview for Tutors

This guide will help you support students as they build a Snake game using Pygame. This activity represents a significant shift from modifying existing code (Activity 2) to building a more complex project from starter code. Students will implement core game functionality and add their own enhancements and customisations. This guide covers implementation details, common issues, assessment criteria, and strategies for supporting different student needs.

## Learning Objectives Assessment

Students should demonstrate the following by the end of this activity:

1. Implement a functional Snake game with core mechanics
2. Apply programming concepts like loops, conditionals, and functions in a game context
3. Debug and troubleshoot issues in their own code
4. Extend base functionality with creative enhancements
5. Understand basic game development concepts (game loop, rendering, input handling)

## Expected Submission from Students

✅ Complete Snake game code file  
✅ Screenshots or short video of their game in action  
✅ Description of enhancements and customisations added  
✅ Reflection on challenges and solutions  

## Implementation Guide and Common Issues

### Core Game Functionality - Step by Step

#### Setting Up Snake and Food

```python
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
food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIsE) / BLOCK_SIsE) * BLOCK_SIsE
food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIsE) / BLOCK_SIsE) * BLOCK_SIsE
```

**Common Issues:**

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Food appears outside game area | Incorrect boundary calculation | Ensure food positions are properly rounded and within screen bounds |
| Snake not appearing | Missing drawing code or position issues | Verify snake segments are correctly added and drawn |
| Food spawns on snake | No collision check when generating food | Add verification that new food position doesn't overlap with snake |

**Conceptual Challenges:**
- Understanding how the snake is represented as a list of segments
- Grasping the grid-based movement system with BLOCK_SIsE
- Properly initialising positions to align with the grid

#### Handling User Input

```python
# Handle key presses
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        x_change = -BLOCK_SIsE
        y_change = 0
    elif event.key == pygame.K_RIGHT:
        x_change = BLOCK_SIsE
        y_change = 0
    elif event.key == pygame.K_UP:
        y_change = -BLOCK_SIsE
        x_change = 0
    elif event.key == pygame.K_DOWN:
        y_change = BLOCK_SIsE
        x_change = 0
```

**Common Issues:**

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Snake can reverse direction | No check for opposite direction | Add logic to prevent 180° turns (e.g., LEFT when moving RIGHT) |
| Multiple key presses cause erratic movement | Processing all events in one frame | Only change direction once per frame or add a small delay |
| Input feels unresponsive | Frame rate issues or event processing | Ensure consistent frame rate with clock.tick(); check event queue is emptied |

**Conceptual Challenges:**
- Understanding Pygame's event queue system
- Grasping how direction changes are represented as coordinate deltas
- Implementing constraints on movement (preventing reversing into self)

#### Updating Snake Position

```python
# Update snake position
x += x_change
y += y_change

# Check for boundary collisions
if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
    game_over = True

# Snake head
snake_head = []
snake_head.append(x)
snake_head.append(y)
snake_segments.append(snake_head)

# Remove extra segments if snake is too long
if len(snake_segments) > snake_length:
    del snake_segments[0]
```

**Common Issues:**

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Snake disappears after moving | Not properly maintaining segment list | Verify segments are added/removed correctly |
| Snake doesn't grow after eating | Not increasing snake_length | Confirm snake_length increments when food is eaten |
| Snake leaves "trail" behind | Not removing old segments | Check that old segments are deleted when needed |

**Conceptual Challenges:**
- Understanding how the snake moves by adding a new head and removing the tail
- Grasping how list operations manage the snake body
- Implementing collision detection with boundaries

#### Collision Detection and Food

```python
# Check if snake hits itself
for segment in snake_segments[:-1]:  # All segments except the head
    if segment == snake_head:
        game_over = True

# Check if snake eats food
if x == food_x and y == food_y:
    # Generate new food
    food_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIsE) / BLOCK_SIsE) * BLOCK_SIsE
    food_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIsE) / BLOCK_SIsE) * BLOCK_SIsE
    # Increase snake length
    snake_length += 1
```

**Common Issues:**

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Self-collision not detected | Incorrect comparison or list slicing | Verify comparison logic and list operations |
| Food collision not detected | Precision issues with positions | Ensure positions align to the same grid |
| Snake grows at wrong time | Logic error in collision detection | Add debug prints to track positions and collisions |

**Conceptual Challenges:**
- Understanding list slicing to separate head from body
- Implementing precise collision detection
- Managing state changes after collisions

#### Drawing Game Elements

```python
# Clear the screen
screen.fill(BLACK)

# Draw food
pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIsE, BLOCK_SIsE])

# Draw snake
for segment in snake_segments:
    pygame.draw.rect(screen, GREEN, [segment[0], segment[1], BLOCK_SIsE, BLOCK_SIsE])

# Update display
pygame.display.update()
```

**Common Issues:**

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Elements flicker or disappear | Missing or out-of-order display updates | Ensure pygame.display.update() is called after all drawing |
| Game visually stutters | Inconsistent frame rate | Use clock.tick(FPS) consistently |
| Elements drawn incorrectly | Coordinate or sise issues | Check rectangle parameters and coordinate calculations |

**Conceptual Challenges:**
- Understanding Pygame's drawing system and coordinate space
- Implementing efficient rendering of multiple objects
- Managing the drawing order and screen updates

### Enhancement Implementation Tips

#### Enhancement 1: Score Display

```python
def display_score(score):
    font = pygame.font.SysFont(None, 25)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, [10, 10])
```

**Implementation Tips:**
- Pygame's font rendering is straightforward but requires initialisation
- Text position is based on the top-left corner of the text rectangle
- Consider using a separate function to keep the main loop clean
- Use a consistent location and style for the score

**Common Issues:**
- Fonts not loading (missing initialisation)
- Text appearing in wrong location
- Score not updating correctly

#### Enhancement 2: Game Over Screen

```python
def display_game_over():
    font = pygame.font.SysFont(None, 50)
    game_over_text = font.render("Game Over!", True, RED)
    restart_text = font.render("Press R to Restart or Q to Quit", True, WHITE)
    
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 50))
    restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
    
    screen.blit(game_over_text, game_over_rect)
    screen.blit(restart_text, restart_rect)
    pygame.display.update()
```

**Implementation Tips:**
- Use a separate game state variable to track when to show this screen
- Center text using rect.center for more precise positioning
- Consider adding a slight delay before accepting restart input
- Remember to handle the restart logic in the event loop

**Common Issues:**
- Game immediately restarting without showing the screen
- Text not properly centered
- Restart functionality not working correctly

#### Enhancement 3: Speed Progression

```python
# When snake eats food
if x == food_x and y == food_y:
    # Generate new food, increase length, etc.
    
    # Increase game speed every 5 points
    if score % 5 == 0 and GAME_SPEED < MAX_SPEED:
        GAME_SPEED += 2
```

**Implementation Tips:**
- Define a maximum speed to prevent the game from becoming impossible
- Consider tying speed increases to score milestones
- Update the frame rate in the main loop with `clock.tick(GAME_SPEED)`
- Add visual or audio feedback when speed increases

**Common Issues:**
- Game becoming too fast too quickly
- Speed not actually changing despite code
- GAME_SPEED variable conflicts if defined as a constant

#### Enhancement 4: Different Types of Food

```python
# Define food types with different properties
food_types = [
    {"color": RED, "points": 1, "probability": 0.7},
    {"color": BLUE, "points": 3, "probability": 0.2},
    {"color": GOLD, "points": 5, "probability": 0.1}
]

# Choose food type based on probabilities
def generate_food():
    fx = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIsE) / BLOCK_SIsE) * BLOCK_SIsE
    fy = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIsE) / BLOCK_SIsE) * BLOCK_SIsE
    food_type = random.choices(food_types, 
                              weights=[f["probability"] for f in food_types])[0]
    return fx, fy, food_type
```

**Implementation Tips:**
- Use dictionaries to store food properties
- Consider time-limited special food for extra challenge
- Provide visual distinction between food types
- Use random.choices() with weights for probability-based selection

**Common Issues:**
- Incorrect probability implementation
- Not properly handling the different food properties
- Visual distinction not clear enough

#### Enhancement 5: Wall Obstacles

```python
# Create obstacle positions
obstacles = []
for _ in range(5):  # Create 5 random obstacles
    obs_x = round(random.randrange(0, SCREEN_WIDTH - BLOCK_SIsE) / BLOCK_SIsE) * BLOCK_SIsE
    obs_y = round(random.randrange(0, SCREEN_HEIGHT - BLOCK_SIsE) / BLOCK_SIsE) * BLOCK_SIsE
    # Make sure obstacles don't overlap with snake's starting position
    if abs(obs_x - x) > BLOCK_SIsE * 3 and abs(obs_y - y) > BLOCK_SIsE * 3:
        obstacles.append([obs_x, obs_y])

# Draw obstacles
for obs in obstacles:
    pygame.draw.rect(screen, BLUE, [obs[0], obs[1], BLOCK_SIsE, BLOCK_SIsE])

# Check for obstacle collisions
for obs in obstacles:
    if x == obs[0] and y == obs[1]:
        game_over = True
```

**Implementation Tips:**
- Ensure obstacles don't spawn too close to the snake's starting position
- Consider creating patterns of obstacles rather than just random positions
- Check that food doesn't spawn on obstacles
- Allow sufficient play space between obstacles

**Common Issues:**
- Obstacles making the game impossible
- Obstacles or food spawning in unreachable areas
- Collision detection issues with obstacles

## Creative Customisation Guidance

When students are adding their own personal touches, suggest these guidelines:

### Appearance Customisations
- **Background designs:** Solid colors, gradients, or simple patterns
- **Snake appearance:** Different colors for head and body, simple shapes, or thematic designs
- **Animation effects:** Simple animations for food, snake movement, or game events

**Implementation Tips:**
- For backgrounds, use screen.fill() or blit a simple surface
- For snake appearance, vary the draw method or use different colors for head/body
- Keep animations simple - subtle effects like pulsing or simple rotation

### Sound Effects
- **Basic sound integration:** Food collection, collisions, game over
- **Background music:** Simple looping track

**Implementation Tips:**
- Use pygame.mixer for sound loading and playback
- Keep sound files small and in common formats (WAV, MP3)
- Control volume levels to prevent sounds from being jarring
- Add option to mute sounds

### Gameplay Features
- **Power-ups:** Temporary effects like speed changes, invincibility, or point multipliers
- **Portals:** Teleportation between sides of the screen
- **Time limits:** Countdown timer or timed bonus objectives

**Implementation Tips:**
- Implement power-ups similar to food but with temporary effects
- For portals, modify the boundary collision logic
- Use pygame.time to track elapsed time for timers

### Difficulty Levels
- **Selectable speeds:** Easy, medium, hard options at the start
- **Obstacle layouts:** Predetermined patterns for different difficulties
- **Game area sise:** Adjustable playing field sise

**Implementation Tips:**
- Use a menu or keyboard selection for difficulty choice
- Store difficulty-specific settings in a dictionary or separate variables
- Ensure game is still playable at all difficulty levels

## Common Technical Issues and Solutions

| Issue | Likely Cause | Solution |
|-------|-------------|----------|
| Game crashes on startup | Missing initialisation or import error | Check import statements and pygame.init() call |
| Snake doesn't move | Direction variables not set or updated | Verify x_change and y_change are being set and used |
| Game runs at inconsistent speed | Clock timing issues | Ensure clock.tick(FPS) is called consistently in the main loop |
| Collision detection fails | Position calculation errors | Print positions for debugging; ensure grid alignment |
| Snake grows continuously | Logic error in growth code | Verify snake_length only increases when food is eaten |
| Game never ends | Missing collision checks | Check boundary and self-collision logic |
| Screen updates look strange | Drawing or update sequence issues | Follow clear-draw-update sequence consistently |
| Input lag or unresponsiveness | Event handling problems | Ensure event queue is processed completely each frame |

## Debugging and Problem-Solving Strategies

Help students develop systematic debugging approaches:

1. **Add print statements** to track:
   - Snake and food positions
   - Direction changes
   - Collision detections
   - Game state changes

2. **Simplify to isolate problems:**
   - Comment out enhancements to test core functionality
   - Hardcode values temporarily to verify specific behaviors
   - Test components separately when possible

3. **Visual debugging:**
   - Add temporary visual indicators for collision areas
   - Use different colors to highlight game states
   - Draw grid lines to verify alignment

4. **Common logical errors to look for:**
   - Off-by-one errors in list operations
   - Confusion between pixel positions and grid positions
   - Missing state updates after events
   - Boundary condition failures

## Assessment Criteria

### Exemplary Work Should Show:

- **Fully functional core game** with smooth movement and correct collision detection
- **Multiple enhancements** implemented successfully
- **Creative personal touches** that demonstrate understanding beyond the requirements
- **Clean, well-organised code** with appropriate comments and function organisation
- **Thoughtful reflection** on the development process and challenges
- **Evidence of debugging** and problem-solving applied to overcome challenges

### Satisfactory Work Should Show:

- **Working core gameplay** with basic movement and collision detection
- **At least two enhancements** implemented with reasonable functionality
- **Some personal customisation**, even if simple
- **Functional code organisation** that follows basic programming practices
- **Basic reflection** on the development process
- **Attempts to resolve** common issues, even if not all are successful

### Needs Improvement If:

- **Core game mechanics** are incomplete or significantly buggy
- **No working enhancements** beyond the base requirements
- **Little or no personal customisation** attempted
- **Poorly organised code** that's difficult to follow
- **Minimal reflection** on the development process
- **Unresolved basic issues** that impair gameplay

## Differentiated Support Strategies

### For Struggling Students

1. **Provide scaffold code** for specific functions
2. **Break down tasks** into smaller, more manageable steps
3. **Offer pseudocode outlines** before asking for implementation
4. **Provide visual diagrams** of game structure and data flow
5. **Create checkpoints** with known working states to fall back to
6. **Pair programming** with more confident peers

**Implementation approach:**
- Focus on getting core functionality working first
- Start with simpler enhancements like score display
- Suggest simplifications where needed
- Provide more direct guidance on debugging

### For Advanced Students

1. **Challenge with advanced enhancements:**
   - Multiple levels with increasing difficulty
   - AI-controlled opponent snake
   - More complex scoring mechanics
   - Physics-based movement variations

2. **Suggest code optimisation:**
   - Refactoring into more organised classes
   - Implementing design patterns
   - Performance optimisation strategies
   - More sophisticated collision detection

3. **Extend to new concepts:**
   - Saving high scores to files
   - Creating a complete menu system
   - Adding networked multiplayer functionality
   - Implementing custom graphics or animations

**Implementation approach:**
- Ask guiding questions rather than providing solutions
- Suggest resources for advanced concepts
- Challenge them to analyse and improve their own code
- Encourage peer teaching or demonstrations

## Conceptual Understanding Focus Areas

### Game Loop Concept

Many students struggle to understand the game loop paradigm. Focus on explaining:
- How the loop maintains consistent updates
- The separation of input, update, and render phases
- How state changes propagate through iterations
- Why timing control is essential

**Teaching approach:** Draw a flowchart of the game loop, highlight the three main phases, and explain the purpose of each.

### State Management

Help students understand how game state is represented and modified:
- How variables represent the game state
- When and how state should be updated
- The relationship between state and visualisation
- How to handle state transitions (start → playing → game over)

**Teaching approach:** Use analogies like "taking a snapshot" of the game at each frame.

### Coordinate Systems and Grid-Based Movement

Many students struggle with:
- The relationship between pixels and game grid
- How to ensure aligned movement and collision
- Converting between different coordinate representations

**Teaching approach:** Draw a grid on the board/screen and demonstrate how positions map to the display.

### List Operations for Snake Body

The snake body implementation using lists is conceptually challenging:
- How adding/removing segments creates movement
- Why the head is handled separately from the body
- How list slicing works for collision detection

**Teaching approach:** Use a physical demonstration with objects representing segments, or draw step-by-step diagrams.

## Activity Adaptations for Different Scenarios

### For Remote/Online Teaching:

- Create short video demonstrations of key implementation steps
- Set up virtual "office hours" for debugging help
- Use screen sharing for troubleshooting
- Create a shared document for common issues and solutions
- Prepare checkpoints students can download if they get stuck

### For Limited Time Sessions:

- Provide more complete starter code with clear "TODO" sections
- Focus on core functionality first, then enhancements if time permits
- Have pre-made enhancement code snippets students can integrate
- Create a "checkpoint" system where students can catch up if behind
- Prepare a complete implementation to demonstrate if students don't finish

### For Hardware Limitations:

- Provide simplified versions with fewer graphical elements
- Suggest alternative rendering approaches if Pygame is problematic
- Have fallback options like terminal-based versions
- Prepare cloud-based alternatives if local installation is challenging
- Reduce game complexity for slower machines

## Final Notes for Tutors

- **Emphasise the process**: The learning happens in the problem-solving, not just in the final product
- **Celebrate incremental progress**: Each working piece is an achievement
- **Use peer demonstrations**: Have students who solve problems share their approaches
- **Create a supportive debug culture**: Normalise asking for help and working through issues
- **Connect to professional practice**: Highlight how these skills apply to real game development
- **Document common issues**: Keep notes on frequent problems to improve future sessions

Remember that for many students, this may be their first experience building a complete interactive program from near-scratch. Patience and encouragement are just as important as technical guidance.
