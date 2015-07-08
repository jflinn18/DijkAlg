shortest_path.py:
   This is the program that will run different search algorithms on the given 
   the graph. To run this program, run Auto.py without a console command for 
   input from a file.
   
   #Note: the Node.py object is only set up to run A* Algorithm. 



Auto.py:
   This program will run shortest_path.py 'n' number of times. To utilize this
   the best, give it a file of input and output the data to a file
   
   #Example: "python Auto.py < input/input28and19.txt > log.txt"


autosim.py:
   This program will run Auto.py with all of the different input files in the 
   input directory. It will then store the parsed output by the input file 
   names in the parsed directory. 


parser.py:
   This program parses through huge text files looking for one of three things. 
   The program asks for a file name to parse through. Then it askes the user for
   three regular expressions to look for in the file. It outputs these to a file

