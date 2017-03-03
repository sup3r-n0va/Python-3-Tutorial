'''Section on Functions'''
#!/bin/python3

import os
import sys
import random

#You define funciton using def
#funciton contains function name and parameters

def AddNumbers(fNum, lNum) :
	SumNum = fNum + lNum
	return SumNum

#to call the funciton you call the function name

print(AddNumbers(1, 5))

print("What is your name?")

#Function  to get user input
name = sys.stdin.readline()

print('Hello', name)
 
