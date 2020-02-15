# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:56:39 2020

@author: mengx
"""

#Practice 13
x=4       
if x>3:
   if x<=5:     #x>3 and x<=5
       y=1     
   elif x!=6:   #x>6, always True for 7,8,9,.....
       y=2
   else:        #will not be excuted at all
       y=3
else:
   y=4          #when x<=3       
print(y)            
# Answer: x>6.