import yaml
import tweepy

# load the yaml file
document = open('secrets/twitter-keys.yml', 'r')
# and finally parse the file
parsed = yaml.load(document)

#keys yei!!
consumer_key = parsed["twitter-keys"]["api-key"]
consumer_secret = parsed["twitter-keys"]["api-secret-key"]
access_token = parsed["twitter-keys"]["access-key"]
access_token_secret = parsed["twitter-keys"]["access-secret-key"]