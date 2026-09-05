---
title: "Review Module 2: Structuring Code and Data" 
subtitle: "From Simple Scripts to Data-Driven Programs"
format: 
  pptx:
    reference-doc: curtin_template.pptx
  html:
    theme: 

      - cosmo
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


## **Welcome to Your Review**

In this module, you'll revisit the crucial step where your simple scripts began to evolve into more powerful and professional applications.

You learned how to **organise your code** into reusable blocks called **functions**, and you started to work with more complex **data structures** and external data from **CSV files**.

## **Organising Your Code: Functions**

You discovered that as programs grew, you needed a way to manage complexity. **Functions** were the answer. You learned to bundle related code into reusable blocks that perform a specific task.

This was your first step toward modular programming, mirroring how real business processes are broken down into manageable tasks.

\# You defined a simple function like this  
def calculate\_tip():  
    bill \= float(input("Enter bill amount: $"))  
    tip\_percent \= float(input("Enter tip percentage: "))  
      
    tip\_amount \= bill \* (tip\_percent / 100\)  
    total\_bill \= bill \+ tip\_amount  
      
    print(f"Tip: ${tip\_amount:.2f}")  
    print(f"Total: ${total\_bill:.2f}")

\# And called it to make it run  
calculate\_tip()

## **Making Functions Flexible and Collaborative**

You quickly learned that just printing a result wasn't enough for building bigger systems.

* **Parameters:** You learned to pass data *into* your functions, making them flexible.  
* **Return Values:** You used the return statement to get results *out* of your functions.

This was a critical skill because it allowed your functions to **work together**. The output from one function could become the input for another, just like in a real business workflow.

## **Return vs. Print: A Professional Distinction**

You learned the crucial difference between displaying information and providing a usable result.

\# A function that returns a value is more useful  
def calculate\_monthly\_payment(principal, annual\_rate, months):  
    \# ... calculation logic ...  
    return payment\_amount

\# You could then use the result in another part of your program  
loan\_payment \= calculate\_monthly\_payment(25000, 0.05, 60\)  
remaining\_income \= monthly\_income \- loan\_payment

print(f"After your loan payment of ${loan\_payment:.2f}, you have ${remaining\_income:.2f} left.")

Returning values enabled you to build more complex, interconnected logic.

## **Expanding Your Toolkit with Modules**

You learned that you didn't have to build everything from scratch. Python's **modules** provided pre-built toolkits for common tasks.

A key module you used was datetime, which allowed you to work with dates and times—essential for timestamping financial transactions.

import datetime

\# You used modules to add professional features  
timestamp \= datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
print(f"Transaction recorded at: {timestamp}")

This was your introduction to leveraging the vast Python ecosystem.

## **Handling More Complex Data: Dictionaries**

As your data needs grew more complex, you moved beyond simple lists to **dictionaries**. Dictionaries allowed you to store information as **key-value pairs**, creating more structured and readable data.

This was perfect for representing a single, detailed record, like one complex transaction.

\# You stored structured data in a dictionary  
transaction \= {  
    "date": "2024-08-01",  
    "description": "Woolworths Weekly Shop",  
    "amount": 45.50,  
    "category": "Groceries"  
}

\# And accessed it using keys  
print(f"Spent ${transaction\['amount'\]} on {transaction\['category'\]}")

## **The Pivot Moment: Handling Real Business Data**

The most significant leap in this part of the course was the shift to becoming a **"code director."** You stopped writing every line of code manually and started directing AI to solve business problems.

This is where you were introduced to **pandas**, the industry-standard library for working with tabular data, like the CSV files common in business.

## **Taming Business Data with Pandas**

You learned that pandas makes working with CSV files incredibly efficient. Instead of writing complex loops to read a file line by line, you could load an entire dataset with a single command.

This was a major step in preparing you for your final project, the **Smart Finance Assistant**, which relies heavily on processing CSV transaction data.

import pandas as pd

\# You loaded an entire CSV file in one line  
df \= pd.read\_csv('transactions.csv')

\# And performed powerful analysis with simple commands  
print("Spending Summary by Category:")  
print(df.groupby('Category')\['Amount'\].sum())

## **Key Takeaways from Module 2**

* You learned to **structure your code** into reusable functions, making your programs modular and professional.  
* You mastered how to pass data between functions using **parameters** and **return values**.  
* You expanded your capabilities by importing external **modules** like datetime.  
* You began handling more complex, structured data with **dictionaries**.  
* You made the pivotal shift to becoming a **code director**, using **pandas** and AI to efficiently process real-world business data from CSV files.

## **Look Ahead to Module 3**

You've learned to structure code and handle data. Next, you'll review how you made your applications:

* **Robust:** Handling errors and unexpected situations gracefully.  
* **Connected:** Fetching live data from the web using APIs.  
* **Professionally Structured:** Using Object-Oriented Programming (OOP) to model real-world business systems.

This is where your applications started to become truly professional-grade.