import pandas as pd
import os

print("Level 2 - Task 4 Running...")

os.makedirs("Outputs", exist_ok=True)


df = pd.read_csv("Dataset/dataset .csv")

print("Dataset Loaded")


chain_counts = df['Restaurant Name'].value_counts()

chains = chain_counts[chain_counts > 1]

print("\n🏢 Restaurant Chains:")
print(chains.head(10))


chain_analysis = df[df['Restaurant Name'].isin(chains.index)]

avg_ratings = chain_analysis.groupby('Restaurant Name')['Aggregate rating'].mean()
total_votes = chain_analysis.groupby('Restaurant Name')['Votes'].sum()


result = pd.DataFrame({
    'Average Rating': avg_ratings,
    'Total Votes': total_votes
}).sort_values(by='Total Votes', ascending=False)

print("\n⭐ Top Chains Analysis:")
print(result.head(10))


chains.to_csv("Outputs/restaurant_chains.csv")
result.to_csv("Outputs/chain_analysis.csv")

print("\n Files saved in Outputs folder")