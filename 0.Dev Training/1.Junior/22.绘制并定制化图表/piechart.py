from pylab import *

# make a square figure and axes
figure( 1, figsize=(6,6) )
ax = axes( [0.1, 0.1, 0.8, 0.8])

# the slices will be ordered and plotted counter-clockwise.
labels = 'Spring', 'Summer', 'Autumn', 'Winter'

# fractions are either x/sum(x) or x if sum(x) <= 1
x = [15, 30, 45, 10]

# explode must be len(x) sequence or None
explode = (0.1, 0.1, 0.1, 0.1)

pie(x, explode = explode, labels = labels, autopct='%1.1f%%', startangle=67 )

title( 'Rainy days by season' )

show()