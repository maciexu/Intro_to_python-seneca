"""
Question 1) Write a code that finds the elements of a sorted list that its index is equal to the item in that
index. For example if the list is lst= [-2,0,2,3,6,7,9] then code has to return 2 and 3 since lst[2]=2 and
lst[3]=3
"""

lst = [-2,0,3,2,6,9,7]
lst1 = sorted(lst)
print(lst)
print(lst1)

for i in range(len(lst1)):
    if i == lst1[i]:
        print(i)