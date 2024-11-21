import pandas as pd

# Load the dataset
data = pd.read_csv('train.csv')
df = pd.read_csv('train.csv')

# Get the column names
column_names = data.columns

# Print the column names
print(df.columns)
print("Column names:")
print("Summary Statistics:")
print(data.describe(include='all')) # this provide descriptive statistics for each column