import shortest_path

i = 0

resp = raw_input("How many iterations do you want to do? ")


while i < int(resp):
    shortest_path.run()
    i = i + 1
