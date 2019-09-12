import yaml
import os
import tweepy


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
