# coding=gbk
import random 
import matplotlib
import matplotlib.pyplot as plt

SAMPLE_SIZE = 1000
#histogram buckets
buckets = 100
plt.figure()

# we need to update font size just for this example
matplotlib.rcParams.update( {'font.size':7} )

# 为了能排列下所有规定的图形, 我们定义了一个由 6 X 2 的subplot 网格 来显示所有的直方图. 第一个图形是在[0,1]之间的分布的
# 随机变量( normal distributed random variable )

plt.subplot(621)
plt.xlabel( "random.random" )
# Return the next random floating point number in the range [0.0, 1.0].
res = [ random.random() for _ in xrange(1, SAMPLE_SIZE) ]
plt.hist( res, buckets )

# 我们绘制的第二个图形 是一个均匀分布的随机变量( uniformly distributed random variable )
plt.subplot( 622 )
plt.xlabel( "random.uniform" )
# Return a random floating point number N such that a <= N <= b for a <= b and b<= N <= a for b < a.
# The end-point value b may or may not be included in the range depending on floating-point rounding in the equation 
# a + (b-a) * random(). 

a = 1
b = SAMPLE_SIZE
res = [ random.uniform(a, b) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist( res, buckets )

# 第三张图形 是一个三角形分布( triangular distribution )
plt.subplot( 623 )
plt.xlabel( "random.triangular" )

# Return a random floating point number N such that low <= N <= high and with the specified
# mode between those bounds. The low and high bounds default to zero and one. The mode argument
# defaults to the midpoint between the bounds, giving a symmetric distribution.

low = 1
high = SAMPLE_SIZE
res = [ random.triangular(low, high) for _ in xrange(1, SAMPLE_SIZE) ]
plt.hist( res, buckets )

# 第四个图形是 beta 分布 ( beta distribution ). 参数的条件是 alpha 和 beta 都要大于0. 返回值在0～1之间。

plt.subplot(624)
plt.xlabel("random.betavariate")
alpha = 1
beta = 10
res = [ random.betavariate(alpha, beta) for _ in xrange(1, SAMPLE_SIZE) ]
plt.hist( res, buckets )

# 第五幅 图形显示了一个指数分布( exponential distribution ). lambd 的值 是 1.0 除以 期望的中值, 是一个不为零的数
# (参数应该叫做 lambda, 但它是 Python 的一个保留字). 如果 lambd 是整数, 返回值的范围是零到正无穷大; 如果 lambd 为负,
# 返回值范围是负无穷大到 零.
plt.subplot( 625 )
plt.xlabel( "random.expovariate" ) 
lambd = 1.0 / ( ( SAMPLE_SIZE+1) / 2. )
res = [random.expovariate(lambd) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist( res, buckets)


# 第六幅图是gamma 分布( gamma distribution), 要求参数alpha 和 beta 都大于零. 概率分布函数如下: (略，在文本里面难写出来)
# 下面是gamma 分布的代码
plt.subplot( 626 )
plt.xlabel( "random.gammavariate")

alpha = 1 
beta = 10
res = [random.gammavariate( alpha, beta) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist( res, buckets )

# 第七幅图 是对数正太分布( Log normal distribution). 如果取这个分布的自然对数, 会得到一个中值为 mu, 标准差为sigma 的正太
# 分布. mu 可以取任何值, sigma 必须大于零.

plt.subplot( 627 )
plt.xlabel( "random.lognormvariate")
mu = 1
sigma = 0.5
res = [ random.lognormvariate(mu, sigma) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist(res, buckets )

# 第八幅图 是一个正态分布( normal distribution), 中值为mu, 标准差为sigma
plt.subplot( 628 )
plt.xlabel( "random.normalvariate" )
mu = 1
sigma = 0.5
res = [random.normalvariate(mu, sigma) for _ in xrange(1, SAMPLE_SIZE) ]
plt.hist( res, buckets )

# 最后一幅图是帕累托分布( Pareto distribution ), alpha 是形状参数
plt.subplot(629)
plt.xlabel( "random.paretovariate " )
alpha = 1
res = [random.paretovariate(alpha) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist(res, buckets )

plt.tight_layout()
plt.show()