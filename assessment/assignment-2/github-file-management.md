## Handout: Managing Files in Your GitHub Repository via the Web Interface

This handout will guide you through performing common file operations directly on the GitHub website. This is useful for organizing your project files, especially when working with Google Colab notebooks that are stored in your GitHub repositories. You won't need to install Git or use any command-line tools.

**Accessing Your Repository:**

1.  Go to [https://github.com](https://github.com) and log in to your account.
2.  Navigate to the repository you want to work with by clicking on its name on your dashboard or your profile page.

---

### 1. Uploading Files

You can upload various file types to your GitHub repository, such as Python scripts (`.py`), data files (`.csv`, `.txt`, `.json`), images, or other project-related documents.

**Steps:**

1.  Once you are in your repository, click on the **"Add file"** button located above the list of files.
2.  From the dropdown menu, select **"Upload files"**.
3.  You can then either:
    * **Drag and drop** your file(s) into the box provided.
    * Click on **"choose your files"** to open a file dialog and select the file(s) from your computer.
4.  After the files have been uploaded, you will see them listed.
5.  Scroll down to the **"Commit changes"** section.
    * In the first text box, provide a brief, meaningful message describing the upload (e.g., "Upload dataset for analysis", "Add utility script"). This is a commit message.
    * You can add a more detailed description in the larger text box below if needed (optional for simple uploads).
6.  Ensure that **"Commit directly to the `main` branch"** is selected (or your default branch, usually `main` or `master`). For beginner purposes, this is the standard workflow.
7.  Click the green **"Commit changes"** button. Your files are now in your repository.

---

### 2. Creating a New Folder (and adding a file to it)

GitHub doesn't allow you to create an empty folder directly. A folder is created automatically when you add a file within it.

**Steps:**

1.  In your repository, click on the **"Add file"** button.
2.  From the dropdown menu, select **"Create new file"**.
3.  In the **"Name your file..."** box at the top, type the name of your desired folder followed by a forward slash `/`. For example, to create a folder named "data", you would type `data/`.
4.  **Important:** After the `/`, you must then type a filename for a new file that will reside within this folder. GitHub requires at least one file to create a folder. Often, people create a placeholder file like `.gitkeep` (an empty file that signals the folder should be tracked) or `README.md` (if you want to describe the folder's contents). For example: `data/.gitkeep` or `data/notes.txt`.
5.  If you are creating a file like `notes.txt`, you can add some content to it in the editing area below. If you are creating a `.gitkeep` file, you can leave the content area blank.
6.  Scroll down to the **"Commit new file"** section.
    * Provide a commit message (e.g., "Create data folder", "Add initial notes for data folder").
7.  Ensure **"Commit directly to the `main` branch"** is selected.
8.  Click the green **"Commit new file"** button. You will now see your new folder in the repository.

---

### 3. Renaming a File

**Steps:**

1.  Navigate to the file you want to rename within your repository.
2.  Click on the filename to open the file view.
3.  On the right side of the file view, above the file content, you will see a set of icons. Click the **pencil icon (Edit this file)**.
4.  At the top of the page, where the filename is displayed, you can now edit the filename directly in the text box. Change it to the new desired name.
5.  Scroll down to the **"Commit changes"** section.
    * GitHub will usually pre-fill a commit message like "Rename [old filename] to [new filename]". You can customize this if needed.
6.  Ensure **"Commit directly to the `main` branch"** is selected.
7.  Click the green **"Commit changes"** button.

---

### 4. Moving a File into a Folder

Moving a file in GitHub's web interface is essentially renaming the file to include the new folder path.

**Steps:**

1.  Navigate to the file you want to move.
2.  Click on the filename to open the file view.
3.  Click the **pencil icon (Edit this file)** on the right side.
4.  In the filename box at the top, you will edit the file's path.
    * To move `myfile.txt` into an existing folder called `documents`, you would change the filename from `myfile.txt` to `documents/myfile.txt`.
    * If the folder doesn't exist yet, typing `newfolder/myfile.txt` will create `newfolder` and place `myfile.txt` inside it.
5.  Scroll down to the **"Commit changes"** section.
    * Provide a commit message (e.g., "Move script to utilities folder", "Organize data files").
6.  Ensure **"Commit directly to the `main` branch"** is selected.
7.  Click the green **"Commit changes"** button.

**Tip:** If you want to move a file "up" one level (out of a folder), you would delete the folder prefix from its name. For example, to move `data/report.txt` to the main (root) directory, you would rename it from `data/report.txt` to `report.txt`.

---

### 5. Deleting a File

**Steps:**

1.  Navigate to the file you want to delete within your repository.
2.  Click on the filename to open the file view.
3.  On the right side of the file view, above the file content, click the **trash can icon (Delete this file)**.
4.  Scroll down to the **"Commit changes"** section.
    * GitHub will pre-fill a commit message like "Delete [filename]". You can customize this.
5.  Ensure **"Commit directly to the `main` branch"** is selected.
6.  Click the green **"Commit changes"** button.

---

### 6. Deleting a Folder

Similar to creating folders, you can't directly delete a folder if it still contains files using a single "delete folder" button. You must first delete or move all files out of the folder. Once a folder becomes empty, GitHub automatically removes it from the repository view.

**Steps:**

1.  Navigate into the folder you wish to delete.
2.  Individually **delete** each file within that folder using the "Deleting a File" steps outlined above.
3.  Once all files within the folder have been deleted, the folder itself will disappear from your repository.

---

### Important Note on "Open in Colab" Buttons

If you have "Open in Colab" buttons in your README files or notebooks, remember that these buttons link to a specific file path in your GitHub repository.

* **If you rename or move a notebook file (`.ipynb`)**, the old "Open in Colab" link will no longer work. You will need to update the link to reflect the new file path. The general format for an "Open in Colab" link is:
    `https://colab.research.google.com/github/YOUR_USERNAME/YOUR_REPOSITORY_NAME/blob/main/PATH_TO_YOUR_NOTEBOOK.ipynb`
    Make sure the `PATH_TO_YOUR_NOTEBOOK.ipynb` part is correct after renaming or moving.

---

**General Tips for GitHub File Management:**

* **Commit Messages are Important:** Always write clear and concise commit messages. This helps you (and others) understand the changes made to the repository over time. Think of it as a logbook for your project.
* **Organize Early, Organize Often:** It's easier to keep your repository tidy if you create a good folder structure early on and stick to it.
* **README Files:** It's good practice to have a `README.md` file in your main repository directory and potentially in sub-folders. This file can explain what the project is about, how to use the files, or what the contents of a specific folder are. You can edit `.md` files directly on GitHub using the pencil icon.

By following these steps, you can effectively manage your project files directly on GitHub without needing to use local Git tools. This will help keep your repositories organized and your Colab notebooks easily accessible.