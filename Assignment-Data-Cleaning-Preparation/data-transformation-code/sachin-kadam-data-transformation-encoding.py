import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

# Load the Titanic dataset
df = pd.read_csv('train.csv')

# One-Hot Encoding for 'Embarked'
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True)

# Label Encoding for 'Sex'
label_encoder = LabelEncoder()
df['Sex'] = label_encoder.fit_transform(df['Sex'])

