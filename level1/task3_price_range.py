import pandas as pd
import matplotlib.pyplot as plt
import os

print(" Task 3 Running...")

os.makedirs("Outputs", exist_ok=True)


df = pd.read_csv("Dataset/dataset .csv")

print(" Dataset Loaded")


price_counts = df['Price range'].value_counts().sort_index()

print("\n Price Range Distribution:")
print(price_counts)

# -------------------------------
# 2. Percentage calculation
# -------------------------------
percentage = (price_counts / price_counts.sum()) * 100

print("\n Percentage:")
print(percentage)

# -------------------------------
# 3. Bar Chart
# -------------------------------
plt.figure()
price_counts.plot(kind='bar')

plt.title("Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")

plt.show()

# -------------------------------
# Save output
# -------------------------------
price_counts.to_csv("Outputs/price_range_counts.csv")
percentage.to_csv("Outputs/price_range_percentage.csv")

print("\n Files saved in Outputs folder")