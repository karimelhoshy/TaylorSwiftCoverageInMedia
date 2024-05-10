import pandas as pd
from textblob import TextBlob
import json
import matplotlib.pyplot as plt

# Open the JSON file and load its contents
with open('annoted_articles.json', 'r') as file:
    json_data = json.load(file)

description_array = []

for i in json_data:
    description_array.append(i['description'])


def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity of the text
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"


data = pd.read_csv('data.csv')
data = data.drop('Sentiment ', axis=1)
# Display the first few rows of the DataFrame

sentiment_array = []

for title in description_array:
    sentiment_array.append(analyze_sentiment(title))

data['Sentiment'] = sentiment_array

# Save the DataFrame as a CSV file
data.to_csv('output.csv', index=False)

# Group by 'sentiment' and 'category', count occurrences, and unstack to pivot the table
grouped = data.groupby(['Sentiment', 'Category']).size().unstack()

# Plotting the bar chart
grouped.plot(kind='bar', stacked=False, figsize=(10, 6))

# Adding labels and title
plt.xlabel('Sentiment')
plt.ylabel('Frequency')
plt.title('Frequency of Each Category for Different Sentiments')

# Show the plot
plt.legend(title='Category')
plt.tight_layout()
plt.show()


