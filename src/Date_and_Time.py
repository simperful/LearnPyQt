# -*- coding:utf-8 -*-
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

##################################################################
# QDate and QDateTime [http://zetcode.com/gui/pyqt5/datetime/]
##################################################################

now = QDate.currentDate()
print('0 ',now.toString(Qt.ISODate))
print('1 ',now.toString(Qt.DefaultLocaleLongDate))

datetime = QDateTime.currentDateTime()
print('2  Local datetime: ', datetime.toString(Qt.ISODate))
print('3  Universal datetime: ', datetime.toUTC().toString(Qt.ISODate))
print('4  The Offset from UTC is: {0} seconds'.format(datetime.offsetFromUtc()))

time = QTime.currentTime()
print('5 ', time.toString(Qt.DefaultLocaleLongDate))


## numbers of days
d = QDate(1945, 8, 15)

print('6  Days in month: {0}' .format(d.daysInMonth()))
print('7  Days in year: {0}' .format(d.daysInYear()))


## Difference in days
my_birth = QDate(1994, 10, 17)
day_exam = QDate(2018, 12, 22)
days_passed = my_birth.daysTo(now)
days_until = now.daysTo(day_exam)
print("8  {0} days has passed since my birth" .format(days_passed))
print('9  {0} days until the final exam' .format(days_until))


## Datetime arithmetic
print('10 Today:',datetime.toString(Qt.ISODate))
print('11 Adding 12 days: {0}'.format(datetime.addDays(12).toString(Qt.ISODate)))
print('12 Subtracting 22 days: {0}'.format(datetime.addDays(-22).toString(Qt.ISODate)))
print('13 Adding 50 seconds: {0}'.format(datetime.addSecs(50).toString(Qt.ISODate)))
print('14 Adding 3 months: {0}'.format(datetime.addMonths(3).toString(Qt.ISODate)))
print('15 Adding 12 years {0}'.format(datetime.addYears(12).toString(Qt.ISODate)))


## Daylight saving time(夏令时)
print('16 Time zone: {0}' .format(datetime.timeZoneAbbreviation()))
if datetime.isDaylightTime():
    print("17 The current date falls into DST time")
else:
    print("17 The current date does not fall into DST time")


## Unix epoch（00:00:00 UTC on 1 January 1970）
### Unix 时间戳
unix_time = datetime.toSecsSinceEpoch()  # toSecsSinceEpoch() returns the Unix time
print('18 epoch:', unix_time)

QDate_time = QDateTime.fromSecsSinceEpoch(unix_time) # fromSecsSinceEpoch() we convert the Unix time to QDateTime.
print('19 Qdatetime:', QDate_time.toString(Qt.ISODate))


## Julian day
# The Julian day number 0 is assigned to the day starting at noon on January 1, 4713 BC. 
# The Julian Day Number (JDN) is the number of days elapsed since the beginning of this period.
test_date = QDate(2017, 9, 11) # same with the tutorial
print("20 Gregorian date for today: ", test_date.toString(Qt.ISODate))
print("21 Julian day for today: ", test_date.toJulianDay()) 


## Historical battles —— An usage of Julian day
### With Julian day it is possible to do calculations that span centuries. —— from the author
### Qdate.daysTo can do the same job
opium_war = QDate(1840, 6, 1)
counter_Japan_war = QDate(1931, 9, 18)

j_today = now.toJulianDay()
j_opium = opium_war.toJulianDay()
j_counter_Japan = counter_Japan_war.toJulianDay()

d1 = j_today - j_opium
d2 = j_today - j_counter_Japan

print("22 Days since opium war: {0}".format(d1))
print("23 Days since counter Japan war: {0}".format(d2))

##### output ########################
# 0  2018-10-15
# 1  2018年10月15日
# 2  Local datetime:  2018-10-15T19:02:35
# 3  Universal datetime:  2018-10-15T11:02:35Z
# 4  The Offset from UTC is: 28800 seconds
# 5  19:02:35
# 6  Days in month: 31
# 7  Days in year: 365
# 8  8764 days has passed since my birth
# 9  68 days until the final exam
# 10 Today: 2018-10-15T19:02:35
# 11 Adding 12 days: 2018-10-27T19:02:35
# 12 Subtracting 22 days: 2018-09-23T19:02:35
# 13 Adding 50 seconds: 2018-10-15T19:03:25
# 14 Adding 3 months: 2019-01-15T19:02:35
# 15 Adding 12 years 2030-10-15T19:02:35
# 16 Time zone: 中国标准时间
# 17 The current date does not fall into DST time
# 18 epoch: 1539601355
# 19 Qdatetime: 2018-10-15T19:02:35
# 20 Gregorian date for today:  2017-09-11
# 21 Julian day for today:  2458008
# 22 Days since opium war: 65149
# 23 Days since counter Japan war: 31804
