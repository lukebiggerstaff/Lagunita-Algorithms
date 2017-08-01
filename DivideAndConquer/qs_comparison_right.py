import os
import sys


class ComparisonCounter(object):

    def __init__(self):
        self.num_comparisons = 0;

    def quicksort(self, lst, left, right):

        if right - left > 0:
            p = self.partition(lst, left, right)
            self.quicksort(lst, left, (p - 1))
            self.quicksort(lst, (p + 1), right)


    def partition(self, lst, left, right):

        self.num_comparisons += len(lst[left:right])
        pivot = lst[right]
        lst[left], lst[right] = lst[right], lst[left]
        i = left + 1
        for j in range(i, right+1):
            if lst[j] < pivot:
                lst[j], lst[i] = lst[i], lst[j]
                i += 1
        lst[left], lst[i-1] = lst[i-1], lst[left]
        return i - 1

    def count(self, lst):
        self.quicksort(lst, 0, (len(lst) - 1) )
        return self.num_comparisons


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        file_lst = [ int(x) for x in f.read().split('\n') if x ]
        comp_counter = ComparisonCounter()
        result = comp_counter.count(file_lst)
        print(result)
