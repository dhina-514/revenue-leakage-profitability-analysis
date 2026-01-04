# ================================
# Revenue Leakage Analysis Project
# Python + MySQL
# ================================

import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# ----------------
# 1. CONNECT TO MYSQL
# ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",   # <-- CHANGE THIS
    database="revenue_analysis"
)

print("✅ Connected to MySQL")

# ----------------
# 2. LOAD DATA FROM SQL
# ----------------
query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)

print("\n📌 DATA FROM DATABASE:")
print(df)

# ----------------
# 3. CREATE PROFIT COLUMN
# ----------------
df["profit"] = (df["price"] - df["cost"] - df["discount"]) * df["quantity"]

print("\n📌 DATA WITH PROFIT:")
print(df[["product", "profit"]])

# ----------------
# 4. TOTAL REVENUE & PROFIT
# ----------------
total_revenue = (df["price"] * df["quantity"]).sum()
total_profit = df["profit"].sum()

print("\n💰 TOTAL REVENUE:", total_revenue)
print("💰 TOTAL PROFIT:", total_profit)

# ----------------
# 5. PROFIT BY PRODUCT
# ----------------
profit_by_product = df.groupby("product")["profit"].sum().sort_values()

print("\n📉 PROFIT BY PRODUCT:")
print(profit_by_product)

# ----------------
# 6. PROFIT BY REGION
# ----------------
profit_by_region = df.groupby("region")["profit"].sum()

print("\n🌍 PROFIT BY REGION:")
print(profit_by_region)

# ----------------
# 7. FIND LOSS-MAKING SALES (LEAKAGE)
# ----------------
loss_sales = df[df["profit"] < 0]

print("\n❌ LOSS MAKING SALES:")
print(loss_sales[["product", "profit", "discount", "return_flag"]])

# ----------------
# 8. VISUALIZATION
# ----------------
plt.figure()
profit_by_product.plot(kind="bar", title="Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.tight_layout()
plt.show()

# ----------------
# 9. CLOSE CONNECTION
# ----------------
conn.close()
print("\n🔒 MySQL Connection Closed")
