#!/usr/bin/env python3

#from muitiprocessing import Pool
import sys
import hashlib
import os.path

# prints if there is too meny arguments
def exit_file():
    print("Not right arguments")
    print("Usage: " + sys.argv[0] + " <word> and <path>")

# checking the the number of arguments is valid right
if len(sys.argv) != 3:
    exit_file()
    sys.exit(1)
if (not os.path.isfile(sys.argv[2])):
    exit_file()
    sys.exit(1)

path = sys.argv[2]
word = sys.argv[1]
print("path",path)

#open and search the word in the array and print
def searching_if_exist(line,num):
    if word.lower() in line.lower():
        print ("Index:", num, "line:" ,line, end="")

# Open the path and assign to array
def assign_to_list(path):
    num=1
    with open(path) as file:
        for line in file:
            searching_if_exist(line,num)
            num=num+1
            
assign_to_list(path)
