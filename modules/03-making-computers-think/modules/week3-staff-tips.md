---
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

# Week 3 Instructor Notes

These  "Instructor Notes" emphasises the importance of framing the self-assessment tool as a confidence booster and clear guide for students, rather than a test or evaluation. It encourages instructors to normalise the need for review, emphasising that revisiting concepts is a normal part of every programmer's journey. The slide also highlights the benefits of this approach, including better overall learning outcomes and increased student agency and self-awareness.

The instructor notes also point out potential pitfalls to avoid, such as students feeling judged or anxious about falling behind. To mitigate these risks, the slide suggests keeping the assessment quick and focused, providing clear next steps, and trusting students to know what they need. By framing the assessment as preparation and emphasising choice and self-direction, instructors can help students feel supported and empowered in their learning journey.



## Philosophy: Empowerment, Not Gatekeeping

This readiness check should feel like:

- **Self-awareness tool**, not a test
- **Confidence booster** for prepared students  
- **Clear guidance** for students needing review
- **Permission** to take the time needed

## Key Messages to Reinforce

### Growth Mindset

- Review is normal and smart
- Foundations matter more than speed
- Every programmer revisits concepts
- Strong preparation leads to better outcomes

### Self-Directed Learning

- Students assess their own readiness
- Clear pointers to specific review materials
- Encouragement to seek help when needed
- Ownership of their learning journey

## Avoiding Common Pitfalls

### Don't Create Anxiety

- Frame as preparation, not evaluation
- Emphasise choice and self-direction
- Normalise the need for review
- Focus on upcoming excitement, not current gaps

### Don't Overwhelm

- Keep assessment quick and focused
- Point to specific resources, don't recreate content
- Trust students to know what they need
- Provide clear next steps

## Success Indicators

**Strong readiness check creates**:

- Confident students who dive into Week 3
- Struggling students who self-identify review needs  
- Reduced confusion and frustration in Week 3
- Better overall learning outcomes
- Increased student agency and self-awareness

**Red flags**:

- Students skipping review when they clearly need it
- Anxiety about "falling behind"
- Feeling judged rather than supported
- Overwhelm from too many requirements


# Instructor Notes - Simple Decisions

This section outlines the timing and key points for presenting the topic of decision patterns and flowcharts. The hook involves discussing smart home thermostats to relate the concept to learners and demonstrate the complexity of AI decision-making. The presenter should emphasise the importance of choosing appropriate decision structures, avoiding overcomplicating simple problems, and recognising when decisions are necessary. Flowcharts are introduced as a valuable tool for algorithm design, debugging, and code review.

The section includes suggested discussion questions and activities to engage learners and reinforce their understanding of decision patterns and flowcharts. By the end of the presentation, learners should feel confident in recognising decision needs, be comfortable with the three decision patterns, and be ready to learn the corresponding Python syntax. The presenter should aim to generate excitement about building interactive programs that incorporate decision-making capabilities.

## Key Teaching Points

### The Hook Works Because

- Everyone relates to thermostats
- AI complexity is immediately obvious
- Easy to simplify to core logic
- Sets expectation for managing complexity

### Pattern Recognition is Critical

Students who master the three patterns can:

- Choose appropriate structures
- Avoid overcomplicating simple problems
- Recognise when they need decisions at all

### Flowcharting Skills Transfer

- Helps with debugging later
- Useful for algorithm design
- Professional skill in many fields
- Makes code review easier

## Common Student Misconceptions

1. **"Every program needs complex decisions"**
   - Many programs are still linear
   - Decisions add complexity - use when needed

2. **"More conditions = better program"**  
   - Start simple, add complexity gradually
   - Each condition needs testing

3. **"Flowcharts are just busy work"**
   - Show how they prevent logic errors
   - Demonstrate debugging value

## Assessment Ideas

**Quick Checks**:

- "What decision pattern fits this scenario?"
- "Draw a simple flowchart for..."
- "Find the missing case in this logic"

**Hands-On**:

- Flowchart peer review
- Pattern identification exercises
- Logic tracing activities

## Preparation for convert decisions to python

Students should complete this module feeling:

- Confident about recognising decision needs
- Comfortable with the three patterns
- Ready to learn Python syntax
- Excited about building interactive programs

**Red Flag**: If students struggle with pattern recognition here, they'll struggle with syntax choices in W3.2.


# Instructor Notes - Decision in Python

The instructor should demonstrate common syntax errors, like using a single equals sign for comparison, and have students articulate the difference between assignment and equality. Python's unique use of whitespace for defining blocks should be highlighted, showing how incorrect indentation breaks program logic. Consistent indentation, typically 4 spaces, and visual alignment are crucial for readability.

When teaching decision structures, always demonstrate the wrong order first, then trace through the corrected version step-by-step, emphasising that the first matching condition wins. Connect the concept to real-world decision-making processes. Students should be encouraged to test expected cases, boundary conditions, and edge cases to understand what breaks the logic. Engage the class with questions like "What prints if the score is 89?" or "Find the syntax error in this code snippet." Progressively challenge them to trace through elif chains, convert flowcharts to code, debug broken decision logic, and write variations of a grade calculator. By the end of the lesson, students should be confident with basic if/elif/else structures, comparison operators, and ready to tackle more complex conditional statements.

## Critical Teaching Points

### The = vs == Error

- Write on board: "= ASSIGNS, == ASKS"
- Show the syntax error when using = 
- Have students verbalise the difference
- This error appears in every class!

### Indentation is Everything

- Python is unique in using whitespace
- Show how wrong indentation breaks logic
- Use consistent spaces (4 is standard)
- Demonstrate visual alignment

### Order in elif Chains

- Always demonstrate wrong order first
- Show step-by-step trace through
- Emphasise "first match wins"
- Connect to real-world decision making

## Live Coding Strategy

### Build Incrementally

1. Start with simple if
2. Add else clause
3. Convert to elif chain
4. Add complexity gradually


### Test Everything
After each addition:

- Test the expected case
- Test boundary conditions  
- Test edge cases
- Show what breaks

## Common Student Errors

1. **Missing Colon**
   ```python
   if score > 90    # Missing :
       grade = "A"
   ```

2. **Wrong Indentation**
   ```python
   if score > 90:
   grade = "A"      # Not indented
   ```

3. **Using = Instead of ==**
   ```python
   if score = 90:   # Assignment, not comparison
   ```

4. **Redundant Conditions**
   ```python
   elif score < 90 and score >= 80:  # < 90 is redundant
   ```

## Assessment Ideas

**Quick Checks**:

- "What prints if score is 89?"
- "Find the syntax error"
- "Trace through this elif chain"

**Hands-On**:

- Convert flowchart to code
- Debug broken decision logic  
- Write grade calculator variations

## Preparing Students for W3.3

Students should leave feeling:

- Confident with basic if/elif/else
- Comfortable with comparison operators
- Ready for complex conditions
- Able to convert simple flowcharts to code

**Success indicator**: Students can write a working grade calculator without help.

# Instructor Notes - Complex Logic

Complex logic requires small amount of time to cover each for the 'and' and 'or' operators, and for the 'not' operator. Parentheses should be used when in doubt, and examples of precedence problems will be shown. The AI partnership section, covering how to provide specific error descriptions, request understanding explanations, set constraints in prompts, and ask for simplification. Practical examples, using real-world analogies and simple examples first, then showing step-by-step evaluation.

Common errors section, focusing on precedence errors, impossible conditions, redundant logic, and edge case testing. The testing strategy , emphasising testing beyond the "happy path", checking boundary conditions, invalid input handling, and edge cases. Truth tables, visual grouping, and simpler alternatives will be shown. Students will practise with complex conditions, fixing precedence errors, identifying impossible and redundant logic, and testing edge cases. Examples include login systems, shipping calculators, and game logic. By the end, students should be able to write complex conditions confidently, use parentheses appropriately, debug logic errors systematically, ask AI effective debugging questions, and test their programs thoroughly.

## Critical Teaching Points

### Logical Operator Priority

- `not` has highest precedence
- `and` comes before `or`
- Use parentheses when in doubt
- Show examples of precedence problems

### AI Partnership Evolution
Students should progress from:

- "Fix my code" → Specific error descriptions
- Copy-paste solutions → Understanding explanations  
- Basic prompts → Constraint-setting prompts
- Accepting complexity → Requesting simplification

### Testing Mindset

- Don't just test "happy path"
- Boundary conditions catch most bugs
- Invalid input handling is crucial
- Edge cases reveal logic flaws

## Live Coding Strategy

### Build Complexity Gradually

1. Start with simple `and` example
2. Add `or` conditions
3. Introduce `not` carefully
4. Combine all three with parentheses
5. Show real-world applications

### Debugging Demonstration
Intentionally create these errors:

1. Missing parentheses in complex conditions
2. Impossible `and` combinations  
3. Redundant conditions in `elif`
4. Wrong operator precedence

## Common Student Struggles

### Logical Operator Confusion

- Create truth tables on board
- Use real-world analogies
- Practice with simple examples first
- Show step-by-step evaluation

### Parentheses Placement

- Mathematical analogy helps
- Show how precedence changes meaning
- Practice grouping exercises
- Use visual grouping on board

### Overcomplicating Simple Logic

- Show simpler alternatives
- Question every `not` - is there a clearer way?
- Prefer positive conditions when possible
- Break complex conditions into variables

## Assessment Ideas

**Quick Checks**:

- "What's the result of True and False or True?"
- "When does this condition become True?"
- "Simplify this complex condition"

**Debugging Exercises**:

- Fix precedence errors
- Find impossible conditions
- Identify redundant logic
- Test with edge cases

**Design Challenges**:

- Login system with multiple user types
- Shipping calculator with various rules
- Game logic with multiple win conditions

## Success Indicators

Students should be able to:

- Write complex conditions confidently
- Use parentheses appropriately  
- Debug logic errors systematically
- Ask AI effective debugging questions
- Test their programs thoroughly

**Red flag**: Students who still struggle with basic `if/else` need remediation before advancing to complex logic.