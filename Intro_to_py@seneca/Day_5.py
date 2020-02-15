# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 20:29:24 2020

@author: mengx
"""

lst=[]
seq1="spam"
seq2="scam"
lst.append(seq1)
lst.append(seq2)
print(lst)



lst = ["1", 1, "1", 2]
for i in lst:
    if lst.count(i)>1:
        lst.remove(i)
print(lst)

lst = ["1", 1, "1", 2]
lst2 =[]
for i in lst:
    if i not in lst2:
       lst2.append(i)
print(lst2)


color = []
color.append("red")
color.extend(["green", "blue"])
print(color)

lst = ["John", "Merry", "Lisa"]
lst.remove("Lisa")
lst.remove("John")
lst.append("Dome")
lst2 = list(reversed(lst))
print(lst2)

import bisect
a = [2,5,7,1,0,4,8]
a.sort()
x=9
i = bisect.bisect(a, x)
if i:
    print(a[i-1])

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
new_lst = list(letters[-3::])

# Q: Create a list with the output of the range() function
r = range(10)
print(r)
print(list(r))

# Accessing items in list
friend = ["Kate", "taylor", "Halsey"]
print(friend[-1])
print("Jack" in friend)
print("Kate" in friend)
# Since the result of the “in” operation is True or False, 
# you can use it in the if or the while statements

# Q2: change items
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
people[0] = "Hannah"
people[-2] = "Jeffrey"
people[-1] = people[-1].capitalize()
print(people)

# for/while iterating over all items
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
result = ""
for i in sounds:
    result += i.upper()
print(result)

result2 = []
for i in sounds:
    i = i.upper()
    result2.append(i)
print(result2)

# Q: Let’s say you want to print each item in a list with unknown length. How can you do that through
# the while loop
# ???

for x in ["spam", "egg", "ham"]:
    print(x)

for x in ["spam", "egg", "ham"]:
    print(x, end = " ")

lst1 = [1,2,3,4,5,6]
lst2 = [3,6]
for x in lst2:
    if x in lst2:
        print(x, "found in the lst1.")
    else: 
        print(x, "was not found in the lst1.")

lst = [1,2,3]
lst.append(4)
print(lst)
lst.append([5,6])
print(lst)
lst.extend([9,8,10])
print(lst)

# Q: write a code that it looks into two strings : seq1 = "spam" and seq2 = "scam" and create a list
# that it list the overlapping characters in those two strings. 
seq1 = "spam"
seq2 = "scam"
lst = []
for i in seq1:
    if i in seq2:
        lst.append(i)
print(lst)


# remove the duplicates
a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)


# insert(position_index, item)
a = [1,2,3,4,5]
a.insert(2, "index2")
print(a)
a.clear()
print(a)

# lst.pop(index#) removes the item in a list with specific index. If no index is given, the last
# item is removed:
lst = [1,2,3,4,5]
lst.pop(0)
print(lst)

del lst[-1]
print(lst)

a = [4,7,1,5,8]
del a[:2]
print(a)

# lst.remove(item), removes the first item in the list that matches with the item and if it
# does not find a match, it throws an error
a = [4,1,1,1,7,1,5,8,2,8]
a.remove(1)
print(a)
a.remove(8)
print(a)

# lst.index(item, start_index) returns the index# of an item in the list

# NOTE: please note that the reverse() method works in place on the original list. If you do not want
# to touch the original list, you can make a copy of a list and then reverse the second one.
# . Another way to reverse a list is using the reversed() 
a = [1,2,3,4]
a.reverse()
print(a)

b = reversed(a)
print(list(b))

a = [4,7,0,1,5,8]
a.sort()                 # another way: sorted
print(a)

# “”.join(lst): it converts the list of items to a string and by putting the character
# between the strings
word = ["Python", "is", "fun"]
" ".join(word)
"".join(word)

# Q: Create a list called instructors and add the following strings to the instructors list 
lst = ["John", "Merry", "Lisa"]
lst.pop()
del lst[-1]
lst.append("Done")
lst.reverse()
print(lst)


# min/ max

# bisect.bisect(lst, x): Locates the insertion point for x in lst assuming that the list is sorted.
# If x is already present in lst, the insertion point will be after (to the right of) any existing
# entries.
# Q: Use the bisect module to find the first smaller value in a list than x (set by user).
# For example, in the following list, the first smaller value in the list that is less than 6 or 7 is 5:
import bisect
a=[2,5,1,0,9,4,8]
a.sort()
x=7
i = bisect.bisect(a, x)
if i:
  print (a[i-1])

# List Slicing: some_list[start:end:step]
# If you want to include all the items but with specific steps, then you should add two ::, like: lst[::2]
lst = [1,2,3,4]
print(lst[::2])

x = range(5)
print(x)
print(list(x))
print(x[2::])
print(list(x[2::]))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
letters[-3:]
letters[::2]

# == and is
lst = [1,2,3,4]
lst1 = lst[0:]
lst2 =lst[:]
print(lst == lst1)
print(lst is lst1)

# switch the lcoation & modify parts of the list
num = [1,2]
num[0], num[1] = num[1], num[0]
print(num)

number = [1,2,3,4,5,6]
number[1:3] = ["a", "b", "c"]
print(number)

lst = [1,2,3,4]
lst1 = []
lst1.extend(lst)
print(lst1)

lst2 = list(lst)
print(lst2)

# copy module, copy method, Shallow copy and Deep copy
# use for loop to copy a list

lst = [1,2,3,4]
lst1 = []
for x in lst:
    lst1.append(x)
print(lst1)


# Q: Given a list numbers = [1,2,3,4], what does numbers[::-1] returns?
lst = [1,2,3,4]
lst1 = lst[::-1]
print(lst1)

# list comprehension
num = [10,20,30]
num1 = [x/2 for x in num]
print(num1)

num = [1,2,3,4,5]
doubb =[x*2 for x in num]
print(doubb)

friends = ['john', 'mattew', 'michael']
fr = [x.capitalize() for x in friends]
print(fr)

lst = [x*10 for x in list(range(1,11))]
print(lst)

print([bool(val) for val in [0, [], '']])

numbers = [1, 2, 3, 4, 5]
num_str = [str(x) for x in numbers]
print(num_str)


lst = ["1", "2", "3"]
lst2 = [x+"Hello" for x in lst]
print(lst2)

num = [1,2,3,4,5,6]
even = [x for x in num if x%2 ==0]
odd = [x for x in num if x%2 !=0]
print(even)
print(odd)

# NOTE:  if comes after “for”. If you want to use “else”, the order is a bit different.
num = [1,2,3,4]
print([x*2 if x%2 ==0 else x/2 for x in num])


s= "This is so much fun!"
print("".join([x for x in s if x not in ["a", "e", "i", "o", "u"]]))


#Q: Create a list of your friends’ names. Then through the list comprehension create a new list that it
#has the first letter of your friend’s names.
names = ["Ethan", "Uma", "Jude"]
names1 = [x[0] for x in names]
print(names1)


#Q: Given a list like [1,2,3,4,5,6], create a new list that just even numbers of this list
lst =  [1,2,3,4,5,6]
even = [x for x in lst if x%2 ==0]
print(even)

#Q: You have two below lists. Create a new list that it has the overlapping items in those two lists:
a = [1,2,3,4]
b = [3,4,5,6]
c = [x for x in a if x in b]
print(c)


#Q: Let’s you have a list of your friends. Create a new list that reverse each name in the list.
names = ["Ethan", "Uma", "Jude"]
nam = [x[::-1] for x in names]
print(nam)

#Q: for all numbers from 1, 100 (inclusive), create a list that contains all numbers devisable by 12
lst = list(range(0,101))
lst1 = [x for x in lst if x%12 ==0]
print(lst1)

#Q: Let’s say you have a word like “amazing”. Generate a list that has all the letters except the vowels
a = "amazing"
b = [x for x in a if x not in["a","e","i","u","o"]]
c = "".join(b)
print(c)

#Nested List
a = [[1,2,3],[4,5,6],[7,8,9]]
for i in a:
    for j in i:
        print(j)


#Q: Create a nested list like below by nested loop and comprehension:
print([[num for num in range(1,4)] for val in range(1,4)])


#Q: Use the above example and put “X” in odd locations and “O” in the even locations. Its output
#would be like this:

b = ["X" if i%2 ==1 else "O" for i in range(1,4)]
c = [b for j in range(1,4)]
print(c)

#Q: Through the range() and nested list write a code that generates this output:
print([["*" for i in range(1,4)] for j in range(1,4)])


#Q: Generate a nested list like this: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]
print([[i for i in range(0,3)] for j in range(0,3)])

#Q: How do you generate a matrix like this?
print([[i for i in range(0,10)] for j in range(0,11)])


# Given a list x = [1,2,3], you can call the __iter__() method to get an iterator for the list and
# then use the __next__() method to iterate through:
dir(it)

x = [1,2,3]
it = x.__iter__()
count = 0
while count < len(x):
 item = next(it)
 print(item)
 count = count + 1

#The For loop make that task easier but there is a loophole too: do not re-size a list (add or remove
#items) while you are iterating over it. The iterator keeps an internal count of how many times next()
#has been called and resizing the list will invalidate this count.









