import sys
import re
import random

from collections import deque, defaultdict

def shortestpath(graph, start, end):
    pass


if __name__ == '__main__':
    graph = defaultdict(dict)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'\d+,?\d*',line)
            graph[int(line_lst[0])] = {
                int(x):int(y) for x,y in [x.split(',') for x in line_lst[1:]]
            }
    for node in graph:
        print(f'node is { node }\n'
              f'edges are { graph[node] }\n')
