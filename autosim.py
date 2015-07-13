import os
import pdb
from time import *

while True:
    directory = raw_input('Enter the input directory: ')
    if directory[:5] == 'input':
        break
    else:
        print 'Try Again...'
    
start = time()

if directory[-1:] == '/':
    directory = directory[:-1]
        

alg = directory.split('/')

dirs = os.listdir(directory)

for f in dirs:
    i = 0
    try:
        os.system('python Auto.py -f ' + directory + '/' + f + ' > log.txt')
    except:
        print "-----EOFError-----"
        print directory + '/' + f

    os.system('mv log.txt data/' + alg[1] + '/' + alg[-1] + '/rawdata_0/' + f)

end = time()

print 'Time: ' + str(start-end)
