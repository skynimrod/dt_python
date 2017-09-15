# coding=gbk

import csv

with open('toolhire.csv') as th:
    toolreader = csv.reader(th)
    print( list(toolreader) )