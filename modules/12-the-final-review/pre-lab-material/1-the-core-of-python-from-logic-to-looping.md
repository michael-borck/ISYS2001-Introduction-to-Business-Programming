---
title: "Review Module 1: The Core of Python" 
subtitle: "From Logic to Looping" 
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

This module revisits the fundamental building blocks of programming you learned.

You started by giving the computer a memory with **variables**, taught it how to think with **conditional logic**, and finally, made it perform repetitive tasks efficiently with **loops**.

These core concepts are the foundation for everything you built afterward.

## **Giving the Computer Memory: Variables**

You learned that to get a computer to remember anything, you needed to store information in **variables**. These were the named containers for your data.

You worked with the basic data types:

* **Strings (str):** For text, like a user's name, "Alice".  
* **Integers (int):** For whole numbers, like an age, 25\.  
* **Floats (float):** For numbers with decimals, like an expense, 12.99.  
* **Booleans (bool):** For storing truth values, True or False.

\# You stored user preferences in variables  
user\_name \= "Alice"  
favourite\_colour \= "Blue"  
monthly\_income \= 4500.50  
is\_student \= True

## **Making the Computer Think: Conditional Logic**

You taught your programs to make decisions using if, elif, and else. This allowed your code to respond differently based on conditions.

The structure you used followed a clear logic:

* if: Checked the first condition.  
* elif: Checked a new condition only if the one before it was false.  
* else: Provided a default action if no other conditions were met.

This was the key to moving from simple scripts to programs with intelligent behaviour.

## **A Familiar Example: The Grade Calculator**

You applied conditional logic to solve real-world problems. The grade calculator was a perfect example of using an if-elif-else chain to handle multiple options.

You learned that the **order of conditions was critical**. Checking from the highest score to the lowest ensured the logic worked correctly.

score \= 85

if score \>= 90:  
    grade \= "A"  
elif score \>= 80:  
    grade \= "B" \# This is chosen  
elif score \>= 70:  
    grade \= "C"  
else:  
    grade \= "F"

\# The program decided the grade was "B"

## **Handling Complex Decisions**

You quickly moved beyond simple comparisons by combining conditions with logical operators. This allowed you to build more sophisticated decision-making systems, like a "Smart Purchase Advisor."

* **and**: Required all conditions to be true.  
  * *e.g., if credit\_score \>= 650 and income \>= 40000:*  
* **or**: Required at least one condition to be true.  
  * *e.g., if day \== "Saturday" or day \== "Sunday":*  
* **not**: Reversed a condition's outcome.  
  * *e.g., if not is\_raining:*

## **Why Programs Need to Repeat**

You discovered that writing code one line at a time wasn't practical for handling large amounts of data. This led to the core concept of **repetition**.

Whether it was processing a whole playlist of songs or entering multiple expenses, you needed a way to tell the computer, "Do this task over and over again."

This is where you learned about **loops**, the tools that allow programs to scale and handle real-world data efficiently.

## **Repetition for Unknown Durations: while Loops**

When you didn't know how many times a task needed to repeat, you used a while loop. This was perfect for **input validation**.

The pattern was simple: "Keep asking while the input is not valid."

\# You used this pattern to ensure the budget was valid  
budget \= 0  
while budget \< 100 or budget \> 50000:  
    try:  
        budget\_str \= input("Enter budget ($100-$50,000): $")  
        budget \= float(budget\_str)  
        if budget \< 100 or budget \> 50000:  
            print("Invalid amount. Please try again.")  
    except ValueError:  
        print("Please enter a valid number.")

print(f"Budget set to: ${budget:.2f}")

## **Repetition for Known Durations: for Loops**

When you knew exactly how many times to repeat, or you had a collection of items to process, the for loop was your tool of choice.

* **Counted Repetition:** You used range() to perform a task a specific number of times.  
  * *e.g., for i in range(3): to set up three savings goals.*  
* **Collection Processing:** You iterated through items in a list.  
  * *e.g., for expense in expenses: to process every transaction.*

## **Working with Collections: Lists and Loops**

You learned that to handle multiple pieces of data, like a series of expenses, you needed to store them in a **list**.

Lists gave your program a way to hold and manage a collection of items. Combined with for loops, this unlocked powerful data processing capabilities.

\# A common pattern you mastered  
expenses \= \[45.50, 12.00, 89.95, 3.50\]  
total\_spent \= 0

\# You looped through the collection to perform a calculation  
for expense in expenses:  
    total\_spent \= total\_spent \+ expense

average\_expense \= total\_spent / len(expenses)

print(f"Total spent: ${total\_spent:.2f}")  
print(f"Average expense: ${average\_expense:.2f}")

## **Key Takeaways from Module 1**

* You learned to give your programs **memory** using variables and data types.  
* You taught your programs to **think** and make decisions with if, elif, and else.  
* You mastered **repetition**, the key to making programs efficient, using both while and for loops.  
* You started working with **collections** of data using lists, preparing you for real business data.

These skills formed the essential foundation for building your first interactive applications.

## **Look Ahead to Module 2**

You've mastered the core logic. Next, you'll review how you:

* **Structured your code** into reusable functions.  
* Began working with more complex **data structures** and files.  
* Used pandas to tackle real business data from **CSVs**.

This is where your scripts started evolving into professional applications.