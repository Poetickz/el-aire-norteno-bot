require_relative '../../secrets/ruby_secrets'
require 'nokogiri'
require 'open-uri'

def get_aqi(city)
  puts city
  url = "https://aqicn.org/city/mexico/nuevo-leon/#{city}"
  doc = Nokogiri::HTML(open(url))
  doc.css("div#aqiwgtvalue")[0].text.to_i
end


time = 1800

  
  # if  not (doc.css(".tags .tag").text.include?("futanari") || doc.css(".tags .tag").text.include?("yaoi"))
  #   @restClient.update("#{tweet}")
  #   puts tweet

  # else
  #   time = 1
  # end


