require_relative '../../secrets/ruby_secrets'
require 'nokogiri'
require 'open-uri'

def get_aqi(city)
  puts city
  url = "https://aqicn.org/city/mexico/nuevo-leon/#{city}"
  doc = Nokogiri::HTML(open(url))
  doc.css("div#aqiwgtvalue")[0].text.to_i
end

def aqi_warning(aqi)
  case aqi 
  when 0..50
    "El aire está hermoso pariente, disfruta tu día compa."
  when 51..100
    "El aire está regular pero no es dañino compa."
  when 101..150
    "El aire está malo, evita realizar cualquier esfuerzo fuerte compa."
  when 151..200
    "El aire está malisimo, trata de no salir a la calle compa."
  when 201..300
    "El aire está horrible, no salgas a la calle compa."
  else
    "¿En serio llegamos a este nivel? Este nivel es lo peor de lo pero, no salgas a la calle. "
  end
   
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

  avg_aqi = (all_aqi.values.reduce(:+) / all_aqi.size.to_f).round

  tweet = "La calidad del aire en la área metropolitana de Monterrey es de #{avg_aqi} AQI.\n#{aqi_warning(avg_aqi)} \n¡Ajua Pariente!🤠"
  puts tweet
  
  # if  not (doc.css(".tags .tag").text.include?("futanari") || doc.css(".tags .tag").text.include?("yaoi"))
  #   @restClient.update("#{tweet}")
  #   puts tweet

  # else
  #   time = 1
  # end


