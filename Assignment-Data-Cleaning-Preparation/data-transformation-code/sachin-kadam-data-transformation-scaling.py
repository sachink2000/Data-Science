import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the Titanic dataset
df = pd.read_csv('train.csv')

# Select numerical columns to scale
numerical_cols = ['Age', 'Fare', 'SibSp', 'Parch']

# Standardize numerical columns (mean=0, std=1)
scaler = StandardScaler()
df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
