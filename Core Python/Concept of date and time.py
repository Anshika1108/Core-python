#present date and time
import datetime
x = datetime.datetime.now()
print(x)

#get day of week
x = datetime.datetime.now()
print(x.strftime("%A"))

#get name of month
x = datetime.datetime.now()
print(x.strftime("%B"))

#date and time selected by own given date
y = datetime.datetime(2003,8,11)
print(y)
