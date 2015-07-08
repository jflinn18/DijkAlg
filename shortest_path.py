from DijkstraAlgorithmH import *
from Astar import *
from DPRRS import *
from HotPotato import *
import graph_creationF


def run():
    da = DijkstraAlgorithmH()
    aa = Astar()
    dprrs = DPRRS()
    hp = HotPotato()
#    gc = graph_creationF()


    while True:
	resp = raw_input("Which Algorithm would you like to run? ")
        graph_creationF.get_file(resp[0])
	if resp[0] == 'a' or resp[0] == 'A':
		aa.as_alg()		
		break
	elif resp == 'dprrs' or resp == 'DPRRS':
		dprrs.dprrs_alg()
		break
	elif resp[0] == 'h' or resp[0] == 'H':
		hp.hp_alg()
		break
	elif resp[0] == 'd' or resp[0] == 'D':
		da.dijk_alg()
		break
	else:
		continue

# for the unautomated program. Comment out to automate it
#run()
