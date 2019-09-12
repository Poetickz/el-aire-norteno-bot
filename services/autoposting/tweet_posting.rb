require_relative '../../secrets/ruby_secrets'
require 'nokogiri'
require 'open-uri'
require 'descriptive_statistics'

CHAUVENET_COEF = {3 => 1.38, 4 => 1.54, 5 => 1.65, 6 => 1.73, 7 => 1.80, 8 => 1.86}

def get_aqi(city)
  url = "https://aqicn.org/city/mexico/nuevo-leon/#{city}"
  doc = Nokogiri::HTML(open(url))
  doc.css("div#aqiwgtvalue")[0].text.to_i
end

def aqi_warning(aqi)
  case aqi 
  when 0..50
    "El aire está hermoso pariente, disfruta tu día compa."
  when 51..100
    "El aire está regular pero no es dañino, una carnita más y no la contamos."
  when 101..150
    "El aire está malo, evita realizar cualquier esfuerzo fuerte compa."
  when 151..200
    "El aire está malisimo, igual que el reggeton."
  when 201..300
    "El aire está horrible, tener la vida de Demmi Lovato es mejor."
  else
    "Vete a Chernobyl es más saludable "
  end
   
end

def chauvenet_criteria( aqis )

  k = CHAUVENET_COEF[aqis.size] ||= CHAUVENET_COEF[1]
  range_of_aqi = {
    max_value: (aqis.mean + k * aqis.standard_deviation),
    min_value: (aqis.mean - k * aqis.standard_deviation)
  }
end

def checking_data(range_of_aqi, aqis)
  ref_aqis = aqis
  aqis = aqis.reject do |key, value| 
    (value == 0 || (not value.between?(range_of_aqi[:min_value], range_of_aqi[:max_value])))
  end
  return checking_data(chauvenet_criteria( aqis ), aqis) if ref_aqis != aqis
  puts aqis
  return aqis
end

def get_aqi_img(aqi)
    img = 0
    case aqi 
    when 0..50
      img = 1
    when 51..100
        img = 2
    when 101..150
        img = 3
    when 151..200
        img = 4
    when 201..300
        img = 4
    else
         img = 4
    end
    "src/images/#{img}.png"
end


begin
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

  avg_aqi = checking_data(chauvenet_criteria( all_aqi ), all_aqi).mean.round

  tweet = "La calidad del aire en la área metropolitana de Monterrey es de #{avg_aqi} AQI.\n#{aqi_warning(avg_aqi)} \n¡Ajua Pariente!🤠"
  @restClient.update_with_media("#{tweet}", File.new("#{get_aqi_img(avg_aqi)}"))
  puts tweet

rescue => exception
  puts "Error ocurrido: \n #{exception}"
end