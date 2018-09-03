import random
from itertools import combinations
from random import shuffle
import sys
from union_find_solutions import eagerUF
import time

random.seed(42)
def generate_pairs(node_combinations, num):
    shuffle(node_combinations)
    return node_combinations[0:num]

def test_solution(solution, unions, finds):
    print solution.count()
    print map(solution.connected, unions)
    start_time = time.time()
    map(solution.union, unions)
    end_time = time.time()
    print("Eager Union Elapsed time was %0.10f micro-seconds" % (float(end_time - start_time)*1e6/len(unions)))
    print map(solution.connected, unions)
    start_time = time.time()
    print map(solution.connected, finds)
    end_time = time.time()
    print("Eager Find Elapsed time was %0.10f micro-seconds" % (float(end_time - start_time)*1e6/len(finds)))
    print solution.count()

def main():
    num_nodes = int(sys.argv[1])
    num_unions = int(sys.argv[2])
    num_finds = int(sys.argv[3])

    print list(xrange(num_nodes))
    nodes =  xrange(num_nodes)
    node_combinations = list(combinations(nodes, 2))

    unions = generate_pairs(node_combinations, num_unions)
    print unions
    finds = generate_pairs(node_combinations, num_finds)
    print finds

    soln = eagerUF(num_nodes)
    test_solution(soln, unions, finds)

    

if __name__ == "__main__":
    # execute only if run as a script
    main()