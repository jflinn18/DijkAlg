from DijkstraAlgorithmH import *
from Astar import *
from graph_creationF import *
import sys
import pdb



def run(resp):
    graph = gr_creation.get_file(resp[0])

    #pdb.set_trace()
    if resp == 'a' or resp == 'A':
        aa = Astar(init_node, goal_node, random_range)
        aa.as_alg(graph)		
    elif resp == 'd' or resp == 'D':
        da = DijkstraAlgorithmH(init_node)
        da.dijk_alg(graph)



try:
    if sys.argv[1] == '-f':
        if sys.argv[2][-4:] == '.txt':
            infile = open(sys.argv[2], 'rb')

            walg = infile.readline()
            walg = walg[:-1]
            wgraph = infile.readline()
            wgraph = wgraph[:-1]
            weighted = infile.readline()
            weighted = weighted[:-1]
            init_node = infile.readline()
            init_node = init_node[:-1]

            if walg[0] == 'a' or walg[0] == 'A':
                goal_node = infile.readline()
                goal_node = goal_node[:-1]
                random_range = infile.readline()
                random_range = random_range[:-1]

            #pdb.set_trace()
            infile.close()

    if sys.argv[3] == '-i':
        times = int(sys.argv[4])
            
except IndexError:
    walg = raw_input("Enter Algorithm: ")
    wgraph = raw_input("Enter graph file: ")
    weighted = raw_input("Do you want a weighted Graph? ")
    init_node = raw_input("Enter starting node: ")

    if walg[0] == 'a' or walg[0] == 'A':
        goal_node = raw_input("Enter goal node: ")
        random_range = raw_input("Enter upper bound for random range: ")

except:
    print "-----Graph File doesn't Exist-----"
 
# see if dijk works with the same graph
# if not...move this into run()       
gr_creation = graph_creationF(weighted, wgraph)
#gr_creation = graph_creationF()

try:
    if sys.argv[3] == '-i':
        i = 0
        while i < times:
            run(walg[0])
            i += 1
except IndexError:
    run(walg[0])
