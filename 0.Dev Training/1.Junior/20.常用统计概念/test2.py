# coding=gbk

# 虚拟价格增长数据的时序图

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

# 这段代码定义了100个数据点(虚拟天数)的序列. 对于接下来的每一天, 从中值为 mean_inc, 标准差为std_dev_inc 的正太分布 (random.normalvariate()) 中选取一个随机值, 然后加上前一天的价格(price_today) 作为当天的价格.

# 如果想要更多的控制, 可以使用不同的分布. 