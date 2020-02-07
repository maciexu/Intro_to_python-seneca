# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:50:01 2020

@author: mengx
"""

"""
Mini Project: Upgrade the RPS game with the following items:
1- It plays until one of the players (computer or human) wins 3 times. 
   That means the winning score is 3
2- It prints the total scores that computer and player has gained every time that 
   the loop iterates
3- Use the sample messages that I have shown in the following print screens. 
   To make your game playable.
4- if player types "quit" or "q" it exits the game.
5- If the human wins it prints "CONGRATS, YOU WON!", if computer wins it prints: 
    "OH NO :-( THE COMPUTER WON..." and if they tie, it prints “NO WINNER, IT'S A TIE"

"""
import random
player = ""
pc = ""
x = 0
y = 0
while player != 'quit' and player != 'q' and x < 3 and y < 3:
    print("...rock... \n...paper... \n...scissor...")      
    player = input("Enter rock, paper, scissor:")
    pc = random.choice(["rock", "paper", "scissor"])      
    if player == pc:
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("it is a tie. \n" + "-"*30)
        x += 1
        y += 1
        print(f'player score: {x}')
        print(f'pc score: {y}')
    elif player == "rock" and pc == "scissor":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
        y = y
        print(f'player score: {x}')
        print(f'pc score: {y}')
    elif player == "paper" and pc == "rock":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
        y = y
        print(f'player score: {x}')
        print(f'pc score: {y}')
    elif player == "scissor" and pc == "paper":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
        y = y
        print(f'player score: {x}')
        print(f'pc score: {y}')
    elif player == 'quit' or player == 'q':
        print("Exit. \n" + "-"*30)
    elif player not in ["rock", "paper", "scissor"]:
        print("Please re-enter")
    else:
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("PC wins. \n" + "-"*30)
        y +=1
        x = x
        print(f'player score: {x}')
        print(f'pc score: {y}')
      

if x ==3 and y==3:
   print("No winner, it is a tie.")    
elif x ==3 and y <3:
   print("CONGRATS, U won!")
elif x<3 and y ==3:
   print("Oh NO :( The PC won...")