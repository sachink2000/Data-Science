# Import pandas libraries
import pandas as pd

# Load the 'train.csv' dataset
df = pd.read_csv('train.csv')

# Step 1: Check for missing values in each column
missing_values = df.isnull().sum()
print("Missing values before imputation:")
print(missing_values)

# Step 2: Impute missing values for each column based on their type

# For numerical columns (e.g., Age, Fare), we can use mean or median imputation
df['Age'] = df['Age'].fillna(df['Age'].median())  # Using median for Age, as it's less affected by outliers
df['Fare'] = df['Fare'].fillna(df['Fare'].mean())  # Using mean for Fare

# For categorical columns (e.g., Embarked), we can use mode imputation
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])  # Mode is the most frequent value

# Step 3: Verify if missing values have been handled
missing_values_after = df.isnull().sum()
print("\nMissing values after imputation:")
print(missing_values_after)

