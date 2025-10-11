---
title: "From Procedural to Object-Oriented: A Refactoring Journey"
subtitle: "Mastering Python's OOP Features for Better Software Design"
author: "Michael Borck"
format: 
  pptx:
    reference-doc: ../../../_assets/template.pptx
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


# Introduction to Refactoring

* Understanding the need for refactoring
* Procedural vs Object-Oriented Programming
* Benefits of moving to Object-Oriented Code

::: {.notes}
Welcome to our session on refactoring procedural code to object-oriented code in Python. Refactoring involves modifying the code to improve its structure without changing its functionality. This process is crucial for maintaining code efficiency and readability as projects grow. Today, we'll explore why and how to transition from a procedural to an object-oriented approach, which promotes modularity and reusability in programming.
:::

# What is Object-Oriented Programming?

* Definition of Object-Oriented Programming (OOP)
* Core concepts: Classes, Objects
* Encapsulation, Inheritance, and Polymorphism

::: {.notes}
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data in the form of fields (often known as attributes), and code, in the form of procedures (often known as methods). OOP allows programmers to create modules that can be reused across different programs. The three pillars of OOP—encapsulation, inheritance, and polymorphism—help in building secure and robust programs.
:::

# Analysing a Procedural Code Example

* Typical structure of procedural code
* Example: Weather Dashboard procedural implementation
* Limitations in scalability and maintenance

::: {.notes}
Let's start with a procedural code example from a typical Weather Dashboard application. This code is linear and function-based, which can make it harder to manage as it grows. Procedural code often becomes more complex and difficult to maintain as new features are added. This complexity can lead to errors and reduce the code's overall reliability.
:::

# Introducing Classes and Objects

* Converting procedural code into classes
* Defining attributes and methods
* Example: Refactoring Weather Dashboard

::: {.notes}
To refactor our procedural code, we begin by identifying natural groupings of data and functions, which can be transformed into classes and objects. For instance, a 'Weather' class could encapsulate attributes like temperature and humidity, along with methods to compute forecast details. This encapsulation makes the code more organized and readable.
:::

# Implementing Inheritance

* What is inheritance?
* Benefits of using inheritance in refactoring
* Example: Extending the Weather class

::: {.notes}
Inheritance is a powerful feature of OOP that allows a new class to inherit attributes and methods from an existing class. In our Weather Dashboard, we might have a general 'Weather' class and specialised classes like 'RainyWeather' or 'SunnyWeather' that inherit from it. This approach reduces redundancy and enhances the clarity of the code structure.
:::

# Exploring Polymorphism

* Concept of polymorphism in OOP
* How polymorphism enhances flexibility
* Example: Different display methods for weather conditions

::: {.notes}
Polymorphism gives us the flexibility to call the same method on different objects and have each of them respond in a unique way. In the context of our Weather Dashboard, polymorphism allows different weather classes to use a common interface for displaying information, which the specific class can override to reflect different weather conditions appropriately.
:::

# Case Study: Refactoring in Action

* Step-by-step refactoring process
* Before and after code comparison
* Challenges faced and how they were resolved

::: {.notes}
Now, let's look at a practical refactoring case study. We'll take a procedural version of the Weather Dashboard and step through its transformation into an OOP design. This will include creating classes, implementing inheritance, and utilising polymorphism. We'll also discuss the challenges encountered during refactoring, such as integrating legacy code and testing changes.
:::

# Benefits of OOP Refactoring

* Improved code readability and maintenance
* Enhanced ability to extend and manage large applications
* Facilitates teamwork and code reuse

::: {.notes}
Refactoring to OOP offers numerous benefits. The code becomes easier to understand, which simplifies maintenance. It's also more scalable, making it easier to extend with new features without disrupting existing functionality. Additionally, OOP's modular nature enhances teamwork by allowing developers to work on different modules simultaneously without conflict.
:::

# Conclusion and Next Steps

* Review of key concepts and benefits
* Encouragement to practice refactoring
* Resources and further learning

::: {.notes}
To summarise, refactoring from procedural to object-oriented code in Python enhances code quality and development efficiency. We encourage you to apply these concepts to refactor your own projects. Continue your learning journey with further resources like Python’s official documentation on classes and real-world examples from sites like Real Python.
:::