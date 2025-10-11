## 🧠🤖 AI Conversation Worksheet – Advanced Programming via Prompting  
> **Title**: *Guiding the AI: Building a Python Gradebook*

### 🧩 Task:  
> **Create a gradebook program that:**
> - Uses a dictionary to store student names and their list of scores  
> - Has a function to calculate average score  
> - Prints each student’s name and average  
> - Handles edge cases (e.g., empty lists, invalid inputs)

---

### 👣 Step-by-Step Prompt Walkthrough

---

### 🔹 Prompt 1: Start Simple

**You ask AI:**  
🟢 `"Can you help me write a Python program to store student names and their test scores, and print their average?"`

**AI replies:**  
```python
students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92],
    "Charlie": [100, 100, 90]
}

for name, scores in students.items():
    avg = sum(scores) / len(scores)
    print(f"{name} has an average of {avg}")
```

---

### 🔍 Reflection:
> ✅ **What’s good about this solution?**  
> ⚠️ **What’s missing?** (Think: user-defined functions, flexibility, edge cases)

✏️ **Your notes:**  
___________________________________________________________  
___________________________________________________________  

---

### 🔹 Prompt 2: Add a Function

**You ask AI:**  
🟢 `"Can you turn the average calculation into a function?"`

**AI replies:**  
```python
def average(scores):
    return sum(scores) / len(scores)

for name, scores in students.items():
    print(f"{name} has an average of {average(scores)}")
```

---

### 🧠 Pause & Think:

> What if `scores` is an empty list?  
> Try this prompt:  
🟢 `"What happens if a student has no scores? Can you fix that?"`

---

### 🔹 Prompt 3: Improve Robustness

**AI replies:**  
```python
def average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)
```

> 💬 Not bad — but is returning 0 always the best choice?

✏️ **Optional Critique:**  
___________________________________________________________  
___________________________________________________________  

---

### 🔂 Optional Fork:
> You realize you want to enter student data manually.

🟢 Prompt: `"Can I ask the user to enter student names and scores?"`

---

### 🔹 Prompt 4: Collect User Input

**AI tries (but gives this shaky code):**  
```python
students = {}
while True:
    name = input("Enter student name (or 'done'): ")
    if name == "done":
        break
    scores = input("Enter scores separated by commas: ").split(",")
    students[name] = scores
```

---

### 🔍 Let’s Critique That:

- 🚫 Scores are strings, not numbers  
- 🚫 No validation  
- ✅ Good start using loop & dictionary

✏️ **Prompt suggestion to fix it:**  
🟢 `"Can you convert scores to numbers and skip blanks?"`

---

### 🔹 Prompt 5: Improve Input Handling

**AI replies:**  
```python
students = {}
while True:
    name = input("Enter student name (or 'done'): ")
    if name == "done":
        break
    raw_scores = input("Enter scores separated by commas: ")
    scores = [int(s) for s in raw_scores.split(",") if s.strip().isdigit()]
    students[name] = scores
```

---

### ✅ Final Prompt: Combine with Function

🟢 `"Can you combine this with the average function and print each student's name and average?"`

---

### ✨ Final Result (AI replies):  
```python
def average(scores):
    if not scores:
        return "No scores"
    return sum(scores) / len(scores)

students = {}
while True:
    name = input("Enter student name (or 'done'): ")
    if name == "done":
        break
    raw_scores = input("Enter scores separated by commas: ")
    scores = [int(s) for s in raw_scores.split(",") if s.strip().isdigit()]
    students[name] = scores

for name, scores in students.items():
    print(f"{name}: Average = {average(scores)}")
```

---

### 🧠 Reflection: Directing the AI Like a Programmer

> - What *concepts* helped you understand what to ask?
> - When did you have to **correct or clarify** the AI?
> - Could someone without a good grasp of `dict`, `functions`, `input()` etc. make this work?

✏️ **Your Thoughts:**  
___________________________________________________________  
___________________________________________________________  

---
