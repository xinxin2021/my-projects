cinema = {'灾难片':'《开学》', '悬疑片':'《假期作业离奇失踪》',
          '恐怖片':'《老师和他那没完成作业的学生》', '青春片':'《匆匆离去的假期》',
          '科幻片':'《学生大战老师》', '苦情片':'《舍不得离开手机》',
          '动作片':'《逃学》', '解放片':'《放假》', '侦探片':'《谁抄了他的作业？》',
          '励志片':'《疯狂补作业》', '搞笑片':'《我当初上学的那些事》',
          '爱情片':'《我与作业的不解之缘》', '战争片':'《学生与老师的课堂大战》'}
keys_list_cinema = list(cinema.keys())
values_list_cinema = list(cinema.values())
print('选择列表：{}'.format(keys_list_cinema))
while True:
    answer = input('请选择种类（每种种类一部电影）：')
    if answer in keys_list_cinema:
        print('{}：{}'.format(answer, values_list_cinema[keys_list_cinema.index(answer)]))
    elif answer == 'exit':
        break
    else:
        print('未找到该分类！')
print('已退出！')
while True:
    pass
