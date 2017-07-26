import os
import sys


def divide_lists(lst):

    if len(lst) is 1:
        return lst
    half = int(len(lst) / 2)
    left = divide_lists(lst[:half])
    right = divide_lists(lst[half:])
    return compare(left, right)

def compare(left, right):
    sorted_lst = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_lst.append(right[j])
            j = j + 1
        else:
            sorted_lst.append(left[i])
            i = i + 1
    sorted_lst += left[i:]
    sorted_lst += right[j:]
    return sorted_lst[:2]

def find_second_largest(lst):
    result = divide_lists(lst)
    return result[1]


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lst = [ int(x) for x in f.read().split('\n') if x ]
        result = find_second_largest(lst)
        print(result)
