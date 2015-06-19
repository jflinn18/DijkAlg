from graph_creationF import *
from heapq2 import *
from random import *
import pdb
from time import *


class Astar(object):
	
	def __init__(self):
		self.initNode = None
		self.goalNode = None
		self.time = ''
		self.cost = 0
		seed()
		
	
	# param - a Node object
	def get_path(self, last_node):
		s = [last_node.getName()]
		while not last_node.prev is None:
			last_node = last_node.prev
			s.append(last_node.getName())
		
		s.reverse()
		return s

		
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

		
	def heuristic_cost_estimate(self):
		#return 0
		return randint(0, 20)

	def as_alg(self):
		closedset = set()

		while True:
			self.initNode = self.input_initNode()
			self.goalNode = self.input_goalNode()
			if self.goalNode in g.nodeList.keys() and self.initNode in g.nodeList.keys():
				break


		
		#initNode = 'a'

		g.getNode(self.initNode).dist = 0
		g.getNode(self.initNode).f_score = 0

		heap = []
		
		start = time()
		
		heappush(heap, g.getNode(self.initNode))


		while len(heap) > 0:
#			pdb.set_trace()
			heapify(heap)
			currNode = heappop(heap)
			print currNode.getName()
			if currNode == g.getNode(self.goalNode):
				path = self.get_path(g.getNode(self.goalNode))
				# This won't work if the graph is unweighted.
				self.cost = currNode.dist
				break
			closedset.add(currNode)
				
			for n in currNode.neighbors:
				if n in closedset:
					continue

				tentative_g_score = currNode.dist + currNode.getCost(n)
#				pdb.set_trace()
	

				if n not in heap or (tentative_g_score < n.dist and n.dist != float("inf")):
					if n not in heap:
						heappush(heap, n)	
						
					n.prev = currNode

					n.dist = tentative_g_score		
#					pdb.set_trace()

#					n.hop_count = currNode.hop_count + 1
					
					n.f_score = n.dist + self.heuristic_cost_estimate()
					
# Note: Is the printed cost the cost of the last Node? Am I updating the cost correctly for			
		
		end = time()
		self.get_time(start, end)
		
		print "\nHops: " + str(len(path)-1)
		print "Cost: " + str(self.cost)
		print "Path: " + str(path)
		print "Time: " + self.time
		
