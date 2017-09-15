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

# Ϊ�������������й涨��ͼ��, ���Ƕ�����һ���� 6 X 2 ��subplot ���� ����ʾ���е�ֱ��ͼ. ��һ��ͼ������[0,1]֮��ķֲ���
# �������( normal distributed random variable )

plt.subplot(621)
plt.xlabel( "random.random" )
# Return the next random floating point number in the range [0.0, 1.0].
res = [ random.random() for _ in xrange(1, SAMPLE_SIZE) ]
plt.hist( res, buckets )

# ���ǻ��Ƶĵڶ���ͼ�� ��һ�����ȷֲ����������( uniformly distributed random variable )
plt.subplot( 622 )
plt.xlabel( "random.uniform" )
# Return a random floating point number N such that a <= N <= b for a <= b and b<= N <= a for b < a.
# The end-point value b may or may not be included in the range depending on floating-point rounding in the equation 
# a + (b-a) * random(). 

a = 1
b = SAMPLE_SIZE
res = [ random.uniform(a, b) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist( res, buckets )

# ������ͼ�� ��һ�������ηֲ�( triangular distribution )
plt.subplot( 623 )
plt.xlabel( "random.triangular" )

# Return a random floating point number N such that low <= N <= high and with the specified
# mode between those bounds. The low and high bounds default to zero and one. The mode argument
# defaults to the midpoint between the bounds, giving a symmetric distribution.

low = 1
high = SAMPLE_SIZE
res = [ random.triangular(low, high) for _ in xrange(1, SAMPLE_SIZE) ]
plt.hist( res, buckets )

# ���ĸ�ͼ���� beta �ֲ� ( beta distribution ). ������������ alpha �� beta ��Ҫ����0. ����ֵ��0��1֮�䡣

plt.subplot(624)
plt.xlabel("random.betavariate")
alpha = 1
beta = 10
res = [ random.betavariate(alpha, beta) for _ in xrange(1, SAMPLE_SIZE) ]
plt.hist( res, buckets )

# ����� ͼ����ʾ��һ��ָ���ֲ�( exponential distribution ). lambd ��ֵ �� 1.0 ���� ��������ֵ, ��һ����Ϊ�����
# (����Ӧ�ý��� lambda, ������ Python ��һ��������). ��� lambd ������, ����ֵ�ķ�Χ���㵽�������; ��� lambd Ϊ��,
# ����ֵ��Χ�Ǹ������ ��.
plt.subplot( 625 )
plt.xlabel( "random.expovariate" ) 
lambd = 1.0 / ( ( SAMPLE_SIZE+1) / 2. )
res = [random.expovariate(lambd) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist( res, buckets)


# ������ͼ��gamma �ֲ�( gamma distribution), Ҫ�����alpha �� beta ��������. ���ʷֲ���������: (�ԣ����ı�������д����)
# ������gamma �ֲ��Ĵ���
plt.subplot( 626 )
plt.xlabel( "random.gammavariate")

alpha = 1 
beta = 10
res = [random.gammavariate( alpha, beta) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist( res, buckets )

# ���߷�ͼ �Ƕ�����̫�ֲ�( Log normal distribution). ���ȡ����ֲ�����Ȼ����, ��õ�һ����ֵΪ mu, ��׼��Ϊsigma ����̫
# �ֲ�. mu ����ȡ�κ�ֵ, sigma ���������.

plt.subplot( 627 )
plt.xlabel( "random.lognormvariate")
mu = 1
sigma = 0.5
res = [ random.lognormvariate(mu, sigma) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist(res, buckets )

# �ڰ˷�ͼ ��һ����̬�ֲ�( normal distribution), ��ֵΪmu, ��׼��Ϊsigma
plt.subplot( 628 )
plt.xlabel( "random.normalvariate" )
mu = 1
sigma = 0.5
res = [random.normalvariate(mu, sigma) for _ in xrange(1, SAMPLE_SIZE) ]
plt.hist( res, buckets )

# ���һ��ͼ�������зֲ�( Pareto distribution ), alpha ����״����
plt.subplot(629)
plt.xlabel( "random.paretovariate " )
alpha = 1
res = [random.paretovariate(alpha) for _ in xrange(1, SAMPLE_SIZE)]
plt.hist(res, buckets )

plt.tight_layout()
plt.show()