---
title: "STAFF ANSWER: Designing a Smart Inventory System: Justifying Decisions"
subtitle: "Applying Analytical Thinking to Inventory Management"
author: "Michael Borck"
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

Activity 1: Conceptual Application & Analysis

1. Key considerations for choosing a dictionary-based approach:
   - Efficient storage and retrieval of inventory data using the key-value structure
   - Ability to easily associate product information (e.g., name, SKU, quantity) with a unique identifier (the key)
   - Suitability for handling a large and dynamic inventory with frequent updates

2. Potential challenges and limitations of using a dictionary:
   - Handling complex inventory data that may require more structure than a simple key-value pair
   - Potential performance issues for large inventories or frequent updates (dictionary lookups have O(1) time complexity, but the underlying hash table implementation can degrade with many collisions)
   - Difficulty in maintaining order or sorting of inventory items (dictionaries are unordered)
   - Limitations in reporting and aggregating inventory data compared to more structured data models

3. Structuring the dictionary:
   - Use product SKU or unique ID as the dictionary key
   - Store relevant inventory information as the value, such as:
     - Product name
     - Quantity in stock
     - Reorder threshold
     - Supplier information
   - Consider using nested dictionaries or other data structures within the values to handle more complex inventory data

Activity 2: Evaluation, Comparison, and Justification

1. Key principles and assumptions of JIT and EOQ:
   - Just-in-Time (JIT):
     - Principle: Produce or deliver goods only as they are needed, minimizing inventory
     - Assumptions: Reliable and frequent supplier deliveries, stable demand, low setup costs
   - Economic Order Quantity (EOQ):
     - Principle: Determine the optimal order quantity to minimize total inventory costs
     - Assumptions: Constant and known demand, fixed ordering and holding costs

2. Advantages and disadvantages of JIT and EOQ for the given business scenario:
   - JIT advantages: Reduced inventory costs, less waste, improved cash flow
   - JIT disadvantages: Reliance on reliable suppliers, potential stock-outs, sensitivity to demand changes
   - EOQ advantages: Systematic approach to determining optimal order quantities, lower ordering costs
   - EOQ disadvantages: Requires accurate demand forecasting, potential for excessive inventory

3. Recommendation and justification:
   Given the small size of the business and the potential for demand fluctuations, the EOQ strategy may be more suitable. The EOQ approach provides a structured way to balance ordering and holding costs, which aligns better with the business owner's needs. While JIT can offer cost savings, the risk of stock-outs may be too high for a small retail business. The EOQ strategy provides a more stable and predictable inventory management system, which is likely more suitable for the given scenario.

Extension: Integrating Concepts

1. Modifying the dictionary structure:
   - Add a "reorder_level" key to track the minimum inventory level that triggers a reorder
   - Include a "forecast" key to store predicted future demand for each product
   - Consider using a nested dictionary to group related inventory data (e.g., product details, sales history, reorder information)

2. Algorithms and techniques for automated reordering and forecasting:
   - Automated reordering:
     - Monitor inventory levels and trigger a reorder when the "reorder_level" is reached
     - Use the EOQ formula to determine the optimal reorder quantity
   - Forecasting:
     - Implement a simple moving average or exponential smoothing algorithm to predict future demand
     - Use the forecasted demand to update the "forecast" key in the dictionary

3. Potential challenges and mitigation strategies:
   - Handling exceptions and edge cases (e.g., sudden demand spikes, supplier issues)
   - Ensuring data integrity and consistency as the inventory system grows more complex
   - Integrating the dictionary-based system with other business systems (e.g., sales, accounting)
   - Scaling the system to handle a larger, more diverse inventory

Reflection:

1. The analytical and evaluative skills practiced in this activity can be applied to other complex, real-world problems that require critical thinking, problem-solving, and justification of design choices. These skills are valuable in software engineering, project management, and various other fields.

2. AI tools were used to explain the underlying principles of JIT and EOQ in a different way, which helped deepen the understanding for the justification needed in Activity 2. The AI's suggestions were critically evaluated to assess their relevance and significance for the expanded inventory management system in the Extension activity.

3. Critically evaluating information and justifying choices was challenging, as it required a deep understanding of the concepts and the ability to apply them to a specific business scenario. The process was insightful, as it forced me to consider multiple perspectives, anticipate potential issues, and provide well-reasoned arguments to support the recommended solutions.