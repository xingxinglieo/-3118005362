from format_num import format_num
from params import MAX
from gcd import reduce_factor
# 测试数字是否符合题目要求
# 生成的题目中计算过程不能产生负数，也就是说算术表达式中如果存在形如e1− e2的子表达式，那么e1≥ e2。
# 生成的题目中如果存在形如e1÷ e2的子表达式，那么其结果应是真分数。


def test_num(num):
    if num == False:
        return False
    num = str(num)
    if num.find('’') > -1:
        if int(num.split('’')[0]) < MAX and test_num(num.split('’')[1]):
            return True
        else:
            return False
    elif num.find('/') == -1:
        if int(num) > MAX:
            return False
        else:
            return True
    else:
        split_num = reduce_factor(num).split('/')
        # formatted_num = format_num(num.split('/')[0], num.split('/')[1])
        if int(split_num[0]) >= int(split_num[1]):
            return test_num(format_num(split_num[0], split_num[1]))
        else:
            return int(split_num[1]) <= MAX

