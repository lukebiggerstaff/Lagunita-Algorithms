import os
import sys


def quicksort(lst, left, right):

    if right - left < 2:
        return
    pivot = lst[left]
    i = left + 1
    for j in range(i, right):
        if lst[j] < pivot:
            lst[j], lst[i] = lst[i], lst[j]
            i += 1
    lst[left], lst[i-1] = lst[i-1], lst[left]
    quicksort(lst, left, i - 2)
    quicksort(lst, i, right)


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        file_lst = [ int(x) for x in f.read().split('\n') if x ]
        quicksort(file_lst, 0, len(file_lst))
        print(file_lst)
