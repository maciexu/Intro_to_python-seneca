# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:13:15 2020

@author: mengx
"""

for x in "Human":
    print(x*10)
    
    
for i in range(8,1,-1):
    print(i)

# Q: Add all the odd numbers from 1-20 and show the results for each step.   
x = 0
for i in range(1,20,2):
    x = x+i
    print(x)

# Q: Add all the odd numbers from 1-20 and show the final result 
x = 0    
for i in range(1,20,2):
    x = x+i
print(x)


# Q: get a number n from the user and print the following messages:
num=int(input("Enter a positive interger:"))
for i in range(1, num+1):
    print(f'This is message number {i}.')

# Q: write a code that generates the following messages:
# For numbers between 1-20, if the number is 13, it prints unlucky, 
# if it is an even number, it prints
# this is an even number and otherwise it prints this is an odd number.
n=int(input("enter a positive integer 1-20:"))
for i in range(1, 21):
    if i==13:
        print("Unlucky")
    elif i%2==1:
        print("Odd")
    elif i%2==0:
        print("Even")

"""
When you do not know how many times you have to run a block of code, you should use the while
loop. It may run once, hundreds of times, fifty times or not even once. It loops over
as long as a specific condition is True. it'd look like:

varibale=value

while Boolean is True:
    #do something
    #counter (false, otherwise it is an infinite loop)
 
"""
for i in range(1,11):
    print("*"*i)

x=1
while x<11:
    print("*"*x)
    x+=1   
# +=   and =+


#Q: write a program that it prints everything you type until you type 
#“stop copying me” and after that it prints: FINE YOU WIN, BRO”

x=input("Say something:")
while x!= "stop copying me":
      user=x
      print(user)   
      x=input("Say something:")


#break
while True:   # if there's no break, any input would be string->True
    command = input("Type 'exit' to exit:")
    if (command == 'exit'):        #counter
        break

# Q: how many times the code block inside the for loop runs?
for x in range(1,101):
    print(x)
    if x==3:
        break

i=1
while i<5:
    #i+i     infinite loop, it does not change the value of i.
    #i=+1    infinite loop, assign +1 to varibale i.
    i+=1     # same as i = i+1
    print(i)

x=0
while x <=11:
    x +=2
    print(x)


# Q: Use a while loop that generates a random number between 1 to 10 until 
# it gets number 5. Every time it runs, it adds to a counter called “Tries”. 
# After it reaches to 5, it exits the loop and it prints how
# many times we tried (Day4_13.py)
import random
i =0
x=0
while x !=5:
    x =random.randint(1,10)
    i +=1
    print(f'random number in the try# {i} was {x}')

for x in range(5):
    print(x)


""" Mini Project: Guessing game
In the guessing game, the computer picks a random number between 1 to 10. 
It asks you to guess that number. If your guess is higher than that number, 
it prints “It is high”, if your guess is less than the number, it prints “It is low”.
If the guess is equal to the random number, it prints “You won!”. After
that it asks if you want to continue? If you type y it starts the game again and 
if you type n, it prints “Thanks for Playing” and exits the game.
"""
import random
answer = 0
while answer != 'n':
    x = int(input("Pick a number from 1 to 10:"))
    y =random.randint(1, 10)
    while x != y:
        if x > y:
            print("it is high")           
        elif x < y:
            print("it is low")
        x = int(input("Pick a number from 1 to 10:"))
        y =random.randint(1, 10)             
    print("U won!")
    answer = input("Do you want to play again? y/n : ")



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
        y +=1
    elif player == "rock" and pc == "scissor":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
    elif player == "paper" and pc == "rock":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
    elif player == "scissor" and pc == "paper":
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("player wins. \n" + "-"*30)
        x +=1
    elif player == 'quit' or player == 'q':
        print("Exit. \n" + "-"*30)
    else:
        print("Your Choice: "+player)
        print("PC choice: " +pc)
        print("PC wins. \n" + "-"*30)
        y +=1
        

if x ==3 and y==3:
   print("No winner, it is a tie.")    
elif x ==3 and y <3:
   print("CONGRATS, U won!")
elif x<3 and y ==3:
   print("Oh NO :( The PC won...")
    

y = 1/2
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, "has factor", x)
        break
    x -= 1
else:         
#when x gets dwon to 1, the while loop above won't be excuted at all. means y is a prime.
#question: if y < 1? or floating? This code fails for that. 
    print(y, "is a prime.")

list = [1,2,3,4]
for i in enumerate(list):
    print(i)
"""
The enumerate() method takes two parameters:
    enumerate(iterable, start=0)
iterable - a sequence, an iterator, or objects that supports iteration
start (optional) - enumerate() starts counting from this number. 
If start is omitted, 0 is taken as start.    
"""
for _ in enumerate(list):
   print(_)      
    
h = "human"
for i in h:
    print(i*2)

hh = ["h", "u", "m", "a", "n"]
for i in hh:
    print(i*2)

for i in range(len(hh)):
    print(hh[i]*2)




        
        
        
        
        
    
    
    
    
    
    
    
    
    






















n=int(input("enter a number"))
for x in range(2, n):
    if n % x == 0:  # if n is divisible by x, it means it's not a prime number.
       print(f"{n} equals {x} * {n//x}")
       break
    else:  # if n was not divisible by any x, it means it is a prime number.
        print(f"{n} is a prime number.")








 





