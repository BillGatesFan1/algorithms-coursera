class UF(object):
    '''Abstract UF Class'''
    def __init__(self, N):
        self.num_nodes = N
        self.component = list(xrange(N))
    
    def union(self, nums):
        '''add connection between nums p and q'''
        pass
    
    def connected(self, nums):
        '''are nums p andd q in the same component'''
        pass
    
    def find(self, p):
        '''component identifier for p'''
        return self.component[p]
    
    def count(self):
        '''number of components'''
        return len(set(self.component))


class eagerUF(UF):
    '''Eager UF Class'''
    def __init__(self, N):
        super(eagerUF, self).__init__(N)
        
    def union(self, nums):
        '''add connection between nums p and q'''
        pid = self.component[nums[0]]
        qid = self.component[nums[1]]
        for i in xrange(self.num_nodes):
            if self.component[i] == pid:
                self.component[i] = qid
    
    def connected(self, nums):
        '''are nums p andd q in the same component'''
        return self.component[nums[0]] == self.component[nums[1]]