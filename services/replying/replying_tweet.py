#!/usr/bin/env python
import tweepy
#from our keys module (twitter-keys.py), import the keys dictionary
from twitter-keys import twitter-keys

CONSUMER_KEY = keys['api-key']
CONSUMER_SECRET = keys['api-secret-key']
ACCESS_TOKEN = keys['access-key']
ACCESS_TOKEN_SECRET = keys['access-secret-key']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

twts = api.search(q="Hello Wor!")     

#list of specific strings we want to check for in Tweets
t = ['Hello wor!',
    'Hello Wor!]

for s in twt:
    for i in t:
        if i == s.text:
            sn = s.user.screen_name
            m = "@%s Hello!" % (sn)
            s = api.update_status(m, s.id)