# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:56:19 2020

@author: mengx
"""

""" Mini Project: Guessing game
In the guessing game, the computer picks a random number between 1 to 10. 
It asks you to guess that number. If your guess is higher than that number, 
it prints “It is high”, if your guess is less than the number, it prints “It is low”.
If the guess is equal to the random number, it prints “You won!”. After
that it asks if you want to continue? If you type y it starts the game again and 
if you type n, it prints “Thanks for Playing” and exits the game.
"""
import random
answer = ""
y = ""
x = ""
while answer != 'n':
    y =random.randint(1, 10) 
    X = input("Pick a number from 1 to 10 only:")  
    try:
      x = int(X)
      while x != y:
          if x>=1 and x<=10 and x > y:
              print("it is high")           
          elif x>=1 and x<=10 and x < y:
              print("it is low") 
          else: 
              print("Please Pick an integer from 1 to 10 only!")
          X = input("Pick a number from 1 to 10:")  
      print("PC input: ", y, " U won!")
      answer = input("Do you want to play again? y/n : ")
    except:
      print("Please Pick an integer from 1 to 10 only!")
    X = int(input("Pick a number from 1 to 10 only:"))   
