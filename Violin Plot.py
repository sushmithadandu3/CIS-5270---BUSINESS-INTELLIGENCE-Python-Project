# -*- coding: utf-8 -*-
"""
Created on Sat May 13 14:08:52 2023

@author: sushm
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
coffee = pd.read_csv('Cleaned_coffee.csv')

# Create a violin plot
sns.violinplot(x='Product Line', y='Margin', data=coffee)

# Add title and labels
plt.title('Distribution of Profit Margin by Product Line')
plt.xlabel('Product Type')
plt.ylabel('Profit Margin')

# Show the plot
plt.show()
