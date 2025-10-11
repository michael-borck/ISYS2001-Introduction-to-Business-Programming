---
title: "Staff Answer Guide: Exploring Code Paradigms: Procedural vs Object-Oriented in Python"
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


## Introduction & Key Concepts
This guide provides solutions and evaluation points for the student worksheet comparing procedural and object-oriented programming (OOP) paradigms in Python.
Ensure students can differentiate the core ideas:

* **Procedural Programming:** Focuses on sequences of instructions grouped into functions/procedures. Data tends to be separate from the functions that operate on it.
* **Object-Oriented Programming (OOP):** Focuses on bundling data (attributes) and behavior (methods) together into objects created from class blueprints.
* **Class:** The template/blueprint (e.g., the `Triangle` definition).
* **Object:** A specific instance created from the class (e.g., `my_triangle`).

## Application Activities

### Activity 1: Identifying Paradigms in Real Code

**Scenario Code:**
```python
def calculate_area(base, height):
    return 0.5 * base * height

area = calculate_area(5, 10)
print("Area:", area)
```

**Expected Response:**

* **Paradigm:** Procedural Programming.
* **Justification:**
    * The code is organised around a function (`calculate_area`) that performs a specific task.
    * Data (`base`, `height`, `area`) is defined separately and passed into the function.
    * There are no classes or objects being defined or used. The focus is on the *procedure* (the function call) rather than on objects having state and behavior.

**Evaluation Notes:**

* The student must correctly identify the paradigm as procedural.
* The justification should mention the use of functions, the separation of data and functions, and the absence of classes/objects.

### Activity 2: Refactoring to OOP

**Task:** Convert the procedural code to an OOP structure using a `Triangle` class.

**Expected Code:**

```python
# Procedural code (for reference)
# def calculate_area(base, height):
#     return 0.5 * base * height
# area = calculate_area(5, 10)
# print("Area:", area)

# Refactor to OOP below

class Triangle:
    """
    Represents a triangle with a base and height,
    and can calculate its area.
    """
    def __init__(self, base, height):
        """
        Initialises a Triangle object with base and height.
        Args:
            base (float/int): The base length of the triangle.
            height (float/int): The height of the triangle.
        """
        self.base = base     # Store base as an instance attribute
        self.height = height # Store height as an instance attribute

    def calculate_area(self):
        """
        Calculates the area of the triangle using its base and height.
        Returns:
            float: The calculated area.
        """
        # Method uses the object's own attributes (self.base, self.height)
        return 0.5 * self.base * self.height

# --- Using the OOP approach ---
# 1. Create an instance (object) of the Triangle class
my_triangle = Triangle(5, 10)

# 2. Call the method on the object to perform the calculation
area_oop = my_triangle.calculate_area()

# 3. Print the result
print("OOP Area:", area_oop)
```

**Expected Output:**
```
OOP Area: 25.0
```

**Evaluation Notes:**

* Check for correct class definition syntax (`class Triangle:`).
* Verify the `__init__` method initialises `base` and `height` as instance attributes (`self.base`, `self.height`).
* Ensure the `calculate_area` method is defined within the class, takes `self`, and uses `self.base` and `self.height`.
* Check that an instance of `Triangle` is created (`my_triangle = Triangle(...)`).
* Verify the `calculate_area` method is called correctly on the instance (`my_triangle.calculate_area()`).

### Extension Task: Enhance the Triangle Class

**Task:** Add perimeter calculation and input validation to the `Triangle` class. *Note: Calculating the perimeter requires the lengths of the three sides. The area calculation uses base and height. For simplicity, we'll add three side attributes alongside base and height, and validate all. Acknowledge that for a general triangle, base/height aren't sufficient alone for perimeter, and side lengths aren't sufficient alone for the area formula used.*

**Expected Code:**

```python
import math # Needed for more complex area if using sides, but sticking to original area formula here.

class Triangle:
    """
    Represents a triangle with base, height, and three side lengths.
    Includes methods for area and perimeter calculation, and input validation.
    """
    def __init__(self, base, height, side1, side2, side3):
        """
        Initialises a Triangle object with dimensions and side lengths.

        Args:
            base (float/int): The base length (for area calc).
            height (float/int): The height (for area calc).
            side1 (float/int): Length of the first side (for perimeter/validation).
            side2 (float/int): Length of the second side (for perimeter/validation).
            side3 (float/int): Length of the third side (for perimeter/validation).

        Raises:
            ValueError: If any dimension/side is not positive, or if sides
                      do not form a valid triangle (triangle inequality).
        """
        # Input Validation
        if not all(isinstance(val, (int, float)) and val > 0 for val in [base, height, side1, side2, side3]):
            raise ValueError("Base, height, and all sides must be positive numbers.")

        # Triangle Inequality Check (sum of any two sides must be greater than the third)
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("The given side lengths do not form a valid triangle.")

        # Assign attributes if validation passes
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        # Note: We store base/height and sides separately as per the task evolution.
        # In a real-world scenario, you might derive some from others if possible
        # (e.g., for a right triangle) or use formulas like Heron's for area from sides.

    def calculate_area(self):
        """
        Calculates the area using base and height.
        Returns:
            float: The calculated area.
        """
        return 0.5 * self.base * self.height

    def calculate_perimeter(self):
        """
        Calculates the perimeter using the three side lengths.
        Returns:
            float: The calculated perimeter.
        """
        return self.side1 + self.side2 + self.side3

# --- Testing the Enhanced Class ---
try:
    # Example valid triangle (e.g., a 3-4-5 right triangle, base=3, height=4)
    valid_triangle = Triangle(base=3, height=4, side1=3, side2=4, side3=5)
    print(f"Valid Triangle - Area: {valid_triangle.calculate_area()}")
    print(f"Valid Triangle - Perimeter: {valid_triangle.calculate_perimeter()}")

    # Example invalid triangle (violates triangle inequality)
    print("\nAttempting to create invalid triangle (sides 1, 2, 5):")
    invalid_triangle_sides = Triangle(base=1, height=1, side1=1, side2=2, side3=5)

except ValueError as e:
    print(f"Error creating triangle: {e}")

try:
    # Example invalid input (non-positive value)
    print("\nAttempting to create triangle with non-positive side:")
    invalid_triangle_input = Triangle(base=3, height=4, side1=3, side2=4, side3=-5)

except ValueError as e:
    print(f"Error creating triangle: {e}")
```

**Expected Output:**
```
Valid Triangle - Area: 6.0
Valid Triangle - Perimeter: 12.0

Attempting to create invalid triangle (sides 1, 2, 5):
Error creating triangle: The given side lengths do not form a valid triangle.

Attempting to create triangle with non-positive side:
Error creating triangle: Base, height, and all sides must be positive numbers.
```

**Evaluation Notes:**

* Check `__init__` includes parameters for sides (`side1`, `side2`, `side3`).
* Verify input validation logic:
    * Checks if inputs are numeric and positive.
    * Checks the triangle inequality theorem.
    * Raises `ValueError` appropriately.
* Ensure the `calculate_perimeter` method is correctly implemented using `self.side1`, `self.side2`, `self.side3`.
* Check the example usage demonstrates both successful creation/method calls and catches validation errors using `try...except`.
* Comments explaining the structure (especially the separate handling of base/height for area and sides for perimeter) are a plus.

## Reflection

**Objective:** Evaluate the student's synthesis of the concepts, self-awareness of AI tool usage, and commitment to academic integrity.

**Evaluation Guidance:**
Focus on the depth and specificity of the answers.

* **Reflect on how you might use the knowledge of different programming paradigms in your future projects.**
    * Look for understanding of trade-offs. When might procedural be suitable (simple scripts, linear workflows, performance-critical loops)? When is OOP better (modeling complex entities, code reuse via inheritance/polymorphism, large projects needing organisation, GUI development)? Specific examples strengthen the response.
* **Discuss how you used AI tools during this activity and evaluate their effectiveness.**
    * Encourage specific examples related to the tasks: "Asked AI for syntax to define a class," "Asked AI how to refactor the function into a method," "Used AI to generate ideas for input validation," "Asked AI to explain the difference between procedural and OOP with examples."
    * Evaluation: Was the AI helpful? Did it provide correct information? Was it easy to integrate its suggestions? This shows engagement with the **Learning Partner** aspect.
* **Describe how you ensured the integrity of your work when using AI suggestions.**
    * Look for actions demonstrating **Critical Evaluation** and **Transparency**. Examples: "I cross-referenced the AI's explanation with the worksheet/lecture notes," "I tested the code suggested by the AI to ensure it worked and I understood it," "I modified the AI's suggestion to fit the specific requirements of the task," "I treated the AI as a tutor to explain concepts, then wrote the code myself," "I noted where AI contributed significantly." Avoidance of simple copy-pasting should be evident.

