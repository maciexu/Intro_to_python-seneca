#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 00:05:59 2020

@author: mengxixu

Challenge 5: familiarize yourself with the “re” module 
(https://docs.python.org/3/library/re.html). 
It is an abbreviation for the Regular Expression. 
They are used to find a string with a specific pattern. 
For example, the phone numbers in Toronto have 10 digits and 
they have this format xxx-yyy-wwww
Use the re module to check if the user has entered a valid phone number 
that follows the above- mentioned pattern.


"""

import re

"""
"^": This expression matches the start of a string
"w+": This expression matches the alphanumeric character in the string
"s": This expression is used for creating a space in the string
"""

def format_match(cell):
    user = input("Plz enter your phone number: ")
    match = re.match("[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]", user)
    is_match = bool(match)
    if is_match:
        print(f"{user} is a valid input. ")
    else: 
        print("Invalid format.")

cell = ""
format_match(cell)
