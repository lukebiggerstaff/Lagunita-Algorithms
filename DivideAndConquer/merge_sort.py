import os
import sys

def merge_sort(lst):
    ''' merge sort takes a list and divides it in two
    halves and then compares the halves together until
    the list is returned sorted.
    '''
    sorted_lst = []
    if len(lst) is 1:
        return lst
    half = int(len(lst) / 2)
    first_half = merge_sort(lst[:half])
    second_half = merge_sort(lst[half:])
    i = 0
    j = 0
    while i < len(first_half) and j < len(second_half):
        if first_half[i] > second_half[j]:
            sorted_lst.append(second_half[j])
            j = j + 1
        else:
            sorted_lst.append(first_half[i])
            i = i + 1
    sorted_lst += first_half[i:]
    sorted_lst += second_half[j:]
    return sorted_lst

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        lst = [ int(x) for x in f.read().split('\n') if x ]
        result = merge_sort(lst)
        print(result)
