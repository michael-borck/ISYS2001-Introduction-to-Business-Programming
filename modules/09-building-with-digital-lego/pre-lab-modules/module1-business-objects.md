---
title: "Business Systems Think in Objects"
subtitle: "Module 1: OOP Fundamentals for BIS Students"
format: 
  pptx:
    reference-doc: curtin_template.pptx
  html:
    theme: 
      - cosmo
      - custom.scss
    toc: true
    toc-expand: 2
    code-fold: true
    embed-resources: true
    fig-cap-location: bottom
    css: module-styles.css
  pdf:
    toc: false
    colorlinks: true
    geometry:
      - top=30mm
      - left=20mm
  docx:
    highlight-style: github
    toc: false
---

## Plot Twist: You've Been Using Objects All Along! {.center}

::: {.fragment}
**Every time you've written:**

- `customer_name.lower()` 
- `transaction_list.append(item)`
- `df.groupby('category')`

**You were calling methods on objects!** 🤯
:::

::: {.fragment}
*Python has been organising code into objects from day one. You just didn't realise it!*
:::

---

## What You Already Know

::: {.columns}

::: {.column width="50%"}
**String Objects:**
```python
customer_name = "John Smith"
customer_name.upper()    # "JOHN SMITH"
customer_name.title()    # "John Smith"
customer_name.split()    # ["John", "Smith"]
```
:::

::: {.column width="50%"}
**List Objects:**
```python
expenses = [100, 200, 50]
expenses.append(75)      # Add new expense
expenses.sort()          # Organize them
len(expenses)            # Count how many
```
:::

:::

::: {.fragment}
**The Pattern:** `object.method()` - You ask an object to do something for you
:::

---

## Why Businesses Naturally Think in Objects {.center}

::: {.r-fit-text}
Every business you know organizes around **"things"** with **properties** and **actions**
:::

---

## Real Business Example: Coffee Shop

::: {.columns}

::: {.column width="50%"}
**Customer "Object":**

*Properties:*
- Name: "Sarah Johnson"
- Phone: "0412 345 678" 
- Loyalty Points: 47
- Favorite Drink: "Flat White"

*Actions:*
- Place order
- Earn points
- Redeem rewards
:::

::: {.column width="50%"}
**Order "Object":**

*Properties:*
- Order ID: "#2024-1205"
- Customer: Sarah Johnson
- Items: 1x Flat White, 1x Muffin
- Total: $8.50
- Status: "Ready"

*Actions:*
- Add item
- Calculate total
- Mark as complete
:::

:::

---

## The Business Problem We're Solving

::: {.callout-important}
## Your Finance App Challenge

You need to build a system that handles:

- **Bulk historical data** (500+ transactions from CSV files)
- **Individual new entries** (employees adding expenses daily)  
- **Smart reporting** (spending by category, budget alerts)
- **User interactions** (chatbot answering questions)

**How do these four different needs work together?**
:::

---

## 🤔 AI Exploration Time

::: {.callout-tip}
## Try This Prompt

*"List the main 'things' in a [choose: coffee shop/gym/online store] business and what information each thing needs to track."*

**What will you discover?**
- AI naturally describes objects without using technical terms
- Customer objects, Product objects, Order objects emerge naturally
- Each "thing" has properties and actions
:::

::: {.fragment}
**Reflection Questions:**

- How does this compare to spreadsheets you've used?
- What happens when customer information is scattered across multiple files?
:::

---

## The Spreadsheet Problem

::: {.columns}

::: {.column width="50%"}
**Traditional Approach:**

- `customers.xlsx`
- `orders.xlsx` 
- `products.xlsx`
- `payments.xlsx`

*What happens when Sarah changes her phone number?*
:::

::: {.column width="50%"}
**Object-Oriented Approach:**

- Customer Sarah "knows" her own details
- Orders "belong to" specific customers
- Updates happen in one place
- System stays consistent
:::

:::

---

## Key Business Benefits

::: {.incremental}
1. **Consistency**: Information lives in one logical place
2. **Scalability**: Easy to add new customers, orders, products
3. **Maintainability**: Changes don't break the whole system
4. **Reusability**: Same customer object used across the business
5. **Real-world mapping**: Code matches how business actually works
:::

---

## Your Banking App Example

::: {.fragment}
**Your bank account app uses objects:**

- **Account object**: balance, account number, transaction history
- **Transaction object**: date, amount, description, category  
- **Customer object**: name, address, accounts owned
:::

::: {.fragment}
**When you check your balance**: The Account object calculates it from all Transaction objects

**When you transfer money**: Creates new Transaction objects in both accounts
:::

---

## Module 1 Checkpoint

::: {.callout-note}
## Before Moving to Module 2

Can you explain to a friend:

1. How your favorite app (Instagram, Spotify, banking) might use objects?
2. Why objects are better than spreadsheets for complex business data?
3. The difference between the "blueprint" (what all customers have in common) and individual customers?

*If yes, you're ready for Module 2!*
:::

---

## Coming Up: Module 2

**"Your Finance App Needs Digital Filing Cabinets"**

We'll design the Transaction object that your Smart Finance App actually needs, and see how it solves real business problems.

::: {.fragment}
*Spoiler: It's going to make handling CSV files AND individual entries much easier!*
:::