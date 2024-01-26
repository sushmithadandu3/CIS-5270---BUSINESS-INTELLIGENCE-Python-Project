# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:28:49 2023

@author: sushm
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
coffee = pd.read_csv('Cleaned_coffee.csv')

# Create a histogram
sns.histplot(x='Total Expenses', hue='Product Type', data=coffee)

# Add title and labels
plt.title('Distribution of Total Expenses by Product Type')
plt.xlabel('Total Expenses')
plt.ylabel('Count')

# Show the plot
plt.show()
