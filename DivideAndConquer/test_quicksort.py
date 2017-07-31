import unittest

import quicksort as qs


class TestMergeSort(unittest.TestCase):

    def setUp(self):
        self.lst = [3,4,2,1,5,6,8,7]
        self.sorted_lst = [1,2,3,4,5,6,7,8]

    def test_returns_list(self):
        self.assertIsInstance(qs.quicksort(self.lst, 0, len(self.lst)), list)

    def test_returns_sorted_list_of_even_amount(self):
        self.assertEqual(qs.quicksort(self.lst, 0, len(self.lst)), self.sorted_lst)


if __name__ == '__main__':
    unittest.main()
