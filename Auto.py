#import shortest_path
import os

i = 0

resp = raw_input("How many iterations do you want to do? ")
infile = raw_input("Enter the input file for shortest_path.py: ")


while i < int(resp):
    #shortest_path.run()
    os.system('python shortest_path.py < ' + infile)
    i = i + 1
