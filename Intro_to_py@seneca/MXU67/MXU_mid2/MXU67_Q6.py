#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 22:29:30 2020

@author: mengxixu

Challenge 3: use the information you have gained so far to create a program that asks the user for a topic 
and search the https://icanhazdadjoke.com and if it finds more than one jokes, 
then it randomly chooses one of those and shows it to the user.

"""

user = input("Plz pick up a topic: ")

import requests
from random import choice

url = "https://icanhazdadjoke.com/search"

response = requests.get(
        url,
        headers = {"Accept": "application/json"},
        params = {"term": user}
)

data = response.json()['results']
#print(data)
#print(len(data))
#print(type(data))
#print(bool(data))


if data:        #if bool(data) == True
    if len(data) == 1:
        print(f"I've got 1 joke about {user}. Here it is:")
        detail = data[0]['joke']
        print(detail)
    elif len(data) > 1:
       total = len(data) 
       print(f"I've got {total} jokes about {user}, Here's one:")
       random_one = choice(data)
       detail = random_one['joke']
       print(detail)
else:
    print(f"Sorry, I don't have any jokes about {user}.")
       









