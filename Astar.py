#from graph_creationF import *
from heapq2 import *
from random import *
import pdb
from time import *


class Astar(object):
	
	def __init__(self, init_node, goal_node, rr):
		self.initNode = init_node
		self.goalNode = goal_node
                self.random_range = int(rr)
		self.time = ''
		self.cost = 0
		seed()
		

        def init():
                self.initNode = init_node
                self.goal = goal_node
                self.random_range = int(rr)
                
	
	# param - a Node object
	def get_path(self, last_node):
		s = [last_node.getName()]
		while not last_node.prev is None:
			last_node = last_node.prev
			s.append(last_node.getName())
		
		s.reverse()
		return s

		
	def input_initNode(self):
		print "\n"
		n = raw_input("Which node is the starting node? ")
		return n
		
	def input_goalNode(self):
		n = raw_input("Which node is the goal node? ")
		return n
                
        def input_range(self):
                resp = raw_input("Enter upper bound for random range: ")
                try:
                        return int(resp)
                except ValueError:
                        print "Please enter an int"
                        self.input_range()
		
	def get_time(self, start, end):
		self.time = str(end - start)

        def in_heap(self, heap, node):
                for n in heap:
                        if n.getName() == node.getName():
                                return True
                return False
		
	def heuristic_cost_estimate(self):
		#return 0
                return randint(0, self.random_range)

	def as_alg(self, graph):
		closedset = set()
                
                #pdb.set_trace()

                if self.initNode == None or self.goalNode == None:
                        while True:
                                self.initNode = self.input_initNode()
                                self.goalNode = self.input_goalNode()
                                self.random_range = self.input_range()
                                if self.goalNode in graph.nodeList.keys() and self.initNode in graph.nodeList.keys():
                                        break


		
		#initNode = 'a'

		graph.getNode(self.initNode).dist = 0
		graph.getNode(self.initNode).f_score = 0

		heap = []
		
		start = time()
                path = None
		
		heappush(heap, graph.getNode(self.initNode))


		while len(heap) > 0:
			#pdb.set_trace()
			heapify(heap)
			currNode = heappop(heap)
			#print currNode
			#pdb.set_trace()
                        if currNode.getName() == graph.getNode(self.goalNode).getName():
                                
				# print currNode
				# print self.goalNode
				# pdb.set_trace()
				path = self.get_path(graph.getNode(self.goalNode))
				
				# This won't work if the graph is unweighted.
				self.cost = currNode.dist
				break
			closedset.add(currNode)
				
			for n in currNode.neighbors:
				if n in closedset:
					continue

				tentative_g_score = currNode.dist + currNode.getCost(n)
				#pdb.set_trace()
	
                                #how does this compare n to the objects in the heap?
				if not self.in_heap(heap, n) or (tentative_g_score < n.dist and n.dist != float("inf")):
					if not self.in_heap(heap, n):
						heappush(heap, n)	
						
					n.prev = currNode

					n.dist = tentative_g_score		
#					pdb.set_trace()

#					n.hop_count = currNode.hop_count + 1
					
					n.f_score = n.dist + self.heuristic_cost_estimate()
					
# Note: Is the printed cost the cost of the last Node? Am I updating the cost correctly for			
		
		end = time()
		self.get_time(start, end)
		
                # Running input100.txt will not assign path before it is referenced
                hops = 0
                if path is None:
                        path = "Goal Node not found"
                else:
                        hops = len(path) - 1
                        
		print "\nHops: " + str(hops)
		print "Cost: " + str(self.cost)
		print "Path: " + str(path)
		print "Time: " + self.time
		
