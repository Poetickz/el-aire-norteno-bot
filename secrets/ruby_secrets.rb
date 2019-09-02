require 'yaml'
require 'twitter'

begin
  twitter_keys = YAML.load(File.read("secrets/twitter-keys.yml"))
rescue => exception
    
end


config = {
    consumer_key:        ENV["API-KEY"] ||= twitter_keys["twitter-keys"]["api-key"],
    consumer_secret:     ENV["API-SECRET-KEY"] ||= twitter_keys["twitter-keys"]["api-secret-key"],
    access_token:        ENV["ACCESS-KEY"] ||= twitter_keys["twitter-keys"]["access-key"],
    access_token_secret: ENV["ACCESS-SECRET-KEY"] ||= twitter_keys["twitter-keys"]["access-secret-key"]
}

@restClient = Twitter::REST::Client.new(config)

