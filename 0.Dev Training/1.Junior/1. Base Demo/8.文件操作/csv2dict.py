# coding=gbk

import csv

with open('toolhire.csv') as th:
    rdr = csv.DictReader( th )
    #for item in rdr:       # 如果这2行不注释的话, 下面的语句执行就有问题。。。。
    #    print item
    print '============='
    items = [item for item in rdr]

n= [item['Name'] for item in items if item['Owner'] == 'Fred']
b=[item['Borrower'] for item in items if item['Owner'] == 'Fred']
print n
print b
print {'Name':item['Name'] for item in items if item['Owner'] == 'Fred'}
dict(zip(n,b))