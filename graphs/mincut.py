import os
import sys
import random

from collections import defaultdict


def compute(graph):
    if len(graph) < 3:
        return graph
    contract(graph)
    return compute(graph)

def contract(graph):
    vertex1 = random.randrange(1, len(graph))
    vertex2 = graph[vertex1][random.randrange(0, len(graph[vertex1]))]
    supernode, contractednode = (
                        (vertex1,vertex2) if vertex1 - vertex2 < 0
                        else (vertex2,vertex1))
    for each in graph[contractednode]:
        if each is supernode: pass
        else:
            # need to change edges with contractednode to supernode
            for index, value in enumerate(graph[each]):
                if value is contractednode:
                    graph[each][index] = supernode
            # need to append any edge to the new supernode edge list
            graph[supernode].append(each)
    del graph[contractednode]


if __name__ == '__main__':
    graph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = [int(x) for x in line.split('\t') if x is not '\n']
            graph[line_lst[0]] = line_lst[1:]
    compute(graph)
    for node in graph:
        print(f'this is node: {node} with edges: {graph[node]}')

