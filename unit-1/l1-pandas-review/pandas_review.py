# pandas_review.py
import pandas as pd
import plotly.express as px

# Load the csv
df = pd.read_csv("unit-1/l1-pandas-review/data.csv")

# Initial Data Inspection
print("Print first 5 rows")
print(df.head(5))

# Display stats of the df
print("\nDataFrame Info")
print(df.describe(include="all"))

# Data Cleanup
# Filter out all rows where age/BMI/Sleep/Health are non-pos
df_cleaned = df[
    (df["Age"] > 0) &
    (df["BMI"] > 0) &
    (df["Sleep_Hours"] > 0) &
    (df["Health_Score"] > 0)
].copy()

# Fill missing values
df_cleaned["Diet_Quality"].fillna(df_cleaned["Diet_Quality"].mean(), inplace=True)
df_cleaned["Exercise_Frequency"].fillna(0, inplace=True)

# Filtering Data
# Filter rows where BMI > 25 & Sleep Hours > 7
