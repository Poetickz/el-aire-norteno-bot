import yaml
import os
import tweepy
import firebase_admin
import json
import os
from firebase_admin import credentials
from firebase_admin import db


if os.path.exists('secrets/el-aire-norteno-bot-firebase-adminsdk-mae3g-6348a4cdc1.json'):
    cred = credentials.Certificate("secrets/el-aire-norteno-bot-firebase-adminsdk-mae3g-6348a4cdc1.json")
else:
    cred_json = json.loads(os.environ['FIREBASE-JSON'])
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(cred_json, f, ensure_ascii=False, indent=0)

    cred = credentials.Certificate('data.json')

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://el-aire-norteno-bot.firebaseio.com'
})

fb_db = db.reference()

if os.path.exists('secrets/twitter-keys.yml'):
    document = open('secrets/twitter-keys.yml', 'r')
    # and finally parse the file
    parsed = yaml.load(document)    
    consumer_key = parsed["twitter-keys"]["api-key"]
    consumer_secret = parsed["twitter-keys"]["api-secret-key"]
    access_token = parsed["twitter-keys"]["access-key"]
    access_token_secret = parsed["twitter-keys"]["access-secret-key"]
else:
    consumer_key = os.environ['API-KEY']
    consumer_secret = os.environ['API-SECRET-KEY']
    access_token = os.environ['ACCESS-KEY']
    access_token_secret = os.environ['ACCESS-SECRET-KEY']
