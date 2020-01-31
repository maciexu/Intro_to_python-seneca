# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:29:33 2020

@author: mengx
"""

print("rock...")
print("paper...")
print("scissors...")
list=["rock", "paper","scissors"]

player1 = input("Player 1, make your move: ")
player1 = player1.lower()
print("***NO CHEATING!******\n\n" * 2)
player2 = input("Player 2, make your move: ")
player2 = player2.lower()

if player1 not in list or player2 not in list:
    print("you have to choice one from 'rock', 'paper', 'scissors' plz.")
else: 
    if player1 == player2:
	     print("It's a tie!")
    elif player1 == "rock" and player2 == "scissors":
		   print("player1 wins!")
    elif player1 == "rock" and player2 == "paper":
        print("player2 wins!")
    elif player1 =="paper" and player2 =="scissors":
        print("player2 wins!")
    elif player1 =="paper" and player2 =="rock":
        print("player1 wins!")
    elif player1 =="scissors" and player2 =="rock":
        print("player2 wins!")
    elif player1 =="scissors" and player2 =="paper":
        print("player1 wins!")