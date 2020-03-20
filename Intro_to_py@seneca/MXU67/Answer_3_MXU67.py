
"""

Question 3) Let’s say we want to check if the sum of two numbers in a list is equal to 10. 
The list can be a very big list. We do not want to iterate through the list more than once. 
Do not use the brute force method.

"""

lst = [3,4,1,2,9,8, 0,10]
print(f"This is a given list. {lst}")

k = []
v = []

for i in range(len(lst)):
    k.append(str(lst[i]))
    v.append(lst[i+1:])
    
    
dd = dict(zip(k,v))

ab = []

for key, value in dd.items():
    if (10 - int(key)) in value:
        two = int(key), 10 - int(key)
        ab.append(two)
        
        
if ab is not None:
    print(f"there'r two numbers that can add up to 10. They'r {ab}.")
else:
    print("there'r NO two numbers that can add up to 10.")


    
