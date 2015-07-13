#import shortest_path
import os
import sys

try:
    if sys.argv[1] == '-f':
        if sys.argv[2][-4:] == '.txt':
            infile = sys.argv[2]
        resp = '1000'
except IndexError:
    resp = raw_input("How many iterations do you want to do? ")
    infile = raw_input("Enter the input file for shortest_path.py: ")


i = 0

while i < int(resp):
    #shortest_path.run()
    os.system('python shortest_path.py < ' + infile)
    i = i + 1
