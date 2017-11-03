from collections import deque


class Node:

    def __init__(self,data):
        self.data = data
        self.height = 1
        self.parent = None
        self.left = None
        self.right = None

    def __str__(self):
        return ''.format(self.data)


def add_node_to_tree(head, node):
    if node < head.data:
        if head.left == None:
            head.left = Node(node)
            head.left.parent = head
            head.left.height = head.height + 1
            return
        add_node_to_tree(head.left, node)
    if node > head.data:
        if head.right == None:
            head.right = Node(node)
            head.right.parent = head
            head.right.height = head.height + 1
            return
        add_node_to_tree(head.right, node)

def print_nodes(tree, queue=None):
    if tree == None: return
    if queue == None: queue = deque()
    print('{}'.format(tree.data), end=' ')
    [queue.append(node) for node in [tree.left, tree.right] if node]
    while queue:
        print_nodes(queue.popleft(), queue)

def traverse(tree, queue=None, node_list=None):
    if tree == None: return
    if queue == None: queue = deque()
    if node_list == None: node_list = list()
    node_list.append([tree.data, tree.height])
    [queue.append(node) for node in [tree.left, tree.right] if node]
    if queue:
        traverse(queue.popleft(), queue, node_list)
    return node_list
