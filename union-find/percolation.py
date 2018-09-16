import random
import sys
import numpy as np
import pprint
from collections import defaultdict
from union_find_solutions import path_compressed_weighted_quick_union_UF

random.seed(42)

class grid_percolation(object):
    '''checks for percolation in a N x N grid'''
    def __init__(self,N,p, cylinder):
        self.grid_dim = N
        self.cylinder = cylinder
        self.open_probability = p
        self.grid = np.random.random((N,N)) < p
        #print self.grid.size
        #print self.grid
        #print
        #print self.grid[1:,:]
        #print 
        #print self.grid[:N-1,:]
        #print self.grid[:N-1,:].size
        #print
        self.south_union = self.grid[1:,:] * self.grid[:N-1,:] 
        #print "south_union "
        #print self.south_union
        #self.south_union = self.grid[:N-2,:] and self.grid[1:,:]
        #print " east_union "
        if self.cylinder == False:
            self.east_union = self.grid[:,:N-1] * self.grid[:,1:]
        else:
            #print
            #print np.roll(self.grid,1, axis=1)
            #print
            self.east_union = self.grid * np.roll(self.grid,1, axis=1)
        #print
        #print self.east_union
        self.pc_wuf = path_compressed_weighted_quick_union_UF(self.grid_dim*self.grid_dim)

    def set_union(self):
        N = self.grid_dim
        unions = [ (x[0]*N+x[1], x[0]*N+x[1]+N) for x in np.argwhere(self.south_union == True)]
        if self.cylinder == False:
            unions.extend( [ (x[0]*N+x[1], x[0]*N+x[1]+1) for x in np.argwhere(self.east_union == True)])
        else:
            unions.extend( [ (x[0]*N+x[1], x[0]*N+(x[1]+1) % (N-1)) for x in np.argwhere(self.east_union == True)])

        #print unions
        map(self.pc_wuf.union, unions)
    
    def find_percolation(self):
        N = self.grid_dim
        #print self.grid[0,:]
        #print self.grid[N-1,:]
        tops = [x[0] for x in list(np.argwhere(self.grid[0,:] == True))]
        bottoms = [x[0] for x in list(np.argwhere(self.grid[N-1,:] == True) + N*(N-1))]
        #print tops
        #print bottoms
        for i in tops:
            for j in bottoms:
                #print type(i)
                if self.pc_wuf.connected((i, j)):
                    return True
        return False
                 
        #unconnected_tops = []
        #while any(tops) 



def main():
    if bool(sys.argv[3]) != True:
        prob = np.arange(0.55, 0.62, 0.005, np.float)
    else:
        prob = np.arange(0.6, 0.7, 0.005, np.float)
    results = defaultdict(list)
    for p in prob:
        for i in range(int(sys.argv[2])):
            soln = grid_percolation(int(sys.argv[1]), p, bool(sys.argv[3]))
            soln.set_union()
            results[p].append(soln.find_percolation())
            #print " Grid Percolation = ", soln.find_percolation()
    #pprint.pprint(sorted(results.items()))
    for k,v in sorted(results.items()):
        print k, float(sum(v))/len(v)

if __name__ == "__main__":
    # execute only if run as a script
    main()