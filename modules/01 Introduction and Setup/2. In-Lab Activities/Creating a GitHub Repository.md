---
title: "GitHub Repository Setup Guide for Python Course"
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


## **Step 1: Create a GitHub Repository**
1. **Go to GitHub**: [https://github.com](https://github.com) and log in.
2. Click the **"+" (plus icon)** at the top-right and select **"New repository"**.
3. **Repository Name**: Choose a meaningful name, e.g., `python-beginners-course`.
4. **Description** (Optional): "This repository contains materials for the beginner's Python course."
5. **Visibility**:
   - Public (if you want anyone to access it).
   - Private (if it's for enrolled students only).
6. **Initialize the repository**:
   - Check **"Add a README file"** (recommended for an overview).
   - Check **".gitignore"** and select **"Python"** (prevents unnecessary files from being tracked).
7. Click **"Create repository"**.

---

## **Step 2: Clone the Repository (For Local Use)**
(If students want to work locally before pushing to GitHub)

1. **Copy the Repository URL**: On the repository page, click the **"Code"** button and copy the HTTPS or SSH link.
2. **Open Terminal or Git Bash** (on Windows/Mac/Linux).
3. Run:
   ```bash
   git clone <repository_url>
   cd python-beginners-course
   ```

---

## **Step 3: Connect Google Colab to GitHub**
1. **Open Google Colab**: [https://colab.research.google.com](https://colab.research.google.com/)
2. **Sign in** with your Google account.
3. Click **"File" > "Open Notebook"**.
4. Select the **GitHub tab** and authorize Colab to access your GitHub account.
5. Choose the repository and the notebook file you want to work on.
6. Click **"Open"** to start editing.

---

## **Step 4: Save Colab Notebooks to GitHub**
1. In Google Colab, after making changes, go to:
   - **File > Save a copy in GitHub**.
2. Select the correct repository and branch.
3. Add a commit message (e.g., "Added loops lesson").
4. Click **OK** to push the changes.

---

## **Step 5: Commit & Push Changes (Command Line)**
(For those who cloned the repository and made local changes)

1. Open Terminal or Git Bash in the repo folder.
2. Add files to staging:
   ```bash
   git add .
   ```
3. Commit changes with a message:
   ```bash
   git commit -m "Added week 1 exercises"
   ```
4. Push changes to GitHub:
   ```bash
   git push origin main
   ```

---

## **Step 6: Pull Changes (To Sync with the Latest Version)**
If changes were made remotely (e.g., by the instructor), students should **pull** updates before making new edits:

```bash
git pull origin main
```

---

## **Bonus: Create Student Submission Folders (Optional)**
If students are required to submit assignments:
- **Option 1**: Each student forks the main repo and submits a pull request.
- **Option 2**: Create a `submissions/` folder where students upload their `.ipynb` files.

---

### ✅ **Now your GitHub repository is ready for use with Google Colab!**  
