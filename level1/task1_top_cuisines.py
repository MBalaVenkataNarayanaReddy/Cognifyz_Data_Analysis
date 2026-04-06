import pandas as pd

print(" Code is running...")

# Load dataset
df = pd.read_csv("Dataset/Dataset .csv")

print(" Dataset loaded")

# Check columns
print("Columns:", df.columns)

# Handle cuisines
df['Cuisines'] = df['Cuisines'].fillna('Unknown')
cuisines_series = df['Cuisines'].str.split(', ').explode()

# Top 3 cuisines
top_cuisines = cuisines_series.value_counts().head(3)

print("\nTop 3 Cuisines:")
print(top_cuisines)

# Percentage
total = len(cuisines_series)
percentage = (top_cuisines / total) * 100

print("\nPercentage:")
print(percentage)

# Save output
top_cuisines.to_csv("Outputs/top_cuisines.csv")
print("\n File saved in Outputs folder")

