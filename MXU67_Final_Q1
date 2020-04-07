#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 20:55:53 2020

@author: mengxixu


from datetime import datetime

now = datetime.now().time() # time object

print("now =", now)
print("type(now) =", type(now))

import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

"""
from datetime import datetime
from operator import itemgetter

size = int(input("Plz determine how many website you wanna save: "))

def fav():
    web = input("Plz enter your favorate website: ")
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    return dict(name = web,
                updated = now)

mycache = [fav() for i in range(size)]
mycache = sorted(mycache,key = itemgetter("updated"),reverse=True) 
# order by the added time from the most recent to the least recent
#print(type(mycache))
webs = [dic["name"]for dic in mycache]

print(f"These are your {size} favorate wbesites: ")
for item in mycache:
    web = item["name"]
    added = item["updated"]
    print(f"{web} was added at {added}.")
    

def new_fav():
    web = input("What is the latest website you visited?: ")
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    global mycache
    if web in webs:
        print("your favorate webs site are the same.")
    else:
        mycache.append(dict(name = web, updated = now))
        mycache = sorted(mycache,key = itemgetter("updated"),reverse=True)
        lru_web = mycache.pop()["name"]
        print(f"The least recently used website is: {lru_web}, and it's been deleted.")
        print(f"These are your {size} favorate wbesites: ")
        for item in mycache:
            web = item["name"]
            added = item["updated"]
            print(f"{web} was added at {added}.")
        return mycache
  
user = "Y"
while user == "Y":
    new_fav()
    user = input("Do you wanna continue updating your favorate webiste(s)? Y/N: ")



