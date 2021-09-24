import json
import random

#NLTK packages
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk import ngrams
from collections import Counter
import seaborn as sns
import matplotlib.pyplot as plt


'''
JSON data format

nlp_data = {"review_id":"",
            "user_id":"",
            "business_id":"",
            "stars":,
            "useful":,
            "funny":,
            "cool":,
            "text":"",
            "date":""
}

'''

with open("reviewSelected100.json", 'r') as read_file:
    data = [json.loads(line) for line in read_file]

#---------------- Check Business Data ----------------------
'''
Total number of reviews = 15300
Total number of business types = 153
Each business has 100 reviews
'''
biz_type = []
all_biz = []
for i in range(len(data)):
    b = data[i]['business_id']
    biz_type.append(b)

biz_dict = {i:biz_type.count(i) for i in biz_type}
#-----------------------------------------------------------

#1. Randomly select a business b1 from the dataset
b1 = random.choice(list(biz_dict.keys())) #everytime the code runs a new business_id is chosen

#2. Extract all reviews for b1 and create a small dataset B1
B1 = {"small_dataset": []}
count = 0
for i in range(len(data)):
    if data[i]['business_id'] == b1:
        count +=1 #must be 100 on every run
        B1['small_dataset'].append(data[i])
