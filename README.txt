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


input_creator.py:
   Args:
	-u: has the user input what is to be written to the file
	-c: has the computer use the default settings and write them to a file
	default: -c

   This creates a .txt file that will be able to be used in the DijkAlg/Auto.py
   program. There are varibles that need to be changed in order to change the 
   input of the algorithm program

      resp: number of times you want DijkAlg/Auto.py to run
      wgraph: the graph that you want the algorithm to run on
      walg: the algorithm that you want to run (Node obj is only set up for A*)
      init_node: the range in the random.randint() must be the number of nodes
                 in your graph. Or a list of the names
      goal_node: the same as above


autoinput.py:
   This creates k number of input files to run through the algorithm. k is given
   by the user. 


pathstats.py: takes the a file with just the paths that have been taken. It
   	      compiles a list of data from that file and outputs in the
	      console.
	      To keep track of these outputs, write the outputed data to a
	      file manaully from the console.
