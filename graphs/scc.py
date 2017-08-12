import sys
import re
import resource

from collections import defaultdict

sys.setrecursionlimit(10 ** 6)
resource.setrlimit(resource.RLIMIT_STACK, (2 ** 29, 2 ** 30))


def reverse_graph(graph):
    reversegraph = defaultdict(list)
    for node in graph.keys():
        for edge in graph[node]:
            reversegraph[edge] += [node]
    return reversegraph

def dfsfirstpass(graph, start, stack=list(), visited=set()):
    visited.add(start)
    for edge in set(graph[start]) - visited:
        dfsfirstpass(graph, edge, stack, visited)
    stack.append(start)
    return stack

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
    sccsizelist = []
    for key in leaderlist.keys():
        size = len(leaderlist[key])
        sccsizelist.append(size)
    sccsizelist.sort()
    return sccsizelist[-5:]


if __name__ == '__main__':
    graph = defaultdict(list)
    rgraph = defaultdict(list)
    with open(sys.argv[1]) as f:
        for line in f:
            line_lst = re.findall(r'(\d+|\w+)',line)
            graph[line_lst[0]] += [line_lst[1]]
            rgraph[line_lst[1]] += [line_lst[0]]
    stack1 = dfsfirstpass(graph, 'Mike')
    print(f'stack is {stack1} and graph is {graph}')
    print(f'stack is {len(stack1)} and keys are {len(graph.keys())}')
