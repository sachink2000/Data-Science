# Import necessary libraries
import pandas as pd

# Load the dataset train.csv
df = pd.read_csv('train.csv')

# Check for missing values in each column
missing_values = df.isnull().sum()

# Print the result
print(missing_values)