import pandas as pd
import matplotlib.pyplot as plt
import os

print("Level 2 - Task 3 Running...")


os.makedirs("Outputs", exist_ok=True)


df = pd.read_csv("Dataset/dataset .csv")

print("Dataset Loaded")


plt.figure()

plt.scatter(df['Longitude'], df['Latitude'])

plt.title("Restaurant Locations Map")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.savefig("Outputs/restaurant_map.png")
plt.show()

print("\n Map created and saved")