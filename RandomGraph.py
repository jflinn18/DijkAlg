from random import * 
from string import *


class RandomGraph(object):

	def __init__(self):
		self.num_nodes = 0
		self.num_edges = 0
		self.cost_range = 0
		self.fname = ''
		self.alpha = "abcdefghijklmnopqrstuvwxyz"
		self.nodes = set()

	def randChar(self, y):
#		return ''.join(choice(ascii_lowercase) for x in range(y))
		while True:
			s = choice(ascii_lowercase)
			try:
				if s in self.alpha[0:(self.num_nodes)]:
					break
			except:
				print " --- Not enough node names --- "
				
		return s
		
		
	def UI(self):
		try:
			print "How many nodes do you want in the network?",
			self.num_nodes = int(raw_input())
			print "How many edges do you want in the network?",
			self.num_edges = int(raw_input())
			print "What file would you like to store this network in?",
			self.fname = raw_input()
			print "What is the upper limit of the range of the cost?",
			self.cost_range = int(raw_input())
			
			if self.num_edges > ((self.num_nodes*(self.num_nodes-1))/2):
				raise Exception(" --- Too Many Edges --- ")
			if self.num_nodes > 26:
				raise Exception(" --- Too Many Nodes --- ")
		except Exception as e:
			print e
			self.UI()
		except:
			print "Something unforeseeable happened"
		
		
	def randNet(self):
		self.UI()
		file = open(self.fname, 'w')
		
		for x in range(int(self.num_edges)):
			while True:
				a = self.randChar(1) 
				b = self.randChar(1)
				if not a == b and not str(a+b) in self.nodes:
					break
					
			file.write(a + " " + b + " " + str(randint(1, self.cost_range)) + "\n")
			self.nodes.add(str(a+b))
			self.nodes.add(str(b+a))
			

		file.close()