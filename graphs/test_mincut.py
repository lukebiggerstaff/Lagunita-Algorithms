import unittest

import mincut as mc

class TestMinCut(unittest.TestCase):


    def test_can_contract(self):
        testdict = {1:[2,3],2:[1,3],3:[1,2]}
        mc.contract(testdict)
        self.assertTrue(len(testdict) < 3)

