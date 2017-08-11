import os
import sys
import re

from collections import defaultdict

def depth_search(graph, start):
    visited, stack = set(), list(start)
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)
    return visited

def depth_search_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for node in set(graph[start]) - visited:
        depth_search_recursive(graph, node, visited)
    return visited


if __name__ == '__main__':
    graph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'\d+',line)
            graph[line_lst[0]] += line_lst[1:]
    for vertex in graph:
        print(f'vertex {vertex} has edges: {graph[vertex]}')
    depth_search(graph, sys.argv[2])
