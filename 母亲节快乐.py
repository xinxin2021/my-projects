import time
from random import randint
for i in range(1,200):
    if i % 7 == 0:
        print(randint(1,150) * ' ' + '母亲节快乐')
    elif i % 3 == 0:
        print(randint(1,150) * ' ' + '妈妈我爱你')
    elif i % 11 == 0:
        print(randint(1,150) * ' ' + '妈妈辛苦了')
    elif i % 5 == 0:
        print(randint(1,150) * ' ' + 'I love you')
    elif i % 2 == 0:
        print(randint(1,150) * ' ' + '♥ ♥ ♥ ♥ ♥')
    else:
        print(randint(1,150) * ' ' + '* * * * *')
    time.sleep(0.1)
