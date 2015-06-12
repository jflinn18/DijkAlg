from Graph import *

def get_file():
	try:
		print "Enter graph file:",
		fname = raw_input()

		print "Do you want to create a weighted Graph?",
		wg = raw_input()
		
		file = open(fname, 'r')
		
		if wg[0] == 'y' or wg[0] == 'Y':
			for line in file:
				s = line.split()
				g.addEdge(s[0], s[1], int(s[2]))
				
		elif wg[0] == 'n' or wg[0] == 'N':
			for line in file:
				s = line.split()
				g.addEdge(s[0], s[1], 1)
			
		file.close()
	except:
		print "---File does not exist---"
		get_file()
		


g = Graph()
get_file()

# for v in g:
	# for w in v.getNeighbors():
		# print "( %s , %s )" % (v.getName(), w.getName())
