import random
import sys

#sys.argv[1] could be either -u or -c. -u is for 'user' and -c is for 'computer'

if sys.argv[1] == '-u':
  resp = raw_input("How many iterations would you like to do? ")
  wgraph = raw_input("Enter graph file: ")
  weighted = raw_input("Do you want to create a weighted graph? ")
  walg = raw_input("Which algorithm will you be using? ")
  init_node = raw_input("Starting Node: ")

  if walg[0] == 'a':
    goal_node = raw_input("Goal Node: ")

  random_range = raw_input("Enter the random range: ")

else:
  random.seed()

  resp = str(1000)
  wgraph = "graphs/gr_n40_d2.txt"
  weighted = 'y'
  walg = 'a'
  init_node = str(random.randint(0, 40))
  goal_node = str(random.randint(0, 40))
  random_range = '10'

  while goal_node == init_node:
    goal_node = str(random.randint(0, 40))

i = 0

fout = open("DijkAlg/input/input" + init_node + "and" + goal_node + ".txt", 'wb')
fout.write(resp + '\n')

while i < int(resp):
  fout.write(wgraph + '\n')
  fout.write(weighted + '\n')
  fout.write(walg + '\n')
  fout.write(init_node + '\n')
  if walg[0] == 'a':
    fout.write(goal_node + '\n')
  fout.write(random_range + '\n')

  i = i + 1

fout.close()
  
  
