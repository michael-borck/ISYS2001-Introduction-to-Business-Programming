---
title: "Strategic Test Design: Guiding Quality in AI-Assisted Development"
subtitle: "Ensuring Software Reliability Through Human Insight and AI Collaboration"
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

* Test Design with AI
* What is a Test Case
* Effective Test Design
* Common Pitfalls
* Tools and Resources
* Strategic Design in an AI World

::: {.notes}

Welcome! In our previous modules, we explored testing frameworks and debugging, increasingly seeing AI as a powerful assistant. Now, we focus on a critical human skill: **strategic test design**. Even if AI can help write code or even draft test cases, *you* define what success looks like. This session is about how to thoughtfully design effective test cases that ensure software quality, especially when collaborating with AI tools. We'll learn how your strategic thinking guides the entire quality assurance process.
:::



# The Power of Test Design in the AI Era

* **Why Test Design Matters:** Defines "correctness" for both human and AI-generated code.
* **Human as the Strategist:** You decide *what* to test, *why* it's important, and *how thoroughly*.
* **AI as the Tactical Assistant:** AI can help generate test ideas, data, or boilerplate, but your design guides its efforts.
* **Effective test cases:** Ensure AI modifications are actual improvements, not just changes.

::: {.notes}

In an era where AI can generate code and even suggest tests, the human role of **designing** those tests becomes paramount.
* A well-designed test case is a clear specification of expected behavior. This is crucial whether a human or an AI wrote the underlying code.
* As the developer, you bring the domain knowledge and understanding of user needs. You are the strategist who decides what aspects of the software are critical to test and what constitutes a meaningful test.
* AI can then act as a powerful tactical assistant, helping you flesh out these strategies by generating test scenarios, suggesting edge cases, or even drafting initial test code based on your design.
* Ultimately, your test design is what validates that any changes, whether human or AI-driven, truly meet the quality bar. Today, we'll cover how to design these vital test cases, integrating AI as a collaborative tool.
:::



# What is a Test Case? (AI Context)

* **Definition:** A set of inputs, execution conditions, test steps, and expected results developed for a particular objective (e.g., to verify compliance with a specific requirement).
* **Core Components:**
    * Test Case ID / Name
    * Preconditions / Setup
    * Test Steps (Actions)
    * Test Data (Inputs)
    * **Expected Results** (Crucial for defining success)
    * Actual Results & Status (Pass/Fail)
    * Postconditions / Teardown
* **AI Assistance in Component Generation:**
    * AI can help draft initial test steps based on a feature description.
    * AI can suggest varied test data (valid, invalid, edge cases).
    * **Human role:** Critically review and refine AI suggestions, especially expected results.

::: {.notes}

A test case is essentially a formal recipe for verifying a piece of functionality. It specifies everything needed to run a test and determine if the software behaves as expected.
* The **expected result** is perhaps the most critical component you define – it’s your assertion of what "correct" means.
* While the core components remain the same, AI can now assist in their creation. For instance, given a user story or a function signature, you could ask an AI: "Suggest test steps and typical test data for a function that does X." Or, "What are some edge case inputs for a feature that validates email addresses?"
* Your crucial role is to then take these AI-generated suggestions, critically review them, refine them (especially the expected results to ensure they align perfectly with requirements), and ensure they form a coherent and effective test.
:::



# Principles of Effective Test Design (Human-Guided, AI-Refined)

* **Clear, Concise, Unambiguous:** Easy to understand and execute by anyone (or any automated tool).
    * *AI Assist:* "Can you make these AI-generated test steps clearer and more concise?"
* **Traceable to Requirements:** Each test case should clearly map to a specific requirement or user story.
    * *AI Assist (Conceptual):* AI might help identify which requirements lack test case ideas (though this is more advanced).
* **Repeatable & Consistent:** Produces the same results every time if the software hasn't changed.
* **Independent & Isolated:** One test case failure shouldn't cascade or affect others unnecessarily.
    * *AI Assist:* "Review this set of test cases. Are there any obvious dependencies between them that I should try to remove?"
* **Covers Likely Failure Points & Edge Cases:** Goes beyond the "happy path."
    * *AI Assist:* "What are common failure points or edge cases for a [type of feature, e.g., 'file upload'] feature?"
* **Maintainable:** Easy to update as the software evolves.
    * *AI Assist:* Help refactor test cases when underlying code changes, but human confirms logic.

::: {.notes}

Effective test cases aren't just thrown together; they follow key principles.
* **Clear and Unambiguous:** If AI generates draft test steps, review them. Are they easy for another human (or you, in six months) to understand? You can even ask another AI instance to "rephrase these test steps for maximum clarity."
* **Traceable:** This ensures you're testing what matters.
* **Repeatable:** Essential for reliable automation.
* **Independent:** This helps pinpoint exactly where a failure lies. AI might help spot potential dependencies if you ask it to review a test suite description.
* **Covers Failure Points/Edge Cases:** This is where AI can shine as a brainstorming partner. Prompt it: "For a user registration form, what are some typical edge cases or invalid inputs I should design test cases for?"
* **Maintainable:** As your software changes, your tests will need to change. AI can help with the mechanical aspects of refactoring tests, but you must ensure the *logic* of the updated test remains sound.
:::



# A Spectrum of Tests: Types & AI Brainstorming

* **Functional Test Cases:** Verify specific actions/functions of the software.
    * *AI Assist:* "For a 'shopping cart checkout' feature, list key functional test cases."
* **User Interface (UI) Test Cases:** Ensure UI elements look and work correctly.
    * *AI Assist:* "What are common UI test cases for a web login form?" (May lead to more specialised UI testing tools).
* **Performance Test Cases:** Evaluate speed, responsiveness, stability under load.
    * *AI Assist (Conceptual):* "What aspects of this [architecture description] should be performance tested?"
* **Security Test Cases:** Assess vulnerabilities and protection.
    * *AI Assist (Conceptual):* "What are common security vulnerabilities I should design test cases for related to user authentication?"
* **Usability Test Cases:** How easy and intuitive is the system to use?
    * *AI Assist:* Can AI analyse a UI description and suggest usability heuristic violations to test for? (Emerging area)
* **Choosing the right types:** Your strategy dictates the mix, AI can help explore options.

::: {.notes}

There are many different types of tests, each focused on a different aspect of quality.
* **Functional tests** are often the most common – does the feature do what it's supposed to do? AI can be great at generating a list of functional scenarios based on a feature description.
* **UI tests** focus on the visual and interactive aspects. AI might help list common UI elements to check on a given screen type.
* **Performance and Security testing** are specialised domains. While AI might not design these complex tests end-to-end for a beginner, it can certainly help you brainstorm *what aspects* to consider testing based on your application's nature. For example, "What are typical performance metrics to test for a real-time data dashboard?"
* **Usability testing** is about the user experience. Emerging AI capabilities might even analyse UI mockups for potential usability issues that you could then design tests around.
Your understanding of the project's risks and priorities will determine which types of tests are most important. AI can then assist in brainstorming specific cases within those types.
:::



# Test Case Design: A Human-AI Collaborative Workflow

1. **Identify Testable Requirements/Scenarios (Human Lead):** What feature or behavior needs testing? Understand the core goal.
2. **Define Test Objectives (Human Lead):** What specific aspect of the requirement will this test case verify?
3. **Brainstorm with AI (Collaborative):**
    * "Given this feature `[description]`, suggest different test scenarios (happy path, negative paths, edge cases)."
    * "What are important preconditions for testing `[feature]`?"
4. **Detail Test Steps (AI Drafts, Human Refines):**
    * Prompt AI: "For the scenario `[specific scenario]`, draft the test steps."
    * Human: Review for clarity, completeness, accuracy. Add necessary detail.
5. **Specify Test Data (AI Suggests, Human Validates):**
    * Prompt AI: "Suggest valid and invalid input data for these test steps."
    * Human: Select appropriate data, ensure it covers boundaries and edge cases.
6. **Define Expected Outcomes (Human Critical, AI can Verify Consistency):**
    * Human: Based on requirements, *you* define the precise expected outcome. This is critical.
    * AI Assist: "If I input X according to these steps, and the requirement is Y, what should the expected outcome be?" (Use AI to check your logic or for simple cases).
7. **Review and Refine (Human Lead):** Does the complete test case meet all principles of effectiveness? Is it unambiguous?

::: {.notes}

Let's look at a practical, AI-augmented workflow for designing a test case:
1.  **You start by identifying what needs to be tested** based on project requirements or user stories. You understand the *why*.
2.  **You define the specific objective** for a particular test case. What single thing is it trying to prove?
3.  **Now, bring in your AI partner for brainstorming.** Describe the feature and ask for different test scenarios – happy paths, what happens if things go wrong, what are the tricky edge cases. Ask about necessary preconditions.
4.  **For a chosen scenario, ask AI to draft the sequence of test steps.** Then, *you* review, edit, and refine these steps. Are they logical? Complete? Easy to follow?
5.  **Need test data? AI can suggest a range of inputs.** "For these steps, give me examples of valid inputs, invalid inputs that should cause an error, and boundary values." You then curate and select the most relevant data.
6.  **Defining the expected outcome is largely a human task, rooted in the requirements.** However, for straightforward logic, you might describe the input and steps to an AI and ask, "Given these inputs and steps, and assuming the function should calculate a 5% discount, what should the output be?" This can act as a sanity check.
7.  **Finally, you review the entire test case.** Is it clear? Does it meet all the principles we discussed? This iterative process, with AI handling some of the generation and you providing the strategic oversight and critical evaluation, can be very powerful.
:::



# Example: Weather Dashboard Test Design with AI
* **Scenario:** Checking weather updates for a user-entered location.
* **AI-Assisted Design Steps:**
    * **Human Objective:** Verify correct real-time weather is shown for a valid city, and graceful error for an invalid city.
    * **AI Brainstorm Scenarios:**
        * Prompt: "Suggest test scenarios for a weather dashboard's location search."
        * *AI Output (example):* Valid city, misspelled city, non-existent city, city with special characters, empty input.
    * **Human Selects Scenario:** "Test with a valid, known city."
    * **AI Drafts Test Steps:**
        * Prompt: "Draft test steps for searching 'Perth, Australia' on a weather dashboard and verifying the temperature."
    * **Human Refines Steps & Expected Result:**
        1. Navigate to dashboard.
        2. Enter "Perth, Australia" in search.
        3. Click "Search."
        4. **Expected:** Weather details for Perth displayed. Temperature shown is within +/- 2 degrees of actual current Perth temperature (requires external check or mock for automation).
    * **AI Suggests Edge Case Data:**
        * Prompt: "Suggest invalid city names that might cause errors."
        * *AI Output (example):* "Xys123", "   ", "!@#$"
    * **Human Designs Negative Test:** Test with "Xys123", expect "City not found" message.

::: {.notes}

Let's apply this to our weather dashboard example.
* Our objective is to check that it shows correct weather for real cities and handles bad input well.
* We could ask an AI: "What are different test scenarios I should consider for the location search feature of a weather dashboard?" The AI might suggest testing with valid cities, misspelled ones, completely fake names, empty inputs, etc.
* We pick a scenario: "Display weather for Perth, Australia." We can ask the AI to "Draft the test steps to search for 'Perth, Australia' and verify the displayed temperature."
* The AI might give us basic steps. We then refine them and, importantly, define a precise expected result. For real-time data like weather, the expected result might be "Temperature displayed is within an acceptable range of the *actual* current temperature," which for automated tests often involves more advanced techniques like mocking or service virtualisation, or a manual check.
* Then we might ask AI for examples of invalid city names. We'd use these to design negative test cases, defining the expected error message like "City not found." This shows how AI can help explore the test space more thoroughly.
:::



# Common Pitfalls in Test Design (AI Era Perspective)**
* **Traditional Pitfalls:**
    * Overly complex test cases (hard to maintain).
    * Testing multiple features in one test (hard to isolate faults).
    * Ambiguity in expected outcomes (leads to incorrect pass/fail).
* **New AI-Related Pitfalls:**
    * **Over-reliance on AI-Generated Scenarios:** AI might miss nuanced business logic or critical-but-unobvious edge cases if not prompted with enough context.
    * **Superficial Test Cases:** AI might generate many "shallow" tests that hit lines of code but don't deeply validate behavior or complex interactions.
    * **Bias in AI Suggestions:** AI's training data might lead it to suggest tests that reflect common patterns but miss unique aspects of *your* application.
    * **Lack of Critical Review:** Accepting AI-generated test cases without thorough human validation of their relevance, steps, and *especially expected outcomes*.
    * **"Quantity over Quality" Illusion:** AI can generate many tests quickly, but if they aren't well-designed and meaningful, they provide false confidence.

::: {.notes}

While AI helps, some classic pitfalls remain, and new ones emerge.
* Traditional issues like overly complex tests or ambiguous expected results still apply. Clear, focused human design is the antidote.
* **AI-Specific Pitfalls:**
    * **Over-reliance:** Don't assume AI will think of everything. If your application has very specific or unusual business rules, you need to guide the AI or design those test cases yourself.
    * **Superficial Tests:** AI might generate tests that seem to cover the code but don't actually verify the critical logic paths or interactions. Your deep understanding is needed to ensure tests have substance.
    * **Bias:** An AI is trained on vast amounts of data. If your problem is unique, the AI's "common" suggestions might not be the best fit.
    * **Lack of Critical Review:** This is the biggest risk. If you blindly accept AI-generated test cases, especially their expected results, you could be institutionalising misunderstandings or even testing for the wrong thing.
    * **Quantity over Quality:** AI can churn out test ideas. Your job is to curate these into a *high-quality, effective* set, not just a large one.
:::



# Tools and Resources (AI Included)**
* **Your Brain!** (Critical thinking, domain knowledge, strategic planning)
* **Requirements Documents / User Stories:** The source of truth for what to test.
* **Diagramming/Flowchart Tools:** To visualise complex logic and identify test paths.
* **Python Testing Frameworks:** `doctest`, `unittest`, `pytest` (to implement the designed tests).
* **Test Case Management Tools:** (e.g., TestRail, sephyr, Jira with plugins) for larger projects.
* **AI Development Assistants:**
    * **LLMs (ChatGPT, Claude, Gemini, etc.):** For brainstorming scenarios, drafting steps, suggesting data, explaining concepts.
    * **IDE-Integrated AI (e.g., GitHub Copilot):** For inline suggestions and explanations during test code implementation.
* **Further Reading & Communities:** Blogs, forums, testing certifications.

::: {.notes}

Your primary tool for test design is your own analytical ability and understanding of the project.
* Requirements are your foundation.
* Visual tools can help map out complex logic.
* The frameworks we discussed (Module 1) are where you'll implement these designs.
* For larger scale efforts, dedicated test management tools help organise and track test cases.
* **And now, AI tools are a significant resource.** Use LLMs for brainstorming, getting initial drafts, or understanding complex requirements. Use AI integrated into your IDE to help as you write the actual test code.
* And, as always, continuous learning from online resources and communities is key.
:::



#  Conclusion: You Are the Test Strategist
* Effective test case design is a critical human skill, amplified by AI.
* Your strategic thinking ensures that AI's tactical assistance is directed effectively.
* Well-designed tests are the ultimate verifier of quality for both human and AI-generated code.
* **Embrace the Human-AI Collaboration:** Use AI to explore more scenarios, generate drafts faster, and learn, but *you* own the design and quality.
* **Encouragement:** Practice strategic test design. The more you do it, the better you'll become at guiding AI and ensuring truly robust software.

::: {.notes}

To conclude, while AI offers exciting new capabilities for assisting in test generation, the role of the human as the **test strategist and designer** is more critical than ever.
* It's your understanding of the requirements, the user, and the potential risks that shapes an effective testing strategy.
* AI can help you execute parts of that strategy much faster, explore more ground, and even overcome writer's block when thinking of test scenarios.
* But the ultimate responsibility for ensuring that tests are meaningful, comprehensive, and correctly define "quality" rests with you. Well-designed tests are your best tool for ensuring that all code, no matter its origin, meets the mark.
So, practice designing test cases thoughtfully. Experiment with how AI can assist you, and always remember that your critical judgment is the most valuable asset in the pursuit of software quality. Happy designing!
:::