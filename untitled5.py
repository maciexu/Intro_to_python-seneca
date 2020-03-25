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
print(Simhash('aa').distance(Simhash('ab')))
print(Simhash('aa').distance(Simhash('aa')))

