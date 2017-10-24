class UnionNode:
    """
    a node of the union find data structure, stores its
    identity, leader, and rank.
    """

    def __init__(self, vertex, leader):
        self.identity = vertex
        self.leader = leader
        self.rank = 1

    def set_leader(self, newleader):
        self.leader = newleader

    def get_leader(self):
        return self.leader

    def get_identity(self):
        return self.identity

    def get_rank(self):
        return self.rank

    def change_rank(self, rank):
        self.rank += rank

    def __str__(self):
        return 'identity: {} and leader: {}'.format(
            self.identity,
            self.leader
        )

class UnionFind:
    """
    Union Find data structure
    supports Find() and Union()
    """

    def __init__(self, nodelist):
        self.storage = self._create_UFDS(nodelist)

    def _create_UFDS(self, lst):
        nodedict = {}
        for node in lst:
            nodedict[node] = UnionNode(node, node)
        return nodedict

    def find(self, vertex):
        if (self.storage[vertex].get_leader()
            == self.storage[vertex].get_identity()):
            return self.storage[vertex].get_identity()
        return self.find(self.storage[vertex].get_leader())

    def union(self, vertex1, vertex2):
        leader1 = self.storage[vertex1].get_leader()
        leader2 = self.storage[vertex2].get_leader()
        if self.storage[leader1].get_rank() > self.storage[leader2].get_rank():
            self.storage[leader2].set_leader(leader1)
            self.storage[leader1].change_rank(self.storage[leader2].get_rank())
        else:
            self.storage[leader1].set_leader(leader2)
            self.storage[leader2].change_rank(self.storage[leader1].get_rank())

    def __str__(self):
        print('UFDS has the following nodes and leaders\n{')
        for node in self.storage:
            print(self.storage[node])
        return '}'
