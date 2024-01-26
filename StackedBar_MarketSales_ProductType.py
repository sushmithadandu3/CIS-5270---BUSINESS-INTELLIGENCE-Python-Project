# -*- coding: utf-8 -*-
"""
Created on Mon May 15 09:34:54 2023

@author: pyadav
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the Coffee chain analysis dataset into a pandas DataFrame
coffee = pd.read_csv('Cleaned_Coffee.csv')

# Group the data by Market and Type columns and aggregate by sum
market_sales = coffee.groupby(['Market', 'Type'])['Sales'].sum().unstack()

# Calculate the total sales for each market
market_totals = market_sales.sum(axis=1)

# Sort the market_sales DataFrame by the total sales in descending order
market_sales_sorted = market_sales.loc[market_totals.sort_values(ascending=False).index]

# Define a list of color values for the two product types
colors = ['#08519C', '#BBDEFB']

# Create a stacked bar chart
market_sales_sorted.plot(kind='bar', stacked=True, color=colors)

# Set the title and labels for the chart
plt.title('Market Sales by Coefee Type')
plt.xlabel('Market')
plt.ylabel('Sales')
plt.legend(title='Coffee Type')

# Display the chart
plt.show()