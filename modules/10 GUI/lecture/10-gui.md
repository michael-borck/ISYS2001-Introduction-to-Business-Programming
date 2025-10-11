---
title: "Introduction to GUIs with Python"
subtitle: "Making Weather Applications Fun!"
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
# Copyright Information

![](../../../_assets/curtin-copy-right.png)

# Acknowledgement of Country

I acknowledge the traditional custodians of the land on which I work and live,
and recognise their continuing connection to land, water and community. I pay
respect to elders past, present and emerging.

![](../../../_assets/ack_country.png)

# Today's Journey:
1. Understanding GUIs and their importance
2. Comparing text-based and GUI inputs
3. Exploring ipywidgets for Google Colab
4. Learning Tkinter for desktop applications
5. Building a simple weather app GUI
6. Brief look at advanced GUI options

- Key Takeaways:
  - Learn two main ways to create GUIs in Python
  - Understand when to use each method
  - Gain hands-on experience with real-world examples

::: {.notes}
**Aim**
This slide aims to provide an overview of the presentation's key learning objectives and set expectations for the audience.

**Context**
The "Today's Journey:" slide follows the "Acknowledgement of Country" and serves as a roadmap for the rest of the presentation. It outlines the main topics that will be covered, including an introduction to GUIs, a comparison of GUI creation methods in Python, and practical examples using ipywidgets and Tkinter.

**Key Takeaways:**
The key takeaways serve as a summary of the presentation's main learning objectives. By the end of the session, attendees should have a clear understanding of the two primary methods for creating GUIs in Python, be able to discern when to use each method based on their specific requirements, and have gained practical experience through hands-on examples.

**Learn two main ways to create GUIs in Python**
This presentation will focus on two popular methods for creating graphical user interfaces (GUIs) in Python: ipywidgets and Tkinter. ipywidgets is a library designed for use within Jupyter notebooks and Google Colab, while Tkinter is a built-in Python module that provides a standard GUI toolkit. Attendees will learn the basics of each method and explore their unique features and capabilities.

**Understand when to use each method**
Choosing the appropriate GUI creation method depends on various factors, such as the development environment, project requirements, and target audience. This presentation will discuss the strengths and limitations of both ipywidgets and Tkinter, helping attendees make informed decisions when selecting a method for their own projects. Factors such as ease of use, platform compatibility, and integration with other tools will be considered.

**Gain hands-on experience with real-world examples**
To reinforce the concepts covered in the presentation, attendees will have the opportunity to work through practical, real-world examples using both ipywidgets and Tkinter. These examples will demonstrate how to create interactive widgets, handle user input, and build functional applications. By engaging in hands-on exercises, attendees will develop a deeper understanding of each method and gain the confidence to apply their newly acquired skills to their own projects.
:::

# What is a GUI?
- A GUI (Graphical User Interface) is a visual way to interact with your program
- GUIs make your apps user-friendly and intuitive
- Examples: Weather apps on your phone or computer

::: {.notes}
**Aim**
The aim of this slide is to introduce the concept of a GUI and explain its purpose in making programs user-friendly.

**Context**
After discussing the broader topics of AI and machine learning, this slide shifts focus to the user interface aspect, specifically GUIs. It sets the stage for the following slides which will delve into using Python to create GUIs.

**A GUI (Graphical User Interface) is a visual way to interact with your program**
A GUI provides a visual and intuitive way for users to interact with a program, as opposed to a text-based command line interface. It consists of graphical elements such as windows, buttons, menus, and icons that users can manipulate with a mouse or touchscreen. GUIs abstract away the underlying complexity of the program, allowing users to focus on their tasks without needing to understand the code behind it.

**GUIs make your apps user-friendly and intuitive**
By presenting a visual interface, GUIs make applications more user-friendly and intuitive to navigate. Users can easily understand the available functions and options without needing to remember specific commands or syntax. Well-designed GUIs guide users through the application's features, making it easier to accomplish tasks and reduce the learning curve. This user-friendliness is essential for applications aimed at a broad audience, including those who may not be technically savvy.

**Examples: Weather apps on your phone or computer**
Weather applications on smartphones and computers are prime examples of how GUIs enhance user experience. These apps present information such as current weather conditions, forecasts, and radar maps in a visually appealing and easy-to-understand format. Users can quickly access the desired information by tapping on icons, selecting from menus, or interacting with sliders and buttons. The GUI design of weather apps makes it simple for users to input their location, view weather details, and customize settings without needing to understand the complex data processing happening behind the scenes.
:::

# Python and GUIs
- You'll learn two ways to create GUIs in Python:
  1. `ipywidgets` for Google Colab
  2. `tkinter` for your local computer
- Focus on these libraries to build interactive weather apps

::: {.notes}
**Aim**
This slide aims to introduce the two main libraries used for creating graphical user interfaces (GUIs) in Python, specifically in the context of building interactive weather applications.

**Context**
Having introduced the concept of GUIs in the previous slide, this slide narrows the focus to Python and the specific libraries used for GUI development. The following slides will delve into each library, providing step-by-step guidance on creating weather apps using ipywidgets and Tkinter.

**You'll learn two ways to create GUIs in Python:** In this presentation, we will explore two popular Python libraries for creating GUIs: ipywidgets and Tkinter. ipywidgets is particularly well-suited for use within Jupyter notebooks and Google Colab, while Tkinter is a standard GUI library that comes bundled with Python installations. By learning both libraries, you'll be equipped to create interactive GUIs in various environments.

**Focus on these libraries to build interactive weather apps:** Throughout the presentation, we will apply our knowledge of ipywidgets and Tkinter to build interactive weather applications. Weather apps provide an engaging and practical example of how GUIs can be used to present data and allow user interaction. By focusing on these specific libraries and the weather app example, you'll gain hands-on experience in creating functional and visually appealing GUIs in Python.
:::

# From Text to GUI: A Comparison
- Text-based Input:
  ```python
  city = input("Enter city name: ")
  print(f"Getting weather for {city}...")
  ```
- ipywidgets (for Colab):
  ```python
  import ipywidgets as widgets
  city_input = widgets.Text(description='City:')
  button = widgets.Button(description="Get Weather")
  display(city_input, button)
  ```
- Tkinter GUI (for local Python):
  ```python
  import tkinter as tk
  entry = tk.Entry(window)
  button = tk.Button(window, text="Get Weather")
  ```
- Similarities:
  - All methods take user input
  - All can trigger actions based on input
- Differences:
  - Text-based is simplest to code, but least interactive
  - ipywidgets works in Colab, great for quick prototypes
  - Tkinter allows for standalone apps, most flexible

::: {.notes}
**Aim**
This slide aims to compare different methods of getting user input in Python: text-based input, ipywidgets in Google Colab, and Tkinter for local Python apps.

**Context**
Having introduced GUIs and how Python can be used to create them, this slide delves into the specifics of three approaches. It sets the stage for the following slides, which will provide hands-on examples of using ipywidgets and Tkinter to build interactive applications.

**Text-based Input:**
Text-based input is the simplest way to get user input in Python. It involves using the built-in `input()` function, which prompts the user to enter text in the console. While straightforward to implement, text-based input provides a basic user experience and is less interactive compared to other methods.

**ipywidgets (for Colab):**
ipywidgets is a library that allows you to create interactive widgets in Jupyter notebooks, including Google Colab. With ipywidgets, you can add GUI elements like buttons, text boxes, and sliders directly in the notebook cells. This makes it convenient for creating quick prototypes and interactive demonstrations without the need for a separate GUI framework.

**Tkinter GUI (for local Python):**
Tkinter is a standard GUI library that comes bundled with Python. It provides a wide range of widgets and tools for building standalone desktop applications with graphical user interfaces. Tkinter offers more flexibility and customization options compared to ipywidgets, allowing you to create fully-featured applications that can be run locally on a user's machine.

**Similarities:**
All three methods—text-based input, ipywidgets, and Tkinter—serve the purpose of receiving user input in a Python program. They allow you to prompt the user for information or actions, which can then be processed by your code. Regardless of the method used, the fundamental concept of capturing and responding to user input remains the same.

**All methods take user input**
Whether it's through the console with text-based input, interactive widgets in ipywidgets, or GUI elements in Tkinter, all three approaches provide a way for users to enter data or trigger actions. This user input can be in the form of text, button clicks, slider movements, or other interactions, depending on the chosen method.

**All can trigger actions based on input**
Once the user provides input, your Python code can respond accordingly. This could involve performing calculations, updating displays, making API requests, or any other desired actions. The specific actions triggered by user input will depend on the logic you implement in your program, regardless of the input method used.

**Differences:**
While all three methods serve the purpose of getting user input, they differ in terms of their ease of implementation, level of interactivity, and the contexts in which they are typically used. Text-based input is the simplest but least interactive, ipywidgets is well-suited for quick prototypes in Colab, and Tkinter provides the most flexibility for building standalone applications.

**Text-based is simplest to code, but least interactive**
Text-based input using the `input()` function is the most straightforward to implement in Python. It requires minimal setup and can be added to your code with just a few lines. However, it provides a command-line interface, which may not be as user-friendly or visually appealing as graphical interfaces. Users interact by typing in the console, which can be less intuitive compared to clicking buttons or manipulating widgets.

**ipywidgets works in Colab, great for quick prototypes**
ipywidgets integrates seamlessly with Jupyter notebooks, including Google Colab. This makes it an excellent choice for creating interactive prototypes, demonstrations, or data exploration tools directly within the notebook environment. With ipywidgets, you can quickly add GUI elements to your code cells and create interactive experiences without the need for a separate GUI framework. However, ipywidgets is primarily designed for use within notebooks and may not be suitable for building standalone applications.

**Tkinter allows for standalone apps, most flexible**
Tkinter is a powerful and flexible GUI library that allows you to create standalone desktop applications with Python. It provides a wide range of widgets, such as buttons, text boxes, labels, and menus, which can be arranged and customized to build professional-looking interfaces. Tkinter apps can be run independently on a user's machine, making it ideal for distributing your software. However, building Tkinter GUIs requires more code and setup compared to ipywidgets or text-based input.
:::

# Python and GUIs
- You'll learn two ways to create GUIs in Python:
  1. `ipywidgets` for Google Colab
  2. `tkinter` for your local computer
- Focus on these libraries to build interactive weather apps
- GUIs build upon your knowledge of text-based inputs, adding visual elements
- Each method has its strengths, choosing depends on your needs

::: {.notes}
**Aim**
The purpose of this slide is to introduce the two main libraries for creating graphical user interfaces (GUIs) in Python and highlight their relevance to building interactive weather applications.

**Context**
Having defined GUIs in the previous slide, this slide narrows the focus to Python-specific GUI tools. It sets the stage for the upcoming content, which will compare text-based and GUI approaches, and provide hands-on examples using ipywidgets and Tkinter.

**You'll learn two ways to create GUIs in Python:**
This presentation will cover two popular Python libraries for building GUIs: ipywidgets and Tkinter. ipywidgets is a library for creating interactive widgets in Jupyter notebooks, while Tkinter is a standard GUI package that comes bundled with Python. By learning these two approaches, you'll be equipped to create GUIs in various contexts.

**Focus on these libraries to build interactive weather apps**
Throughout this presentation, we'll apply our knowledge of ipywidgets and Tkinter to create interactive weather applications. Weather apps provide a practical and engaging context for learning GUI development, as they involve user input, data retrieval, and dynamic displays. By building weather apps, you'll gain hands-on experience with GUI concepts and techniques.

**GUIs build upon your knowledge of text-based inputs, adding visual elements**
Creating GUIs involves building upon the fundamentals of Python programming, such as handling user input and displaying output. However, GUIs introduce visual elements like buttons, text boxes, and labels, which enhance the user experience. As you learn about GUIs, you'll see how they extend the capabilities of text-based programs and provide a more intuitive interface for users.

**Each method has its strengths, choosing depends on your needs**
Both ipywidgets and Tkinter have their own strengths and use cases. ipywidgets is particularly well-suited for creating interactive widgets within Jupyter notebooks, making it ideal for data exploration and visualization. On the other hand, Tkinter is a versatile library that allows you to create standalone GUI applications that can be run independently of Jupyter. The choice between the two depends on your specific requirements and the context in which you're developing your application.
:::

# Getting Started with ipywidgets in Google Colab
- To use ipywidgets, run this in a Colab cell:
  ```python
  !pip install ipywidgets
  ```
- Colab automatically supports ipywidgets after installation

::: {.notes}
**Aim**
This slide aims to provide instructions on setting up ipywidgets in Google Colab for creating interactive GUIs in Python.

**Context**
After introducing the concept of GUIs and their importance in Python programming, this slide focuses on the practical steps to start using ipywidgets in Google Colab. The following slides will demonstrate how to create and interact with various ipywidgets components.

**To use ipywidgets, run this in a Colab cell:** To begin using ipywidgets in Google Colab, you need to execute a specific command in a Colab cell. This command installs the necessary dependencies and sets up the environment for creating interactive widgets. By running this command, you ensure that your Colab notebook is ready to work with ipywidgets.

**Colab automatically supports ipywidgets after installation** Once you have run the installation command, Google Colab automatically supports ipywidgets without requiring any further configuration. This means that you can immediately start creating and using interactive widgets in your Colab notebook. Colab takes care of the necessary setup, allowing you to focus on building your GUI components.
:::

# Your First ipywidget
- Create a simple text input for a weather app:
  ```python
  import ipywidgets as widgets
  city_input = widgets.Text(description='City:', placeholder='Enter city name')
  display(city_input)
  ```
- Try typing a city name in the input box!

::: {.notes}
**Aim**
The purpose of this slide is to demonstrate how to create a simple text input widget using ipywidgets and show its functionality in the context of a weather app.

**Context**
This slide follows an introduction to ipywidgets in Google Colab, providing a practical example of widget usage. It precedes slides that cover adding a button and making widgets work together to create a complete weather app using ipywidgets.

**Create a simple text input for a weather app:**
To create a text input widget, use the `widgets.Text` class from the ipywidgets library. This class allows users to enter and edit text in a single-line input field. By setting the `placeholder` parameter, you can provide a hint or example of the expected input, such as "Enter a city name". The text input widget can be displayed using the `display` function from IPython.

**Try typing a city name in the input box!**
Encourage your audience to interact with the text input widget by typing a city name into the input box. This hands-on experience helps them understand the functionality of the widget and its role in the weather app. As they type, explain that the entered city name can be accessed programmatically through the `value` attribute of the text input widget, which will be used later to fetch weather data for the specified city.
:::

# Adding a Button
- Create a button to submit your weather query:
  ```python
  button = widgets.Button(description="Get Weather")
  display(button)
  ```
- The button appears, but doesn't do anything yet

::: {.notes}
**Aim**
This slide aims to introduce the process of adding a button to the weather app GUI, which will later be used to submit the user's weather query.

**Context**
Having introduced the concept of GUIs and the basics of ipywidgets, this slide focuses on adding a specific widget - a button - to the weather app. The following slides will cover making the button functional and integrating it with other widgets.

**Create a button to submit your weather query:**
To allow users to interact with the weather app, we need to provide a way for them to submit their weather queries. A button is a common and intuitive way to do this. By creating a button widget, we give users a clear point of interaction within the GUI. The code for adding a button will be demonstrated, showing how to instantiate the widget and specify its properties such as the label text.

**The button appears, but doesn't do anything yet:**
At this stage, the button will be visible in the GUI, but it won't have any functionality associated with it. This is because we haven't yet defined what should happen when the button is clicked. The presenter will emphasise that this is normal and expected at this point in the development process. The next steps will involve linking the button to a function that will be executed when the button is clicked, allowing it to actually perform an action and interact with other parts of the program.
:::

# Making Widgets Work Together
- Combine input and button to display weather info:
  ```python
  output = widgets.Output()
  
  def on_button_click(b):
      with output:
          print(f"Getting weather for {city_input.value}...")
  
  button.on_click(on_button_click)
  display(city_input, button, output)
  ```
- Now you can enter a city and click the button!

::: {.notes}
**Aim**
This slide demonstrates how to combine ipywidgets to create interactive functionality, allowing users to enter a city and retrieve weather information by clicking a button.

**Context**
Having introduced ipywidgets and shown how to create individual widgets like text inputs and buttons, this slide builds on that knowledge by illustrating how to make widgets work together. This sets the stage for the subsequent slide, which presents a complete weather app using ipywidgets.

**Combine input and button to display weather info:**
By connecting an input widget (for entering a city) and a button widget, we can create an interactive experience where the user provides input and triggers an action. When the button is clicked, the value from the input widget is retrieved and used to fetch the corresponding weather information. This interaction between widgets is a key concept in building functional GUIs.

**Now you can enter a city and click the button!**
With the input and button widgets combined, users can now interact with the app more intuitively. They simply need to type the name of a city into the input field and click the button to initiate the weather retrieval process. This interactive flow makes the app more user-friendly and engaging, as users can easily specify their desired location and obtain weather information with a single click.
:::

# Complete Weather App with ipywidgets
```python
import ipywidgets as widgets

city_input = widgets.Text(description='City:', placeholder='Enter city name')
button = widgets.Button(description="Get Weather")
output = widgets.Output()

def get_weather(city):
    # In a real app, you'd fetch actual weather data here
    return f"It's sunny and 22°C in {city}!"

def on_button_click(b):
    with output:
        output.clear_output()
        print(get_weather(city_input.value))

button.on_click(on_button_click)
display(city_input, button, output)
```

::: {.notes}
**Aim**
Showcase a complete weather app built using ipywidgets, demonstrating the practical application of the concepts covered in the presentation.

**Context**
After introducing ipywidgets and guiding the audience through the process of creating simple widgets and making them interact, this slide presents a fully functional weather app. It serves as a culmination of the ipywidgets section before transitioning to Tkinter and discussing when to use each toolkit.
:::

# Moving Beyond Google Colab
- ipywidgets works great in Colab, but what about on your own computer?
- Enter `tkinter`: Python's built-in GUI library for local app

::: {.notes}
**Aim**
This slide aims to introduce tkinter as a solution for creating GUI applications locally, beyond the Google Colab environment.

**Context**
After exploring ipywidgets for building interactive GUIs within Google Colab, this slide transitions to discussing GUI development on a local computer. It sets the stage for introducing tkinter, Python's built-in GUI library, which will be covered in the subsequent slides.

**ipywidgets works great in Colab, but what about on your own computer?**
While ipywidgets is an excellent library for creating interactive widgets and GUIs within the Google Colab environment, it may not be the most suitable choice when developing GUI applications on your local machine. Google Colab is a web-based platform, and ipywidgets is designed to work seamlessly within Jupyter notebooks. However, when it comes to building standalone GUI applications that can run on your computer, you need a library that is compatible with the local environment.

**Enter `tkinter`: Python's built-in GUI library for local app**
This is where tkinter comes into play. Tkinter is Python's standard GUI library that comes built-in with the Python installation. It provides a set of tools and widgets for creating graphical user interfaces that can run as standalone applications on your local computer. Tkinter offers a wide range of GUI elements such as windows, buttons, labels, text boxes, and more, allowing you to build feature-rich and interactive applications. With tkinter, you can create GUIs that have a native look and feel, integrating seamlessly with the operating system. In the upcoming slides, we will explore tkinter in more detail and learn how to create GUI applications using this powerful library.
:::

# Why Tkinter Doesn't Work on Google Colab
- Tkinter requires a local display to show windows
- Google Colab runs in the cloud without a graphical interface
- Colab is designed for web-based interactions, not desktop applications
- That's why we use ipywidgets in Colab - it's web-friendly!
- To use Tkinter, you'll need to run Python on your own computer

::: {.notes}
**Aim**
This slide aims to explain why Tkinter, a popular Python GUI toolkit, is not compatible with Google Colab, a web-based Python environment.

**Context**
After introducing ipywidgets as a GUI solution for Google Colab, this slide addresses a potential question learners might have: why not use Tkinter, a well-known Python GUI toolkit, in Colab? The slide then transitions to introducing Tkinter for use on learners' own computers.

**Tkinter requires a local display to show windows**
Tkinter is designed to create desktop applications with graphical user interfaces. It requires a local display server to render the windows and widgets of the application. Without a local display, Tkinter cannot function properly.

**Google Colab runs in the cloud without a graphical interface**
Google Colab is a cloud-based Jupyter notebook environment. It runs on remote servers and provides access through a web browser. Colab does not have a local graphical display server, which is necessary for Tkinter to operate.

**Colab is designed for web-based interactions, not desktop applications**
The primary purpose of Google Colab is to facilitate interactive development, data analysis, and machine learning in a web-based environment. It is optimised for running code, displaying outputs, and sharing results through the browser, rather than creating standalone desktop applications.

**That's why we use ipywidgets in Colab - it's web-friendly!**
Ipywidgets is a library specifically designed for creating interactive widgets in Jupyter notebooks, including Google Colab. It leverages the web-based nature of Colab and allows you to build interactive GUIs that can be displayed and controlled directly within the notebook.

**To use Tkinter, you'll need to run Python on your own computer**
If you want to develop desktop applications using Tkinter, you'll need to run Python locally on your own computer. This ensures that you have access to the necessary display server and can create and interact with Tkinter windows and widgets directly on your machine.
:::

# Introduction to Tkinter
- Tkinter is Python's built-in GUI library
- It comes pre-installed with Python on your computer
- Tkinter allows you to create standalone desktop applications
- You'll run these apps directly on your computer, not in a browser

::: {.notes}
**Aim**
This slide introduces Tkinter, Python's built-in GUI library, and highlights its key features and capabilities for creating standalone desktop applications.

**Context**
After discussing GUIs in general and exploring ipywidgets in Google Colab, the presentation now shifts focus to Tkinter, a powerful library for creating desktop applications. The following slides will provide a step-by-step guide on using Tkinter to build a weather app.

**Tkinter is Python's built-in GUI library**
Tkinter comes as part of the standard Python distribution, making it readily accessible to developers. As a built-in library, Tkinter is well-documented and has a large community of users, providing ample resources and support for those learning to create GUIs with Python.

**It comes pre-installed with Python on your computer**
Since Tkinter is included with Python, there's no need to install additional packages or libraries. This makes it convenient for developers to start building GUIs without the hassle of managing external dependencies, ensuring a smooth and efficient development process.

**Tkinter allows you to create standalone desktop applications**
With Tkinter, developers can create fully-functional desktop applications that run independently on a user's computer. These applications have access to system resources and can perform a wide range of tasks, from simple utilities to complex software solutions.

**You'll run these apps directly on your computer, not in a browser**
Unlike web-based applications that run in a browser, Tkinter applications are executed directly on the user's computer. This allows for better performance, offline functionality, and direct access to system resources, providing a native and seamless user experience.
:::

# Your First Tkinter Window
- Create a basic window with tkinter:
  ```python
  import tkinter as tk
  
  window = tk.Tk()
  window.title("My Weather App")
  window.mainloop()
  ```
- Save this as `weather_app.py` and run it with `python weather_app.py`

::: {.notes}
**Aim**
The aim of this slide is to guide the audience through creating their first basic window using the Tkinter library in Python.

**Context**
After discussing the limitations of using ipywidgets in Google Colab, the presentation introduces Tkinter as an alternative for building GUI applications. This slide provides a practical example of how to create a simple Tkinter window, setting the stage for the following slides that will expand on adding widgets and functionality to the application.

**Create a basic window with tkinter:**
To create a basic window using Tkinter, you need to import the library and create an instance of the Tk class, which represents the main window of your application. You can set the title of the window using the `title()` method and specify its dimensions using the `geometry()` method. Finally, you need to call the `mainloop()` method to display the window and start the event loop that handles user interactions.

**Save this as `weather_app.py` and run it with `python weather_app.py`**
After writing the code to create a basic Tkinter window, save the file with a descriptive name, such as `weather_app.py`. To run the application, open a terminal or command prompt, navigate to the directory where you saved the file, and execute the command `python weather_app.py`. This will launch your Tkinter application, displaying the window you created.
:::

# Adding Widgets to Your Tkinter Window
- Let's add a label and text entry for the city:
  ```python
  import tkinter as tk
  
  window = tk.Tk()
  window.title("My Weather App")
  
  label = tk.Label(window, text="Enter City:")
  label.pack()
  
  entry = tk.Entry(window)
  entry.pack()
  
  window.mainloop()
  ```

::: {.notes}
**Aim**
This slide aims to demonstrate how to add a label and text entry widget to a Tkinter window to allow the user to input a city name.

**Context**
Having introduced Tkinter and shown how to create a basic window, the presentation now progresses to adding interactive elements. This slide builds upon the previous one about creating a Tkinter window and leads into the next slides on creating buttons and displaying results.

**Let's add a label and text entry for the city:**
To allow the user to input a city name, we need to add two widgets to our Tkinter window: a label and a text entry. The label provides a text description of what the user should enter, while the text entry is an input field where the user can type the city name. These widgets are positioned within the window using a geometry manager, such as pack, grid, or place. By adding these interactive elements, we make our application more functional and user-friendly.
:::

# Creating a Button in Tkinter
- Add a button to get the weather:
  ```python
  button = tk.Button(window, text="Get Weather")
  button.pack()
  ```
- Add this code before `window.mainloop()`

::: {.notes}
**Aim**
This slide aims to demonstrate how to add a button to a Tkinter window and explain where the code for creating the button should be placed.

**Context**
Having introduced Tkinter and shown how to create a basic window, the presentation now progresses to adding interactive elements to the window. This slide focuses on adding a button, which is a fundamental interactive component in most GUI applications. The subsequent slides will cover displaying results and making the app functional, building upon the concepts introduced here.

**Add a button to get the weather:** 
To add a button to your Tkinter window, you can use the `Button` widget. The button is created with the `Button()` constructor, which takes the window as its first argument. You can specify the text to display on the button using the `text` parameter. For example, to create a button that says "Get Weather", you would use:

```python
get_weather_button = Button(window, text="Get Weather")
```

**Add this code before `window.mainloop()`**
It's important to place the code for creating and configuring the button before the `window.mainloop()` call. The `mainloop()` function starts the event loop and displays the window, so any code that modifies the window should come before it. If you add the button code after `mainloop()`, the button will not appear in the window. For example:

```python
window = Tk()
# ...
get_weather_button = Button(window, text="Get Weather")
window.mainloop()
```
:::

# Displaying Results in Tkinter
- Create a label to show the weather results:
  ```python
  result_label = tk.Label(window, text="")
  result_label.pack()
  ```
- Add this code before `window.mainloop()`

::: {.notes}
**Aim**
This slide aims to demonstrate how to display the results of the weather app in a Tkinter window.

**Context**
After creating the basic structure of the Tkinter window and adding widgets such as buttons, the next step is to display the results of the weather app. This slide builds upon the previous slides that introduced Tkinter and showed how to create a window and add widgets.

**Create a label to show the weather results:**
To display the weather results in the Tkinter window, you need to create a label widget. The label will be used to show the text output from the weather app. You can create a label using the `Label()` function from Tkinter, specifying the parent window and the initial text to display. For example: `result_label = Label(window, text="")`.

**Add this code before `window.mainloop()`**
It's important to add the code for creating and positioning the label before the `window.mainloop()` line in your Tkinter app. The `mainloop()` function starts the event loop and displays the window, so any widgets you want to appear in the window must be created and positioned before calling `mainloop()`. Make sure to place the label creation code in the appropriate location to ensure it appears in the window when the app is run.
:::

# Making Your Tkinter App Functional
- Let's add some action to the button:
  ```python
  def get_weather():
      city = entry.get()
      # In a real app, you'd fetch actual weather data here
      weather = f"It's sunny and 22°C in {city}!"
      result_label.config(text=weather)
  
  button.config(command=get_weather)
  ```
- Add this code before `window.mainloop()`

::: {.notes}
**Aim**
This slide aims to demonstrate how to make the button in the Tkinter app functional by adding code that responds to user interactions.

**Context**
Having created a basic Tkinter window with a button in the previous slides, this slide builds on that foundation by showing how to make the button actually do something when clicked. This is a crucial step in creating a fully functional GUI application with Tkinter.

**Let's add some action to the button:**
Now that we have a button displayed in our Tkinter window, it's time to make it interactive. By default, the button doesn't do anything when clicked. To change this, we need to define a function that will be called whenever the button is pressed. This function can contain any code we want to execute when the button is clicked, such as updating labels, performing calculations, or opening new windows.

**Add this code before `window.mainloop()`**
To associate a function with a button click event, we need to modify the button creation code. Before calling `window.mainloop()`, which starts the main event loop of the Tkinter application, we'll add a command parameter to the button constructor. This parameter takes the name of the function (without parentheses) that should be called when the button is clicked. By placing this code before `window.mainloop()`, we ensure that the button's functionality is defined before the application starts running.
:::

# Complete Tkinter Weather App
```python
import tkinter as tk

def get_weather():
    city = entry.get()
    # In a real app, you'd fetch actual weather data here
    weather = f"It's sunny and 22°C in {city}!"
    result_label.config(text=weather)

window = tk.Tk()
window.title("My Weather App")

label = tk.Label(window, text="Enter City:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Get Weather", command=get_weather)
button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
```

::: {.notes}
**Aim**
The aim of this slide is to showcase the final result of the Tkinter weather app project.

**Context**
This slide serves as the culmination of the Tkinter section of the presentation. It follows the progression from introducing Tkinter, creating a window, adding widgets, making the app functional, and finally arriving at the completed weather app. The next slide discusses running the Tkinter app, and subsequent slides compare ipywidgets and Tkinter, and explore the broader world of GUIs.
:::

# Running Your Tkinter App
- Save the complete code as `weather_app.py`
- Open your terminal or command prompt
- Navigate to the folder containing your script
- Run the command: `python weather_app.py`
- Your weather app will appear in a new window!

::: {.notes}
**Aim**
This slide aims to guide the audience through the process of running their completed Tkinter weather application.

**Context**
After introducing Tkinter and walking through the creation of a functional weather app, this slide provides the final steps to save and run the application. It prepares the audience to use their new skills independently and see their app in action.

**Save the complete code as `weather_app.py`** 
Once you have finished coding your Tkinter weather app, save the entire script in a file named `weather_app.py`. This file will contain all the necessary code to create the GUI and fetch weather data. Choose a location on your computer that you can easily navigate to using the command line.

**Open your terminal or command prompt** 
To run your Tkinter app, you'll need to use the command line. On macOS, open the Terminal application. For Windows users, open the Command Prompt. If you're using Linux, open your preferred terminal emulator. Familiarise yourself with the basic commands for navigating through directories in your command line interface.

**Navigate to the folder containing your script** 
Using the `cd` command followed by the appropriate file path, navigate to the directory where you saved your `weather_app.py` file. For example, if your file is saved in a folder called `tkinter_projects` on your desktop, you would type `cd Desktop/tkinter_projects` and press Enter to move into that directory.

**Run the command: `python weather_app.py`** 
Once you're in the correct directory, type `python weather_app.py` and press Enter to execute your script. This command tells your computer to run the Python interpreter and execute the code contained in the `weather_app.py` file. Make sure you have Python installed on your system and accessible from the command line.

**Your weather app will appear in a new window!** 
After running the command, your Tkinter weather app will launch in a new window. You'll see the GUI elements you created, such as the input field, button, and label for displaying the weather information. Interact with your app by entering a city name and clicking the button to fetch the current weather data. Celebrate your success in creating a functional GUI application using Python and Tkinter!
:::

# When to Use Each
- Use ipywidgets when:
  - Working in Google Colab or Jupyter Notebooks
  - Quickly prototyping ideas
  - Sharing interactive code online
- Use tkinter when:
  - Creating standalone desktop applications
  - Building apps that don't require an internet connection
  - Developing more complex GUI structures

::: {.notes}
**Aim**
The aim of this slide is to provide guidance on when to choose ipywidgets versus tkinter for building GUI applications in Python.

**Context**
Having introduced both ipywidgets and tkinter, this slide helps learners understand the strengths and appropriate use cases for each library. It sets the stage for the upcoming slides that discuss expanding GUI skills and exploring the broader world of GUI development.

**Use ipywidgets when:**
ipywidgets is the ideal choice when working within Google Colab or Jupyter Notebooks. Its seamless integration allows for quick prototyping of ideas and interactive exploration of code. The ability to easily share ipywidget-based apps online makes it a great option for collaborating with others or showcasing your work.

**Working in Google Colab or Jupyter Notebooks**
Google Colab and Jupyter Notebooks provide a browser-based environment for developing and running Python code. ipywidgets is built to work smoothly within these platforms, allowing you to create interactive widgets directly in your notebook cells. This integration makes it convenient to experiment with GUI elements alongside your data analysis or machine learning code.

**Quickly prototyping ideas**
ipywidgets enables rapid prototyping of interactive features. With just a few lines of code, you can create sliders, buttons, text inputs, and other widgets to control and visualise your Python scripts. This speed of development is particularly useful when testing out new ideas or iterating on existing ones.

**Sharing interactive code online**
One of the key advantages of ipywidgets is the ability to share your interactive code online. By hosting your Jupyter Notebook on a platform like GitHub or Binder, others can access and run your ipywidget-based apps through their web browser. This ease of sharing facilitates collaboration and allows you to showcase your work to a wider audience.

**Use tkinter when:**
tkinter is the go-to choice when creating standalone desktop applications that don't rely on an internet connection. It provides a wide range of widgets and allows for the development of more complex GUI structures compared to ipywidgets. If your goal is to build a feature-rich, offline-capable Python app, tkinter is the way to go.

**Creating standalone desktop applications**
tkinter is designed for building standalone desktop applications. Unlike ipywidgets, which are tied to the browser-based environment of Google Colab or Jupyter Notebooks, tkinter apps can be packaged and distributed as executable files. This allows users to run your application on their local machines without the need for a web browser or internet connection.

**Building apps that don't require an internet connection**
Since tkinter apps are standalone, they can function fully offline. This is particularly useful when developing applications for environments with limited or no internet connectivity. With tkinter, you can create self-contained Python programs that run independently of web-based resources.

**Developing more complex GUI structures**
tkinter offers a wider range of widgets and layout options compared to ipywidgets. This flexibility allows for the creation of more intricate and feature-rich GUI structures. From multi-window interfaces to custom dialog boxes and menus, tkinter provides the tools to build sophisticated desktop applications that go beyond the capabilities of ipywidgets.
:::

# Expanding Your GUI Skills
- Next steps to explore:
  - Learn about layout management in tkinter
  - Explore styling and theming your GUI
  - Try other GUI libraries like PyQt or Kivy
  - Integrate real weather APIs into your app

::: {.notes}
**Aim**
The aim of this slide is to provide the audience with guidance on how they can further develop their GUI skills beyond the basics covered in the presentation.

**Context**
Having demonstrated how to create functional weather apps using both ipywidgets in Google Colab and Tkinter, this slide serves as a bridge to more advanced GUI topics. It encourages the audience to explore these areas independently to continue their learning journey.

**Next steps to explore:**
This bullet point introduces the main theme of the slide, which is to provide the audience with specific areas they can investigate to expand their GUI skills.

**Learn about layout management in tkinter**
Layout management is a critical aspect of creating professional-looking GUIs. By learning how to effectively use geometry managers like pack, grid, and place in Tkinter, the audience can create well-organised and responsive user interfaces that adapt to different window sizes and resolutions.

**Explore styling and theming your GUI**
Styling and theming can greatly enhance the visual appeal and user experience of a GUI application. The audience should explore how to customise colours, fonts, and other visual properties using Tkinter's styling options or by leveraging external libraries like ttk (Themed Tkinter) for a more modern and polished look.

**Try other GUI libraries like PyQt or Kivy**
While Tkinter is a great starting point for GUI development in Python, there are many other powerful libraries worth exploring. PyQt is a comprehensive set of Python bindings for the Qt framework, offering a wide range of widgets and tools for building feature-rich desktop applications. Kivy, on the other hand, is an open-source library for developing cross-platform applications with a focus on touch-based interfaces and mobile devices.

**Integrate real weather APIs into your app**
To make the weather app examples more practical and useful, the audience should consider integrating real-time weather data from external APIs. Popular weather APIs like OpenWeatherMap or WeatherAPI.com offer free and paid plans for accessing current weather conditions, forecasts, and other meteorological data. By learning how to make HTTP requests and parse JSON responses, the audience can create dynamic and informative weather applications.
:::

# The Broader World of GUIs
- We've focused on ipywidgets and Tkinter, but there's more to explore:
- Web Interfaces:
  - Frameworks like Flask or Django let you create web-based GUIs
  - Example: A weather website where users enter their city
- Mobile Apps:
  - Tools like Kivy or BeeWare can create Python-based mobile apps
  - Platforms like Anvil let you build web apps that work on phones
- Remember:
  - Start with the basics (ipywidgets, Tkinter) to learn core concepts
  - These advanced options build on the fundamentals you're learning now

::: {.notes}
**Aim**
This slide aims to provide a glimpse into the broader world of GUI development beyond ipywidgets and Tkinter, introducing web interfaces and mobile app development.

**Context**
Having covered the basics of GUI development with ipywidgets and Tkinter, this slide expands students' horizons by touching on more advanced GUI options. It serves as a bridge between the foundational concepts already covered and the potential for further exploration in the field.

**We've focused on ipywidgets and Tkinter, but there's more to explore:** The world of GUI development extends far beyond the scope of this presentation. While ipywidgets and Tkinter provide a solid foundation, there are numerous other tools and frameworks available for creating graphical user interfaces across different platforms.

**Web Interfaces:** Web-based GUIs offer the advantage of being accessible through a web browser, making them platform-independent. Frameworks such as Flask and Django, which are built on top of Python, enable developers to create interactive web interfaces. These frameworks handle the backend logic and provide tools for rendering HTML templates, handling user input, and managing data.

**Example: A weather website where users enter their city** To illustrate the concept of a web-based GUI, consider a weather website where users can input their city name to retrieve current weather information. This involves creating a user-friendly interface with input fields and buttons, handling user input on the backend, making API calls to retrieve weather data, and dynamically updating the webpage with the retrieved information.

**Mobile Apps:** Python can also be used to develop mobile applications for platforms like iOS and Android. Tools such as Kivy and BeeWare provide frameworks for building cross-platform mobile apps using Python. These frameworks abstract away platform-specific details and allow developers to write code once and deploy it on multiple mobile platforms.

**Platforms like Anvil let you build web apps that work on phones** In addition to traditional mobile app development, platforms like Anvil offer a simplified approach to creating mobile-friendly web applications. Anvil provides a drag-and-drop interface for building web apps visually, and the resulting apps are responsive and work seamlessly on mobile devices.

**Remember:** As you explore more advanced GUI options, it's crucial to remember that the concepts and principles you've learned with ipywidgets and Tkinter form the foundation of GUI development. Understanding event handling, widget placement, and data flow between components is essential regardless of the specific framework or tool you choose.

**Start with the basics (ipywidgets, Tkinter) to learn core concepts** Mastering the fundamentals through hands-on experience with ipywidgets and Tkinter will equip you with the necessary problem-solving skills and logical thinking required for tackling more complex GUI projects. These basic tools serve as stepping stones, allowing you to grasp the core concepts before diving into more advanced frameworks.

**These advanced options build on the fundamentals you're learning now** As you progress in your GUI development journey, you'll find that the advanced options mentioned, such as web frameworks and mobile app development tools, build upon the same principles you're learning now. The skills you acquire working with ipywidgets and Tkinter, such as layout management, event handling, and data binding, will be applicable and transferable to these more advanced contexts.
:::

# Wrap-up and Q&A
- We've covered a lot:
  1. Text-based inputs
  2. ipywidgets for interactive notebooks
  3. Tkinter for desktop applications
  4. Brief intro to web and mobile possibilities
- Focus on mastering ipywidgets and Tkinter first
- The skills you're learning apply to more advanced frameworks too
- Any questions about what we've covered or the broader world of GUIs?

::: {.notes}
**Aim**
The purpose of this slide is to summarise the key points covered in the presentation and open the floor for questions from the audience.

**Context**
This is the final slide of the presentation, following slides that have introduced GUIs, demonstrated how to create GUIs using ipywidgets and Tkinter, and explored the broader world of GUI frameworks. It aims to reinforce the main takeaways and provide an opportunity for clarification and discussion.

**We've covered a lot:**
Throughout this presentation, we've introduced the concept of GUIs and explored how to create them using Python. We started with ipywidgets in Google Colab, learning how to create widgets, make them interact, and build a complete weather app. We then moved on to Tkinter, covering the basics of creating windows, adding widgets, and building a functional weather app. Finally, we discussed when to use each framework and touched on the broader world of GUIs.

**Focus on mastering ipywidgets and Tkinter first**
While there are many GUI frameworks available, it's important to start with the basics. ipywidgets and Tkinter are excellent starting points, as they provide a solid foundation in GUI development. By mastering these frameworks, you'll gain the skills and understanding needed to work with more advanced options in the future. Don't feel pressured to learn everything at once; take your time to become proficient with these tools first.

**The skills you're learning apply to more advanced frameworks too**
The concepts and techniques you've learned while working with ipywidgets and Tkinter are transferable to other GUI frameworks. The process of creating widgets, laying out your interface, and handling user interactions is similar across many frameworks. As you explore more advanced options, you'll find that the skills you've developed will serve you well. Keep practicing and building projects to solidify your understanding.

**Any questions about what we've covered or the broader world of GUIs?**
Now is your opportunity to ask any questions you may have about the topics we've covered or GUI development in general. Whether you need clarification on a specific concept, want to know more about a particular framework, or are curious about best practices, feel free to ask. Remember, there are no silly questions, and your fellow learners may benefit from the discussion as well. Don't hesitate to speak up and seek the information you need to further your understanding of GUIs.
:::

