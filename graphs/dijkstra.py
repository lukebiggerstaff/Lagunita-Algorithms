import sys
import re
import random

from collections import deque, defaultdict

def shortestpath(graph, start, end):
    pass


if __name__ == '__main__':
    graph = defaultdict(set)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'(\d+|\w+)',line)
            print(f'line_lst is { line_lst }')
