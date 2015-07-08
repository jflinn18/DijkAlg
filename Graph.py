from Node import *

#class Graph:      ---Python3
class Graph(object):

	def __init__(self):
		self.nodeList = {}
		self.numNode = 0
                self.alg = ''
		
		
	def addNode(self, key):
		self.numNode = self.numNode + 1
		newNode = Node(key, self.alg)
		self.nodeList[key] = newNode
		return newNode
		
	def getNode(self, n):
		if n in self.nodeList:
			return self.nodeList[n]
		else:
			return None
			
	def __contains__(self):
		return n in self.nodeList
	
	def addEdge(self, f, t, cost=0):
		if f not in self.nodeList:
			nv = self.addNode(f)
		if t not in self.nodeList:
			nv = self.addNode(t)
			
		self.nodeList[f].addNeighbor(self.nodeList[t], cost)
		self.nodeList[t].addNeighbor(self.nodeList[f], cost)
		
	def getNodes(self):
		return self.nodeList.keys()
		
	def __iter__(self):
		return iter(self.nodeList.values())
