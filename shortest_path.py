from DijkstraAlgorithmH import *



again = True
da = DijkstraAlgorithmH()

def again():
	print "Do you want to go again? "
	resp = raw_input()
	
	print "\n\n"
	
	if resp == 'no' or resp == 'n' or resp == 'N':
		return False

		
		
while again:
	da.dijk_alg()
	again = again()