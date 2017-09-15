# coding=gbk

import csv

items = [
    ['1','LawnMower','Small Hover mower','Fred','Joe','2012-04-01','2014-04-26'],
    ['2','LawnMower','Ride-on mower','Mike','Anne','2014-09-05','2013-01-05'],
    ['3','Bike','BMX bike','Joe','Rob','2013-07-03','2013-07-22'],
    ['4','Drill','Heavy duty hammer','Rob','Fred','2013-11-19','2013-11-29'],
    ['5','Scarifier','Quality, stainless steel','Anne','Mike','2013-12-05'],
    ['6','Sprinkler','Cheap but effective','Fred','2013-12-15']
    ]

with open('tooldesc.csv', 'w') as tooldata:
    toolwriter = csv.writer( tooldata )
    for item in items:
        toolwriter.writerow( item )