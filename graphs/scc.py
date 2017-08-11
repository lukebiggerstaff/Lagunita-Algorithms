import sys
import re

from collections import defaultdict


def graph_reverse(graph):
    reversegraph = defaultdict(list)
    for node in graph.keys():
        for edge in graph[node]:
            reversegraph[edge] += node
    return reversegraph

def dfsfirstpass(graph, stack=list(), start=1):
    visited = set()
    vertex = start
    if start not in visited:
        visited.add(start)
        for edge in set(graph[start]) - visited:
            dfsfirstpass(graph, edge)
    stack.append(vertex)
    return stack


if __name__ == '__main__':
    graph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'(\d+|\w+)',line)
            graph[line_lst[0]] += line_lst[1:]
    print(graph)
    stack1 = dfsfirstpass(graph)
    print(stack1)
    stack2 = dfsfirstpass(graph_reverse(graph))
    print(stack2)
