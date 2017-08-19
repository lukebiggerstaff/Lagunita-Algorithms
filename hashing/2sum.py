import sys

from collections import defaultdict

def find_2_sum(numset):
    values_left = 0
    resultset = set()
    for num in numset:
        for total in range(-10000,10001):
            if (total - num) in numset:
                if (total - num) != num:
                    resultset.add(total)
                elif (total - num) == num and num_set[num] > 1:
                    resultset.add(total)
        values_left += 1
        print(f'{len(numset) - values_left} values are remaining')
    return resultset


if __name__ == '__main__':
    num_set = defaultdict(None)
    with open(sys.argv[1]) as f:
        for line in f:
            num = int(line)
            if num not in num_set:
                num_set[num] = 1
            else:
                num_set[num] += 1
    print(f'Created num set and starting algorithm now.')
    results = find_2_sum(num_set)
    print(f'Number of t values are {len(results)} \n')

