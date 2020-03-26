#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:04:29 2020

Please read this link (https://leons.im/posts/a-python-implementation-of-simhash-algorithm/) 
and install simhash and test it with two files that are similar together and prove that 
you can find similar contents

@author: mengxixu
"""

from simhash import Simhash
#print(Simhash('aa').distance(Simhash('aa')))

"""
def get_file_hash(file):
    path = input("plz enter the file path including the full name: ")
    file = open(path, "rb")
    file = file.read()
    return Simhash(file)
file = ""
file1 = get_file_hash(file)  
file2 = get_file_hash(file)    
"""    

"""
file1 = input("plz enter a 'virtual' file name. : ")
file2 = input("plz enter another 'virtual' file name. : ")
print(Simhash(file1).distance(Simhash(file2)))
"""



"""
import re
from simhash import Simhash
def get_features(s):
    width = 3
    s = s.lower()
    s = re.sub(r'[^\w]+', '', s)
    return [s[i:i + width] for i in range(max(len(s) - width + 1, 1))]

print(Simhash(get_features('How are you? I am fine. Thanks.')).value)
print(Simhash(get_features('How are u? I am fine.     Thanks.')).value)
print(Simhash(get_features('How r you?I    am fine. Thanks.')).value)

"""
    

"""
def split_hash(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]   
    #range(1,10,2) ->[1,3,5,7,9]

hashes = {}

for doc_id, doc in documents.items():
    hash = simhash(doc)

    # you can either use the whole hash for higher precision or split into chunks for higher recall
    hash_chunks = split_hash(hash, 4)

    for chunk in hash_chunks:
        if chunk not in hashes:
            hashes[chunk] = []
        hashes[chunk].append(doc_id)

# now you can print the duplicate documents:
for hash, doc_list in hashes:
    if doc_list > 1:
        print("Duplicates documents: ", doc_list)
"""

""" It's not working between files.
def similarity(path):
    path = input("plz enter the file path including the full name: ")
    file = open(path, "rb")
    file = file.read()
    simhasher = Simhash(file)
    sim_value = simhasher.value
    return sim_value

path = ""
a = float(similarity(path))
b = float(similarity(path))

if a > b:
    similar = b / a
else:
    similar = a / b
    
print(similar)
"""   




# seeking two article similarities
def simhash_similarity(text1,text2):
    """
         :param tex1: text 1
         :param text2: text 2
         :return: returns the similarity of two articles
    """
    aa_simhash = Simhash(text1)
    bb_simhash = Simhash(text2)

         # print simhash value binary
    #print(bin(aa_simhash.value))
    #print(bin(bb_simhash.value))

         
    #distince = aa_simhash.distance(bb_simhash)
    

    a = float(aa_simhash.value)
    b = float(bb_simhash.value)

    if a > b:
        similar= b / a
    else:
        similar= a / b

    return similar


text1 = input("Plz enter some text: ")
text2 = input("Plz enter some text: ")
similar=simhash_similarity(text1,text2)
print(similar)






    
    






















