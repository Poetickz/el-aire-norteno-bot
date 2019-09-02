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
  
  all_aqi = {
    aq_garcia: get_aqi("garcia"),
    aq_monterrey: get_aqi("metrorrey"),
    aq_san_nicolas: get_aqi("san-nicolas"),
    aq_santa_catarina: get_aqi("s.-catarina"),
    aq_san_pedro: get_aqi("s.-pedro"),
    aq_guadalupe: get_aqi("pastora"),
    aq_apodaca: get_aqi("apodaca"),
    aq_escobedo: get_aqi("escobedo")
  }

  avg_aqi = all_aqi.values.reduce(:+) / all_aqi.size.to_f


  puts avg_aqi.round

  tweet = "Link: \nName:"
  
  # if  not (doc.css(".tags .tag").text.include?("futanari") || doc.css(".tags .tag").text.include?("yaoi"))
  #   @restClient.update("#{tweet}")
  #   puts tweet

  # else
  #   time = 1
  # end


