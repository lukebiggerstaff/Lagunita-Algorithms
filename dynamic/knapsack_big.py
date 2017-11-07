import sys

def read_file(file):
    item_list = []
    with open(file) as f:
        for line in f:
            line_lst = [int(x) for x in line.split(' ')]
            item_list.append(line_lst)
    return item_list

def return_max_value_knapsack(items, weight):
    n = len(items)
    w = weight + 1
    a = [0 for i in range(w)]
    for i in range(1, n):
        temp = []
        for j in range(w):
            ci_w = items[i][1]
            ci_v = items[i][0]
            pv_at_w = a[j]
            cv_w_item = a[j-ci_w] + ci_v if ci_w <= j else 0
            max_value = max(pv_at_w,cv_w_item)
            temp.append(max_value)
        a = list(temp)
    return a[w-1]


if __name__ == '__main__':
    items = read_file(sys.argv[1])
    result = return_max_value_knapsack(items, items[0][0])
    print(result)

