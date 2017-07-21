from unittest import TestCase
import unittest

import merge_sort as Merge


class TestMergeSort(TestCase):


    def test_returns_list(self):
        self.assertIsInstance(Merge.merge_sort([1]), list)

    def test_returns_sorted_list_of_even_amount(self):
        result = Merge.merge_sort([4,3,2,1])
        self.assertEqual(result, [1,2,3,4])

    def test_returns_sorted_list_of_odd_amount(self):
        newresult = Merge.merge_sort([4,3,2,1,8])
        self.assertEqual(newresult, [1,2,3,4,8])

    def test_returns_sorted_list_of_letters(self):
        result = Merge.merge_sort(['a', 'b', 'e', 'z', 'k', 'l'])
        self.assertEqual(result, ['a', 'b', 'e', 'k', 'l', 'z'])


if __name__ == '__main__':
    unittest.main()
