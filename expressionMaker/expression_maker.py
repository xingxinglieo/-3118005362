from random import randint
from gcd import reduce_factor
from infix2prefix import infix2prefix
from tree import prefix2tree
from tree import valueTree
from tree import tree2prefix
from params import MAX
# 生成分数


def decimal_maker():
    # 分母
    denominator = randint(2, MAX)
    # 分子
    numerator = randint(1, denominator - 1)
    # 进行约分
    return reduce_factor(str(numerator) + '/' + str(denominator))


# 生成符合要求的数
def num_maker():
  # random_num用于判定生成数的类型的概率
  # 1-6 生成整数 7-9生成不带整数的真分数 10生成带整数的真分数
    # def n():
    result = 0
    random_num = randint(1, 10)
    if random_num <= 6:
        result = randint(1, MAX)
    elif random_num <= 9:
        result = decimal_maker()
    else:
        result = str(randint(1, MAX-1)) + '’' + str(decimal_maker())
    return str(result)
    # return n

# 生成运算符


def operator_maker():
    # random_num用于判定生成数的类型的概率
    random_num = randint(1, 10)
    if random_num <= 3:
        return '+'
    elif random_num <= 6:
        return '-'
    elif random_num <= 8:
        return '*'
    elif random_num <= 10:
        return '/'


def expression_maker():
    # 确定操作符数量（1-3个）
    # num_maker_MAX = num_maker()
    expression = [num_maker()]
    operator_num = randint(1, 3)
    while(operator_num):
        # expression = expression + ' ' + operator_maker() + ' ' + num_maker_MAX()
        expression.append(operator_maker())
        expression.append(num_maker())
        operator_num -= 1
    return expression

# 给乘号和除号加上括号
# def add_brackets(expression):
#     expression = expression[:]

#     def inner(expression):
#         index = -1
#         for i in range(len(expression)):
#             if expression[i] in ['*', '/']:
#                 index = i
#                 break
#         if index > -1:
#             expression[index-1:index+2] = [expression[index-1:index+2]]
#             return add_brackets(expression)
#         else:
#             def flat(expression):
#                 index = - 1
#                 for i in range(len(expression)):
#                     if isinstance(expression[i], list):
#                         index = i
#                 if index > -1:
#                     expression[index].insert(0, '(')
#                     expression[index].append(')')
#                     expression[index:index+1] = expression[index]
#                     return flat(expression)
#                 else:
#                     return expression
#             return flat(expression)
#     return inner(expression)

class Expression:
    def __init__(self, expression, prefix, tree):
        self.prefix = prefix
        self.tree = tree
        self.expression = expression
        self.expression_add_space = ' '.join(expression)


def expression_producer():
    expression = expression_maker()
    prefix = infix2prefix(expression)
    tree = prefix2tree(prefix)
    valueTree(tree)
    prefix = tree2prefix(tree)
    return Expression(expression, prefix, tree)