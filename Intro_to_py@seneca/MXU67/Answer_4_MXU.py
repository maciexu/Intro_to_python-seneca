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
#for item in range(len(json_data)):
#    print(json_data[item]["name"])

from collections import defaultdict
d = defaultdict(list)

for k, v in json_data.items():
    d[k].append(v)

print(d)
    







