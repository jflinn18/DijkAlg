import os
import time

directory = raw_input('Enter directory: ')
lines = raw_input("Expected lines: ")

def line_counter(f):
    fl = open(directory + '/' + f, 'rb')

    i = 0
    for line in fl:
        i += 1

    return i

start = time.time()

files = os.listdir(directory)

for f in files:
    n = line_counter(f)
    
    if not n == int(lines): 
        print f + ' --- ' + str(n)

end = time.time()

print "Time: " + str(end - start)
