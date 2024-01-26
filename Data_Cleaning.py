# -*- coding: utf-8 -*-
"""
Created on Fri May 12 09:24:13 2023

@author: pyadav
"""

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import seaborn as sns

#Read the CSV file into the dataframe
coffee = pd.read_csv('Coffee.csv')
#print(coffee)


#Before cleaning check
print(coffee['Type'])

#Convert the 'Type' column to title case using the apply() method
coffee['Type'] = coffee['Type'].apply(lambda x: x.title())

# Print the resulting DataFrame
print(coffee['Type'])



#View the information of the dataframe, col name, data type, total entries etc. 
#print(coffee.info())

# View the top 10 values
#print(coffee.head(10))

#Checking the Null values 
print(coffee.isnull().sum())
print('\n Profit has null rows:' + str(coffee['Profit'].isnull().sum()))


#Drop NAN values from the Profit column
coffee.dropna(subset=['Profit'], inplace=True)
print(coffee.isnull().sum())
print('\n Profit has null rows:' + str(coffee['Profit'].isnull().sum()))



# define lambda function to convert date integers to formatted strings
to_date_string = lambda x: datetime.fromordinal(datetime(1900, 1, 1).toordinal() + x - 2).strftime('%m/%d/%Y')
 
#apply lambda function to 'Date' column with formatted date strings
coffee['Date'] = coffee['Date'].apply(to_date_string)
 
#print(coffee)

# split date column into month, date, and year columns
coffee[['month', 'date', 'year']] = coffee['Date'].str.split('/', expand=True)

# print the modified dataframe
#print(coffee)

#print(coffee['Type'])
#Convert the 'Type' column to title case using the apply() method
coffee['Type'] = coffee['Type'].apply(lambda x: x.title())
print(coffee)

# Print the resulting DataFrame
print(coffee['Type'])


# Save the modified DataFrame to a new CSV file
coffee.to_csv('Cleaned_Coffee.csv', index=False)











