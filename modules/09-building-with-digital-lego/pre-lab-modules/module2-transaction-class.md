---
title: "Your Finance App Needs Digital Filing Cabinets"
subtitle: "Module 2: Classes as Business Templates"
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

## The Business Problem {.center}

::: {.r-fit-text}
Your finance app needs to handle **thousands of transactions** from different sources
:::

::: {.fragment}
**Without organisation = Digital chaos** 📊💥
:::

---

## The Messy Reality

::: {.columns}

::: {.column width="50%"}
**Your Data Sources:**

- CSV files from bank (500+ transactions)
- Manual expense entries from employees  
- Recurring payment schedules
- Budget categories and limits
- User questions via chatbot
:::

::: {.column width="50%"}
**Your Boss Wants:**

- "How much did we spend on coffee this month?"
- "Which department is over budget?"
- "Show me all transactions over $100"
- "Generate a monthly spending report"
:::

:::

::: {.fragment}
**The Challenge:** How do you organize this chaos into a system that can answer these questions?
:::

---

## Enter: The Transaction Blueprint

::: {.callout-tip}
## Think Like a Business

What information defines **every** financial transaction?

- Date: "When did this happen?"
- Description: "What was this for?"  
- Amount: "How much?" (+ for income, - for expenses)
- Category: "What type of spending?"
:::

::: {.fragment}
**This becomes our Transaction "template" or "blueprint"**
:::

---

## 🤖 AI Exploration: The Natural Solution

::: {.callout-note}
## Try This Prompt

*"I have these 10 random transactions as a simple list. How would you organize them so I can easily find all coffee purchases, or all transactions over $50?"*

**Sample transactions:**
- Starbucks Coffee, -$4.50, Food, 2025-09-20
- Salary Deposit, +$3000, Income, 2025-09-15  
- Office Supplies, -$67.80, Business, 2025-09-18
:::

::: {.fragment}
**What will AI suggest?** Grouping, structuring, standardizing - exactly what a class does!
:::

---

## From Chaos to Structure

::: {.columns}

::: {.column width="50%"}
**Before: Scattered Data**
```
"Coffee -4.50 2025-09-20"
"Salary +3000.00 15/09/25"
"office supplies -67.8 Sep 18"
```

*Different formats, inconsistent, hard to analyze*
:::

::: {.column width="50%"}
**After: Structured Objects**
```
Transaction 1:
  description: "Coffee"
  amount: -4.50
  category: "Food" 
  date: "2025-09-20"

Transaction 2:
  description: "Salary"
  amount: +3000.00
  category: "Income"
  date: "2025-09-15"
```
:::

:::

---

## The Transaction Class Blueprint

::: {.fragment}
**What every Transaction needs to store:**

- `description`: "Starbucks Coffee"
- `amount`: -4.50 (negative = expense)
- `category`: "Food"
- `date`: "2025-09-23"
:::

::: {.fragment}
**What every Transaction should be able to do:**

- `is_expense()`: Check if amount is negative
- `is_large_purchase()`: Check if over a certain limit
- `format_for_display()`: Show nicely for users
:::

---

## Real-World Connection: Banking Systems

::: {.callout-important}
## This Is How Banks Actually Work

Every transaction in your bank statement is an object with:

- **Standardized format**: Date, description, amount, balance
- **Consistent behavior**: All debits show as negative, all credits as positive
- **Easy querying**: "Show me all ATM withdrawals this month"
- **Reliable calculations**: Balance = previous balance + transaction amount
:::

::: {.fragment}
Banks process **millions** of transactions daily using this exact pattern!
:::

---

## 🤖 AI-Assisted Learning: Build Your Blueprint

::: {.callout-tip}
## Your Turn - Guide the AI

**Step 1:** *"Write a Python class named Transaction that stores date, description, amount, and category."*

**Step 2:** *"Add a method called is_expense that returns True if amount is negative."*

**Step 3:** Test it - create two different transactions and verify they work
:::

::: {.fragment}
**Critical Skill:** You're learning to **direct AI** to build what you need, then **test and verify** it works correctly.
:::

---

## The Power Pattern: Template + Instances

::: {.columns}

::: {.column width="50%"}
**One Blueprint (Class):**
```
Transaction Template:

- description (text)
- amount (number)  
- category (text)
- date (date)
- is_expense() method
```
:::

::: {.column width="50%"}
**Many Instances (Objects):**
```
coffee_purchase = Transaction(
  "Coffee", -4.50, "Food", "2025-09-23")

salary = Transaction(
  "Salary", +3000, "Income", "2025-09-15")

office_supplies = Transaction(
  "Supplies", -67.80, "Business", "2025-09-18")
```
:::

:::

::: {.fragment}
**One template creates unlimited instances - just like business forms!**
:::

---

## Solving the CSV vs Individual Entry Problem

::: {.fragment}
**The Breakthrough:** Both CSV data AND manual entries become Transaction objects!

- **Loading from CSV**: Each row becomes a Transaction object
- **Manual entry**: User input creates a new Transaction object  
- **Analysis**: Work with objects regardless of their source
- **Storage**: Save objects back to CSV when needed
:::

::: {.fragment}
**Same structure, same methods, same reliability** - whether you have 1 transaction or 1 million!
:::

---

## Business Benefits in Action

::: {.incremental}
1. **Consistency**: Every transaction follows the same rules
2. **Validation**: Can't create invalid transactions (empty description, etc.)
3. **Easy Filtering**: `if transaction.is_expense()` works on any transaction
4. **Scalability**: Add new transaction types without breaking existing code
5. **Integration**: Works with CSV files, databases, APIs, user input
:::

---

## Module 2 Checkpoint

::: {.callout-note}
## Ready for Module 3?

Can you explain:

1. Why a Transaction class is better than storing transactions as simple text?
2. How the same Transaction blueprint works for both CSV data and manual entries?
3. What business problems this structure solves?

**Test yourself:** Ask AI to create a simple Customer class, then critique its response.
:::

---

## Coming Up: Module 3

**"Making Your Objects Work Together (Like a Real Business)"**

Individual transactions are useful, but businesses need **systems** that connect multiple objects to solve complex problems.

::: {.fragment}
*Preview: How does a FinanceTracker manage hundreds of Transaction objects to generate reports and answer business questions?*
:::