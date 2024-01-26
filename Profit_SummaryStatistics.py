# -*- coding: utf-8 -*-
"""
Created on Sat May 13 16:48:59 2023

@author: pyadav
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

#Read the CSV file into the dataframe
coffee = pd.read_csv('Cleaned_Coffee.csv')
#print(coffee)
print('\nSummary of the Profit column:\n' + str(coffee['Profit'].describe()))
print('\nPrinting individual statistics for the Profit:')
print('\nMean of the Profit:', "{0:.2f}".format(coffee.Profit.mean()))
print('\nMinimum of the Profit:', "{0:.2f}".format(coffee.Profit.min()))
print('\nMaximum of the Profit:', "{0:.2f}".format(coffee.Profit.max()))
print('\nStandard Deviation of the Profit:', "{0:.2f}".format(coffee.Profit.std()))
coffee['Profit'].plot(kind='box')
plt.show()



