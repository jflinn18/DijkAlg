import os


wgraph = raw_input("Enter a graph file: ")
weighted = raw_input("Do you want a weighted graph? ")

num_nodes = wgraph.split('_')
num_nodes = num_nodes[1]
num_nodes = num_nodes[1:]
num_nodes = int(num_nodes)

if weighted == 'y':
    w = 'w'
else:
    w = 'uw'


heur_count = 0
init_node_count = 0
goal_node_count = 0

while heur_count < 16:
    while init_node_count < num_nodes:
        while goal_node_count < num_nodes:
            files = os.listdir('input/astar')
            f = 'input/astar/' + str(init_node_count) + 'and' + str(goal_node_count) + '_' + 'n' + str(num_nodes) + '_' + w + '_rr' + str(heur_count) + '.txt'
            if f not in files:
                fout = open(f, 'wb')

                fout.write('a\n')
                fout.write(wgraph + '\n')
                fout.write(weighted + '\n')
                fout.write(init_node_count + 'n')
                fout.write(goal_node_count + 'n')
                fout.write(heur_count + '/n')

                fout.close()


                init_node_count += 1
                goal_node_count += 1
                heur_count += 1
