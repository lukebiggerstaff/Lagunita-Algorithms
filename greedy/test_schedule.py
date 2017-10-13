import unittest
import schedule as S


class TestScheduler(unittest.TestCase):


    def test_can_sort_different_lengths(self):
        ex1 = [[1,1], [1,3], [1,2]]
        correct = [[1,1], [1,2], [1,3]]
        S.schedule_jobs(ex1)
        self.assertEqual(ex1, correct)

    def test_can_sort_different_weights(self):
        ex1 = [[1,1], [3,1], [2,1]]
        correct = [[3,1], [2,1], [1,1]]
        S.schedule_jobs(ex1)
        self.assertEqual(ex1, correct)

    def test_can_find_weight(self):
        ex1 = [[1,1], [1,2], [1,3]]
        S.schedule_jobs(ex1)
        result = S.find_weight(ex1)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
