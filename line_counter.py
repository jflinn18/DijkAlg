import os
import time

directory = raw_input('Enter directory: ')

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
    
    if not n == 6: 
        print f + ' --- ' + str(n)

end = time.time()

print "Time: " + str(end - start)
