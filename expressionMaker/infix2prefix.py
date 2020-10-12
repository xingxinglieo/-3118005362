# 判断运算符的优先级
def opOrder(op1, op2):
    order_dic = {'*':4,'/':4,'+':3,'-':3}
    if op1 == '(' or op2 == '(':
        return False
    elif op2 == ')':
        return True
    else:
        if order_dic[op1] < order_dic[op2]:
            return False
        else:
            return True

# 中缀表达式转化为前缀表达式
def infix2prefix(str_list):
    prefix = []
    stack = []
    string_tmp = []
    for s in str_list[::-1]:
        if s == '(':
            string_tmp.append(')')
        elif s == ')':
            string_tmp.append('(')
        else:
            string_tmp.append(s)
    for s in string_tmp:
        if(s in ['+', '-', '*', '/','(',')']):
            while len(stack) and opOrder(stack[-1], s):
                op = stack.pop()
                prefix.insert(0, op)
            if len(stack) == 0 or s != ')':
                stack.append(s)
            else:
                stack.pop()
        else:
            prefix.insert(0, s)
    if len(stack):
        prefix = stack + prefix
    return prefix
