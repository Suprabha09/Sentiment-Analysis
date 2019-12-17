# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 22:56:00 2019

@author: ASUS
"""

import tweepy
from textblob import TextBlob
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from string import punctuation
import string

consumer_key = 'tf21vNlOqbQS1SMXkN0qt8cWA'
consumer_secret = 'P11tgAbCxNHic0VUwjgyrteLnyzOt8TVj7CSXd2FEbjTlSg3D7'
access_token = '1206453702933938177-FefaIdwhtGvuWkJ29P1ZkjRSPwVyjg'
access_token_secret = 'R5QbUKhnbc8JakCdg633IcqfphoQMM0O4QrINstEDIktu'
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search('Donald Trump')



for tweet in public_tweets:
    print(tweet.text)
    sp = string.punctuation
#    tweet = list(map(lambda t: ''.join(["" if c.isdigit() else c for c in t]), tweet))
#    tweet = list(map(lambda t: ''.join(["" if c in sp else c for c in t]), tweet))
#    tweet = list(map(str.lower, tweet))
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    

#public_tweets['Tweet'][:10].apply(lambda x: TextBlob(x).sentiment)