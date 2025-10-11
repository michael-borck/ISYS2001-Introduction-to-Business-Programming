---
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

# 🧠 Learning from Mistakes: Debugging with AI Tools

## 📘 Background

During the development of a starter notebook for our Smart Finance Assistant project, an accidental error was introduced in the code. Althuhg I have since corrected the code, I decided to turn it into a **teaching moment** to show how students can use AI tools to **diagnose**, **understand**, and **fix** issues in their code.

This handout walks through the problem-solving process using Microsoft Copilot and the `hands-on-ai` package. It demonstrates how to craft prompts, use documentation, and interpret feedback from AI tools.

---

## 🧭 Strategy: Turning Errors into Learning

We approached the problem as a beginner might:

- **Step 1**: Write a simple prompt describing the issue (without a traceback).
- **Step 2**: Paste the code snippet.
- **Step 3**: Upload the `LLM.txt` file from the `hands-on-ai` package (provided in the starter repo).
- **Step 4**: Ask Copilot to help identify the issue and suggest a fix.

This simulates a realistic student workflow and encourages exploration and self-directed learning.

---

## 🧩 The Problem

Here’s the original code that caused the error:

```python
from hands_on_ai import chat 

# Test the connection to the hands-on-ai server
try:
    response = chat.say("Hello! I'm building a Smart Finance Assistant.")
    print("✅ Hands-on-AI connection successful!")
    print(f"Response: {response}")
except Exception as e:
    print(f"❌ Connection issue: {e}")
    print("You can still work on the data processing foundation without this.")
```

The error message indicated that the `say` function does not exist.

---

## 💬 Conversation with Copilot

### 🧠 Step 1: Ask for Help

> I get an error with the following code, think it says the 'say' function doesn't exist. Please read LLM.txt and let me know what’s wrong with the code and suggest a fix.

### 🤖 Copilot's Response

Thanks for sharing the code and the reference guide. Based on the contents of `LLM.txt`, here's what's going wrong and how to fix it:

---

### ❌ **Issue in Your Code**

You're using:

```python
response = chat.say("Hello! I'm building a Smart Finance Assistant.")
```

But according to the documentation in `LLM.txt`, the `chat` module **does not have a `say` function**.

---

### ✅ **Correct Usage**

You should use the `get_response` function from `hands_on_ai.chat`, like this:

```python
from hands_on_ai.chat import get_response

# Test the connection to the hands-on-ai server
try:
    response = get_response("Hello! I'm building a Smart Finance Assistant.")
    print("✅ Hands-on-AI connection successful!")
    print(f"Response: {response}")
except Exception as e:
    print(f"❌ Connection issue: {e}")
    print("You can still work on the data processing foundation without this.")
```

---

### 🔧 Optional Enhancements

You can also customize the system prompt or personality:

```python
response = get_response(
    "Hello! I'm building a Smart Finance Assistant.",
    system="You are a financial advisor. Help users make smart money decisions.",
    personality="friendly"
)
```

---

### 🤝 Follow-up Request

> Are you able to convert this conversation into a handout for the students?

---

## 🎓 Conclusion & Observations

This exercise highlights several key lessons:

- **Documentation matters**: Uploading and referencing `LLM.txt` helped Copilot give an accurate answer.
- **Prompt quality affects results**: A beginner-style prompt worked, but including the traceback would have helped Copilot diagnose faster.
- **AI is a learning partner**: Copilot didn’t just fix the code—it explained why the fix works and offered enhancements.

---

## 🛠️ Tips for Better Prompts

- Include **error messages or tracebacks** when possible.
- Mention the **source of your code or documentation**.
- Be clear about what you’ve tried and what you’re trying to achieve.

---

## 📎 Appendix: Reference Fix

```python
from hands_on_ai.chat import get_response

try:
    response = get_response("Hello! I'm building a Smart Finance Assistant.")
    print("✅ Hands-on-AI connection successful!")
    print(f"Response: {response}")
except Exception as e:
    print(f"❌ Connection issue: {e}")
    print("You can still work on the data processing foundation without this.")
```

---
