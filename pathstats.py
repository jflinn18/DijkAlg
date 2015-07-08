import pdb
import sys

set_paths = set()
map_paths = {}
num_paths = 0

try:
    if sys.argv[1] == '-f':
        if sys.argv[2][-4:] == '.txt':
            infile = sys.argv[2]
except IndexError:
    while True:
        infile = raw_input("Input a path file: ")
        if infile[-4:] == '.txt':
            break

file_paths = open(infile, 'rb')

for line in file_paths:
    num_paths = num_paths + 1
    set_paths.add(line)

#pdb.set_trace()

for n in set_paths:
    map_paths[n[:-1]] = 0

file_paths.seek(0)
for line in file_paths:
    #pdb.set_trace()
    map_paths[line[:-1]] = map_paths[line[:-1]] + 1


#pdb.set_trace()

total_paths_taken = len(set_paths)


list_paths = map_paths.keys()


print '{1:10} {0:50}'.format('Path:', '%:')

total_perc = 0.0

for path in list_paths:
    #pdb.set_trace()
    print '{1:10} {0:50}'.format(path, str(float(map_paths[path]) / float(num_paths) * 100) + '%')
    total_perc = total_perc + float(map_paths[path]) / float(num_paths) * 100



print 'Number of paths: ' + str(num_paths)
print 'Number of paths taken: ' + str(total_paths_taken)
print 'Total percentage is: ' + str(total_perc)
file_paths.close()
