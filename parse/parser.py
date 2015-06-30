import re


while True:
    infile = raw_input("What file would you like to parse? ")
    if infile[-4:] == '.txt':
        break

hops_regex = re.compile(r"Hops.*")
path_regex = re.compile(r"Path.*")
fin = open(infile, 'r')
fout = open("parsed_text.txt", 'wb')

for line in fin:
    m = re.search(hops_regex, line)
    if m is not None: 
        fout.write(m.group() + '\n')
    n = re.search(path_regex, line)
    if n is not None:
        fout.write(n.group() + '\n')
    
    
fin.close()
fout.close()

