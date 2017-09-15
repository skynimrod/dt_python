#coding=gbk
import csv

filename = '2_1.csv'

data = []

print "hello world"

with open( filename ) as f:
	reader = csv.reader(f)

	header = reader.next()

    	data = [row for row in reader]

	i = 0
	print ', '.join(header).decode('gb2312')
        for datarow in data:
	    i += 1
            print  ', '.join(datarow).decode('gb2312')
	    if (i>=1): break