from newsapi import NewsApiClient
from datetime import datetime, timedelta
import json
import os
import csv
file_path = 'total_articles.json'  # Replace with your file path

if not os.path.exists(file_path):
# Init
    newsapi = NewsApiClient(api_key='4d74ea7094ff4072a06d93c27f7789b9')
    start_date = datetime(2023, 11, 5)
    end_date = datetime(2023, 12, 5)
    current_date = start_date
    articles = []
    while current_date <= end_date:
        date = current_date.strftime('%Y-%m-%d')
        current_date += timedelta(days=1)
        num = 1
        while True : 
            top_headlines = newsapi.get_everything(qintitle='Taylor Swift',language='en',sort_by='relevancy', from_param=date, to = date, page = num)
            articles.extend(top_headlines['articles'])
            num_results =len(top_headlines['articles'])-100
            num += 1
            if num_results<0:
                break

    with open('total_articles.json', 'w', encoding="utf-8") as file:
        json.dump(articles, file, ensure_ascii=False)


with open('total_articles.json', 'r', encoding="utf-8") as file:
     articles = json.load(file)

articles_map = {}
selected_articles = []
length = 0
for i in articles[::2]:
    source = i['source']['name']
    if source!='[Removed]' and source!='Biztoc.com' and source!= 'Slashdot.org':
        if source in articles_map:
            if not articles_map[source]>100:
                selected_articles.append(i)
                articles_map[source]+=1
                length+=1
        else:
            selected_articles.append(i)
            articles_map[source]=1
            length+=1
        if length>=500:
            break

with open('selected_articles.json', 'w', encoding="utf-8") as file:
    json.dump(selected_articles, file, ensure_ascii=False, indent=4)
    

with open('selected_articles.json', 'r', encoding="utf-8") as file:
     particles = json.load(file)

print(len(particles))
data = [['Source', 'Title', 'url', 'Category']]

for i in particles:
    row = []
    row.append(i['source']['name'])
    row.append(i['title'])
    row.append(i['url'])
    row.append("")
    data.append(row)

file_path = 'data.csv'

# Writing data to a CSV file
with open(file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"Data has been written to '{file_path}'")
