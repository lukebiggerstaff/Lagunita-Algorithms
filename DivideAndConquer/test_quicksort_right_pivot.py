import unittest
import random

import quicksort_right as qs


class TestQuicksort(unittest.TestCase):

    def setUp(self):
        self.random_lst = [random.randint(0,10000) for x in range(0,random.randrange(start=0,stop=50))]

    def is_list_sorted(self,lst,a=0,b=1):
        if b >= len(lst): return True
        if lst[b] < lst[a]: return False
        return self.is_list_sorted(lst,a=a+1,b=b+1)

    def test_returns_sorted_list_of_random_integers(self):
        print(self.random_lst)
        qs.quicksort(self.random_lst, 0, (len(self.random_lst) - 1) )
        print(self.random_lst)
        self.assertTrue(self.is_list_sorted(self.random_lst))


if __name__ == '__main__':
    unittest.main()
