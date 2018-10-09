# -*- coding:utf-8 -*-
# __author__ = '32830'


f = open('C:/Users/32830/Desktop/daily_summary.txt', 'w+')

def clock_subtraction(clock_minuend, clock_subtrahend):
    seconds = int(clock_minuend.split(':')[2]) - int(clock_subtrahend.split(':')[2])
    minutes = int(clock_minuend.split(':')[1]) - int(clock_subtrahend.split(':')[1])
    if seconds < 0:
        seconds += 60
        minutes -= 1
    if minutes < 0:
        minutes += 60
    print_str = str(minutes)+'分'+str(seconds)+'秒'
    return print_str

def getstr():
    summary_data = {
        '热车': 0,
        '热车完毕': 0,
        '准备起飞': 0,
        '离地': 0,
        '到达预定位置': 0,
        '返航': 0,
        '着陆': 0
    }

    str_time = input("热车时间： ")
    if str_time:
        split_s = str_time.split(' ')
        summary_data['热车'] = split_s[0]+':'+split_s[1]+':'+split_s[2]

    str_time = input("热车完毕时间： ")
    if str_time:
        split_s = str_time.split(' ')
        summary_data['热车完毕'] = split_s[0]+':'+split_s[1]+':'+split_s[2]

    str_time = input("准备起飞时间： ")
    if str_time:
        split_s = str_time.split(' ')
        summary_data['准备起飞'] = split_s[0]+':'+split_s[1]+':'+split_s[2]
        
    str_time = input("离地时间： ")
    if str_time:
        split_s = str_time.split(' ')
        summary_data['离地'] = split_s[0]+':'+split_s[1]+':'+split_s[2]
    
    str_time = input("到达预定位置时间： ")
    if str_time:
        split_s = str_time.split(' ')
        summary_data['到达预定位置'] = split_s[0]+':'+split_s[1]+':'+split_s[2]
    
    str_time = input("返航时间： ")
    if str_time:
        split_s = str_time.split(' ')
        summary_data['返航'] = split_s[0]+':'+split_s[1]+':'+split_s[2]
    
    str_time = input("着陆时间： ")
    if str_time:
        split_s = str_time.split(' ')
        summary_data['着陆'] = split_s[0]+':'+split_s[1]+':'+split_s[2]


    str_location = input('预定位置1/2： ')
    str_oil = input('余油L： ')
    str_ele = input('余电%： ')
    str_duration = clock_subtraction(summary_data['着陆'],summary_data['离地'])
    str_reason = input('返航缘由/中途备注： ')

    # print(summary_data['热车']+'开始热车，'+summary_data['热车完毕']+'热车完毕,'+summary_data['起飞']+'准备起飞，'+summary_data['离地']+'无人机离地，'+summary_data['到达预定位置']+'到达预定位置，'+summary_data['返航']+'开始返航，'+summary_data['着陆']+'无人机着陆，')

    print_str = ''
    if summary_data['热车']:
        print_str = summary_data['热车']+'开始热车，'

    if summary_data['热车完毕']:
        print_str += summary_data['热车完毕']+'热车完毕,'
    else:
        print_str += summary_data['准备起飞']+'热车完毕并准备起飞，'

    print_str += summary_data['离地']+'无人机离地，'

    if str_location == '1':
        print_str += summary_data['到达预定位置']+'到达预定位置1(经度：119.2974025，纬度：31.7733392，高度：35.5m)并悬停，'
    elif str_location == '2':
        print_str += summary_data['到达预定位置']+'到达预定位置2(经度：119.2987012，纬度：31.7729744，高度：35.5m)并悬停，'

    if str_reason:
        print_str += str_reason+'，'

    print_str += summary_data['返航']+'开始返航，'+summary_data['着陆']+'无人机着陆，余油'+str_oil+'L，余电'+str_ele+'%，滞空时间'+str_duration+'。'
    print(print_str)
    return print_str



write_str = getstr()
f.write(write_str)
f.close()
