from graph_creationF import *
from heapq import *
from set import *


class Astar(object):
	
	def __init__(self):
		self.initNode = None
		
	
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


	def As_alg(self, start, goal):
		closedset = set()

		while True:
			self.initNode = self.input_initNode()
			if self.initNode in g.nodeList.keys():
				break

		
		#initNode = 'a'

		g.getNode(self.initNode).dist = 0

		heap = []
		heappush(heap, self.initNode)
		
		# for i in g.nodeList:
		  # heappush(heap, g.getNode(i))
		  
		  
		  #pseudocode
		  
		# g_score[start] := 0    // Cost from start along best known path.
		# // Estimated total cost from start to goal through y.
		# f_score[start] := g_score[start] + heuristic_cost_estimate(start, goal)
		
		  

					
		while len(heap) > 0:
			heapify(heap)
			currNode = heappop(heap)
			if currNode == goal:
				get_path(goal)
			closedset.add(currNode)
			
			for n in currNode.neighbors:
				if n in closedset:
					continue
				tentative_g_score = currNode.dist + currNode.getCost(n)
				if n in heap or (tentative_g_score < currNode.getCost(n)):
					n.prev = currNode
					n.dist = currNode.dist + currNode.getCost(n)
					#pseudocode
					#f_score[neighbor] = g_score[neighbor] + heuristic_cost_estimate(neighbor, goal)
					if n not in heap:
						heappush(heap, n)
					
						
					
		# for i in g.nodeList:
			# print str("Shortest Distance (" + self.initNode + "," + g.getNode(i).getName() + ")"+ " --- " + str(g.getNode(i).dist))
		
		print '\n{0:12} {1:7} {3:7} {2:10}'.format('Start/End:', 'Cost:', 'Path:', 'Hops:')
			
		for i in g.nodeList:
			p= self.get_path(g.getNode(i))
			print '{0:12} {1:7} {3:7} {2:10}'.format('('+self.initNode+','+g.getNode(i).getName()+')', str(g.getNode(i).dist), str(p), str(len(p)-1))
			
			
		# for i in g.nodeList:
			# print "Shortest Path (" + self.initNode + "," + g.getNode(i).getName() + ")"+ " --- " + str(self.get_path(g.getNode(i)))