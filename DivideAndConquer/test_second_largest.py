import unittest

import second_largest as second


class TestCounter(unittest.TestCase):


    def test_returns_int(self):
        result = second.find_second_largest([3,4,2,1])
        self.assertIsInstance(result, int)


    def test_returns_second_largest_num(self):
        result = second.find_second_largest([3,4,2,1])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
