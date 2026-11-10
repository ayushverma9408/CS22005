import pandas as pd

data = {
    "Name": ["Ayush", "Rahul", "Priya", "Rahul"],
    "Age": [19, 20, None, 20],
    "Marks": [85, None, 92, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Age to integer
df["Age"] = df["Age"].round().astype(int)

print("\nCleaned Data:")
print(df)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved to cleaned_data.csv")