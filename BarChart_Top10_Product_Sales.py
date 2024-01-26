# -*- coding: utf-8 -*-
"""
Created on Sun May 14 12:21:15 2023

@author: pyadav
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns
import numpy as np

#Read the CSV file into the dataframe
coffee = pd.read_csv('Cleaned_Coffee.csv')
print(coffee)


# Calculate the total sales for each product
product_sales = coffee.groupby('Product').sum().sort_values('Sales', ascending=False)

# Get the top 10 products
top_products = product_sales[:10]

# Define the color map
color_map = plt.cm.get_cmap('Blues')

# Create a bar chart of the top products with sales
ax = top_products.plot(kind='bar', y='Sales', legend=False, color=color_map(np.linspace(1.0, 0.2, len(top_products))))

# Set the title and axis labels
ax.set_title('Top 10 Coffee Products Sales for the year 2012 and 2013')
ax.set_xlabel('Product')
ax.set_ylabel('Total Sales')

# Rotate the x-axis labels to vertical view
plt.xticks(rotation=90)

# Display the plot
plt.show()

