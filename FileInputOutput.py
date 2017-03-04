'''This section is on File Input and Output
'''
#!/bin/python3

import sys
import os
import random

#if you want to create and/or open a text file 
#to write to file you need the wb

TestFile = open("Test.txt", "wb")

#To read and append to a file
TestFile2 = open("Test2.txt", "ab+")

#to print the file mode that is being used
print(TestFile.mode)
print(TestFile2.mode)

#to display the files name
print(TestFile.name)
print(TestFile2.name)

#if you want to write text to a file you use 
TestFile.write(bytes("Write me to the file\n", "UTF-8"))
TestFile2.write(bytes("Write me to a file as well\n", "UTF-8"))
TestFile2.read()

#if you want to close a file just use the close function
TestFile.close()
TestFile2.close()


#if you want to read a file 
TestFile = open("Test.txt", "r+")
#to read just use the read function
TestFile = TestFile.read()
print(TestFile)

TestFile2 = open("Test2.txt", "r+")
TestFile2 = TestFile2.read()
print(TestFile2)

#if you want to delete a file you use os in os module
os.remove("Test.txt")
os.remove("Test2.txt")

