var_data=True
print(var_data)
print(type(var_data))

print(int(True))

#print(int(true))  it won't work.

print(type(1))

print(type(int(12.3)))

print(int(False))

print('+'>'!') #check ASCII
print('A'>'B')
print('BA'>'AB')

print('hello \n world!')

first="my name is :"+" Macie"
second="Mengxi"
print(first)

#print(first|second) 

first_string='foot'
print(first_string*3)

first_string+='ball'  
# += operator: all ball to the previous one and save it.
print(first_string)

#format
x=28
print(f'my age is {x+1}.')

age=20
happy='John, happy birthday for your ' + str(age+1) + ' years old!'
print(happy)

x=10
y=20
print('I was {} 10 years ago, and now I am {}.'.format(x,y))
#old version 3.5

print(f'I was {x} years old, and now I am {y}.')

xx="hello"
print(xx[0])


time=9-5
speed=81.34
distance=time*speed
print(distance)
print(f'travel distance is {time}*{speed}.')

print("python"[2])
print("python"[2:4])  #ending not included


str1='hello world!'
print(str1.find('w'))
print(str1.find('p')) #nothing there returns -1

print(str1.find('l'))
print(str1.rfind('l'))  #from the right

print('python'[-1])

print('python'[0:-1])

"""
-6, -5, -4, -3, -2, -1
p    y   t   h   o   n
0    1   2   3   4   5
"""

print("python"[0:-3])

print("python"[2:])
print("python"[:4])

print("python"[-3:])
print("pythin"[:-3])

#if str is consisting a numeric exp, the eval function will evaluate the expression to an integer or floating-point number as appropriate.

print(float("23"))
print(eval("23"))
print(eval("23.5"))

xxx=5
#compare:
print("23+(xxx*2)")
print(eval("23+(xxx*2)"))

age1=int(input("enter ur age:"))
print(age1+20)

age2=float(input("enter ur age:"))
print(age2+10)

age3=eval(input("enter ur age:"))
print(age3+10)

# function and .method






