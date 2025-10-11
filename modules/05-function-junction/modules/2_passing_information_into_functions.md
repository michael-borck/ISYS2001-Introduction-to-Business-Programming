---
title: "Supercharge Your Functions with Data"
subtitle: "Using Parameters, Arguments, and Defaults to Create Dynamic Code"
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
# Passing Information to Functions

Welcome to Module 2! In this module, we'll learn how to send data into your functions. This transforms your functions from simple, fixed operations into powerful, flexible tools that can handle different financial scenarios.

::: {.notes}
Passing information to functions is a fundamental concept in programming. Functions can accept input values, known as arguments, which are used within the function to perform specific tasks or calculations. These arguments are defined as parameters in the function definition, specifying the expected input values.

When calling a function, you provide the necessary arguments, which can be literals, variables, or expressions. The arguments are passed to the corresponding parameters in the function, allowing the function to operate on the provided values. By utilising parameters and arguments effectively, you can create reusable and modular code that can be easily customised for different scenarios.

For Information Systems students, this concept is particularly important because it mirrors how business systems work. A loan calculator function needs different inputs (principal, rate, term) for different loans. An expense categorisation function needs the expense amount and budget information. Parameters allow you to create flexible business logic that adapts to different situations while maintaining the same underlying process.
:::

# Objectives

- Understand the difference between parameters and arguments.
- Learn how positional arguments work.
- Discover how to assign default values to parameters.

::: {.notes}
Presenter notes for "Objectives" slide:

This slide outlines the key learning objectives for the section on passing information to functions. Firstly, we'll clarify the distinction between parameters and arguments, which are often used interchangeably but have different meanings. Parameters are the variables defined in a function's definition, whereas arguments are the actual values passed to the function when it's called. Understanding this difference is crucial for working effectively with functions.

Next, we'll explore how positional arguments work. In Python, the order in which arguments are passed matters, and this is determined by the position of the corresponding parameters in the function definition. We'll look at examples to illustrate this concept. Lastly, we'll learn how to assign default values to parameters, which allows us to provide a fallback value if an argument isn't passed. This can make our functions more flexible and easier to use in different contexts.
:::

# Parameters vs. Arguments

- **Parameters:**  
  These are placeholders in your function definition. They represent the data your function needs.
- **Arguments:**  
  These are the actual values you pass into your function when you call it.
  
For example, in:
  
```python
def calculate_simple_interest(principal, rate, time):
    interest = principal * rate * time
    print(f"Interest earned: ${interest:.2f}")
```

`principal`, `rate`, and `time` are parameters. When you call `calculate_simple_interest(1000, 0.05, 2)`, the values 1000, 0.05, and 2 are arguments.

::: {.notes}
Parameters are variables defined in a function declaration that receive values when the function is called. They act as placeholders for the values that will be passed to the function, allowing it to work with different data each time it is invoked. Parameters are specified within the parentheses of the function declaration, and they can have default values assigned to them.

Arguments, on the other hand, are the actual values passed to a function when it is called. These values are supplied within the parentheses of the function call and are used to replace the corresponding parameters in the function definition. The number and order of arguments must match the number and order of parameters in the function declaration unless default values are provided for the parameters.
:::

# Positional Arguments

- Arguments are passed into functions based on their order.
- The first argument goes to the first parameter, the second to the second parameter, and so on.
- This is why it is important to keep the order consistent when calling your function.

::: {.notes}
Positional arguments are passed into functions based on their order. The first argument corresponds to the first parameter, the second argument to the second parameter, and so forth. It is crucial to maintain consistency in the order of arguments when calling a function to ensure the intended behaviour and avoid unexpected results.

When using positional arguments, the position of each argument determines which parameter it is assigned to within the function. This means that if the order of the arguments is changed when calling the function, the values will be assigned to different parameters, potentially leading to errors or incorrect outputs. Therefore, it is important to be mindful of the order and provide the arguments in the same sequence as the function's parameter list.
:::

# Default Parameter Values

- You can assign a default value to a parameter in your function definition.
- This allows the function to be called even if one or more arguments are missing.
- Example:
  
```python
def calculate_compound_interest(principal, rate, time, compound_frequency=1):
    amount = principal * (1 + rate/compound_frequency) ** (compound_frequency * time)
    return amount - principal
```

In this function, if you don't provide a compound frequency, it defaults to 1 (annual compounding).

::: {.notes}
Default parameter values allow functions to be called even when one or more arguments are not provided. In the function definition, a default value can be assigned to a parameter, which will be used if the corresponding argument is missing when the function is called. This provides flexibility and convenience, as it eliminates the need to specify every argument if some have suitable default values.

Here's an example to illustrate the concept: def greet(name, greeting="Hello"): print(f"{greeting}, {name}!") In this function, the "greeting" parameter has a default value of "Hello". If the function is called with only one argument, like greet("Alice"), the default value will be used, and the output will be "Hello, Alice!". However, if both arguments are provided, such as greet("Bob", "Hi"), the specified value will override the default, resulting in "Hi, Bob!".
:::

# AI and Function Parameters

- **AI Strength:** Generating functions with correct parameter structure
- **Your Strength:** Designing meaningful parameters for real problems
- **Partnership:** You design the interface, AI helps with implementation
- **Business Impact:** Well-designed parameters make functions truly useful

::: {.notes}
When working with AI, you'll often describe what parameters a function should take, and AI will help implement the logic. Understanding parameter design—what inputs a function needs and why—becomes a crucial skill for directing AI effectively.

For Information Systems professionals, this is particularly valuable because you understand the business context that AI lacks. You know that a loan function needs principal, rate, and term. You know that an expense function needs amount and category. You understand which parameters should have defaults and which are required.

This combination of business knowledge and technical understanding makes you an effective AI collaborator—you can specify what needs to be built and evaluate whether AI's implementation meets business requirements.
:::

# Activity: Create Your Own Finance Function

**Task:**  
Create a function named `budget_recommendation` that takes three parameters: `monthly_income`, `current_expenses`, and `savings_goal` (with a default of 20%).  
- Calculate how much they should save based on their goal
- Calculate how much they have left for additional expenses
- Print helpful recommendations

Take a moment to write your own version of this function.

::: {.notes}
In this activity, you will create a finance-focused function that demonstrates how parameters enable flexible business logic. The function should calculate budget recommendations based on income and expenses, with a sensible default for savings goals.

This activity reinforces several key concepts: required parameters (income and expenses), optional parameters with defaults (savings goal), and business logic implementation. Students practice designing function interfaces that mirror real-world financial planning processes.

The default savings goal of 20% reflects common financial advice, showing how defaults can encode business rules and best practices. Students will see how this makes the function easier to use while maintaining flexibility for different scenarios.
:::

# Example Answer

Here's one way to write the function:

```python
def budget_recommendation(monthly_income, current_expenses, savings_goal=0.20):
    recommended_savings = monthly_income * savings_goal
    available_for_additional = monthly_income - current_expenses - recommended_savings
    
    print(f"Monthly income: ${monthly_income:.2f}")
    print(f"Current expenses: ${current_expenses:.2f}")
    print(f"Recommended savings ({savings_goal*100:.0f}%): ${recommended_savings:.2f}")
    print(f"Available for additional expenses: ${available_for_additional:.2f}")
    
    if available_for_additional < 0:
        print("⚠️ Warning: You're overspending your budget!")
    elif available_for_additional < 100:
        print("💡 Budget is tight. Consider reducing expenses.")
    else:
        print("✅ Good budget balance!")

# Example calls
budget_recommendation(3000, 2200)  # Uses default 20% savings
budget_recommendation(3000, 2200, 0.15)  # Custom 15% savings goal
```

This demonstrates how parameters let you create flexible business logic that adapts to different financial situations.

# Business Parameter Patterns

Common patterns you'll use in finance applications:
- **Financial calculations:** principal, rate, time
- **Data processing:** data, filters, output_format  
- **User interface:** prompt, validation_rules, default_value
- **Business rules:** amount, thresholds, policy_settings

::: {.notes}
Understanding common parameter patterns helps students design better functions and work more effectively with AI tools. These patterns reflect how business software is actually structured—with clear interfaces that separate business logic from implementation details.

The financial calculation pattern (principal, rate, time) appears throughout finance applications. The data processing pattern becomes important as students work with CSV files and larger datasets. The user interface pattern helps them build better interactive programs.

These patterns also help when working with AI—students can describe the type of function they need and AI can suggest appropriate parameter structures based on these common patterns.
:::


