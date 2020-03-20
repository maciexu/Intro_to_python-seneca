# Day10_Module

# hashlib simhash

# pip install package_name

# from module import balabala

import math
print(math.sqrt(49))

import keyword

def contain_keyword(*args):
    for x in args:
        if keyword.iskeyword(x):
            return True
    return False

print(contain_keyword("ace", "elif", "if", "nothing"))


def contain_keyword(*args):
    for x in args:
        if keyword.iskeyword(x):
            print(x)

contain_keyword("ace", "elif", "if", "nothing")

# python -m pip install requests

import requests
url = "https://news.ycombinator.com/"
res = requests.get(url)
print(res.headers)
print(res.ok)
print(res)
