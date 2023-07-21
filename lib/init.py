#!/usr/local/bin/python3
import datetime
import os
import math

from string import Template

    
startNum = 1841
startNumDate = '2021-02-21'

d1Num = 328
d1Date = '2023-05-08'
d1Cate = '看图说话'

d2Num = 1306
d2Date = '2023-06-27'
d2Cate = '与喵共舞'

d3Num = 407
d3Date = '2023-07-19'
d3Cate = '黄金屋'

d4Num = 371
d4Date = '2023-06-29'
d4Cate = '杂谈'

d5Num = 247
d5Date = '2023-06-30'
d5Cate = '小学'

d6Num = 1307
d6Date = '2023-07-01'
d6Cate = '与喵共舞'

d7Num = 1308
d7Date = '2023-07-02'
d7Cate = '与喵共舞'




file_parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir) + os.path.sep)
tpl_path = file_parent_path + os.path.sep + 'tpl'
tpl_path_art = tpl_path + os.path.sep + 'art.tpl'
tpl_path_log = tpl_path + os.path.sep + 'log'
tpl_path_log_read = tpl_path + os.path.sep + 'log_read.tpl'
tpl_path_log_workout = tpl_path + os.path.sep + 'log_workout'
tpl_path_log_skip = tpl_path + os.path.sep + 'log_skip.tpl'


output_path = file_parent_path + os.path.sep + 'output'
output_path_art = '/Users/zhuxu/Documents/mmjstool/momiaojushi'
output_path_log = output_path + os.path.sep + 'log.md'
output_path_log_workout = output_path + os.path.sep + 'log_workout.md'
output_path_log_read = output_path + os.path.sep + 'log_read.md'
output_path_log_skip = output_path + os.path.sep + 'log_skip.md'

weekDayDict = {
    
    '1': '周一',
    '2': '周二',
    '3': '周三',
    '4': '周四',
    '5': '周五',
    '6': '周六',
    '7': '周日',

}

tplKanTuShuoHua = '\n**拍摄时间：2018.12.17**\n\n**拍摄地点：**\n'
tpl5Slogan = '\n***有的小朋友对我说不想上小学，因为乘法太难了，其实小学里有趣的事可多了，包括乘法在内。***\n'

tplLogVipkid = '\n* vipkid'



def getNumByDate(date):

    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return startNum + (date - datetime.datetime.strptime(startNumDate, '%Y-%m-%d')).days



def makeArt(num, day, weekDay):

    cateTitle = ''
    if weekDay == 1:
        cate = d1Cate
        cateNum = d1Num + int((day - datetime.datetime.strptime(d1Date, '%Y-%m-%d')).days / 7)
    elif weekDay == 2:
        cate = d2Cate
        cateNum = d2Num + int((day - datetime.datetime.strptime(d2Date, '%Y-%m-%d')).days / 7) * 3
    elif weekDay == 3:
        cate = d3Cate
        cateNum = d3Num + int((day - datetime.datetime.strptime(d3Date, '%Y-%m-%d')).days / 7)   
        cateTitle = '《》'
    elif weekDay == 4:

        cate = d4Cate
        cateNum = d4Num + int((day - datetime.datetime.strptime(d4Date, '%Y-%m-%d')).days / 7)
        # if ((day - datetime.datetime.strptime(d4Date, '%Y-%m-%d')).days / 7) % 2 == 0:
        #     cate = d4Cate
        #     cateNum = d4Num + int((day - datetime.datetime.strptime(d4Date, '%Y-%m-%d')).days / 14)
        # else:
        #     cate = d4Cate1
        #     cateNum = d4Num1 + int((day - datetime.datetime.strptime(d4Date1, '%Y-%m-%d')).days / 14)
    elif weekDay == 5:
        cate = d5Cate
        cateNum = d5Num + int((day - datetime.datetime.strptime(d5Date, '%Y-%m-%d')).days / 7)   
    elif weekDay == 6:
        cate = d6Cate
        cateNum = d6Num + int((day - datetime.datetime.strptime(d6Date, '%Y-%m-%d')).days / 7 ) * 3
        cateTitle = '周末活动'
    elif weekDay == 7:
        cate = d7Cate
        cateNum = d7Num + int((day - datetime.datetime.strptime(d7Date, '%Y-%m-%d')).days / 7 ) * 3
        cateTitle = '周末活动'

    name_date = day.strftime('%Y%m%d')
    tpl  = Template('${num}.${cate}${cateNum}~*${cateTitle}')
    title = tpl.substitute(num = num, cate = cate, cateNum = math.floor(cateNum), cateTitle = cateTitle)
    print(title)

    f = open(tpl_path_art)
    tplContent = f.read()
    f.close()
    tpl = Template(tplContent)
    if weekDay == 1:
        # 周一看图说话，添加日期和地点模板
        content = tpl.substitute(num = num, day = day.strftime('%Y.%m.%d'), weekDay = weekDay, tplKanTuShuoHua = tplKanTuShuoHua, tpl5Slogan = '')
    elif weekDay == 5:
        # 周五上小学，加slogan模板
        content = tpl.substitute(num = num, day = day.strftime('%Y.%m.%d'), weekDay = weekDay, tplKanTuShuoHua = '', tpl5Slogan = tpl5Slogan)
    else:
        content = tpl.substitute(num = num, day = day.strftime('%Y.%m.%d'), weekDay = weekDay, tplKanTuShuoHua = '', tpl5Slogan = '')
    # print(content)

    f = open(output_path_art + os.path.sep + title + '.md', 'w')
    f.write(content)
    f.close()

def makeLogContent(day, weekDay):

    f = open(tpl_path_log + str(weekDay) + '.tpl')
    tplContent = f.read()
    f.close()

    tpl = Template(tplContent)
    content = tpl.substitute(day = day.strftime('%Y.%m.%d'), weekDay = weekDayDict[str(weekDay)]) + '\n\n'
    
    return content

def makeLogReadContent(day, weekDay):

    f = open(tpl_path_log_read)
    tplContent = f.read()
    f.close()

    tpl = Template(tplContent)
    content = tpl.substitute(day = day.strftime('%Y.%m.%d'), weekDay = weekDayDict[str(weekDay)]) + '\n\n\n\n'
    
    return content

def makeLogWorkoutContent(day, weekDay):

    f = open(tpl_path_log_workout + str(weekDay) + '.tpl')
    tplContent = f.read()
    f.close()

    tpl = Template(tplContent)
    content = tpl.substitute(day = day.strftime('%Y.%m.%d'), weekDay = weekDayDict[str(weekDay)]) + '\n\n'
    
    return content

def makeLogSkipContent(day, weekDay):

    f = open(tpl_path_log_skip)
    tplContent = f.read()
    f.close()

    tpl = Template(tplContent)
    content = tpl.substitute(day = day.strftime('%Y.%m.%d'), weekDay = weekDayDict[str(weekDay)]) + ''
    
    return content


