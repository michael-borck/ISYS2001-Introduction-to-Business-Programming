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

# 🎓 Week 8 Facilitator's Guide: The Pivot to AI-Assisted Programming

**ISYS2001: Introduction to Business Programming**  
**Week 8: Business Data Processing & Assignment Launch**  
**Duration:** 2 hours  
**Key Message:** "Today you become code directors, not code writers - and start your final assignment!"

---

## 🎯 Session Overview & Learning Objectives

### Primary Goals
- **Workflow Transformation**: Students transition from writing code to directing AI
- **Assignment Launch**: Students successfully start their Smart Finance Assistant project
- **Confidence Building**: Reduce assignment anxiety through guided beginning
- **AI Collaboration Skills**: Establish effective AI prompting and critique practices

### Success Criteria
By session end, students should have:
- ✅ Forked assignment repository and made first commit
- ✅ Working CSV data processing with AI assistance
- ✅ Documented 3+ AI interactions in Developer's Diary
- ✅ Generated business insights from transaction data
- ✅ Completed Week 8 exit ticket requirements

---

## ⏰ Detailed Session Timeline

### Pre-Session Setup (15 minutes before class)
- [ ] Test all sample CSV files load correctly
- [ ] Verify GitHub template repository is accessible
- [ ] Check Quarto renders properly for demonstrations
- [ ] Prepare backup plans for common technical issues

---

## 📋 Part 1: Mindset Shift Demo (20 minutes)

### Opening Hook (5 minutes)
**Script**: *"Congratulations! You've reached the most important moment in this course. Today you stop being code writers and become code directors. Even better - you're starting your final assignment and will make real progress on it today."*

**Key Points to Emphasize**:
- This isn't about learning more syntax - it's about changing workflow
- Assignment anxiety ends today because they'll start it together
- Modern professional practice involves AI collaboration
- BIS graduates direct technology solutions, not write every line

### Old vs New Demonstration (15 minutes)

**Live Demo Structure**:
1. **Show traditional approach** (5 minutes)
   - Manually write pandas code with syntax struggles
   - Demonstrate common errors and debugging time
   - "This is how you learned in Weeks 1-7"

2. **Show AI collaboration approach** (7 minutes)
   - Demonstrate effective AI prompting
   - Show immediate, working solutions
   - Highlight code quality improvements
   - "This is your new workflow"

3. **Assignment Connection** (3 minutes)
   - "Your Smart Finance Assistant uses exactly these skills"
   - "You'll finish today 10% done with your final project"

**Facilitator Notes**:
- Use the provided sample code examples
- Make mistakes intentionally in traditional approach
- Show genuine surprise/delight at AI results
- Keep energy high - this should feel exciting!

---

## 🤖 Part 2: Guided Practice with Sample Data (30 minutes)

### Setup Phase (5 minutes)
**Student Actions**:
- Load the workshop notebook
- Import necessary libraries
- Load `transactions.csv` data

**Facilitator Role**:
- Circulate to help with technical setup
- Address common import/file path issues
- Ensure all students have data loaded before proceeding

### Guided AI Collaboration (20 minutes)

**Exercise 1: Basic Analysis** (10 minutes)
- **Facilitator demonstrates** effective AI prompting live
- **Students attempt** same analysis with their own AI interactions
- **Key Teaching Moment**: Show how to improve AI responses

**Sample Prompts to Model**:
```
"I have CSV transaction data with columns Date, Amount, Category, Description. 
The Amount column has dollar signs. I want to calculate total spending by 
category and show results sorted from highest to lowest. Please write pandas 
code with comments explaining each step."
```

**Exercise 2: Critique Practice** (10 minutes)
- Show example of poor AI code
- Demonstrate critique process
- Students practice improving AI responses

**Facilitator Notes**:
- Don't let students get stuck on syntax errors
- Focus on AI communication, not pandas mastery
- Encourage multiple students to share their AI interactions
- Address the "is this cheating?" question directly

### Wrap-up and Transition (5 minutes)
- **Celebrate** working solutions
- **Connect** to assignment requirements
- **Build excitement** for starting their actual project

---

## 🏗️ Part 3: Assignment Setup (20 minutes)

### Repository Fork and Clone (10 minutes)

**Step-by-step guidance**:
1. Navigate to template repository
2. Fork to personal account
3. Clone or open in preferred environment
4. Explore project structure

**Common Issues and Solutions**:

| Issue | Symptoms | Solution |
|-------|----------|----------|
| Fork not visible | Student can't find their fork | Check they're logged into correct GitHub account |
| Clone fails | Permission denied errors | Ensure SSH keys or use HTTPS method |
| Wrong repository | Working in template not fork | Guide to check repository URL |
| File path issues | Can't load CSV files | Show relative path structure |

**Facilitator Notes**:
- Have students work in pairs for this section
- Pre-identify students who might struggle with Git
- Keep energy focused on "starting your assignment"

### Project Structure Exploration (10 minutes)

**Guided Tour**:
- **Main notebook**: "This is where you'll build everything"
- **Developer's Diary**: "This is worth 20% of your grade"
- **Data folder**: "Your transaction files go here"
- **README**: "Professional documentation"

**Key Message**: *"You're not starting from scratch - you have professional structure and clear guidance"*

---

## 🚀 Part 4: Start Your Assignment! (40 minutes)

### Transition Messaging (5 minutes)
**Script**: *"This is it - the moment you officially start your Smart Finance Assistant. By the end of today, you'll have made genuine progress on your final project. No more assignment anxiety!"*

### Guided Implementation (30 minutes)

**Phase 1: Data Loading** (10 minutes)
- Students work in assignment notebook
- Use AI to create robust data loading code
- Facilitator circulates providing individual support
- Focus on documenting AI interactions

**Phase 2: Analysis Functions** (15 minutes)
- Create spending summary functions with AI help
- Practice critique and improvement
- Generate business insights

**Phase 3: Documentation** (5 minutes)
- Update Developer's Diary with AI interactions
- Write clear commit message
- Prepare for final commit

**Facilitator Strategies**:
- **Pair students** if some are struggling
- **Share good examples** from circulating observations
- **Manage pace** - better to have working basics than incomplete advanced features
- **Celebrate progress** publicly to maintain motivation

### Documentation and Reflection (5 minutes)
- Ensure diary entries are being made
- Check that AI interactions are being recorded
- Verify exit ticket requirements are met

---

## 💾 Part 5: Commit and Reflect (10 minutes)

### Git Commit Ceremony (7 minutes)

**Build this up as significant moment**:
- "You're about to make your first commit on your final assignment"
- Guide through proper commit message format
- Have students announce when they've successfully committed

**Model Commit Message**:
```
Week 8: Initial CSV processing and analysis implemented

- Set up data loading with error handling
- Created spending analysis functions
- Generated business insights report
- Documented AI collaboration in diary

🤖 Generated with AI assistance - see diary.md for details
```

### Success Celebration (3 minutes)
- Public acknowledgment of progress
- Reinforce what they've accomplished
- Build excitement for Week 9

---

## 🔧 Troubleshooting Guide

### Technical Issues

**Git/GitHub Problems**:
- Keep backup of template files locally
- Have GitHub Desktop as alternative to command line
- Pre-create class organization if needed

**Python/Pandas Errors**:
- Focus on AI collaboration, not debugging syntax
- Have working code examples ready to share
- Redirect to AI for error resolution

**File Path Issues**:
- Standardize on relative paths in examples
- Have students check current working directory
- Provide absolute path examples as backup

### Pedagogical Challenges

**"Is This Cheating?" Concerns**:
- Address directly and positively
- Reference professional practice norms
- Emphasize learning objectives (business problem-solving)
- Point to assignment rubric showing AI collaboration is required

**Students Overwhelmed by Assignment Scope**:
- Return focus to today's achievable goals
- Emphasize incremental weekly progress
- Show how today's work maps to final requirements
- Pair struggling students with confident ones

**Advanced Students Wanting More**:
- Direct to practice notebook for additional challenges
- Have them help struggling classmates
- Suggest exploring business contexts more deeply

### Pacing Issues

**Running Behind Schedule**:
1. Skip advanced examples in guided practice
2. Reduce discussion time in favor of hands-on work
3. Have students continue assignment work at home
4. Focus on exit ticket completion over perfection

**Finishing Early**:
1. Direct to practice notebook exercises
2. Encourage peer mentoring
3. Discuss Week 9 preview material
4. Have students explore assignment enhancement options

---

## 📊 Exit Ticket Assessment

### Real-time Progress Checking

**Walk around and verify**:
- Repository successfully forked
- CSV data loads without errors
- At least one analysis function works
- Developer's Diary has entries
- Student can explain their AI interactions

### Success Indicators
- Student demonstrates working data processing
- Can articulate how AI helped solve problems
- Shows evidence of critique/improvement process
- Has made meaningful Git commit
- Expresses confidence about continuing assignment

### Red Flags Requiring Intervention
- No working code after 40 minutes of assignment time
- Haven't successfully forked repository
- No diary entries or AI documentation
- Expressing high anxiety about assignment
- Technical setup preventing progress

---

## 🎨 Creating the Right Atmosphere

### Energy Management
- **High energy** for workflow transition demo
- **Supportive focus** during technical setup
- **Celebratory** for assignment milestone moments
- **Encouraging** when students struggle

### Key Messages to Reinforce
- "You're now code directors, not code writers"
- "Your assignment is already 10% complete!"
- "AI is your junior developer - you review its work"
- "Start simple, then iterate"
- "Modern professionals work this way"

### Handling Resistance
- Some students may resist AI workflow
- Acknowledge their concerns but maintain course direction
- Reference industry practice and future career needs
- Show concrete benefits through working examples

---

## 📝 Post-Session Follow-up

### Immediate Actions
- [ ] Check all students made their first commit
- [ ] Review diary entries for AI collaboration evidence
- [ ] Identify students needing additional support
- [ ] Prepare Week 9 materials building on today's foundation

### Week 9 Preparation Notes
- Students should have working CSV processing foundation
- Developer's Diary should have Week 8 entries
- Assignment repositories should be active and accessible
- AI collaboration workflow should be established

### Success Metrics
- **Participation**: Students actively engaged with AI tools
- **Technical**: Working data processing in assignment notebooks
- **Documentation**: Evidence of AI collaboration in diaries
- **Confidence**: Reduced anxiety about final assignment
- **Commitment**: First meaningful Git commits completed

---

## 💡 Facilitator Success Tips

### Before the Session
- Practice the AI collaboration demos yourself
- Test all technical components thoroughly
- Prepare for GitHub issues (common at universities)
- Have backup plans for every major component

### During the Session
- **Model the AI workflow** extensively - students learn by watching
- **Celebrate small wins** publicly to build confidence
- **Focus on progress over perfection** - working basics beat advanced failures
- **Connect everything to assignment value** - maintain motivation

### After the Session
- **Follow up with struggling students** quickly
- **Share success stories** to build class confidence
- **Document common issues** for future sessions
- **Prepare Week 9** based on actual student progress

**Remember**: This session sets the tone for the remainder of the course. Students should leave feeling excited about their assignment and confident in their new AI collaboration skills. The goal is transformation - they should feel like different programmers than they were 2 hours ago!