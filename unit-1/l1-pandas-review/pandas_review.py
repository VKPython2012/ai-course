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
filtered_df = df_cleaned[(df_cleaned["BMI"] > 25) & (df_cleaned["Sleep_Hours"] > 7)]
print(f"\nFitlered DF (BMI > 25 % Sleep Hours > 7):")
print(filtered_df)

### Grouping & Aggregrating Data
# Group Data (by smoking status and calculate summary statistics)
grouped_df = filtered_df.groupby("Smoking_Status").agg(
    Avg_Health_Score = ("Health_Score", "mean"),
    Avg_Exercise = ("Exercise_Frequency", "mean"),
    Total_Alcohol_Consumption = ("Alcohol_Consumption", "sum")
).reset_index()
print(f"\nGrouped Data by Smoking Status")
print(grouped_df)

### Questions ###

questions = [
    "1. What is the average health scorer for smokers and non-smokers?",
    "2. How does BMI correlate with health score for individuals who exercise frequently?",
    "3. What is the total alcohol consumption for each smoking status group?",
    "4. What is the average exercise frequency among individuals with BMI over 30?",
    "5. How does the amount of sleep hours relate to health score on average?"
]

print("\nQuestions")
for q in questions:
    print(q)

# 1. What is the average health scorer for smokers and non-smokers?
avg_health_score = df_cleaned.groupby("Smoking_Status")["Health_Score"].mean().reset_index()
avg_health_score.rename(columns={"Health_Score":"Avg_Health_Score"}, inplace=True)
print('\n1. What is the average health scorer for smokers and non-smokers?')
print(avg_health_score)

# 2. How does BMI correlate with health score for individuals who exercise frequently?
# print(df_cleaned["Exercise_Frequency"].mean())
# print(df_cleaned["Exercise_Frequency"].quantile())
# print(df_cleaned["Exercise_Frequency"].max())
frequent_exercisers = df_cleaned[df_cleaned["Exercise_Frequency"] > 4]
colleration_BMI_health = frequent_exercisers[["BMI", "Health_Score"]].corr().iloc[0, 1]
print("\n2. How does BMI correlate with health score for individuals who exercise frequently?")
print(colleration_BMI_health)

# 3. What is the total alcohol consumption for each smoking status group?
total_alcohol_consumption = grouped_df[["Smoking_Status", "Total_Alcohol_Consumption"]]
print("\n3. What is the total alcohol consumption for each smoking status group?")
print(total_alcohol_consumption)

# 4. What is the exercise frequency among individuals with BMI over 30?"
avg_exercise_bmi_30 = df_cleaned[df_cleaned["BMI"] > 30]["Exercise_Frequency"].mean()
print("\n4. What is the exercisr frequency among individuals with BMI over 30?")
print(avg_exercise_bmi_30)