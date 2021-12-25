# coding=utf-8
from random import randint
print('按下回车生成激活码')
print('Press enter to generate the activation code')
while True:
    a = input()
    if a == '':
        abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
        ots = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        d = ''
        for z in range(4):
            b = []
            c = randint(2, 5)
            for y in range(c):
                b.append(abc[randint(0, 25)])
            for x in range(5 - c):
                b.append(ots[randint(0, 9)])
            for w in range(5):
                d += b[w]
            d += '-'
        b = []
        c = randint(2, 5)
        for x in range(c):
            b.append(abc[randint(0, 25)])
        for w in range(5 - c):
            b.append(ots[randint(0, 9)])
        for v in range(5):
            d += b[v]
        print(d)
    else:
        if a == 'exit':
            break
