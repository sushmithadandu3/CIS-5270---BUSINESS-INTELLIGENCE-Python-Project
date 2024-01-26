# -*- coding: utf-8 -*-
"""
Created on Sat May 13 12:55:10 2023

@author: pyadav
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


coffee = pd.read_csv('Cleaned_Coffee.csv')
print(coffee)

# extract Profit, COGS, and Type columns
cogs = coffee['COGS']
profit = coffee['Profit']
Product_Line = coffee['Product Line']

# Create a scatter plot
plt.scatter(profit[Product_Line == 'Beans'], cogs[Product_Line == 'Beans'], c='#56B4E9', label='Beans')
plt.scatter(profit[Product_Line == 'Leaves'], cogs[Product_Line == 'Leaves'], c='#08519C', label='Leaves')
plt.xlabel('Cogs(Cost Of Goods)')
plt.ylabel('Profit')
plt.title('Correlation between Cogs and Profit for Product Line')
plt.legend(title='Product Line')
plt.show()






