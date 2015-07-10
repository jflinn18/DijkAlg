import os
import pdb

while True:
    input = raw_input("Enter an input file: ")
    dir = os.listdir('input')
    if input in dir or input == 'all':
        break

if input == all:
    for n in dir:
        os.system("python input_creator.py -u < ic_input.txt")
        os.system("python Auto.py < input/" + input + " > log.txt")
        os.system("cp log.txt data/rawdata_0/" + input)
        os.system("python parser.py -f log.txt < parser_input1.txt")
        os.system("cp parsed.txt data/parsed_1/" + input)
        os.system("mv parsed.txt parsed1.txt")
        os.system("python parser.py -f parsed1.txt < parser_input2.txt")
        os.system("cp parsed.txt data/paths_2/" + input)
        os.system("python pathstats.py -f parsed.txt > data/stats_3/" + input)
else:
    os.system("python input_creator.py -u < ic_input.txt")
    os.system("python Auto.py < input/" + input + " > log.txt")
    os.system("cp log.txt data/rawdata_0/" + input)
    os.system("python parser.py -f log.txt < parser_input1.txt")
    os.system("cp parsed.txt data/parsed_1/" + input)
    os.system("mv parsed.txt parsed1.txt")
    os.system("python parser.py -f parsed1.txt < parser_input2.txt")
    os.system("cp parsed.txt data/paths_2/" + input)
    os.system("python pathstats.py -f parsed.txt > data/stats_3/" + input)
