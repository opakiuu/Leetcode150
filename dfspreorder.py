import math


class STreeNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def printNodes(nodes):
    for i in range(len(nodes)):
        leftStr = "None"
        if nodes[i].left is not None:
            leftStr = str(nodes[i].left.val)
        rightStr = "None"
        if nodes[i].right is not None:
            rightStr = str(nodes[i].right.val)
        print("%d-left %s right %s " % (nodes[i].val, leftStr, rightStr))


def PreOrder(nodes, startIdx, endIdx, i):  # free modify the interface.

    # vals = [8, 5, 3, 2, 9, 1]
    # HW0127
    n = math.ceil(math.log2(len(nodes) + 1) - 1)
    # exception
    if i > endIdx:
        return nodes
    elif startIdx == n or (
        nodes[startIdx].left != None and nodes[startIdx].right != None
    ):
        return PreOrder(nodes, startIdx - 1, endIdx, i)

    # general
    if nodes[startIdx].left == None:
        nodes[startIdx].left = nodes[i]
    else:
        nodes[startIdx].right = nodes[i]

    if (
        startIdx + 1 < len(nodes)
        and nodes[startIdx + 1].left != None
        and nodes[startIdx + 1].right != None
    ):
        return PreOrder(nodes, i, endIdx, i + 1)
    elif i + 1 == endIdx:
        return PreOrder(nodes, startIdx, endIdx, i + 1)
    else:
        return PreOrder(nodes, startIdx + 1, endIdx, i + 1)


vals = [8, 5, 3, 2, 9, 1]
nodes = [STreeNode(val) for val in vals]
printNodes(nodes)
print("\n")

root = PreOrder(nodes, 0, len(nodes) - 1, 1)
printNodes(root)
