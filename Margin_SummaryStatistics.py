# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:54:10 2023

@author: pyadav
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

#Read the CSV file into the dataframe
coffee = pd.read_csv('Cleaned_Coffee.csv')
#print(coffee)
print('\nSummary of the Margin column:\n' + str(coffee['Margin'].describe()))
print('\nPrinting individual statistics for the Margin:')
print('\nMean of the Margin:', "{0:.2f}".format(coffee.Margin.mean()))
print('\nMinimum of the Margin:', "{0:.2f}".format(coffee.Margin.min()))
print('\nMaximum of the Margin:', "{0:.2f}".format(coffee.Margin.max()))
print('\nStandard Deviation of the Margin:', "{0:.2f}".format(coffee.Margin.std()))
coffee['Margin'].plot(kind='box')
plt.show()









