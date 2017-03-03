#!/bin.python3
'''These are modules which are some  of the 
functions in python program need'''

import random
import sys
import os

'''This section will cover the lists.
A list is going to allow you to create a list of values,
Which allow to manipulate the values in the list,
each value is going to have a index , the first one being 0 
'''

# To initalise a list you need the square brackets [ ]

GroceryList = ['Juice', 'Tomatoes', 'Potatoes', 'Bananas']

# to display first item in the list 
print("First item is = ", GroceryList[0])

#to change the value of the element in a list
GroceryList[0] = "AppleJuice"
print("First item now is = ", GroceryList[0])

#to display the first element to the third but not including the first
print(GroceryList[1:3])

#You can also store list in lists inside of a list
#you can also store the list inside of of string variable
OtherEvents = ["Go to school", "do some work", "come back home"]

ToDoList = [OtherEvents, GroceryList]
print(ToDoList)

#to print the second item for the second list
print((ToDoList[1][1]))

#to print all the items in the second list which is the grocery list
print((ToDoList[1][0:]))

#You cn also append items you just use .append
GroceryList.append("Grapes")
print((ToDoList[1][0:]))

#If you want to insert a items use the .insert
GroceryList.insert(1, "Pickle")

#To remove a item add the .remove
OtherEvents.remove("Go to school")

# to sort items use the .sort
GroceryList.sort()

#to reverse this sort
GroceryList.reverse()

#if you want to delete a spefic item in a list 
del OtherEvents[1]

#Now display both lists
print(ToDoList)

#we can also add list together

ToDoList2 = OtherEvents + GroceryList

#we can get the length of list
print(len(ToDoList2))

#we can also find the max of a list, which ever comes last alphabetically
print(max(ToDoList2))
#we can also find the min of a list, which ever comes first alphabetically
print(min(ToDoList2))
