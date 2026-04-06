import pandas as pd
import matplotlib.pyplot as plt
import os

print("Level 3 - Task 3 Running...")


os.makedirs("Outputs", exist_ok=True)


df = pd.read_csv("Dataset/dataset .csv")

print("Dataset Loaded")


delivery_analysis = pd.crosstab(df['Price range'], df['Has Online delivery'])

print("\nPrice vs Online Delivery:")
print(delivery_analysis)


table_analysis = pd.crosstab(df['Price range'], df['Has Table booking'])

print("\nPrice vs Table Booking:")
print(table_analysis)


delivery_analysis.plot(kind='bar', stacked=True)

plt.title("Price Range vs Online Delivery")
plt.xlabel("Price Range")
plt.ylabel("Count")

plt.savefig("Outputs/price_vs_delivery.png")
plt.show()


table_analysis.plot(kind='bar', stacked=True)

plt.title("Price Range vs Table Booking")
plt.xlabel("Price Range")
plt.ylabel("Count")

plt.savefig("Outputs/price_vs_table.png")
plt.show()


delivery_analysis.to_csv("Outputs/price_vs_delivery.csv")
table_analysis.to_csv("Outputs/price_vs_table.csv")

print("\nFiles saved in Outputs folder")