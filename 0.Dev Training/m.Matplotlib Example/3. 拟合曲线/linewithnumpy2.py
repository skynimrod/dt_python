# -*- coding: utf-8 -*-

#二次多项式拟合

import numpy

def polyfit(x, y, degree):
    results = {}
    coeffs = numpy.polyfit(x, y, degree)
    results['polynomial'] = coeffs.tolist()

    # r-squared
    p = numpy.poly1d(coeffs)
    # fit values, and mean
    yhat = p(x)                         # or [p(z) for z in x]
    ybar = numpy.sum(y)/len(y)          # or sum(y)/len(y)
    ssreg = numpy.sum((yhat-ybar)**2)   # or sum([ (yihat - ybar)**2 for yihat in yhat])
    sstot = numpy.sum((y - ybar)**2)    # or sum([ (yi - ybar)**2 for yi in y])
    results['determination'] = ssreg / sstot #准确率
    return results

x=[ 1 ,2  ,3 ,4 ,5 ,6]
y=[ 2.5 ,3.51 ,4.45 ,5.52 ,6.47 ,7.2]
z1 = polyfit(x, y, 2)
print( z1 )

# {'determination': 0.99893014166855998, 'polynomial': [-0.024285714285714417, 1.1
# 257142857142868, 1.37]}
