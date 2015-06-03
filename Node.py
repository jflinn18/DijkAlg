#class Node:    ---Python3
class Node(object):

	def __init__(self, key):
		self.name = key;
		self.neighbors = {}
#		self.visited = False
		self.dist = float('inf')
		self.prev = None
		
	def addNeighbor(self, nbr, cost=0):
		self.neighbors[nbr] = cost
		
	def __str__(self):
		return str(self.name) + ' connected to: ' + str([x.name for x in self.neighbors])
		
	def __cmp__(self, other):
		# if self.dist < other.dist:
			# return self
		# else:
			# return other
		return cmp(self.dist, other.dist)
		
	def getNeighbors(self):
		return self.neighbors.keys()
		
	def getName(self):
		return self.name
		
	def getCost(self, nbr):
		return self.neighbors[nbr]