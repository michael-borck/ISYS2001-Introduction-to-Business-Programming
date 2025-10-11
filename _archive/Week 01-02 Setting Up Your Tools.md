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

# What is Google Colab?

- Cloud-based Jupyter Notebook environment
- No installation required
- Free GPU access for AI projects
- Ideal for learning Python in a browser

::: {.notes}
Google Colab allows you to write and execute Python code in your web browser without needing to install anything. It’s a cloud-based tool that’s great for beginners and advanced users alike. You can use it to write Python code, analyze data, and even leverage powerful GPUs for machine learning projects.
:::


# Getting Started - Google Account Required

- A **Google Account** is required to use Google Colab.
- Sign in at [colab.research.google.com](https://colab.research.google.com).
- Notebooks are stored in Google Drive.
- Can be shared and collaborated on in real-time.

::: {.notes}
To use Google Colab, you must have a **Google Account**. If you don’t have one, you can create one at [accounts.google.com](https://accounts.google.com). Your notebooks will be saved automatically in Google Drive, making it easy to access and collaborate.
:::


# Creating Your First Notebook

- Go to Google Colab.
- Click **File > New Notebook**.
- A new notebook with a code cell will appear.
- Start writing Python code!

::: {.notes}
After logging into Google Colab, creating a new notebook is simple. You can add multiple code and text cells to organize your work and execute code step by step.
:::


# Running Your First Python Code

- Click inside a code cell.
- Type: `print("Hello, World!")`
- Press **Shift + Enter** to execute the code.
- See the output immediately!

::: {.notes}
Google Colab provides an interactive environment. Type `print("Hello, World!")` and run the cell by pressing **Shift + Enter**. The result will be displayed right below the cell.
:::


# Saving and Accessing Notebooks

- Notebooks are auto-saved in **Google Drive**.
- Download as `.ipynb` or `.py` for offline use.
- Shareable via link for collaboration.
- We will be using GitHub

::: {.notes}
Colab automatically saves your work in Google Drive. You can also download your notebooks in different formats and share them with others, just like Google Docs.
:::



# Why Use GitHub?

- **Version control** – Keep track of code changes over time.
- **Collaboration** – Work with peers and instructors.
- **Backup & Accessibility** – Access notebooks from any device.
- **Integration with Google Colab** – Save directly from Colab to GitHub.

::: {.notes}
GitHub is a powerful tool that allows you to store and manage your Python notebooks securely. Using version control, you can track changes, collaborate on projects, and restore previous versions of your work. This is essential for maintaining clean and organized coding projects.
:::


# Setting Up GitHub in Google Colab

- A **GitHub account** is required ([Sign up](https://github.com/))
- Authorize **Google Colab** to access GitHub.
- Create a new **repository** or use an existing one.

::: {.notes}
Before saving notebooks to GitHub, you need a GitHub account and must allow Google Colab to interact with GitHub. You can either create a new repository or use an existing one to store your notebooks.
:::


# Connecting Google Colab to GitHub

- Open **Google Colab**.
- Click **File > Save a Copy in GitHub**.
- Select a repository and add a commit message.
- Click **OK** to upload.

::: {.notes}
In Google Colab, saving to GitHub is straightforward. This ensures your work is stored safely and is accessible from anywhere. The commit message helps keep track of changes.
:::


# Retrieving and Updating Notebooks from GitHub

- Open a **GitHub repository**.
- Click on the **notebook file (.ipynb)**.
- Click **Open in Colab** to edit.
- After modifications, **save back to GitHub**.

::: {.notes}
Once a notebook is stored on GitHub, you can easily access and edit it later. Simply open the notebook from GitHub and continue working in Colab. Be sure to save changes back to GitHub frequently.
:::


# Best Practices for Saving Notebooks

- Write **clear commit messages** (e.g., "Updated data analysis section").
- Regularly **push updates** to GitHub to prevent data loss.
- Use **branches** for experimental changes before merging into the main repository.
- Keep notebooks **organized** within folders in your repository.

::: {.notes}
Following best practices ensures that your notebooks remain well-documented and organized. Good commit messages help track progress, and using branches allows for safe experimentation without affecting the main codebase.
:::


# Troubleshooting Common Issues

# Common Issues and Fixes

- **Can't access Google Colab?** Check if you're logged into a Google Account.
- **Code not running?** Check for syntax errors in your Python code.
- **Authorization errors** – Ensure Google Colab has GitHub access.
- **Repository not showing?** – Refresh Colab or check GitHub permissions.
- **Failed to save?** – Check internet connection or re-authenticate.

::: {.notes}
Sometimes, you might face issues when using Google Colab. Make sure you're logged in, have given the necessary permissions to GitHub, and double-check your Python syntax if your code isn’t running correctly. Sometimes, saving to GitHub may encounter issues like authorization errors or conflicts. These can be fixed by refreshing Colab, verifying permissions, or using GitHub’s conflict resolution tools.
:::


# Hands-on Practice

- Save a sample notebook to GitHub.
- Retrieve and modify it from GitHub.
- Commit changes with a clear message.
- Open your updated notebook in Colab.

::: {.notes}
The best way to learn is by doing! Try saving a test notebook to GitHub, retrieving it, making changes, and committing updates. This will give you hands-on experience with version control in Google Colab.
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

::: {.notes}
Remember that AI is here to supplement your learning. Always review AI-generated code, test its functionality, and use it as a guide rather than a final solution.
:::

---
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
These practical examples demonstrate how AI can serve as a reliable assistant in your Python journey. Utilize these tools to explore different coding solutions, but always validate the output through your own testing and review.
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