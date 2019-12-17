# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:04:09 2019

@author: ASUS
"""
# Adding needed libraries and reading data
import pandas as pd
import numpy as np

import warnings
warnings.filterwarnings('ignore')



# for text 
import nltk
nltk.download('stopwords')
from textblob import TextBlob

dat = pd.read_csv('tweetsdata.csv')

print(dat.shape)
print("------------------------------------------------")

print(dat.head())

print("------------------------------------------------")

print(dat['tweet_text'][:20].apply(lambda x: TextBlob(x).sentiment))

#dat['sentiment'] = dat['tweet_text'].apply(lambda x: TextBlob(x).sentiment[0])
#print(dat.head())