'''These are modules which some of the funcitons in python
program need'''

import random
import sys
import os

#to escape a quotes in string do the following
quote = "\"Always remember you are unique"

multi_line_quote = '''just like everyone else'''

#to print out the following variables with containing strings
# you use a format specifier in this case we use the 
# string format specifier %s
print("%s %s %s" % ('I like the quote', quote, multi_line_quote))

#to get rid of the new lines use the end=
print("I don't like ", end="")
print("newlines")

#if you want to print for example 5 new kines
print('\n' * 5)



