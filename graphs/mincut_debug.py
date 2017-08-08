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
    print(f'#####Debugging when starting contract: graph is {graph}\n')
    vertex1 = random.choice(list(graph.keys()))
    try:
        vertex2 = graph[vertex1][random.randrange(0, len(graph[vertex1]))]
    except ValueError as e:
        print(f'ERROR: current graph is {graph}')
        print(e)
    finally:
        print(f'1) Debugging after setting vert2: graph is {graph}')
    supernode, contractednode = (
                        (vertex1,vertex2) if vertex1 - vertex2 < 0
                        else (vertex2,vertex1))
    # transfer all edges that go to contracted node to super node
    for edge in graph[contractednode]:
        graph[edge][:] = [x if x is not contractednode else supernode
                          for x in graph[edge]]
        graph[supernode].append(edge)
    print(f'2) Debugging after transfer: graph is currently {graph}')
    # remove self loops from super node
    graph[supernode][:] = [x for x in graph[supernode]
                        if x is not supernode or not contractednode]
    print(f'3) Debugging after removing self loops: graph is currently {graph}')
    # remove contracted node
    del graph[contractednode]
    print(f'4) Debugging after removing contractednode: graph is currently {graph}\n')


if __name__ == '__main__':
    graph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = [int(x) for x in line.split('\t') if x is not '\n']
            graph[line_lst[0]] = line_lst[1:]
    compute(graph)
    for node in graph:
        print('this is node: {} with edges: {}'.format(node, graph[node]))

