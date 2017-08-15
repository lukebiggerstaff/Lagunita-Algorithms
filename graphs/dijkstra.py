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

    for node in Q:
        dist[node] = 10 ** 20
        prev[node] = None

    dist[start] = 0

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
        print(f'distance for { each } is { dist[each] }')


if __name__ == '__main__':
    graph = defaultdict(dict)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'\d+,?\d*',line)
            graph[int(line_lst[0])] = {
                int(x):int(y) for x,y in [x.split(',') for x in line_lst[1:]]
            }
    shortestpath(graph, 1)
