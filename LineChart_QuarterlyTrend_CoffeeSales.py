# -*- coding: utf-8 -*-
"""
Created on Thu May 11 16:50:17 2023

@author: pyadav
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import seaborn as sns

#Read the CSV file into the dataframe
coffee = pd.read_csv('Cleaned_Coffee.csv')
print(coffee)


#1. What is the quarterly trend of coffee sales? 


coffee['Date'] = pd.to_datetime(coffee['Date'], format='%m/%d/%Y')
coffee['Quarter'] = coffee['Date'].dt.quarter
coffee['Year'] = coffee['Date'].dt.year
coffee = coffee[['Year', 'Quarter', 'Sales']]

# Group the data by year and quarter, and calculate the total sales
coffee = coffee.groupby(['Year', 'Quarter']).sum().reset_index()

# Filter the data for the years 2012 and 2013
coffee_2012 = coffee[coffee['Year'] == 2012]
coffee_2013 = coffee[coffee['Year'] == 2013]

# Plot the data for 2012 and 2013 using different colors
plt.plot(coffee_2012['Quarter'], coffee_2012['Sales'], color='blue', marker='o', label='2012') 
plt.plot(coffee_2013['Quarter'], coffee_2013['Sales'], color='orange', marker='o', label='2013')

# Set the plot title and axis labels
plt.title('Quarterly Trend of Coffee Sales')
plt.xlabel('Quarter')
plt.ylabel('Sales')

# Set the x-axis ticks and tick labels
plt.xticks([1, 2, 3, 4], ['Q1', 'Q2', 'Q3', 'Q4'])

# Add a legend to the plot
plt.legend()

# Show the plot
plt.show()









