---
title: "STAFF ANSWER: Data visualisation with Python and Pandas"
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

### Tasks

#### Task 1: Load the Dataset

**Note 1: Assume the students has downloaded from unit's blackboard site and upload csv file to Google Colab virtual machine**

**Note 2: This is CRITICAL for all questions, assuming it has been uploaded to Google Colab virtual machine, in the file tab, right click on file and select 'copy path', and can use this as the 'filename' name path in the *pd.read_csv('path_to_weather_data.csv')* below**

1. Load the weather dataset into a Pandas DataFrame.
   - Use the `pd.read_csv()` function to read the CSV file.
   - Display the first 5 rows of the DataFrame using the `.head()` method.

   **Questions:**
   - What are the column names in your dataset?
   - How many rows and columns does the dataset have?

   **Code Example:**
   ```python
   import pandas as pd

   # Load the dataset, assume in same folder as script
   df = pd.read_csv('mock_weather_data_seasonal.csv')

   # Display the first 5 rows
   print(df.head())
   ```

#### Task 2: Line Plot for Temperature Trends
2. Generate a line plot to visualize temperature trends over time.
   - Use the `plt.plot()` function from Matplotlib to plot the data.
   - Set appropriate labels for the x-axis (e.g., date) and y-axis (temperature).
   - Include a title for your plot.

   **Questions:**
   - What trends do you observe in the temperature over time?
   - Are there any noticeable patterns or anomalies?

   **Code Example:**
   ```python
   import matplotlib.pyplot as plt

   # Line plot for temperature trends
   plt.figure(figsize=(10, 5))
   plt.plot(df['Date'], df['Temperature'], label='Temperature', color='blue')
   plt.xlabel('Date')
   plt.ylabel('Temperature (°C)')
   plt.title('Temperature Trends Over Time')
   plt.xticks(rotation=45)
   plt.legend()
   plt.show()
   ```

#### Task 3: Scatter Plot for Temperature vs. Humidity
3. Create a scatter plot to explore the relationship between temperature and humidity.
   - Use the `plt.scatter()` function from Matplotlib.
   - Set labels for the axes and include a title.

   **Questions:**
   - Describe the relationship between temperature and humidity. Is there a correlation?
   - How would you describe the strength and direction of this relationship?

   **Code Example:**
   ```python
   # Scatter plot for Temperature vs. Humidity
   plt.figure(figsize=(8, 5))
   plt.scatter(df['Temperature'], df['Humidity'], color='green')
   plt.xlabel('Temperature (°C)')
   plt.ylabel('Humidity (%)')
   plt.title('Temperature vs. Humidity')
   plt.show()
   ```

#### Task 4: Bar Plot for Monthly Precipitation
4. Design a bar plot to compare monthly precipitation levels.
   - Group the data by month and calculate the total precipitation for each month.
   - Use the `plt.bar()` function to create the bar plot.
   - Set labels and a title.

   **Questions:**
   - Which month has the highest total precipitation?
   - Are there any months with significantly lower or higher precipitation levels?

   **Code Example:**
   ```python
   # Converting date column to datetime format and extracting the month
   df['Date'] = pd.to_datetime(df['Date'])
   df['Month'] = df['Date'].dt.month

   # Grouping by month and summing up precipitation
   monthly_precipitation = df.groupby('Month')['Precipitation'].sum()

   # Bar plot for Monthly Precipitation
   plt.figure(figsize=(10, 5))
   plt.bar(monthly_precipitation.index, monthly_precipitation.values, color='skyblue')
   plt.xlabel('Month')
   plt.ylabel('Total Precipitation (mm)')
   plt.title('Monthly Precipitation Levels')
   plt.xticks(ticks=range(1, 13), labels=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
   plt.show()
   ```

#### Task 5: Multi-Panel Figure with Subplots
5. Combine the line plot, scatter plot, and bar plot into a multi-panel figure using subplots.
   - Use the `plt.subplots()` function to create a multi-panel layout.
   - Arrange the plots for easy comparison and analysis.

   **Questions:**
   - How do the different visualizations complement each other?
   - What insights can you draw by comparing these visualizations side by side?

   **Code Example:**
   ```python
   # Creating subplots
   fig, axs = plt.subplots(2, 2, figsize=(15, 10))

   # Line plot in the first subplot
   axs[0, 0].plot(df['Date'], df['Temperature'], color='blue')
   axs[0, 0].set_title('Temperature Trends Over Time')
   axs[0, 0].set_xlabel('Date')
   axs[0, 0].set_ylabel('Temperature (°C)')

   # Scatter plot in the second subplot
   axs[0, 1].scatter(df['Temperature'], df['Humidity'], color='green')
   axs[0, 1].set_title('Temperature vs. Humidity')
   axs[0, 1].set_xlabel('Temperature (°C)')
   axs[0, 1].set_ylabel('Humidity (%)')

   # Bar plot in the third subplot
   axs[1, 0].bar(monthly_precipitation.index, monthly_precipitation.values, color='skyblue')
   axs[1, 0].set_title('Monthly Precipitation Levels')
   axs[1, 0].set_xlabel('Month')
   axs[1, 0].set_ylabel('Total Precipitation (mm)')

   # Hide the fourth subplot (empty)
   axs[1, 1].axis('off')

   # Adjust layout
   plt.tight_layout()
   plt.show()
   ```

