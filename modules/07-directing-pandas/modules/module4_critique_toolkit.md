---
title: "Module 4: Your AI Critique Toolkit - Becoming a Smart Code Director"
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

# AI Is Your Junior Developer - Review Everything!

Imagine you just hired a smart but inexperienced intern. They work fast, have lots of ideas, but sometimes:
- Overcomplicate simple tasks
- Miss important edge cases
- Write code that works but is hard to understand
- Make assumptions about your data

**This is exactly how AI behaves.** Your job as the code director is to review, guide, and improve their work.

::: {.notes}
AI can be a powerful tool for developers, but it's crucial to review its output carefully. As a junior developer, AI may overcomplicate simple tasks, miss important edge cases, write code that works but is difficult to understand, and make assumptions about your data. These issues can lead to poor code quality and incorrect results.

To ensure the best outcomes when working with AI, it's important to critique its suggestions using a structured framework. This involves checking for comprehension, simplicity, business logic, data assumptions, and output quality. By asking the right questions and providing clear feedback, you can guide the AI to produce more effective and maintainable code. Documenting your interactions with the AI and keeping a checklist of red flags can also help you spot potential issues and improve the quality of your work.
:::


# The Business Impact of Poor Code Review

**Scenario**: Your AI assistant generates code to analyze customer spending data. You run it without review and present results to your manager. Later you discover:

- The code ignored negative values (refunds)
- It counted duplicate transactions twice
- Currency formatting was wrong
- Results were completely misleading

**Lesson**: Always critique AI code before trusting it with business decisions.

::: {.notes}
The slide highlights the significant negative business impact that can result from poor code review practices. It presents a real-world example where code ignored negative values (refunds), counted duplicate transactions twice, used incorrect currency formatting, and ultimately produced completely misleading results. These issues demonstrate how oversights in code review can lead to inaccurate financial reporting and analysis, potentially causing businesses to make misinformed decisions.

The slide's content underscores the critical importance of thorough and rigorous code review, particularly when dealing with financial data and business metrics. It suggests that developers and reviewers must be vigilant in scrutinising code for potential errors, edge cases, and assumptions that could compromise the accuracy and reliability of the results. By using this real-world example, the slide aims to drive home the message that poor code review can have far-reaching and detrimental consequences for businesses, emphasising the need for a robust and systematic approach to code review.
:::


# Your 5-Step Critique Framework
1. Comprehension Check
2. Simplicity Check
3. Business Logic Check
4. Data Assumption Check
5. Output Quality Check

::: {.notes}
Your 5-Step Critique Framework provides a structured approach to reviewing AI-generated code for data analysis projects. The framework covers key aspects such as comprehension, simplicity, business logic, data assumptions and output quality. By systematically checking each of these areas, you can identify potential issues and request improvements from the AI assistant.

The slide emphasises the importance of active critique and not simply accepting the first code solution provided by AI. It encourages asking clarifying questions to ensure the code is well-suited to the specific business problem and data set. By engaging in this critique process, you can work with the AI assistant to iteratively refine the code and achieve high-quality, business-relevant results.
:::


# 1. **Comprehension Check**: "Do I understand this?"

**Red Flags**:
- Code looks like magic
- Variable names are unclear
- No comments explaining business logic

**Your Response**:
- "Can you add comments explaining each step?"
- "Rename variables to be more business-friendly"
- "Break this into smaller, clearer pieces"

**Example**:
```python
# ❌ AI gives you this:
df.groupby('cat')['amt'].agg(['sum','count','mean'])

# ✅ Ask for this instead:
# Group transactions by category and calculate business metrics
spending_summary = transactions.groupby('Category')['Amount'].agg({
    'Total_Spent': 'sum',
    'Transaction_Count': 'count', 
    'Average_Amount': 'mean'
})
```

::: {.notes}
The slide titled "1. **Comprehension Check**: 'Do I understand this?'" highlights common issues with AI-generated code that make it difficult to comprehend. These include code that looks like magic, unclear variable names, and a lack of comments explaining the business logic behind the code. To address these issues, the slide suggests asking the AI to add comments explaining each step, rename variables to be more business-friendly, and break the code into smaller, clearer pieces.

Ensuring code comprehension is a crucial part of the code review process when working with an AI developer. By requesting these clarifications and improvements, the human reviewer can better understand the AI's thought process and the business logic behind the code. This step helps to demystify the AI-generated code and make it more accessible to non-technical stakeholders, ultimately leading to more effective collaboration between the AI and the human team members.
:::


# 2. **Simplicity Check**: "Is this too complicated?"

**Red Flags**:
- Solution uses advanced concepts you haven't learned
- Multiple steps that could be one
- Imports lots of libraries

**Your Response**:
- "Give me the simplest version that works"
- "Use only pandas - no other libraries"
- "Show me a basic approach first"

::: {.notes}
The slide "2. **Simplicity Check**: "Is this too complicated?"" encourages you to critically assess the complexity of the AI-generated code. Look out for solutions that rely on advanced concepts you haven't learned yet, break down a task into more steps than necessary, or import an excessive number of libraries. When you spot these issues, ask the AI to provide the simplest version that works, using only the essential libraries like pandas.

Request a basic approach first, and then progressively refine the solution if needed. This allows you to understand the core logic before adding complexity. By applying this simplicity check, you can ensure the code is easy to comprehend, maintain, and adapt to your specific business requirements.
:::


# 3. **Business Logic Check**: "Does this make sense for my problem?"

**Red Flags**:
- Ignores negative amounts (refunds)
- Doesn't handle missing data
- Makes assumptions about your business rules

**Your Response**:
- "How does this handle refunds and negative amounts?"
- "What happens if some categories are missing?"
- "Test this with edge cases"

::: {.notes}
The slide focuses on checking whether the code makes sense for your specific business problem. It highlights common issues such as ignoring negative amounts like refunds, not handling missing data properly, and making assumptions about your unique business rules. The bullet points provide examples of questions to ask when reviewing code, like how refunds and negative amounts are handled, what happens if certain categories are missing, and the importance of testing with edge cases.

Ensuring the code aligns with your business logic is crucial for generating meaningful and accurate results. By critically examining how the code deals with scenarios specific to your business, such as refunds, missing data, and edge cases, you can identify potential flaws or assumptions that may lead to incorrect outputs. Asking targeted questions and thoroughly testing the code with diverse datasets will help uncover any issues and ensure the analysis is tailored to your business needs.
:::


# 4. **Data Assumption Check**: "What is AI assuming about my data?"

**Red Flags**:
- AI assumes perfect, clean data
- No validation or error checking
- Hardcoded values

**Your Response**:
- "What assumptions are you making about my data?"
- "Add checks for common data issues"
- "Show me how to validate the input first"

::: {.notes}
AI assumes data is perfect and clean, without performing any validation or error checking. It may use hardcoded values instead of handling different data scenarios. To address this, ask AI, "What assumptions are you making about my data?" and request that it adds checks for common data issues. Have AI show you how to properly validate the input data first before processing it further.

When working with AI-generated code for data analysis, it's crucial to critically examine the data assumptions being made. AI may naively assume data is flawless, leading to incorrect results or system failures when encountering unexpected values or formats. By proactively questioning AI about its data assumptions and requiring robust input validation, you can ensure the code handles real-world data reliably. This step is key to developing trustworthy data pipelines and analyses.
:::


# 5. **Output Quality Check**: "Are the results useful for business?"

**Red Flags**:
- Results are hard to interpret
- No business context in output
- Poor formatting for presentation

**Your Response**:
- "Format this for presenting to a manager"
- "Add Australian dollar signs and proper rounding"
- "Include context about what these numbers mean"

::: {.notes}
The slide "5. **Output Quality Check**: "Are the results useful for business?"" emphasises the importance of producing output that is relevant and valuable for business purposes. It highlights common issues with AI-generated results, such as being hard to interpret, lacking business context, and having poor formatting for presentation. The examples show how to guide AI to produce more business-friendly output, like "Format this for presenting to a manager", "Add Australian dollar signs and proper rounding", and "Include context about what these numbers mean".

Checking the output quality is a critical step in the 5-step critique framework for reviewing AI-generated code. The slide stresses that the results should be easily understandable, properly formatted, and contextualised for the business problem at hand. By ensuring the output meets these criteria, the AI-generated code can be more effectively utilised and integrated into business processes and decision-making.
:::


# Common AI Code Issues in Business Data Analysis

1. Overcomplicated Pandas Operations
2. Ignoring Data Quality
3. Poor Business Interpretation

::: {.notes}
Here are the presenter notes for the slide "Common AI Code Issues in Business Data Analysis":

This slide highlights three prevalent issues that can arise when using AI-generated code for business data analysis. First, AI may suggest overcomplicated Pandas operations that are difficult to understand and maintain. Instead, it's better to break the analysis down into clear, step-by-step operations. Second, AI code might ignore data quality issues, so it's important to validate the data first, such as removing non-numeric amounts and handling negative values. Third, AI can sometimes provide results that lack proper business interpretation or context.

Throughout this presentation, we've covered key topics related to working effectively with AI in a business context. These include the importance of thorough code review, understanding the business impact of poor code, and having a structured critique framework. The five-step critique process involves checks for comprehension, simplicity, business logic, data assumptions, and output quality. By applying these principles and being aware of common pitfalls, you can leverage AI-generated code more effectively to drive business insights and decision-making.
:::


# Issue 1: Overcomplicated Pandas Operations

**AI Tendency**: Uses complex multi-level operations
```python
# AI might suggest this complex approach:
result = df.pivot_table(values='Amount', index='Date', columns='Category', aggfunc='sum').fillna(0).sum(axis=0).sort_values(ascending=False)
```

**Your Direction**: "Break this into clear steps"
```python
# Much better - step by step
monthly_spending = df.groupby('Category')['Amount'].sum()
monthly_spending = monthly_spending.sort_values(ascending=False)
```

::: {.notes}
AI-generated code for pandas operations can be unnecessarily complex, making it difficult to understand and maintain. Instead of accepting convoluted code, ask the AI to break down the solution into clear, step-by-step operations that are easy to follow and debug.

For example, rather than a single, dense line of code, request a series of simpler operations that group the data, calculate the required metrics, and present the results in a readable format. This approach will result in more maintainable code that aligns with business requirements and can be efficiently reviewed and updated as needed.
:::


# Issue 2: Ignoring Data Quality

**AI Tendency**: Assumes perfect data
```python
# AI might write this:
total = df['Amount'].sum()
```

**Your Direction**: "Check for data issues first"
```python
# Better - validate data first
# Remove any non-numeric amounts and handle negatives
df['Amount'] = pd.to_numeric(df['Amount'].str.replace('$', ''), errors='coerce')
df = df.dropna(subset=['Amount'])  # Remove invalid amounts
total = df['Amount'].sum()
```

::: {.notes}
AI-generated code may overlook data quality issues, leading to inaccurate or misleading results. It's crucial to validate and clean the data before performing any analysis. This includes checking for missing values, outliers, inconsistencies, and ensuring the data is in the correct format.

The slide illustrates an example where the AI code fails to handle non-numeric and negative values in the transaction amounts. To address this, the presenter suggests removing any non-numeric amounts and properly handling negative values before proceeding with the analysis. By prioritising data quality, the results will be more reliable and useful for making business decisions.
:::


# Issue 3: Poor Business Interpretation

**AI Tendency**: Technical output only
```python
print(spending_by_category.head())
```

**Your Direction**: "Make this business-friendly"
```python
print("📊 Monthly Spending Summary")
print("=" * 30)
for category, amount in spending_by_category.head().items():
    print(f"{category}: ${amount:.2f}")
print(f"\nTotal Monthly Spending: ${spending_by_category.sum():.2f}")
```

::: {.notes}
AI code suggestions can sometimes fall short in interpreting business problems effectively. Issues may include oversimplifying complex business logic, making incorrect assumptions about data, or generating outputs that aren't useful for decision-making.

When reviewing AI-generated code for business data analysis, carefully consider whether the approach truly captures the nuances and edge cases of your specific business context. Don't hesitate to push back and ask for revisions if the code seems to miss important aspects of the problem you're trying to solve.
:::


# Your Critique Conversation Templates

## Template 1: Asking for Simplification
*"This solution looks more complex than needed. I'm working on a business assignment and need code that's easy to understand and explain. Can you give me a simpler approach using just basic pandas operations?"*

## Template 2: Checking Business Logic
*"I'm analyzing personal spending data. This code needs to handle refunds (negative amounts) and missing categories properly. Can you update it to address these business requirements and explain your approach?"*

## Template 3: Requesting Clarity
*"I need to understand every line of this code for my assignment documentation. Can you add detailed comments explaining what each section does and why it's necessary for the business analysis?"*

## Template 4: Testing Edge Cases
*"Before I trust this code with real data, let's test it. Can you show me what happens if the CSV has missing values, or if amounts are formatted as text with dollar signs?"*

::: {.notes}
Your Critique Conversation Templates provide a set of phrases and questions to guide your interactions with the AI model when reviewing code. These templates cover key areas such as asking for simplification, checking business logic, requesting clarity and testing edge cases. By using these templates, you can ensure that you are effectively communicating your requirements and expectations to the AI, and that the generated code meets your needs.

The templates are designed to be adaptable and can be customised to suit your specific project or use case. They serve as a starting point for your conversations with the AI, helping you to structure your feedback and critique in a clear and concise manner. By incorporating these templates into your workflow, you can streamline the code review process and improve the quality of the AI-generated code, ultimately leading to better outcomes for your business data analysis tasks.
:::


# Your Developer's Diary Documentation

After each AI interaction, document your critique process:

**Template**:
```
# AI Interaction #[number]
**My Request**: [What I asked for]
**AI's First Response**: [Brief summary]
**My Critique**: [What I questioned or requested to improve]
**Final Solution**: [What we ended up with]
**What I Learned**: [Key insight for next time]
```

**Example**:
```
# AI Interaction #3
**My Request**: Calculate spending by category from transactions.csv
**AI's First Response**: Complex pivot table with multiple operations in one line
**My Critique**: Asked for step-by-step approach with comments
**Final Solution**: Simple groupby with clear variable names and business formatting
**What I Learned**: Always ask for simple, commented versions first
```

::: {.notes}
Your Developer's Diary is a vital tool for tracking your interactions with the AI developer. It serves as a central repository where you document each conversation, including the prompts you provide, the AI's responses, and your reflections on the code quality and any issues identified.

Maintaining a well-organised and detailed Developer's Diary is crucial for several reasons. It allows you to keep a historical record of your progress, enabling you to refer back to previous interactions and track the evolution of your project. The diary also facilitates effective communication with your team and stakeholders, providing a clear and transparent account of the development process. Additionally, it serves as a valuable resource for identifying patterns, recurring issues, and areas for improvement in your collaboration with the AI developer.
:::


# Red Flag Checklist for Your Assignment

Before accepting any AI code, ask:

- ☐ **Can I explain this code to someone else?**
- ☐ **Does it handle real-world messy data?**
- ☐ **Are the variable names business-friendly?**
- ☐ **Would this work with different CSV files?**
- ☐ **Are the results formatted for business presentation?**
- ☐ **Have I tested it with edge cases?**

::: {.notes}
Here is your checklist for reviewing AI-generated code before using it in your business data analysis assignment:

Can you explain the code to someone else? Does it handle real-world messy data? Are the variable names business-friendly? Would it work with different CSV files? Are the results formatted for business presentation? Have you tested it with edge cases?

If you can't confidently tick off all these items, ask the AI to revise the code. Request simplification, check the business logic matches your requirements, ask for clearer variable names and comments, and give examples of messy data to see how the code handles it. Keep iterating until you have code you fully understand and trust for your specific business scenario.
:::


# Practice: Spot the Issues

**AI Generated Code**:
```python
import pandas as pd
df = pd.read_csv('data.csv')
result = df.groupby(df.columns[2])[df.columns[1]].sum().sort_values()[::-1]
print(result)
```

**What's Wrong?** (Think before checking the answer)

<details>
<summary>Issues to Critique</summary>

1. **Unclear column references** - What are columns[1] and columns[2]?
2. **No data validation** - What if CSV format is different?
3. **Poor output formatting** - Not business-friendly
4. **No comments** - Hard to understand the purpose
5. **Confusing sorting** - Why the [::-1] slice?

**Your Response**: "Can you rewrite this with clear column names, add data validation, and format the output for business presentation?"

</details>

::: {.notes}
This slide, titled "Practice: Spot the Issues", serves as an interactive exercise for the audience to apply the knowledge and techniques covered in the previous slides. The presenter should engage the participants in identifying potential problems or areas for improvement in a given code sample or business analysis scenario.

The exercise aims to reinforce the key concepts discussed throughout the presentation, such as the importance of thorough code review, the 5-step critique framework, and common AI code issues in business data analysis. By actively participating in this practice session, attendees will gain hands-on experience in recognising and addressing these issues, better preparing them to effectively collaborate with AI in their own projects.
:::


# Ready for the Workshop

You now have the tools to:
- ✅ Direct AI like a junior developer
- ✅ Critique code for business appropriateness  
- ✅ Ensure solutions are understandable and maintainable
- ✅ Document your learning process

**In today's workshop, you'll put these critique skills into practice as you start building your Smart Finance Assistant with AI collaboration.**

Remember: **You're not just accepting AI code - you're improving it to meet professional business standards.**

---

Time to practice! Head to the workshop where you'll use these critique skills while starting your actual assignment.

::: {.notes}
🎉 Congratulations! You have now acquired the essential skills to effectively guide AI as a junior developer. You can confidently review AI-generated code for business suitability, ensuring solutions are comprehensible and sustainable. You have also learnt how to document your learning journey throughout the process.

✨ This workshop has equipped you with a robust 5-step critique framework to assess AI code. You can now perform comprehension checks, evaluate code simplicity, validate business logic, examine data assumptions, and assess output quality. With these tools, you are well-prepared to tackle common AI code issues in business data analysis, such as overcomplicated operations, data quality oversights, and poor business interpretation. Let's put your new skills into practice! 💪
:::
