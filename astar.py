from graph_creationF import *
from heapq import *
from random import *
import pdb
from time import *


class Astar(object):
	
	def __init__(self):
		self.initNode = None
		self.goalNode = None
		self.time = ''
		self.cost = 0
		
	
	# param - a Node object
	def get_path(self, last_node):
		s = [last_node.getName()]
		while not last_node.prev is None:
			last_node = last_node.prev
			s.append(last_node.getName())
			
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
		seed()
		return randint(0, 5)

	def as_alg(self):
		closedset = set()

		while True:
			self.initNode = self.input_initNode()
			self.goalNode = self.input_goalNode()
			if self.goalNode in g.nodeList.keys() and self.initNode in g.nodeList.keys():
				break


		
		#initNode = 'a'

		g.getNode(self.initNode).dist = 0

		heap = []
		
		start = time()
		
		heappush(heap, g.getNode(self.initNode))
		
		# for i in g.nodeList:
		  # heappush(heap, g.getNode(i))
		  
		  
		  #pseudocode
		  
		g_score = 0    # Cost from start along best known path.
		# Estimated total cost from start to goal through y.
		f_score = g_score + heuristic_cost_estimate()
		
		  

		while len(heap) > 0:
			heapify(heap)
			currNode = heappop(heap)
#			print currNode.getName()
			if currNode == g.getNode(self.goalNode):
				path = self.get_path(g.getNode(self.goalNode))
				self.cost = currNode.dist
				break
			closedset.add(currNode)
			
			for n in currNode.neighbors:
				if n in closedset:
					continue
				tentative_g_score = currNode.dist + currNode.getCost(n)

				
				if n not in heap or (tentative_g_score < n.dist and n.dist != float("inf")):
					if n not in heap:
						heappush(heap, n)	
						
					n.prev = currNode

					n.dist = tentative_g_score			
					n.hop_count = currNode.hop_count + 1				
					#pseudocode
					#f_score[neighbor] = g_score[neighbor] + heuristic_cost_estimate(neighbor, self.goal)
		
		end = time()
		self.get_time(start, end)
		
		print "\nHops: " + str(len(path)-1)
		print "Cost: " + str(self.cost)
		print "Path: " + str(path)
		print "Time: " + self.time
		# for i in g.nodeList:
			# print str("Shortest Distance (" + self.initNode + "," + g.getNode(i).getName() + ")"+ " --- " + str(g.getNode(i).dist))
		
		# print '\n{0:12} {1:7} {3:7} {2:10}'.format('Start/End:', 'Cost:', 'Path:', 'Hops:')
			
		# for i in g.nodeList:
			# p= self.get_path(g.getNode(i))
			# print '{0:12} {1:7} {3:7} {2:10}'.format('('+self.initNode+','+g.getNode(i).getName()+')', str(g.getNode(i).dist), str(p), str(len(p)-1))
			
			
		# for i in g.nodeList:
			# print "Shortest Path (" + self.initNode + "," + g.getNode(i).getName() + ")"+ " --- " + str(self.get_path(g.getNode(i)))