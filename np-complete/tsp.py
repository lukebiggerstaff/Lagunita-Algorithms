import sys
import math
from itertools import combinations
from copy import deepcopy as dc

def read_file(plot):
    data = []
    with open(plot) as f:
        for line in f:
            line_lst = [float(x) for x in line.rsplit()]
            data.append(line_lst)
    return data

def find_distance(plot1, plot2):
    x = plot1[0]
    y = plot1[1]
    z = plot2[0]
    w = plot2[1]
    # Euclidean distance formula
    distance = math.sqrt(
        (x - z) ** 2 + (y - w) ** 2
    )
    return distance

def create_distance_matrix(data):
    n = len(data)
    dist = [[] for i in range(n)]
    for i in range(n):
        for j in range(n):
            result = find_distance(data[i], data[j])
            dist[i].append(result)
    return dist

def initialize_subproblem_matrix(data):
    sub = dict()
    n = len(data)
    sub[(0,)] = {0 : 0}
    for m in range(1,n):
        for i in combinations(range(1,n),m):
            tup_s = (0,) + i
            sub[tup_s] = {0 : 10 ** 20}
    return sub

def find_optimal_route(n, sub, dist):
    final_S = tuple(range(n))
    min_route = 10 ** 20
    for j in range(1,n):
        c_j0 = dist[j][0]
        path_value = sub[final_S][j]
        total_trip = path_value + c_j0
        if total_trip < min_route:
            min_route = total_trip
    return min_route

def solve_subproblems_and_find_route(data):
    n = len(data)
    sub = initialize_subproblem_matrix(data)
    dist = create_distance_matrix(data)
    # m = subproblem size - initial indice
    for m in range(1,n):
        for i in combinations(range(1,n),m):
            tup_s = (0,)  + i
            set_s = set(tup_s)
            for j in [x for x in tup_s if x != 0]:
                # deep copy set s in order to keep set s
                # and have {S} - j
                set_woj = dc(set_s)
                set_woj.remove(j)
                # create tuple of the set in order 
                # to use set as hash for dictionary key
                tup_woj = tuple(sorted([x for x in set_woj]))
                min_value = 10 ** 20
                for k in [x for x in set_s if x != j]:
                    cost_kj = dist[k][j]
                    p_prime = sub[tup_woj][k]
                    cur_path_value = cost_kj + p_prime
                    if cur_path_value < min_value:
                        min_value = p_prime + cost_kj
                sub[tup_s][j] = min_value
    optimal_route = find_optimal_route(n, sub, dist)
    return optimal_route


if __name__ == '__main__':
    data = read_file(sys.argv[1])
    result = solve_subproblems_and_find_route(data)
    print('best route is {}'.format(result))

