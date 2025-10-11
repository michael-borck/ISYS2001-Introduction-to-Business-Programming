---
title: "Designing a Simple Menu"
subtitle: "Module 4: Building a Text-Based Menu Interface"
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
# Overview  
In this module, we'll learn how to create a text-based menu interface using basic output and input.  
You'll understand the steps needed to display a menu and capture the user's choice.

::: {.notes}
The "Overview" slide provides a high-level summary of the presentation, introducing the concept of a menu interface and its role in user interaction. It sets the stage for the subsequent slides, which will delve into the specifics of implementing menu interfaces using Python programming techniques.

The slide outlines the key topics that will be covered throughout the presentation, including the definition of a menu interface, displaying menus using the `print()` function, capturing user input, and a practical example of a simple menu programme. Additionally, it highlights the inclusion of a practice exercise and a summary of the key points, along with a look ahead to the next steps in the learning journey.
:::

# What Is a Menu Interface?  
- A menu interface presents the user with numbered options.  
- It guides the user to choose between different functionalities or messages.  
- This is a common technique to improve the user experience in text-based programmes.

::: {.notes}
A menu interface is a powerful tool for guiding users through text-based programmes. It presents users with a list of numbered options, each corresponding to a specific functionality or message. By selecting an option, the user can easily navigate to their desired action without the need for complex commands or inputs.

Menu interfaces are a common technique for improving user experience in text-based programmes. They provide a clear and intuitive structure that helps users understand the available options and make informed decisions. By breaking down the programme into distinct choices, menu interfaces reduce confusion and make the programme more accessible to a wider range of users.
:::

# Displaying a Menu with `print()`  
- Use the `print()` function to list out the menu options.  
- Each option is displayed on a separate line for clarity.  
- Example:
  
  ```python
  print("1. Show greeting")
  print("2. Display farewell")
  ```

::: {.notes}
The `print()` function is a powerful tool for displaying information to users, and it's particularly useful when creating menu interfaces. By using `print()` to list out the available options, each on a separate line, you can present a clear and easily readable menu to the user. This approach helps to avoid confusion and ensures that the user can quickly identify and select their desired choice.

To illustrate this concept, the slide includes an example of how a menu might be displayed using `print()`. By examining this example, you can see how the function is used to create a well-formatted menu, with each option presented on a new line for improved readability. This example serves as a foundation for understanding how to create effective menu interfaces in your own programs.
:::

# Capturing User Input  
- Use the `input()` function to prompt the user for a choice.  
- Store the user's input in a variable for further processing.  
- Example:
  
  ```python
  choice = input("Enter your choice (1 or 2): ")
  ```
  
- This allows your programme to react based on the user's selection.

::: {.notes}
To capture user input in your programme, use the `input()` function, which prompts the user to enter a choice. The user's response is then stored in a variable for further processing within the programme. For example, you might display a menu of options and ask the user to select one by entering a corresponding number or letter.

By capturing and storing the user's input, your programme can react dynamically based on the selection made. This allows for interactive decision-making and enables your programme to follow different paths or perform specific actions depending on the user's preferences. Utilising the `input()` function is a fundamental way to create responsive and engaging command-line interfaces that adapt to user input.
:::

# Example: A Simple Menu Programme  
- Combining `print()` and `input()` to create a functional menu:
  
  ```python
  print("Menu:")
  print("1. Show greeting")
  print("2. Display farewell")
  choice = input("Enter your choice (1 or 2): ")
  
  if choice == "1":
      print("Hello! Welcome to our programme.")
  elif choice == "2":
      print("Goodbye! Have a nice day.")
  else:
      print("Invalid choice. Please try again.")
  ```
  
- This snippet demonstrates how to guide the user and respond to their input.

::: {.notes}
This slide demonstrates how to create a functional menu by combining the `print()` and `input()` functions in Python. The code snippet guides the user through a series of options and prompts them to make a selection, which the program then responds to accordingly.

By presenting a clear and concise menu interface, the user can easily navigate the available choices and interact with the program effectively. This example serves as a foundation for building more complex menu-driven applications, highlighting the importance of user-friendly design and logical flow in software development.
:::

# Practice Exercise  
- Create your own menu programme that lets a user choose between two simple messages.  
- Steps to follow:
  1. Display two menu options using `print()`.
  2. Prompt the user to enter their choice with `input()`.
  3. Use an if-else structure to print the corresponding message.
- Experiment with different messages and options.

::: {.notes}
To complete this practice exercise, create your own simple menu programme that presents the user with a choice between two messages. Experiment with different messages and options to gain a better understanding of how menu interfaces work. Follow the steps outlined in the previous slides to guide you through the process of displaying the menu using `print()` statements and capturing the user's input.

This exercise provides an opportunity to apply the concepts covered so far and reinforce your learning. Feel free to be creative with your messages and options, and don't hesitate to try different variations to see how they affect the user experience. By practising and experimenting with menu interfaces, you'll develop a stronger grasp of the fundamentals and be better prepared for more advanced programming challenges.
:::

# Summary and Next Steps  
- You learned how to build a text-based menu using basic Python functions.  
- Key points:
  - Display options with `print()`.
  - Capture choices using `input()`.
  - Process user input with conditional statements.
- With these skills, you're ready to create interactive programmes that respond to user selections.

::: {.notes}
In this slide, we summarise the key points you've learned about building a text-based menu using basic Python functions. You now know how to display menu options using the `print()` function, capture user choices with `input()`, and process user input using conditional statements. These fundamental skills form the foundation for creating interactive programmes that respond to user selections.

With the knowledge gained from this presentation, you're ready to apply these techniques to develop your own menu-driven programmes. As you continue to practise and expand your Python skills, you'll be able to create increasingly sophisticated interactive applications that engage users and provide a seamless experience. The possibilities are endless, and the concepts covered in this presentation will serve as a solid starting point for your future programming endeavours.
:::

