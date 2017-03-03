#!/bin/python3

import random
import sys
import os

#this tutorial is dictionaries

# Dictionaries contain a value with a unique key for each value
# They are simailar to lists but you can't add them together

#Dictionary of super villans
SuperVillans = {'Fiddler' : 'Isaac Bowin',
		'Captain Cold' : 'Leonard Snart',
		'Weather Wizard' : 'Mark Mardon',
		'Mirror Master' : 'Sam Scudder',
		'Pied Piper': 'Thomas Peterson'}


#to get the value of key
print(SuperVillans['Captain Cold'])

#To delete a item from the list use the del
del SuperVillans['Fiddler']

print(SuperVillans)

# to replace a value  of key
SuperVillans['Pied Piper'] = 'Hartley Rathaway'
print(SuperVillans)

#to find the length of the Dictionary use len
print(len(SuperVillans))

#to get the value of a key 
print(SuperVillans.get("Pied Piper"))
print(SuperVillans.get("Weather Wizard"))

#this displays keys of list
print(SuperVillans.keys())

#to get the values of a dictionary
print(SuperVillans.values())


