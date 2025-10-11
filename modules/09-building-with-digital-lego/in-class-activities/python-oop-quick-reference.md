---
title: "Python OOP Quick Reference"
subtitle: "For When AI Gets Too Technical"
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

# Python OOP Quick Reference
*For When AI Gets Too Technical*

## The Big Picture
- **Templates** (called "classes") define what something should look like
- **Individual items** (called "objects") are created from templates
- Each item can store its own information and perform actions

---

## Basic Template Creation

```python
class Transaction:                    # Create a template called "Transaction"
    def __init__(self, amount, desc): # This runs when creating each item
        self.amount = amount          # Store information in this item
        self.description = desc       # 'self' means "this specific item"
    
    def is_expense(self):            # Define what this item can do
        return self.amount < 0       # Return True/False
    
    def display(self):               # Another action this item can do
        return f"{self.description}: ${self.amount}"
```

## Using the Template

```python
# Create individual items from the template
coffee = Transaction(-4.50, "Coffee")       # Creates one transaction
salary = Transaction(1000, "Paycheck")      # Creates another transaction

# Use the items
print(coffee.display())          # "Coffee: $-4.50"
print(coffee.is_expense())       # True
print(salary.is_expense())       # False

# Access stored information
print(coffee.amount)             # -4.50
print(salary.description)       # "Paycheck"
```

---

## Key Python Words

| Word | What It Means | Example |
|------|---------------|---------|
| `class` | Creates a template/blueprint | `class Customer:` |
| `def __init__` | Setup that runs when item is created | Like filling out a form |
| `self` | "This specific item" | `self.name = "John"` |
| `def method_name` | An action the item can perform | `def calculate_total()` |

---

## Common Patterns

### Storing Information
```python
class Customer:
    def __init__(self, name, email):
        self.name = name        # Each customer remembers their name
        self.email = email      # Each customer remembers their email
        self.orders = []        # Start with empty order list
```

### Performing Actions
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount    # Change stored information
    
    def get_balance(self):
        return self.balance                     # Return stored information
```

### Working with Collections
```python
class OrderManager:
    def __init__(self):
        self.orders = []                # Store multiple items
    
    def add_order(self, order):
        self.orders.append(order)       # Add new item to collection
    
    def count_orders(self):
        return len(self.orders)         # Count items in collection
```

---

## Reading AI Code

When AI gives you code with these patterns, look for:

1. **What information does each item store?** (Look for `self.something = value`)
2. **What actions can items perform?** (Look for `def action_name(self):`)
3. **How do you create new items?** (Look for the `__init__` section)
4. **How do you use the items?** (Look for examples like `item.action()`)

---

## Quick Debugging

**Error: "NameError: name 'self' is not defined"**
- Fix: Make sure you're inside a class method and the first parameter is `self`

**Error: "TypeError: missing required argument"**  
- Fix: Check the `__init__` method - you need to provide all required information

**Error: "AttributeError: object has no attribute"**
- Fix: Check spelling, or make sure you defined that information/action in the class

---

## Business Translation

| Business Concept | Python Code |
|------------------|-------------|
| "Customer form template" | `class Customer:` |
| "Fill out a new customer form" | `new_customer = Customer("John", "john@email.com")` |
| "Customer's stored information" | `new_customer.name` |
| "What can customers do?" | Methods like `place_order()`, `update_email()` |
| "Filing cabinet of customers" | `customers = []` then `customers.append(new_customer)` |

---

## Remember
- **Focus on the business problem** - what are you trying to solve?
- **Let AI handle the syntax** - use the business-focused prompts from your worksheets
- **This reference is backup** - most of the time, good prompts mean you won't need these details
- **Templates + Individual Items = Powerful Business Systems**