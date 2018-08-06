#!/usr/local/bin/python3
import sys
import datetime
import time
from lib import init



try:
    input = raw_input
except:
    pass

if len(sys.argv) > 1:
    date = sys.argv[1]
else:
    date = input('日志，请输入日期，xxxx-xx-xx\n文章，请输入日期，xxxx-xx-xx art\n>  ')

runType = 'log'
if len(sys.argv) > 2:
    runType = sys.argv[2]

print(date)

if date == '':
    date = datetime.datetime.now().strftime('%Y-%m-%d')

date = datetime.datetime.strptime(date, '%Y-%m-%d')

# d1 = datetime.datetime(2018, 3, 15)
# print(d1 - date)

# d2 = date + datetime.timedelta(days=1)
# print(d2)

weekDay = date.weekday();
print(weekDay)


content_log = ''
content_log_read = ''
content_log_workout = ''
content_log_skip = ''

for i in range(6, -1, -1):
    
    newDay = date + datetime.timedelta(days = i - weekDay)
    newNum = init.getNumByDate(newDay.strftime('%Y-%m-%d'))
    # print(newNum)
    newWeekDay = i + 1
    if newWeekDay == 8:
        newWeekDay = 1;
    # print(newWeekDay)
    if runType == 'all' or runType == 'art':
        init.makeArt(newNum, newDay, newWeekDay)

    
    content_log = content_log + init.makeLogContent(newDay, newWeekDay)
    if i < 5:
        content_log_read = content_log_read + init.makeLogReadContent(newDay, newWeekDay)
        content_log_skip = content_log_skip + init.makeLogSkipContent(newDay, newWeekDay)
    content_log_workout = content_log_workout + init.makeLogWorkoutContent(newDay, newWeekDay)

if runType == 'all' or runType == 'log':  
    f = open(init.output_path_log, 'w')
    f.write(content_log)
    f.close()

    f = open(init.output_path_log_read, 'w')
    f.write(content_log_read)
    f.close()

    f = open(init.output_path_log_skip, 'w')
    f.write(content_log_skip)
    f.close()

    f = open(init.output_path_log_workout, 'w')
    f.write(content_log_workout)
    f.close()


