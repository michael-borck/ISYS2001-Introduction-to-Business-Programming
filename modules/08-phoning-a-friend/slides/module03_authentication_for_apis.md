---
title: "Securing API Access: A Beginner's Guide with AI Support"
subtitle: "Understanding Authentication Mechanisms for Web APIs"
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


# Introduction to API Security

* Importance of securing APIs
* Overview of authentication and authorisation
* Using AI to understand and implement security
* What you'll learn in this presentation

::: {.notes}
Welcome to our session on securing API access! As APIs become a critical part of web and mobile applications, ensuring that these interfaces are secure is paramount. This presentation will explore the fundamental concepts of authentication and authorisation, focusing on how they help protect data and systems from unauthorised access. We'll also learn how to use AI tools to help understand, implement, and troubleshoot API security. By the end, you'll understand the various mechanisms available to secure API access and how to leverage AI assistance to implement them effectively.
:::

# What is an API?

* Definition of API (Application Programming Interface)
* Role of APIs in modern software
* Examples of API usage
* **AI Prompt**: "Explain APIs like I'm a business student - use real examples"

::: {.notes}
API stands for Application Programming Interface, a set of rules that allows different software entities to communicate with each other. APIs play a crucial role in modern software development by enabling applications to interact seamlessly, whether retrieving data from a server or sending data to be processed. Common examples include pulling real-time data from weather services or integrating with social media platforms to post updates directly from an app. If you need clearer explanations, try asking AI to explain APIs using business examples you're familiar with.
:::

# Why Secure an API?

* Protect sensitive data
* Ensure data integrity
* Prevent unauthorised access
* **Real-world impact**: Data breaches, financial losses, privacy violations

::: {.notes}
Securing an API is essential for several reasons. Primarily, it helps protect sensitive data from being exposed to unauthorised users. Furthermore, security measures ensure the integrity of the data being exchanged, preventing malicious actors from altering it. Lastly, robust security prevents unauthorised access, ensuring that only legitimate users can interact with the API, thus maintaining the overall system's reliability and trustworthiness. Understanding these risks helps you appreciate why API security isn't optional - it's essential for any business application.
:::

# Basic Authentication

* Simplest form of API authentication
* Utilises a username and password
* Suitable for less critical data
* **AI Helper**: "Show me how basic authentication works in Python with the requests library"

::: {.notes}
Basic Authentication is the simplest form of securing an API. It works by sending a username and password with each API request, usually encoded in Base64. While this method is easy to implement, it is less secure compared to other methods and is generally recommended for scenarios where security demands are lower, such as accessing non-sensitive data. When you need to implement basic authentication, AI can provide you with clean, working code examples and explain exactly how the encoding process works.
:::

# Token-Based Authentication

* More secure than basic authentication
* Uses access tokens
* Example: OAuth 2.0
* **Common use case**: Social media APIs, cloud services

::: {.notes}
Token-based authentication is a more secure alternative to basic authentication. In this method, the user first logs in using their credentials to receive a token. This token is then used for subsequent requests to the API. OAuth 2.0 is a popular framework that utilises tokens, providing robust security for accessing resources. This method is widely used due to its scalability and security features, especially in applications that require handling sensitive data. You'll see this pattern everywhere - from accessing Google APIs to connecting with social media platforms.
:::

# API Keys: Simple but Powerful

* Simple way to control access
* Unique to each user or application
* **Critical limitations**: potential for leakage, no expiration
* **AI Prompt**: "Explain API key security best practices and show me how to use them safely"

::: {.notes}
API keys are another common method for authenticating API requests. Each key is unique to a user or application and is included in the request to authenticate the user. While API keys are simple to use and implement, they must be kept secure. If an API key is leaked, it can provide an attacker access to the API, potentially leading to data breaches. This is where AI can be particularly helpful - it can show you secure ways to store and use API keys, and warn you about common security mistakes.
:::

# Hands-On: Working with API Keys

Ask AI to help you with:
* **"How do I safely store API keys in my Python project?"**
* **"Show me how to use environment variables for API keys"**
* **"What are the signs that my API key might be compromised?"**

```python
# AI will likely suggest something like this:
import os
import requests

api_key = os.getenv('WEATHER_API_KEY')
url = f"http://api.openweathermap.org/data/2.5/weather?q=Perth&appid={api_key}"
```

::: {.notes}
This is where AI really shines in helping with API security. Instead of memorizing security patterns, you can ask AI to show you the current best practices. AI will typically suggest using environment variables to keep keys out of your code, show you how to set them up, and explain why this approach is more secure. It can also help you recognize security problems in existing code and suggest improvements.
:::

# Understanding Authentication Errors

Common error messages and what they mean:
* **401 Unauthorized**: Wrong or missing credentials
* **403 Forbidden**: Valid credentials but insufficient permissions  
* **429 Too Many Requests**: Rate limiting in effect

**AI Debugging Prompt**: "I got a 401 error when calling this API: [paste your code]. What's wrong with my authentication?"

::: {.notes}
Authentication errors are some of the most common issues you'll face when working with APIs. Learning to recognize these error codes helps you quickly diagnose problems. 401 usually means your API key is wrong or missing. 403 means your key works but doesn't have permission for what you're trying to do. 429 means you're making too many requests too quickly. When you encounter these errors, AI can quickly help you understand what went wrong and how to fix it.
:::

# AI-Assisted Security Review

Use AI to review your code security:

**Prompt**: "Review this API code for security issues and suggest improvements:"

```python
# Your code here
api_key = "sk-1234567890abcdef"  # This is bad!
url = f"https://api.example.com/data?key={api_key}"
response = requests.get(url)
```

AI will flag the hardcoded API key and suggest better practices.

::: {.notes}
One of the most powerful ways to use AI for security is having it review your code for common vulnerabilities. AI can quickly spot hardcoded API keys, insecure transmission methods, and other security anti-patterns. It's like having a security expert looking over your shoulder, pointing out issues you might miss. This is especially valuable for beginners who might not yet recognize all the ways security can go wrong.
:::

# Best Practices for API Security

* Use HTTPS for secure communication
* Regularly rotate and manage credentials  
* Implement rate limiting to prevent abuse
* **AI Support**: "What security checklist should I follow when working with APIs?"

::: {.notes}
To enhance API security, it is crucial to follow best practices. Always use HTTPS to encrypt data transmitted between the client and the server, ensuring that sensitive information is protected from interceptors. Regularly rotating and managing credentials, such as passwords and API keys, helps mitigate the risk of unauthorised access. Additionally, implementing rate limiting on your API can prevent abuse and help manage the load on your infrastructure. AI can provide you with comprehensive security checklists and help you understand why each practice matters.
:::

# Real-World Scenario: Social Media API

Let's work through authenticating with a social media API:

**Challenge**: Connect to Twitter/X API to get trending topics
**AI Prompts to try**:
* "How do I get Twitter API credentials?"
* "Show me Python code to authenticate with Twitter API"  
* "What permissions do I need for reading trending topics?"

::: {.notes}
Working with real APIs like Twitter's gives you practical experience with OAuth authentication flows. This is more complex than simple API keys, involving multiple steps and token exchanges. Rather than trying to memorize the OAuth process, use AI to guide you through it step by step. AI can explain the authentication flow, help you set up your credentials, and provide working code examples. This approach lets you focus on understanding the concepts while AI handles the implementation details.
:::

# Building Your AI Prompt Library

Save these patterns for API security work:

**🔐 Understanding**: "Explain [authentication method] in simple terms with examples"
**🛠️ Implementation**: "Show me how to [authentication task] in Python"  
**🚨 Debugging**: "I got this authentication error: [error message]. How do I fix it?"
**✅ Security Review**: "Check this code for API security issues: [code]"

::: {.notes}
Building a collection of proven prompt patterns makes you much more efficient when working with API security. These four categories cover most situations you'll encounter: understanding new concepts, implementing authentication, debugging problems, and reviewing code for security issues. Save these patterns and customize them for your specific needs. Over time, you'll develop your own variations that work well for your learning style and the types of projects you work on.
:::

# Common Security Mistakes (and How AI Helps Avoid Them)

* **Hardcoding API keys** - AI: "Never put keys directly in code"
* **Using HTTP instead of HTTPS** - AI: "Always use secure connections"  
* **Sharing keys in public repos** - AI: "Use .gitignore for sensitive files"
* **Not rotating expired keys** - AI: "Set up key rotation reminders"

::: {.notes}
These are the most common security mistakes beginners make with APIs. The good news is that AI is excellent at catching these issues and explaining why they're problematic. When you ask AI to review your code, it will consistently flag these patterns and suggest better approaches. This means you can learn secure practices from the start rather than having to unlearn bad habits later. AI serves as your security mentor, helping you develop good practices naturally.
:::

# Testing Your Understanding

**Scenario**: You're building a weather app for your business. You need to:
* Get weather data from OpenWeatherMap API
* Keep your API key secure
* Handle authentication errors gracefully

**What AI prompts would you use to solve this step by step?**

::: {.notes}
This scenario tests your ability to break down a real problem into AI-assistable chunks. You might ask: "How do I get an OpenWeatherMap API key?", "Show me secure ways to store API keys in Python", "How do I make authenticated requests to OpenWeatherMap?", and "What authentication errors should I handle for weather APIs?" This type of problem decomposition is a key skill for working effectively with AI - breaking complex tasks into specific, answerable questions.
:::

# When Authentication Goes Wrong

**Debugging with AI workflow**:
1. **Copy the exact error message**
2. **Ask**: "I got this authentication error: [error]. What does it mean?"
3. **Share your code**: "Here's my authentication code: [code]. What's wrong?"
4. **Test the fix**: Apply AI's suggestions
5. **Verify security**: "Is this authentication approach secure?"

::: {.notes}
Authentication problems are common but usually straightforward to fix with AI assistance. The key is providing good information: exact error messages and the specific code that's causing issues. AI can quickly identify whether you have a credential problem, a permission issue, or a code structure problem. Always follow up by asking AI to verify that your fix is also secure - sometimes a quick fix might work but introduce security vulnerabilities.
:::

# Beyond Basic Authentication

**Advanced topics to explore with AI**:
* JWT (JSON Web Tokens) for stateless authentication
* Multi-factor authentication for sensitive APIs
* Role-based access control
* **AI Learning Prompt**: "Explain JWT authentication like I'm a business student, with pros and cons"

::: {.notes}
Once you're comfortable with basic authentication methods, AI can help you explore more advanced concepts. JWT tokens are becoming very common for modern APIs. Multi-factor authentication adds extra security layers. Role-based access control helps manage different permission levels. The key is using AI to learn these concepts progressively - start with understanding what they are and why they matter, then move to implementation when you need them for specific projects.
:::

# Conclusion

* API security is essential, not optional
* AI makes security implementation accessible to beginners
* Focus on understanding concepts, let AI handle implementation details
* Build your prompt library for common security tasks
* **Remember**: Security is an ongoing process, not a one-time setup

::: {.notes}
We've covered the critical aspects of API security and demonstrated how AI can make these concepts accessible even for beginners. The key insight is that you don't need to memorize all the security implementation details - you need to understand the concepts and know how to leverage AI for secure implementation. API security isn't something you set up once and forget; it's an ongoing process of reviewing, updating, and improving your security practices. AI can be your partner throughout this journey.
:::

# Your Security Action Plan

1. **Practice with a real API** - Try the OpenWeatherMap example
2. **Build your prompt collection** - Save patterns that work for you
3. **Review existing code** - Ask AI to check any API code you've written
4. **Stay curious** - Ask AI about security concepts you encounter

::: {.notes}
Here's your practical homework for building API security skills. Start with a real but safe API like OpenWeatherMap to practice authentication flows. Build your own collection of AI prompts that work well for your learning style. If you have existing API code, ask AI to review it for security issues - you might be surprised by what it finds. Most importantly, stay curious about security concepts you encounter in documentation or discussions, and use AI to deepen your understanding.
:::

# Further Resources

* [Python Requests Library Documentation](https://requests.readthedocs.io/en/latest/)
* [Understanding APIs for Beginners](https://www.smashingmagazine.com/2018/01/understanding-using-rest-api/)
* [OAuth 2.0 Authorization Framework](https://oauth.net/2/)
* **AI Prompt**: "Create a learning plan for API security based on my current Python knowledge"

::: {.notes}
For those interested in diving deeper into API security or needing specific guidance on implementing these concepts in Python, these resources will be invaluable. They provide detailed documentation and tutorials that can help you better understand and implement secure API strategies in your projects. Additionally, consider asking AI to create a personalized learning plan based on your current knowledge level and specific interests - this can help you progress systematically through more advanced security topics.
:::

# Questions and AI Experimentation

* **Share your authentication challenges** - Let's solve them together!
* **Discuss AI prompt strategies** - What works best for learning?
* **Plan your secure API projects** - What data do you want to access?

::: {.notes}
This final slide encourages active participation and community learning around both API security and effective AI collaboration. Invite students to share authentication challenges they've encountered so the class can practice using AI to solve them together. Discuss different approaches to prompting AI for security help and let students learn from each other's strategies. Most importantly, help them connect security concepts to their own project interests - when they're excited about the data they want to access, they'll be more motivated to implement proper security practices.
:::
