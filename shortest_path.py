from DijkstraAlgorithmH import *
from Astar import *



da = DijkstraAlgorithmH()
aa = Astar()


while True:
	print "Which Algorithm would you like to run?",
	resp = raw_input()
	if resp[0] == 'a' or resp[0] == 'A':
		path = aa.as_alg()
		print path
		break
	elif resp[0] == 'd' or resp[0] == 'D':
		da.dijk_alg()
		break
	else:
		continue