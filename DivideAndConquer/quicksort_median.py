import os
import sys


def quicksort(lst, left, right):

    if right - left > 0:
        p = partition(lst, left, right)
        quicksort(lst, left, (p - 1))
        quicksort(lst, (p + 1), right)


def partition(lst, left, right):

    pivot = lst[left]
    i = left + 1
    for j in range(i, right+1):
        if lst[j] < pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[left], lst[i-1] = lst[i-1], lst[left]
    return i - 1


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        file_lst = [ int(x) for x in f.read().split('\n') if x ]
        quicksort(file_lst, 0, len(file_lst) - 1)
        print('here is the final list: {}\n'.format(
            file_lst
            )
        )
