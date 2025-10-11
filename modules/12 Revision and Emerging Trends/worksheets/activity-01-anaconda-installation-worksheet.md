---
title: "Activity 1: Setting Up Your Local Python Environment"
author: "Michael Borck"
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


## Introduction

So far, we've been using Google Colab to write and run our Python code online. Now it's time to set up Python on your own computer! This worksheet will guide you through installing Anaconda, a popular Python distribution that includes Python itself plus many useful libraries and tools for data science, visualisation, and more.

## Why Anaconda?

- **All-in-one package**: Includes Python, key libraries, and useful tools
- **Easy to install**: Works on Windows, Mac, and Linux with minimal configuration
- **Includes Jupyter Notebooks**: The same notebook interface we've been using in Colab
- **Package management**: Makes it easy to install additional libraries
- **Industry standard**: Widely used in data science, research, and education

## Part 1: Installing Anaconda

### Step 1: Download the Installer

1. Open your web browser and go to: https://www.anaconda.com/download
2. Select your operating system (Windows, macOS, or Linux)
3. Download the **Anaconda Individual Edition** installer
   - Choose the **Python 3.x** version (not Python 2.x)
   - Note: This is a large download (500MB+) so it may take some time

### Step 2: Run the Installer

**For Windows:**
1. Double-click the downloaded `.exe` file
2. Select "Install for Just Me" (recommended)
3. Choose an installation location (the default is fine)
4. **Important:** Check both boxes for:
   - Add Anaconda to my PATH environment variable
   - Register Anaconda as my default Python
5. Click "Install" and wait for the installation to complete

**For macOS:**
1. Double-click the downloaded `.pkg` file
2. Follow the prompts in the installer
3. Install for "Just Me" (recommended)
4. Use the default installation location
5. At the end, you can choose whether to install VS Code (optional)

**For Linux:**
1. Open Terminal and navigate to the download directory
2. Run: `bash ./Anaconda3-2023.XX-Linux-x86_64.sh` (replace with your version number)
3. Follow the prompts, agreeing to the license terms
4. Allow the installer to initialise Anaconda in your shell

### Step 3: Verify Installation

Let's make sure Anaconda installed correctly:

1. **For Windows**: Click Start, search for and open "Anaconda Navigator"
2. **For macOS**: Open Spotlight (Cmd+Space), type "Navigator" and open Anaconda Navigator
3. **For Linux**: Open a terminal and type `anaconda-navigator`

You should see the Anaconda Navigator home screen with various applications like Jupyter, VS Code, and others.

## Part 2: Exploring the Anaconda Environment

### Step 1: Launch Jupyter Notebook

Jupyter Notebooks are interactive documents where you can write and run code, add explanations, and visualise results.

1. In Anaconda Navigator, click the "Launch" button under Jupyter Notebook
2. Your web browser should open, showing the Jupyter file browser
3. Navigate to a folder where you want to create your first notebook
4. Click the "New" button in the upper right and select "Python 3" to create a new notebook

### Step 2: Create Your First Local Notebook

Let's test your installation by creating a simple notebook:

1. In the first cell of your new notebook, type the following code:
   ```python
   print("Hello from my local Python environment!")
   ```

2. Run the cell by clicking the "Run" button or pressing Shift+Enter
   - You should see the greeting printed below the cell

3. In a new cell, let's verify that some important libraries are installed:
   ```python
   import pandas as pd
   import matplotlib.pyplot as plt
   import numpy as np
   
   print("Pandas version:", pd.__version__)
   print("Matplotlib version:", plt.__version__)
   print("NumPy version:", np.__version__)
   
   # Create a simple plot
   plt.figure(figsise=(8, 4))
   x = np.linspace(0, 10, 100)
   plt.plot(x, np.sin(x))
   plt.title("A Simple Sine Wave")
   plt.show()
   ```

4. Run this cell to make sure all the libraries work and you can create plots

5. Save your notebook by clicking File → Save or pressing Ctrl+S (Cmd+S on Mac)

## Part 3: Installing Additional Packages

One advantage of having a local Python environment is the ability to install any package you need. Let's try installing a new package:

### Step 1: Use Conda to Install a Package

1. Close Jupyter Notebook (File → Close and Halt)
2. Return to Anaconda Navigator
3. Click on the "Environments" tab on the left sidebar
4. In the packages search box, type "pygame" (we'll need this for our game development later)
5. Check the box next to pygame and click "Apply" to install it

### Step 2: Test Your New Package

1. Return to the "Home" tab and launch Jupyter Notebook again
2. Create a new notebook
3. Enter and run the following code to verify pygame is installed:
   ```python
   import pygame
   print("Pygame version:", pygame.version.ver)
   
   # Initialise pygame
   pygame.init()
   
   # Print available pygame modules
   modules = pygame.get_init()
   print("Pygame initialised successfully!")
   
   # Clean up
   pygame.quit()
   ```

## Part 4: Understanding Your New Environment

Let's explore some key components of the Anaconda environment:

1. **Anaconda Navigator**: The graphical interface to manage your Python environment
2. **Jupyter Notebook**: Interactive coding environment for Python (and other languages)
3. **conda**: The package manager (similar to pip) for installing and managing libraries
4. **Environments**: Isolated workspaces that can have different Python versions/packages

## Checkpoint Questions

Answer these questions to check your understanding:

1. What are two advantages of using Anaconda instead of installing Python directly?

2. What is the difference between Jupyter Notebook and Python IDLE?

3. Why might you want to create different environments for different projects?

4. How would you install a new package that isn't currently in your Anaconda installation?

5. What does the following code do in a Jupyter Notebook?
   ```python
   import sys
   print(sys.executable)
   ```

## Next Steps and Troubleshooting

### Common Issues:

- **"Anaconda is not recognised as a command"**: You may need to restart your computer after installation
- **Jupyter doesn't show plots**: Try adding `%matplotlib inline` at the top of your notebook
- **Package installation fails**: Make sure you're connected to the internet and try again
- **Slow performance**: Some older computers may run Jupyter slowly - try closing other applications

### Getting Help:

If you encounter problems:
1. Check the error message carefully
2. Search for the error message online
3. Ask for help in our class forum
4. Visit the Anaconda documentation: https://docs.anaconda.com/

## Submission Guidelines

To complete this activity:

1. Take a screenshot of your running Jupyter Notebook showing the sine wave plot
2. Answer the checkpoint questions in a text document
3. Submit both files via the course platform

Great work setting up your local Python environment! In the next activity, we'll explore some exciting Python projects that build on the fundamentals you've learned so far.
