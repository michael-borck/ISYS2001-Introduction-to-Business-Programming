Absolutely! Here's a **mini-lab worksheet** that introduces `safe_` wrappers through guided examples. It walks students through:

1. What can go wrong with built-in functions
2. How to handle it manually
3. How to wrap it into reusable `safe_` functions
4. A few small challenges to practice building their own

---

## 🧪 Mini-Lab: Building Safe Wrappers in Python

**Topic:** Handling errors with `safe_` functions  
**Level:** Week 7 – Intro to error handling (pre-exceptions deep dive)  
**Goal:** Help students recognize where things might break, and how to prevent it using wrapper functions.

---

### 🧭 Part 1: The Problem with Unreliable Input

Try running this in a Python cell:

```python
import json

bad_json = "Not valid JSON at all!"
parsed = json.loads(bad_json)
```

❓What happens?

✍️ **Write the error message below:**

```text
# Your answer here
```

---

### 🛡️ Part 2: Adding Basic Protection

Update the code to handle this more safely:

```python
try:
    parsed = json.loads(bad_json)
except json.JSONDecodeError:
    parsed = {}
```

🧠 Why do we use a `try` block here?

```text
# Your answer here
```

---

### 🧰 Part 3: Turning It Into a Safe Wrapper

Let’s wrap that logic into a **reusable function**:

```python
def safe_json_loads(text):
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}
```

✅ Test it:

```python
print(safe_json_loads('{"name": "Alice"}'))         # Should return a dictionary
print(safe_json_loads("This is not JSON!"))         # Should return {}
```

---

### 🧪 Part 4: Build Your Own Safe Wrapper

Let’s build a safe version of a function that might fail: `int()`  
What happens when we try to convert text to a number?

```python
print(int("123"))       # ✅
print(int("hello"))     # ❌
```

🔧 Fill in the blanks:

```python
def safe_int(text):
    try:
        return int(text)
    except ValueError:
        return 0  # Or None
```

✅ Test your function:

```python
print(safe_int("42"))       # ➜ 42
print(safe_int("banana"))   # ➜ 0
```

---

### 🧠 Reflection Questions

1. Why might we want to return a default value (like `{}` or `0`)?
2. What would happen if we didn’t catch the error?
3. When is it okay to crash, and when should we try to recover?

✍️ Write your thoughts here:

```text
# Your thoughts...
```

---

### 🎯 Extension Challenge (Optional)

Try writing your own `safe_float()` function.

```python
def safe_float(text):
    # Your code here
    ...
```

---

### 📎 Instructor Notes (for you)

- This lab bridges the gap between practical problem-solving and formal exception handling.
- Ideal to follow up next week by "unpacking" the try/except syntax they've already used inside `safe_` wrappers.
- You can extend this to `safe_divide(a, b)`, `safe_list_access(lst, i)`, or even `safe_open(filename)`.

---

Would you like this exported as a PDF/Markdown/Colab/Quarto version for your class?



Great instinct — **yes**, making a `safe_` wrapper for file operations is a **very practical idea**, especially for beginner programmers.

### 🧨 Why?

File operations often fail in ways that **crash programs**:
- File doesn't exist → `FileNotFoundError`
- No permission → `PermissionError`
- File is in use or locked → `OSError`
- Encoding errors → `UnicodeDecodeError` (when reading text)

At Week 7, students may not yet be ready to handle all of this — but a `safe_open()` or `safe_read_file()` can let them move forward **without fear** of runtime crashes.

---

## ✅ Example: `safe_read_file()` (Beginner Version)

```python
def safe_read_file(filename):
    """
    Tries to read a file. Returns the file contents as a string,
    or an empty string if something goes wrong.
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Could not read file: {e}")
        return ""
```

### 🔧 Usage:

```python
data = safe_read_file("myfile.txt")
print(data)
```

---

## 🧪 Mini-Lab Exercise: Reading Files Safely

### ⚠️ Step 1: What happens if the file is missing?

```python
with open("not_a_real_file.txt", "r") as f:
    data = f.read()
```

✍️ What error do you see?

```text
# Your answer
```

---

### ✅ Step 2: Use `safe_read_file()` instead

```python
def safe_read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return ""
```

Test with:
```python
print(safe_read_file("not_a_real_file.txt"))
```

---

### 🔁 Bonus: A Safe File Writer

```python
def safe_write_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            print("Write successful.")
    except Exception as e:
        print(f"Failed to write file: {e}")
```

---

### 🧠 Why This Matters

Having students **build and use safe_ wrappers**:
- Encourages reuse
- Builds awareness of failure points in code
- Eases anxiety around crashing
- Lays a foundation for exception handling next week

---

Would you like me to bundle `safe_json_loads()`, `safe_int()`, and `safe_read_file()` into a mini “safe_utils.py” module for student use? Or make a short coding task sheet around just `safe_read_file()`?