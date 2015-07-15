import os
import multiprocessing as mp
import pdb
from time import *
import Queue
import threading


def run_auto(f):
    try:
        os.system('python shortest_path.py -f ' +  directory + '/' + f + ' -i 1000 > data/' + alg[1] + '/' + alg[-1] + '/rawdata_0/' + f)

    except:
        print "-----Error-----"
        print directory + '/' + f

  

    return directory + '/' + f + '   -----Done-----'



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

pool = mp.Pool(processes = len(dirs))
#[pool.map(run_auto, f) for f in dirs]
results = [pool.apply_async(run_auto, args=(f,)) for f in dirs]
#[pool.apply_async(run_auto, args=(f,)) for f in dirs]
#output = (p.get() for p in results)



end = time()

for r in results:
    print r

print 'Time: ' + str(end - start)
