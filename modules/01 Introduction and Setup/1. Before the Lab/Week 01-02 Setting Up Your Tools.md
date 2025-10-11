---
title: "Setting Up Your Tools"
subtitle: "Colab Noteboooks & GitHub"
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
# In this module

- Learn essential tools for Python development
- Master Google Colab for cloud-based coding
- Understand GitHub for version control
- Discover how AI can accelerate your learning
- Get hands-on practice with real examples

::: {.notes}
In this module, you'll gain essential skills for Python development using powerful tools like Google Colab and GitHub. You'll learn how to create and run Python code in the cloud with Colab, and how to use GitHub for version control and collaboration. By the end of this module, you'll have hands-on experience with real-world examples and be ready to apply these tools to your own projects.

Throughout the module, we'll explore how AI can accelerate your Python learning journey. You'll discover practical examples of integrating AI into your workflow, and learn about AI tools specifically designed for Python development and learning. By leveraging these cutting-edge technologies, you'll be well-equipped to tackle complex problems and build innovative solutions with Python.
:::

# What is Google Colab?

- Cloud-based Jupyter Notebook environment
- No installation required
- Free GPU access for AI projects
- Ideal for learning Python in a browser

::: {.notes}
Google Colab is a cloud-based Jupyter Notebook environment that allows users to write and execute Python code directly in their web browser, without the need for any local installation. This makes it an ideal platform for learning Python, as users can start coding immediately without worrying about setting up a development environment. Additionally, Google Colab offers free access to GPUs, which is particularly useful for AI and machine learning projects that require significant computational power.

One of the key advantages of using Google Colab is its simplicity and accessibility. Users only need a Google account to get started, and they can create, save, and access their notebooks from anywhere with an internet connection. This makes it easy for learners to collaborate on projects, share their work, and learn from others in the community. Furthermore, Google Colab integrates seamlessly with other Google services, such as Google Drive and Google Sheets, allowing users to import and export data easily.
:::

# Getting Started - Google Account Required

- A **Google Account** is required to use Google Colab.
- Sign in at [colab.research.google.com](https://colab.research.google.com).
- Notebooks are stored in Google Drive.
- Can be shared and collaborated on in real-time.

::: {.notes}
To use Google Colab, you must have a Google Account. Sign in at colab.research.google.com to access the platform. Once you're signed in, your notebooks will be stored in your Google Drive, making it easy to access them from anywhere.

One of the great features of Google Colab is its collaborative capabilities. You can share your notebooks with others and work on them together in real-time, just like you would with a Google Doc. This makes it an excellent tool for team projects and group learning.
:::

# Creating Your First Notebook

- Go to Google Colab.
- Click **File > New Notebook**.
- A new notebook with a code cell will appear.
- Start writing Python code!

::: {.notes}
To create your first notebook in Google Colab, simply navigate to the Google Colab website and click on "File" in the top menu, then select "New Notebook". This will open a fresh notebook with a code cell ready for you to start writing Python code straight away.

The process of creating a new notebook in Google Colab is quick and easy, allowing you to dive right into coding without any setup or installation required. With the notebook open, you can immediately begin experimenting with Python code, exploring libraries, and building your projects in a user-friendly, cloud-based environment.
:::

# Running Your First Python Code

- Click inside a code cell.
- Type: `print("Hello, World!")`
- Press **Shift + Enter** to execute the code.
- See the output immediately!

::: {.notes}
Running your first Python code in Google Colab is straightforward. Simply click inside a code cell and type the line `print("Hello, World!")`. Once you've entered the code, press **Shift + Enter** to execute it. The output will appear immediately below the code cell, allowing you to see the results of your code instantly.

Google Colab provides an intuitive and user-friendly environment for running Python code. With the ability to execute code directly in the browser, you can quickly test and iterate on your Python scripts without the need for any additional setup. This makes it an ideal platform for beginners learning Python or for experienced developers who want to prototype ideas rapidly.
:::

# Saving and Accessing Notebooks

- Notebooks are auto-saved in **Google Drive**.
- Download as `.ipynb` or `.py` for offline use.
- Shareable via link for collaboration.
- We will be using GitHub

::: {.notes}
Google Colab notebooks are automatically saved in Google Drive, providing a convenient and secure storage solution. Users have the option to download the notebooks in either `.ipynb` or `.py` format for offline use, allowing for flexibility in working environments. The notebooks can also be easily shared with others via a shareable link, facilitating seamless collaboration among team members.

While Google Colab offers built-in saving and sharing features, the course will also utilise GitHub as an additional platform for notebook management. GitHub provides version control and collaborative features that complement Google Colab's functionality. By integrating GitHub into the workflow, users can effectively track changes, manage multiple versions of their notebooks, and collaborate with others on a larger scale.
:::

# Why Use GitHub?

- **Version control** – Keep track of code changes over time.
- **Collaboration** – Work with peers and instructors.
- **Backup & Accessibility** – Access notebooks from any device.
- **Integration with Google Colab** – Save directly from Colab to GitHub.

::: {.notes}
GitHub is an essential tool for version control, collaboration, backup, and accessibility when working with code. It allows you to keep track of changes to your code over time, ensuring that you can easily revert to previous versions if needed. GitHub also facilitates seamless collaboration with peers and instructors, enabling you to work together on projects and share your code with others.

In addition to its version control and collaboration features, GitHub provides a reliable backup solution for your code and notebooks. By storing your work on GitHub, you can access your notebooks from any device with an internet connection, giving you the flexibility to work from anywhere. Furthermore, GitHub integrates seamlessly with Google Colab, allowing you to save your notebooks directly from Colab to your GitHub repository, streamlining your workflow and ensuring that your work is always up to date.
:::

# Setting Up GitHub in Google Colab

- A **GitHub account** is required ([Sign up](https://github.com/))
- Authorize **Google Colab** to access GitHub.
- Create a new **repository** or use an existing one.

::: {.notes}
Setting up GitHub in Google Colab is a straightforward process that requires a GitHub account. If you don't have one, you can easily sign up on the GitHub website. Once you have an account, you need to authorise Google Colab to access your GitHub repositories. This allows seamless integration between the two platforms, enabling you to save and manage your Colab notebooks using version control.

After linking your GitHub account, you can either create a new repository or use an existing one to store your Colab notebooks. Creating a dedicated repository for your Colab projects helps keep your work organised and easily accessible. With GitHub set up, you're ready to start saving, sharing, and collaborating on your Colab notebooks, leveraging the power of version control and the convenience of cloud-based development.
:::

# Connecting Google Colab to GitHub

- Open **Google Colab**.
- Click **File > Save a Copy in GitHub**.
- Select a repository and add a commit message.
- Click **OK** to upload.

::: {.notes}
To connect Google Colab to GitHub, start by opening Google Colab in your web browser. Once the Colab interface loads, click on the "File" menu and select "Save a Copy in GitHub" from the dropdown options. This will initiate the process of linking your Colab notebook to a GitHub repository.

After selecting "Save a Copy in GitHub", a new window will appear prompting you to choose a repository where you want to save your notebook. Select the desired repository from the list and enter a commit message to describe the changes you're making. Once you've chosen the repository and added a commit message, click the "OK" button to finalise the upload process and establish the connection between your Colab notebook and the selected GitHub repository.
:::

# Retrieving and Updating Notebooks from GitHub

- Open a **GitHub repository**.
- Click on the **notebook file (.ipynb)**.
- Click **Open in Colab** to edit.
- After modifications, **save back to GitHub**.

::: {.notes}
To retrieve and update notebooks from GitHub, start by opening the GitHub repository containing your notebook files. Locate the specific notebook you wish to edit, identifiable by the .ipynb file extension, and click on it. GitHub will display a preview of the notebook's contents. To make changes, click the "Open in Colab" button, which will launch the notebook in Google Colab, a cloud-based Python development environment.

Once you've made the necessary modifications to your notebook in Google Colab, save the changes by clicking the "File" menu and selecting "Save a copy in GitHub". This action will commit the updated notebook back to your GitHub repository, ensuring that the latest version is accessible for future reference or collaboration. By following these steps, you can seamlessly retrieve notebooks from GitHub, make edits in Google Colab, and push the changes back to the repository, streamlining your workflow and facilitating effective version control.
:::

# Best Practices for Saving Notebooks

- Write **clear commit messages** (e.g., "Updated data analysis section").
- Regularly **push updates** to GitHub to prevent data loss.
- Use **branches** for experimental changes before merging into the main repository.
- Keep notebooks **organized** within folders in your repository.

::: {.notes}
When saving notebooks in Google Colab, it's important to follow best practices to ensure your work is organised, secure, and easily accessible. Write clear commit messages that concisely describe the changes you've made, such as "Updated data analysis section", to help you and your collaborators understand the progress of your project. Regularly push updates to GitHub to prevent data loss and maintain a backup of your work in case of any unexpected issues with Google Colab.

To keep your repository clean and manageable, use branches for experimental changes before merging them into the main repository. This allows you to test new ideas without affecting the main codebase. Additionally, keep your notebooks organised within folders in your repository, making it easier to navigate and find specific files when needed. By following these best practices, you'll create a more efficient and productive workflow while collaborating with others on your Google Colab projects.
:::

# Common Issues and Fixes

- **Can't access Google Colab?** Check if you're logged into a Google Account.
- **Code not running?** Check for syntax errors in your Python code.
- **Authorization errors** – Ensure Google Colab has GitHub access.
- **Repository not showing?** – Refresh Colab or check GitHub permissions.
- **Failed to save?** – Check internet connection or re-authenticate.

::: {.notes}
This slide covers common issues you may encounter when working with Google Colab and GitHub, along with their respective solutions. If you can't access Google Colab, the first step is to ensure you're logged into a valid Google Account. Code not running is often due to syntax errors in your Python code, so double-check for any mistakes. Authorization errors can be resolved by granting Google Colab access to your GitHub account. If your repository isn't showing up, try refreshing Colab or verifying your GitHub permissions.

Lastly, if you're unable to save your work, check your internet connection and re-authenticate if necessary. These troubleshooting tips should help you overcome the most frequent obstacles and maintain a smooth workflow between Google Colab and GitHub. Don't hesitate to refer back to this slide if you run into any of these issues during your hands-on practice session or future projects.
:::

# Hands-on Practice

- Save a sample notebook to GitHub.
- Retrieve and modify it from GitHub.
- Commit changes with a clear message.
- Open your updated notebook in Colab.

::: {.notes}
Save a sample notebook to your GitHub repository, then retrieve and modify it from GitHub. When committing changes, use a clear and descriptive message to document the modifications made. Once the changes are committed, open the updated notebook in Google Colab to confirm the changes have been successfully applied.

This hands-on practice reinforces the concepts covered in the previous slides, such as setting up GitHub in Google Colab, connecting Google Colab to GitHub, and retrieving and updating notebooks from GitHub. By following best practices for saving notebooks and providing clear commit messages, you can effectively manage your notebooks and collaborate with others on your Python projects.
:::

# How AI Can Accelerate Your Python Learning

- **AI-Powered Code Suggestions:**  
  Tools like GitHub Copilot and ChatGPT offer real-time code completions and ideas.
  
- **Instant Explanations & Debugging:**  
  Use AI to explain error messages, clarify complex code segments, and suggest fixes.
  
- **Generate & Refactor Code:**  
  Let AI propose code samples or refactor existing code to improve efficiency.
  
- **Access to Summarized Documentation:**  
  Quickly get overviews of Python libraries and algorithms to enhance understanding.


---

::: {.notes}
* AI can provide intelligent code suggestions as you type, helping you write Python code faster and more efficiently. It can recommend relevant libraries, functions, and syntax based on your context, reducing the need for manual lookups and speeding up your coding process.

* AI can explain code snippets, identify potential bugs, and suggest fixes, saving you time in debugging. It can generate and refactor code based on your requirements, handle repetitive tasks, and provide summarized documentation, making it easier to understand and use new libraries or frameworks in your Python projects.
:::

# Practical Examples: Integrating AI in Your Workflow

- **Debugging Assistance:**  
  Paste error messages into ChatGPT for step-by-step debugging help.
  
- **Real-Time Code Suggestions:**  
  Use GitHub Copilot in Google Colab to get instant code completions and alternative approaches.
  
- **Learning New Libraries:**  
  Ask AI for concise summaries and usage examples when exploring unfamiliar Python libraries.
  
- **Interactive Q&A Sessions:**  
  Engage with AI to answer questions about Python syntax, logic, and best practices during your coding sessions.

::: {.notes}
Practical examples of integrating AI into your Python workflow include debugging assistance, where AI can help identify and fix errors in your code, saving you time and frustration. AI can also provide real-time code suggestions, offering intelligent recommendations as you type, which can improve your coding efficiency and help you discover new ways to solve problems. When learning new libraries, AI can quickly provide relevant documentation, usage examples, and answers to your questions, accelerating your learning process. Interactive Q&A sessions with AI allow you to dive deeper into Python concepts, clarify doubts, and receive personalised explanations tailored to your level of understanding.

By leveraging these AI-powered tools and techniques, you can streamline your Python development process, overcome challenges more easily, and expand your knowledge at a faster pace. Whether you're a beginner or an experienced programmer, integrating AI into your workflow can help you write better code, learn new concepts efficiently, and solve complex problems with greater ease. As you continue to explore the possibilities of AI in Python development, you'll find even more ways to enhance your productivity and take your skills to the next level.
:::

# AI Tools for Python & Learning

| AI Tool | Coding (Python) | Setup Difficulty |
|---|---|---|
| ChatGPT (OpenAI) | Excellent | Easiest (Sign up) |
| Gemini (Google) | Good | Easiest (Google account) |
| LLaMA (Meta AI) | Good | Medium (Technical setup) |
| Claude (Anthropic) | Good | Easiest (Sign up) |
| GitHub Copilot | Excellent | Easy (Extension install) |
| Perplexity.ai | Good | Easiest (Web access) |
| Bing (Microsoft) | Good | Easiest (Built-in) | 
| Leo (Brave) | Basic | Easiest (Built-in) |
| Bard (Google) | Good | Easiest (Google account) |
| Hugging Face | Varies | Medium (Technical knowledge) |
| DeepSeek AI | Excellent | Medium (Technical knowledge) |
| Phi (Microsoft) | Good | Medium (Technical knowledge) |

**Disclaimer:** This infographic is for informational purposes only.  The AI landscape is constantly changing.  Verify the information and consider your specific needs before choosing an AI model or tool.  This is not an exhaustive list, and other excellent AI models and tools are available.  Always review the terms of service and privacy policies of the respective providers.

::: {.notes}
AI tools like ChatGPT can accelerate your Python learning by providing instant explanations, code examples, and troubleshooting help. These AI assistants can answer your Python questions, clarify concepts, and even help you write and debug code. They're like having a personal Python tutor available 24/7.

Integrating AI into your Python workflow can boost your productivity and capabilities. For example, you can use AI to auto-generate boilerplate code, refactor existing code, and even get AI-powered code suggestions and completions as you type. AI can also help with tasks like data analysis, visualisation, and machine learning in Python.
:::

# Key Takeaways

  - Google Colab for cloud-based Python development
  - GitHub for version control and collaboration
  - Saving and retrieving work from GitHub
  - Access to powerful AI coding assistants
  - Enhanced learning through AI-powered tools
  - Faster development with intelligent suggestions

::: {.notes}
In this slide, we've highlighted the key takeaways from our exploration of using Google Colab and GitHub for Python development. Google Colab provides a cloud-based platform that allows you to write and run Python code without the need for local setup, while GitHub enables version control and collaboration, making it easy to save, retrieve, and share your work with others. By leveraging these tools, you can access powerful AI coding assistants that offer intelligent suggestions and help accelerate your development process.

Moreover, we've discussed how AI-powered tools can enhance your learning experience by providing tailored guidance and real-time feedback. These tools can help you grasp complex concepts more quickly and efficiently, enabling you to focus on applying your knowledge to practical projects. As you continue your Python journey, remember to take advantage of these resources to streamline your workflow and unlock new possibilities in your programming endeavours.
:::

# Next Steps

Start practising with these tools by creating your first notebook and connecting it to GitHub. Remember that mastering these foundational tools will accelerate your Python learning journey.

::: {.notes}
- Explore the wealth of resources available, such as online tutorials, coding challenges, and open-source projects to continue honing your Python skills and expanding your knowledge of AI applications
- Consider joining coding communities, attending workshops or conferences, and collaborating with others to stay motivated, learn from shared experiences, and discover new opportunities to apply your skills in real-world projects
:::

