import unittest

import mincut as mc

class TestMinCut(unittest.TestCase):


    def test_returns_list_of_edges(self):
        self.assertIsInstance(mc.compute({1:[1,2,3],2:[4,5,6],3:[7,8,9]}), [])

    def test_can_contract(self):
        result = mc.compute({1:[1,2,3],2:[4,5,6],3:[7,8,9]})
        self.assertTrue(len(result) < 3)

