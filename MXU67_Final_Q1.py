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
print("===INSTRUCTION=== \n \n")
print("First Stage Input:")
print("User will define the number of cache. And the original cashe.")
print("First Stage Output: \nTo show the user the origal cache with timestamp.\n")
print("Second Stage Input:")
print("User will update their cache if Y is entered.")
print("Second Stage Output: \nThe deleted LRU cache and the updated cache with timestamp.")
 


from datetime import datetime
from operator import itemgetter

size = int(input("Plz determine how many website you wanna save: "))

webs = []
def fav():
    web = input(f"Plz enter your favorate {size} website: ").upper()
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
    

def new_fav(web):
    web = input("What is the latest website you visited?: ").upper()
    now = datetime.now()
    now = now.strftime("%d/%m/%Y %H:%M:%S")
    global mycache
    global webs
    if web in webs:
        print("your favorate webs site are the same.")
    else:
        mycache.append(dict(name = web, updated = now))
        mycache = sorted(mycache,key = itemgetter("updated"),reverse=True)
        lru_web = mycache.pop()["name"]
        webs = [dic["name"]for dic in mycache]
        print(f"The least recently used website is: {lru_web}, and it's been deleted.")
        print(f"These are your {size} favorate wbesites: ")
        for item in mycache:
            web = item["name"]
            added = item["updated"]
            print(f"{web} was added at {added}.")
        return mycache
  
user = input("Do you wanna continue updating? Y or enter any other key to stop: ").upper()
    
while user == "Y":
    new_fav(web)
    user = input("Do you wanna continue updating? Y or enter any other key to stop: ").upper()

