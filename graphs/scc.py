import os
import sys

from collections import defaultdict, dequeue

if __name__ == '__main__':
    graph = defaultdict(list)
    reversegraph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = [x for x in line.rstrip().split(' ')]
            graph[line_lst[0]].append(line_lst[1])
            reversegraph[line_lst[1]].append(line_lst[0])
