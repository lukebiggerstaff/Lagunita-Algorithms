import os
import sys
import re

from collections import defaultdict, deque

def breadth_search(graph, start):
    visited, queue = set(), deque(start)
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
            print(vertex)
    return visited

if __name__ == '__main__':
    graph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'\d+',line)
            graph[line_lst[0]] += line_lst[1:]
    breadth_search(graph, sys.argv[2])
