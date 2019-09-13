#!/usr/bin/env python
# Este archivo usa el encoding: utf-8
import tweepy
import time
import difflib
from bs4 import BeautifulSoup
import requests

import os, sys
sys.path.insert(0, "./secrets/")
from python_secrets import *

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)

def aqi_adjetive(aqi):
    if aqi in range(0,50):
        return "excelente"
    elif aqi in range(51,100):
        return "regular"
    elif aqi in range(101,150):
        return "mala"
    elif aqi  in range(151, 200):
        return "pésima"
    elif aqi in range(201, 300):
        return "horrible"
    else:
        return "Error"



def listas(full_text):
    ciudad = "-" 
    cities = {
        "#monterrey": "metrorrey",
        "#cumbres": "metrorrey",
        "#guadalupe": "pastora",
        "#sanpedro": "s.-pedro",
        "#garcia": "garcia",
        "#sannicolas": "san-nicolas",
        "#santacatarina": "s.-catarina",
        "#escobedo": "escobedo",
        "#apodaca": "apodaca"
    }   
    not_full_text = full_text.split()
    for x in range(len(not_full_text)): 
        if not_full_text[x].startswith('#') and not_full_text[x]!="#comoesta":     
            ciudad = not_full_text[x]
            if not (ciudad in cities):
                return "-"
            ciudad = cities[ciudad] 
            
    return ciudad

def busco_cuidad(full_text):
    ciudad = listas(full_text)
    print(ciudad+"ciudad")
    if (ciudad != "-"):
        URL ="https://aqicn.org/city/mexico/nuevo-leon/" + ciudad
        r = requests.get(URL) 
        soup = BeautifulSoup(r.text, 'html.parser')
        datos = soup.find('div', id='aqiwgtvalue').text.strip()
        print(datos)
    else:
        datos=-1
    return datos

#lee el id
def retrieve_last_seen_id():
    return fb_db.get()["last_id"]

#reescribe el id por el más nuevo
def store_last_seen_id(last_seen_id):
    fb_db.update({"last_id": str(last_seen_id)})

#contesta los tweets encontrados
def reply_to_tweets():
    cities = {
        "#monterrey": "metrorrey",
        "#cumbres": "metrorrey",
        "#guadalupe": "pastora",
        "#sanpedro": "s.-pedro",
        "#garcia": "garcia",
        "#sannicolas": "san-nicolas",
        "#santacatarina": "s.-catarina",
        "#escobedo": "escobedo",
        "#apodaca": "apodaca"} 
    last_seen_id = retrieve_last_seen_id()
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')            
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id)
        if '#comoesta' in mention.full_text.lower():
            datos = busco_cuidad(mention.full_text.lower())
            ciudad = "-" 
            not_full_text = mention.full_text.split()
            for x in range(len(not_full_text)): 
                if not_full_text[x].startswith('#') and not_full_text[x]!="#comoesta":     
                    ciudad = not_full_text[x]
                    if not (ciudad in cities):
                        return "-"
                    ciudad2 = ciudad
            if datos == "-":
                a = "á"
                resp = "Lo siento compa, no hay informacion disponible actualmente, intenta m"+a+"s tarde!"

            elif int(datos) != -1 and int(datos)<301:
                resp = "La calidad del aire esta " + aqi_adjetive(int(datos)) + " en " +ciudad2+" con un AQI de "+str(datos)+ ".\n¡Ajua Pariente!🤠."

            else:
                resp = "Lo siento, no te entendi, recuerda que debes usar #comoesta #ciudad.\n Las ciudades que estan: #monterrey, #cumbres, #guadalupe, #sanpedro, #garcia, #sannicolas, #apodaca, #escobedo, #santacatarina"

            print(resp)
   
            api.update_status('@' + mention.user.screen_name+"  "+resp, mention.id)

reply_to_tweets()