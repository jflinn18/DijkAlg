import os

i = 0

resp = raw_input("How many times? ")

while i < int(resp):
    os.system('python input_creator.py')
    i = i + 1
    

dir = os.listdir('DijkAlg/input')

count = 0
for file in dir:
    count = count + 1

print "\nThere are " + str(count) + " files in /input" 
