import yaml
import tweepy

with open('twitter-keys.yml', 'r') as f:
    doc = yaml.load(f)
    
print (doc["twitter-keys"]["api-key"])

# Authenticate to Twitter
#auth = tweepy.OAuthHandler("api-key", "api-secret-key:")
#auth.set_access_token("access-key", "access-secret-key")

# Create API object
#api = tweepy.API(auth)

#try:
#    api.verify_credentials()
#    print("Authentication OK")
#except:
#    print("Error during authentication")