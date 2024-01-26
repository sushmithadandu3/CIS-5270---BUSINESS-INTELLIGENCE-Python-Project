import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
coffee = pd.read_csv('Cleaned_coffee.csv')

# Convert 'Date' column to datetime type
coffee['Date'] = pd.to_datetime(coffee['Date'])

# Create pivot table
table = pd.pivot_table(coffee, values='Sales', index='Date', columns='Product Type', aggfunc='sum')

# Create area chart
ax = table.plot(kind='area', stacked=False, alpha=0.7, figsize=(10,6), colormap='Pastel1')

# Add axis labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Sales')
ax.set_title('Trend of Sales by Product Type over Time')

# Show plot
plt.show()
