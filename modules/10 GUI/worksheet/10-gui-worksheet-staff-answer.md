---
title: "STAFF ANSWER: Building a Simple Weather App GUI in Google Colab with ipywidgets"
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
This staff guide provides solutions, explanations, and tips for assessing
students' progress through the worksheet. The main goal of the worksheet is to
help students learn about creating simple GUIs using `ipywidgets` in Google
Colab, and to introduce them to visualizing data with `matplotlib`.

---

### **Expected Outcomes:**

1. **Basic Weather App with ipywidgets**:
   - Students should successfully create a text input widget, a button, and a
     label to display simulated weather results.
   - The app should display a simulated weather message like "Weather in [City]:
     Sunny, 25°C" when a user enters a city and clicks the button.
   
2. **Extended Weather App with Visualization**:
   - Students will simulate a 5-day temperature trend for the entered city and
     plot this data using `matplotlib`.
   - The temperature trend will be random, but plotted with proper labels and a
     line graph.
   
3. **Version Control**:
   - Students are encouraged to frequently save their work to GitHub. They
     should submit their GitHub links or evidence of regular commits.

---

### **Frequently Save Your Work to GitHub**

Students should follow the instructions to save their work to GitHub. Look for:

- Regular commits with meaningful messages such as *"Added temperature trend
  plotting"*.
- Ensuring they push their final notebook with complete functionality (input,
  button, label, and visualization).

---

### **Step-by-Step Guide: Basic Weather App**

#### **Step 1: Import Necessary Libraries**

Expected Solution:
```python
import ipywidgets as widgets
from IPython.display import display
```

#### **Step 2: Input Widget for City Name**

Expected Solution:
```python
city_input = widgets.Text(
    placeholder='Enter city name',
    description='City:',
    disabled=False
)
```
Assessment:
- The widget should display an input box with the label "City:" and placeholder text "Enter city name."

#### **Step 3: Add a Button**

Expected Solution:
```python
fetch_button = widgets.Button(
    description='Get Weather',
    disabled=False,
    button_style='primary'  # Optional styling
)
```
Assessment:
- Ensure the button is created correctly with the label "Get Weather."

#### **Step 4: Create a Label for Weather Display**

Expected Solution:
```python
weather_output = widgets.Label(value="")
```
Assessment:
- Check that the label is initialized with an empty string.

#### **Step 5: Simulate Weather Fetching Function**

Expected Solution:
```python
def fetch_weather(b):
    city = city_input.value
    weather = "Sunny, 25°C" if city else "No city entered"
    weather_output.value = f"Weather in {city}: {weather}"
```
Assessment:
- Check that the function returns the correct message depending on whether a city is entered.
- Ensure that `"No city entered"` is displayed if the user clicks the button without entering a city.

#### **Step 6: Bind Button to Function**

Expected Solution:
```python
fetch_button.on_click(fetch_weather)
```

#### **Step 7: Display All Widgets**

Expected Solution:
```python
display(city_input, fetch_button, weather_output)
```

### **Exercise: Customize Your Weather App**

Students are expected to modify the app in various ways:

1. **Change Placeholder Text**:
   ```python
   city_input.placeholder = "Type your city here"
   ```

2. **Error Handling**:
   - The `fetch_weather` function should be updated to display an error message like:
   ```python
   if not city:
       weather_output.value = "Please enter a city name"
   ```

3. **Additional Button**:
   - Students should add a "Clear" button that resets the label to an empty string:
   ```python
   clear_button = widgets.Button(description="Clear")
   def clear_output(b):
       weather_output.value = ""
   clear_button.on_click(clear_output)
   display(clear_button)
   ```

---

### **Step-by-Step Guide: Weather App with Visualization**

#### **Step 1: Import Necessary Libraries**

Expected Solution:
```python
import ipywidgets as widgets
from IPython.display import display
import matplotlib.pyplot as plt
import numpy as np
```

#### **Step 2: Input Widget for City Name**

Expected Solution:
(Same as before, Step 2)

#### **Step 3: Add Button for Fetching Weather and Plotting**

Expected Solution:
```python
fetch_button = widgets.Button(
    description='Get Weather and Show Trend',
    disabled=False,
    button_style='primary'
)
```

#### **Step 4: Create Label for Weather Display**

Expected Solution:
(Same as before, Step 4)

#### **Step 5: Simulate 5-Day Temperature Trend Data**

Expected Solution:
```python
def get_temperature_trend(city):
    np.random.seed(0)  # For reproducible results
    return 20 + 5 * np.random.randn(5)
```
Assessment:
- The `get_temperature_trend` function should simulate temperature data using `numpy`.

#### **Step 6: Fetch Weather and Plot the Trend**

Expected Solution:
```python
def fetch_weather_and_plot(b):
    city = city_input.value
    if not city:
        weather_output.value = "No city entered"
    else:
        weather_output.value = f"Today's weather in {city}: Sunny, 25°C"
        temperatures = get_temperature_trend(city)
        plt.figure(figsize=(6, 4))
        days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
        plt.plot(days, temperatures, marker='o')
        plt.title(f"5-Day Temperature Trend for {city}")
        plt.ylabel("Temperature (°C)")
        plt.xlabel("Days")
        plt.grid(True)
        plt.show()
```
Assessment:
- Ensure the function handles both weather text and temperature plotting.
- Check that the plot includes proper labels (days on x-axis, temperature on y-axis).

#### **Step 7: Bind Button to Function**

Expected Solution:
```python
fetch_button.on_click(fetch_weather_and_plot)
```

#### **Step 8: Display All Widgets**

Expected Solution:
(Same as before, Step 7)

---

### **Exercise: Customise Your Weather App with Visualization**

1. **Customise the Plot**:
   - Students should modify the plot to add titles, labels, and other custom styles.
   - For example, add axis labels:
   ```python
   plt.xlabel("Days of the Week")
   plt.ylabel("Temperature in °C")
   ```

2. **Randomise Temperature Trends**:
   - Modify the `get_temperature_trend()` function to provide a different range of temperatures based on the city entered.

3. **Advanced Challenge**:
   - This would involve connecting to a real weather API such as OpenWeatherMap to fetch real weather data. This is optional and requires students to understand how to interact with external APIs.

---

### **Reflection Questions (Answers)**

1. **How does the `on_click` function help make the app interactive?**
   - The `on_click` function binds the button to a function that is triggered when the user clicks the button, making the app responsive to user inputs.

2. **What is the benefit of using `ipywidgets` in Google Colab for quick prototyping of GUIs?**
   - `ipywidgets` makes it easy to create simple interactive elements without requiring complex front-end development knowledge. It's ideal for prototyping GUIs in a Jupyter/Colab environment.

3. **Can you think of another scenario (besides weather) where a simple GUI like this could be helpful?**
   - Examples might include a basic financial calculator, a to-do list app, or an interactive form for entering survey data.

---

### **Conclusion**

This guide provides a comprehensive solution and explanation for assessing the student's work. The goal is to ensure students understand the basic GUI elements and have the opportunity to apply these concepts in a simple, fun project.