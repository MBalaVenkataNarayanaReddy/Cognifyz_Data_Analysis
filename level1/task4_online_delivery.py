import pandas as pd
import os

print(" Task 4 Running...")

# Create Outputs folder
os.makedirs("Outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("Dataset/dataset .csv")

print(" Dataset Loaded")

# -------------------------------
# 1. Percentage of online delivery
# -------------------------------
delivery_counts = df['Has Online delivery'].value_counts()

percentage = (delivery_counts / delivery_counts.sum()) * 100

print("\n Online Delivery Percentage:")
print(percentage)

# -------------------------------
# 2. Average rating comparison
# -------------------------------
avg_rating = df.groupby('Has Online delivery')['Aggregate rating'].mean()

print("\n Average Ratings:")
print(avg_rating)

# -------------------------------
# Save outputs
# -------------------------------
percentage.to_csv("Outputs/online_delivery_percentage.csv")
avg_rating.to_csv("Outputs/online_delivery_ratings.csv")

print("\n Files saved in Outputs folder")