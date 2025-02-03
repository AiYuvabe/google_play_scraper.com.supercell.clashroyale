from google_play_scraper import app
import pandas as pd

# Fetch the app details
result = app(
    'com.supercell.clashroyale',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
)

# Convert the result dictionary into a DataFrame
df = pd.DataFrame([result])

# Save the DataFrame to a CSV file
df.to_csv("appdetails.csv", index=False, encoding='utf-8-sig')

print(df)

# import pandas as pd
# from google_play_scraper import Sort, reviews

# # Fetch the reviews
# result, continuation_token = reviews(
#     'com.supercell.clashroyale',
#     lang='en',
#     country='us', 
#     sort=Sort.NEWEST,
#     count=20, 
#     filter_score_with=5 
# )

# df = pd.DataFrame(result)

# # 1. Distribution of Ratings (In this case, all will be 5)
# rating_distribution = df['score'].value_counts()

# # 2. Total Number of Upvotes
# total_upvotes = df['thumbsUpCount'].sum()

# # 3. Male-to-Female Distribution (Data not available)
# gender_distribution = "Not available"

# # 4. Longest Review
# longest_review = df.loc[df['content'].str.len().idxmax()]['content']

# # 5. Frequency of Reviews
# review_frequency = df['at'].value_counts()

# # 6. Common Submission Times
# common_submission_times = df['at'].dt.hour.value_counts().sort_index()

# # 7. Overall Sentiment (With only 5-star, sentiment is positive)
# overall_sentiment = "Positive"

# # Save the DataFrame to a CSV file
# df.to_csv("review.csv", index=False, encoding='utf-8-sig')

# # Print results
# print("Rating Distribution:\n", rating_distribution)
# print("Total Upvotes: ", total_upvotes)
# print("Gender Distribution: ", gender_distribution)
# print("Longest Review: ", longest_review)
# print("Review Frequency:\n", review_frequency)
# print("Common Submission Times:\n", common_submission_times)
# print("Overall Sentiment: ", overall_sentiment)

