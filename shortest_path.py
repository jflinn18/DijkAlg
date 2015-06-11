from DijkstraAlgorithmH import *
from Astar import *



da = DijkstraAlgorithmH()
aa = Astar()


while True:
	print "Which Algorithm would you like to run?",
	resp = raw_input()
	if resp[0] == 'a' or resp[0] == 'A':
		aa.as_alg()		
		break
	elif resp[0] == 'd' or resp[0] == 'D':
		da.dijk_alg()
		break
	elif resp[0] == 'h' or resp[0] == 'H':
		
		break
	else:
		continue