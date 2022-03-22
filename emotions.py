#libraries used to extract, clean and manipulate the data
from re import I
#from bleach import clean
from helpers import *
import pandas as pd
import numpy as np
import string

#To create the sentiment analysis model, tokenization and lemmatization
import nltk

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import word_tokenize
import nltk.data
# nltk.download('vader_lexicon')
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

access_token = "dTEDSEgYrLVPy9VIlmAYjOSfv39HrizCcf2mVKey9D-CkkA9e_gAk6Ve7xEERLue"
# df0 = search_data('Metallica',3,access_token)
# df = clean_lyrics(df0,'lyric')
# df = df[df['lyric'].notnull()]
#df.to_csv('lyrics.csv',index=False)

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
# words = []
# #iterate trought each lyric and split unique words appending the result into the words list
# df = df.reset_index(drop=True)
# for word in df['lyric'].tolist():
#     words.append(unique(lyrics_to_words(word).split()))
# #create the new column with the information of words lists
# df['words'] = words
# print(df.head())

def getLyricsInfo(listaCanciones):
  df = pd.DataFrame()
  for item in listaCanciones:
    df0 = search_data(item['artist'], item['song'],1,access_token)
    if(not df0.empty):
      print(df0.head())
      df = pd.concat([df,df0])
  df = clean_lyrics(df,'lyric')
  df = df[df['lyric'].notnull()]
  
  negative = []
  neutral = []
  positive = []
  compound = []
  sid = SentimentIntensityAnalyzer()

  df['negative'] = 0
  df['neutral'] = 0
  df['positive'] = 0
  df['compound'] = 0
  df = df.reset_index(drop=True)
  for i in df.index:
      scores = sid.polarity_scores(df['lyric'].iloc[i])
      df['negative'].iloc[i] = scores['neg']
      df['neutral'].iloc[i] = scores['neu']
      df['positive'].iloc[i] = scores['pos']
      df['compound'].iloc[i] = scores['compound']
      # negative.append(scores['neg'])
      # neutral.append(scores['neu'])
      # positive.append(scores['pos'])
      # compound.append(scores['compound'])

  # df['negative'] = negative
  # df['neutral'] = neutral
  # df['positive'] = positive
  # df['compound'] = compound

  return df
