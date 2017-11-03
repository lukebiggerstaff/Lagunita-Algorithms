import unittest
import bst


class TestBinarySearchTree(unittest.TestCase):


    def test_create_Node(self):
        test_node = bst.Node(5)
        test_node1 = bst.Node(500)
        self.assertEqual("<class 'bst.Node'>", str( type(test_node1) ))
        self.assertEqual("<class 'bst.Node'>", str( type(test_node) ))
        self.assertEqual(test_node.data, 5)
        self.assertEqual(test_node1.data, 500)


    def test_add_Node_to_Node(self):
        test_head = bst.Node(5)
        bst.add_node_to_tree(test_head, 4)
        bst.add_node_to_tree(test_head, 6)
        self.assertEqual(test_head.data, 5)
        self.assertEqual(test_head.left.data, 4)
        self.assertEqual(test_head.right.data, 6)

if __name__ =='__main__':
    unittest.main()
