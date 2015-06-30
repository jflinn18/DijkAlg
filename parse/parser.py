import re


while True:
    infile = raw_input("What file would you like to parse? ")
    if infile[-4:] == '.txt':
        break

regex = re.compile(r"Hops.*")
fin = open(infile, 'r')

for line in fin:
    m = re.search(regex, line)
    if m is not None: 
        print m.group()
    
    
fin.close()

