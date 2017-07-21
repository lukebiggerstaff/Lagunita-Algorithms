from unittest import TestCase
import unittest

import inversion_counter as IC


class TestInversionCounter(TestCase):

    def setUp(self):
        self.inv_counter = IC.InversionCounter()

    def test_returns_int(self):
        self.inv_counter.merge_sort([1])
        self.assertEqual(self.inv_counter.num_inversions, 0)

    def test_returns_zero_inversions_correctly(self):
        self.inv_counter.merge_sort([1,2,3])
        self.assertEqual(self.inv_counter.num_inversions, 0)

    def test_returns_one_inversion_correctly(self):
        self.inv_counter.merge_sort([1,3,2])
        self.assertEqual(self.inv_counter.num_inversions, 1)

    def test_returns_two_inversions_correctly(self):
        self.inv_counter.merge_sort([3,1,2])
        self.assertEqual(self.inv_counter.num_inversions, 2)

    def test_returns_three_inversions_correctly(self):
        self.inv_counter.merge_sort([3,2,1])
        self.assertEqual(self.inv_counter.num_inversions, 3)

    def test_returns_zero_inversions_with_all_equal(self):
        self.inv_counter.merge_sort([8,8,8])
        self.assertEqual(self.inv_counter.num_inversions, 0)

    def test_can_return_split_inversions_correctly(self):
        self.inv_counter.count_inversions([1,3,5,2,4,6])
        self.assertEqual(self.inv_counter.num_inversions, 3)


if __name__ == '__main__':
    unittest.main()
