import pandas as pd

# Load the dataset
df = pd.read_csv("superstore_sales.csv")

# Total sales by region
sales_by_region = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
top_region = sales_by_region.idxmax()
top_region_sales = sales_by_region.max()

# Total profit by region
profit_by_region = df.groupby("Region")["Profit"].sum().sort_values(ascending=False)
top_profit_region = profit_by_region.idxmax()
top_profit_value = profit_by_region.max()

# Total sales by category
sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
top_category = sales_by_category.idxmax()
top_category_sales = sales_by_category.max()

# Display results
print(f"Top region by sales: {top_region} (${top_region_sales:,.2f})")
print(f"Top region by profit: {top_profit_region} (${top_profit_value:,.2f})")
print(f"Top category by sales: {top_category} (${top_category_sales:,.2f})")
