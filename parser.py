import re
import sys

try:
    if sys.argv[1] == '-f':
        if sys.argv[2][-4:] == '.txt':
            infile = sys.argv[2]
except IndexError:
    while True:
        infile = raw_input("What file would you like to parse? ")
        if infile[-4:] == '.txt':
            break

#hops_regex = re.compile(r"Hops.*")
#path_regex = re.compile(r"Path.*")
print "\nYou are allowed to search for three regular expressions"
regex1 = raw_input("Enter regex1: ")
regex2 = raw_input("Enter regex2: ")
regex3 = raw_input("Enter regex3: ")

fin = open(infile, 'r')
fout = open("parsed.txt", 'wb')

for line in fin:
    #m = re.search(hops_regex, line)
    #if m is not None: 
    #    fout.write(m.group() + '\n')
    #n = re.search(path_regex, line)
    #if n is not None:
    #    fout.write(n.group() + '\n')
    if not regex1 == '&&&':
        m = re.search(regex1, line)
        if m is not None:
            fout.write(m.group() + '\n')
    if not regex2 == '&&&':
        n = re.search(regex2, line)
        if n is not None:
            fout.write(n.group() + '\n')
    if not regex3 == '&&&':
        w = re.search(regex3, line)
        if w is not None:
            fout.write(w.group() + '\n')
    
    
fin.close()
fout.close()

