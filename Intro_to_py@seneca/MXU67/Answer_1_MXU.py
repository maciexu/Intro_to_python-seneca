"""
Question 1) Write a code that finds the elements of a sorted list that its index is equal to the item in that
index. For example if the list is lst= [-2,0,2,3,6,7,9] then code has to return 2 and 3 since lst[2]=2 and
lst[3]=3
"""

example_lst = [-2,0,3,2,6,9,7]
print(f"example_list is {example_lst}.")
lst1 = sorted(example_lst)
print("The number that its index is equal to the item is:")
for i in range(len(lst1)):
    if i == lst1[i]:
        print(i)



user = input("please enter a number (Attention: number only!). If you finish you entering, plz enter OK :")
lst = []
while user != "OK":      
      lst.append(int(user))
      user = input("please enter a number. If you finish you entering, plz enter OK :")     
print(f"This is your list: {lst}.")          

lst1 = sorted(lst)

print("The number that its index is equal to the item is:")
for i in range(len(lst1)):
    if i == lst1[i]:
        print(i)