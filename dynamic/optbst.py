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
    print('wnl is {} '.format(weighted_node_list),end=' ')
    for lst in weighted_node_list:
        weight += (key[lst[0]] * lst[1])
    return weight

def find_min_tree(node_list, key):
    print('##begin find_min_tree##\n')
    min_weight = 10 ** 10
    for lst in permutations(node_list):
        temp_lst = [x for x in lst]
        tree = create_tree(temp_lst)
        weight = find_weight_of_tree(tree, key)
        print('weight {}'.format(weight))
        if weight < min_weight:
            min_weight = weight
            retree = tree
    print('##end find_min_tree##\n')
    return min_weight, retree

if __name__ == '__main__':
    lst = create_node_list(keys)
    result,resultree = find_min_tree(lst, keys)
    print('min tree is {}\n'.format(result))
    print('order of list {}'.format(resultree))
