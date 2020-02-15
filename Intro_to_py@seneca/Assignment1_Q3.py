# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 21:26:16 2020

@author: mengx
"""

#Assignment1->Practice 3

mark=input("Enter your mark:")

if int(bool(mark))==0 or mark.upper()=="N/A":  #if no mark or mark is N/A: means the student did not attend
    print('Letter Grade:DNA (Registered, did not attend, did not officially withdraw.) \nGrade Point Value: 4.0')
elif int(bool(mark))==1:
    if int(mark)>100 or int(mark)<0:
        print("The mark should be between 0 and 100. Please re-start the program.")
    if int(mark)>=90 and int(mark)<=100:
        print("Letter Grade: A+ \nGrade Point Value: 4.0")
    elif int(mark)>=80 and int(mark)<90:
        print("Letter Grade: A \nGrade Point Value: 4.0")
    elif int(mark)>=75 and int(mark)<80:
        print("Letter Grade: B+ \nGrade Point Value: 3.5")
    elif int(mark)>=70 and int(mark)<75:
        print("Letter Grade: B \nGrade Point Value: 3.0")
    elif int(mark)>=65 and int(mark)<70:
        print("Letter Grade: C+ \nGrade Point Value: 2.5")
    elif int(mark)>=60 and int(mark)<65:
        print("Letter Grade: C \nGrade Point Value: 2.0")
    elif int(mark)>=55 and int(mark)<60:
        print("Letter Grade: D+ \nGrade Point Value: 1.5")
    elif int(mark)>=50 and int(mark)<55:
        print("Letter Grade: D \nGrade Point Value: 1.0")
    elif int(mark)>=0 and int(mark)<50-5:
        print("Letter Grade: F \nGrade Point Value: 0.0")













