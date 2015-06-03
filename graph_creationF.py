from Graph import *


g = Graph()
print "Enter graph file:",
fname = raw_input()

file = open(fname, 'r')

for line in file:
	s = line.split()
	g.addEdge(s[0], s[1], int(s[2]))
	
file.close()