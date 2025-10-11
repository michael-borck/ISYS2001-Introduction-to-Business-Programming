---

title: "Week 8 – Business Data Processing (CSV + Gradio Intro)"
author: "ISYS2001: Introduction to Business Programming"
format: pdf
-----------

# Week 8 – Business Data Processing (CSV + Gradio Intro)

## 🎯 Learning Goals (student-facing)

* Load and summarize transaction data from a CSV in Colab.
* Compare two approaches: `open()/csv` vs **Pandas**.
* Prompt an LLM effectively to generate/refine code (“vibe programming”).
* Document code with **docstrings** and comments.
* Validate results with simple manual checks (preview of testing).
* (Stretch) Wrap the summary in a tiny **Gradio** UI.
* Produce Week 8 **AI Evidence** + **meaningful GitHub commit** toward the final project.

---

## Pre-class (Flipped) – \~60 min

### Module 1 – CSVs & Data Ingestion Basics (10–15 min)

* **Concepts:** file uploads in Colab, CSV headers, rows/columns.
* **Demo (raw Python):**

  ```python
  import csv, io
  from google.colab import files

  uploaded = files.upload()
  fname = next(iter(uploaded))
  with io.StringIO(uploaded[fname].decode("utf-8")) as f:
      reader = csv.DictReader(f)
      amounts = [float(r["Amount"]) for r in reader]
  total, avg = sum(amounts), (sum(amounts)/len(amounts) if amounts else 0)
  print(total, avg)
  ```

### Module 2 – Pandas for Business CSVs (15–20 min)

* **Concepts:** `read_csv`, coercion, handling messy data.
* **Demo (Pandas):**

  ```python
  import pandas as pd
  uploaded = files.upload()
  fname = next(iter(uploaded))
  df = pd.read_csv(io.StringIO(uploaded[fname].decode("utf-8")))
  df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)
  summary = {
      "total": float(df["Amount"].sum()),
      "average": float(df["Amount"].mean()),
      "transactions": int(len(df))
  }
  summary
  ```

### Module 3 – Vibe Programming & Prompt Patterns (15–20 min)

* Teach **5 useful prompts**:

  1. “Given this CSV header and 3 rows, write minimal code to load and summarize totals/average.”
  2. “Rewrite using Pandas; handle missing/invalid amounts safely.”
  3. “Explain why my average is NaN and fix it.”
  4. “Wrap it in a tiny Gradio UI with a file uploader.”
  5. “Add comments and docstrings to explain this function.”
* Anti-prompt: “Before you answer, list assumptions about the CSV columns.”

### Module 4 – Validation & Documentation (10–15 min)

* **Concepts:** Validation = “sanity checks” (not formal testing yet).
* **Demo:**

  ```python
  print(summarize_csv_file("test_expenses.csv"))  # expect total=300, average=100
  ```
* Introduce **docstrings**:

  ```python
  def summarize_csv(file):
      """
      Summarize transactions from a CSV file.

      Args:
          file: Uploaded CSV with an 'Amount' column.
      Returns:
          A string with total and average values.
      """
      # code here
  ```
* Message: “From now on, **every function must include a docstring**.”

---

## In-class Workshop (2 hours)

### 0) Warm-up (5 min)

* Reframe: “AI is now your junior dev. Your job: specify, test, refine.”

### 1) Repo Setup (15–20 min)

* Students fork/create assignment repo from template.
* Open `starter_notebook.ipynb`, add provided `transactions.csv` sample.
* **Commit 1:** “Week 8: repo setup + sample CSV.”

### 2) Implement Ingestion & Summary (45–60 min)

* **Task A (raw Python):** load CSV with `csv.DictReader` → total + average.
* **Task B (Pandas):** re-do with `pd.read_csv` + coercion.
* Encourage prompting AI with headers + rows.

### 3) Stretch – Gradio App (15–20 min)

```python
import gradio as gr, pandas as pd

def summarize(file):
    df = pd.read_csv(file.name)
    df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce").fillna(0)
    return {
        "transactions": int(len(df)),
        "total": float(df["Amount"].sum()),
        "average": float(df["Amount"].mean())
    }

gr.Interface(fn=summarize, inputs=gr.File(), outputs="json").launch()
```

### 4) Validation & Documentation (10–15 min)

* Students run manual checks (expected totals/averages).
* Add docstrings + inline comments.
* (Optional preview): show one `assert()` but say “formal testing comes later.”

### 5) Evidence & Commit (10 min)

* Add Week 8 **AI Evidence entry** to diary.
* **Commit 2:** “Week 8: CSV ingestion + summary (+ Gradio optional).”

---

## Exit Ticket (Assignment Progress)

Students pass if they show:

* Notebook loads CSV and prints **totals + averages**.
* Code includes **docstrings and comments**.
* At least one manual validation check.
* One AI Evidence entry in Developer’s Diary.
* Repo has Week 8 commit(s).

---

## Instructor Notes

* Why show both raw + Pandas? → clarifies what Pandas abstracts.
* Why validation, not `assert()`? → builds habit gently; formal testing waits for Week 12.
* Why docstrings now? → aligns with Clarity & Reflection rubric, AI can scaffold them easily.

---
