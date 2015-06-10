from graph_creationF import *
from heapq import *


class DijkstraAlgorithmH(object):
	
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


	def dijk_alg(self):	

		while True:
			self.initNode = self.input_initNode()
			if self.initNode in g.nodeList.keys():
				break

		
		#initNode = 'a'

		g.getNode(self.initNode).dist = 0

		heap = []

		for i in g.nodeList:
		  heappush(heap, g.getNode(i))

					
		while len(heap) > 0:
			heapify(heap)
			currNode = heappop(heap)
			print currNode
			for n in currNode.neighbors:
				if n.dist > currNode.dist + currNode.getCost(n) or (n.dist == currNode.dist + currNode.getCost(n) and n.hop_count > currNode.hop_count + 1):
					n.dist = currNode.dist + currNode.getCost(n)
					n.prev = currNode
					n.hop_count = currNode.hop_count + 1
					heappush(heap, currNode)
						
					
		for i in g.nodeList:
			print g.getNode(i)
		
		print '\n{0:12} {1:7} {3:7} {2:10}'.format('Start/End:', 'Cost:', 'Path:', 'Hops:')
			
		for i in g.nodeList:
			p= self.get_path(g.getNode(i))
			print '{0:12} {1:7} {3:7} {2:10}'.format('('+self.initNode+','+g.getNode(i).getName()+')', str(g.getNode(i).dist), str(p), str(len(p)-1))
			
			
		# for i in g.nodeList:
			# print "Shortest Path (" + self.initNode + "," + g.getNode(i).getName() + ")"+ " --- " + str(self.get_path(g.getNode(i)))
