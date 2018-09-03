import random
from itertools import combinations
from random import shuffle
import sys
from union_find_solutions import quick_find_UF
from union_find_solutions import quick_union_UF
from union_find_solutions import weighted_quick_union_UF
import time

random.seed(42)
def generate_pairs(node_combinations, num):
    shuffle(node_combinations)
    return node_combinations[0:num]

def test_solution(solution, unions, finds):
    #print solution.count()
    map(solution.connected, unions)
    start_time = time.time()
    map(solution.union, unions)
    end_time = time.time()
    print("Union op = %6.10f micro-seconds" % (float(end_time - start_time)*1e6/len(unions)))
    #map(solution.connected, unions)
    start_time = time.time()
    result = map(solution.connected, finds)
    end_time = time.time()
    print("Find op = %6.10f micro-seconds" % (float(end_time - start_time)*1e6/len(finds)))
    print solution.count()
    solution.set_result(result)

def main():
    num_nodes = int(sys.argv[1])
    num_unions = int(sys.argv[2])
    num_finds = int(sys.argv[3])

    #print list(xrange(num_nodes))
    nodes =  xrange(num_nodes)
    node_combinations = list(combinations(nodes, 2))

    unions = generate_pairs(node_combinations, num_unions)
    #print unions
    finds = generate_pairs(node_combinations, num_finds)
    #print finds

    quick_find = quick_find_UF(num_nodes)
    print quick_find.__doc__
    test_solution(quick_find, unions, finds)

    quick_union = quick_union_UF(num_nodes)
    print quick_union.__doc__
    test_solution(quick_union, unions, finds)

    weighted_quick_union = weighted_quick_union_UF(num_nodes)
    print weighted_quick_union.__doc__
    test_solution(weighted_quick_union, unions, finds)

    if quick_find.compare_result(quick_union.get_result()):
        print "quick union Results match"
    else:
        print "quick union Results don't match"
    
    if quick_find.compare_result(weighted_quick_union.get_result()):
        print "weighted quick union Results match"
    else:
        print "weighted quick union Results don't match"
    

if __name__ == "__main__":
    # execute only if run as a script
    main()