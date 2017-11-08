import sys

def read_file(file):
    """
    open file and read contents line by line.
    add to dictionary that represents
    an adjacency list
    """
    graph = dict()
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

def print_distance(dist):
    """
    utility function to print all u,v paths from
    distance matrix
    """
    n = range(len(dist))
    for u in n:
        for v in n:
            print('u: {} v: {} weight: {}'.format(
                u + 1,
                v + 1,
                dist[u][v] if dist[u][v] != 10 ** 20 else "inf"
                )
            )

def floyd_warshall(graph):
    """
    get shortest distance from all points in a graph.
    return result in 2d matrix.
    """
    vertices = set(
        [x for x in graph]).union(
        [y for x in graph for y in graph[x]]
    )
    n = range(len(vertices))
    # initialize 2d distance matrix to 10 ** 20 for inf or 0 if i == j
    dist = [[10 ** 20 if j != i else 0 for j in n ] for i in n]
    # set minpath equal to infinity
    minpath = 10 ** 20
    # input all edges from adjacency list into distance matrix
    for u in graph:
        for v in graph[u]:
            # adjust indicies for 0 based distance matrix
            u_adj = u - 1
            v_adj = v - 1
            dist[u_adj][v_adj] = graph[u][v]
            if dist[u_adj][v_adj] < minpath: minpath = dist[u_adj][v_adj]
    for k in n:
        for i in n:
            for j in n:
                # check to see if either path is equal to the "infinity" value
                if dist[i][k] == 10 ** 20 or dist[k][j] == 10 ** 20:
                    pass
                elif dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    if  minpath > dist[i][k] + dist[k][j]:
                        minpath = dist[i][k] + dist[k][j]
    # check for negative cycles and return result
    for c in n:
        if dist[c][c] < 0:
            return "this graph has a negative cycle"
    return minpath

if __name__ == '__main__':
    graph = read_file(sys.argv[1])
    result = floyd_warshall(graph)
    print(result)
