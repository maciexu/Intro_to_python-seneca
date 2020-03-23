#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:02:20 2020

@author: mengxixu

Challenge 3: create a tic-tac-toe game 
"""

# Create a board
board = [" ", " ", " ", " ", " ", " ", " ", " "," "]
def boardd():
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")


while True:
    user1 = int(input("Player1: Plz enter your move (between 1 and 9): ")) - 1
    if board[user1] == " ":
        board[user1] = "X"
    else: 
        print("Player1: It's been taken, pass.")
    boardd()
    
    is_full = True
    for items in board:
        if items == " ":
            is_full = False
            break
    
    if is_full == True:
        print("It is a draw.")
        break
    
    if (board[0]== "X" and board[1]== "X" and board[2]== "X") or \
       (board[3]== "X" and board[4]== "X" and board[5]== "X") or \
       (board[6]== "X" and board[7]== "X" and board[8]== "X") or \
       (board[0]== "X" and board[3]== "X" and board[6]== "X") or \
       (board[1]== "X" and board[4]== "X" and board[7]== "X") or \
       (board[2]== "X" and board[5]== "X" and board[8]== "X") or \
       (board[0]== "X" and board[4]== "X" and board[8]== "X") or \
       (board[2]== "X" and board[4]== "X" and board[6]== "X"):
           print("Player1->X wins.")
           break
    
     
    user2 = int(input("Player2: Plz enter your move (between 1 and 9): ")) - 1
    if board[user2] == " ":
        board[user2] = "O"
    else: 
        print("Player2: It's been taken, pass.")
    boardd()
    
    for items in board:
        if items == " ":
            is_full = False
            break   
    if is_full == True:
        print("It is a draw.")
        break
    
    
    if  (board[0]== "O" and board[1]== "O" and board[2]== "O") or \
        (board[3]== "O" and board[4]== "O" and board[5]== "O") or \
        (board[6]== "O" and board[7]== "O" and board[8]== "O") or \
        (board[0]== "O" and board[3]== "O" and board[6]== "O") or \
        (board[1]== "O" and board[4]== "O" and board[7]== "O") or \
        (board[2]== "O" and board[5]== "O" and board[8]== "O") or \
        (board[0]== "O" and board[4]== "O" and board[8]== "O") or \
        (board[2]== "O" and board[4]== "O" and board[6]== "O"):
           print("Player2->O wins.")
           break
       
   

    
     
    
            
    
    
    
