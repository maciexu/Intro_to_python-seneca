# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:33:42 2020

@author: mengx
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
    
user = input("plz enter a product name:")
if user not in d.keys():
    print(f"{user} NOT found.")
elif user in d.keys():
    for x in d[user]:
        print(x)





