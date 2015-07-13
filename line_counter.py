import os

directory = raw_input('Enter directory: ')

files = os.listdir(directory)

for f in files:
    i = 0
    for line in f:
        i += 1
    
    if i < 6: 
        print f
