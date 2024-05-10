import json

import csv

# File path
file_path = '370Data.csv'

annotions ={}
urls ={}
placeholder = ""
# Open the CSV file
with open(file_path, newline='') as csvfile:
    # Create a CSV reader
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    print(f'Header: {header}')
    num = 1
    # Read the rows
    for row in csv_reader:
        url = row[2].lower()
        urls[url] = row[3]
        if row[3] in annotions:
            annotions[row[3]]+=1
        else:
            annotions[row[3]]=1


# Now, you can save the JSON data to a file
with open('selected_articles.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for i in data:
    key = i['url'].lower()
    i["category"] = urls[key]


article_data = json.dumps(data, indent=4, ensure_ascii=False)
json_data = json.dumps(annotions, indent=4, ensure_ascii=False)

# Now, you can save the JSON data to a file
with open('annotation.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

# Now, you can save the JSON data to a file
with open('annoted_articles.json', 'w', encoding='utf-8') as file:
    file.write(article_data)
