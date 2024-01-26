# -*- coding: utf-8 -*-
"""
Created on Sat May 13 17:09:49 2023

@author: pyadav
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

#Read the CSV file into the dataframe
coffee = pd.read_csv('Cleaned_Coffee.csv')
print(coffee)

# Creating a dataframe and grouping the columns
coffee_product = coffee.groupby(['State', 'month'])['Sales'].sum().reset_index() 

 
# Pivot dataframe to create heatmap data 
heatmap_data = pd.pivot_table(coffee_product, values='Sales', index=['State'], columns=['month']) 

# Create heatmap using Seaborn 
sns.heatmap(heatmap_data, cmap='Blues') 


# Set plot title and axis labels 

plt.title('Monthly Sales of Coffee Products by States') 
plt.xlabel('month') 
plt.ylabel('State') 

 
# Display the plot 
plt.show()




