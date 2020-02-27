# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 00:38:24 2020

@author: mengx
"""

lst = [3,4,1,2,9]
k = []
v = []

for i in range(len(lst)):
    k.append(str(lst[i]))
    v.append(lst[i+1:])
    
    
dd = dict(zip(k,v))

for key, value in dd.items():
    if (10 - int(key)) in value:
        a = int(key)
        b = 10 - a
        
if a is not None:
    print(f"there'r two numbers that can add up to 10. They'r {a} and {b}.")
else:
    print("there'r NO two numbers that can add up to 10.")


    
