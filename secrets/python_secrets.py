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
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://el-aire-norteno-bot.firebaseio.com'
    })
else:
    firebase_admin.initialize_app( credentials.Certificate({
    "type": os.environ["FIREBASE_TYPE"],
    "project_id": "el-aire-norteno-bot",
    "private_key_id": os.environ["FIREBASE_PRIVATE_KEY_ID"],
    "private_key": os.environ["FIREBASE_PRIVATE_KEY"],
    "client_email": os.environ["FIREBASE_CLIENT_EMAIL"],
    "client_id": os.environ["FIREBASE_CLIENT_ID"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": os.environ["FIREBASE_CLIENT_X509_CERT_URL"]}),
    'databaseURL': 'https://el-aire-norteno-bot.firebaseio.com'})


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
