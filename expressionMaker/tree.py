from operate import operate


class Node:
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None
        if value in ['+', '-', '*', '/']:
            self.result = None
        else:
            self.result = value

# 将前缀表达式转化为二叉树


def prefix2tree(expression):
    expression = expression[:]
    expression.reverse()

    def traverse():
        if len(expression) > 0:
            value = expression.pop()
            node = Node(value)
            if value in ['+', '-', '*', '/']:
                node.lchild = traverse()
                node.rchild = traverse()
            return node
    return traverse()

# 对树每一个节点进行计算并将树按照一定规则进行重排序
# 规则: 左节点的计算值小于右节点的计算值


def valueTree(tree):
    if tree == None:
        return
    # 已经有结果直接退出
    if tree.result != None:
        return
    valueTree(tree.lchild)
    valueTree(tree.rchild)
    if tree.value in ['+', '-', '*', '/']:
        tree.result = operate(tree.lchild.result,
                              tree.value, tree.rchild.result)
        # 加号和乘号重排序
        if tree.value in ['+',  '*']:
            if tree.rchild.result != False and tree.lchild.result != False:

                if operate(tree.rchild.result, '-', tree.lchild.result) == False:
                    temp = tree.lchild
                    tree.lchild = tree.rchild
                    tree.rchild = temp


def tree2prefix(tree):
    prefix = []

    def traverse(tree):
        if tree == None:
            return
        prefix.append(tree.value)
        traverse(tree.lchild)
        traverse(tree.rchild)
    traverse(tree)
    return prefix
