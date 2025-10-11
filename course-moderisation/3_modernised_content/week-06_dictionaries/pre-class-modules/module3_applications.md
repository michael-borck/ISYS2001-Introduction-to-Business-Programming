---
title: "Module 3: Dictionary Applications"
subtitle: "Part of Week 6: Organising Your Thoughts (with Dictionaries)"
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

# Module Overview
- **Duration:** 20 minutes
- **Position:** Module 3 of 3
- **Prerequisites:** Modules 1 and 2 completed

# Learning Objectives
After this module, you will be able to:
- [ ] Design and work with nested dictionaries for hierarchical data
- [ ] Transform parallel list structures into dictionary-based solutions
- [ ] Apply dictionary patterns to solve real-world problems
- [ ] Prepare for implementing dictionary solutions in your finance tracker

---

# Nested Dictionaries: Storing Complex Information

## Why Nested Dictionaries?

Sometimes you need to store information that has multiple levels. Think about a university system:
- Each **student** has personal details
- Each **student** has multiple **courses**  
- Each **course** has its own details

Nested dictionaries let you model this naturally!

## Example: Student Academic Record

```python
# A comprehensive student record using nested dictionaries
student_record = {
    "S12345": {
        "personal": {
            "name": "Alice Chen",
            "email": "alice.chen@university.edu",
            "program": "Information Systems",
            "year": 2
        },
        "academic": {
            "gpa": 3.8,
            "credits_completed": 72,
            "status": "Full-time"
        },
        "courses": {
            "ISYS2001": {
                "title": "Business Programming",
                "credits": 6,
                "grade": 85,
                "semester": "2024-S2"
            },
            "MATH101": {
                "title": "Mathematics Foundations", 
                "credits": 6,
                "grade": 92,
                "semester": "2024-S1"
            }
        }
    }
}
```

## Accessing Nested Data

```python
# Access Alice's name (3 levels deep!)
student_id = "S12345"
alice_name = student_record[student_id]["personal"]["name"]
print(f"Student name: {alice_name}")

# Access her ISYS2001 grade
isys_grade = student_record[student_id]["courses"]["ISYS2001"]["grade"]
print(f"ISYS2001 grade: {isys_grade}")

# Calculate total credits from all courses
total_credits = 0
for course_info in student_record[student_id]["courses"].values():
    total_credits += course_info["credits"]
print(f"Total course credits: {total_credits}")
```

**Output:**
```
Student name: Alice Chen
ISYS2001 grade: 85
Total course credits: 12
```

## Safe Access with Nested Dictionaries

```python
# Safe access using .get() at each level
def get_student_grade(records, student_id, course_code):
    """Safely get a student's grade for a specific course"""
    student = records.get(student_id, {})
    courses = student.get("courses", {})
    course = courses.get(course_code, {})
    return course.get("grade", "Not found")

# Test with existing and non-existing data
print(get_student_grade(student_record, "S12345", "ISYS2001"))  # 85
print(get_student_grade(student_record, "S12345", "PHYS101"))   # Not found
print(get_student_grade(student_record, "S99999", "ISYS2001")) # Not found
```

---

# From Parallel Lists to Dictionaries

## The Problem with Parallel Lists

Remember from Module 1? Let's see a more complex example of why parallel lists become problematic:

```python
# ❌ Managing student data with parallel lists (messy!)
student_ids = ["S12345", "S67890", "S11111"]
names = ["Alice Chen", "Bob Smith", "Charlie Davis"]
programs = ["Information Systems", "Computer Science", "Business"]
years = [2, 1, 3]
gpas = [3.8, 3.2, 3.9]
emails = ["alice@uni.edu", "bob@uni.edu", "charlie@uni.edu"]

# To find all info about Alice:
alice_index = student_ids.index("S12345")
alice_info = {
    "name": names[alice_index],
    "program": programs[alice_index], 
    "year": years[alice_index],
    "gpa": gpas[alice_index],
    "email": emails[alice_index]
}
print("Alice's info:", alice_info)
```

**Problems:**
- 6 separate lists to maintain
- Easy to make index errors
- Hard to add new students
- Difficult to add new fields
- Complex code for simple operations

## ✅ The Dictionary Solution

```python
# ✅ Same data organized as a dictionary (clean!)
students = {
    "S12345": {
        "name": "Alice Chen",
        "program": "Information Systems",
        "year": 2,
        "gpa": 3.8,
        "email": "alice@uni.edu"
    },
    "S67890": {
        "name": "Bob Smith", 
        "program": "Computer Science",
        "year": 1,
        "gpa": 3.2,
        "email": "bob@uni.edu"
    },
    "S11111": {
        "name": "Charlie Davis",
        "program": "Business", 
        "year": 3,
        "gpa": 3.9,
        "email": "charlie@uni.edu"
    }
}

# To find all info about Alice (much simpler!):
alice_info = students["S12345"]
print("Alice's info:", alice_info)
```

**Benefits:**
- All related data grouped together
- Direct access by meaningful ID
- Easy to add new students or new fields
- Intuitive and readable code
- Much less chance of errors

---

# Real-World Problem-Solving Patterns

## Pattern 1: Data Aggregation and Analysis

```python
def analyze_student_data(students_dict):
    """Analyze student performance across the class"""
    analysis = {
        "total_students": len(students_dict),
        "programs": {},
        "year_levels": {},
        "gpa_stats": {
            "gpas": [],
            "average": 0,
            "highest": 0,
            "lowest": 0
        }
    }
    
    # Collect data for analysis
    for student_id, info in students_dict.items():
        # Count programs
        program = info["program"]
        analysis["programs"][program] = analysis["programs"].get(program, 0) + 1
        
        # Count year levels
        year = info["year"] 
        analysis["year_levels"][year] = analysis["year_levels"].get(year, 0) + 1
        
        # Collect GPAs
        analysis["gpa_stats"]["gpas"].append(info["gpa"])
    
    # Calculate GPA statistics
    gpas = analysis["gpa_stats"]["gpas"]
    if gpas:
        analysis["gpa_stats"]["average"] = sum(gpas) / len(gpas)
        analysis["gpa_stats"]["highest"] = max(gpas)
        analysis["gpa_stats"]["lowest"] = min(gpas)
    
    return analysis

# Run the analysis
results = analyze_student_data(students)
print("Class Analysis:")
print(f"Total students: {results['total_students']}")
print(f"Programs: {results['programs']}")
print(f"Year levels: {results['year_levels']}")
print(f"Average GPA: {results['gpa_stats']['average']:.2f}")
```

## Pattern 2: Data Transformation and Export

```python
def create_student_report(students_dict):
    """Transform student data into a formatted report"""
    report = []
    
    for student_id, info in students_dict.items():
        # Create a summary for each student
        student_summary = {
            "ID": student_id,
            "Name": info["name"],
            "Program": info["program"],
            "Year": f"Year {info['year']}",
            "GPA": f"{info['gpa']:.2f}",
            "Status": "Dean's List" if info["gpa"] >= 3.5 else "Good Standing" if info["gpa"] >= 2.0 else "Probation"
        }
        report.append(student_summary)
    
    return report

# Generate and display report
report = create_student_report(students)
print("\nStudent Report:")
print("-" * 60)
for student in report:
    print(f"{student['ID']}: {student['Name']} ({student['Program']}, {student['Year']}) - GPA: {student['GPA']} - {student['Status']}")
```

## Pattern 3: Dynamic Dictionary Building

```python
def build_program_statistics(students_dict):
    """Build statistics grouped by academic program"""
    program_stats = {}
    
    for student_id, info in students_dict.items():
        program = info["program"]
        
        # Initialize program entry if it doesn't exist
        if program not in program_stats:
            program_stats[program] = {
                "count": 0,
                "students": [],
                "total_gpa": 0,
                "year_distribution": {}
            }
        
        # Update statistics
        program_stats[program]["count"] += 1
        program_stats[program]["students"].append(info["name"])
        program_stats[program]["total_gpa"] += info["gpa"]
        
        year = info["year"]
        program_stats[program]["year_distribution"][year] = program_stats[program]["year_distribution"].get(year, 0) + 1
    
    # Calculate averages
    for program, stats in program_stats.items():
        stats["average_gpa"] = stats["total_gpa"] / stats["count"]
    
    return program_stats

# Build and display program statistics
program_stats = build_program_statistics(students)
print("\nProgram Statistics:")
print("-" * 40)
for program, stats in program_stats.items():
    print(f"{program}:")
    print(f"  Students: {stats['count']}")
    print(f"  Average GPA: {stats['average_gpa']:.2f}")
    print(f"  Year distribution: {stats['year_distribution']}")
    print()
```

---

# Applying Dictionaries to Finance Tracking

## From Last Week's Lists to This Week's Dictionaries

Think about your Week 5 finance tracker. You might have used lists like this:

```python
# Week 5 approach with lists
expenses = [450, 67.50, 89, 25, 120]
descriptions = ["Rent", "Groceries", "Fuel", "Coffee", "Phone bill"]
categories = ["Housing", "Food", "Transport", "Food", "Utilities"]
```

## Week 6 Dictionary Approach

```python
# Week 6 approach with dictionaries
expense_tracker = {
    "budget": {
        "monthly_limit": 2500,
        "remaining": 0  # Will be calculated
    },
    "expenses": {
        "EXP001": {
            "amount": 450,
            "description": "Monthly rent payment",
            "category": "Housing",
            "date": "2024-08-01",
            "essential": True
        },
        "EXP002": {
            "amount": 67.50,
            "description": "Weekly groceries",
            "category": "Food", 
            "date": "2024-08-03",
            "essential": True
        },
        "EXP003": {
            "amount": 89,
            "description": "Petrol for car",
            "category": "Transport",
            "date": "2024-08-05", 
            "essential": True
        }
    },
    "categories": {
        "Housing": {"budget": 800, "spent": 0},
        "Food": {"budget": 400, "spent": 0},
        "Transport": {"budget": 200, "spent": 0},
        "Utilities": {"budget": 150, "spent": 0},
        "Entertainment": {"budget": 100, "spent": 0}
    }
}
```

## Finance Dictionary Operations

```python
def add_expense(tracker, expense_id, amount, description, category, date, essential=True):
    """Add a new expense to the tracker"""
    tracker["expenses"][expense_id] = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": date,
        "essential": essential
    }
    
    # Update category spending
    if category in tracker["categories"]:
        tracker["categories"][category]["spent"] += amount
    
    return f"Added expense {expense_id}: ${amount} for {description}"

def get_category_summary(tracker):
    """Get spending summary by category"""
    summary = {}
    for category, info in tracker["categories"].items():
        budget = info["budget"]
        spent = info["spent"]
        remaining = budget - spent
        percentage = (spent / budget * 100) if budget > 0 else 0
        
        summary[category] = {
            "budget": budget,
            "spent": spent,
            "remaining": remaining,
            "percentage": percentage,
            "status": "Over budget" if spent > budget else "Within budget"
        }
    
    return summary

def find_expensive_items(tracker, threshold=100):
    """Find expenses above a certain threshold"""
    expensive_items = []
    for exp_id, details in tracker["expenses"].items():
        if details["amount"] >= threshold:
            expensive_items.append({
                "id": exp_id,
                "amount": details["amount"],
                "description": details["description"],
                "category": details["category"]
            })
    
    return sorted(expensive_items, key=lambda x: x["amount"], reverse=True)
```

---

# Try It Yourself! 🧪

## Exercise 1: Personal Course Tracker

Create a nested dictionary to track your university courses:

```python
# Create your course tracker
my_courses = {
    "current_semester": "2024-S2",
    "student_info": {
        # Add your details here
    },
    "courses": {
        "ISYS2001": {
            # Add course details: title, credits, instructor, 
            # assessments with weights, current grade estimate
        },
        # Add your other courses
    },
    "summary": {
        "total_credits": 0,
        "expected_gpa": 0
    }
}

# TODO: Write functions to:
# 1. Add a new course
# 2. Update a grade estimate
# 3. Calculate current GPA
# 4. Generate a progress report

# Your code here:
```

## Exercise 2: Transform Parallel Lists

Take this parallel list structure and convert it to dictionaries:

```python
# Old parallel list approach
movie_titles = ["The Matrix", "Inception", "Interstellar", "Blade Runner 2049"]
movie_years = [1999, 2010, 2014, 2017]
movie_directors = ["Wachowskis", "Nolan", "Nolan", "Villeneuve"]
movie_ratings = [8.7, 8.8, 8.6, 8.0]
movie_genres = ["Sci-Fi", "Sci-Fi", "Sci-Fi", "Sci-Fi"]

# TODO: Convert to a dictionary structure
# TODO: Add functions to search, filter, and analyze the movie data
# TODO: Create a recommendation system based on ratings

# Your code here:
```

---

# Knowledge Check 🎯

<details>
<summary><strong>Question 1:</strong> How do you safely access data that's 3 levels deep in a nested dictionary?</summary>

**Answer:** Use `.get()` at each level: `value = dict.get('key1', {}).get('key2', {}).get('key3', 'default')` or write a helper function to handle the nested access safely.
</details>

<details>
<summary><strong>Question 2:</strong> What's the main advantage of dictionaries over parallel lists for related data?</summary>

**Answer:** Dictionaries group related information together logically, eliminate index synchronization problems, provide meaningful key-based access, and make it easier to add new fields without restructuring everything.
</details>

<details>
<summary><strong>Question 3:</strong> How would you count occurrences of items when building a dictionary dynamically?</summary>

**Answer:** Use the pattern: `dict[key] = dict.get(key, 0) + 1` or initialize with `collections.defaultdict(int)` for cleaner code.
</details>

<details>
<summary><strong>Question 4:</strong> What's a good strategy for converting parallel lists to a dictionary structure?</summary>

**Answer:** 1) Identify which list contains the unique identifiers (keys), 2) Create a dictionary where each key maps to a sub-dictionary containing the related data from other lists, 3) Use `zip()` to iterate through lists together: `for key, val1, val2 in zip(keys, list1, list2):`
</details>

---

# Advanced Patterns for Problem Solving 💡

## Pattern 1: Dictionary Merging and Updates
```python
# Merge multiple dictionaries
student_basic = {"name": "Alice", "id": "S12345"}
student_academic = {"gpa": 3.8, "year": 2}
student_contact = {"email": "alice@uni.edu", "phone": "04XX"}

# Modern Python way (3.9+)
complete_student = student_basic | student_academic | student_contact

# Compatible way for older Python
complete_student = {}
complete_student.update(student_basic)
complete_student.update(student_academic) 
complete_student.update(student_contact)
```

## Pattern 2: Dictionary Comprehensions for Data Transformation
```python
# Transform student data efficiently
students_simplified = {
    student_id: info["name"] 
    for student_id, info in students.items()
}

# Filter and transform
high_performers = {
    student_id: info 
    for student_id, info in students.items() 
    if info["gpa"] >= 3.5
}
```

## Pattern 3: Grouping Data by Attributes
```python
def group_students_by_program(students_dict):
    """Group students by their academic program"""
    grouped = {}
    for student_id, info in students_dict.items():
        program = info["program"]
        if program not in grouped:
            grouped[program] = []
        grouped[program].append({
            "id": student_id,
            "name": info["name"],
            "gpa": info["gpa"]
        })
    return grouped
```

---

# Module Summary 📋

**Key Takeaways:**
- **Nested dictionaries** model complex, hierarchical data naturally
- **Dictionary patterns** solve real problems more elegantly than lists
- **Data transformation** from lists to dictionaries improves code organisation
- **Problem-solving patterns** like aggregation, filtering, and grouping are powerful with dictionaries

**Essential Patterns You've Learned:**
- Safe nested access with `.get()` chains
- Dynamic dictionary building during iteration
- Data aggregation and statistical analysis
- Converting parallel list structures to dictionaries

**Real-World Applications:**
- Student information systems
- Financial tracking and budgeting
- Inventory and catalog management
- Data analysis and reporting
- Configuration and settings management

---

# Ready for the Lab! 🚀

You now have the foundation to tackle the Week 6 lab activities:

**In the upcoming lab, you'll:**
- Work with interactive dictionary exercises
- Build a library management system using dictionaries
- Choose your path for the finance tracker mini-project:
  - **Path A:** Extend your Week 5 tracker with dictionaries
  - **Path B:** Build a fresh dictionary-based finance tracker

**Key Skills You Can Apply:**
- Replace parallel lists with elegant dictionary structures
- Create nested dictionaries for complex financial data
- Use dictionary methods for analysis and reporting
- Build dynamic, flexible data management systems

**Preparation Checklist:**
- [ ] Completed all three modules
- [ ] Practiced the "Try It Yourself" exercises
- [ ] Answered all knowledge check questions
- [ ] Thought about how to apply these concepts to your finance tracker

**Ready to organize your thoughts with dictionaries? Let's build something amazing in the lab!** 🏗️💰