#!/bin/python3

import sys
import random
import os


#This section is on conditonals

age = 21

if age >= 21 :
	print("You are old enough to drive a tractor")
elif age >= 16 :
	print("You are old enough to drive")
else :	

	print("You are not old enough to drive")


#logical operators

if ((age >= 1) and (age <= 18)):
	print("You get a birthday")
elif ((age == 21) or (age >= 65)) :
	print("You get a birthday")
elif not(age == 30) :
	print("You don't get a birthday")
else :
	print("You get a birthday")

