require 'yaml'
require 'twitter'

twitter_keys = YAML.load(File.read("secrets/twitter-keys.yml"))

config = {
    consumer_key:        twitter_keys["twitter-keys"]["api-key"],
    consumer_secret:     twitter_keys["twitter-keys"]["api-secret-key"],
    access_token:        twitter_keys["twitter-keys"]["access-key"],
    access_token_secret: twitter_keys["twitter-keys"]["access-secret-key"]
}

@restClient = Twitter::REST::Client.new(config)

