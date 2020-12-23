# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from binarytree import tree
from binarytree import Node
from binarytree import  bst
from typing import *
import sys
from collections import namedtuple
MinMax = namedtuple("MinMax", "min level")

mytree = bst()
k=5

print(mytree)

# def getLessThan(k, *vals: MinMax) ->MinMax:
#     max = -1
#     ret = MinMax(-1, -1)
#
#     for val in vals:
#         if val.min <= k and val.level > max:
#             ret=val
#             max = val.min
#     return ret
#
# def getGrtrThan(k, *vals: MinMax)->MinMax:
#     min = sys.maxsize
#     ret = MinMax(-1, sys.maxsize)
#
#     for val in vals:
#         if val.min >= k and val.level < min:
#             ret = val
#             min = val.level
#
#     return ret
#
# #find min value
# def findFloor(node: Node, k, level) ->MinMax:
#     if node is None:
#         return (MinMax(sys.maxsize, -1), MinMax(-1, sys.maxsize))
#
#     (minmaxL, maxMinL) = findFloor(node.left, k, level+1)
#     (minmaxR, maxMinR) = findFloor(node.right, k, level+1)
#     minmaxN = maxMinN = MinMax(node.val, level)
#
#     minmax = getLessThan(k, minmaxN, minmaxL, minmaxR)
#     maxmin = getGrtrThan(k, maxMinL, maxMinR, maxMinN)
#
#     return (minmax, maxmin)

def findFloor2(node: Node, k, level):
    if not node:
        return sys.maxsize

    if node.val <= k:
        return level
    else:
        return findFloor2(node.left, k, level+1)



def findCeil2(node: Node, k, level):
    if not node:
        return -1

    l= findCeil2(node.left, k, level+1)
    r = findCeil2(node.right, k, level+1)

    merge= [l,r]
    if node.val >=k:
        merge.append(level)

    return max(merge)




# min = findFloor(mytree, k, 0)
# print(min)

min2 = findFloor2(mytree, k, 0)
print(min2)

max = findCeil2(mytree, k, 0)
print(max)


