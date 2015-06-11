from graph_creationF import *
from random import *
from time import *
import pdb

class HotPotato(object):
		
	def __init__(self):
		self.initNode = None
		self.goalNode = None
		self.time = ''
		self.cost = 0
		self.hop_count = 0
		seed()

		
	def input_initNode(self):
		print "\nWhich node is the starting node?",
		n = raw_input()
		return n
		
	def input_goalNode(self):
		print "\nWhich node is the goal node?",
		n = raw_input()
		return n
		
	def get_time(self, start, end):
		self.time = str(end - start)
		
	def rand_neighbor(self, node):
#		pdb.set_trace()
		gl = g.nodeList.keys()
		nl = []
		for n in node.neighbors.keys():
			nl.append(n.getName())
		
		while True:
			i = randint(1, g.numNode) - 1
			
			if gl[i] in nl:
				return g.getNode(gl[i])
			
			

	# the nodes only know their neighbors, not the whole network
	def hp_alg(self):
		
		while True:
			self.initNode = self.input_initNode()
			self.goalNode = self.input_goalNode()
			if self.goalNode in g.nodeList.keys() and self.initNode in g.nodeList.keys():
				break
		
		start = time()
		path = []
		g.getNode(self.initNode).dist = 0

		currNode = g.getNode(self.initNode)		
		path.append(currNode.getName())
		while True:
#			pdb.set_trace()
			if currNode.getName() == self.goalNode:
				self.cost = currNode.dist
				break
			n = self.rand_neighbor(currNode)
			path.append(n.getName())
			n.dist = currNode.dist + currNode.getCost(n)
			n.hop_count = n.hop_count + 1
			currNode = n
			
		end = time()
		self.get_time(start, end)
		
		print "\nHops: " + str(len(path)-1)
		print "Cost: " + str(self.cost)
		print "Path: " + str(path)
		print "Time: " + self.time
		