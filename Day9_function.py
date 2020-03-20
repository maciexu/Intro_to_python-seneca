def say_hi():
  print("Hi")
say_hi()


def sing(x):
  print(f'HBD to {x}.')
for i in ['U', 'U', 'Dear U', 'U']:
  sing(i)


def sqr(x):
  return x**2
print(sqr(7))


def say_Hello():
  return 'Hello!'
print(say_Hello())

#One important note about the return() is that it exits the function. Anything after return will not be executed.
def even():
  result=[]
  for x in range(1, 50):
    if x%2==0:
      result.append(x)
  return result
print(even())

#The random function of the random module returns a value between 0 and 1.

from random import random
r=random()
print(r)

#We want to simulate the flipping coin by writing a function that it returns “head” or “Tail” every time it runs.
def coin():
  r=random()
  if r>0.5:
    return "Head"
  else:
    return "Tail"
print(coin())


#create a function that it receives a string and make all the letters of the string uppercase and return the string back
word=input("Plz enter something:")
def upper(word):
  word2=word.upper()
  return word2
print(upper(word))    

"""
global local nonlocal
NOTE: you learned about the global and the local variables but there is another scoping that is called nonlocal. You need to declare your variable in a nested function as nonlocal when you want to change the value of a variable in the child function when that is defined in the parent function. It is used in the nested functions.

Put it in other words:
if i want to change the value of a varibale, I need to declare that variable as nonlocal in the child function.

Note: If you define a variable in local level while it is also defined in the global level, the local level overwrites the global level value.
"""
total = 0
def countt():
  global total
  total += 1
  return total
print(countt())
print(countt())
print(countt())
print(countt())
print(countt())


def outer():
  total = 0
  def inner():
    nonlocal total
    total += 1
    return total
  return inner()
print(outer())
print(outer())


"""Q24: write a function that gets two numbers as its parameters and returns the product of those two numbers
"""
def product(x,y):
  z = x * y
  return z
print(product(3,7))

"""Q25: Q: write a function that it gets a number between 1 to 7 and it returns the day of the week (Sunday for 1, Monday for 2 ...)
"""
day = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thur", 5:"Fri", 6:"Sat", 7:"Sun"}
num = input("Enter a number between 1 and 7: ")
def what_day(num):
  return day.get(int(num),"")
print(what_day(num))

"""Q26:Q: write a function that it gets one parameter that is a list and it returns the last item of the list.
"""
def last_item():
  lst = input("Plz enter a series of number/letter/symbol with no space: ")
  lst = list(lst)
  last = lst[-1]
  return last
print(last_item())


""" If it is series of numbers and want to get the last number

lst2 = [int(i) for i in lst]

Or
 
lst2 = [] 
for i in lst:
  j = int(i)
  lst2.append(j)
 
"""

""" Q27: write a function that gets two numeric parameters and compares them and returns “The first one is bigger than the second one” or “Second one is bigger than the first one"
"""
x = float(input("Plz enter a number: "))
y = float(input("Plz enter another number: "))
def bigger(x, y):
  if x > y:
    return f"{x} is bigger than {y}."
  elif x < y:
    return f"{y} is bigger than {x}."
  elif x == y:
    return "equal."
print(bigger(x, y))

""" Q28: Take advantage of the count() method and write a function that gets two strings: the first one is one or more words. The second parameter is a letter. The function returns how many times the letter is used in the word(s). The function has to be insensitive to the user input (it does not matter the input is upper case or lower case) """
x = input("Plz enter some words: ").lower()
x = x.replace(" ","")
xlst = list(x)
y = input("Plz enter a letter: ").lower()
def count(x, y):
  i = 0
  for item in xlst:
    if y == item:
      i += 1
  return i   
print(count(x, y))

"""Q29: Write a function that it takes one string as its parameter and it returns a dictionary that its keys are
the letters of the string and the values are the number of times that letter is used in the string."""

# One method is:

from collections import defaultdict
a_str = ""
def repeat(a_str):
  a_str = input("Plz enter a string: ").lower()
  count = defaultdict(int)
  for i in a_str:
    count[i] += 1
  return count
print(repeat(a_str)) 
print(repeat(a_str).items()) 


string = ""
def repeat2(string): 
  string = input("Plz enter a word: ").lower
  #USE collections.Counter() TO MAP CHARACTER FREQUENCIES OF A STRING
  import collections
  frequencies = collections.Counter(string)
  repeated = {}
  for key, value in frequencies.items():
  #iterate through frequencies dictionary
    if value >= 1:
        repeated[key] = value
  return repeated
print(repeat2(string))
      



  
whvbjchleakwfijewkcjwelkfwjlskcnlkwejdoqwjx



