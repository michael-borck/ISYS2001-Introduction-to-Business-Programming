# 🧰 Week 11 Mini-Project: Building Your Safe Utils Module

**Topic:** Creating Error-Resistant Utility Functions  
**Goal:** Build a Python module of reusable "safe_" wrapper functions that handle errors gracefully

## 📝 Introduction

When programs encounter unexpected situations, they often crash with error messages. While these errors are helpful for debugging, they can create a poor user experience. In this mini-project, you'll:

1. Learn why programs crash and how to prevent it
2. Create wrapper functions that make unsafe operations safe
3. Build your own Python module that you can reuse in future projects

### 🔄 Connecting to Previous Knowledge

Earlier in the semester, we used packages like **PyInputPlus** to handle user input validation without worrying about exception handling:

```python
import pyinputplus as pyip

# Gets an integer input with automatic validation
age = pyip.inputInt("Enter your age: ")
```

Similarly, we used **pandas** to process file contents without dealing with low-level file operations:

```python
import pandas as pd

# Reads a CSV file without manual file handling
df = pd.read_csv("data.csv")
```

Now it's time to understand what's happening "under the hood" of these helpful packages and build our own error-resistant utilities!

## 🧭 Part 1: Understanding Errors with Unreliable Input

### Example 1: JSON Parsing

Try running this in a Python cell:

```python
import json

bad_json = "Not valid JSON at all!"
parsed = json.loads(bad_json)
```

❓What happens?

✍️ **Write the error message here:**

```text
# Your answer here
```

### Example 2: Converting Text to Numbers

Try running this:

```python
user_input = "hello"
number = int(user_input)
```

✍️ **Write the error message here:**

```text
# Your answer here
```

### Example 3: Reading Files

Try running this:

```python
with open("file_that_doesnt_exist.txt", "r") as f:
    content = f.read()
```

✍️ **Write the error message here:**

```text
# Your answer here
```

## 🛡️ Part 2: Adding Basic Protection with try/except

### How to Handle JSON Errors

```python
import json

bad_json = "Not valid JSON at all!"

try:
    parsed = json.loads(bad_json)
    print("JSON parsed successfully:", parsed)
except json.JSONDecodeError:
    parsed = {}
    print("JSON parsing failed, using empty dictionary instead.")
```

### How to Handle Conversion Errors

```python
user_input = "hello"

try:
    number = int(user_input)
    print("Converted to number:", number)
except ValueError:
    number = 0
    print("Conversion failed, using 0 instead.")
```

### How to Handle File Errors

```python
try:
    with open("file_that_doesnt_exist.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    content = ""
    print("File not found, using empty string instead.")
```

🧠 **Question:** Why do we use `try` blocks in these examples?

```text
# Your answer here
```

## 🧰 Part 3: Creating Reusable Safe Wrapper Functions

Let's wrap the error-handling logic into reusable functions:

### Safe JSON Parser

```python
def safe_json_loads(text):
    """
    Safely parse JSON, returning an empty dict if parsing fails.
    
    Args:
        text (str): The JSON string to parse
        
    Returns:
        dict: The parsed JSON data or an empty dict if parsing failed
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}
```

### Safe Integer Converter

```python
def safe_int(text):
    """
    Safely convert text to integer, returning 0 if conversion fails.
    
    Args:
        text (str): The text to convert to an integer
        
    Returns:
        int: The converted integer or 0 if conversion failed
    """
    try:
        return int(text)
    except ValueError:
        return 0
```

### Safe File Reader

```python
def safe_read_file(filename):
    """
    Safely read a file, returning an empty string if reading fails.
    
    Args:
        filename (str): The path to the file to read
        
    Returns:
        str: The file content or an empty string if reading failed
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Could not read file: {e}")
        return ""
```

**Note:** While pandas is excellent for processing structured data files (like CSV or Excel), understanding basic file operations is still essential. This function demonstrates proper file handling with the `with` statement, which ensures files are properly closed even if errors occur.

## 🧪 Part 4: Testing Your Safe Functions

Test your safe functions with both valid and invalid inputs:

```python
# Test safe_json_loads
print(safe_json_loads('{"name": "Alice"}'))         # Should return a dictionary
print(safe_json_loads("This is not JSON!"))         # Should return {}

# Test safe_int
print(safe_int("123"))       # Should return 123
print(safe_int("hello"))     # Should return 0

# Test safe_read_file
print(safe_read_file("existing_file.txt"))          # Should return file content
print(safe_read_file("non_existent_file.txt"))      # Should return ""
```

## 🔧 Part 5: Build Your Own Safe Function

Now it's your turn! Create a `safe_float` function that converts text to a floating-point number:

```python
def safe_float(text):
    """
    Safely convert text to float, returning 0.0 if conversion fails.
    
    Args:
        text (str): The text to convert to a float
        
    Returns:
        float: The converted float or 0.0 if conversion failed
    """
    # Your code here
    ...
```

Test your function with:

```python
print(safe_float("3.14"))       # Should return 3.14
print(safe_float("pi"))         # Should return 0.0
```

**Challenge question:** Would a different default value than 0.0 ever be more appropriate? What situations might call for a different default?

## 📊 Part 6: Creating More Advanced Safe Functions

Let's build a few more useful safe functions:

### Safe Division

```python
def safe_divide(a, b):
    """
    Safely divide two numbers, returning 0 if division by zero would occur.
    
    Args:
        a (number): The dividend
        b (number): The divisor
        
    Returns:
        float: The result of a/b or 0 if b is 0
    """
    try:
        return a / b
    except ZeroDivisionError:
        return 0
```

### Safe List Access

```python
def safe_list_access(lst, index):
    """
    Safely access a list element, returning None if the index is out of range.
    
    Args:
        lst (list): The list to access
        index (int): The index to access
        
    Returns:
        Any: The element at lst[index] or None if index is out of range
    """
    try:
        return lst[index]
    except IndexError:
        return None
```

### Safe File Writer

```python
def safe_write_file(filename, content):
    """
    Safely write content to a file, returning True if successful, False otherwise.
    
    Args:
        filename (str): The path to the file to write
        content (str): The content to write to the file
        
    Returns:
        bool: True if writing was successful, False otherwise
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Failed to write file: {e}")
        return False
```

## 🎯 Part 7: Create Your Safe Utils Module

Now let's organize all these functions into a reusable Python module. This is an important step as we transition from notebook-based learning to working with Python scripts and modules in the coming weeks.

### Creating Your First Python Module

1. Create a new file called `safe_utils.py`
2. Add all the safe functions we've created
3. Add proper docstrings and comments

Here's how your file should look:

```python
# safe_utils.py

import json

def safe_json_loads(text):
    """
    Safely parse JSON, returning an empty dict if parsing fails.
    
    Args:
        text (str): The JSON string to parse
        
    Returns:
        dict: The parsed JSON data or an empty dict if parsing failed
    """
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {}

def safe_int(text):
    """
    Safely convert text to integer, returning 0 if conversion fails.
    
    Args:
        text (str): The text to convert to an integer
        
    Returns:
        int: The converted integer or 0 if conversion failed
    """
    try:
        return int(text)
    except ValueError:
        return 0

def safe_float(text):
    """
    Safely convert text to float, returning 0.0 if conversion fails.
    
    Args:
        text (str): The text to convert to a float
        
    Returns:
        float: The converted float or 0.0 if conversion failed
    """
    try:
        return float(text)
    except ValueError:
        return 0.0

def safe_read_file(filename):
    """
    Safely read a file, returning an empty string if reading fails.
    
    Args:
        filename (str): The path to the file to read
        
    Returns:
        str: The file content or an empty string if reading failed
    """
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Could not read file: {e}")
        return ""

def safe_write_file(filename, content):
    """
    Safely write content to a file, returning True if successful, False otherwise.
    
    Args:
        filename (str): The path to the file to write
        content (str): The content to write to the file
        
    Returns:
        bool: True if writing was successful, False otherwise
    """
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except Exception as e:
        print(f"Failed to write file: {e}")
        return False

def safe_divide(a, b):
    """
    Safely divide two numbers, returning 0 if division by zero would occur.
    
    Args:
        a (number): The dividend
        b (number): The divisor
        
    Returns:
        float: The result of a/b or 0 if b is 0
    """
    try:
        return a / b
    except ZeroDivisionError:
        return 0

def safe_list_access(lst, index):
    """
    Safely access a list element, returning None if the index is out of range.
    
    Args:
        lst (list): The list to access
        index (int): The index to access
        
    Returns:
        Any: The element at lst[index] or None if index is out of range
    """
    try:
        return lst[index]
    except IndexError:
        return None
```

### Creating Your Module in Colab

Since we've been using Google Colab all semester, here are options for creating and using your module:

1. **Generate the module file in Colab:**
   ```python
   %%writefile safe_utils.py
   # Copy the module code here
   ```

2. **Test importing your module:**
   ```python
   import safe_utils
   
   # Test a function
   print(safe_utils.safe_int("123"))  # Should display 123
   ```

3. **Download your module** for use in upcoming weeks when we begin working with local Python development.

## 🚀 Part 8: Using Your Module

### Testing in Colab

If you're working in Colab, you can test your module in the same notebook:

```python
# After creating safe_utils.py with %%writefile
import safe_utils

# Test all functions
print("Testing safe_json_loads:")
print(safe_utils.safe_json_loads('{"name": "Alice"}'))
print(safe_utils.safe_json_loads("Not JSON"))

print("\nTesting safe_int:")
print(safe_utils.safe_int("42"))
print(safe_utils.safe_int("banana"))

# Additional tests for other functions...
```

### Testing as a Script

For the upcoming weeks when we'll be working with Python scripts locally, you can create a test file called `test_safe_utils.py`:

```python
# test_safe_utils.py

import safe_utils

# Test all functions
print("Testing safe_json_loads:")
print(safe_utils.safe_json_loads('{"name": "Alice"}'))
print(safe_utils.safe_json_loads("Not JSON"))

print("\nTesting safe_int:")
print(safe_utils.safe_int("42"))
print(safe_utils.safe_int("banana"))

print("\nTesting safe_float:")
print(safe_utils.safe_float("3.14"))
print(safe_utils.safe_float("pi"))

print("\nTesting safe_divide:")
print(safe_utils.safe_divide(10, 2))
print(safe_utils.safe_divide(10, 0))

print("\nTesting safe_list_access:")
print(safe_utils.safe_list_access([1, 2, 3], 1))
print(safe_utils.safe_list_access([1, 2, 3], 10))

print("\nTesting safe_write_file:")
print(safe_utils.safe_write_file("test.txt", "Hello, world!"))

print("\nTesting safe_read_file:")
print(safe_utils.safe_read_file("test.txt"))
print(safe_utils.safe_read_file("nonexistent.txt"))
```

### Multiple Ways to Use Your Module

1. **In Colab (current environment):** 
   - Create the module using `%%writefile`
   - Import it directly in the same session

2. **Between Colab notebooks:**
   - Upload the .py file to Colab
   - Import it in any notebook

3. **In local Python (coming weeks):**
   - Download your module
   - Place it in the same directory as your script
   - Import it using `import safe_utils`

This project serves as a bridge between our notebook-based work and the upcoming weeks focused on local Python development and debugging.

## 🧠 Part 9: Extension Challenges

Choose one or more of these challenges to extend your module:

1. **Create a `safe_input_int` function** that keeps asking for input until valid integer is given:

```python
def safe_input_int(prompt):
    """
    Repeatedly ask for input until a valid integer is given.
    
    Args:
        prompt (str): The prompt to display to the user
        
    Returns:
        int: The valid integer input
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
```

**Discussion Point:** How does this function compare to PyInputPlus's `inputInt()` function we learned about earlier? What advantages or disadvantages does each approach have?

2. **Create a `safe_dict_access` function** that safely gets a value from a dictionary:

```python
def safe_dict_access(d, key, default=None):
    """
    Safely access a dictionary value, returning a default if the key doesn't exist.
    
    Args:
        d (dict): The dictionary to access
        key: The key to look up
        default: The value to return if the key doesn't exist (default: None)
        
    Returns:
        Any: The value at d[key] or default if key doesn't exist
    """
    try:
        return d[key]
    except (KeyError, TypeError):
        return default
```

3. **Create a `safe_json_file` function** that combines reading a file and parsing JSON:

```python
def safe_json_file(filename):
    """
    Safely read a JSON file, returning an empty dict if reading or parsing fails.
    
    Args:
        filename (str): The path to the JSON file
        
    Returns:
        dict: The parsed JSON data or an empty dict if reading or parsing failed
    """
    content = safe_read_file(filename)
    return safe_json_loads(content)
```

**Discussion point:** This function demonstrates function composition - using simpler functions to build more complex ones. How does this compare to pandas' approach of having a `pd.read_json()` function? What are the advantages of each approach?

## 🌟 Part 10: Publish Your Module to GitHub

1. Create a GitHub repository
2. Upload your `safe_utils.py` file
3. Create a `README.md` file explaining your module
4. Add a `LICENSE` file (optional)
5. Share your module with classmates

## 🧠 Reflection Questions

1. Why is it important to handle errors in code?
2. When is it appropriate to use a `try`/`except` block?
3. What default values did you choose for your safe functions? Why?
4. When might it be better to let an error crash your program rather than handling it silently?
5. How could you improve your module to make it even more robust?
6. Compare creating your own safe functions versus using existing libraries like PyInputPlus or pandas. When would you choose each approach?

✍️ Write your reflections here:

```text
# Your thoughts...
```

## 🏆 Submission Requirements

1. Your completed `safe_utils.py` module
2. Your `test_safe_utils.py` test file
3. Answers to the reflection questions
4. Link to your GitHub repository (if created)
5. At least one additional safe function that you created on your own

## 📚 Resources

- [Python Exception Handling Tutorial](https://docs.python.org/3/tutorial/errors.html)
- [Python Module Documentation](https://docs.python.org/3/tutorial/modules.html)
- [GitHub Quickstart Guide](https://docs.github.com/en/get-started/quickstart)
- [PyInputPlus Documentation](https://pypi.org/project/PyInputPlus/)
- [pandas Documentation](https://pandas.pydata.org/docs/)

## 🤖 Learning with AI Guidance

As you work through this mini-project, you might consider using an AI assistant like Claude to help deepen your understanding. Here are some effective prompting strategies to maximize your learning:

### ✅ Effective Learning Prompts 

1. **Get conceptual explanations:** 
   "Explain the difference between catching specific exceptions vs. catching all exceptions in Python."

2. **Request step-by-step reasoning:**
   "Walk me through how I should decide what default value to return from a safe function."

3. **Ask for analogies:**
   "Can you provide an analogy that explains why exception handling is important in programming?"

4. **Get debugging help:**
   "My safe_json_loads function is returning None instead of an empty dictionary. What might be wrong?"

5. **Request implementation variations:**
   "How would you implement safe_read_file differently if you wanted to return the error message instead of an empty string?"

### ❌ Avoid These Approaches

1. **Don't copy-paste complete solutions:**
   Instead of "Write me a safe_dict_access function," try "What considerations should I keep in mind when designing a safe_dict_access function?"

2. **Don't request fully-written code without understanding it:**
   Instead of "Give me a complete safe_utils module," ask "How should I structure my safe_utils module and what functions should I include?"

3. **Don't skip reflection:**
   Take time to understand *why* certain approaches work better than others. Ask about tradeoffs and alternatives to deepen your understanding.

Remember: AI tools are most valuable when they help you understand concepts more deeply, not when they just provide answers!
