#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:05:37 2020

@author: mengxixu

The above module can be used to compare the big file sizes. 
For example, if you want to see if your 5 TB file is same as the one that your colleague has, 
you can check their message digest. Try to solve this problem. 
You can get some idea by looking at the code in this link but do not use md5 and 
also do not use the file I/O methods that is suggested in this code 
(https://stackoverflow.com/questions/36873485/compare-md5-hashes-of-two-files-in-python) 

"""
"""
import hashlib

h1 = hashlib.sha256()
file1 = open("/Users/mengxixu/Intro_to_python-seneca/Intro_to_py@seneca/MXU67/MXU_mid2/file1/CRT-en.png","rb")
file1 = file1.read()
a = h1.update(file1)
a = str(h1.hexdigest())


h2 = hashlib.sha256()
file2 = open("/Users/mengxixu/Intro_to_python-seneca/Intro_to_py@seneca/MXU67/MXU_mid2/file2/CRT-en.png","rb")
file2 = file2.read()
b = h2.update(file2)
b = str(h2.hexdigest())

h3 = hashlib.sha256()
file3 = open("/Users/mengxixu/Intro_to_python-seneca/Intro_to_py@seneca/MXU67/MXU_mid2/file3/Day5_22.docx", "rb")
file3 = file3.read()
c = h3.update(file3)
c = str(h3.hexdigest())


print(a == b)
print(b == c)
print(a == c)
"""

#import re
#import os
import hashlib 
file = ""
def hasher(file): 
    path = input("plz enter the file path including the full name: ")
    #hash_id = hashlib.sha256()   #use sha256
    file = open(path, "rb")
    file = file.read()
    hash_id = hashlib.sha256(file).hexdigest()
    #hash_id = str(hash_id.hexdigest())
    return str(hash_id)

a = hasher(file)
b = hasher(file)

if a == b:
    print("True, file1 and file2 are the same.")
else:
    print("False, file1 and file2 are different.")




















