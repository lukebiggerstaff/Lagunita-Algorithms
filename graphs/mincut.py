import os
import sys
import random

from copy import deepcopy
from collections import defaultdict


def compute(graph):
    if len(graph) < 3:
        return len(graph[random.choice(list(graph.keys()))])
    contract(graph)
    return compute(graph)

def contract(graph):
    vertex1 = random.choice(list(graph.keys()))
    vertex2 = graph[vertex1][random.randrange(0, len(graph[vertex1]))]
    supernode, contractednode = (
                        (vertex1,vertex2) if vertex1 - vertex2 < 0
                        else (vertex2,vertex1))
    # transfer all edges that point to contracted node to super node
    for edge in graph[contractednode]:
        graph[edge][:] = [x if x is not contractednode else supernode
                          for x in graph[edge]]
        graph[supernode].append(edge)
    # remove self loops from super node
    graph[supernode][:] = [x for x in graph[supernode]
                        if x is not supernode or not contractednode]
    # remove contracted node
    del graph[contractednode]

def find_min_cut(graph, interval):
    counter = interval
    mincut = 0
    while counter > 0:
        graph_copy = deepcopy(graph)
        result = compute(graph_copy)
        print(f'result is {result} and mincut is currently {mincut}')
        if mincut is 0:
            mincut = result
        else:
            mincut = result if result < mincut else mincut
        counter -= 1
    return mincut


if __name__ == '__main__':
    graph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = [int(x) for x in line.split('\t') if x is not '\n']
            graph[line_lst[0]] += line_lst[1:]
    find_min_cut(graph, int(sys.argv[2]))
