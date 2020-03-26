#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:21:47 2020

@author: mengxixu

Challenge 4: Write a program to count a number of files for each extension in the given directory. 
The program should take a directory name as argument and print count 
and extension for each available file extension. 

"""

import os 
import glob
import collections

path = ""


def get_files_counter(path):
    path = input("plz input a directory: ")
    #dirpath = r'path'
    os.chdir(path)
    counter = collections.Counter()
    for file in glob.glob("*.*"):
        name, ext = os.path.splitext(file)
        counter[ext] += 1
    #return counter
    for k, v in counter.items():
        print(k, v)

get_files_counter(path)
        





    
        
    

