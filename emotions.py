#libraries used to extract, clean and manipulate the data
from helpers import *
import pandas as pd
import numpy as np
import string
#To plot the graphs
import matplotlib.pyplot as plt
plt.style.use('seaborn')
#library used to count the frequency of words
from sklearn.feature_extraction.text import CountVectorizer
#To create the sentiment analysis model, tokenization and lemmatization
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import nltk.data
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

access_token = "dTEDSEgYrLVPy9VIlmAYjOSfv39HrizCcf2mVKey9D-CkkA9e_gAk6Ve7xEERLue"
df0 = search_data('Metallica',3,access_token)
df = clean_lyrics(df0,'lyric')
df = df[df['lyric'].notnull()]
df.to_csv('lyrics.csv',index=False)

def unique(list1):
   # intilize a null list
     unique_list = []
   # traverse for all elements
     for x in list1:
         # check if exists in unique_list or not
         if x not in unique_list:
              unique_list.append(x)
     return unique_list

#Stores unique words of each lyrics song into a new column called words
#list used to store the words
words = []
#iterate trought each lyric and split unique words appending the result into the words list
df = df.reset_index(drop=True)
for word in df['lyric'].tolist():
    words.append(unique(lyrics_to_words(word).split()))
#create the new column with the information of words lists
df['words'] = words
print(df.head())

