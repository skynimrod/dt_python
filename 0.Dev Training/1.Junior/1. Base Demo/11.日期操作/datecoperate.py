# -*-  coding: utf-8  -*-

import datetime

from datetime import date
from datetime import time
from datetime import timedelta

dt = datetime.datetime.now()
print( dt )
print( dt.year )
print( dt.month )
print( dt.day )

t = dt.date()
print(t)

print( dt.hour )
print( dt.minute )
print( dt.second )
print( dt.microsecond )

s1 = dt.strftime('%Y%m%d')
#s2 = dt.hour < 17 ? "_1" : "_2"
s2 = "_1" if dt.hour < 17 else "_2"

print("s1="+s1)
print("s2="+s2)

dt1 = date.today()


print(dt1)
print( dt1.year )
print( dt1.month )
print( dt1.day )

days = -3
td = timedelta(days=days)
print(td)
print(type(td))

d2 = dt1+td
print(d2)
print(td.days)
print(d2.strftime("%Y%m%d"))
print('=====')
while(days<0):
    print(d2)
    datestr = d2.strftime("%Y%m%d")
    pathstr = datestr + "/" + datestr+".txt"
    print(pathstr)

    days += 1
    td = timedelta(days=days)
    d2 = dt1+td


a = -3
print(-(a))

