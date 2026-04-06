import pandas as pd
import os

print(" Task 2 Running...")

# Create Outputs folder if not exists
os.makedirs("Outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("Dataset/Dataset .csv")

print(" Dataset Loaded")

# -------------------------------
# 1. City with highest restaurants
# -------------------------------
city_counts = df['City'].value_counts()

top_city = city_counts.idxmax()
top_count = city_counts.max()

print("\n City with highest restaurants:")
print(top_city, "-", top_count)

# -------------------------------
# 2. Average rating per city
# -------------------------------
avg_rating = df.groupby('City')['Aggregate rating'].mean()

print("\n Average rating per city:")
print(avg_rating.head())  # first few only

# -------------------------------
# 3. City with highest avg rating
# -------------------------------
best_city = avg_rating.idxmax()
best_rating = avg_rating.max()

print("\n City with highest average rating:")
print(best_city, "-", best_rating)

# -------------------------------
# Save outputs
# -------------------------------
city_counts.to_csv("Outputs/city_counts.csv")
avg_rating.to_csv("Outputs/avg_rating_per_city.csv")

print("\n Files saved in Outputs folder")