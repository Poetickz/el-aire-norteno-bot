import tweepy
import time
import difflib
from bs4 import BeautifulSoup
import requests

first = ["monterrey"]
second = ["garcia", "metrorrey", "san-nicolas", "s.-catarina", "s.-pedro", "pastora", "apodaca", "escobedo"]
result = [s for f in first for s in second if is_similar(f,s, 0.7)]
lugar = result
print(lugar)