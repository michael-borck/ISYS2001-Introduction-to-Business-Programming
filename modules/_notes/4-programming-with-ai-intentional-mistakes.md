## 🧠🤖 AI Conversation Worksheet – Debugging AI Outputs  
> **Title**: *Be the Boss: Guide the AI to Build a Gradebook*

---

### 🧩 The Challenge:
> Build a **Gradebook Program** that:
> - Stores **student names and their test scores**
> - Uses a **function** to calculate average score
> - Handles **invalid input** and **empty scores**
> - Outputs each student’s **name and average**

---

### 🗣 Prompt 1: “Can you help me write a program that stores student names and scores, and prints their average?”

**🤖 AI Response (has subtle mistakes):**
```python
students = {
    "Alice": "85, 90, 78",
    "Bob": "70, 88, 92"
}

for name in students:
    avg = sum(students[name]) / len(students[name])
    print(f"{name}: {avg}")
```

---

### ❌ What’s wrong with this code?

✅ Use this space to **list the problems**:

- _________________________________________________________  
- _________________________________________________________  

🧠 Hint: Think about **data types**, **string vs. list**, and `sum()`.

✏️ Suggested Prompt:  
`"Your code stores scores as strings. Can you fix it so each student has a list of numbers instead?"`

---

### 🗣 Prompt 2: “Can you fix the scores so they’re stored as numbers in a list?”

**🤖 AI Response (better, but still not ideal):**
```python
students = {
    "Alice": [85, 90, 78],
    "Bob": [70, 88, 92]
}

for name in students:
    total = 0
    for score in students[name]:
        total += score
    avg = total / 3
    print(f"{name} average is {avg}")
```

---

### ❌ Critique This:

1. What assumption is made about score count?
2. Could we use a function here?

✏️ Prompt Idea:  
`"Can you make a function to calculate the average of any list of scores, instead of assuming 3?"`

---

### 🗣 Prompt 3: “Please use a function to calculate the average instead of hardcoding ‘3’.”

**🤖 AI Response (Oops! Watch this one):**
```python
def average(scores):
    return sum(scores) / len(scores)

for name in students:
    print(f"{name} average: {average(name)}")
```

---

### ❌ Spot the Mistake:

- What is being passed to `average()` here?
- Why does it crash?

✏️ Prompt Idea:  
`"You're passing the name to average instead of the list of scores. Can you fix the for-loop?"`

---

### 🗣 Prompt 4: Fixing the Loop

**🤖 AI Response (Corrected):**
```python
def average(scores):
    return sum(scores) / len(scores)

for name, scores in students.items():
    print(f"{name} average: {average(scores)}")
```

🎉 This version works — but now let’s push it further...

---

### 🗣 Prompt 5: “Can you modify the code to ask the user to enter student names and scores?”

**🤖 AI Response (Flawed Input Handling):**
```python
students = {}

while True:
    name = input("Enter name (or 'done'): ")
    if name == "done":
        break
    scores = input("Enter scores separated by spaces: ")
    students[name] = scores.split()
```

---

### ❌ Critique the Input Code:

- Are the scores strings or integers?
- What happens if the user enters bad input?

✏️ Prompt Idea:  
`"Can you convert the scores to integers and ignore blank entries?"`

---

### 🗣 Prompt 6: Fix Input Parsing

**🤖 AI Response (Improving):**
```python
scores = [int(s) for s in scores.split() if s.strip() != ""]
```

✏️ Extension Prompt:  
`"Can you skip entries that aren’t valid numbers?"`

---

### 🗣 Final Prompt: “Can you combine this with the average function and print student averages?”

**🤖 AI Final Version (Almost There... but what’s missing?):**
```python
def average(scores):
    return sum(scores) / len(scores)

for name in students:
    print(f"{name} average: {average(students[name])}")
```

---

### ❌ Final Check:

- Does this handle **empty scores**?
- What if someone enters no valid numbers?

✏️ Prompt Idea:  
`"Can you make sure the average function handles an empty list without crashing?"`

---

### ✅ Your Turn: Rewrite the Final Version with Fixes

```python
# Your improved version here:
```

---

### 🔍 Wrap-Up: What You Learned About Directing the AI

- What kinds of mistakes did the AI make?
- How did your understanding of Python help you fix them?
- How would you change your prompts next time?

✏️ Notes:  
_________________________________________________________  
_________________________________________________________  

---
