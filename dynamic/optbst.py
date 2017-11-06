import sys
import bst

from itertools import permutations

keys = {
  1:.05 ,
  2: .4 ,
  3: .08 ,
  4: .04 ,
  5: .1 ,
  6: .1 ,
  7: .23
}

def create_node_list(keys):
    node_list = [x for x in keys.keys()]
    return node_list

def create_tree(node_list):
    tree = bst.Node(node_list[0])
    for node in node_list[1:]:
        bst.add_node_to_tree(tree, node)
    return tree

def find_weight_of_tree(tree, key):
    weight = 0
    weighted_node_list = bst.traverse(tree)
    for lst in weighted_node_list:
        weight += (key[lst[0]] * lst[1])
    return weight

def find_min_tree(node_list, key):
    min_weight = 10 ** 10
    for lst in permutations(node_list):
        temp_lst = [x for x in lst]
        tree = create_tree(temp_lst)
        weight = find_weight_of_tree(tree, key)
        if weight < min_weight:
            min_weight = weight
    return min_weight

if __name__ == '__main__':
    lst = create_node_list(keys)
    result = find_min_tree(lst, keys)
    print('min tree is {}\n'.format(result))
