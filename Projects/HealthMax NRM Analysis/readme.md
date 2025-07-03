# Net Revenue Management Analysis


## Project Background  
**HealthMax** is a Fast-Moving Consumer Goods (FMCG) company engaged in the personal care industry, one of its products is shampoo. Known for its commitment to quality and innovation, HealthMax continuously strives to strengthen its position in the competitive market by deeply understanding market dynamics and consumer behavior. The company is active in various marketing and promotional initiatives to ensure its products reach a wide target market.

This analysis will include identifying opportunities for net revenue optimization, evaluating the effectiveness of product pricing, and assessing the effectiveness of existing promotions. The results of this analysis are expected to provide strategic insights for HealthMax to make more informed decisions in terms of pricing, promotion allocation, and overall sales strategy, in order to maximize profitability and market share. 

## Executive Summary 
This project conducts an in-depth Net Revenue Management (NRM) analysis for HealthMax's shampoo products to identify optimization opportunities and enhance profitability. Our findings reveal HealthMax's consistent market dominance, alongside a critical insight: while sales value has grown, unit sales volume has declined since 2020. This analysis further identifies optimal pricing strategies for key products and highlights the clear effectiveness of specific promotional mechanics (e.g., "Buy 2, Get 20% Off") through strong ROI. Moving forward, we recommend leveraging high-margin, high-contribution products, refining promotional investments based on profitability, and capitalizing on the identified growth potential within the organic product category to secure HealthMax's continued market leadership and profitability.

## Key Findings:
1. **What has happened over the past few years?**: A review of historical sales data to understand unit sales volume and overall sales performance trends for HealthMax products over time.   
2. **Effectiveness of Pricing and Promotion Strategy**: An analysis to determine if the existing pricing and promotion strategies are effective in maximizing net revenue for HealthMax products. 
3. **HealthMax New Product Identification**: Insights derived from market analysis and consumer trends to identify potential opportunities for new product development or expansion within the HealthMax product line.


## Data
This Net Revenue Management (NRM) analysis leverages a comprehensive dataset specifically designed to capture key sales and performance metrics for HealthMax's shampoo products. The data provides a granular view of market activities, enabling a detailed assessment of revenue drivers. 

*(Note: If you'd like to explore the Excel file used for this project in more detail, please refer to the data section.)* 

The columns are structured as follows:
- ***Category***: High-level product grouping (e.g., "Shampoo").
- ***Subcategory***: More specific product type within the category (e.g., "Anti-dandruff").
- ***Supplier***: The entity supplying the product (e.g., "Apex Trading Co.").
- ***Brand***: The specific brand of the product (e.g., "RedRose").
- ***Region***: The geographical sales region (e.g., "Center").
- ***Year***: The year of the sales data.
- ***Month***: The month of the sales data (represented numerically, 1-12).
- ***Units Month***: Total units sold within that specific month.
- ***Values Month***: Total revenue generated within that specific month.
- ***Units YTD***: Cumulative units sold from the beginning of the year up to the current month.
- ***Values YTD***: Cumulative revenue generated from the beginning of the year up to the current month.
- ***Units MAT***: Total units sold over the last 12 months (Moving Annual Total).
- ***Values MAT***: Total revenue generated over the last 12 months (Moving Annual Total).

## Methodology of Analysis
The methodology for this project was descriptive, agnostic, and predictive analysis. The selection of these methods was designed for a comprehensive overview of understanding HealthMax's current sales conditions, evaluating performance, and predicting future trends.

### Tools and Technology
| Tools             | Description                                                                 |
|-------------------------|--------------------------------------------------------------------------------------|
| **Microsoft Excel 2021**     | The ultimate platform for data analysis, metrics calculation, and results visualization.      |
| **Power Query**     | Used for pre-processing and initial data transformation      |
| **PivotTable & PivotChart** | Used to organize and visualize data based on certain dimensions.   |
| **Forecast Sheet**      | Used to generate forecasts of future sales revenue based on historical data.             |


## Insights Deep Dive 
### What has happened over the past few years?
**HEALTHMAX PRODUCTS**   
To look at HealthMax's performance in recent years, a descriptive analysis was performed. In the dataset, the data used to review sales performance can be seen in the *Values Month* and *Units Month* columns. Currently, HealthMax's shampoo products only consist of **Shinez** for anti-dandruff and **Starbust** for volumizing. The following chart shows the performance of these two products year-on-year.

![HealthMax Products trends](./img/HealthMaxProductsTrends.png)   

From the graph, it can be concluded that:
> Both products experienced a **decrease in sales in 2019** compared to the previous year, but Shinez showed significant recovery and growth in 2020 and **reaching 8.03% in 2022**, while Starbust showed slower growth and even a slight stagnation in 2022 with an increase of only 0.39%.

**HEALTHMAX MARKETSHARES**   
HealthMax is not the only company in this area, there are several competitors in the same field. The graph below shows the market share based on the dataset. 

![HealthMax MarketShares](./img/HealthMax_MarketShares.png)   
Until 2022, HealthMax products dominate the market and are the most purchased by customers compared to other competitors.   
> **HealthMax has consistently maintained its dominant position** with a market share of approximately **33-35%** on a monthly basis in 2022, followed by *FreshCo Industries* and *GreenLeaf Distributors* as the other largest companies.


**HOW HAVE SALES OF HEALTHMAX PRODUCTS BEEN?**   
HealthMax's sales performance has shown interesting dynamics in recent years. While the volume of units sold has tended to decline overall since 2020, the value of sales has shown a steady upward trend, especially in recent years. 
<table>
  <tr>
    <td style="width: 50%; padding: 10px;">
      <img src="./img/HealthMax_Sales.png" alt="HealthMax Sales Trends" style="width: 100%;">
    </td>
    <td style="width: 50%; padding: 10px;">
      <img src="./img/HealthMax_Solds.png" alt="HealthMax Unit Solds Trends" style="width: 100%;">
    </td>
  </tr>
</table>   

- **Units Sold**; from the graph “HealthMax Unit Solds Trends” it is known that a decline in unit sold volume occurred from 2018 to 2019, with a slight increase in 2020 (marked “Covid 2019”) which then became the starting point of a continuous unit decline trend until 2022. This implies the potential impact of the pandemic or changes in consumer behavior that reduce unit sales volume gradually.
- **Sales**; In contrast, the “HealthMax Sales Trends” chart displays a consistent recovery and growth in sales value from 2020, reaching a peak of $31,443K in 2022. This shows that despite the decline in unit volume, HealthMax managed to increase total revenue.

### Effectiveness of Pricing and Promotion Strategy   
**EFFECTIVENESS OF PRICING**   
For the scope of this project, let's assume that the elasticity of HealthMax consumers is the same as FMCG consumers for other daily products. Consumers for this product have high elasticity, where if the price of the product changes slightly; the sales volume decreases.   
Is the pricing of HealthMax products optimal? It should be noted from HealthMax products (judging from the analysis in the previous section) that HealthMax is the dominating product among other shampoo products. To be more convincing, let's look at the following graph:

![HealthMax_profitMatrix](./img/HealthMax_profitMatrix.png)

The chart visualizes the price effectiveness and **contribution of each HealthMax shampoo** product to the company's *net revenue* in 2022, by comparing Gross Margin (%) and Net Sales Contribution (%).   
- The chart clearly highlights **Starbust Ultra Soft 100ml** as the flagship product with the best combination of a high **Gross Margin** of 71% and the largest **net sales contribution** of 18%. This indicates that the product is very effectively priced and a key revenue driver,

- Other products such as **Shinez Repair 100ml** also showed a high sales contribution of 19%, but with a slightly lower gross margin of 67%, 

- While **Starbust Strong Hair 100ml** is in the lower quadrant with lower gross margin and sales contribution, indicating an opportunity to review pricing or promotion strategies to increase profitability or sales volume.

> Based on purchase patterns, it appears that consumers favor 100ml shampoo products over other sizes. This indicates that consumers like compact shampoo products (small, compact, and space-saving size). 

**EFFECTIVENESS OF PROMOTION**   
During 2022, HealthMax conducted 3 promotions for Shinez products, in April, August, and November. To have an overall idea of how it affected sales see the graph below.

![Shinez_sales](./img/Shinez_sales.png
)


Based on the “HealthMax's Shinez Sales In 2022” chart, it is clear that sales of Shinez products show significant volatility throughout the year, with notable peaks. Sharp increases in sales in April, August, and November coincided with different promotional periods (Buy 2 Get 1 Free, Buy 2 Get 20% Off, and 2nd at 50% Off respectively), indicating consumers' positive response to the incentives. Although Shinez is said to have performed slightly worse than other HealthMax products, these promotions managed to drive a spike in sales above the monthly average. This suggests that promotions are an effective tool to boost the sales volume of Shinez, although further analysis is required to evaluate the net profitability of each promotion type.

*But which promotion is more effective?* 
The following table details the promotions applied to Shinez products.

![promotion_table](./img/promotion_table.png)

> There are 3 promotions applied in each month, to see the effectiveness of which promotion is the best can be seen in ROI (Return Of Investments). The “buy 2, get 20% off” promotion turned out to be more effective so this promotion might be applied by the marketing team for the next promotion.

--- 

### NEW PRODUCT OPPORTUNITIES
The HealthMax Product Team decided to release a new product. The first thing they did was market research. Using Excel's *PivotTables*, this was easy to do.

![UnitSoldsGrowth for each Category](./img/product_growth.png)

Based on the data, shampoo products in the **Organic** category experienced the highest unit sales growth compared to other products. In 2022, the unit sales of organic shampoo products increased by 22.86% from the previous year.

Therefore, the product team decided to launch a new product for the *Organic* category. This will add the HealthMax product category, which previously only had *Anti-dandruff* and *Volumizing* product categories.

Currently, there are two products that are planned to be added, namely: **HerbEssentials** and **HerbaShine**. To determine which one will generate the highest profit, calculations were made to calculate the estimated gross margin (%). The product with the highest estimated gross margin is the product that will be launched.

![newProduct_calc](./img/newProduct_calc.png)

Based on the calculation, the product to be launched is **HerbaShine** because this product is estimated to generate a gross margin of 67%.

## Recommendation

Based on an in-depth analysis of HealthMax's sales data, market share, product profitability and promotional effectiveness, the data analysis team has identified several key areas for Net Revenue Management (NRM) optimization. The following recommendations aim to maximize profitability and strengthen HealthMax's market position by leveraging product strengths, optimizing promotional investments, and exploring new growth opportunities identified in the market.

### 1. Prioritize Promotion Mechanisms with Proven Positive ROI (Focus on “Buy 2, Get 20% Off”)
The promotion analysis for Shinez products explicitly showed that the “Buy 2, Get 20% Off” mechanism in August 2022 generated the highest positive ROI of 11.84%. In contrast, the “Buy 2, Get 1 Free” promotion showed a negative ROI (-2.45%), indicating financial ineffectiveness. Optimizing the promotional budget allocation to strategies that prove to be profitable will directly increase net revenue.

### 2. Product Portfolio Optimization by Encouraging High Contribution and High Margin Products
The HealthMax Profit Matrix identified Starbust Ultra Soft 100ml as the flagship product with a Gross Margin of 71% and the highest net sales contribution of 18%. Such products are the key drivers of profitability and should be maximized. On the other hand, products with lower margins and contribution (e.g. Starbust Strong Hair 100ml) need to be evaluated. Focusing on superior performing products will optimize overall net revenue. 

### 3. Capitalize on Organic Category Growth with HerbaShine Launch and Further Exploration
Data shows that the Organic category has the highest unit sales growth of 22.86% in 2022, indicating strong market demand in this segment. The decision to launch HerbaShine with an estimated gross margin of 67% is the right move to capitalize on profitability in a growing category.

Accelerate the launch process of HerbaShine. In addition, HealthMax should continue to monitor organic market trends and explore the potential of expanding to other organic product lines, or even adapting existing products (e.g. Shinez or Starbust) to organic variants, to further capture this growing market share and diversify revenue sources. 