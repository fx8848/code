import datetime
import calendar

firstday = datetime.datetime(1901, 1, 1)
lastday = datetime.datetime(2000, 12, 31)
oneday = datetime.timedelta(days=1)

nextsunday = firstday
number = 0

while nextsunday.weekday() != calendar.SUNDAY:
	nextsunday += oneday

while nextsunday <= lastday:
	if nextsunday.day == 1:
		number += 1
	nextsunday += datetime.timedelta(days=7)
print number
