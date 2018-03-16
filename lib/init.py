#!/usr/local/bin/python3
import datetime
import os

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
output_path = file_parent_path + os.path.sep + 'output'
output_path_art = output_path + os.path.sep + 'art'



def getNumByDate(date):

    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return startNum + (date - datetime.datetime.strptime(startNumDate, '%Y-%m-%d')).days



def makeArt(num, day, weekDay):

    f = open(tpl_path_art)
    tplContent = f.read()
    f.close()

    title = str(num) + '_' + day.strftime('%Y%m%d') + '_xx~xx'
    print(title)

    if weekDay == 4:
        print(day)
        print((day - datetime.datetime.strptime(d4Date, '%Y-%m-%d')).days / 7)

    tpl = Template(tplContent)
    content = tpl.substitute(num = num, day = day.strftime('%Y.%m.%d'), weekDay = weekDay)
    # print(content)

    # f = open(output_path_art + os.path.sep + title + '.md', 'w')
    # f.write(content)
    # f.close()


