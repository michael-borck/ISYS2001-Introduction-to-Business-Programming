---
title: "Building a Simple Weather App GUI in Google Colab with ipywidgets"
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

### **Introduction:**

Graphical User Interfaces (GUIs) allow users to interact with applications
visually, providing a more intuitive experience compared to text-based
interfaces. In this worksheet, we will explore how to build a simple interactive
weather app using Python’s `ipywidgets` library in Google Colab. This app will
allow users to input a city name and display simulated weather information. This
activity reinforces basic GUI concepts, while also giving you a practical
introduction to building interactive widgets in a Jupyter/Colab environment.

### **Objectives:**
By the end of this worksheet, you will be able to:

1. Understand the basic concepts of GUIs.
2. Build and display simple interactive widgets using `ipywidgets` in Google Colab.
3. Create input fields, buttons, and labels to simulate a weather application.
4. Write Python code to handle user inputs and display output based on these inputs.
5. Create a basic visualisation of a 5-day temperature trend using `matplotlib`.
6. Combine different GUI elements to create a cohesive application.


---

### **Frequently Save Your Work to GitHub**

As you progress through this worksheet, it's important to frequently save your
work by pushing the latest version of your notebook to GitHub. This helps
prevent data loss and allows you to track changes over time. Follow these steps
to save your notebook directly from Google Colab to GitHub:

1. **Save a Copy to GitHub**:
   - In your Google Colab notebook, go to the **File** menu.
   - Select **Save a copy in GitHub** from the dropdown menu.

2. **Enter a Commit Message**:
   - A popup box will appear asking for a commit message.
   - Type a meaningful commit message that describes your changes, for example:
     - *"Added weather fetching function"*
     - *"Created input widget for city name"*
     - *"Fixed bug in city input handling"*

3. **Select the Target Repository**:
   - In the same popup box, make sure you select the correct GitHub repository where you want to save the file.
   - You can also choose the branch if you're working with multiple branches.

4. **Click 'OK'**:
   - Once you’ve entered your commit message and selected the repository, click **OK** to save your notebook to GitHub.

By frequently saving your work using this method, you ensure that your progress
is well-documented and securely stored in your GitHub repository. This also
allows you to easily share your work and track changes over time.

---

### **Step-by-Step Guide: Creating the Weather App in ipywidgets**

#### **Step 1: Import Necessary Libraries**
Before starting, you need to import the `ipywidgets` library and other necessary modules. These libraries will allow us to create interactive elements in our app.

```python
import ipywidgets as widgets
from IPython.display import display
```

#### **Step 2: Create the Input Widget for City Name**
The first step in our weather app is to allow the user to input a city name. We’ll use the `Text` widget to create an input field.

```python
city_input = widgets.Text(
    placeholder='Enter city name',
    description='City:',
    disabled=False
)
```

- The `placeholder` attribute shows text inside the input box when it’s empty.
- The `description` attribute adds a label next to the input field.

#### **Step 3: Add a Button to Fetch Weather**
Now, let’s create a button that users will click to "fetch" the weather data. We use the `Button` widget for this.

```python
fetch_button = widgets.Button(
    description='Get Weather',
    disabled=False,
    button_style='primary'  # Optional styling
)
```

- The `description` attribute specifies the text displayed on the button.
- The `button_style` can be used to add some visual flair (optional).

#### **Step 4: Create a Label to Display Weather Information**
Next, we need a place to display the weather results. A `Label` widget is perfect for this task.

```python
weather_output = widgets.Label(value="")
```

- The `value` attribute initialises the label’s text, which we’ll update when the button is clicked.

#### **Step 5: Write the Function to Simulate Fetching Weather**
In this step, we create the logic that will simulate weather retrieval based on the input city name. Since we aren’t connecting to an actual weather API, we’ll display a mock result (e.g., "Sunny, 25°C").

```python
def fetch_weather(b):
    city = city_input.value
    # Simulate weather data
    weather = "Sunny, 25°C" if city else "No city entered"
    weather_output.value = f"Weather in {city}: {weather}"
```

- The function `fetch_weather` will get the value entered in the `city_input` widget and display a simulated weather result.

#### **Step 6: Bind the Button to the Function**
Now, let’s connect the button to the weather fetching function. We use the `on_click` method to trigger the function whenever the button is clicked.

```python
fetch_button.on_click(fetch_weather)
```

#### **Step 7: Display All the Widgets Together**
Finally, we use the `display()` function to show all the widgets in the notebook (input, button, and weather output).

```python
display(city_input, fetch_button, weather_output)
```

At this point, you should have a fully functioning weather app in Colab! The user can enter a city name, click the button, and see a simulated weather result.

---

### **Exercise: Customize Your Weather App**
Now that you've created the basic weather app, let’s extend it with a few extra features. Try to implement the following:

1. **Change the Placeholder Text**: Modify the placeholder text in the `city_input` field to say "Type your city here".
   
2. **Error Handling**: Update the `fetch_weather` function to display an error message if the user clicks "Get Weather" without entering a city name.

3. **Additional Button**: Add a second button that clears the weather result when clicked.


---

### **Reflection Questions:**
1. How does the `on_click` function help make the app interactive?
2. What is the benefit of using `ipywidgets` in Google Colab for quick prototyping of GUIs?
3. Can you think of another scenario (besides weather) where a simple GUI like this could be helpful?




### **Step-by-Step Guide: Creating the Weather App with Visualisation**

#### **Step 1: Import Necessary Libraries**
Before starting, you need to import the `ipywidgets` library, `matplotlib` for the graph, and other necessary modules.

```python
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
```

#### **Step 2: Create the Input Widget for City Name**
The first step in our weather app is to allow the user to input a city name. We’ll use the `Text` widget to create an input field.

```python
city_input = widgets.Text(
    placeholder='Enter city name',
    description='City:',
    disabled=False
)
```

#### **Step 3: Add a Button to Fetch Weather and Plot Data**
Now, let’s create a button that users will click to fetch the weather data and display a temperature trend.

```python
fetch_button = widgets.Button(
    description='Get Weather and Show Trend',
    disabled=False,
    button_style='primary'  # Optional styling
)
```

#### **Step 4: Create a Label to Display Weather Information**
Next, we need a place to display the weather results (such as today's temperature) and the city name entered.

```python
weather_output = widgets.Label(value="")
```

#### **Step 5: Simulate 5-Day Temperature Trend Data**
For the sake of this exercise, we will simulate a 5-day temperature trend using `numpy` to generate random temperature data for the city.

```python
def get_temperature_trend(city):
    # Simulate a 5-day temperature trend
    np.random.seed(0)  # For reproducible results
    return 20 + 5 * np.random.randn(5)
```

#### **Step 6: Write the Function to Fetch Weather and Plot the Trend**
In this step, we create the logic that will simulate weather retrieval and display a temperature trend for the next 5 days using a line chart.

```python
def fetch_weather_and_plot(b):
    city = city_input.value
    if not city:
        weather_output.value = "No city entered"
    else:
        # Simulate fetching today's weather
        weather_output.value = f"Today's weather in {city}: Sunny, 25°C"
        
        # Get temperature trend
        temperatures = get_temperature_trend(city)
        
        # Plot the 5-day temperature trend
        plt.figure(figsize=(6,4))
        days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
        plt.plot(days, temperatures, marker='o')
        plt.title(f"5-Day Temperature Trend for {city}")
        plt.ylabel("Temperature (°C)")
        plt.xlabel("Days")
        plt.grid(True)
        plt.show()
```

#### **Step 7: Bind the Button to the Function**
Now, let’s connect the button to the weather fetching and plotting function. We use the `on_click` method to trigger the function whenever the button is clicked.

```python
fetch_button.on_click(fetch_weather_and_plot)
```

#### **Step 8: Display All the Widgets Together**
Finally, we use the `display()` function to show all the widgets in the notebook (input, button, and weather output), and we add a plot to visualize the temperature trend.

```python
display(city_input, fetch_button, weather_output)
```

At this point, you should have a fully functioning weather app in Colab! The user can enter a city name, click the button, and see both the current weather and a 5-day temperature trend.

---

### **Exercise: Customise Your Weather App with Visualisation**
Now that you've created the basic weather app with visualisation, let’s extend it with a few extra features. Try to implement the following:

1. **Customise the Plot**: Add labels for the x and y axes and experiment with different plot styles in `matplotlib`.
   
2. **Randomise Temperature Trends**: Modify the `get_temperature_trend()` function to simulate different weather conditions based on the city entered (e.g., higher temperatures for tropical cities).

3. **Advanced Challenge (Optional)**: Connect to a real weather API (like OpenWeatherMap) and fetch real temperature data for the 5-day forecast.
