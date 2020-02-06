# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 19:15:51 2020

@author: mengx
"""
from random import randint

player1=input("Player 1, make your move: ")
player1=player1.lower()

x = randint(0, 2)


if x==0:
   player2='paper'
elif x==1:
   player2='rock'
elif x==2:
   player2='scissor'




if player1 == player2:
	 print("It's a tie!")
elif player1 == "rock" and player2 == "scissors":
	 print("player1 wins!")
elif player1 =="paper" and player2 =="rock":
    print("player1 wins!")
elif player1 =="scissors" and player2 =="paper":
    print("player1 wins!")
else:
    print("player2 wins!")




