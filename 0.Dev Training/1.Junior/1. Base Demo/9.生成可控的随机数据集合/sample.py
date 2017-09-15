import pylab
import random

SAMPLE_SIZE = 100

# seed random generator
# if no argument provided
#uses system current time
random.seed()

# store generated random values here
real_rand_vars = []

# pick some random values
real_rand_vars = [ random.random() for val in xrange(SAMPLE_SIZE) ]
# create histogrm from data in 10 buckets
pylab.hist( real_rand_vars, 10 )

#define x and y labels
pylab.xlabel("Number range")
pylab.ylabel("Count")

# show figure
pylab.show()