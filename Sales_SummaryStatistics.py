# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:44:08 2023

@author: pyadav
"""


import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

#Read the CSV file into the dataframe
coffee = pd.read_csv('Cleaned_Coffee.csv')
#print(coffee)
print('\nSummary of the Sales column:\n' + str(coffee['Sales'].describe()))
print('\nPrinting individual statistics for the Sales:')
print('\nMean of the Sales:', "{0:.2f}".format(coffee.Sales.mean()))
print('\nMinimum of the Sales:', "{0:.2f}".format(coffee.Sales.min()))
print('\nMaximum of the Sales:', "{0:.2f}".format(coffee.Sales.max()))
print('\nMedian of the Sales:', "{0:.2f}".format(coffee.Sales.median()))
print('\nStandard Deviation of the Sales:', "{0:.2f}".format(coffee.Sales.std()))
coffee['Sales'].plot(kind='box')
plt.show()


