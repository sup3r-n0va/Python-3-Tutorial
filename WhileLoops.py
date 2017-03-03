#!/bin/python3

import os
import random
import sys

#This section is on while loops

#To initialise a random number generator

#This will generate a random number between 0 - 100
random_num = random.randrange(0, 100)

#this loop will loop through all the numbers until 42 is displayed
#while(random_num != 42) :
#	print(random_num)
#	random_num = random.randrange(0, 100)

#print out all the even numbers
i = 0

while(i <= 100) :
	if(i % 2 == 0) :
		print(i)
	elif( i == 88) :
		break
	else :
		i += 1	#which is the same as i = i + 1
		continue
	
	i += 1

