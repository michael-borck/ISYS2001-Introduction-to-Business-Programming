---
title: "Module 3: AI Collaboration - Having Productive Conversations with Your Digital Assistant"
subtitle: "Duration: 10-15 minutes"
format: 
  pptx: default
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

# Think of AI as Your Junior Developer

When you start your first business job, you might get a junior developer or intern to work with. You wouldn't just say "make a website" and walk away. You'd provide context, be specific, and guide them through the process.

**AI works the same way.** The better you communicate, the better results you get.

::: {.notes}
Think of AI as your junior developer - a capable but inexperienced programmer that can assist with coding tasks. Like a junior dev, AI requires clear instructions, sample data, and context about the business problem to produce quality code.

When collaborating with AI, provide specific requirements, share relevant data, explain the business use case, and ask for explanations of the code. Iterate on the AI's responses to refine the code until it meets your needs. By working effectively with AI, you can accelerate development while still maintaining control over the final output.
:::


# The Art of AI Prompting for Business Tasks

## ❌ Vague Prompts (Don't Do This)
- "Help me with pandas"
- "Write some code"
- "Analyze this data"
- "Make a function"

## ✅ Effective Prompts (Do This Instead)

**Template**: *Context + Specific Task + Format Preference*

**Example 1**: 
> "I'm working on a finance assignment. I have a CSV file with columns: Date, Amount, Category, Description. I need to calculate total spending by category and show the results in descending order. Please write pandas code with comments explaining each step."

**Example 2**:
> "I'm analyzing retail sales data for my business assignment. The CSV has: Date, Product, Quantity, Unit_Price, Total_Sale, Region. I want to find which region has the highest total sales and what the average sale amount is per region. Can you write pandas code that's easy to understand?"

::: {.notes}
\u274c Vague prompts like "Help me with pandas", "Write some code", "Analyse this data", and "Make a function" are not effective when collaborating with AI. These prompts lack context, specificity, and clarity about the desired output, leading to suboptimal or incorrect responses from the AI assistant.

\u2705 Instead, provide detailed context about your task, be specific about the output format and content you need, and ask the AI to explain its reasoning and interpretation. For example, "I have a pandas DataFrame called 'sales_data' with columns 'date', 'product', and 'revenue'. Please write a function to calculate the total revenue for each product, and return the results in a new DataFrame sorted by total revenue in descending order. Explain how the function works and interpret the business implications of the results."
:::


# The Conversation Flow: Iterate and Improve

Good AI collaboration is rarely one prompt. It's a conversation:

## Round 1: Get the Basic Code
**You**: "I have transaction data with Date, Amount, Category. I want to create a spending summary by category."

**AI**: *[Provides basic code]*

## Round 2: Add Business Context  
**You**: "That's great! Can you modify it to also show what percentage each category represents of total spending? This is for a personal finance analysis."

**AI**: *[Enhances the code with percentages]*

## Round 3: Handle Real-World Issues
**You**: "The Amount column has dollar signs ($) in it. Can you update the code to handle this?"

**AI**: *[Adds data cleaning steps]*

::: {.notes}
The Conversation Flow: Iterate and Improve

To get the most out of collaborating with AI, it's crucial to approach the conversation iteratively. Rather than accepting the first response, engage in a back-and-forth dialogue, refining your prompts and providing additional context and clarification as needed. This iterative process allows you to guide the AI towards delivering outputs that align closely with your specific requirements and business objectives.

By iterating and improving your prompts over multiple rounds of conversation, you can progressively build upon the AI's responses, adding nuance, addressing edge cases, and incorporating real-world considerations. Through this process, you'll develop a more sophisticated and tailored solution that effectively meets your needs. Remember, effective AI collaboration is a skill that improves with practice, so don't be afraid to experiment and refine your approach over time.
:::


# AI Conversation Best Practices

## 1. Always Provide Context
- What's the business purpose?
- What does your data look like?
- Who will use this analysis?

## 2. Be Specific About Output
- "Show results as a table"
- "Include comments in the code"
- "Format currency as Australian dollars"
- "Sort by highest to lowest"

## 3. Ask for Explanations
- "Can you explain what this line does?"
- "Why did you choose this approach?"
- "What would happen if the data was different?"

## 4. Request Business Interpretation
- "What business insights can I draw from this?"
- "How would I present this to a manager?"
- "What questions should I ask about this data?"

::: {.notes}
Here are the presenter notes for the "AI Conversation Best Practices" slide:

To have effective conversations with AI for business tasks, it's critical to provide sufficient context about the purpose, data, and intended audience. Be specific in your requests, such as asking for results in a certain format like a table, comments in the code, or sorting in a particular order. This allows the AI to better understand your needs and deliver more relevant and useful outputs.

When collaborating with AI, treat it like a junior developer. Ask probing questions to understand its thought process, like why it chose a certain approach or what would happen with different data. Request explanations of key code elements. Most importantly, ask the AI to provide business insights and recommendations on presenting the analysis to stakeholders. By engaging in this back-and-forth dialogue, you can iterate and improve the AI's outputs to best meet your business objectives.
:::


# Effective Prompting Templates for Your Assignment

## Template 1: Data Loading and Exploration
```
"I'm building a Smart Finance Assistant for my assignment. I have a CSV file called [filename] with columns [list columns]. I need to:
1. Load the data
2. Check for any issues (missing values, data types)
3. Show basic statistics
Please write pandas code with explanations."
```

## Template 2: Analysis and Calculations
```
"Using transaction data with [describe columns], I want to calculate [specific business metric]. The analysis should help someone understand [business goal]. Please include code comments and suggest what insights this might reveal."
```

## Template 3: Troubleshooting
```
"I'm getting this error: [paste error message]. My data looks like [describe structure]. I'm trying to [explain goal]. Can you help me fix this and explain what went wrong?"
```

::: {.notes}
Here are the presenter notes for the slide "Effective Prompting Templates for Your Assignment":

The slide "Effective Prompting Templates for Your Assignment" aims to provide you with ready-to-use prompts that you can adapt for common AI collaboration tasks in your work. These templates cover key areas such as data loading and exploration, analysis and calculations, and troubleshooting, which are essential for effectively leveraging AI capabilities in your projects.

By using these prompting templates as a starting point, you can save time and effort in crafting effective prompts for your AI collaborator. Simply customise the templates with the specific details and requirements of your assignment, and you'll be well on your way to productive AI-assisted problem-solving and task completion.
:::


# AI Tip: Build Your Prompt Library 💡

As you work on your assignment, save effective prompts! Here are some starters:

**For Financial Analysis**:
- "Calculate monthly spending trends with percentage changes"
- "Identify unusual transactions that might need attention"
- "Create a spending summary suitable for a budget review meeting"

**For Data Quality**:
- "Check this financial data for common issues and suggest cleaning steps"
- "Validate that all amounts are reasonable and properly formatted"

**For Business Insights**:
- "What financial patterns or trends should I highlight to a bank manager?"
- "How would I explain this spending analysis to someone non-technical?"

::: {.notes}
Your prompt library should include reusable prompts for common financial analysis tasks, such as calculating spending trends with percentage changes, identifying unusual transactions, and generating spending summaries for budget review meetings. These prompts should guide the AI to check data quality, validate amounts are reasonable and properly formatted, and highlight key financial patterns or trends.

When building your prompt library, consider including prompts that request explanations of the analysis in non-technical language suitable for a general audience. This will help you communicate insights effectively to stakeholders who may not have a technical background. Regularly review and refine your prompts based on the AI's responses to ensure they are clear, specific, and aligned with your business needs.
:::


# Common AI Collaboration Mistakes (And How to Fix Them)

## Mistake 1: Accepting First Response
**Problem**: Taking whatever AI gives you without iteration  
**Solution**: Always ask "Can you improve this by..." or "What if I also wanted to..."

## Mistake 2: Not Providing Sample Data
**Problem**: AI guesses what your data looks like  
**Solution**: Share a few example rows or describe the exact column structure

## Mistake 3: Forgetting Business Context
**Problem**: Getting technically correct but business-irrelevant code  
**Solution**: Always explain WHY you need this analysis

## Mistake 4: Not Asking for Explanations
**Problem**: Getting code you don't understand  
**Solution**: Always ask "Can you explain how this works?" for complex parts

::: {.notes}
Common AI collaboration mistakes include accepting the first response without iterating, not providing sample data for the AI to work with, forgetting to include relevant business context, and not asking the AI for explanations of its outputs. These mistakes can lead to suboptimal or even incorrect results that don't meet the specific needs of the business problem at hand.

To fix these mistakes, always engage in multiple rounds of back-and-forth with the AI, refining your prompts and providing feedback. Share representative sample data so the AI can better understand the structure and format you need. Clearly explain the business context and goals to guide the AI towards more relevant and useful outputs. Finally, prompt the AI to walk through its reasoning so you can verify the logic and catch any potential errors or faulty assumptions.
:::


# Practice Exercise: Write Better Prompts

**Scenario**: You want to analyze spending patterns to identify potential savings opportunities.

**❌ Weak Prompt**: "Help me find where I spend too much money"

**✅ Strong Prompt**: Try writing your own improved version using the templates above!

<details>
<summary>Sample Strong Prompt</summary>

"I'm analyzing personal spending data for my Smart Finance Assistant assignment. My CSV has columns: Date, Amount, Category, Description. I want to identify categories where spending might be higher than typical budgets (like spending more than $200/month on dining or more than $50/month on coffee). Please write pandas code that:
1. Calculates monthly spending by category  
2. Highlights categories that exceed common budget thresholds
3. Includes comments explaining the business logic
This analysis will help create spending alerts for the finance assistant."

</details>

::: {.notes}
- This slide provides an opportunity for the audience to practise writing effective prompts based on the principles and techniques covered in the previous slides.
- The presenter should encourage attendees to work on crafting prompts individually or in small groups, focusing on providing clear context, specifying desired outputs, requesting explanations, and incorporating business interpretation. After the exercise, the presenter can invite volunteers to share their prompts and discuss how they applied the best practices covered in the presentation.
:::


# Your Assignment Strategy

For your Smart Finance Assistant project, plan to have multiple AI conversations:

1. **Initial Setup**: "Help me load and explore the transaction data"
2. **Basic Analysis**: "Create spending summaries and categories"
3. **Business Insights**: "Identify patterns and trends"
4. **User Experience**: "Format results for non-technical users"
5. **Documentation**: "Help me explain how this works"

::: {.notes}
Start by identifying the key components of your assignment, such as data sources, analysis methods and expected deliverables. Break the assignment down into smaller, manageable tasks and allocate sufficient time for each one, including buffer time for unexpected challenges.

Leverage AI to assist with tasks like data cleaning, exploratory analysis, and generating visualisations. Provide the AI with clear, specific prompts that include relevant business context and sample data. Iterate on the prompts to refine the outputs, and ask the AI for explanations and interpretations to ensure the results align with your objectives.
:::


# Ready for Real Collaboration

In Module 4, you'll learn how to evaluate and improve the code that AI gives you. Remember: **you're the director, AI is your assistant.** The better you communicate your vision, the better your results will be.

**Coming up**: Learn to spot when AI gets it wrong and how to guide it toward better solutions.



Ready to become an AI code reviewer? Let's move to Module 4!

::: {.notes}
Ready for real collaboration with your AI assistant? Follow these key steps to make the most of your AI partnership:

1. Provide clear context about your business goals, target audience, and desired outcomes. Share relevant data samples to help your AI understand the specifics of your project.

2. Iterate on your prompts, asking for explanations, business interpretations, and troubleshooting help. Build a library of effective prompts tailored to common tasks in your domain.
:::
