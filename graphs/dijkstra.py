import sys
import re
import random

from collections import defaultdict, deque

def shortestpath(graph, start):
    Q = set(
        [x for x in graph]).union(
        [y for x in graph for y in graph[x]]
    )

    prev = defaultdict(None)
    dist = defaultdict(int)

    for v in Q:
        dist[v] = 10 ** 20
        prev[v] = None

    dist[start] = 0

    def printinfo():
        for v in Q:
            print(f'Q has { v }')
        for v in dist:
            print(f'dist for { v } is { dist[v] }')
        for v in prev:
            print(f'prev for { v } is { prev[v] }')


    def traceback(node, path):
        if node is start:
            path.appendleft(node)
            print(path)
            return
        print(f'{node} -> {prev[node]}')
        path.appendleft(node)
        traceback(prev[node],path)

    def findmin(Q, dist):
        klist = [x for x in dist if x in Q]
        mindict = defaultdict(dict)
        for k in klist: mindict[k] = dist[k]
        minvalue =  min(mindict, key=mindict.get)
        Q.remove(minvalue)
        return minvalue

    while Q:

        node = findmin(Q, dist)


        if node in graph:
            for edge, length in graph[node].items():
                alt = dist[node] + length
                if alt < dist[edge]:
                    dist[edge] = alt
                    prev[edge] = node

    resultset = [7,37,59,82,99,115,133,165,188,197]
    for each in resultset:
        path = deque()
        traceback(each, path)

    return dist, prev


if __name__ == '__main__':
    graph = defaultdict(dict)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'\d+,?\d*',line)
            graph[int(line_lst[0])] = {
                int(x):int(y) for x,y in [x.split(',') for x in line_lst[1:]]
            }
    shortestpath(graph, 1)
