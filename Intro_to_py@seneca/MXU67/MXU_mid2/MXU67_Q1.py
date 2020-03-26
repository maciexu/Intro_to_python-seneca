#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:56:31 2020

@author: mengxixu

Midterm#2

#Challenge 1: write a program that finds all nonsingle letter substrings that are palindromes. 
"""

user_input = ""
def sub_palindrome(user_input):
    user_input = str(input("Plz enter a str: "))
    sub_palind = []
    for i in range(2, len(user_input)+1):
        min = 0
        while (min + i) < len(user_input)+1:
            if user_input[min:(min+i)] == user_input[min:(min+i)][::-1]:
                sub_palind.append(user_input[min:min+i])
            min = min + 1
    return sub_palind
print(sub_palindrome(user_input))
                