# Net Revenue Management Analysis

**HealthMax** is a Fast-Moving Consumer Goods (FMCG) company engaged in the personal care industry, one of its products is shampoo. Known for its commitment to quality and innovation, HealthMax continuously strives to strengthen its position in the competitive market by deeply understanding market dynamics and consumer behavior. The company is active in various marketing and promotional initiatives to ensure its products reach a wide target market.

---

## Project Background  

**HealthMax** is a *Fast-Moving Consumer Goods (FMCG)* company and one of its best products is Shampoo. As a data analyst, this project was initiated to conduct an in-depth analysis of net revenue management (NRM).   

This analysis will include identifying opportunities for net revenue optimization, evaluating the effectiveness of product pricing, and assessing the effectiveness of existing promotions. The results of this analysis are expected to provide strategic insights for HealthMax to make more informed decisions in terms of pricing, promotion allocation, and overall sales strategy, in order to maximize profitability and market share. 

## Key Findings:
1. **What has happened over the past few years?**: A review of historical sales data to understand unit sales volume and overall sales performance trends for HealthMax products over time.   
2. **Effectiveness of Pricing and Promotion Strategy**: An analysis to determine if the existing pricing and promotion strategies are effective in maximizing net revenue for HealthMax products. 
3. **Identifikasi Product Baru HealthMax**: Insights derived from market analysis and consumer trends to identify potential opportunities for new product development or expansion within the HealthMax product line.


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

## Metodologi Analisis
Metodologi untuk projek ini berupa analisis deskripsi, agnostistik, dan prediktif. Pemilihan metode ini dirancang untuk gambaran menyeluruh dari memahami kondisi penjualan HealthMax saat ini, mengevaluasi kinerja, dan melakukan prediksi tren di masa depan.

### Tools and Technology
| Tool / Fitur            | Deskripsi Penggunaan                                                                 |
|-------------------------|--------------------------------------------------------------------------------------|
| **Microsoft Excel 2021**     | Platform utama untuk analisis data, perhitungan metrik, dan visualisasi hasil.      |
| **Power Query**     | Digunakan untuk pra-pemrosesan dan transformasi data awal      |
| **PivotTable & PivotChart** | Digunakan untuk menyusun dan memvisualisasikan data berdasarkan dimensi tertentu.   |
| **Forecast Sheet**      | Digunakan untuk menghasilkan prakiraan pendapatan penjualan di masa depan berdasarkan data historis Anda.             |
| **Conditional Formatting** | Digunakan untuk menandai outlier dan pola data secara visual.                     |



## Insights Deep Dive 
### What has happened over the past few years?
**HEALTHMAX PRODUCTS**   
Untuk melihat performa HealthMax dalam beberapa tahun terakhir, analisis deskriptif dilakukan. Dalam dataset, data yang digunakan untuk meninjau performa penjualan dapat dilihat pada kolom *Values Month* dan *Units Month*. Saat ini, produk shampoo dari HealthMax hanya terdiri dari **Shinez** untuk anti-dandruff dan **Starbust** untuk volumizing. Grafik berikut menunjukkan performa kedua produk tersebut dari tahun ke tahun.

![HealthMax Products trends](./img/HealthMaxProductsTrends.png)   

Dari grafik, disimpulkan bahwa:
> Kedua produk mengalami **penurunan penjualan pada tahun 2019** dibandingkan dari tahun sebelumnya, namun Shinez menunjukkan pemulihan dan pertumbuhan signifikan di tahun 2020 dan **2022 mencapai 8,03% di 2022**, sedangkan Starbust menunjukkan pertumbuhan yang lebih lambat dan bahkan sedikit stagnasi di tahun 2022 yaitu mengalami kenaikan hanya 0,39%.

**HEALTHMAX MARKETSHARES**   
HealthMax bukan satu-satunya perusahaan di daerah ini, terdapat beberapa kompetitior yang bergerak dibidang yang sama. Grafik dibawah ini merupakan gambar pangsa pasar berdasarkan dataset.   

![HealthMax MarketShares](./img/HealthMax_MarketShares.png)   
Hingga tahun 2022, produk HealthMax mendominasi pasar dan paling banyak dibeli oleh customer dibandingkan pesaing lainya.   
> **HealthMax secara konsisten mempertahankan posisi dominan** dengan pangsa pasar sekitar **33-35%** setiap bulannya di tahun 2022, diikuti oleh *FreshCo Industries* dan *GreenLeaf Distributors* sebagai perusahaan terbesar lainnya.


**BAGAIAMAN PENJUALAN PRODUK HEALTHMAX SELAMA INI?**   
