---
title: "STAFF ANSWER: Mastering Dictionaries: Unlocking Insights from Business Data"
subtitle: "Analyse, Evaluate, and Justify Your Decisions with Dictionaries"
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

## Activity 1: Conceptual Application & Analysis

1. To calculate the total revenue generated from the sales data:

   - Iterate through the `sales_data` dictionary using a `for` loop or the `items()` method.
   - For each product, multiply the `price` and `qty_sold` values to get the revenue for that product.
   - Sum up the individual product revenues to get the total revenue.

   Example code:
   ```python
   total_revenue = 0
   for product_id, product_data in sales_data.items():
       revenue = product_data['price'] * product_data['qty_sold']
       total_revenue += revenue
   print(f"Total revenue: ${total_revenue:.2f}")
   ```

   Potential challenges:
   - Handling missing or invalid data in the dictionary (e.g., missing price or quantity sold).
   - Accounting for discounts, taxes, or other factors that may impact the final revenue calculation.

2. To determine the best-selling product:

   - Iterate through the `sales_data` dictionary and keep track of the product with the highest `qty_sold` value.
   - Use the `max()` function with a `key` parameter to find the product with the maximum quantity sold.

   Example code:
   ```python
   best_selling_product = max(sales_data.items(), key=lambda x: x[1]['qty_sold'])
   print(f"The best-selling product is {best_selling_product[1]['name']} with {best_selling_product[1]['qty_sold']} units sold.")
   ```

   Explanation:
   - The `max()` function is used to find the key-value pair with the maximum `qty_sold` value.
   - The `key` parameter in `max()` specifies that we want to compare the values of the `qty_sold` field for each product.
   - The resulting `best_selling_product` variable contains the product ID and its corresponding data dictionary, from which we can extract the product name and quantity sold.

## Activity 2: Evaluation, Comparison, and Justification

To evaluate the two new product options and recommend the better one:

1. Calculate the potential monthly revenue for each new product:
   - Product A: $19.99 x 50 units = $999.50
   - Product B: $14.75 x 80 units = $1,180.00

2. Compare the potential monthly revenue:
   - Product B has a higher potential monthly revenue of $1,180.00 compared to $999.50 for Product A.

3. Justify the recommendation:
   - Based on the potential monthly revenue, Product B would be the better addition to the business. The higher estimated sales volume and slightly lower price point for Product B result in a higher overall revenue potential compared to Product A.

   Additional factors to consider (per the AI tip):
   - Production costs and profit margins for each product
   - Potential cannibalization of existing product sales
   - Customer demand and market trends for the new product types

   By considering these additional factors, you can provide a more comprehensive justification for the recommendation.

## Extension: Combining Concepts

1. Calculate the total revenue generated from all products:
   ```python
   total_revenue = 0
   for product_data in sales_data.values():
       total_revenue += product_data['price'] * product_data['qty_sold']
   print(f"Total revenue: ${total_revenue:.2f}")
   ```

2. Determine the product with the highest total revenue:
   ```python
   highest_revenue_product = max(sales_data.items(), key=lambda x: x[1]['price'] * x[1]['qty_sold'])
   print(f"The product with the highest total revenue is {highest_revenue_product[1]['name']}")
   ```

3. Calculate the average price of all products:
   ```python
   total_price = sum(product_data['price'] for product_data in sales_data.values())
   average_price = total_price / len(sales_data)
   print(f"The average price of all products is ${average_price:.2f}")
   ```

Explanation:
- For the total revenue, we iterate through the values in the `sales_data` dictionary and multiply the price and quantity sold for each product, then sum the results.
- To find the product with the highest total revenue, we use the `max()` function with a `key` parameter that calculates the total revenue for each product (price * quantity sold) and returns the product with the maximum value.
- To calculate the average price, we sum the prices of all products and divide by the number of products in the `sales_data` dictionary.

## Reflection

1. The analytical and evaluative skills practiced with dictionaries can be applied to many other data structures and problem domains, such as:
   - Analyzing and manipulating complex data structures (e.g., nested dictionaries, lists of dictionaries) to extract insights.
   - Choosing appropriate data representations (e.g., lists, sets, dataframes) to model and solve problems effectively.
   - Evaluating the trade-offs and suitability of different data structures for specific use cases.
   - Justifying design decisions and data analysis approaches based on the characteristics and capabilities of the chosen data structures.

2. In this worksheet, I used AI tools to suggest alternative approaches and identify additional factors to consider when evaluating the new product options. The AI's suggestions helped me broaden my perspective and incorporate more comprehensive considerations into my justification. However, I carefully examined the AI's outputs, verified their relevance and accuracy, and adapted them to fit the specific requirements of the task.

3. Critically evaluating information and justifying choices was challenging, as it required me to think critically about the assumptions, limitations, and potential biases in the data and analysis. It was insightful to consider alternative viewpoints and factors that could impact the decision-making process. This exercise helped me develop a more holistic and nuanced approach to problem-solving and decision-making.