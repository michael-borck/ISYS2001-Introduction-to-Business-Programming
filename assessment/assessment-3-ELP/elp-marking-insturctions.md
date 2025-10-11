---
format:
  pdf:
    toc: true
    number-sections: false
    colorlinks: true
  docx:
    toc: true
    number-sections: false
    highlight-style: github
  html:
    toc: true
    toc-expand: 2
    embed-resources: true
---

# Tutor Tips/Instructions for Marking

1. **Clone the Student Repository:**
   - Clone the repository using the `git clone` command. Ensure you are accessing the correct branch if multiple branches are present.
   - **Command:**  
     ```bash
     git clone <student_repository_url>
     ```
   - Check that all work is contained in the repository, including the notebook, code, and any additional files required for marking.

2. **Review Commit History and Comments:**
   - Open the commit history and look through the commit messages.
   - **Checkpoints:**
     - Are commits frequent, indicating iterative work?
     - Are messages descriptive, detailing changes in a meaningful way?
     - If any messages appear as "generic" (e.g., "fix," "update"), verify whether the commit content aligns with the message.
   - **Red Flags for AI Usage:**  
     - Unusual gaps in the timeline, suggesting rapid completion of complex tasks.
     - Large commits with minimal changes over time, indicating possible copying.
   - **Action:** If you suspect AI-generated work, mark it down, and add a comment in the spreadsheet for review. Michael will address any appeals.

3. **Open and Run Notebooks in Google Colab:**
   - Download or open the student notebook in Google Colab.
   - **Execution Verification:** Run each cell from top to bottom to ensure:
     - The notebook is functional and that cells execute correctly without errors.
     - All dependencies are properly imported and the code runs as expected.
   - **Output Verification:** Check outputs for correctness and whether results align with the code provided.
   - **Non-Text Answers:** Where there are visualisations or interactive elements, ensure the output matches the instructions.

4. **Evaluate Process and Reasoning:**
   - Look for clear explanations within the notebook or accompanying documentation:
     - Did the student explain the approach they took and any assumptions?
     - Have they described their design decisions, explaining why they chose certain methods or steps?
   - **Process Evaluation:** Assess the logical flow of their work. For example:
     - Are functions modular and reusable?
     - Is data handled efficiently and accurately?
     - Do the steps follow a structured methodology?
   - **Deduct Marks:** If the process is missing explanations or lacks clarity in design decisions, deduct marks accordingly. The focus is not just on the correct answer but also on understanding and communicating their approach.

5. **Documentation and Comments:**
   - **Code Comments:** Ensure that code is adequately commented, with explanations for complex logic or less intuitive parts of the code.
   - **External Documentation:** Check if students provided any additional documentation files or explanations (Word documents, PDFs) that clarify their work.



6. **Summary for Feedback:**
   - Write a brief summary of strengths and areas of improvement.
   - Note any areas of concern related to academic integrity or AI usage.
   - Highlight specific instances of good explanations or clear logic that contributed positively to the overall solution.
