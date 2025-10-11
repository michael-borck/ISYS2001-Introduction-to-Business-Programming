---
title: "Making Your Objects Work Together"
subtitle: "Module 3: Like a Real Business System"
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

## Individual vs System Thinking {.center}

::: {.columns}

::: {.column width="50%"}
**Individual Transaction:**

- "Coffee purchase: $4.50"
- Useful for recording one event
:::

::: {.column width="50%"}
**Business Questions:**

- "What's my spending pattern this month?"
- "Which category am I overspending in?"
- "Am I on track with my budget?"
:::

:::

::: {.fragment}
**The Gap:** Individual objects can't answer business-level questions
:::

---

## Real Business Challenge

::: {.callout-important}
## Your Smart Finance App Needs

**Data Sources:**
- Historical transactions from CSV (500+ records)
- New manual entries from users
- Budget limits by category

**Business Intelligence:**
- Monthly spending reports
- Budget vs actual comparisons  
- Spending trend analysis
- Category-based insights
- Automated alerts and warnings
:::

---

## Enter: The System Object

::: {.fragment}
**FinanceTracker** - The "manager" that coordinates everything:

- **Holds** all individual Transaction objects
- **Organizes** them for analysis  
- **Calculates** summaries and reports
- **Manages** interactions between data sources
- **Provides** business intelligence
:::

::: {.fragment}
*Think of it as the "office manager" that knows about all the individual transactions*
:::

---

## How Real Businesses Work

::: {.columns}

::: {.column width="50%"}
**Restaurant Example:**

- **Individual Objects:**
  - Order #1234
  - Customer "John Smith"  
  - Menu Item "Burger"

- **System Object:**
  - Restaurant Manager
  - Tracks all orders
  - Manages all customers
  - Coordinates everything
:::

::: {.column width="50%"}
**Banking Example:**

- **Individual Objects:**
  - Transaction #5678
  - Account #9999
  - Customer "Sarah"

- **System Object:**  
  - Banking System
  - Processes all transactions
  - Manages all accounts
  - Generates statements
:::

:::

---

## The FinanceTracker System

::: {.fragment}
**What it manages:**

- Collection of all Transaction objects
- Budget limits for each category
- Running totals and balances
- Analysis and reporting logic
:::

::: {.fragment}
**What it can do:**

- Load transactions from CSV files
- Add new individual transactions
- Calculate spending by category  
- Generate budget alerts
- Create monthly reports
- Answer user questions
:::

---

## 🤖 AI Exploration: System Design

::: {.callout-tip}
## Try This Prompt

*"I need a system that can store multiple transactions and answer questions like 'How much did I spend on food this month?' and 'Am I over budget in any category?' How would you design this?"*

**Follow-up:** *"How would this system handle both bulk data from CSV files and individual new transactions?"*
:::

::: {.fragment}
**What will AI suggest?** A container object that manages collections of individual objects - exactly our pattern!
:::

---

## The Collaboration Pattern

::: {.columns}

::: {.column width="50%"}
**FinanceTracker (System):**
```
Properties:

- transactions: [list of Transaction objects]
- monthly_budget: {category: amount}
- current_month: "2025-09"

Methods:
- load_from_csv(filename)
- add_transaction(transaction)
- spending_by_category(category)
- budget_status()
- monthly_report()
```
:::

::: {.column width="50%"}
**Transaction (Individual):**
```
Properties:

- description: "Coffee"
- amount: -4.50
- category: "Food"
- date: "2025-09-23"

Methods:
- is_expense()
- is_large_purchase()
- format_display()
```
:::

:::

---

## The Magic: Bulk + Individual Processing

::: {.fragment}
**Loading Historical Data:**

1. Read CSV file (500+ transactions)
2. Create Transaction object for each row
3. Add all objects to FinanceTracker
:::

::: {.fragment}
**Adding New Entries:**

1. User enters transaction details
2. Create new Transaction object  
3. Add to same FinanceTracker
:::

::: {.fragment}
**Analysis Works on Both:**

- `tracker.spending_by_category("Food")` works whether you have 10 or 10,000 transactions
- Same methods, same reliability, unlimited scale
:::

---

## Business Intelligence in Action

::: {.fragment}
**Budget Analysis:**
```python
# FinanceTracker can answer complex questions
spending = tracker.spending_by_category("Food")
budget = tracker.monthly_budget["Food"]

if spending > budget:
    return "⚠️ Over budget in Food category!"
```
:::

::: {.fragment}
**This is exactly how business dashboards work** - objects collaborate to provide insights
:::

---

## 🤖 AI-Assisted Building

::: {.callout-tip}
## Progressive Development

**Step 1:** *"Create a FinanceTracker class that can store multiple transactions"*

**Step 2:** *"Add a method to calculate total spending by category"*  

**Step 3:** *"Add budget comparison with alert messages"*

**Step 4:** *"How would this integrate with CSV loading and user input?"*
:::

::: {.fragment}
**Your Role:** Guide the AI, test the results, understand the connections between objects
:::

---

## Real-World System Examples

::: {.incremental}
- **E-commerce:** A **ShoppingCart** (system object) manages multiple **Product** objects
- **CRM:** A **CustomerManager** (system object) organizes a collection of **Customer** objects  
- **Payroll:** A **PayrollSystem** (system object) processes multiple **Employee** objects
- **Inventory:** A **StockManager** (system object) tracks a collection of **Product** objects
- **Project Management:** A **ProjectTracker** (system object) coordinates individual **Task** objects
:::

::: {.fragment}
**The Pattern:** System objects coordinate individual objects to solve business problems
:::

---

## Integration with Your Assignment

::: {.callout-note}
## Your Smart Finance App

**Individual Objects:**
- Transaction (for each expense/income)
- User (for personalization)
- BudgetCategory (for spending limits)

**System Objects:**  
- FinanceTracker (manages all transactions)
- ChatBot (answers user questions)
- ReportGenerator (creates summaries)

**User Interface:**
- Gradio components (also objects!) that collect input and display results
:::

---

## The Complete Picture

::: {.columns}

::: {.column width="50%"}
**Data Flow:**

1. CSV loads → Transaction objects
2. User input → new Transaction objects
3. All stored in FinanceTracker system
4. ChatBot queries FinanceTracker  
5. Results displayed via Gradio objects
:::

::: {.column width="50%"}
**Object Collaboration:**

- User Interface objects ↔ System objects
- System objects ↔ Individual objects  
- AI chatbot ↔ All objects
- Everything working together seamlessly
:::

:::

---

## Module 3 Checkpoint

::: {.callout-note}
## Ready to Build?

Can you explain:

1. Why you need both individual Transaction objects AND a system FinanceTracker object?
2. How the same system handles CSV data and manual entries?
3. How objects collaborate to answer complex business questions?

**Final Test:** Describe how your favorite app (Instagram, Spotify) might use this individual + system object pattern.
:::

---

## What's Next: Implementation

::: {.fragment}
**You now understand:**

- Objects mirror real business thinking
- Classes provide templates for consistency
- Systems coordinate individual objects
- The same patterns work at any scale
:::

::: {.fragment}
**Ready for the worksheet:** Time to see these concepts in action with actual code and your Smart Finance App!
:::

::: {.fragment}
*Spoiler: When you write `gr.Textbox()`, you're creating objects that will work with your Transaction and FinanceTracker objects!*
:::

---

## Summary: The OOP Mindset {.center}

::: {.r-fit-text}
**OOP is how businesses naturally organise**

**Individual things** + **Systems that manage them** = **Scalable solutions**
:::

::: {.fragment}
*Now you're thinking like a systems analyst!*
:::