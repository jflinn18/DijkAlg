import os
import multiprocessing as mp
import pdb
from time import *


def run_auto(f):
    try:
        os.system('python Auto.py -f ' + directory + '/' + f + ' > log.txt')
    except:
        print "-----EOFError-----"
        print directory + '/' + f

    os.system('mv log.txt data/' + alg[1] + '/' + alg[-1] + '/rawdata_0/' + f)



while True:
    try:
        directory = raw_input('Enter the input directory: ')
        if directory[:5] == 'input':
            break
        else:
            print 'Try Again...'
    except:
        print 'Try Again...'
    
start = time()

if directory[-1:] == '/':
    directory = directory[:-1]
        

alg = directory.split('/')

dirs = os.listdir(directory)

#pool = mp.Pool(processes = 4)
#[pool.map(run_auto, f) for f in dirs]
#results = [pool.apply_async(run_auto, args=(f,)) for f in dirs]
#output = (p.get() for p in results)
    

end = time()

print 'Time: ' + str(end - start)
