# coding=gbk

# ����۸��������ݵ�ʱ��ͼ

import pylab
import random

# days to generate data for 
duration = 100

# mean value
mean_inc = 0.2

# standard deviation
std_dev_inc = 1.2

# time sries
x = range(duration)
y = []
price_today = 0

for i in x:
    next_delta = random.normalvariate( mean_inc, std_dev_inc )
    price_today += next_delta
    y.append( price_today )

pylab.plot(x, y )
pylab.xlabel("Time" )
pylab.ylabel("Value")

pylab.show()

# ��δ��붨����100�����ݵ�(��������)������. ���ڽ�������ÿһ��, ����ֵΪ mean_inc, ��׼��Ϊstd_dev_inc ����̫�ֲ� (random.normalvariate()) ��ѡȡһ�����ֵ, Ȼ�����ǰһ��ļ۸�(price_today) ��Ϊ����ļ۸�.

# �����Ҫ����Ŀ���, ����ʹ�ò�ͬ�ķֲ�. 