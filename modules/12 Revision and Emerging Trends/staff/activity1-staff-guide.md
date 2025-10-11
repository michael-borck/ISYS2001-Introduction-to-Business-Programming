---
title: "STAFF-ANSWER-GUIDE Activity 1: Setting Up Your Local Python Environment"
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

## Overview for Tutors

This guide will help you support students as they install Anaconda and set up their local Python environment. The transition from cloud-based environments (like Google Colab) to local development is a significant step that often presents challenges for beginners. This guide highlights common issues, provides troubleshooting strategies, and offers additional context to help you guide students effectively.

## Learning Objectives Assessment

Students should demonstrate the following by the end of this activity:

1. Successfully installed Anaconda on their system
2. Created and run a Jupyter Notebook locally
3. Verified that essential libraries (pandas, matplotlib, numpy) work properly
4. Installed an additional package (pygame) for future activities
5. Basic understanding of Anaconda's components and environment management

## Expected Submission from Students

✅ Screenshot showing Jupyter Notebook with working matplotlib plot  
✅ Written answers to the checkpoint questions  

## Answer Key for Checkpoint Questions

### 1. What are two advantages of using Anaconda instead of installing Python directly?

**Strong answers include any two of:**
- Includes many pre-installed scientific and data analysis packages
- Provides an integrated package manager (conda) for easy installation of additional libraries
- Includes tools like Jupyter Notebook, Spyder IDE, and Anaconda Navigator
- Simplifies environment management and package dependencies
- Works consistently across different operating systems
- Avoids conflicts with system Python installations

**Weak answers:**
- "It's easier" (without specifics)
- "It's better for beginners" (without explaining why)
- Answers that confuse Anaconda with Python itself

### 2. What is the difference between Jupyter Notebook and Python IDLE?

**Strong answers include:**
- Jupyter Notebook provides an interactive, cell-based interface where code, text, and visualisations can coexist; IDLE is a basic code editor and shell
- Jupyter supports markdown, HTML, and rich media outputs; IDLE is primarily text-based
- Jupyter Notebooks can be shared as documents with outputs included; IDLE is focused on writing and running scripts
- Jupyter runs in a web browser; IDLE is a standalone application

**Weak answers:**
- Answers that don't recognise the fundamentally different purposes and interfaces
- Answers that claim one is "better" without explaining the differences

### 3. Why might you want to create different environments for different projects?

**Strong answers include:**
- To manage different package versions or dependencies between projects
- To avoid conflicts between packages that may be incompatible
- To ensure reproducibility by isolating project requirements
- To experiment with different Python versions
- To share exact environment specifications with collaborators

**Weak answers:**
- Vague responses about "organisation" without mentioning package management
- Answers that suggest environments are just for file organisation

### 4. How would you install a new package that isn't currently in your Anaconda installation?

**Strong answers include either:**
- Using conda: `conda install package_name`
- Using pip within Anaconda: `pip install package_name`
- Using Anaconda Navigator's graphical interface to search and install packages

**Bonus points** for mentioning:
- Specifying the channel: `conda install -c conda-forge package_name`
- Creating/activating environments before installing: `conda activate myenv`
- Using environment files: `conda env create -f environment.yml`

**Weak answers:**
- Incorrect syntax for installation commands
- Methods that don't use conda or pip (within the Anaconda ecosystem)

### 5. What does the following code do in a Jupyter Notebook?
```python
import sys
print(sys.executable)
```

**Strong answer:**
- It displays the path to the Python executable that's currently running the notebook
- This helps verify which Python installation/environment is being used

**Weak answers:**
- Answers that don't recognise this shows the Python interpreter location
- Answers that confuse this with displaying Python version information

## Common Technical Issues and Solutions

### Installation Problems

| Issue | Common Causes | Solution |
|-------|--------------|----------|
| "Anaconda is not recognised" in command prompt/terminal | PATH not set correctly during installation | 1. Reinstall with "Add to PATH" option checked<br>2. Manually add Anaconda to PATH<br>3. Use Anaconda Prompt instead |
| Installation appears to hang | Large download, slow extraction on older hardware | Be patient - the installer may take 10-30 minutes on slower systems |
| "Permission denied" errors on macOS/Linux | Not running as administrator/sudo | Rerun installer with appropriate permissions |
| "Failed to create Anaconda menu" on Windows | Multiple users on system | Run installer as administrator |
| Disk space errors | Insufficient free space (Anaconda needs ~3GB) | Help student clear space or identify another drive with sufficient space |

### Jupyter Notebook Issues

| Issue | Common Causes | Solution |
|-------|--------------|----------|
| Jupyter doesn't launch from Navigator | Browser issues, port conflicts | 1. Try launching from command line: `jupyter notebook`<br>2. Check if another notebook server is running |
| "Kernel not found" error | Python kernel not registered properly | Run: `python -m ipykernel install --user` |
| Plots don't display | Missing matplotlib backend config | Add `%matplotlib inline` at top of notebook |
| Notebook runs slowly | Low system resources, too many notebooks open | Close other applications, restart kernel between tests |
| Cannot connect to kernel | Background process issues | Restart computer; if persists, reinstall Jupyter: `conda install -c conda-forge notebook` |

### Package Installation Issues

| Issue | Common Causes | Solution |
|-------|--------------|----------|
| Package install fails | Internet connectivity, conflicts | 1. Check internet connection<br>2. Try `conda install -c conda-forge package_name`<br>3. Create a fresh environment for problematic packages |
| "PackagesNotFoundError" | Package not in default channels | Try pip instead: `pip install package_name` |
| "EnvironmentNotWritableError" | Trying to install in base env without permissions | Use `conda create -n myenv` to create a new environment first |
| Installing pygame specifically | Missing dependencies | On Linux: install SDL dev libraries<br>On Windows: update Visual C++ Redistributable |
| Different versions between pip and conda | Using both package managers | Stick to one manager per environment when possible |

### Platform-Specific Issues

#### Windows
- Command Prompt vs. Anaconda Prompt confusion
- PATH environment variable limitations
- Windows Defender/antivirus blocking executables

#### macOS
- M1/M2 chip compatibility issues with some packages
- XCode command-line tools requirements
- Homebrew conflicts

#### Linux
- Different package dependencies across distributions
- X11 requirements for graphical applications
- Permissions and multi-user setup complexities

## Teaching Tips

### Beginning of Session
- **Verify system requirements** before students begin installation
- **Ask students to download** Anaconda installer before the session starts
- **Prepare a backup plan** for students with unsuitable hardware (e.g., temporary cloud alternatives)
- **Group students by OS** to address platform-specific issues efficiently

### During Installation
- **Set expectations** about download and installation time (10-30 minutes)
- **Encourage screenshots** of any error messages
- **Create a help queue** for students stuck on installation issues
- **Prepare a demo environment** to show expected outcomes while students wait

### For Struggling Students
- **Prioritise getting Jupyter working** - even if not all packages install correctly
- **Offer "pair programming"** to let struggling students work with those who are successful
- **Provide screenshots** of expected outputs and interfaces
- **Consider alternative paths** (e.g., online Jupyter environments) if local installation is impossible

### For Advanced Students
- **Challenge them to explore** conda environments more deeply
- **Have them assist** peers who are having trouble
- **Introduce more advanced topics** like environment.yml files or JupyterLab
- **Discuss IDEs** like VS Code or PyCharm as alternatives to Jupyter

## Activity Extensions

For students who finish early or need additional challenges:

1. **Create a new environment** with a different Python version and observe differences
2. **Install and test JupyterLab** as an alternative to Jupyter Notebook
3. **Export their environment** to an environment.yml file and recreate it
4. **Install a specialised package** like scikit-learn, OpenCV, or TensorFlow and test it
5. **Compare performance** between local Jupyter and Google Colab for identical notebooks

## Assessment Guidance

### Exemplary Work Should Show:
- Complete, successful installation with all test code running
- Clear understanding of Anaconda's purpose and components
- Thoughtful answers to checkpoint questions that demonstrate understanding
- Evidence of exploration beyond minimum requirements
- Clean, well-organised notebook with appropriate markdown cells

### Satisfactory Work Should Show:
- Successful installation with basic functionality working
- Basic understanding of Anaconda's purpose
- Reasonable answers to checkpoint questions
- Completed basic tasks as outlined in worksheet

### Needs Improvement If:
- Installation incomplete or non-functional
- Unable to run basic Python code locally
- Minimal or incorrect answers to checkpoint questions
- No evidence of independent problem-solving

## Preventing Common Conceptual Misunderstandings

### Anaconda vs. Python
Many students confuse Anaconda with Python itself. Clarify that Anaconda is a distribution that includes Python plus additional tools and packages.

### Jupyter vs. Python
Some students think Jupyter is a different language. Emphasise that Jupyter is just an interface for running Python (and other languages).

### Conda vs. Pip
Students often don't understand the difference between these package managers. Explain that conda can handle non-Python dependencies and environment management, while pip is Python-specific.

### Environments vs. Folders
Students may conflate environments with simple file organisation. Explain that environments are isolated installations with their own packages and dependencies.

## Post-Activity Follow-Up

After all students have completed the activity:

1. **Conduct a brief survey** to identify common challenges
2. **Prepare a follow-up document** addressing frequently asked questions
3. **Create a troubleshooting guide** specific to your class's common issues
4. **Check installation status** before the next activity that requires local Python

## Final Notes for Tutors

- **Be patient** - this is often students' first experience with development environment setup
- **Validate frustration** - acknowledge that environment setup is challenging even for professionals
- **Emphasise the value** of learning to set up local environments despite the initial hurdles
- **Document unique issues** you encounter for future sessions

Remember that successfully navigating installation challenges is itself a valuable learning experience for students, preparing them for real-world development environments.
