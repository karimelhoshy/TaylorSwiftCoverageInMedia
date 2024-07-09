# Taylor Swift in North American Media

This repository contains the project files and documentation for the analysis of Taylor Swift's portrayal in North American media.

## Project Overview

This project explores how Taylor Swift is depicted in North American media, focusing on the sentiments expressed and the prevalent themes. By diving into these aspects, we gain valuable insights into the media's portrayal tactics and how the public perceives Taylor Swift.

## Data Collection

For this project, we used NewsAPI to gather our dataset. Given the limitations of the developer accounts, we made separate calls on each date, looking for articles mentioning "Taylor Swift" and sorting by relevance. We then took the most relevant 100 articles per day, filtering out articles from Biztoc.com and Slashdot.org, which simply linked to other articles. We aimed to minimize bias by ensuring diversity in our sources.

## Methodology

### Typology Building

We randomly sampled 200 articles from our dataset and divided them among team members to develop initial typologies. After the annotation process, we established clear definitions for our final typologies, which include:

- Love Life
- Branding
- Music
- Concert
- Celebrity Mention
- Personal Life
- Culture

### TF-IDF Calculation

We calculated the TF-IDF scores for each word in their respective categories using the formula, limiting the analysis to the article descriptions due to truncation by NewsAPI.

### Sentiment Analysis

We created a Python script to automate the sentiment analysis of articles, categorizing them as positive, negative, or neutral using a sentiment score. We utilized the TextBlob module for this task and validated our results by comparing a subset of articles manually.

## Results

### Typology Analysis

Our typology analysis revealed distinct themes in the media portrayal of Taylor Swift. Each category showed specific top words reflecting their respective themes. For example, the "Love Life" category included words related to relationships and football, while the "Music" category featured words related to albums and awards.

### Sentiment Analysis

The sentiment analysis showed a generally positive portrayal of Taylor Swift across all categories. The "Music" category had the highest frequency of positive articles, while the "Love Life" category had a noticeable amount of negative articles. The "Culture" category had a significant number of neutral articles.

## Discussion

The limitations of NewsAPI's developer account features restricted our dataset to the last 30 days and to article descriptions. For a more comprehensive analysis, future work should include a larger variety of articles and a more detailed analysis of the full article content.

The unexpected results in our TF-IDF analysis, such as the prevalence of news-related words in the "Culture" category and celebrity names in the "Personal Life" category, highlight the need for further refinement in our methodology.

