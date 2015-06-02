from Graph import *


g = Graph()

g.addEdge('a', 'b', 2)
g.addEdge('a', 'c', 3)
g.addEdge('b', 'c', 2)
g.addEdge('b', 'd', 1)
g.addEdge('c', 'd', 5)
g.addEdge('d', 'g', 1)
g.addEdge('c', 'e', 5)
g.addEdge('c', 'f', 2)
g.addEdge('e', 'f', 1)
g.addEdge('f', 'g', 3)
g.addEdge('e', 'g', 2)


for v in g:
	for w in v.getNeighbors():
		print("( %s , %s )" % (v.getName(), w.getName()))