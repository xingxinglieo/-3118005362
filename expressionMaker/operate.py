from gcd import reduce_factor
from test_num import test_num
from format_num import format_num

# 将数字化为分数
# 1 -> 1/1
# 3 -> 3/1
# 1`1/3 -> 4/3
# 1/2 -> 1/2


def handle_num(num):
    if num.find('’') > -1:
        split = num.split('’')
        integer = split[0]
        fraction = split[1]
        # 分子
        numerator = fraction.split('/')[0]
        # 分母
        denominator = fraction.split('/')[1]
        return str(int(integer) * int(denominator) + int(numerator)) + '/' + denominator
    elif num.find('/') > -1:
        return num
    else:
        return num + '/' + '1'

# 对分数进行约分并将数字规范化
# 3/6 -> 1/2
# 4/3 -> 1`1/3
# 9/6 -> 1`1/2


# 两个数字进行计算
# 产生负数返回 False
# 计算过程中除数或者分母为0时返回 False


def operate(left, operator, right):
    if test_num(left) == False or test_num(right) == False:
        return False
    left = handle_num(left)
    right = handle_num(right)
    result = 0
    # 通分且此步不进行约分

    def handle(num1, num2):
        num1 = num1.split('/')
        num2 = num2.split('/')
        denominator = int(num1[1])*int(num2[1])
        numerator1 = int(num1[0])*int(num2[1])
        numerator2 = int(num2[0])*int(num1[1])
        return [[numerator1, numerator2], denominator]
    handled_num = handle(left, right)
    left_numerator = handled_num[0][0]
    right_numerator = handled_num[0][1]
    denominator = handled_num[1]
    if(operator == '+'):
        result = [left_numerator + right_numerator, denominator]
    elif(operator == '-'):
        result = [left_numerator - right_numerator, denominator]
    elif(operator == '*'):
        result = [left_numerator * right_numerator, denominator*denominator]
    elif(operator == '/'):
        result = [left_numerator, right_numerator]
    if(result[0] < 0 or result[1] == 0):
        return False
    result = format_num(result[0], result[1])
    if test_num(result) == False:
        return False
    else:
        return result
