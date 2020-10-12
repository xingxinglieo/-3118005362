# 求两整数最大公因数
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# 对分数进行约分
def reduce_factor(factor):
    s = factor.split('/')
    common = gcd(int(s[0]),int(s[1]))
    return str(int(s[0])//common) + '/' + str(int(s[1])//common)