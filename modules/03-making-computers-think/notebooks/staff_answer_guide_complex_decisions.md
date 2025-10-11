---
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
# Staff Answer Guide: Complex Decision Logic with AI

## 🎯 Session Overview

**Duration**: 45 minutes  
**Learning Objectives**: Students will learn to analyze complex multi-factor problems, design logical decision systems, and collaborate effectively with AI tools.

**Key Skills Developed**:
- Problem decomposition and systematic analysis
- Boolean logic and conditional statements
- Debugging complex logical expressions
- Effective AI collaboration strategies

---

## 🚀 Engaging Opening Hook (5 minutes)

### "The Netflix Dilemma" Interactive Demonstration

**Setup**: Ask students to open their Netflix/streaming app or imagine they're designing one.

**Hook Question**: *"Why did Netflix just recommend 'The Great British Baking Show' to someone who only watches action movies?"*

**Interactive Discussion**:
1. **Crowd-source factors**: "What should Netflix consider when recommending?" (Let them brainstorm: viewing history, time of day, device, mood, ratings, etc.)
2. **Reveal complexity**: Show how even 4-5 factors create 2^n possible combinations
3. **The challenge**: "Today you'll learn to think like these recommendation systems - but for problems YOU care about"

**Transition**: "Every interesting decision involves multiple factors. Today you'll master the art of thinking through these systematically."

---

## 📋 Activity 1: Problem Decomposition (15 minutes)

### Model Answer: Gaming Achievement System

#### Strong Student Examples:

**Achievement 1: "Master Strategist"**
- Requires: Win 5 games in a row AND average game time < 10 minutes AND use at least 3 different strategies
- Logic: `(consecutive_wins >= 5) AND (avg_game_time < 10) AND (strategies_used >= 3)`

**Achievement 2: "Community Champion"**  
- Requires: Help 20+ other players OR donate 1000+ in-game currency OR host 5+ community events
- Logic: `(players_helped >= 20) OR (donations >= 1000) OR (events_hosted >= 5)`

**Achievement 3: "Night Warrior"**
- Requires: Play between 10PM-6AM AND maintain 80%+ win rate AND play for 7 consecutive days
- Logic: `(play_time in night_hours) AND (win_rate >= 0.8) AND (consecutive_days >= 7)`

### Teaching Tips:

**🔍 Common Pitfalls:**
- Students often make logic too simple (only 2 conditions)
- Forgetting edge cases (what if someone plays at exactly 10PM?)
- Using impossible thresholds (requiring 100% win rate)

**💡 Coaching Strategies:**
- Ask "What makes this achievement special/challenging?"
- Push for specificity: "How many exactly?" instead of "a lot"
- Encourage testing: "Walk me through someone who should just barely qualify"

**🤖 AI Collaboration Guidance:**
- **Good prompt**: "I'm designing an achievement called [name] that requires [conditions]. Does this logic make sense? What edge cases should I consider?"
- **Follow-up**: "How could I make this more balanced between challenging and achievable?"
- **Avoid**: Letting AI generate the entire achievement concept

---

## 💻 Activity 2: Logic Implementation Challenge (20 minutes)

### Model Answer: College Admissions System

```python
def evaluate_application(gpa, sat_score, extracurriculars, essay_score, leadership_roles, special_circumstances=False):
    """
    College Admissions Decision System
    
    Admission criteria:
    - Strong Academic: (GPA >= 3.7 AND SAT >= 1400) OR (GPA >= 3.9)
    - Well-Rounded: extracurriculars >= 3 AND leadership_roles >= 1
    - Strong Communication: essay_score >= 8
    - Special consideration for unique circumstances
    """
    
    # Academic strength check
    strong_academic = (gpa >= 3.7 and sat_score >= 1400) or (gpa >= 3.9)
    
    # Well-rounded check  
    well_rounded = extracurriculars >= 3 and leadership_roles >= 1
    
    # Communication skills
    strong_communication = essay_score >= 8
    
    # Main admission logic
    if strong_academic and well_rounded and strong_communication:
        return "ACCEPTED - Excellent all-around candidate"
    elif strong_academic and (well_rounded or strong_communication):
        if special_circumstances:
            return "ACCEPTED - Strong academics with special consideration"
        else:
            return "WAITLIST - Strong potential, competitive pool"
    elif special_circumstances and (strong_academic or (well_rounded and strong_communication)):
        return "ACCEPTED - Unique circumstances and demonstrated potential"
    else:
        return "DENIED - Does not meet minimum criteria"

# Test cases
test_cases = [
    {"gpa": 3.8, "sat_score": 1450, "extracurriculars": 4, "leadership_roles": 2, "essay_score": 9},  # Should accept
    {"gpa": 3.5, "sat_score": 1200, "extracurriculars": 2, "leadership_roles": 0, "essay_score": 6},  # Should deny
    {"gpa": 3.6, "sat_score": 1350, "extracurriculars": 5, "leadership_roles": 1, "essay_score": 7, "special_circumstances": True}  # Borderline with special circumstances
]

for i, case in enumerate(test_cases, 1):
    result = evaluate_application(**case)
    print(f"Test Case {i}: {result}")
```

### Alternative Simpler Implementation:

```python
def college_admission_decision(gpa, test_score, activities, essay_rating):
    """Simplified admissions system focusing on clear logic"""
    
    print(f"\nEvaluating application:")
    print(f"GPA: {gpa}, Test Score: {test_score}, Activities: {activities}, Essay: {essay_rating}/10")
    
    # Define thresholds
    min_gpa = 3.0
    min_test = 1200
    min_activities = 2
    min_essay = 6
    
    # Check each criterion
    gpa_met = gpa >= min_gpa
    test_met = test_score >= min_test  
    activities_met = activities >= min_activities
    essay_met = essay_rating >= min_essay
    
    print(f"\nCriteria met: GPA({gpa_met}) Test({test_met}) Activities({activities_met}) Essay({essay_met})")
    
    # Decision logic: need to meet at least 3 out of 4 criteria
    criteria_met = sum([gpa_met, test_met, activities_met, essay_met])
    
    if criteria_met >= 3:
        # Extra check for academic minimum
        if gpa >= 2.5 and test_score >= 1000:
            return "ACCEPTED"
        else:
            return "DENIED - Below academic minimum"
    else:
        return "DENIED - Insufficient criteria met"

# Example usage
result = college_admission_decision(3.4, 1350, 3, 7)
print(f"\nDecision: {result}")
```

### Teaching Strategies:

**🎯 Guided Implementation Approach:**
1. **Start with pseudocode**: Have students write logic in plain English first
2. **Build incrementally**: Start with simple if/else, then add complexity
3. **Test early and often**: Run code with simple test cases first

**🔍 Common Student Mistakes:**
- **Operator precedence issues**: `a and b or c` vs `a and (b or c)`
- **Assignment vs comparison**: Using `=` instead of `==`
- **Logic errors**: Confusing AND/OR relationships
- **Edge case handling**: Not considering boundary values

**💡 Debugging Coaching:**
- "Walk me through what happens when GPA is exactly 3.7"
- "What should happen if someone meets all criteria? Let's trace through the code"
- "Can you give me an input that would break this logic?"

**🤖 AI Collaboration Strategies:**

**For Logic Design:**
```
Good prompt: "I want to check if a student meets admission criteria where they need strong academics (GPA 3.5+ OR test score 1400+) AND at least one of (leadership experience OR exceptional essay). How should I structure this logic?"

Follow-up: "Can you help me identify potential edge cases in this logic?"
```

**For Implementation Review:**
```
Good prompt: "Here's my admissions code: [paste code]. Does this implement my intended logic correctly? I want to accept students who meet criteria A AND (criteria B OR criteria C)."

Avoid: "Write a college admissions system for me"
```

---

## 🐛 Activity 3: Debugging Complex Logic (10 minutes)

### The Problem Analysis:

**Original buggy code:**
```python
if gpa >= 3.0 and community_hours >= 50 or financial_need == "yes" and essay_score >= 7:
```

**What it actually checks (due to operator precedence):**
```python
if (gpa >= 3.0 and community_hours >= 50) or (financial_need == "yes" and essay_score >= 7):
```

**What it SHOULD check:**
```python
if gpa >= 3.0 and (community_hours >= 50 or financial_need == "yes") and essay_score >= 7:
```

### Model Answer: Corrected Code

```python
print("=== Scholarship Eligibility Checker (CORRECTED) ===")

gpa = float(input("Enter GPA (0.0-4.0): "))
community_hours = int(input("Community service hours: "))
financial_need = input("Have financial need? (yes/no): ").lower()
essay_score = int(input("Essay score (1-10): "))

# Corrected logic: GPA 3.0+ AND (community hours 50+ OR financial need) AND essay 7+
if gpa >= 3.0 and (community_hours >= 50 or financial_need == "yes") and essay_score >= 7:
    print("✅ Eligible for scholarship!")
    print(f"Qualified with: GPA {gpa}, {community_hours} service hours, financial need: {financial_need}, essay score: {essay_score}")
else:
    print("❌ Not eligible")
    
    # Helpful feedback on what's missing
    issues = []
    if gpa < 3.0:
        issues.append(f"GPA {gpa} below minimum 3.0")
    if community_hours < 50 and financial_need != "yes":
        issues.append("Need either 50+ service hours OR financial need")
    if essay_score < 7:
        issues.append(f"Essay score {essay_score} below minimum 7")
    
    if issues:
        print("Missing requirements:", ", ".join(issues))
```

### Teaching the Debugging Process:

**🔍 Step-by-Step Approach:**

1. **Understand Intent**: "What was the programmer trying to achieve?"
2. **Trace Execution**: "Let's walk through this with specific values"
3. **Identify Precedence**: "What gets evaluated first in this expression?"
4. **Test Edge Cases**: "When would this give unexpected results?"
5. **Fix and Verify**: "Does our fix handle all the cases correctly?"

**💡 Interactive Debugging Technique:**
- Use specific test values: GPA=3.2, hours=30, need=yes, essay=8
- Trace through original logic step by step
- Show how parentheses change the result

**🤖 AI Debugging Collaboration:**

**Effective Approach:**
```
Tutor prompt to demonstrate: "I have this conditional logic that should check (A AND (B OR C) AND D), but it's not working correctly. Can you help me understand operator precedence in this expression: [paste expression]"

Follow-up: "Can you show me how to use parentheses to make this logic clearer?"
```

**Less Effective:**
```
"Fix this code" (too direct, doesn't teach debugging process)
```

---

## 🎨 Advanced Challenge: Design Your Own System

### Sample Solutions by Domain:

#### Music Recommendation System:
```python
def recommend_music(user_history, current_mood, time_of_day, weather, social_context):
    """
    Music recommendation based on multiple factors
    """
    recommendations = []
    
    # Time-based preferences
    if time_of_day in ["morning", "afternoon"]:
        energy_preference = "high" if current_mood in ["happy", "motivated"] else "medium"
    else:  # evening/night
        energy_preference = "low" if current_mood in ["relaxed", "tired"] else "medium"
    
    # Weather influence
    if weather == "rainy" and current_mood != "happy":
        genre_boost = ["indie", "acoustic", "classical"]
    elif weather == "sunny":
        genre_boost = ["pop", "rock", "reggae"]
    else:
        genre_boost = user_history["favorite_genres"][:3]
    
    # Social context
    if social_context == "alone":
        recommend_personal_favorites = True
    else:
        recommend_personal_favorites = False
        genre_boost = ["pop", "rock"]  # more universally appealing
    
    return {
        "energy_level": energy_preference,
        "recommended_genres": genre_boost,
        "personalization_level": "high" if recommend_personal_favorites else "medium"
    }
```

#### Job Application Screening:
```python
def screen_application(years_experience, education_level, skills_match, culture_fit_score, references):
    """
    Initial job application screening system
    """
    # Define scoring criteria
    experience_score = min(years_experience * 20, 100)  # Cap at 100
    education_bonus = {"phd": 30, "masters": 20, "bachelors": 10, "other": 0}
    education_score = education_bonus.get(education_level.lower(), 0)
    
    # Calculate total score
    total_score = (
        experience_score * 0.4 +  # 40% weight
        skills_match * 0.3 +      # 30% weight (0-100 scale)
        culture_fit_score * 0.2 + # 20% weight (0-100 scale)
        education_score * 0.1     # 10% weight
    )
    
    # Decision logic
    if total_score >= 75 and references >= 2:
        return "INTERVIEW - Strong candidate"
    elif total_score >= 60 and (skills_match >= 80 or culture_fit_score >= 85):
        return "INTERVIEW - Good potential"
    elif total_score >= 50:
        return "MAYBE - Review manually"
    else:
        return "REJECT - Below threshold"
```

### Coaching Advanced Students:

**🎯 Challenge Them With:**
- "How would you handle conflicting criteria?"
- "What happens when your system needs to learn and adapt?"
- "How do you ensure fairness across different user groups?"
- "What would you do if you had incomplete information?"

---

## 🎓 Assessment Rubric & Common Student Challenges

### Competency Levels:

**🥉 Beginner (Struggling)**:
- Can identify factors but struggles with logic relationships
- Makes basic syntax errors in conditionals
- Doesn't test their logic systematically
- Asks AI to write entire solutions

**🥈 Developing (On Track)**:
- Designs logical multi-factor systems with guidance
- Implements basic conditional logic correctly
- Tests with some scenarios but misses edge cases
- Uses AI for clarification and syntax help

**🥇 Proficient (Exceeding)**:
- Independently designs sophisticated decision systems
- Handles complex logic with proper precedence
- Systematically tests including edge cases
- Collaborates with AI as a thinking partner

**🏆 Advanced (Mastery)**:
- Creates elegant, maintainable decision systems
- Considers fairness, bias, and real-world implications
- Teaches concepts to other students
- Uses AI to explore alternative approaches and optimizations

### Red Flags to Watch For:

**🚨 Technical Issues:**
- Confusing `=` and `==`
- Logical operator precedence errors
- Not handling user input validation
- Infinite loops in complex conditions

**🚨 Conceptual Issues:**
- Creating overly complex logic for simple problems
- Not considering edge cases or boundary conditions
- Designing unfair or biased decision systems
- Not testing their logic thoroughly

**🚨 AI Collaboration Issues:**
- Copying AI solutions without understanding
- Not verifying AI suggestions against their intent
- Using AI as a search engine rather than thinking partner
- Over-relying on AI for basic syntax

---

## 🤖 AI Integration Guidelines for Tutors

### During Live Sessions:

**✅ Encourage These AI Interactions:**

1. **Logic Review**: "I designed this decision system [describe]. Can you help me check if my logic makes sense?"

2. **Concept Clarification**: "I'm confused about when to use AND vs OR in this scenario. Can you explain the difference with an example?"

3. **Debugging Partnership**: "My condition isn't working as expected. Can you help me trace through what happens when [specific input]?"

4. **Implementation Discussion**: "I have this logic design [describe]. What's the clearest way to implement this in Python?"

**❌ Discourage These Approaches:**

1. **Direct Solutions**: "Write a college admissions system"
2. **Vague Requests**: "Fix my code"
3. **Over-Reliance**: Using AI for every small syntax question
4. **Copy-Paste**: Taking AI code without understanding it

### Tutor AI Prompting Strategies:

**For Generating Hints (Not Solutions):**
```
"A student is trying to implement logic that checks if (condition A AND (condition B OR condition C)). They're getting confused about operator precedence. Can you suggest a way to explain this concept without giving them the exact code?"
```

**For Creating Additional Examples:**
```
"I need 2-3 more examples of multi-factor decision systems that students could design and implement. They should be engaging for college students but not too complex for a 45-minute session."
```

**For Debugging Assistance:**
```
"A student wrote this logic: [paste code]. It should check X but it's actually checking Y. How can I guide them to discover the error themselves rather than just telling them the answer?"
```

---

## 💬 Facilitating Rich Discussions

### Key Discussion Questions:

**🧠 Technical Depth:**
- "When you have 4 conditions, how do you decide which ones are most important?"
- "What's the difference between making a decision system strict vs. flexible?"
- "How do you balance simplicity with accuracy in decision logic?"

**🌍 Real-World Applications:**
- "Where do you encounter decision systems in your daily life?"
- "What makes a decision system fair vs. biased?"
- "How should decision systems handle incomplete information?"

**🤝 AI Collaboration:**
- "When was AI most helpful in your problem-solving process today?"
- "How do you know when to trust vs. verify AI suggestions?"
- "What's the difference between AI helping you think vs. AI thinking for you?"

### Managing Common Situations:

**😤 "This is too complicated!"**
- Response: "Let's break it down. What's ONE decision you make that has TWO factors?"
- Follow-up: Build complexity gradually from there

**🤖 "AI just gave me the answer!"**
- Response: "Great! Now explain to me how it works and what would happen if we changed [specific condition]."
- Follow-up: Use this as a teaching moment about verification

**⚡ "I finished early!"**
- Challenge: "Design a system for something you actually care about - what decision do YOU make that could be automated?"
- Extension: "How would you make your system learn and improve over time?"

---

## 📚 Additional Resources & Extensions

### For Students Who Want More:

**🔗 Recommended Practice Problems:**
- LeetCode: Boolean logic problems
- Codewars: Decision tree challenges  
- Real-world datasets: Build recommendation systems

**📖 Conceptual Extensions:**
- Machine learning decision trees
- Ethical AI and algorithmic bias
- Game theory and multi-agent systems

### For Tutors to Deepen Understanding:

**📚 Background Reading:**
- "Algorithms to Live By" - Christian & Griffiths
- "Thinking, Fast and Slow" - Kahneman (decision-making psychology)
- "The Master Algorithm" - Domingos (machine learning fundamentals)

**🛠️ Technical Skills to Develop:**
- Boolean algebra and formal logic
- Decision tree algorithms
- Basic machine learning concepts
- Ethical considerations in automated decision-making

---

## 🎯 Session Success Indicators

**✅ You'll know the session was successful when:**

- Students can design multi-factor decision systems independently
- Students ask specific, thoughtful questions about logic relationships
- Students test their systems with realistic scenarios
- Students use AI as a collaborator, not a solution provider
- Students connect the concepts to real-world applications they care about
- Students help each other debug and improve their logic

**✅ Students leave with:**

- Confidence in breaking down complex problems systematically
- Understanding of boolean logic and conditional statements  
- Experience collaborating effectively with AI tools
- Appreciation for the complexity of real-world decision systems
- Practical skills they can apply to future programming challenges

**Remember**: The goal isn't perfect code - it's developing systematic thinking and effective AI collaboration skills that will serve them throughout their careers!