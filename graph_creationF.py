from Graph import *


def get_file():
	try:
		print "Enter graph file:",
		fname = raw_input()

		file = open(fname, 'r')

		for line in file:
			s = line.split()
			g.addEdge(s[0], s[1], int(s[2]))
			
		file.close()
	except:
		print "---File does not exist---"
		get_file()
		


g = Graph()
get_file()
