import unittest
import optbst
from collections import deque

class TestOptBST(unittest.TestCase):


    def create_list_of_tree_nodes(self, tree):
        nodes_arr = list()
        queue = deque()
        queue.append(tree)
        while queue:
            curr_node = queue.popleft()
            nodes_arr.append(curr_node)
            for node in [curr_node.left, curr_node.right]:
                if node != None:
                    queue.append(node)
        return nodes_arr

    def test_create_node_list(self):
        key = {1:1, 2:2, 3:3}
        node_list = optbst.create_node_list(key)
        key_list = [1,2,3]
        node_list.sort()
        self.assertEqual(node_list, key_list)

    def test_create_tree(self):
        node_list = [1,2,3]
        tree = optbst.create_tree(node_list)
        nodes_arr = self.create_list_of_tree_nodes(tree)
        nodes_arr = [x.data for x in nodes_arr]
        nodes_arr.sort()
        self.assertEqual(nodes_arr, node_list)


if __name__ == '__main__':
    unittest.main()
