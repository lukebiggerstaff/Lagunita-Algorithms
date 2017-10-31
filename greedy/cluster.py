import sys
import unionfind as uf


def read_file_into_sorted_edgelist(file):
    edgelist = list()
    with open(file) as f:
        for line in f:
            line_lst = [int(x) for x in line.strip().split()]
            edgelist.append(line_lst)
    edgelist.sort(key=lambda x: x[2])
    return edgelist

def create_node_list(edgelist):
    nodes = set()
    for row in edgelist:
        nodes.add(row[0])
        nodes.add(row[1])
    return nodes

def create_unionfind_ds(edgelist):
    nodes = create_node_list(edgelist)
    UFDS = uf.UnionFind(nodes)
    return UFDS

def join_nodes_remove_leader(unionfind, leaderboard, node1, node2):
    node1leader = unionfind.find(node1)
    node2leader = unionfind.find(node2)
    leader_to_remove = unionfind.union(node1,node2)
    leaderboard.remove(leader_to_remove)

def check_amount_of_clusters(leaderboard):
    return len(leaderboard) <= 4

def cluster(edgelist, UFDS, leaderboard):
    for edge in edgelist:
        if UFDS.find(edge[0]) != UFDS.find(edge[1]):
            if check_amount_of_clusters(leaderboard):
                return edge[2]
            join_nodes_remove_leader(UFDS, leaderboard, edge[0], edge[1])


if __name__ == '__main__':
    edgelist = read_file_into_sorted_edgelist(sys.argv[1])
    UnionFind = create_unionfind_ds(edgelist)
    leaderboard = create_node_list(edgelist)
    print(cluster(edgelist, UnionFind, leaderboard))
