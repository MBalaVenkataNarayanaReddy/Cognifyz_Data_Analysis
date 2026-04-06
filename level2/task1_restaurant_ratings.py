import pandas as pd
import matplotlib.pyplot as plt
import os

print(" Level 2 - Task 1 Running...")

os.makedirs("Outputs", exist_ok=True)

df = pd.read_csv("Dataset/dataset .csv")

print(" Dataset Loaded")


rating_counts = df['Aggregate rating'].value_counts().sort_index()

print("\n Rating Distribution:")
print(rating_counts.head())

# -------------------------------
# 2. Most common rating
# -------------------------------
most_common_rating = df['Aggregate rating'].mode()[0]

print("\n Most Common Rating:")
print(most_common_rating)

# -------------------------------
# 3. Average votes
# -------------------------------
avg_votes = df['Votes'].mean()

print("\n Average Votes:")
print(avg_votes)

# -------------------------------
# Graph
# -------------------------------
plt.figure()
rating_counts.plot(kind='hist', bins=10)

plt.title("Rating Distribution")
plt.xlabel("Ratings")
plt.ylabel("Frequency")

plt.savefig("Outputs/rating_distribution.png")
plt.show()

# -------------------------------
# Save outputs
# -------------------------------
rating_counts.to_csv("Outputs/rating_counts.csv")

print("\n Files saved in Outputs folder")