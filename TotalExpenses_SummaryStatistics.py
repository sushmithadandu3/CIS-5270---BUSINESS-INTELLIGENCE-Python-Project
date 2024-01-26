# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:50:18 2023

@author: pyadav
"""


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

# Read the CSV file into the dataframe
coffee = pd.read_csv('Cleaned_Coffee.csv')

# Print summary of the 'Total Expenses' column
print('\nSummary of the Total Expenses column:\n', coffee['Total Expenses'].describe())

# Print individual statistics for the 'Total Expenses'
print('\nMean of the Total Expenses:', "{0:.2f}".format(coffee['Total Expenses'].mean()))
print('\nMinimum of the Total Expenses:', "{0:.2f}".format(coffee['Total Expenses'].min()))
print('\nMaximum of the Total Expenses:', "{0:.2f}".format(coffee['Total Expenses'].max()))
print('\nStandard Deviation of the Total Expenses:', "{0:.2f}".format(coffee['Total Expenses'].std()))

# Plot a boxplot of the 'Total Expenses' column
coffee['Total Expenses'].plot(kind='box')
plt.show()