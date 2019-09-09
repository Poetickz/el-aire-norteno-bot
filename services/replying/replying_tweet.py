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




def switchvalue(datos):
    if datos == 0 or datos >= 301:
        sr = 'error'
    if datos >= 1 or datos <= 50:
        sr = 'poco'
    if datos >= 51 or datos <= 100:
        sr = 'medio'
    if datos >= 101 or datos <= 150:
        sr = 'mucho'
    if datos >= 151 or datos <= 200:
        sr = 'mal'
    if datos >= 201 or datos <= 300:
        sr = 'pesimo'
    return sr



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
        if not_full_text[x].startswith('#') and not_full_text[x]!="#comoestaelairede":     
            ciudad = not_full_text[x]
            if not (ciudad in cities):
                return "-"
            ciudad = cities[ciudad] 
    return ciudad

def busco_cuidad(full_text):
    ciudad = listas(full_text)
    if (ciudad != "-"):
        URL ="https://aqicn.org/city/mexico/nuevo-leon/" + ciudad
        r = requests.get(URL) 
        soup = BeautifulSoup(r.text, 'html.parser')
        datos = soup.find('div', id='aqiwgtvalue').text.strip()
        print(datos)
    else:
        datos=0
    return datos

#file guarda el id del ultimo tweet contestado
FILE_NAME = './services/replying/last_seen_id.txt'

#lee el id
def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = (f_read.read().strip())
    f_read.close()
    return last_seen_id

#reescribe el id por el más nuevo
def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

#contesta los tweets encontrados
def reply_to_tweets():
    print('Revisando nuevos tweets', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#comoestaelairede' in mention.full_text.lower():
            print('encontre #comoestaelairede', flush=True)
            datos = busco_cuidad(mention.full_text.lower())
            if datos != "-":
                resp = switchvalue(int(datos))
            else:
                resp = 'no'
            print (datos)
            switcher = {
                'no' : "Lo siento compa, no hay informacion disponible, intenta mas tarde!",
                'error' : "Lo siento, no te entendi, vuelve a preguntar por favor compa",
                'poco' : "La calidad del aire es de "+str(datos)+ " AQI \n¡Ajua Pariente!🤠.",
                'medio' : "La calidad del aire es de "+str(datos)+ " AQI \n¡Ajua Pariente!🤠.",
                'mucho' : "La calidad del aire es de "+str(datos)+ " \n¡Ajua Pariente!🤠.",
                'mal' : "La calidad del aire es de "+str(datos)+ " AQI \n¡Ajua Pariente!🤠.",
                'pesimo' : "La calidad del aire es de "+str(datos)+ " AQI \n¡Ajua Pariente!🤠.",
            }
            
            api.update_status('@' + mention.user.screen_name+"  "+switcher[resp], mention.id)
            

while True:
    reply_to_tweets()
    time.sleep(5)