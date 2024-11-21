# Import necessary libraries
import pandas as pd

# Load the dataset train.csv
df = pd.read_csv('train.csv')

# Check for duplicate rows
duplicates = df.duplicated().sum()

# Print the number of duplicate rows
print(f"Number of duplicate rows: {duplicates}")
print(f"Number of duplicate coloums: {duplicates}")
