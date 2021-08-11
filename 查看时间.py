import time
print('按回车即可查看当前时间')
while 1:
    answer = input()
    now = time.localtime(time.time())
    now = time.strftime('%Y-%m-%d %H:%M:%S',now)
    print('当前时间：{}'.format(now))
