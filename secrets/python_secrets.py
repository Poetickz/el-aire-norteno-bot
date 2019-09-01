import yaml
with open('twitter-keys.yml', 'r') as f:
    doc = yaml.load(f)
    
print (doc["twitter-keys"]["api-key"])