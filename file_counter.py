import os

directory = raw_input("Enter the directory: ")

files = os.listdir(directory)

i = 0
for f in files:
    i += 1


print "Number of files in " + directory + " is: " + str(i)
