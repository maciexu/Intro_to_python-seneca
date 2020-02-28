"""
Question 2) Let’s say I give you two strings that contain digits like “234” and “45”. How do you compare
the equivalent numeric values of those two strings without converting them to an integer by the int()
method? For example, 234>45 in the above case.

"""

num1 = input("Plz enter an integer:")
while len(num1) == 0 or int(num1) < 0:
    num1 = input("Plz re-enter a positive integer:")
    
num2 = input("Plz enter another integer:")
while len(num2) == 0 or int(num2) < 0:
    num2 = input("Plz re-enter a positive integer:")
    

if len(num1) > len(num2):
    print(f'{num1} > {num2}')
elif len(num1) < len(num2):
    print(f'{num1} < {num2}')
elif len(num1) == len(num2):
       i = 0
       while i < len(num1) and num1[i] == num2[i]:   # cannot change the order, remember AND/OR checks the first condition.
             i = i + 1
       if i == len(num1):
           print("equal")
       elif i < len(num1):
          if int(num1[i]) > int(num2[i]):
              print(f"{num1} > {num2}")
          elif int(num1[i]) < int(num2[i]):
              print(f"{num1} < {num2}")
    
    
    
    
        
    
            
            











    
