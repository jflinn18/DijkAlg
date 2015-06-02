from graph_creation import *
from heapq import *

#print("Which node is the starting node: ")
#initNode = input()

initNode = 'a'

# param - a Node object
def get_path(last_node):
	s = last_node.getName()
	while not last_node == initNode:
		last_node = last_node.prev
		s.append(last_node.getName())
		
	return s

	
g.getNode(initNode).dist = 0

heap = []

for i in g.nodeList:
  heappush(heap, g.getNode(i))
  
print str([i.name for i in heap])
	
	
#while not heap.empty():    # heap will never be empty. FIX ME
# while len(heap) > 0:
	# currNode = heappop(heap)
	# print currNode
	# for n in g.getNode(currNode).neighbors:
		# if n.dist > currNode.dist + g.getNode.getCost(n):
			# n.dist = currNode.dist + g.getNode.getCost(n)
			# n.prev = currNode.getName()
			# heappush(heap, (n.dist, n))
			
			
while len(heap) > 0:
	currNode = heappop(heap)
	print currNode
	for n in currNode.neighbors:
		print n
		if n.dist > currNode.dist + currNode.getCost(n):
			n.dist = currNode.dist + currNode.getCost(n)
			n.prev = currNode.getName()
			heappush(heap, currNode)
			
for i in g.nodeList:
	print str(g.getNode(i).getName() + " " + str(g.getNode(i).dist))
