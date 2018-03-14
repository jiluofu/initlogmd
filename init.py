#!/usr/local/bin/python3
import sys
import datetime
import time

startNumDate = '2018-03-08'
startNum = 760

def getNumByDate(date):

    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return startNum + (date - datetime.datetime.strptime(startNumDate, '%Y-%m-%d')).days

try:
    input = raw_input
except:
    pass

if len(sys.argv) > 1:
    date = sys.argv[1]
else:
    date = input('请输入日期，xxxx-xx-xx\n>  ')

print(date)

if date == '':
    date = datetime.datetime.now().strftime('%Y-%m-%d')

date = datetime.datetime.strptime(date, '%Y-%m-%d')

# d1 = datetime.datetime(2018, 3, 15)
# print(d1 - date)

# d2 = date + datetime.timedelta(days=1)
# print(d2)

weekDay = date.weekday();



for i in range(0, 8):
    
    newDay = date + datetime.timedelta(days = i - weekDay)
    print(newDay)
    newNum = getNumByDate(newDay.strftime('%Y-%m-%d'))
    print(newNum)
    newWeekDay = i + 1
    if newWeekDay == 8:
        newWeekDay = 1;
    print(newWeekDay)





