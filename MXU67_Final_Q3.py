#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 21:14:22 2020

@author: mengxixu

Q3: Find Meeting point
"""


xlst = []
ylst = []

def mpoint():
    X = int(input("plz enter the x-demension, must be a positive integer:"))
    Y = int(input("plz enter the y-demension, must be a positive integer:"))
    num = int(input("how many will join the meeting?:"))
    xlst = []
    ylst = []
    for i in range(num):
        xx = int(input("Plz enter the your x-position:"))
        yy = int(input("Plz enter the your y-position:"))
        while xx > X or yy > Y:
            print(f"Your position should be within the {X}*{Y} grid.")
            xx = int(input("Plz enter the your x-position:"))
            yy = int(input("Plz enter the your y-position:"))
        xlst.append(xx)
        ylst.append(yy)
    xmean = round(sum(xlst)/len(xlst), 0)
    ymean = round(sum(xlst)/len(xlst), 0) 
    print("The meeting point should be: ")     
    print(xmean, ymean) 
    return xmean, ymean
    
mpoint()
