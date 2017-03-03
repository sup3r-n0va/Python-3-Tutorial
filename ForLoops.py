'''For Loops'''
#!/bin/python3

import random
import sys
import os

#this section is on for loops
#loops let us repeat a action a set number of times

#to print from 0 to 9
for x in range(0, 10) :
	print(x, ' ', end=' ')


#to cycle through a list 
# first we create a list

GroceryList = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

#now we loop through the list
for y in GroceryList:
	print(y)
	print('\n')

#to loop through a list numbers
for x in [2,4,6,8,10]:
	print(x)

#to loop through list in a list

NumList = [[1,2,3], [10,20,30],[100,200,300]]

for x in range(0,3) :
	for i in range (0, 3) :
		print(NumList[x][i])

