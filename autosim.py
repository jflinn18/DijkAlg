import os
import pdb

dir = os.listdir("input")

for file in dir:
    os.system("python Auto.py < input/" + file + " > log.txt")
    #pdb.set_trace()
    os.system("python parser.py < parser_input.txt")
    #pdb.set_trace()
    
    f = file.split('input')
    os.system("mv parsed.txt data/data" + f[1])

