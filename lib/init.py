#!/usr/local/bin/python3
import datetime
import os
import math

from string import Template

    
startNum = 760
startNumDate = '2018-03-08'

d1Num = 91
d1Date = '2018-03-19'
d1Cate = '看图说话'

d2Num = 382
d2Date = '2018-03-20'
d2Cate = '与喵共舞'

d3Num = 58
d3Date = '2018-03-21'
d3Cate = '读书'

d4Num = 84
d4Date = '2018-03-22'
d4Cate = '朝花夕拾'
d4Num1 = 36
d4Date1 = '2018-03-15'
d4Cate1 = '读历史'

d5Num = 1
d5Date = '2018-03-23'
d5Cate = '小学'

d6Num = 383
d6Date = '2018-03-24'
d6Cate = '与喵共舞'

d7Num = 384
d7Date = '2018-03-25'
d7Cate = '与喵共舞'




file_parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir) + os.path.sep)
tpl_path = file_parent_path + os.path.sep + 'tpl'
tpl_path_art = tpl_path + os.path.sep + 'art.tpl'
tpl_path_log = tpl_path + os.path.sep + 'log.tpl'
tpl_path_log_read = tpl_path + os.path.sep + 'log_read.tpl'
tpl_path_log_workout = tpl_path + os.path.sep + 'log_workout'


output_path = file_parent_path + os.path.sep + 'output'
output_path_art = output_path + os.path.sep + 'art'
output_path_log = output_path + os.path.sep + 'log.md'
output_path_log_workout = output_path + os.path.sep + 'log_workout.md'
output_path_log_read = output_path + os.path.sep + 'log_read.md'

weekDayDict = {
    
    '1': '周一',
    '2': '周二',
    '3': '周三',
    '4': '周四',
    '5': '周五',
    '6': '周六',
    '7': '周日',

}



def getNumByDate(date):

    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return startNum + (date - datetime.datetime.strptime(startNumDate, '%Y-%m-%d')).days



def makeArt(num, day, weekDay):

    cateTitle = ''
    if weekDay == 1:
        cate = d1Cate
        cateNum = d1Num + (day - datetime.datetime.strptime(d1Date, '%Y-%m-%d')).days / 7
    elif weekDay == 2:
        cate = d2Cate
        cateNum = d2Num + ((day - datetime.datetime.strptime(d2Date, '%Y-%m-%d')).days / 7) * 3
    elif weekDay == 3:
        cate = d3Cate
        cateNum = d3Num + (day - datetime.datetime.strptime(d3Date, '%Y-%m-%d')).days / 7   
        cateTitle = '《》'
    elif weekDay == 4:

        if ((day - datetime.datetime.strptime(d4Date, '%Y-%m-%d')).days / 7) % 2 == 0:
            cate = d4Cate
            cateNum = d4Num + (day - datetime.datetime.strptime(d4Date, '%Y-%m-%d')).days / 14
        else:
            cate = d4Cate1
            cateNum = d4Num1 + (day - datetime.datetime.strptime(d4Date1, '%Y-%m-%d')).days / 14
    elif weekDay == 5:
        cate = d5Cate
        cateNum = d5Num + (day - datetime.datetime.strptime(d5Date, '%Y-%m-%d')).days / 7   
    elif weekDay == 6:
        cate = d6Cate
        cateNum = d6Num + ((day - datetime.datetime.strptime(d6Date, '%Y-%m-%d')).days / 7 ) * 3
        cateTitle = '周末活动'
    elif weekDay == 7:
        cate = d7Cate
        cateNum = d7Num + ((day - datetime.datetime.strptime(d7Date, '%Y-%m-%d')).days / 7 ) * 3
        cateTitle = '周末活动'

    tpl  = Template('${num}.${cate}${cateNum}~${cateTitle}')
    title = tpl.substitute(num = num, cate = cate, cateNum = math.floor(cateNum), cateTitle = cateTitle)
    print(title)

    f = open(tpl_path_art)
    tplContent = f.read()
    f.close()
    tpl = Template(tplContent)
    content = tpl.substitute(num = num, day = day.strftime('%Y.%m.%d'), weekDay = weekDay)
    # print(content)

    f = open(output_path_art + os.path.sep + title + '.md', 'w')
    f.write(content)
    f.close()

def makeLogContent(day, weekDay):

    f = open(tpl_path_log)
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


