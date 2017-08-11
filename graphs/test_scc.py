import unittest
import scc

from collections import defaultdict

class TestSCC(unittest.TestCase):

    def dictionaries_are_equal(self, d1, d2):
        for key in d1.keys() & d2.keys():
            value1 = d1[key]
            value2 = d2[key]
            if value1 != value2:
                return False
        return True

    def test_can_reverse_graph(self):
        graph = defaultdict(list)
        graph['a'] += 'b'
        graph['b'] += 'c'
        graph['c'] += 'd'
        revgraph = scc.graph_reverse(graph)
        self.assertFalse(self.dictionaries_are_equal(graph, revgraph))
        revgraph = scc.graph_reverse(revgraph)
        self.assertTrue(self.dictionaries_are_equal(graph, revgraph))

    def test_can_return_ordered_stack(self):
        pass
