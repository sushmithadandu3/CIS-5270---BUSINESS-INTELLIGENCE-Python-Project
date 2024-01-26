import pandas as pd
import matplotlib.pyplot as plt

coffee = pd.read_csv('Cleaned_Coffee.csv')
print(coffee)

# Group data by product type and calculate total sales for each group
sales_by_product_type = coffee.groupby('Product Type')['Sales'].sum()

# Calculate total sales for all product types
total_sales = coffee['Sales'].sum()

# Calculate the percentage of sales for each product type
sales_pct = sales_by_product_type / total_sales * 100

# Set the colors for the pie chart
colors = ['#08519C', '#64B5F6', '#90CAF9', '#BBDEFB']

# Plot the pie chart
fig, ax = plt.subplots()
ax.pie(sales_pct, labels=sales_pct.index, autopct='%1.1f%%', startangle=90, colors=colors)
ax.set_title('Sales by Product Type')
plt.show()
