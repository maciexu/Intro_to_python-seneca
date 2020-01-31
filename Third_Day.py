print(17%3)    #remainder

from random import randint
choice=randint(1, 10)
print(choice)


if choice==7:
    print("You lucky")
else:
    print("Try again")

#practice 1
odd_or_even=randint(1, 100)
print(odd_or_even)

if odd_or_even%2==0:
    print("odd_or_even is even")
else:
    print("odd_or_even is odd")
    
#practice 2
color=input("your color:")
colorl=color.lower()
if colorl=="Purple".lower():
    print("Excellent choice!")
elif colorl=="Red".lower():
    print("Energetic!")
elif colorl=="Yellow".lower():
    print("Medicore")
elif colorl=="Pure Darkness".lower():
    print("I like the way u think")
else:
    print("what?")
    
# is->operator  
# anything outcome with T/F conditions is qualified for if conditions.
# bool("") and bool(None) can be tested
    
x=1
if x is 1:
    print(f'{x} is one.')
    
#empty str->False
x=""
print(bool(x))
if x:
    print("it is true")
else:
    print("it is false")
    
y=None
print(bool(y))
if y:
    print("it is true")
else:
    print("it is false")
    
z=0
print(bool(z))
if z:
    print("it is true")
else:
    print("it is false")

# outside of 0&1, python cannot automatically casting to boolean

x=input("plz enter a number:")
#note: input-> casting to str
if 0: #it is not even testing x
    print("U entered 0")
elif 1:
    print("U entered 1")
else:
    print("U did not enter a thing")


#and, or not. Short-circuit
#or check the first, T->stop; or else check the second
xxx=1
a=10 if xxx else 20
print(a)

#list zero-indexing
print(["f", "t"][bool("fucku")])
print(["f","t"][bool("")])
    
# is vs ==
#is->exactly same, saved in the same memory address.
#== checks the values of variables

if True:
    pass #






    
    
    