import pandas as pd
import os

print("Level 3 - Task 1 Running...")


os.makedirs("Outputs", exist_ok=True)


df = pd.read_csv("Dataset/dataset .csv")

print("Dataset Loaded")


df['Rating text'] = df['Rating text'].fillna('Unknown')


word_counts = df['Rating text'].value_counts()

print("\nMost Common Review Words:")
print(word_counts)


df['review_length'] = df['Rating text'].apply(len)

avg_length = df['review_length'].mean()

print("\nAverage Review Length:")
print(avg_length)


relation = df.groupby('Rating text')['Aggregate rating'].mean()

print("\nRating vs Review Text:")
print(relation)


word_counts.to_csv("Outputs/review_word_counts.csv")
relation.to_csv("Outputs/review_rating_relation.csv")

print("\nFiles saved in Outputs folder")