#class Node:    ---Python3
class Node(object):

	def __init__(self, key):
		self.name = key;
		self.neighbors = {}
#		self.visited = False
		self.dist = float('inf')
		self.f_score = float('inf')
		self.prev = None
		self.hop_count = 0
		
	def addNeighbor(self, nbr, cost=0):
		self.neighbors[nbr] = cost
		
	def __str__(self):
		return str(self.name) + ' connected to: ' + str([x.name for x in self.neighbors])
		
	def __cmp__(self, other):
		return cmp(self.f_score, other.f_score)
		
	#def __cmp__(self, other):
		#return cmp(self.dist, other.dist)
		
	def getNeighbors(self):
		return self.neighbors.keys()
		
	def getName(self):
		return self.name
		
	def getCost(self, nbr):
		return self.neighbors[nbr]
	
	# neighbor is a node object
	def removeNode(self):
		for n in self.neighbors:
			self.neighbors[n] = float('inf')
			
	def changeNeighborCost(self, neighbor):
		self.neighbors[neighbor] = float('inf')