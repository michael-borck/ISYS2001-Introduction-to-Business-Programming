---
title:"Staff Answer Guide: Introduction to File Operations and Basic Error Handling"
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


## Overview
This worksheet introduces students to essential file operations in Python and basic error handling techniques. The activities focus on opening, reading, writing, and closing files, as well as implementing try-except blocks to handle potential errors gracefully.

## Learning Objectives
- Apply basic file operations in Python
- Identify common errors in file operations
- Implement exception handling with try-except blocks
- Use context managers with the `with` statement

## Key Concepts Review

### File Operations
Students will learn:
- Opening files with different modes (`'r'`, `'w'`, `'a'`)
- Reading and writing file content
- Importance of properly closing files

### Exception Handling
Students will practice:
- Identifying errors that occur during file operations
- Using try-except blocks to catch specific exceptions
- Creating more robust programs that don't crash on common errors

## Expected Error Messages

When students run the code that attempts to open a nonexistent file, they should see an error like:
```
FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
```

## Solution to Task 1: Write the Basic Log Function

```python
from datetime import datetime

def add_log_entry(note):
    """
    Adds a timestamped entry to a log file.
    
    Args:
        note (str): The message to log
    """
    try:
        # Method 1: Without context manager
        # file = open('daily_log.txt', 'a')
        # current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # file.write(f"[{current_time}] {note}\n")
        # file.close()
        
        # Method 2: With context manager (preferred)
        with open('daily_log.txt', 'a') as file:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            # Optional: Check if note is empty
            if not note.strip():
                note = "(Empty entry)"
                
            file.write(f"[{current_time}] {note}\n")
            
    except Exception as e:
        print(f"Error writing to log file: {e}")
```

## Solution to Task 2: Test Your Function

Key points to discuss with students:
- The function should handle empty strings
- Additional test cases might include:
  - Very long entries
  - Entries with special characters
  - Multiple entries in succession

```python
# Testing with valid input
add_log_entry("Started working on Python file operations assignment")

# Testing with empty input
add_log_entry("")

# Additional test cases
add_log_entry("Entry with special characters: !@#$%^&*()")
add_log_entry("A" * 1000)  # Very long entry
```

## Solution to Extension: Reading and Processing the Log

```python
def display_recent_logs(num_entries=5):
    """
    Displays the most recent log entries.
    
    Args:
        num_entries (int): Number of recent entries to display
    """
    try:
        with open('daily_log.txt', 'r') as file:
            # Read all lines and convert to a list
            lines = file.readlines()
            
            # Calculate how many entries to show
            entries_to_show = min(num_entries, len(lines))
            
            if entries_to_show == 0:
                print("No log entries found.")
                return
                
            print(f"Displaying the {entries_to_show} most recent log entries:")
            
            # Display the most recent entries (from the end of the file)
            for i in range(1, entries_to_show + 1):
                print(lines[-i].strip())
                
    except FileNotFoundError:
        print("Log file doesn't exist yet. Try adding some entries first.")
    except Exception as e:
        print(f"Error reading log file: {e}")
```

## Discussion Points for Reflection Questions

### 1. Benefits of try-except blocks
- Programs continue running instead of crashing
- Errors can be handled gracefully with user-friendly messages
- Allows for recovery strategies when operations fail
- Makes code more robust in unpredictable environments

### 2. Importance of closing files
- Prevents resource leaks (open file handles)
- Ensures all data is properly written (flushes buffers)
- Makes files available to other processes
- The `with` statement ensures files are closed even if exceptions occur

### 3. Other potential file errors to handle
- `PermissionError`: Insufficient permissions to read/write the file
- `IOError`: General input/output errors
- `IsADirectoryError`: Trying to open a directory as a file
- `DiskFullError`: No space left on the device
- `JSONDecodeError`: When working with JSON files
- `UnicodeDecodeError`: Issues with character encoding

## Teaching Tips

1. **Demonstrate Real-World Relevance**: Explain how proper file handling is crucial in professional applications (databases, log systems, data processing).

2. **Visualization**: Draw diagrams showing the flow of try-except blocks and how they change program execution.

3. **Common Pitfalls to Highlight**:
   - Forgetting to close files
   - Using bare `except:` without specifying exceptions
   - Not handling empty or malformed input

4. **Scaffolding**: 
   - For struggling students, provide a partially completed solution
   - For advanced students, challenge them to add features like:
     - Searching the log by keyword
     - Deleting old entries
     - Sorting or filtering entries

5. **Check for Understanding**:
   - Ask students to explain why the `with` statement is preferred
   - Have them predict what happens with different error scenarios

## Extension Activities

For students who finish early or want additional challenges:

1. **Log Parser**: Create a function that analyzes the log file to show statistics (e.g., entries per day)

2. **Categories**: Modify the log system to support different categories of entries (e.g., INFO, WARNING, ERROR)

3. **Multiple Log Files**: Extend the program to maintain separate log files for different users or purposes

4. **CSV Integration**: Convert the log to CSV format for easier data analysis

## Assessment Criteria

When reviewing student work, look for:

- Proper use of context managers (`with` statement)
- Appropriate exception handling
- Input validation
- Clear, well-formatted output
- Thoughtful reflection responses