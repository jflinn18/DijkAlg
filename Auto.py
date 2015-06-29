import pexpect
import pdb

#resp = raw_input("How many iterations of the script do you want? ")
#graph_file = raw_input("Enter graph file: ")
#wgraph = raw_input("Do you want a weighted graph? ")
#walg = raw_input("Which Algoritm would you like to run? ")
#starting_node = raw_input("Enter starting node: ")
#if walg[0] == 'a':
#  end_node = raw_input("Enter end node: ")

i = 0

while i < 1:
  child = pexpect.spawn("python shortest_path.py")

  fout = open('log.txt', 'ab')
  child.logfile = fout
#  child.expect("Enter graph file: ")
  child.send("graphs/gr_n20_d2.txt")
#  pdb.set_trace()
#  child.expect("Do you want to create a weighted Graph? ")
  child.send("y")
#  child.expect("Algorithm")
  child.send("a")
#  child.expect("starting")
  child.send('0')
#  if walg[0] == 'a':
  child.expect("goal")
  child.send('10')

  child.expect("Hops:")
  child.close()
  

  i = i + 1
