#!/user/bin/env python
# -*- coding:utf-8 -*-
# Author: Juntao YU

import random

'''\ 033 [显示方式;字体色;背景色m ...... [\ 033 [0m]'''

content = ('看小说','弹琴','看文献','睡觉','看漫画','举铁','洗衣服','拖地')


while True:
    print('\033[34;1m Hi~ o(*￣▽￣*)ブ！这里是随机摸鱼酱 \033[0m'.center(50, '-'))
    time_moyu = input('接下来你有多少分钟可以摸鱼？\033[4;30;47m请输入0-360间的整数：\033[0m')
    if time_moyu.strip().isdigit():
        time_moyu_int = int(time_moyu)
        while True:
            if 0<= time_moyu_int <=360 :
                print('活动选项：'+'\033[34;1m %s \033[0m'%str(content))
                choice_num = input('希望开展几项活动？\033[34;1m最多8项，如希望随机安排请输入0：\033[0m')
                if choice_num.strip().isdigit():
                    choice_num_int = int(choice_num)
                    if 0<= choice_num_int <=8:
                        if choice_num_int == 0:
                            choice_num_int = random.randint(1,8)
                        choice_item = random.sample(content,choice_num_int) # 随机项目选择完成
                        # 开始随机分配时间
                        choice_time = []
                        stick = [0] + random.sample(range(1, time_moyu_int), choice_num_int - 1) + [time_moyu_int]
                        stick.sort()
                        for i in range(len(stick) - 1):
                            choice_time.append(stick[i + 1] - stick[i]) # 随机时间选择完成
                        choice_combine = dict(zip(choice_item,choice_time)) # 合并项目和时间
                        print('\033[34;1m Hi~ 今天的摸鱼项目 \033[0m'.center(50, '-'))
                        for key,value in choice_combine.items():
                            print('{}：{} min'.format(key,value))
                        choice = input('是否需要重新选择？y/n')
                        if choice != 'y':
                            exit()
                        break
                    else:
                        print('\033[3;31m项目数量超过预期！请重新选择\033[0m')
                else:
                    print('\033[3;31m输入的是啥？摸鱼酱不认识，请重新输入_(:зゝ∠)_\033[0m')
            else:
                print('\033[3;31m时间太长，摸鱼酱无法计算，请重新输入\033[0m')
                break
    else:
        print('\033[3;31m输入的是啥？摸鱼酱不认识，请重新输入_(:зゝ∠)_\033[0m')
