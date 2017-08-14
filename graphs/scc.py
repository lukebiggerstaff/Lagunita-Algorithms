import sys
import re
import resource

from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))

def dfsfirstpass(graph):
    visited = set()
    stack = list()
    for i in graph.keys():
        start = str(i)
        if start in graph:
            dfsfirstpassrecursive(graph, start, stack, visited)
    return stack

def dfsfirstpassrecursive(graph, start, stack, visited):
    if start not in visited:
        visited.add(start)
        if start in graph:
            for edge in graph[start]:
                if edge not in visited:
                    dfsfirstpassrecursive(graph, edge, stack, visited)
        stack.append(start)

def dfssecondpass(rgraph, stack):
    visited = set()
    leaderlist = defaultdict(list)
    while stack:
        start = stack.pop()
        if start not in visited:
            visited.add(start)
            leader = start
            leaderlist[leader] += [start]
            for edge in set(rgraph[start]) - visited:
                dfsrecursive(rgraph, edge, visited, leaderlist, leader)
    return leaderlist

def dfsrecursive(graph, start, visited, leaderlist, leader):
    visited.add(start)
    leaderlist[leader] += [start]
    for edge in set(graph[start]) - visited:
        dfsrecursive(graph, edge, visited, leaderlist, leader)

def return_top_five_scc(leaderlist):
    sccsizelist = list()
    for key in leaderlist.keys():
        size = len(leaderlist[key])
        sccsizelist.append(size)
    sccsizelist.sort()
    return sccsizelist[-5:]

def kosaraju(graph, rgraph):
    stack = dfsfirstpass(rgraph)
    #print(f'stack is {stack}')
    leaderdict = dfssecondpass(graph, stack)
    #print(f'graph is {graph}\n'
          #f'leader is {leaderdict}\n')
    top5 = return_top_five_scc(leaderdict)
    return top5


if __name__ == '__main__':
    graph = defaultdict(list)
    rgraph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'(\d+|\w+)',line)
            graph[line_lst[0]] += [line_lst[1]]
            rgraph[line_lst[1]] += [line_lst[0]]
    print(kosaraju(graph,rgraph))
