---
title: "Mastering Exception Management in Python"
subtitle: "Best Practices for Robust and Resilient Code"
author: "Michael Borck"
format: 
  pptx:
    reference-doc: ../../../_assets/template.pptx
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

# Introduction to Exception Handling

* Understanding exceptions in Python
* Importance of error handling for program reliability
* Overview of today's key concepts

::: {.notes}
Welcome to our exploration of exception handling in Python! Today, we will delve into how Python handles errors and exceptions, which are critical for writing robust and user-friendly applications. Understanding this concept will not only help you debug programs but also allow you to anticipate and manage potential issues effectively. Let's start by defining what exceptions are and why they are fundamental in Python programming.
:::

# What are Exceptions?

* Exceptions: Events that disrupt normal program flow
* Difference between syntax errors and exceptions
* Why handling exceptions is important for program stability

::: {.notes}
In programming, an exception is an event that disrupts the normal flow of a program. It occurs whenever the program encounters an error during execution. While syntax errors are mistakes in the use of the programming language, which are caught before the execution of the program, exceptions can occur during execution. Without proper handling, exceptions will cause the program to crash. Understanding these differences is crucial for effective error handling and creating more resilient applications.
:::

# Python's Exception Hierarchy

```
BaseException
├── SystemExit
├── KeyboardInterrupt
├── Exception
│   ├── ArithmeticError
│   │   ├── ZeroDivisionError
│   │   └── OverflowError
│   ├── LookupError
│   │   ├── IndexError
│   │   └── KeyError
│   ├── TypeError
│   └── ValueError
└── ... (other exceptions)
```

* Python organizes exceptions in a hierarchical structure
* Most exceptions you'll handle derive from `Exception`
* Understanding the hierarchy helps with effective exception catching

::: {.notes}
Python organizes exceptions in a hierarchical structure. At the top of this hierarchy is the BaseException class, from which all other exceptions inherit. Directly under BaseException is the Exception class, which serves as the base for most exceptions you will typically handle. Examples of specific exceptions inheriting from Exception include ValueError, which is raised when a function receives an argument of the correct type but inappropriate value, TypeError, and IOError. By understanding this hierarchy, you can make informed decisions about which exceptions to catch and how to structure your error handling code.
:::

# Basic Exception Handling Syntax

* Using `try` and `except` blocks
* Basic syntax pattern
* Example of simple exception handling

```python
try:
    # Code that might raise an exception
    x = int(input("Enter a number: "))
    result = 10 / x
    print(f"10 divided by {x} is {result}")
except ValueError:
    # Handles invalid input
    print("That was not a valid number.")
except ZeroDivisionError:
    # Handles division by zero
    print("Cannot divide by zero.")
```

::: {.notes}
Exception handling in Python is primarily conducted using `try` and `except` blocks. You wrap the code that might cause an exception in a `try` block, and the code to execute if an exception occurs goes in an `except` block. You can have multiple `except` blocks to handle different types of exceptions differently. In this example, we're handling two specific exceptions: ValueError for invalid input conversion and ZeroDivisionError for division by zero. This targeted approach allows for more precise error responses.
:::

# Complete Exception Handling Structure

* The full `try`/`except`/`else`/`finally` structure
* When to use each clause
* Complete example

```python
try:
    # Code that might raise an exception
    x = int(input("Enter a number: "))
    result = 100 / x
except ValueError:
    # Handles invalid input
    print("That's not a valid number!")
except ZeroDivisionError:
    # Handles division by zero
    print("Cannot divide by zero!")
else:
    # Executes if no exceptions were raised
    print(f"100 divided by {x} is {result}")
finally:
    # Always executes, regardless of what happened
    print("Execution completed")
```

::: {.notes}
The complete exception handling structure in Python includes four components: `try`, `except`, `else`, and `finally`. The `try` block contains code that might raise exceptions. The `except` blocks handle specific exceptions. The `else` clause runs only if no exceptions were raised in the `try` block, making it a good place for code that should run only if the operation was successful. The `finally` clause contains code that will execute no matter what, whether an exception occurred or not, making it perfect for cleanup operations.
:::

# Catching Multiple Exceptions

* Different ways to handle multiple exception types
* Using tuple of exceptions
* Using Exception hierarchy for broader catching

```python
# Method 1: Multiple except blocks
try:
    # Risky code
    pass
except ValueError:
    # Handle ValueError
    pass
except TypeError:
    # Handle TypeError
    pass

# Method 2: Catching multiple exceptions in one block
try:
    # Risky code
    pass
except (ValueError, TypeError):
    # Handle either ValueError or TypeError
    pass

# Method 3: Catching parent exception
try:
    # Risky code
    pass
except Exception:
    # Handle any exception that inherits from Exception
    # Be careful with this approach!
    pass
```

::: {.notes}
Python offers several ways to handle multiple types of exceptions. You can use separate `except` blocks for each exception type, which allows for different handling logic for each. You can also catch multiple exception types in a single `except` block by specifying them as a tuple, which is useful when you want to handle different exceptions in the same way. Finally, you can catch a parent exception class to handle all its child exceptions, but this approach should be used carefully as it might catch unexpected exceptions and mask bugs.
:::

# Example: Handling File Errors

```python
try:
    with open('data.txt', 'r') as file:
        content = file.read()
        data = int(content)
except FileNotFoundError:
    print("Error: File does not exist.")
    data = 0
except ValueError:
    print("Error: File does not contain a valid number.")
    data = 0
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    data = 0
finally:
    print(f"Processing complete. Data value: {data}")
```

* Practical example of file error handling
* Handling specific file-related exceptions
* Using general exception as a fallback

::: {.notes}
Let's consider a practical example where we handle various exceptions that might occur when working with files. Here, we're trying to open a file, read its content, and convert it to an integer. Several things might go wrong: the file might not exist (FileNotFoundError), the content might not be a valid number (ValueError), or some other unexpected error might occur. We handle each specific case differently and use a generic Exception handler as a fallback. The finally block ensures we always print a completion message.
:::

# Raising Exceptions

* When to raise exceptions in your code
* Using `raise` to signal errors
* Re-raising exceptions after handling

```python
def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is unrealistically high")
    return age

# Example of re-raising an exception
try:
    age = validate_age("twenty")
except TypeError as e:
    print(f"Error: {e}")
    print("Please enter a number instead.")
    # Re-raise if you want calling code to also handle it
    # raise
```

::: {.notes}
Sometimes you need to raise exceptions in your own code to signal error conditions. The `raise` statement allows you to trigger a specific exception when a condition occurs that should interrupt normal program flow. In this example, we've created a function that validates an age value, raising appropriate exceptions for different invalid inputs. Additionally, you can re-raise an exception after handling it partially, which allows the exception to propagate up the call stack while still performing some local error handling.
:::

# Exception Chaining

* Using `raise ... from ...` to indicate causality
* Preserving the exception stack
* Helps with debugging complex applications

```python
try:
    x = int("not a number")
except ValueError as e:
    # This creates a new exception while preserving the original cause
    raise RuntimeError("Processing failed") from e

# Example of implicit chaining
try:
    try:
        x = int("not a number")
    except ValueError:
        # This implicitly chains the exceptions
        # (Python remembers the original cause)
        raise RuntimeError("Processing failed")
except RuntimeError as e:
    print(f"Error: {e}")
    # Access the original cause
    print(f"Original cause: {e.__cause__}")
```

::: {.notes}
Exception chaining is a feature in Python 3 that allows you to indicate that one exception was caused by another. Using the syntax `raise new_exception from original_exception`, you explicitly link the two exceptions, which helps with debugging by preserving the full exception history. Python also supports implicit chaining when you raise a new exception inside an except block. This feature is especially valuable in complex applications where errors might propagate through multiple layers of code.
:::

# Creating Custom Exceptions

* Benefits of custom exception classes
* How to create your own exception types
* Example of using custom exceptions

```python
# Define custom exceptions
class NetworkError(Exception):
    """Exception raised for network-related errors."""
    pass

class DatabaseError(Exception):
    """Exception raised for database-related errors."""
    pass

# Using custom exceptions
def fetch_data(database_url):
    try:
        # Attempt to connect...
        if "database" not in database_url:
            raise DatabaseError(f"Invalid database URL: {database_url}")
        # More code...
    except ConnectionError:
        # Convert standard exception to our custom one
        raise NetworkError("Could not connect to the database") from ConnectionError
```

::: {.notes}
Creating custom exception classes allows you to define application-specific error types that provide more context about what went wrong. Custom exceptions typically inherit from the Exception class or one of its subclasses. They can be as simple as empty classes that just define a new type, or they can include additional attributes and methods to provide more information about the error. Using custom exceptions makes your code more readable and allows calling code to catch specific application-level exceptions.
:::

# Using Assertions

* Purpose of assertions in code
* When to use assertions vs. exceptions
* Example of effective assertion usage

```python
def calculate_average(numbers):
    # Assert that the input is a non-empty list
    assert isinstance(numbers, list), "Input must be a list"
    assert len(numbers) > 0, "List cannot be empty"
    
    total = sum(numbers)
    return total / len(numbers)

# Assertions can be disabled in production with -O flag
# Use exceptions for errors that should always be checked
```

::: {.notes}
Assertions are a debugging aid that tests a condition and triggers an error if the condition is false. Unlike regular exception handling, assertions are typically used to catch programming errors rather than runtime errors. They're often used to verify assumptions about your code's state or input values. It's important to note that assertions can be disabled in production code by running Python with the -O (optimize) flag, so you shouldn't rely on them for security or data validation that must always occur. For such checks, use regular exception handling instead.
:::

# Common Pitfalls in Exception Handling

* Overusing `try` blocks
* Catching too general exceptions
* Ignoring caught exceptions
* Silent failures

```python
# Bad: Too general, masks errors
try:
    # A lot of code...
    process_data()
    save_results()
except Exception:  # Catches everything!
    pass  # Silent failure!

# Better: Specific, informative
try:
    # Minimal code that might fail
    data = process_data()
except ValueError as e:
    print(f"Data processing error: {e}")
    log_error(e)  # Log for debugging
```

::: {.notes}
Several common pitfalls can reduce the effectiveness of exception handling. First, wrapping too much code in a single try block makes it harder to determine which part caused the error. Second, catching overly general exceptions like `Exception` might mask bugs by catching exceptions you didn't anticipate. Third, ignoring exceptions by using empty except blocks or just passing creates silent failures that are difficult to debug. Always include minimal code in try blocks, catch specific exceptions, and provide meaningful error messages or logging to help diagnose issues.
:::

# Common Exception Handling Patterns

* Retry pattern for transient failures
* Logging and re-raising for debugging
* Converting between exception types
* Default values for graceful degradation

```python
# Retry pattern
def retry_operation(max_attempts=3):
    attempts = 0
    while attempts < max_attempts:
        try:
            return perform_operation()  # Might fail
        except TransientError:
            attempts += 1
            if attempts == max_attempts:
                raise  # Re-raise after max attempts
            time.sleep(1)  # Wait before retrying

# Default value pattern
def get_config_value(key, default=None):
    try:
        return config[key]
    except KeyError:
        return default
```

::: {.notes}
Several exception handling patterns are commonly used in Python. The retry pattern attempts an operation multiple times before giving up, which is useful for transient errors like network timeouts. Logging and re-raising helps with debugging by recording the error but still allowing it to propagate. Converting between exception types helps abstract lower-level errors into application-specific ones. The default value pattern provides graceful degradation by substituting a sensible default when an operation fails, allowing the program to continue running with reduced functionality rather than crashing.
:::

# Real-World Application: Data Processing Pipeline

```python
def process_data_pipeline(input_file, output_file):
    try:
        # Step 1: Read input file
        with open(input_file, 'r') as f:
            data = f.read()
        
        # Step 2: Parse data
        try:
            parsed_data = json.loads(data)
        except json.JSONDecodeError:
            # Attempt CSV parsing as a fallback
            parsed_data = parse_csv(data)
        
        # Step 3: Transform data
        transformed_data = transform(parsed_data)
        
        # Step 4: Write output
        with open(output_file, 'w') as f:
            json.dump(transformed_data, f)
            
        return True
    except Exception as e:
        log_error(f"Pipeline failed: {e}")
        return False
```

* Exception handling in a multi-step process
* Using nested try-except blocks for specific steps
* Implementing fallback strategies

::: {.notes}
This real-world example shows exception handling in a data processing pipeline. We have an outer try-except block that catches any unhandled exceptions in the overall process, while inner try-except blocks handle specific steps that might fail. We also implement a fallback strategy: if JSON parsing fails, we try CSV parsing instead. This approach combines different exception handling patterns to create a robust pipeline that can deal with various error conditions while still attempting to complete the task. The function returns a boolean indicating success or failure, allowing calling code to take appropriate action.
:::

# Looking Ahead: Safe Utility Functions

* Combining exception handling with reusable functions
* Creating "safe" versions of operations that might fail
* Preview of our upcoming mini-project

```python
def safe_json_loads(text, default=None):
    """
    Safely parse JSON text, returning a default value if parsing fails.
    
    Args:
        text (str): The JSON string to parse
        default: Value to return if parsing fails (default: None)
        
    Returns:
        The parsed JSON data or the default value
    """
    if default is None:
        default = {}
        