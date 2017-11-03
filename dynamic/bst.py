from collections import deque


class Node:

    def __init__(self,data):
        self.data = data
        self.height = 1
        self.parent = None
        self.left = None
        self.right = None

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

def traverse(tree, queue=deque(), node_list=list()):
    if tree == None:
        return
    node_list.append([tree.data, tree.height])
    [queue.append(node) for node in [tree.left, tree.right] if node]
    if queue:
        traverse(queue.popleft(), queue, node_list)
    return node_list
