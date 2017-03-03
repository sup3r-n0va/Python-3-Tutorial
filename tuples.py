#!/bin/python3

'''These are some of modules required
for some of the functions in python'''

import random
import sys
import os


#This tutorial will be about tuples

#Tuples are slightly different from lists as after you have created 
#a tuple you can not change it like a list

# You usually use a tuple when you don't want to change the items inside it

#tuples use the ()

PiTuple = (3,4,2,5,3,2,5,)
# to convert a tuple into a list
new_tuple = list(PiTuple)
new_list = tuple(new_tuple)

print(PiTuple)
print(new_tuple)
print(new_list)

#to get length of a tuple use len
print(len(PiTuple))
print(len(new_list))

#to get max of tuple
print(max(PiTuple))
print(max(new_list))

#to get min of tuple us the min function
print(min(PiTuple))
print(min(new_list))

