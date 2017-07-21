import os
import sys


class InversionCounter(object):


    def __init__(self):
        self.num_inversions = 0;

    def merge_sort(self, lst):

        sorted_lst = []
        if len(lst) is 1:
            return lst
        half = int(len(lst) / 2)
        first_half = self.merge_sort(lst[:half])
        second_half = self.merge_sort(lst[half:])
        i = 0
        j = 0
        while i < len(first_half) and j < len(second_half):
            if first_half[i] > second_half[j]:
                sorted_lst.append(second_half[j])
                self.num_inversions = self.num_inversions + len(first_half[i:])
                j = j + 1
            else:
                sorted_lst.append(first_half[i])
                i = i + 1
        sorted_lst += first_half[i:]
        sorted_lst += second_half[j:]
        return sorted_lst

    def count_inversions(self, lst):
        self.num_inversions = 0
        self.merge_sort(lst)
        return self.num_inversions

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lst = [ int(x) for x in f.read().split('\n') if x ]
        inv_counter = InversionCounter()
        result = inv_counter.count_inversions(lst)
        print(result)
