import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("superstore_sales.csv")

print("Dataset loaded successfully")
print(df.head())

# Sales by Region
sales_region = df.groupby("Region")["Sales"].sum()

plt.figure()
sales_region.plot(kind="bar")
plt.title("Total Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_region.png")

# Sales by Category
sales_category = df.groupby("Category")["Sales"].sum()

plt.figure()
sales_category.plot(kind="bar")
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")

# Profit by Region
profit_region = df.groupby("Region")["Profit"].sum()

plt.figure()
profit_region.plot(kind="bar")
plt.title("Total Profit by Region")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("profit_by_region.png")

print("Charts created successfully.")

# Advanced insights (makes it look like a real analyst project)
top_region_sales = sales_region.idxmax()
top_region_profit = profit_region.idxmax()
best_category_sales = sales_category.idxmax()

highest_sales_value = sales_region.max()
highest_profit_value = profit_region.max()
highest_category_sales_value = sales_category.max()

print("\n=== Key Business Insights ===")
print(f"Region with highest sales: {top_region_sales} (${highest_sales_value:,.2f})")
print(f"Region with highest profit: {top_region_profit} (${highest_profit_value:,.2f})")
print(f"Product category with highest sales: {best_category_sales} (${highest_category_sales_value:,.2f})")