import pandas as pd
import os

print("Level 2 - Task 2 Running...")


os.makedirs("Outputs", exist_ok=True)


df = pd.read_csv("Dataset/dataset .csv")

print(" Dataset Loaded")

df['Cuisines'] = df['Cuisines'].fillna('Unknown')

# -------------------------------
# 1. Most common combinations
# -------------------------------
combo_counts = df['Cuisines'].value_counts().head(10)

print("\n Top Cuisine Combinations:")
print(combo_counts)

# -------------------------------
# 2. Average rating per combination
# -------------------------------
combo_rating = df.groupby('Cuisines')['Aggregate rating'].mean()

top_rated_combos = combo_rating.sort_values(ascending=False).head(10)

print("\n Top Rated Cuisine Combinations:")
print(top_rated_combos)

# -------------------------------
# Save outputs
# -------------------------------
combo_counts.to_csv("Outputs/top_cuisine_combinations.csv")
top_rated_combos.to_csv("Outputs/top_rated_combinations.csv")

print("\n Files saved in Outputs folder")