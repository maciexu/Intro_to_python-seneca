# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 11:30:36 2020

@author: mengx
"""

print(7/8)
print(7//8)

print(int(True))
print(int(False))

#backslash
print('Hello \n or hi?')
print ("This is a backslash: \\")
print ("There is a tab \t between us")
print ("He said \" YES \" while he was crying")
print("/\\/\\/\\")

#formating
name='Jim'
age=55
print(f'HBD {name} {age+1}!')

#string is immutable
x="Go pithon"
# del x[0]  TypeError: 'str' object doesn't support item deletion
del x
# to change a string: 1: use +; or 2. use replace methind
course="pithon"
course=course.replace("i", "y")
print(course)

#reverse
s="I love u"
print(s[::-1])

#build-in functions->methods
print(len("pythonn"))
print(list(enumerate("python")))
x="pythON"
print(x.capitalize())
print(x.title())
print(x.swapcase())
print(x.lower())
print(x.upper())
print(x.find("n"))

#in
print('th' in x)
print("macie jessi JK".find("macie"))
print("macie jessi JK".index("macie"))
print("macie jessi JK".rfind("JK"))

#print("macie jessi JK".find("jessi"))
#print("macie jessi JK".index("jessi"))


#str.count(substr, from, to)
print("I hate you, I love you.".count("you"))
print("I hate you, I love you.".count("you", 5, 12))

print('abc123'.isalnum())
print('abc$123'.isalnum())
print(''.isalnum())

print('ABCabc'.isalpha())
print('abc123'.isalpha())

print('123'.isdigit())
print('123abc'.isdigit())

print('foo'.center(10))
print('foo'.center(10,'-'))


print('foo'.ljust(10))
print('foo'.ljust(10, '-'))

print('      foo bar bazz '.lstrip())

print('      foo bar bazz            '.strip())

print('42'.zfill(5))

print("abcd"[2:])

print('new' 'line')

#practice Day2-2 page 11 question
letter="ABCD \nEFGH \nIJKL \nLMNO \nPQRS \nTUVW \nXYZ"
print(letter)
import textwrap  #warp and fill
letter2=textwrap.fill(letter)
print(letter2.strip())   #strip only removes the leading&trailing whitespaces.
letter3=letter2.replace(" ", "")
print(letter3)

letter4=textwrap.wrap(letter2, width=5)
print(letter4)


for x in textwrap.wrap(letter3, width=4):
    print(x)


import this  #The Zen of Python

from random import randint
#generate a LIST of 10 random numbers, first of all, you have to enerate an empty list
my_list=[]
for i in range(0,10):
  x=randint(1,100)
  my_list.append(x)
print(my_list)
  




























