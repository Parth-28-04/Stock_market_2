#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the Dataset
file_path = 'C:\\Users\\chandrakanta\\Desktop\\GME_stock.csv'  # Replace with your actual file name
stock_data = pd.read_csv(file_path)

# Display the first few rows
print(stock_data.head())

# Step 2: Data Cleaning and Preprocessing

# Convert 'date' to datetime format
stock_data['date'] = pd.to_datetime(stock_data['date'])

# Check for missing values

print(stock_data.isnull().sum())

# Fill missing values (if necessary)
stock_data.fillna(method='ffill', inplace=True)

# Step 3: Exploratory Data Analysis (EDA)

# Plot closing price over time
plt.figure(figsize=(12, 6))
plt.plot(stock_data['date'], stock_data['close_price'], label='Close Price')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Plot volume traded over time
plt.figure(figsize=(12, 6))
plt.plot(stock_data['date'], stock_data['volume'], label='Volume Traded', color='orange')
plt.title('Volume Traded Over Time')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# Calculate and plot the correlation matrix
correlation_matrix = stock_data[['open_price', 'high_price', 'low_price', 'close_price', 'adjclose_price', 'volume']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Step 4: Feature Engineering

# Calculate daily returns
stock_data['daily_return'] = stock_data['close_price'].pct_change()

# Calculate moving averages
stock_data['10_day_ma'] = stock_data['close_price'].rolling(window=10).mean()
stock_data['50_day_ma'] = stock_data['close_price'].rolling(window=50).mean()

# Display the updated dataset
print(stock_data.head())

# Step 5: Save the cleaned and updated dataset (optional)
stock_data.to_csv('C:\\Users\\chandrakanta\\Desktop\\GME_stock.csv', index=False)

