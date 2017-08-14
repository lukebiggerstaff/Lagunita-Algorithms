import sys
import re
import random

from collections import deque, defaultdict

def shortestpath(graph, start, end):
    Q, V = deque([start]), set()
    prev = defaultdict(None)

    prev[start] = start

    def traceback(node, path):
        if node is start:
            path.appendleft(node)
            print(path)
            return
        print(f'{node} -> {prev[node]}')
        path.appendleft(node)
        traceback(prev[node],path)

    while Q:
        node = Q.popleft()
        print(f'searching node { node }')
        if node not in V:
            V.add(node)
            for edge in [graph[node]]:
                if edge is end:
                    path = deque([edge])
                    print(f'found end "{ end }"')
                    print(f'{edge} -> {node}')
                    traceback(node,path)
                if edge in graph:
                    Q.append(edge)
                    prev[edge] = node


if __name__ == '__main__':
    graph = defaultdict(set)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'(\d+|\w+)',line)
            graph[line_lst[0]].add(line_lst[1])
    allnodes = [x for x in set(
                                [x for x in graph]
                              ).union(
                                [y for x in graph for y in [z for z in graph[x]]]
                              )]
    sortednodes = sorted(allnodes)
    begin = sortednodes[0]
    end = sortednodes[len(sortednodes)- 1]
    print(f'graph is { graph }\n'
          f'type of graph is { type( graph ) }\n')
    shortestpath(graph, begin, end)
