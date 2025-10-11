---
title: "When Things Go Wrong: Debugging Network Issues with AI"
subtitle: "Learning to Spot Problems and Use AI to Fix Them"
author: "Michael Borck"
format: 
  pptx:
    reference-doc: curtin_template.pptx
  html:
    theme: 
      - cosmo
      - custom.scss
    toc: true
    toc-expand: 2
    code-fold: true
    embed-resources: true
    fig-cap-location: bottom
    css: module-styles.css
  pdf:
    toc: false
    colorlinks: true
    geometry:
      - top=30mm
      - left=20mm
  docx:
    highlight-style: github
    toc: false
---

# The Reality of Working with Internet Data

* Things will go wrong - and that's normal!
* Learning to recognize when something's broken
* Using AI as your debugging partner
* Building confidence through problem-solving

::: {.notes}
Welcome to the reality of programming with internet data! Here's the truth: things will break, APIs will be down, your internet will hiccup, and you'll see error messages. This isn't a sign you're doing something wrong - it's just part of working with live data from the internet. Today we'll learn to recognize common problems and, more importantly, how to use AI tools to diagnose and fix them quickly. This skill will make you a confident programmer who can tackle real-world data challenges.
:::

# What Can Go Wrong? Common Scenarios

* **The API is down** - "It worked yesterday!"
* **Slow internet** - Your code just hangs forever
* **Wrong URL or API key** - Permission denied messages
* **Rate limits** - "Too many requests" errors
* **Bad data format** - When the API returns something unexpected

::: {.notes}
Let's start by understanding what typically goes wrong when working with internet data. APIs can go offline for maintenance, your internet connection might be slow, you might have typos in URLs or API keys, many APIs limit how often you can call them, and sometimes the data format changes unexpectedly. Recognizing these patterns helps you quickly identify what type of problem you're facing, which makes it much easier to fix.
:::

# Recognizing Error Messages

* **Connection errors**: "ConnectionError", "Failed to resolve"
* **Timeout errors**: "ReadTimeout", "took too long"
* **Permission errors**: "401 Unauthorized", "403 Forbidden"  
* **Not found errors**: "404 Not Found"
* **Rate limit errors**: "429 Too Many Requests"

::: {.notes}
Error messages might look scary, but they're actually helpful clues about what went wrong. Connection errors usually mean network problems or the server is down. Timeout errors happen when things take too long - maybe slow internet or an overloaded server. Permission errors (401, 403) often mean API key problems. 404 means the URL is wrong. 429 means you're making requests too quickly. Learning to recognize these patterns helps you quickly understand what type of fix you need.
:::

# Your AI Debugging Toolkit

When something breaks, ask AI:

* **"I got this error message: [paste the error]. What went wrong and how do I fix it?"**
* **"This code worked yesterday but not today. What might have changed?"**
* **"Help me check if this API is working: [paste your code]"**
* **"My code is running but never finishing. What could be wrong?"**

::: {.notes}
AI is incredibly good at diagnosing common programming problems, especially network issues. The key is providing good information in your questions. Always paste the actual error message - don't try to describe it. If something worked before but doesn't now, mention that. If your code seems to hang forever, that's a specific type of problem (usually timeouts). The more specific your question, the better help you'll get from AI.
:::

# Hands-On: Breaking Things on Purpose

Let's intentionally create problems and fix them:

```python
import requests

# This will fail - wrong URL
response = requests.get('https://api.wrong-url.com/data')
print(response.json())

# This will timeout - taking too long
response = requests.get('https://httpbin.org/delay/30')
print(response.json())

# This needs an API key but we didn't provide one
response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=London')
print(response.json())
```

::: {.notes}
The best way to learn debugging is to break things intentionally and then fix them. This code snippet shows three common failure scenarios. The first uses a fake URL that doesn't exist. The second tries to connect to a service that deliberately delays responses for 30 seconds - most systems will timeout before then. The third tries to access a weather API without providing the required API key. Run these examples, see what error messages you get, then practice asking AI to help you fix them.
:::

# AI Prompt Patterns for Network Debugging

**🔍 Understanding What Happened:**
"Explain this error message in simple terms: [error]"

**🚨 Quick Fix:**
"How do I fix this network error: [error message]"

**🛠️ Prevention:**
"How can I make this code more reliable: [paste code]"

**✅ Health Check:**
"Help me test if this API is working: [API URL]"

::: {.notes}
Having a toolkit of prompt patterns makes debugging much faster. Use the understanding pattern when you want to learn what an error means. The quick fix pattern is for when you just need to get things working again. The prevention pattern helps you write more robust code. The health check pattern is useful for testing if an API or service is working properly. Save these patterns - you'll use them constantly when working with real-world data.
:::

# Common Solutions AI Will Suggest

* **Adding timeouts**: Don't wait forever for slow responses
* **Checking status codes**: Making sure the request succeeded
* **Using different URLs**: Sometimes APIs change endpoints
* **Adding delays**: Respecting rate limits
* **Validating data**: Checking if the response looks right

::: {.notes}
When you ask AI for help with network issues, you'll commonly see these types of solutions. Timeouts prevent your code from hanging forever. Status code checking helps you handle different types of responses appropriately. APIs sometimes change their URLs, so AI might suggest alternatives. Adding delays between requests helps avoid rate limits. Data validation catches cases where the API returns something unexpected. Understanding these common patterns helps you recognize good advice when AI suggests it.
:::

# Building Robust Code with AI Assistance

Ask AI: **"Make this code more reliable for real-world use"**

```python
# Your simple code
import requests
response = requests.get('https://api.example.com/data')
data = response.json()
print(data)
```

AI will likely suggest improvements like timeouts, status checking, and handling missing data.

::: {.notes}
This is where AI really shines - taking your working but basic code and making it production-ready. Start with simple code that works in ideal conditions, then ask AI to make it more robust. You'll learn about timeouts, error checking, retry logic, and graceful degradation. This approach lets you focus on solving your main problem first, then use AI to handle the edge cases and error conditions.
:::

# Debugging Workflow: Your Step-by-Step Process

1. **Run your code** - See what happens
2. **Copy the error message** - Exact text, not paraphrased  
3. **Ask AI** - "I got this error: [paste error]. What's wrong?"
4. **Try the fix** - Apply AI's suggestion
5. **If still broken** - Ask "This fix didn't work. What else could it be?"
6. **Learn the pattern** - Understand why this happened

::: {.notes}
Having a systematic debugging process makes you much more effective. Don't panic when you see errors - they're just information. Always copy the exact error message rather than trying to describe it. AI is very good at recognizing specific error patterns. If the first suggestion doesn't work, keep asking - there might be multiple issues. Most importantly, try to understand why the problem happened so you can recognize similar issues in the future.
:::

# Real-World Example: Weather API Debugging

Let's debug a weather API call together:

```python
import requests

# Let's see what goes wrong and fix it with AI
url = "http://api.openweathermap.org/data/2.5/weather"
params = {"q": "Perth", "appid": "your_api_key_here"}
response = requests.get(url, params=params)
print(response.json())
```

**Practice:** Run this, get the error, then ask AI how to fix it!

::: {.notes}
This example demonstrates a typical real-world scenario. The code looks right but will fail because you need a real API key from OpenWeatherMap. This gives us a perfect opportunity to practice the debugging workflow: run the code, see the error message (probably 401 Unauthorized), copy that exact message, and ask AI for help. AI will explain that you need to sign up for an API key and show you how to get one. This is exactly how you'll work with APIs in the real world.
:::

# When to Ask for Help vs. When to Investigate

**Ask AI immediately for:**
* Error messages you don't understand
* Code that hangs or crashes
* "It worked yesterday" problems
* Rate limiting issues

**Investigate first:**
* Typos in your code
* Missing imports
* Basic syntax errors

::: {.notes}
Learning when to use AI versus when to check your own work is an important skill. For network-related errors, weird error messages, or mysterious failures, AI is usually your best first step. But for basic coding errors like typos or forgotten imports, quickly scanning your code yourself is often faster. As you gain experience, you'll develop intuition about which problems are worth investigating yourself versus immediately asking for AI assistance.
:::

# Testing Your Understanding

**Scenario:** Your code to get stock prices worked fine last week, but today it just sits there doing nothing (no error, no output).

**What do you think happened?**
**What would you ask AI?**
**What type of solution would you expect?**

::: {.notes}
This scenario tests your understanding of common network issues. A program that hangs without errors or output typically indicates a timeout issue - the API might be slow or unresponsive. You should ask AI something like "My code hangs without any error message when trying to get stock prices. It worked last week. What could be wrong?" You'd expect AI to suggest adding timeout parameters, checking if the API is down, or looking for changes in the API endpoint. This type of reasoning helps you become a more effective debugger.
:::

# Building Confidence Through Problem-Solving

* **Every error is a learning opportunity**
* **AI makes you a more capable programmer**
* **Focus on understanding, not memorizing**
* **The goal: solve real problems with real data**

::: {.notes}
The key message here is building confidence. Programming with internet data means dealing with uncertainty and problems, but that's also what makes it exciting and valuable. Every error you encounter and fix makes you more capable. AI doesn't replace your thinking - it amplifies your problem-solving abilities. Focus on understanding the patterns and concepts rather than memorizing specific syntax. The ultimate goal is solving real business problems with real data, and being comfortable with debugging is essential for that.
:::

# Your Action Plan for This Week

1. **Try the weather API example** - Experience the debugging process
2. **Intentionally break something** - Practice recognizing errors  
3. **Ask AI for help** - Build comfort with the debugging workflow
4. **Keep a "lessons learned" list** - Track common problems and solutions

::: {.notes}
Here's your practical homework for putting these concepts into practice. Start with the weather API example to get hands-on experience with the debugging process. Then deliberately create some errors to practice recognizing different types of problems. Most importantly, get comfortable asking AI for help - it's a skill that improves with practice. Keep notes about what you learn so you can build your own debugging knowledge base over time.
:::

# Resources and Next Steps

* **Bookmark error lookup sites**: StackOverflow, Python docs
* **Practice with different APIs**: Weather, news, social media
* **Join communities**: Reddit r/learnpython, Python Discord
* **Remember**: Every expert was once a beginner who kept debugging!

::: {.notes}
Building your debugging skills is an ongoing process. Bookmark resources like StackOverflow where you can see how other people solve similar problems. Practice with various APIs to encounter different types of errors and solutions. Join programming communities where you can ask questions and learn from others. Most importantly, remember that debugging is a core skill for all programmers - every expert developer spent lots of time figuring out why their code wasn't working. You're building essential professional skills, not just learning syntax.
:::

# Questions and Debugging Practice

* **Share your error messages** - Let's debug together!
* **Discuss debugging strategies** - What works for you?
* **Plan your API projects** - What data interests you?

::: {.notes}
This final slide encourages active participation and community learning. Invite students to share actual error messages they've encountered so the class can practice the debugging workflow together. Discuss different approaches to problem-solving and let students learn from each other's strategies. Most importantly, help them connect debugging skills to their own interests by discussing what APIs and data sources they want to work with. This connects the technical skills to their personal motivation and curiosity.
:::
