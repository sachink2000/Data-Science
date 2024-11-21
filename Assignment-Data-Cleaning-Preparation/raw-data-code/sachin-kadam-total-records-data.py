import pandas as pd

# Load the dataset
data = pd.read_csv('train.csv')

# Get the total number of records (rows)
total_records = data.shape[0]

# Print the total number of records
print(f'Total number of records: {total_records}')
