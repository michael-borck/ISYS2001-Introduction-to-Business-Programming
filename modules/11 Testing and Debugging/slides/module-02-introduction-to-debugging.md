---
title: "Mastering Debugging: Human Insight, AI Assistance"
subtitle: "Navigating Complex Code with Confidence in the AI Era"
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


# Introduction

* Debugging in the Age of AI
* Understanding the importance of debugging
* Overview of advanced debugging techniques

::: {.notes}

Welcome! Debugging is an essential skill for every developer – it's the art of being a code detective. In this session, we'll explore advanced debugging techniques. But more importantly, we'll discuss how your human intuition and analytical skills, when combined with the capabilities of modern AI tools, can make you exceptionally effective at pinpointing and resolving even the most complex software issues. We're moving beyond basic fixes to understand root causes, with AI as a powerful investigative partner.
:::



# What is Debugging in the Age of AI?**

* **Core Definition:** Still the process of identifying, analysing, and resolving defects in software.
* **New Challenges & Opportunities:**
    * AI can generate code (and bugs!) rapidly.
    * AI can suggest fixes, but are they superficial or foundational?
* **Human's Role is Elevated:** From just fixing to *deeply understanding* why bugs occur and ensuring robust solutions, even when AI assists.
* **Basic vs. Advanced Debugging (AI Context):**
    * Basic: Quick fixes, perhaps AI-suggested, for obvious errors.
    * Advanced: Systematic investigation of complex issues, using tools and critical thinking, with AI providing targeted support (e.g., explaining complex tracebacks, suggesting hypotheses).

::: {.notes}
Debugging is still about finding and fixing bugs. However, the landscape is changing with AI.
* AI can generate vast amounts of code, which means more potential for bugs, but also more opportunities for AI to *help find* them.
* AI tools can often propose quick fixes. The challenge for you, the developer, is to determine if an AI's suggestion truly solves the root problem or just patches a symptom.
* This elevates your role. It's not just about making the error message go away; it's about deep understanding. Advanced debugging, therefore, involves a systematic, human-led investigation where AI acts as a knowledgeable assistant, perhaps explaining an obscure error message or helping you understand a complex piece of code before you even start the debugger.
:::



# Key Advanced Debugging Techniques

* **Strategic `print()` Statements & Logging:** Still your first line of detailed inquiry.
    * *AI Assist:* "Based on this error and code, where would `print()` statements be most effective for tracing variable `x`?"
* **Breakpoints & Stepping Through Code (Debuggers):** Pause execution, inspect state, understand flow line-by-line.
    * *AI Assist:* "At this breakpoint, variable `foo` is `None`. What are common reasons for this in such a function?" or "Explain this section of the call stack."
* **Conditional Breakpoints:** Pause only when specific conditions are met (e.g., `loop_counter > 1000`).
    * *AI Assist:* "Help me formulate a condition for a breakpoint that triggers if this list ever becomes empty."
* **Watch Expressions & Call Stack Navigation:** Track specific variables; understand the path to the current error.
    * *AI Assist:* "Explain the role of function `bar()` in this call stack leading to the error."
* **Code Profiling & Performance Analysis:** Identify bottlenecks or excessive resource usage that might indicate or cause bugs.
    * *AI Assist:* "This function is unexpectedly slow. What are common performance pitfalls I should look for using a profiler?"

::: {.notes}
Let's look at some powerful techniques. Remember, AI doesn't replace these; it can make you more effective when using them.
* **Strategic `print()`/Logging:** Before even launching a full debugger, targeted print statements can give you quick insights. You can even ask AI where the most informative print statements might go.
* **Debuggers (Breakpoints & Stepping):** This is where you truly become a code detective, stopping time to examine the crime scene. Set a breakpoint, run your code, and when it pauses, inspect variable values. Step through line by line. If you see a variable with an unexpected value at a breakpoint, you can ask an AI to brainstorm reasons why that might happen in that specific code context. Or, if the call stack (the list of functions that led to this point) is confusing, AI can help explain it.
* **Conditional Breakpoints:** Super useful for bugs that only appear after many iterations or under specific circumstances. AI can help you think through the logic for these conditions.
* **Watch Expressions & Call Stack:** Modern debuggers let you 'watch' specific variables or expressions as they change. Understanding the call stack is vital, and AI can help decipher complex ones.
* **Profilers:** Sometimes bugs aren't just errors but performance issues that break functionality (e.g., a timeout). Profilers help find slow code. AI can suggest what to look for.
Your human insight guides where to look; AI can help interpret what you find or suggest avenues for investigation.
:::



# Tools for Advanced Debugging (AI Integration)**

* **Integrated Development Environments (IDEs):** PyCharm, VS Code, etc., offer powerful built-in debuggers.
    * Features: Breakpoint management, variable inspection, step controls, call stack view.
* **AI-Integrated IDEs/Tools:**
    * **Inline Code Explanation/Suggestions:** AI like GitHub Copilot can explain selected code or suggest fixes *within* your editor.
    * **AI-Powered Error Analysis:** Tools that analyse tracebacks and offer more sophisticated explanations or troubleshooting steps.
    * **AI Chat for Debugging:** Dedicated AI chat interfaces where you can paste code/errors and ask for debugging help.
* **Choosing the Right Combination:** Leverage your IDE's debugger for control, and AI tools for insights and suggestions.

::: {.notes}

Your IDE (like PyCharm, VS Code, Spyder, etc.) is your primary debugging command center, with its built-in debugger offering fine-grained control.
* **AI Integration is Key:** Many IDEs are now integrating AI directly. GitHub Copilot, for example, can explain code snippets or even suggest fixes as you type. Other tools might offer more detailed AI analysis of error messages. You might use an AI chat interface side-by-side with your debugger, feeding it information from your debugging session to get hypotheses or explanations. The goal is to use these tools in concert: the IDE debugger for control and detailed inspection, and AI for accelerating understanding and idea generation.
:::



# A Case Study (AI-Assisted Workflow)**

* **Scenario:** (Use a slightly more complex but still understandable example than just `a+b` vs `a*b`. Perhaps a list processing error, an off-by-one, or a simple state-related bug).

* **Step-by-Step (Illustrative):**
    1. **The Bug Appears:** Program produces unexpected output or crashes with a traceback.
    2. **Initial Human Analysis:** Read error. Form initial thoughts.
    3. **AI for Error Explanation:** "Explain this `IndexError` and traceback in the context of my list processing function `[code snippet]`."
    4. **Strategic `print()`/Logging (Human + AI):** "Where should I add prints to see the list's state before the error?"
    5. **Debugger Time (Human Control):** Set breakpoints based on insights. Step through.
    6. **AI for Hypothesis at Breakpoint:** "At this breakpoint, `my_list` is `[1,2]` but I expected `[1,2,3]`. What could have removed an element before this line in my function `[code snippet]`?"
    7. **AI for Solution Brainstorming:** "I think the bug is related to `[specific line/logic]`. Can you suggest ways to fix this potential off-by-one error?"
    8. **Human Implements & Verifies:** Critically review AI's idea, implement a fix, and *test thoroughly* (ideally with pre-existing unit tests, or write a new one).
* **Lessons:** AI speeds up understanding and idea generation, but human controls the process and validates the outcome.

::: {.notes}

Let's walk through a hypothetical debugging session. Imagine a function that's supposed to process a list of items but sometimes misses the last item or throws an error.
1.  You run it, and it either crashes or gives the wrong result.
2.  You look at the error (if any) or the incorrect output.
3.  You could paste the error and relevant code into an AI and ask for an explanation of what the error *means* generally, or what it might mean in *your specific code*.
4.  Based on this, or your own intuition, you add `print` statements. Or ask AI, "Where are good places to print the list and loop index to understand what's happening?"
5.  The prints narrow it down, so you fire up the debugger, setting a breakpoint just before the suspected problematic line.
6.  You step through. At a breakpoint, you see the state isn't what you expect. You could describe this state and the code to an AI and ask for potential reasons *why* it's in that state.
7.  Once you have a strong hypothesis (e.g., "I think my loop condition is wrong"), you can ask AI to suggest fixes for *that specific kind of problem*.
8.  Crucially, you evaluate AI's suggestions. Does it make sense? Does it address the root cause? You implement the fix, and then you *test it thoroughly*, ideally with unit tests we discussed in Module 1. This AI-assisted workflow allows you to combine your analytical skills with AI's rapid information processing and pattern matching.
:::



# Debugging Best Practices (for the AI Era)**

* **Systematic Approach:** Don't just guess. Form hypotheses (use AI to help brainstorm), test them (with `print`, debugger, or by asking AI to evaluate a hypothesis against the code), and iterate.
* **Understand, Don't Just Swap Code:** If AI suggests a fix, understand *why* it works before applying it.
* **Reproduce the Bug Consistently:** Before fixing, know how to make it happen reliably.
    * *AI Assist:* "Help me identify the conditions or inputs that might be causing this intermittent bug."
* **Keep a Log (Physical or Digital):** Note what you've tried, your theories, AI prompts, and AI's useful (or not useful) responses. This prevents going in circles.
* **Write a Test for the Bug:** Once found and fixed, write a test case that *would have caught this bug*. This prevents regressions.
    * *AI Assist:* "I fixed this bug `[describe bug and fix]`. Help me write a `pytest` test case that specifically targets this scenario."
* **Regular Code Reviews (Human + AI?):** Humans discuss logic. AI can spot potential issues or suggest areas for clarification.

::: {.notes}

Effective debugging relies on good habits:
* **Systematic Approach:** Avoid randomly changing code. Develop a theory about the bug, then test that theory. AI can help you develop theories by explaining parts of the code or suggesting potential causes for an observed behavior.
* **Understand the Fix:** If an AI gives you a code snippet that fixes the bug, don't just paste it in. Figure out *why* it's the correct solution. This is how you learn.
* **Reproduce Consistently:** It's hard to fix a bug you can't reliably trigger. AI might help you brainstorm conditions or inputs that lead to an intermittent bug.
* **Keep a Log:** Debugging complex issues can take time. Jot down what you've tried, what you observed, and even key AI interactions.
* **Test for the Bug:** This is crucial. Once you've fixed a bug, add a test that specifically covers that scenario. AI can be very helpful here: "I found a bug where X happened. I fixed it by doing Y. Can you help me write a unit test that would have failed before my fix and passes now?"
* **Code Reviews:** Having another human look at your code is invaluable. AI tools are also emerging that can provide automated code review feedback, spotting potential issues or areas for improvement.
:::



# Common Pitfalls in Debugging (AI Edition)**

* **Fixing Symptoms, Not Root Causes:**
    * *AI Risk:* AI might suggest a narrow fix that handles a specific case but misses the underlying systemic issue. Human critical thinking is needed to ask "why?" repeatedly.
* **Overlooking Simple Solutions:** Sometimes it *is* just a typo! Don't jump to complex AI queries immediately.
* **Not Replicating the Environment:** Bug appears in production but not locally. (AI less helpful here, more about environment setup).
* **Misinterpreting AI Suggestions:** Applying AI advice without fully understanding its implications for your specific codebase.
* **"Black Box" AI Fixes:** Accepting an AI fix that works but you don't understand. This creates unmaintainable code.
* **Ignoring Version Control:** Not using branches for debugging attempts; makes it hard to revert changes (AI or human-made).

::: {.notes}

Even with AI, pitfalls await:
* **Symptom vs. Root Cause:** This is a big one with AI. An AI might see an error and suggest a way to prevent *that specific error instance* (e.g., adding a null check) without addressing *why* the value is null in the first place. Your job is to dig deeper for the root cause.
* **Overlooking the Obvious:** Before crafting a complex AI prompt, double-check for simple typos or basic logical errors yourself!
* **Environment Mismatches:** A classic. AI can't easily solve this; it requires careful comparison of environments.
* **Misinterpreting AI:** AI communicates in language, but its "understanding" of code isn't human. Ensure its suggestions make sense in *your* full context.
* **"Black Box" Fixes:** If AI fixes something and you don't know why the fix works, you've learned little, and that part of the code is now a mystery to you. This is technical debt.
* **Version Control:** Always use Git or similar. Create branches for experimental fixes (whether suggested by AI or your own). If it doesn't work, you can easily revert.
:::



# Integrating Debugging with Testing (Synergy with AI)**

* **Effective Testing Minimises Debugging:** Fewer bugs escape to later stages.
* **Tests Help Reproduce Bugs:** A failing test *is* a reproducible bug.
* **Test-Driven Debugging (TDD style):**
    1. Identify a bug.
    2. Write a test that *fails* because of this bug. (AI can help draft this test: "Write a test that demonstrates bug X in function Y.")
    3. Debug and fix the code until the test passes.
* **AI for Post-Fix Test Generation:** "I fixed bug X by changing Y. Help me write tests to ensure this fix works and doesn't break other things."
* **Debugging Informs Future Tests:** Understanding a bug helps you write better tests to prevent similar issues. AI can help generalise from a specific bug to broader test case ideas.

::: {.notes}

Debugging and testing are two sides of the same quality coin.
* Good tests, as we discussed in Module 1, catch many bugs early, reducing the time you spend in complex debugging sessions.
* When a bug *does* occur, a failing test is the best way to reproduce it consistently.
* Consider "Test-Driven Debugging": When you find a bug, first write a test that specifically triggers it and fails. Then, debug your code until that new test (and all others) pass. AI can assist in drafting that initial failing test: "I have a bug where my function `process_items` fails if the input list is empty. Can you help me write a `pytest` test that shows this failure?"
* After you've fixed a bug (with or without AI's help in finding the fix), ask AI to help you write robust tests around that fix to prevent it from recurring (regression testing).
Understanding why a bug occurred often gives you insights into what other kinds of tests you should be writing. AI can help you take a specific bug instance and brainstorm related test scenarios.
:::



# Conclusion: Becoming a Code Detective in the AI Era

* Advanced debugging is about deep investigation and understanding, not just quick fixes.
* AI tools are powerful *assistants*, not replacements for your analytical skills and critical judgment.
* Master traditional techniques (`print`, debuggers) to effectively guide and verify AI suggestions.
* **Practice the Human-AI Workflow:** Investigate -> Hypothesise (with AI) -> Verify (with tools) -> Implement (with understanding) -> Test.
* Continuous learning in both debugging techniques and effective AI interaction is key.
* **Call to Action:** Embrace debugging as a challenging but rewarding part of development. Use every tool, including your brain and AI, to master it!

::: {.notes}

In conclusion, mastering advanced debugging in this AI era means becoming a skilled investigator who knows how to use every tool at their disposal – including powerful AI assistants.
* It's about the deep dive, the root cause analysis. AI can help you get there faster, explain complexities, and offer ideas, but your critical thinking steers the ship.
* Your proficiency with fundamental techniques like `print` statements and interactive debuggers actually makes you *better* at using AI, because you can provide it with more precise information and better evaluate its responses.
* Focus on practicing that collaborative workflow: your initial investigation, using AI to explore possibilities or explain roadblocks, using debuggers to confirm, understanding and implementing solutions, and finally, testing your fixes.
Debugging will always be part of software development. By combining your growing expertise with the evolving capabilities of AI, you'll be well-equipped to tackle any bug that comes your way.
:::
