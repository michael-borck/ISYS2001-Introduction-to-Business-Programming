---
format:
  pdf:
    toc: false
    number-sections: false
    colorlinks: true
  docx:
    toc: false
    number-sections: false
    highlight-style: github
  html:
    toc: true
    toc-expand: 2
    embed-resources: true
---
# WeatherWise: Intelligent Weather Analysis & Advisory System - Enhanced Marking Guide

## Executive Summary

**Assignment Focus**: This assignment assesses students' ability to develop a Python application ("Weather Advisor") within a Google Colab Notebook, integrating weather data access, data visualisation, and a natural language interface. The critical component is the documented use of AI tools through intentional prompting, demonstrating an AI-assisted development process rather than AI-generated solutions.

**Expected Marking Time**: 45-60 minutes per submission

**Key Assessment Priorities**:
1. AI-assisted development process (45% total weight)
2. Functional Python application in Colab (40% total weight)
3. Code quality and organisation (15% total weight)

**Most Common Failure Points**:
- Hardcoded API keys or missing key management
- Screenshot-based conversation documentation
- Superficial AI interactions without iterative refinement
- Notebook dependencies on external files without upload mechanisms

---

## Quick Assessment Checklist

Before detailed marking, complete this initial assessment:

**Critical Requirements (Pass/Fail)**:
- [ ] Colab notebook (.ipynb) present and opens without errors
- [ ] GitHub repository accessible with michael-borck invited
- [ ] AI conversation files in text format (.txt) - not screenshots
- [ ] At least 15 meaningful GitHub commits
- [ ] Core functions implemented with correct signatures

**Functionality Check**:
- [ ] Application runs end-to-end without crashes
- [ ] Weather data retrieval works (with appropriate API key setup)
- [ ] Both required visualisations display correctly
- [ ] Natural language interface responds to user input
- [ ] Menu system functions properly

**Documentation Check**:
- [ ] At least 5 AI conversation files submitted
- [ ] Before/after code examples present
- [ ] Implementation options exploration documented
- [ ] Reflection document included (300-500 words)

---

## Marker Setup Instructions

### Required Preparation
1. **Google Account**: Ensure access to Google Colab
2. **API Keys**: 
   - OpenWeatherMap API key: Register at openweathermap.org/api
   - Store your key securely for testing Extension Option submissions
3. **GitHub Access**: Verify you can access student repositories

### API Key Testing Protocol
For students using Extension Option (OpenWeatherMap):
```python
# Add this cell at the beginning of their notebook before testing
import os
os.environ['OPENWEATHER_API_KEY'] = 'YOUR_TUTOR_API_KEY_HERE'
```

**Backup Testing Strategy**: If API services are unavailable, focus assessment on:
- Code structure and error handling
- AI conversation quality and prompting techniques
- Implementation logic and design decisions

---

## Detailed Assessment Framework

### I. Initial Submission Check & Setup

#### File Verification
**Primary Deliverable**: Single Google Colab Notebook (.ipynb file)

**Critical Issue**: If student submitted Python scripts (.py) as primary solution instead of notebook, this indicates fundamental misunderstanding of requirements.

**Supporting Files Required**:
- GitHub repository link
- ZIP file of repository (LMS submission)
- AI conversation text files (.txt format)
- Reflection document

#### GitHub Repository Assessment
- [ ] Repository accessible with michael-borck invited
- [ ] README.md present with setup instructions
- [ ] Commit history shows progression (minimum 15 commits)
- [ ] Commits have meaningful messages showing development stages

#### Python Script Import Handling
If notebook imports external .py files:
- **Required**: In-notebook upload mechanism using `files.upload()` or similar
- **Critical Failure**: If imports exist without upload capability, notebook cannot run independently
- **Assessment Impact**: Significant deduction if self-contained requirement not met

---

### II. Weather Data Component & API Management

#### API Source Identification
**Foundation Option** (fetch-my-weather):
- No API key required
- Focus on implementation logic and integration

**Standard Option** (wttr.in direct):
- No API key required
- Assess direct API handling and error management

**Extension Option** (OpenWeatherMap/similar):
- API key management critical
- Eligible for bonus marks with advanced features

#### API Key Security Assessment
**Excellent** (No deduction):
- Uses `os.environ.get("OPENWEATHER_API_KEY")`
- Or prompts user for key input securely

**Acceptable** (Minor deduction):
- Prompts for key but doesn't use secure methods

**Critical Failure** (Major deduction):
- Hardcoded API key visible in code
- No key management mechanism provided

#### Function Implementation Check
Verify presence and functionality of core functions:
```python
def get_weather_data(location, forecast_days=5):
def parse_weather_question(question):
def generate_weather_response(parsed_question, weather_data):
def create_temperature_visualisation(weather_data, output_type='display'):
def create_precipitation_visualisation(weather_data, output_type='display'):
```

---

### III. Core Functionality Assessment

#### Weather Data Component
- [ ] Retrieves and displays current conditions
- [ ] Shows forecast data
- [ ] Handles invalid locations gracefully
- [ ] Includes error handling for API failures

#### Natural Language Interface
- [ ] Accepts plain English weather questions
- [ ] Parses questions to extract intent
- [ ] Provides relevant natural language responses
- [ ] Demonstrates understanding of user queries

#### Visualisation Requirements
- [ ] At least 2 different visualisation types implemented
- [ ] Charts are properly labeled and clear
- [ ] Visualisations relevant to weather data
- [ ] Both temperature and precipitation charts functional

#### User Experience
- [ ] Intuitive menu system (pyinputplus or ipywidgets)
- [ ] Clear instructions provided
- [ ] Appropriate error handling and user feedback
- [ ] Application flow is logical and user-friendly

---

### IV. AI Interaction Assessment Framework

This section carries the highest weight (45% combined) and requires careful evaluation.

#### Intentional Prompting Documentation (30%)

**Implementation Options Exploration**:
- [ ] Student compared all three weather data options
- [ ] Analysis shows technical understanding
- [ ] Decision-making process clearly documented
- [ ] Demonstrates analytical thinking beyond simple Q&A

**Required Prompting Techniques** (Minimum 5 of):
- [ ] Restated problems in own words
- [ ] Identified input/output requirements
- [ ] Requested pseudocode before implementation
- [ ] Challenged edge cases in AI-generated code
- [ ] Requested modular design improvements
- [ ] Asked for code explanations
- [ ] Requested iterative improvements
- [ ] Queried design trade-offs

**Before/After Examples** (Minimum 3):
- [ ] Initial AI-generated code shown
- [ ] Student's specific follow-up prompts documented
- [ ] Improved code resulting from prompts
- [ ] Clear explanation of why prompting was effective

#### AI Conversation Quality (15%)

**Format Requirements**:
- [ ] Plain text files (.txt) - not screenshots
- [ ] Sequential naming (conversation1.txt, etc.)
- [ ] Clear speaker identification ("Me:", "AI:")
- [ ] Meaningful headers for context

**Content Quality Indicators**:
- **Excellent**: Shows iterative refinement, critical evaluation of AI suggestions, handling of incorrect responses, clear problem-solving journey
- **Good**: Some iteration visible, generally thoughtful interactions, mostly appropriate use of AI
- **Poor**: Simple request-response pattern, minimal critical engagement, copy-paste approach

**Red Flags**:
- Screenshots instead of text files (major deduction)
- Very brief, superficial conversations
- No evidence of challenging or refining AI suggestions
- Conversations don't align with implemented code

---

### V. Assessment Criteria: Detailed Grading Framework

#### Functionality (15%)
**Excellent (13-15%)**:
- All core features implemented robustly
- Application handles edge cases appropriately
- Stable performance across different inputs
- Clear evidence of development progression in AI conversations

**Good (8-12%)**:
- Most core features present with minor limitations
- Generally usable application
- Basic error handling implemented
- Some development process visible

**Poor (0-7%)**:
- Missing core features or significant bugs
- Application crashes frequently
- Basic functionality non-operational

#### Code Quality (10%)
**Excellent (9-10%)**:
- Clean, well-organised, readable code
- Consistent naming conventions throughout
- Comprehensive docstrings and comments
- Clear function responsibilities and modularity
- Evidence of code refinement through AI conversations

**Good (6-8%)**:
- Generally well-structured code
- Some documentation and comments present
- Reasonable organisation with room for improvement

**Poor (0-5%)**:
- Disorganised, difficult to follow code
- Minimal or no documentation
- Poor naming conventions and structure

#### Notebook Organisation (10%)
**Excellent (9-10%)**:
- Clear section organisation using markdown cells
- All required sections present and well-developed
- Easy navigation and logical flow
- Evidence of planning in AI conversations

**Good (6-8%)**:
- Some sectioning present but could be clearer
- Most required sections included
- Generally navigable structure

**Poor (0-5%)**:
- Poor or no sectioning
- Difficult to understand notebook flow
- Missing required organisational elements

#### User Experience (10%)
**Excellent (9-10%)**:
- Intuitive, clear interface design
- Excellent error handling and user feedback
- Information well-organised and clearly presented
- Evidence of UI iteration in AI conversations

**Good (6-8%)**:
- Functional interface with room for improvement
- Basic error handling present
- Information adequately presented

**Poor (0-5%)**:
- Confusing or difficult-to-use interface
- Poor or missing error handling
- Unclear information presentation

#### Intentional Prompting (30%)
**Excellent (24-30%)**:
- Comprehensive implementation options analysis
- All required prompting techniques clearly demonstrated
- Strong before/after examples with clear improvements
- Student's active guidance role very apparent

**Good (15-23%)**:
- Most required elements present
- Some prompting techniques evident
- Before/after examples present but may lack depth
- Some evidence of student direction

**Poor (0-14%)**:
- Missing key documentation elements
- Superficial prompting techniques
- Unclear or missing before/after examples
- Little evidence of intentional AI guidance

#### AI Conversation Quality (15%)
**Excellent (13-15%)**:
- At least 5 substantial conversations in correct format
- Clear problem-solving journey documented
- Evidence of critical evaluation and refinement
- Strong demonstration of student thinking process

**Good (8-12%)**:
- Required conversations submitted in correct format
- Some depth and problem-solving visible
- Generally appropriate AI interaction

**Poor (0-7%)**:
- Missing, poorly formatted, or superficial conversations
- Little insight into student thought process
- Inappropriate format (screenshots) or minimal content

#### Technical Implementation (10%)
**Excellent (9-10%)**:
- Appropriate and effective library usage
- Efficient, well-designed implementation
- Good understanding of technical trade-offs
- Evidence of technical decision-making in conversations

**Good (6-8%)**:
- Generally appropriate library use
- Functional implementation with room for optimisation
- Some technical understanding demonstrated

**Poor (0-5%)**:
- Inappropriate library use or inefficient implementation
- Poor understanding of technical concepts
- Overly complex or poorly designed solutions

---

### VI. Bonus Marks (Up to 5% Extra)

**Eligibility**: Only for Standard Option (wttr.in direct) or Extension Option (OpenWeatherMap/similar)

**Bonus Features to Look For**:
- Robust caching mechanisms
- Comprehensive error handling with informative feedback
- Multi-source weather data support
- Advanced data processing for enhanced user experience

**Bonus Award Guidelines**:
- **1-2%**: Basic bonus feature implemented correctly
- **3-4%**: Significant bonus feature or multiple minor ones
- **5%**: Multiple significant features or exceptionally complex implementation

**Evidence Required**: Features must be functional and clearly enhance the application beyond core requirements.

---

### VII. Red Flags & Critical Issues

#### Immediate Disqualification Issues
- **Wrong submission format**: Python scripts as primary deliverable instead of Colab notebook
- **Non-functional dependencies**: Notebook imports files without upload mechanism
- **Screenshot documentation**: AI conversations submitted as images instead of text

#### Major Deduction Issues
- **API security violations**: Hardcoded API keys visible in code
- **Missing core functions**: Required function signatures not implemented
- **Broken functionality**: Application doesn't run or crashes consistently
- **Superficial AI documentation**: No evidence of intentional prompting process

#### Escalation Protocol
- **Zero marks**: For submissions that fundamentally misunderstand assignment requirements
- **Partial credit**: For incomplete but well-documented attempts showing proper process
- **Moderation**: Consult with course coordinator for borderline cases

---

### VIII. Student Feedback Framework

#### Constructive Feedback Templates

**For Technical Issues**:
- "Your implementation shows good understanding of [specific concept], but could be improved by [specific suggestion]"
- "Consider how [specific AI prompting technique] might have helped address [identified issue]"

**For AI Interaction**:
- "Your AI conversations demonstrate good initial prompting, but would benefit from more iterative refinement"
- "Excellent use of [specific prompting technique] - this clearly improved your [specific outcome]"

**For Process Documentation**:
- "Your development process is well-documented. Consider also including [specific missing element]"
- "The progression in your GitHub commits clearly shows your development journey"

#### Avoid These Feedback Patterns
- Don't provide solutions for next assignments
- Avoid being overly prescriptive about specific implementation details
- Don't criticise AI tool choice - focus on how tools were used

---

### IX. Final Review Protocol

#### Before Submitting Marks
- [ ] Cross-reference AI conversations with implemented code
- [ ] Verify GitHub commit history aligns with documented process
- [ ] Confirm bonus marks only awarded for eligible implementations
- [ ] Check all assessment criteria scores add up correctly
- [ ] Ensure feedback is constructive and specific

#### Quality Assurance Checklist
- [ ] Marking rationale clear for any scores below 60%
- [ ] Evidence noted for any bonus marks awarded
- [ ] Consistent application of rubric across all criteria
- [ ] Student's unique contribution clearly identified despite AI assistance

---

## Time Management for Markers

**Phase 1 (10 minutes)**: Initial setup and quick assessment checklist
**Phase 2 (20 minutes)**: Run notebook and assess core functionality
**Phase 3 (15 minutes)**: Review AI conversations and prompting documentation
**Phase 4 (10 minutes)**: Score all criteria and write feedback
**Phase 5 (5 minutes)**: Final review and quality check

**Total**: 60 minutes maximum per submission

---

## Common Edge Cases & Solutions

**Issue**: Notebook won't run due to missing dependencies
**Solution**: Note the issue, attempt manual installation, assess based on code structure if runtime fails

**Issue**: API service temporarily unavailable
**Solution**: Focus on code logic, error handling, and AI conversation quality

**Issue**: Student used unsupported AI tool
**Solution**: Assess based on documented process following alternative documentation guidelines

**Issue**: Unclear whether code is student's or AI-generated
**Solution**: Use AI conversation logs to determine student's contribution and understanding

---

This enhanced marking guide provides clearer structure, specific assessment criteria, and practical guidance for consistent evaluation while maintaining focus on the AI-assisted development process that is central to this assignment.