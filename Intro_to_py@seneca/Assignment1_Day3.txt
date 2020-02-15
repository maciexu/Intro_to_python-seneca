# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 17:18:53 2020

@author: mengx
"""
#Day_3_Code_practice

#Practice 1
if True:
    pass

#Practice 2
print(7==7.0)
x=0.1
print(1==10*x)
print(1==x+x+x+x+x+x+x+x+x+x)    

#Practice 3
#The link is NOT working at all. 

#Practice 4
number=input("Enter a number:")
#digits=list(number)
digits = [int(i) for i in number]
print(min(digits))

#Practice 5
number=input("Enter a number:")
digits = [int(i) for i in number]
"""
for i in digits:
    x=int(i)
    ct=digits.count(x)
    list=f'The dight {x} is repeated {ct} time(s).' 
    print(list)
"""   
import collections
freq=dict(collections.Counter(digits))      #print(freq)
for key, value in freq.items():
    print(f'The digit {key} is repeated {value} times.')
       
#Practice 6
n=int(input("Enver a number:"))
if n%3==0:
    print(f'{n} is a power of 3.')
else:
    print(f'{n} is NOT a power of 3.')
    
##Practice 7
h=int(input('Enter a number:'))
if h%2==0 and h%3==0 and h%5==0:
    print(f'{h} is a Hamming number.')
else:
    print(f'{h} is NOT a Hamming number')

#Practice 8
word1=input("Enter a word:")
word2=input("Enter another word:")
a="".join(sorted(word1))
b="".join(sorted(word2))
if a==b:
    print(f'{word1} and {word2} are anagrams.')
else: 
    print(f'{word1} and {word2} are NOT anagrams')
    
#Practice 9:
items5=input('Enter 5 items, please seperate with comma:')
a,b,c,d,e=items5.split(",")
my_list=[a,b,c,d,e] 

length=[len(i) for i in my_list]

my_dict=dict(zip(my_list, length))

longest=max(my_dict.values())
for k, v in my_dict.items():
    if v==longest:
        print(f'{k} is the (one of) the longest substring.')
         

#Practice 10:
x=input('Enter a number:')
y=sum(map(int, x))
print(y)
if y<=9:
    print(y)
else:
    while y>9:
      z=sum(map(int,str(y)))
      y=z
      print(z)

"""
x=int(input('Enter a number:'))
while x>9:
      y=sum(map(int,str(x)))
      x=y
      #print(y)   print inside the loop will output all values of y, not just the last one.
print(y)    
"""

#Practice 11-1:
number=map(int,input("Enter a number:"))
import collections
frequ=dict(collections.Counter(number)) 
#print(frequ) 
highest=max(frequ.values())
#print(highest)
for k, v in frequ.items():
    if v==highest:
       print(f"The number {k} is repeated more than the others.")

#Practice 11-2    
number=map(int,input("Enter a number:"))
frequ=dict(collections.Counter(number)) 
#kk=max(frequ, key=frequ.get)                 it only give the first hightest... 
kk=[k for k,v in frequ.items() if v==max(frequ.values())]
print(kk)  # check which are the highest values
print(f'{kk} are repeated more than others.')

#Practice 12
x=int(input("Enter a number:"))
if x<=1:
    pass
else:
    while x!=1:
        if x%2==0:
           x=x/2
           y=x
           print(int(y))
        else: 
           x=3*x+1
           y=x
           print(int(y))

#Practice 13
x=10       
if x>3:
   if x<=5:     #x>3 and x<=5
       y=1     
   elif x!=6:   #x>3 and x<>6, always True for 4,5,7,8,9,.....
       y=2
   else:        #will not be excuted at all
       y=3
else:
   y=4          #when x<=3       
print(y)            
# Answer: x>3 and x<>6.         
        
    
    
    

 













