# 📊 Sales Performance & Customer Analytics Dashboard

## Project Background
**OfficeTech Solutions** is a leading retailer specializing in furniture, office supplies, and technology products. 
Established in 2005, the company has been actively serving both individual consumers and businesses for over 18 years. 
OfficeTech Solutions operates in the retail and e-commerce industry, with a strong focus on providing high-quality products 
that enhance productivity and comfort in modern workspaces.

**OfficeTech Solutions** relies heavily on data-driven insights to stay competitive. 
My work involves analyzing sales data, customer behavior, and market trends to provide actionable recommendations.
*This project thoroughly analyzes this data in order to uncover insights that will improve
company success.*  

Insights and recommendations are provided on the following key areas:

- **Sales Trend Analysis**: Evaluation of historical sales patterns, focusing on revenue, total profit, and quantity.
- **Product Level Performance**: Evaluating the performance of individual products to determine best-sellers, underperformers, and opportunities for optimization.
- **RFM Segmentation**: Categorizing customers based on Recency, Frequency, and Monetary value to tailor marketing strategies and improve customer retention.

An interactive Tableau dashboard used to report and explore sales trends and customers can be found here [Sales & Customer Dashboard](https://public.tableau.com/shared/HZM8MSM38?:display_count=n&:origin=viz_share_link).


## 📚 Table of Contents
- [Data Structures](#-data-sources)
- [Business Questions](#-business-questions)
- [Executive Summary](#-executive-summary)
- [Contributing](#-contributing)
- [License](#-license)

## 📂 Data Structures
| Source | Description
|--------|-------------
| [Orders](data/Orders.csv) | Historical transaction records
| [Customer Demographics](data/Customers.csv) | Customer demographic data 
| [Location](data/Location.csv) | Orders taking place 
| [Product Detail](data/Products.csv) | Product metadata 

## ❓ Business Questions
This dashboard answers critical business questions:
1. How did **sales, profits, and product quantity perform** between this year and the previous year?
2. How is the **trend of sales, profit, and quantity** per month compared to the previous year?
3. How is the **relationship between sales and profit in each product subcategory?** Are there any subcategories that are experiencing losses?
4. How do the **total number of customers, total sales per customer, and total number of orders** this year compare to the previous year?
5. Who are the **Top 10 customers** with the highest profit  for the company, and how do they contribute to total sales  and profit?


## 🔍 Executive Summary

### Overview of Findings
Customer engagement grew significantly, with total customers up 8.6% and orders increasing 28.3% from last year, showing strong retention and acquisition. Sales rose 20.4% to $733K, driven by a 10.8% increase in sales per customer, but profit only grew 4.1%, suggesting a need for better cost control or pricing strategies. Key product categories like phones and chairs performed well, while machines and tables saw losses, highlighting areas for improvement to boost overall profitability.

Below is the overview dashboard from Tableau for Sales and Customer Analysis:
<div align="center">
  <table>
    <tr>
      <td width="50%">
        <img src="img/Sales Dashboard.png" alt="Sales Dashboard">
        <p align="center"><em>Sales Performance Dashboard</em></p>
      </td>
      <td width="50%">
        <img src="img/Customers Dashboard.png" alt="Customer Analytics Dashboard">
        <p align="center"><em>Customer Analytics Dashboard</em></p>
      </td>
    </tr>
  </table>
</div>

### Sales Trend Analysis:
- **In 2023, the company's sales peaked in November 2023 with total sales of $733k, which was an increase of 20.4% from last year**.  This growth can be attributed to several factors, including a significant rise in the total quantity of products sold, driven by increased demand during the holiday season and the success of targeted marketing campaigns. 
- Despite a significant increase in total sales, **profit growth was limited to 4.1% year-over-year**, indicating rising costs or margin pressures. The highest profit margin occurred in **March 2023**, surging by **38.8%** compared to the same month in the previous year, reflecting a period of exceptional financial performance.

### Product Level Performance:
- **The technology category emerged as the top-performing segment** in terms of sales volume, followed by furniture, while office supplies ranked the lowest. This trend suggests a decline in the use of traditional office items, such as envelopes and fasteners, likely driven by the shift toward digital solutions and modern workplace practices.

### Customers Analysis:
- The total number of customers grew by 8.6%, while total orders increased by 28.3% compared to the previous year. This suggests improved customer retention and higher purchase frequency per customer.
- Average sales per customer rose by 10.8%, indicating stronger spending behavior. However, sales fluctuations throughout the year highlight periods of peak and low engagement, requiring targeted strategies to maintain consistency.
- A small group of high-value customers generated a large portion of the company's profit, with the top 10 customers contributing significantly. Strengthening relationships with these key customers and expanding similar customer segments could further enhance profitability.

## 🧭 Recommendation
Based on the findings, here are actionable recommendations to address key challenges and capitalize on opportunities:

1. Optimize Profit Margins:   
- **Review Cost Structures**: Conduct a detailed analysis of operational costs to identify areas for reduction, particularly in underperforming product categories like machines and tables.   
- **Adjust Pricing Strategies**: Consider revising pricing for high-demand products (e.g., phones and chairs) to improve margins without compromising sales volume.

2. Enhance Product Portfolio
- **Focus on High-Performing Categories**: Allocate more resources to the technology and furniture categories, which are driving sales, while phasing out or redesigning underperforming products like traditional office supplies.   
- **Introduce Bundles or Promotions**: Create product bundles (e.g., desks with chairs or tech accessories) to increase average order value and clear slow-moving inventory.

3. Leverage Customer Insights
- **Target High-Value Customers**: Develop personalized loyalty programs or exclusive offers for the top 10% of customers who contribute significantly to profits.

- **Boost Retention and Frequency**: Implement targeted marketing campaigns during low-engagement periods to encourage repeat purchases and maintain consistent sales throughout the year.

4. Improve Operational Efficiency:
- **Invest in Digital Transformation**: Accelerate the shift toward digital solutions to align with declining demand for traditional office supplies and modernize the product offering.