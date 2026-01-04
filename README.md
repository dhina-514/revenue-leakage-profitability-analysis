# Revenue Leakage & Profitability Analysis 📉📊

An end-to-end data analytics project that identifies **revenue leakage sources** using SQL, Python, and Power BI.  
The project helps businesses understand **why profits are declining despite healthy revenue** and provides actionable insights.

---

## 🔍 Problem Statement

Despite strong sales revenue, many businesses experience declining profitability due to:
- Excessive discounts
- High product returns
- Cost inefficiencies
- Poor regional performance

This project analyzes retail sales data to **identify loss-making products, regions, and discount patterns** that contribute to revenue leakage.

---

## 🛠 Tech Stack

- **Database:** MySQL  
- **Data Analysis:** Python (Pandas, Matplotlib)  
- **Visualization:** Power BI  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure

revenue-leakage-profitability-analysis/
│
├── python/
│ └── analysis.py # Data extraction & analysis
│
├── sql/
│ └── revenue_analysis.sql # Database schema & sample data
│
├── powerbi/
│ └── Revenue_Leakage_Analytics.pbix
│
├── screenshots/
│ └── dashboard.png
│
├── .gitignore
└── README.md



---

## 📊 Dataset Description

The dataset represents retail sales transactions with the following fields:

- Product name & category  
- Price, cost, discount  
- Quantity sold  
- Return flag  
- Region  
- Order date  

---

## 🔄 Data Pipeline (End-to-End Flow)

1. **Data Storage:** Sales data stored in MySQL  
2. **Data Extraction:** Python connects to MySQL using `mysql-connector`  
3. **Data Processing:** Profit calculated using Pandas  
4. **Analysis:** Loss-making products & regions identified  
5. **Visualization:** Interactive Power BI dashboard built on processed data  

---

## 🧮 Profit Formula Used

Profit = (Price − Cost − Discount) × Quantity


This formula highlights how **discounts and costs directly impact profitability**.

---

## 📈 Analysis Performed

- Total Revenue vs Total Profit
- Profit by Product
- Profit by Region
- Impact of Discounts on Profit
- Identification of Top Loss-Making Products

---

## 📊 Power BI Dashboard

![Dashboard](screenshots/dashboard.png)

### Dashboard Highlights:
- KPI cards for Revenue & Profit
- Top loss-making products
- Profit distribution by region
- Discount vs profit insights
- Interactive filters by category

---

## 💡 Key Business Insights

- High discounts are the **primary driver of revenue leakage**
- Certain products consistently generate losses
- Product returns significantly impact profitability
- Regional performance varies drastically
- Healthy revenue does **not guarantee profitability**

---

## 🎯 Outcome & Business Value

This project enables decision-makers to:
- Reduce unnecessary discounts
- Improve pricing strategies
- Optimize product portfolio
- Identify underperforming regions
- Make data-driven profitability decisions

---

## 🚀 Future Enhancements

- Automate data refresh using scheduled ETL
- Add time-series trend analysis
- Introduce customer-level profitability
- Deploy dashboard using Power BI Service

---

## 👤 Author

**Dinesh R**  
Aspiring Data Analyst / Data Engineer  

🔗 GitHub: https://github.com/dhina-514

