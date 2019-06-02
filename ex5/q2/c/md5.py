#!/usr/bin/env python3

#from muitiprocessing import Pool
import sys
import hashlib
import os.path
from multiprocessing import Pool

# prints if there is too meny arguments
def exit_file():
    print("Not right arguments")
    print("Usage: " + sys.argv[0] + " <path>")

# checking the the number of arguments is valid right
if len(sys.argv) != 2:
    exit_file()
    sys.exit(1)

path = sys.argv[1]
print(path)

if (not os.path.isdir(path)):
    exit_file()
    sys.exit(1)

#Assing assistim
if (not os.path.isfile("./md5.csv")):
    csv = open("./md5.csv", "x")
num = 1
file_list = []

#open and change a file to md5
def file_as_bytes(file):
    with file:
        return file.read()

def change_to_md5(arr):
    md5 = hashlib.md5(file_as_bytes(open(arr[0], 'rb'))).hexdigest()
    csv = open("md5.csv", "a")
    md5 = str(arr[2])+",./"+str(arr[1])+str(md5)+"\n"
    csv.write(md5)
    csv.close()


# Recursive func to get all file in dir
for folder, subfolders, files in os.walk(os.getcwd()):
    for file in files:
        filePath = os.path.join(os.path.abspath(folder), file)
        file_list.append([filePath,file,num])
        num += 1

if __name__ == '__main__':
    p = Pool(5)
    p.map(change_to_md5, file_list)

