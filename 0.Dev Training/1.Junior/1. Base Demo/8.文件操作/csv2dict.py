# coding=gbk

import csv

with open('toolhire.csv') as th:
    rdr = csv.DictReader( th )
    #for item in rdr:       # �����2�в�ע�͵Ļ�, ��������ִ�о������⡣������
    #    print item
    print '============='
    items = [item for item in rdr]

n= [item['Name'] for item in items if item['Owner'] == 'Fred']
b=[item['Borrower'] for item in items if item['Owner'] == 'Fred']
print n
print b
print {'Name':item['Name'] for item in items if item['Owner'] == 'Fred'}
dict(zip(n,b))