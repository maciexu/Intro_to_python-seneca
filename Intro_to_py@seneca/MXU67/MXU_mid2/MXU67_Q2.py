#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:30:04 2020

@author: mengxixu

Challenge 2: there is a sorting algorithm called Quick Sort that used a recursive method. Learn how that works.

"""

def sort(lst):

    less = []
    equal = []
    greater = []

    if len(lst) > 1:               #if lst only has 1 number, len(lst) ==1
        pivot = lst[0]             # choice 
        for x in lst:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return sort(less)+equal+sort(greater)  # recurse the sort function to the smaller sub_lists
    else:  
        return lst

lst = [7,9,8,5,3,12,100,0]
print(sort(lst))

lst = list(input("plz enter some numbers (seperate with comma): ").split(","))
lst = [int(x) for x in lst]
print(sort(lst))


