#!/usr/bin/env python3

#from muitiprocessing import Pool
import sys
import json
import os.path

def exit_file():
    print("Not right arguments")
    print("Usage: " + sys.argv[0] + " <String>")

# checking the the number of arguments is valid right
if len(sys.argv) != 2:
    exit_file()
    sys.exit(1)

#Defines variables
string = str(sys.argv[1])
d = {}
json_file = "./json.csv"

#Checks whether the value exists in the dictionary
def check_if_exist(key):
    if key in d:
        d[key] += 1
    else:
        d[key] = 1

#Json writes to a file
def set_json_to_file(d, json):
    csv = open(json_file, "a")
    dictionenery = json.dumps(d)
    csv.write(dictionenery+"\n")
    csv.close()
    
if __name__ == '__main__':
    for s in string:
        check_if_exist(s)
    if not os.path.isfile(json_file):
        csv = open(json_file, "x")
    set_json_to_file(d, json)
