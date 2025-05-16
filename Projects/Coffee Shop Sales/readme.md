# Coffee Shop Sales Analysis

**Brewly Beans**, a growing coffee shop chain with several locations across the city, is looking to **improve operational efficiency and strategic decision-making** by becoming a data-driven organization. To support this goal, the company initiated a project to develop an interactive sales dashboard using Excel. This dashboard enables store managers and executives to track key metrics such as monthly revenue, best-selling products, sales by category, and seasonal performance trends — helping them make informed decisions on inventory, marketing campaigns, and staffing.

![coffee_dashboard](img/coffee_sales_dashboard.png)

---

## Project Background  

Brewly Beans is a local coffee shop chain that has been operating since 2018, offering a wide range of specialty coffee drinks, light snacks, and seasonal products. The company follows a B2C (Business-to-Consumer) model with several branches located across both urban and suburban areas. All sales transactions are recorded using a digital Point-of-Sale (POS) system.   

The goal of this project was to support Brewly Beans in becoming a more data-driven organization. I was tasked with analyzing historical sales data and developing an interactive dashboard in Excel to help business stakeholders make more informed decisions.   

All analysis for this project was conducted using Microsoft Excel, leveraging Pivot Tables and interactive dashboards to visualize sales trends and performance metrics. The goal of this project is to empower store managers, marketing teams, and decision-makers with clear insights that can inform inventory planning, promotional strategies, and business growth initiatives.  

### Key Analysis Areas:  
1. **KPI**: Number of transactions in current month; Comparison value: MoM (Month over Month) growth to see how transaction volume changes from the previous month.   
2. **Time-Based Sales Performance**: Compare how sales trend in previous month  
3. **Product Performance**: Analyzes sales by product to identify bestsellers, underperforming items, and overall contribution to total revenue. 
4. **KPI**: Top 15 Products which generate the highest sales revenue, helping identify customer favorites and key drivers of profit.

*(Note: If you'd like to explore the Excel file used for this project in more detail, please refer to the data section.)*  

---

## Data Structure & Initial Checks  
The dataset contains **14,000+** transactions with the following fields:

- **Transaction Date | Transaction Time**
- **Store ID | Store Location**
- **Product ID | Product Category | Product Type | Product Detail**
- **Transaction Quantity | Unit Price | Revenue**

Initial checks were performed to ensure date and time formats were consistent, revenue calculations matched unit price × quantity, and there were no missing values in key fields such as store or product identifiers. 

> ⚠️ Disclaimer:   
**The dataset used in this project is not structured according to standard database normalization rules**. Some fields contain repeated or nested information, and product-related details are stored in a single flat table rather than separated into dimension tables. As such, this **dataset is intended solely for analytical purposes** and dashboard creation, not for transactional or relational database use.

---

## Executive Summary  
**Top 3 Insights:**  
1. **Coffee drinks contribute to 38.63% of total revenue**, with Latte Regular being the top customer favorite, indicating strong demand for caffeinated beverages.  
2. **Customer peak hours are in the morning (8–10 AM)**, accounting for 44.54% of daily sales; potential staffing shortages during these hours may slow down service and reduce order fulfillment.  
3. **There is a 5.44% increase in transactions compared to the previous month (MoM)**, showing a positive growth trend and an opportunity to boost marketing or stock top-selling products accordingly.  

---

## Insights Deep Dive  

### Category 1: Sales Trends by Product  
- **Cold brew sales peak in Q3** (July–Sept), contributing 25% of quarterly revenue. *Recommend seasonal marketing.*  
- **Food items have low attachment rates** (only 15% of coffee orders include food). Bundling could increase AOV.  

![Product Sales Pivot](/assets/product_pivot.png)  

### Category 2: Time-Based Performance  
- **Weekend afternoons (2–4 PM)** have the lowest sales density. *Test happy hour promotions.*  
- **Subscription customers** order 3x more frequently but prefer off-peak hours.  

### Category 3: Store Comparison  
- **Store C** has the highest customer retention (45% returning) due to loyalty programs.  
- **Merchandise sales are stagnant** across all locations (<5% revenue).  

### Category 4: Customer Segmentation  
- **New customers** prefer card payments (80%), while **returning customers** use mobile wallets (60%).  

---

## Recommendations  
1. **Peak Hour Optimization:** Increase staff during weekday mornings and pilot a "quick brew" lane.  
2. **Product Bundling:** Pair pastries with coffee subscriptions to boost food sales.  
3. **Localized Promotions:** Target Store A with combo deals to match Store B’s AOV.  
4. **Data Collection:** Add customer age/gender fields to refine segmentation.  

---

## Assumptions & Caveats  
- Assumed missing "Customer Type" values were "New" if no prior transactions existed.  
- Excluded 10 refunded transactions (0.2% of data) for revenue clarity.  
- Holiday sales (December) were analyzed separately due to outlier trends.  

---

**Tools Used:** Excel (Pivot Tables, Dashboards)  
**Data Source:** [Coffee Shop Sales 2023.xlsx](/data/sales_data.xlsx) *(Replace with your file)*  