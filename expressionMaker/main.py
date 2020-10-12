# def main:
from expression_maker import expression_producer
from params import expression_num

def main():
    collect = []
    i = 0
    while i < 8:
        collect.append([])
        i += 1
    collectNum = 0
    while collectNum < expression_num:
        e = expression_producer()
        no_repeat = len(list(filter(lambda c: c.expression_add_space ==
                                    e.expression_add_space, collect[len(e.expression)]))) == 0
        if e.tree.result != False and no_repeat:
            collect[len(e.expression)].append(e)
            collectNum += 1
    resuslt = []
    for c in collect :
      resuslt.extend(c)
    text = ''
    for i in range(len(resuslt)):
      text += (str(i+1) + '、 ' + resuslt[i].expression_add_space + '\n')
    f = open('Exercises.txt','w')
    f.write(text)
    f.close()
main()
