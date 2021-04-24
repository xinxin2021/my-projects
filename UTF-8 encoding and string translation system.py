# coding=utf-8
from time import sleep
a=0
b=0
hycy=['Welcome ','to ','UTF-8 ','encoding ','and ','string ','translation ','system']
i=1
for i in range(len(hycy)):
    print(hycy[i],end='')
    sleep(0.5)
print('!',end='')
while 1:
    while 1:
        print('\nPlease select:\nA.UTF-8 encoding to string\nB.String to UTF-8 encoding')
        a=input()
        if not a in ['A','a','B','b']:
            print('Please enter the correct option!')
        else:
            break
    if a in ['a','A']:
        while 1:
            print('Please enter UTF-8 code(press enter to exit):')
            a=input()
            if a != '':
                while 1:
                    try:
                        int(a)
                    except ValueError:
                        print('Please input the correct UTF-8 code!')
                        break
                    else:
                        try:
                            chr(int(a))
                        except:
                            print('Please input the correct UTF-8 code!')
                            break
                        else:
                            print(chr(int(a)))
                            break
            else:
                break
    else:
        while 1:
            print('Please enter a string(press enter to exit):')
            while 1:
                a=input()
                if len(a) > 1:
                    print('At present, the system only supports a word translation!')
                else:
                    break
            if a != '':
                print(ord(a))
            else:
                break
