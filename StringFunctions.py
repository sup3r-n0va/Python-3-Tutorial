'''String Functions
'''

#!/bin/python3

#to print characters from a string

LongString = "I'll catch you if you fall - The floor"

#the following prints the characters 0 to 4 in the string above
print(LongString[0:4])
#To print the last five characters int he string
print(LongString[-5:])
#To print everything except the last five characters
print(LongString[0:-5])

#you can add concatencate strings together
print(LongString[:4] + " be there")

#Format specifiers are the following
print("%c is my %s letter and my number %d number is %.5f" %('B', "Hello", 12, 2.42422))

#If you want to capitalize the first character in string

print(LongString.capitalize())

#To a the position of a string or character use the find function
print(LongString.find("floor"))

#to check if all values are characters use
print(LongString.isalpha())

#to check if all the values are numbers use
print(LongString.isalnum())

#to get the length of a string
print(len(LongString))

#if you want to replace a specfic word with another word
print(LongString.replace("floor", "door"))

#If you want to strip whitespace
print(LongString.strip())

#to split a string into a list

QuoteList = LongString.split(" ")
print(QuoteList)

