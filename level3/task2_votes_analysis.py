import pandas as pd
import matplotlib.pyplot as plt
import os

print("Level 3 - Task 2 Running...")


os.makedirs("Outputs", exist_ok=True)


df = pd.read_csv("Dataset/dataset .csv")

print("Dataset Loaded")


highest_votes = df.sort_values(by='Votes', ascending=False).head(5)
lowest_votes = df.sort_values(by='Votes', ascending=True).head(5)

print("\nTop 5 Restaurants by Votes:")
print(highest_votes[['Restaurant Name', 'Votes']])

print("\nLowest 5 Restaurants by Votes:")
print(lowest_votes[['Restaurant Name', 'Votes']])


correlation = df['Votes'].corr(df['Aggregate rating'])

print("\nCorrelation between Votes & Rating:")
print(correlation)


plt.figure()

plt.scatter(df['Votes'], df['Aggregate rating'])

plt.title("Votes vs Rating")
plt.xlabel("Votes")
plt.ylabel("Rating")

plt.savefig("Outputs/votes_vs_rating.png")
plt.show()


highest_votes.to_csv("Outputs/highest_votes.csv")
lowest_votes.to_csv("Outputs/lowest_votes.csv")

print("\nFiles saved in Outputs folder")