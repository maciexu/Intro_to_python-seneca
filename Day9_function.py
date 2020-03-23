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
num = ""
def what_day(num):
    day = {1:"Mon", 2:"Tue", 3:"Wed", 4:"Thur", 5:"Fri", 6:"Sat", 7:"Sun"}
    num = input("Enter a number between 1 and 7: ")
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


def repeat2(a_str): 
  a_str = input("Plz enter a word: ").lower()
  a_str_lst = list(a_str)
  #USE collections.Counter() TO MAP CHARACTER FREQUENCIES OF A STRING
  from collections import Counter
  frequencies = Counter(a_str_lst)
  repeated = {}
  for key, value in frequencies.items(): #iterate through frequencies dictionary
    if value >= 1:
        repeated[key] = value
  return repeated
print(repeat2(a_str))


string = ""
def multiple_letter_count(string):
    string = input("Plz enter a string: ").lower()
    return {letter: string.count(letter) for letter in string}
print(multiple_letter_count(string))

# parameters, *args, defalut paremeters, **kwargs
#unpack tuple/list use *
#unpack dictionary use **
def sum_of_nums(*args):
  print(args)
  total = 0
  for num in args:
    total += num
  print(total)
nums = (2,3,4,5,6,7)
sum_of_nums(*nums)

"""Q46: let’s say we have the following list. 
Please write a function that it counts the number sevens (7s) 
in the list (use unpacking)"""
Nums= [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34, 45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56, 67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]
def seven(*args):
  total = 0
  for num in Nums:
    if str(7) in str(num):
      total += 1
  print(total)
seven(*Nums) 

def dis_name(first, last):
  print(f'{first} {last}')
my_name = {"first": "Macie", "last": "Xu"}
dis_name(**my_name)

"""Q49: If we have a dictionary like this: data = dict(a=1,b=2,c=3). 
Write a function that adds the three values in the dictionary """
data = dict(a=1,b=2,c=3)
def sum_value(**kwargs):
  total = sum(kwargs)
  print(total)
sum_value(**data)
# not working

def add_numbers(a,b,c):
    print(a + b + c)  
data = dict(a=1,b=2,c=3)
add_numbers(**data)


# recusion

def fib(n):
    if n <=2:
        return 1
    else:
        return fib(n-1)+ fib(n-2)
    
print (fib(6))

"""Q56: Through recursion, check if a word is a palindrome (remember that palindromes are read backward as
they read normally, e.g., Ada, racecar.)"""


def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False

a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")

