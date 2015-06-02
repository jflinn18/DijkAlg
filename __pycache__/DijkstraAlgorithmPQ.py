from graph_creation import *
from queue import *

#print("Which node is the starting node: ")
#initNode = input()

g.getNode('a').dist = 0

q = PriorityQueue()

for i in g.nodeList:
	q.put(g.getNode(i))

#currNode=[]
	
while not q.empty():
	currNode = q.get()
	print(currNode)
	# for n in g.getNode(currNode).neighbors:
		# if n.dist > currNode.dist + g.getNode.getCost(n):
			# n.dist = currNode.dist + g.getNode.getCost(n)
			# n.prev = currNode.getName()
			# q.put(n.dist, n)
			
			
# for i in g.nodeList:
	# print(i.getName + " " + i.dist)