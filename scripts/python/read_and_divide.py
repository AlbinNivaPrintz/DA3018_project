import graph_class as gc
import sys
from time import time


start_1 = time()

print('Initializing parsing...')

g = gc.Graph.parse("resources/unsocial_contigs_over_{}.txt".format(sys.argv[1]))

end_1 = time()

print('Parsing complete and took {} seconds'.format(end_1 - start_1))

print('Creating subgraphs...')

start_3 = time()

l = g.csg_ify()

end_3 = time()

print('Subgraphs created. It took {} seconds'.format(end_3 - start_3))

print('Creating resultfile...')

start_4 = time()

with open('/results/Result_'+sys.argv[1]+'.txt', 'w+') as res:
    while l:
        res.write(l.popleft()+'\n')


end_4 = time()

print('Creating the result file took {} seconds'.format(end_4 - start_4))

print('Finished.')
