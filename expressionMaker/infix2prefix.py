def infix2prefix(str_list):
    str_list = str_list[:]
    s1 = []
    s2 = []
    order_dic = {'+': 0, '-': 0, '*': 1, '/': 1}

    def opOrder(s):
        # 如果S1为空，或栈顶运算符为右括号“)”，则直接将此运算符入栈
        if len(s1) == 0 or s1[-1] == ')':
            s1.append(s)
        # 否则，若优先级比栈顶运算符的较高或相等，也将运算符压入S1；
        elif order_dic[s] - order_dic[s1[-1]] >= 0:
            s1.append(s)
        # 否则，将S1栈顶的运算符弹出并压入到S2中，再次转到函数相比较；
        else:
            s2.append(s1.pop())
            opOrder(s)
    while len(str_list):
        s = str_list.pop()
        if s in ['+', '-', '*', '/']:
            opOrder(s)
        # 如果是右括号“)”，则直接压入S1；
        elif s == ')':
            s1.append(s)
        # 如果是左括号“(”，则依次弹出S1栈顶的运算符，并压入S2，直到遇到右括号为止
        # 此时将这一对括号丢弃
        elif s == '(':
            while True:
                s = s1.pop()
                if s == ')':
                    break
                else:
                    s2.append(s)
        # 遇到操作数时，将其压入S2；
        else:
            s2.append(s)
    s2.reverse()
    prefix = s1 + s2
    return prefix

# s = infix2prefix(['A', '-', 'B', '/', 'C', '-', 'D'])
# print(s)
