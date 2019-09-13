import yaml
import os
import tweepy
import pyrebase


else:
    config = {
    "apiKey": "AIzaSyAXMJf1fYUs6lPxB4fT9uvtu2jPB_zhHPQ",
    "authDomain": "el-aire-norteno-bot.firebaseapp.com",
    "databaseURL": "https://el-aire-norteno-bot.firebaseio.com",
    "projectId": "el-aire-norteno-bot",
    "storageBucket": "el-aire-norteno-bot.appspot.com"}

    firebase = pyrebase.initialize_app(config)
    fb_db = firebase.database()




if os.path.exists('secrets/twitter-keys.yml'):
    document = open('secrets/twitter-keys.yml', 'r')
    # and finally parse the file
    parsed = yaml.load(document)    
    consumer_key = parsed["twitter-keys"]["api-key"]
    consumer_secret = parsed["twitter-keys"]["api-secret-key"]
    access_token = parsed["twitter-keys"]["access-key"]
    access_token_secret = parsed["twitter-keys"]["access-secret-key"]
    config = {
    "apiKey": parsed["firebase-keys"]["apiKey"],
    "authDomain": parsed["firebase-keys"]["authDomain"],
    "databaseURL": parsed["firebase-keys"]["databaseURL"],
    "projectId": "el-aire-norteno-bot",
    "storageBucket": parsed["firebase-keys"]["storageBucket"]}
else:
    consumer_key = os.environ['API-KEY']
    consumer_secret = os.environ['API-SECRET-KEY']
    access_token = os.environ['ACCESS-KEY']
    access_token_secret = os.environ['ACCESS-SECRET-KEY']
    config = {
    "apiKey": os.environ["apiKey"],
    "authDomain": os.environ["authDomain"],
    "databaseURL": os.environ["databaseURL"],
    "projectId": "el-aire-norteno-bot",
    "storageBucket": os.environ["storageBucket"]}
