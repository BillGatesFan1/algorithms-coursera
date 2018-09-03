class UF(object):
    '''Abstract UF Class'''
    def __init__(self, N):
        self.num_nodes = N
        self.component = list(xrange(N))
        self.result = []
    
    def union(self, nums):
        '''add connection between nums p and q'''
        raise NotImplementedError

    def connected(self, nums):
        '''are nums p andd q in the same component'''
        raise NotImplementedError
    
    def find(self, p):
        '''component identifier for p'''
        return self.component[p]
    
    def count(self):
        '''number of components'''
        return len(set(self.component))
    
    def get_result(self):
        return self.result
    
    def set_result(self, res):
        self.result = list(res)

    def compare_result(self, result):
        if self.result == result:
           return True
        return False

class quick_find_UF(UF):
    '''Quick-Find'''
    def __init__(self, N):
        super(quick_find_UF, self).__init__(N)
        
    def union(self, nums):
        '''add connection between nums p and q'''
        pid = self.component[nums[0]] # component of p
        qid = self.component[nums[1]] # component of q
        for i in xrange(self.num_nodes):
            # for all nodes that share the same component as p
            if self.component[i] == pid:
                # set the component of this node to the component of q
                self.component[i] = qid
    
    def connected(self, nums):
        '''are nums p andd q in the same component'''
        return self.component[nums[0]] == self.component[nums[1]]

class quick_union_UF(UF):
    '''Quick Union'''
    def __init__(self, N):
        super(quick_union_UF, self).__init__(N)
    
    def give_parent(self, p):
        return self.component[p]

    def give_root(self, p):
        while self.component[p] != p:
            p = self.component[p]
        return p
    
    def union(self, nums):
        '''add connection between nums p and q'''
        # set the root node of q to be the root of p 
        self.component[self.give_root(nums[1])] = self.give_root(self.component[nums[0]])
    
    def connected(self, nums):
        '''are nums p andd q in the same component'''
        # if the nodes share root node, they are connected
        return self.give_root(self.component[nums[0]]) == self.give_root(self.component[nums[1]])

    def count(self):
        '''number of components'''
        return len(set(map(self.give_root,self.component)))

class path_compressed_quick_union_UF(quick_union_UF):
    '''path compressed Quick Union'''
    def __init__(self, N):
        super(path_compressed_quick_union_UF, self).__init__(N)
    
    def give_root(self, p):
        while self.component[p] != p:
            self.component[p] = self.component[self.component[p]]
            p = self.component[p]
        return p


class weighted_quick_union_UF(quick_union_UF):
    '''weighted quick union'''
    def __init__(self, N):
        self.component_size = [1 for x in range(N)]
        super(weighted_quick_union_UF, self).__init__(N)
    
    def union(self, nums):
        '''add connection between nums p and q'''
        # is the second tree bigger than the first?
        if self.component_size[self.give_root(nums[1])] > self.component_size[self.give_root(nums[0])]:
            # set the root node of first to be the root of second, since the first tree is smaller 
            self.component[self.give_root(nums[0])] = self.give_root(self.component[nums[1]])
            self.component_size[self.give_root(nums[0])] += \
                        self.component_size[self.give_root(self.component[nums[1]])]
        else:
            # set the root node of second to be the root of first, since the second tree is smaller or equal 
            self.component[self.give_root(nums[1])] = self.give_root(self.component[nums[0]])
            self.component_size[self.give_root(nums[1])] += \
                        self.component_size[self.give_root(self.component[nums[0]])]

class path_compressed_weighted_quick_union_UF(weighted_quick_union_UF):
    '''path compressed weighted quick union'''
    def __init__(self, N):
        self.component_size = [1 for x in range(N)]
        super(path_compressed_weighted_quick_union_UF, self).__init__(N)
    
    def give_root(self, p):
        while self.component[p] != p:
            self.component[p] = self.component[self.component[p]]
            p = self.component[p]
        return p