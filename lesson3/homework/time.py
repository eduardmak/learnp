import locale
from datetime import datetime,date,timedelta

daytoday = (date.today())

yasterday_delta = timedelta(days=1)

print (daytoday-yasterday_delta)
print (daytoday)
print (daytoday - timedelta(days=30))

str_time = "01/01/17 12:10:03.234567"
print(datetime.strptime(str_time,"%d/%m/%y %H:%M:%S.%f"))