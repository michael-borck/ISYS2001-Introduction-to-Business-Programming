---
title: "Review Module 3: Building Professional and Robust Applications"
subtitle: "From Scripts to Systems"
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

In this module, you'll revisit how you moved beyond simple scripts to build applications that were **robust**, **connected**, and **professionally structured**.

You learned to anticipate problems, interact with the wider web, and organise your code to mirror real-world business systems. These skills are what separate a simple script from a true business application.

## **Expecting the Unexpected: Error Handling**

You learned that real-world applications can't just work on the "happy path." They must be **robust** and handle unexpected situations gracefully.

Your primary tool for this was the try...except block, which you used as a "safety net" for risky code.

* **try block:** This was your "Plan A," where you optimistically ran code that might fail (like reading a user's uploaded file).  
* **except block:** This was your "Plan B," which ran only if a specific error occurred, preventing your app from crashing and providing a helpful message to the user.

## **Error Handling in Action**

You practiced building robust applications by deliberately trying to break them and then implementing try...except to handle the failures. This was crucial for creating a user-friendly Gradio app.

import pandas as pd

def process\_file\_robustly(uploaded\_file):  
    try:  
        \# Plan A: Try to read the file  
        df \= pd.read\_csv(uploaded\_file.name)  
        return f"Successfully loaded {len(df)} rows."  
    except pd.errors.ParserError:  
        \# Plan B: Handle the case where it's not a valid CSV  
        return "Error: Please upload a valid CSV file."  
    except AttributeError:  
        \# Plan C: Handle the case where no file was uploaded  
        return "Error: Please upload a file before processing."

## **Phoning a Friend: Working with APIs**

You learned that your applications could connect to the internet to fetch live data using **APIs (Application Programming Interfaces)**.

This allowed you to incorporate real-time information, such as stock prices or weather data, directly into your programs. You used the requests library to make these connections.

import requests

\# You learned to make a request to an API endpoint  
api\_url \= "\[https://api.example.com/data\](https://api.example.com/data)"  
response \= requests.get(api\_url)

\# And then process the data that came back  
data \= response.json() 

This skill was key to building dynamic, data-driven applications.

## **Understanding Web Data: The JSON Format**

When you received data from an API, it was often in **JSON (JavaScript Object Notation)** format. You learned that JSON was a standard way to structure data using key-value pairs, much like a Python dictionary.

A crucial step was converting this JSON text into a Python object (usually a dictionary or a list of dictionaries) that you could easily work with in your code.

\# API response in JSON format (as a string)  
json\_string \= '{"product": "Laptop", "price": 1899.00, "in\_stock": true}'

\# You converted it into a Python dictionary  
import json  
product\_data \= json.loads(json\_string)

\# Now you could work with it like any other dictionary  
print(f"The {product\_data\['product'\]} costs ${product\_data\['price'\]:.2f}")

## **Building with Digital Lego: Object-Oriented Programming**

You took a major step toward professional software design when you were introduced to **Object-Oriented Programming (OOP)**.

You learned to think of your program in terms of real-world "things" or **objects**. The core idea was creating a **class** as a blueprint, and then making individual copies, or **instances**, of that blueprint.

This approach mirrored how businesses naturally organise information, with templates (like a customer form) and individual instances (each filled-out form).

## **OOP in Action: The Transaction Class**

Your finance application became much more organised when you created a Transaction class. This blueprint ensured that every single transaction in your system had the same structure and capabilities.

\# You created a blueprint for all transactions  
class Transaction:  
    def \_\_init\_\_(self, description, amount, category):  
        self.description \= description  
        self.amount \= amount  
        self.category \= category

    def is\_expense(self):  
        return self.amount \< 0

\# Then you created individual instances (objects) from that blueprint  
coffee\_purchase \= Transaction("Morning coffee", \-4.50, "Food")  
salary \= Transaction("Paycheck", 3000.00, "Income")

\# You could then ask each object to perform actions  
print(f"Was coffee an expense? {coffee\_purchase.is\_expense()}") \# True  
print(f"Was salary an expense? {salary.is\_expense()}")   \# False

## **A New Mindset: Verification and Debugging**

In the final phase of building your foundational skills, you learned to shift your mindset from just *writing* code to **proving that it works correctly**.

* **Verification:** The process of checking if your code meets the specifications.  
* **Debugging:** The systematic investigation into why your code isn't working as expected.

You learned that your role as an AI-assisted developer was not just to generate code, but to be the **architect of quality**.

## **The Foundation of Testing: Assertions**

You learned that the simplest way to verify your code was with an **assert** statement. An assertion is a simple declaration: "I claim this must be true." If the claim is false, the program stops.

Assertions became your way of creating **executable specifications**—clear, testable definitions of what "correct" means for a piece of code.

def calculate\_discount(price, percent):  
    return price \* (percent / 100\)

\# These assertions SPECIFY and VERIFY the function's behaviour  
assert calculate\_discount(100, 10\) \== 10.0  
assert calculate\_discount(200, 5\) \== 10.0

## **Key Takeaways from Module 3**

* You learned to build **robust** applications by anticipating errors and handling them with try...except.  
* You learned how to **connect your programs to the web** using APIs to fetch live data in JSON format.  
* You started thinking like a software architect by using **Object-Oriented Programming** to model business concepts with classes and objects.  
* You adopted a **professional verification mindset**, learning to prove your code's correctness with assertions and to debug systematically.

## **Look Ahead to Module 4**

You've built robust, structured, and verified applications. Next, you'll review how you solidified your role as an **AI-First Developer**. You'll revisit:

* The strategies for effective **AI collaboration**.  
* The art of writing **good prompts** and **critiquing AI code**.  
* The professional practices of **documentation** and **version control**.

This final module focuses on the mindset that makes you an effective and modern business programmer.