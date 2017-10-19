import sys
from collections import defaultdict

def readFileIntoGraph(file):
    graph = defaultdict(dict)
    with open(file) as f:
        for line in f:
            line_lst = [int(x) for x in line.strip().split()]
            if line_lst[0] not in graph:
                graph[line_lst[0]] = {
                    line_lst[1]:line_lst[2]
                }
            else:
                graph[line_lst[0]][line_lst[1]] = line_lst[2]
    return graph


def prim(graph):
    # initialize set to keep track of verticies not yet in tree
    vertsnotintree = set(
        [x for x in graph]).union(
        [y for x in graph for y in graph[x]]
    )

    # create empty set to keep track of verts and start with random vertex
    vertsintree = set()
    vertsintree.add(vertsnotintree.pop())
    print('starting vert is {}'.format(vertsintree))

    # initialize mst
    mst = defaultdict(dict)

    def findNextEdge():
        x,y,min_edge_weight = 0, 0, 10 ** 20
        for vert in vertsintree:
            for endpoint in graph[vert]:
                if endpoint not in vertsintree:
                    cur_edge_weight = graph[vert][endpoint]
                    if cur_edge_weight < min_edge_weight:
                        x,y,min_edge_weight = vert, endpoint, cur_edge_weight
        return x,y,min_edge_weight

    def addToMST(begin,end,weight):
        #print('true or false :{}'.format(begin in mst))
        if begin not in mst:
            mst[begin] = {
                end:weight
            }
        else:
            #print('begin {}, end {}, weight {}'.format(begin, end, weight))
            mst[begin][end] = weight

    while vertsnotintree:
        # find minimum edge to add to mst
        v1,v2,edgeweight = findNextEdge()
        print('v1 is: {}, v2 is : {}'.format(v1, v2))
        # add new edge to vertsintree and remove from vertsnotintree
        vertsnotintree.remove(v2)
        vertsintree.add(v2)
        #print('verts NOT in : {}'.format(vertsnotintree))
        #print('verts IN : {}'.format(vertsintree))
        # add edge to mst
        addToMST(v1,v2,edgeweight)
        print('ongoing mst {}'.format( mst ))
    return mst

def findTotalEdgeWeight(tree):
    totalweight = 0
    for k in tree:
        for k2 in tree[k]:
            totalweight += tree[k][k2]
    return totalweight


if __name__ == '__main__':
    graph = readFileIntoGraph(sys.argv[1])
    mst = prim(graph)
    print('final mst: {}'.format(mst))
    print(findTotalEdgeWeight(mst))
