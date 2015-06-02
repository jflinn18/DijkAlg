from DijkstraAlgorithmH import *



again = True
da = DijkstraAlgorithmH()

def again():
	print "Do you want to go again?",
	resp = raw_input()
	
	if resp == 'no' or resp == 'n' or resp == 'N':
		return False

		
		
while again:
	da.dijk_alg()
	print "\n"
	again = again()