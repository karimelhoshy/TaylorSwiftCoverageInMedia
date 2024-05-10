import json
import math
from collections import defaultdict
from argparse import ArgumentParser
def get_top_10_scores(scores_list):
    # Sort the list of dictionaries by the 'score' key in descending order
    sorted_scores = sorted(scores_list, key=lambda x: x['score'], reverse=True)
    
    # Return the top 10 scores if available, or all scores if less than 10
    return sorted_scores[:10]


# Get the top 10 scores

def compute_tfidf(articles):

    cat_word_count = {
        "Music": {},
        "Branding": {},
        "Love Life": {},
        "Personal Life": {},
        "Concert": {},
        "Culture": {},
        "Celebrity Mention": {}
    }

    word_count = {}
    
    for i in articles:
        cat = i['category']
        descripton = i['description'].lower()
        words = descripton.split()
        for j in words:
            if j in word_count:
                if cat not in word_count[j]:
                    word_count[j].append(cat)
            else:
                word_count[j] = [cat]

            if j in cat_word_count[cat]:
                cat_word_count[cat][j]+=1

            else:
                cat_word_count[cat][j] = 1
    tfidf = {
        "Music": [],
        "Branding": [],
        "Love Life": [],
        "Personal Life": [],
        "Concert": [],
        "Culture": [],
        "Celebrity Mention":[]
    }     
    for i in cat_word_count:
        for j in cat_word_count[i]:
            tfscore = cat_word_count[i][j]
            idfscore = math.log(7/len(word_count[j]))
            tfidf[i].append({
                "word": j,
                "score": tfscore*idfscore
                })

    top_scores = {
        "Music": [],
        "Branding": [],
        "Love Life": [],
        "Personal Life": [],
        "Concert": [],
        "Culture": [],
        "Celebrity Mention":[]
    }
    for i in tfidf:
        temp = get_top_10_scores(tfidf[i])
        top_scores[i] = temp

    return top_scores


words = {}
with open('annoted_articles.json', 'r', encoding='utf-8') as file:
    articles = json.load(file)

    
tfidf = {
    "Music": [],
    "Branding": [],
    "Love Life": [],
    "Personal Life": [],
    "Concert": [],
    "Culture": [],
    "Celebrity Mention": []
}

tfidf = compute_tfidf(articles)

with open("tfidf.json", 'w') as json_file:
    json.dump(tfidf, json_file, indent=4)