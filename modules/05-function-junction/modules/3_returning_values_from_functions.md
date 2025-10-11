---
title: "Unlocking Results with Returning Values"
subtitle: "How Your Functions Share Their Results with Your Code"
author: "Michael Borck"
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

# Unlocking Results with Returning Values

Welcome to Module 3! In this module, you'll learn how functions process data and send results back to your programme using the `return` statement. This is crucial for building professional applications where functions work together to solve complex business problems.

::: {.notes}
The "Unlocking Results with Returning Values" slide serves as an introduction to the concept of using return statements in functions to produce output. It sets the stage for the subsequent slides, which will delve into the specifics of how the return statement works and provide examples to illustrate its usage.

For Information Systems students, understanding return values is particularly important because it enables the composability that makes business software powerful. When a loan calculation function returns a payment amount, that result can become input to a budget analysis function. When an expense categorisation function returns a category, that can be used by a reporting function.

This pattern of functions returning values that feed into other functions mirrors how business processes work in the real world—each step produces output that becomes input for the next step. Understanding this concept is essential for building the kind of integrated business applications that Information Systems professionals design and manage.
:::

# The return Statement

- **Purpose:**  
  The `return` statement sends a value back to the part of your code that called the function.
- **Why use it?**  
  Instead of printing a result immediately, returning a value lets you store and use that result later.
- **Key Difference:**  
  - **Printing:** Displays a value on the screen.  
  - **Returning:** Provides a value that can be used elsewhere in your code.

::: {.notes}
The return statement serves two main purposes in programming. It allows you to exit a function and optionally send a value back to the caller. Using return is beneficial when you need to terminate a function's execution early or when you want to provide a result that can be utilised in other parts of your code.

It's important to distinguish between printing and returning values. Printing simply displays a value on the screen for informational purposes. In contrast, returning a value using the return statement makes it available for further use and processing within your program, enabling more flexible and modular code design.
:::

# Simple Arithmetic Example

Consider a function that calculates return on investment:

```python
def calculate_roi(initial_investment, final_value):
    profit = final_value - initial_investment
    roi_percentage = (profit / initial_investment) * 100
    return roi_percentage

investment_return = calculate_roi(1000, 1200)
print(f"Your ROI is {investment_return:.1f}%")
```

- Here, `calculate_roi` processes the investment data and returns the percentage.
- We store this result and can use it for further analysis or reporting.

::: {.notes}
The slide "Simple Arithmetic Example" demonstrates how the `add_numbers` function processes the input numbers and returns their sum. This returned value is then assigned to the variable `result`, allowing us to store and utilise the computed sum for further operations or output.

By printing the `result` variable, we can display the sum of the numbers to the user, showcasing the successful execution of the `add_numbers` function and the returned value. This example highlights the importance of returning values from functions, enabling us to capture and work with the results of computations performed within the function's scope.
:::

# Return vs. Print in Professional Context

- **Composability:** Return values can become inputs to other functions
- **Testing:** Returned values can be automatically tested
- **Flexibility:** Same calculation can be used in different contexts  
- **AI Integration:** AI tools work better with clear input/output patterns

::: {.notes}
Professional applications rarely print directly to screen. Instead, functions return values that can be used by other parts of the program. This pattern becomes especially important when working with AI tools, which often generate functions that need to work together in larger systems.

For Information Systems students, this composability is crucial for building business applications. A function that calculates loan payments should return the amount so it can be used in budget analysis, financial reporting, or decision-making workflows. Functions that print their results directly can't easily be integrated into larger systems.

When working with AI to generate code, functions that return values are much more useful than functions that only print. AI can more easily combine returned values into complex business logic workflows.
:::

# Activity: Calculate Monthly Loan Payment

**Your Task:**

- Create a function named `calculate_monthly_payment` that:
  - Accepts three parameters: `principal`, `annual_rate`, and `months`.
  - Calculates the monthly payment using the formula:  
    _Payment = principal × (monthly_rate × (1 + monthly_rate)^months) / ((1 + monthly_rate)^months - 1)_
  - Returns the calculated payment amount.
- Call your function and use the result in a budget analysis.

**Example:**

```python
def calculate_monthly_payment(principal, annual_rate, months):
    monthly_rate = annual_rate / 12
    if monthly_rate == 0:  # Handle 0% interest
        return principal / months
    
    payment = principal * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
    return payment

# Use the returned value in other calculations
loan_payment = calculate_monthly_payment(25000, 0.05, 60)
monthly_income = 4000
remaining_income = monthly_income - loan_payment
print(f"Monthly payment: ${loan_payment:.2f}")
print(f"Remaining income: ${remaining_income:.2f}")
```

- Notice how the returned value enables further analysis.

::: {.notes}
This financial calculation activity demonstrates several key concepts for Information Systems students. First, it shows how complex business formulas can be encapsulated in functions, making them reusable across different parts of an application. The loan payment calculation is something students might actually use in their personal lives or professional work.

The example also demonstrates the power of return values—the payment amount becomes input for budget analysis. This composability is essential in business applications where calculations feed into each other. Students can see how returned values enable the kind of integrated financial analysis that professional software provides.

The inclusion of edge case handling (0% interest) introduces the concept that business functions need to handle real-world scenarios robustly. This prepares students for more sophisticated error handling and validation that they'll encounter in professional development.
:::

# Introduction to Testing Concepts

When functions return values, you can test them systematically:

```python
def test_calculate_roi():
    # Test with known values
    result = calculate_roi(1000, 1200)
    expected = 20.0  # 20% return
    
    if abs(result - expected) < 0.01:  # Allow for small rounding differences
        print("✅ ROI calculation test passed!")
    else:
        print(f"❌ Test failed: expected {expected}, got {result}")

test_calculate_roi()
```

Testing becomes much more important in the AI era—you need to verify that AI-generated code produces correct results.

::: {.notes}
Introducing testing concepts here prepares students for more sophisticated quality assurance practices they'll encounter later in the course and in professional development. When functions return values instead of printing them, automated testing becomes possible and practical.

For Information Systems students, understanding testing is particularly important because business applications must be reliable. Financial calculations, in particular, need to be accurate and verifiable. The concept that you can automatically check whether code produces correct results is fundamental to professional software development.

As students begin working with AI tools, testing becomes even more critical. AI can generate code quickly, but humans need to verify that the code produces correct business results. Functions that return values can be systematically tested, while functions that only print cannot.
:::

# Recap

- The `return` statement lets a function send data back to the calling code.
- This technique allows you to use the results of a function in other parts of your programme.
- Returned values enable function composition and systematic testing.
- Practice writing functions that return values to become more confident in your coding skills.

Happy coding, and enjoy exploring the power of returning values from your functions!

::: {.notes}
In this slide, we recap the key points about returning values from functions. The `return` statement allows a function to send data back to the calling code, enabling you to use the results of the function in other parts of your programme. This is a powerful technique that can make your code more modular and reusable.

To become more confident in your coding skills, it's recommended that you practise writing functions that return values. By doing so, you'll gain a better grasp of how to structure your code and how to pass data between different parts of your programme. With time and practice, you'll find that using functions with return values becomes second nature and greatly improves the efficiency and readability of your code.
:::

