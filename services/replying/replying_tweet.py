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
    return switcher[datos]

def is_similar(first, second, ratio):
    return difflib.SequenceMatcher(None, first, second).ratio() > ratio

def listas(full_text):
    ciudad = "-"
    posibles = ["garcia", "mnty", "monterrey", "monty", "monterey", "san nico", "sannico", "san nicolas", "san nicolás", "sannicolas", "sannicolás", "sn", "s n", "s. n.", "s.n.", "santa catarina", "s c", "s. c.", "sc", "santa cata", "s catarina", "san pedro", "sanpedro", "sp", "s.p.", "s p", "s. p.", "guadalupe", "gpe", "la pastora", "apodaca", "escobedo"]
    not_full_text = full_text.split()

    for x in range(len(posibles)):
        for y in range(len(not_full_text)):
            if not_full_text[y] == "s" or not_full_text[y] == "san" or not_full_text[y] == "santa": 
                not_full_text[y] = not_full_text[y]+" "+not_full_text[y+1]
            if posibles[x] == not_full_text[y] and ciudad == "-":
                ciudad = posibles[x]
            
    return ciudad

def busco_cuidad(full_text):
    ciudad = listas(full_text)
    
    if (ciudad != "-"):
        first = [ciudad]
        second = ["garcia", "metrorrey", "san-nicolas", "s.-catarina", "s.-pedro", "pastora", "apodaca", "escobedo"]
        result = [s for f in first for s in second if is_similar(f,s, 0.7)]
        lugar = result[0]
        URL ="https://aqicn.org/city/mexico/nuevo-leon/" + lugar
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
    print('retrieving and replying to tweets...', flush=True)
   
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
   
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#comoestaelairede' in mention.full_text.lower():
            print('found #comoestaelairede', flush=True)
            print('responding back...', flush=True)
            ciudad = "0"
            datos = busco_cuidad(mention.full_text.lower())
            
            switcher = {
                'error' : "Lo siento, no te entendi, vuelve a preguntar por favor compa",
                'poco' : "La calidad del aire en" +ciudad+ "es de "+datos+ " AQI El aire está hermoso pariente, disfruta tu día compa.",
                'medio' : "La calidad del aire en" +ciudad+ "es de "+datos+ " AQI El aire está regular pero no es dañino, una carnita más y nos lleva la @$%&%.",
                'mucho' : "La calidad del aire en" +ciudad+ "es de "+datos+ " AQI El aire está malo, evita realizar cualquier esfuerzo fuerte compa.",
                'mal' : "La calidad del aire en" +ciudad+ "es de "+datos+ " AQI El aire está malisimo, igual que el reggeton.",
                'pesimo' : "La calidad del aire en" +ciudad+ "es de "+datos+ " AQI El aire está horrible, tener la vida de Demmi Lovato es mejor.",
            }

            resp = switchvalue(datos)
            
            api.update_status('@' + mention.user.screen_name+"  "+resp, mention.id)
            

while True:
    reply_to_tweets()
    time.sleep(5)