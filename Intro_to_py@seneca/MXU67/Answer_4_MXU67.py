
"""
Question 4) I have shown you how to make a dictionary suggestion in the Day 07 notes. 
Now I want you to use that knowledge in answering the following question:
We want to implement an autocomplete feature that provides suggestions as a user types a phrase in the search field. 
The autocomplete is like the Google search suggests a feature. 
When you start searching for a keyword in the Google search, it suggests a few items to you to make life easier for you. 
The list we have in mind currently has a product catalog of around 3 million objects and only want to autocomplete the product name. 
Use the products.json in the following link: https://github.com/BestBuyAPIs/open-data- set
"""

import json
data = []
json_file = open('products.json', encoding = 'utf8')
json_str = json_file.read()
json_data = json.loads(json_str)
dlst = []
for i in range(len(json_data)):
    name = json_data[i]["name"]
    if name is not None:
       fir_sec = name.split(' - ', maxsplit=1)
       if len(fir_sec) == 1:
           first = fir_sec[0]
           second = ""
           dic = {first: second}
       elif len(fir_sec) > 1:
           first = fir_sec[0]
           second = fir_sec[1]
           dic = {first: second}
       dlst.append(dic)       
#print(dlst)
    
from collections import defaultdict
d = defaultdict(list)

for myd in dlst:
    for k, v in myd.items():
        d[k].append(v)
#print(d)
    
user = input("plz enter a product name:").capitalize()

from difflib import get_close_matches

if user in d.keys():
    meaning = d[user]
    for x in meaning:
        print(x)
elif user not in d.keys():
    closet_word = get_close_matches(user, d.keys())[0]  
    user2 = input(f"Do you mean {closet_word}? Y/N:  ")
    while user2 not in ["N", "Y"]:
        user2 = input("plz enter Y or N only: ")
    if user2 == "N":
        print("Sorry, there's no such product. Plz check the product name and re-run the program.")
    elif user2 == "Y":
        meaning2 = d[closet_word]
        for x in meaning2:
            print(x)
        
            
        
