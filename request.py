import requests
import json
import pandas as pd
import prep1 as py
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import numpy as np
df=pd.read_csv("youtubedata.csv")
# df_title, df_desc = df['title'].values,df['description'].values
# df_title,df_description = df_title[0], df_desc[0]
c0 = py.corpus_build(["Things to know BEFORE you go to ROME | Travel Tips 2020"])
c1 = py.corpus_desc(["""⭐ This video is sponsored by CEPTICS, a number one brand for travel adapters 🔌 on Amazon 👉 https://www.ceptics.com
🔥📚 Our Rome PDF guide ONLY $4.99 👉 https://gum.co/RmeGD 🔥 ⭐⭐⭐ 20% DISCOUNT - use code: HUNGRY20 (limited time offer) ⭐⭐⭐
_____________________

ALSO WATCH:
Travel Adapters: https://youtu.be/IX3Fksa7ukI 
Best apps to BOOK HOTELS & accommodation: https://youtu.be/B7usOIXzAJk
Best apps to book CHEAP FLIGHTS: https://youtu.be/adCcuDUrtOU
Best TRAVEL APPS: https://youtu.be/LJjdKJqWzw0
_____________________

In this video, we’ll cover all you need to know before traveling to Rome, Italy:

#18: ABOUT THE CITY
#17: MAP OF ROME 
#16: WEATHER AND CLIMATE 
#15: BEST TIME TO VISIT
#14: WHERE TO STAY AND PRICE OF THE ACCOMMODATION
#13: LINES & CROWDS
#12: CURRENCY
#11: LANGUAGE & EXPRESSIONS
#10: TIME ZONE
#9: TRANSPORTATION: from and to the airport, arriving by train, arriving by car, getting around the city (public transportation, etc.)
#8: GENERAL INFORMATION: drinking water, public toilets, opening hours, Italian national vacations in August (ferragosto), free attractions
#7: FOR INTERNATIONAL TRAVELERS: travel adapters (Italian power plugs, power outlets), internet providers (SIM cards), Pocket WiFi, Google Fi
#6: SAFETY
#5: BEST APPS TO USE IN ROME
#4: FREE CITY TOURS
#3: ROME CITY PASS
#2: FOOD AND DRINKS
#1: BEST FREE VIEWS OF THE CITY

Plug images credit: ostapenko / 123RF Stock Photo
_____________________

OUR SOCIAL MEDIA:
⭐Instagram: https://www.instagram.com/hungrypassp...  
⭐Facebook: https://www.facebook.com/hungrypasspo...  
⭐Twitter: https://twitter.com/Hungry_Passport   

For collaboration and inquiries: hpassport.travel(at)gmail.com 
👉Visit our WEBSITE: https://www.hungrypassport.xyz/

#rome #travelguide #tips"""])
print(c0,c1)
f=open("corpus.txt","r")
cor=f.read().splitlines()
f.close()
cor=cor[0]
points,y = py.vector(c0,c1,cor,df)
print(points)
url = 'http://192.168.43.84:5000/api/'
j_data = points.tolist()
j_data = json.dumps(j_data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print(r, r.text)