#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 19:47:01 2020

@author: mengxixu
"""
"""
lst = [(2,7),(1,2)]
items = []

for i in range(len(lst)):
    for j in lst[i]:
        items.append(j)
        
print(items)
"""
from operator import itemgetter

def Sort_Tuple(tup):  
  
    # reverse = None (Sorts in Ascending order)  
    # key is set to sort using second element of  
    # sublist lambda has been used  
    tup.sort(key = lambda x: x[0])  
    return tup  


def interval():
    num_of_tasks = int(input("Plz enter how many subtasks do you have: "))
    lst = []
    while len(lst) < num_of_tasks:
        start = int(input("Plz enter the starting timestamp:"))
        end = int(input("Plz enter the ending timestamp: "))
        if start >= end:
            print("Staring timestamp should be smaller than the ending timestamp.")
        else:
           pair = (start, end)
           lst.append(pair)
    lst = Sort_Tuple(lst)
    print(f"This is the list of the intervals: {lst}.")
    items = []
    for i in range(len(lst)):
        for j in lst[i]:
            items.append(j)
    a = min(items)
    b = max(items)
    ab = (a, b)
    print(f"The bigger interval is {ab}.")
    return (a,b)
    
interval()
