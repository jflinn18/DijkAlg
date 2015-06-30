resp = raw_input("How many iteration will you be making? ")
wgraph = raw_input("Enter graph file: ")
weighted = raw_input("Do you want to create a weighted graph? ")
walg = raw_input("Which algorithm will you be using? ")
starting_node = raw_input("Starting Node: ")

if walg[0] == 'a':
  goal_node = raw_input("Goal Node:")

i = 0

fout = open("input" + resp + ".txt", 'wb')
fout.write(resp + '\n')

while i < int(resp):
  fout.write(wgraph + '\n')
  fout.write(weighted + '\n')
  fout.write(walg + '\n')
  fout.write(starting_node + '\n')
  if walg[0] == 'a':
    fout.write(goal_node + '\n')

  i = i + 1

fout.close()
  
  
