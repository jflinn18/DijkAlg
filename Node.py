class Node:

	def __init__(self, key):
		self.name = key;
		self.neighbors = {}
		self.visited = False
		
	def addNeighbor(self, nbr, cost=0):
		self.neighbors[nbr] = cost
		
	def __str__(self):
		return str(self.name) + ' connected to: ' + str([x.name for x in self.neighbors])
		
	def getNeighbors(self):
		return self.neighbors.keys()
		
	def getName(self):
		return self.name
		
	def getCost(self, nbr):
		return self.neighborss(nbr)