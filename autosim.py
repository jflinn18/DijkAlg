import os
import pdb

dir = os.listdir("input/auto_input/")

for file in dir:
    os.system("python Auto.py < input/auto_input/" + file + " > log.txt")
    #pdb.set_trace()
    os.system("python parser.py -f log.txt < parser_input.txt")
    #pdb.set_trace()

    os.system("mv parsed.txt data/rawdata/" + file)

