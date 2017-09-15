# coding=gbk
import scipy.misc
import matplotlib.pyplot
import numpy.random
import numpy.testing

# 加载数组Lena
lena = scipy.misc.lena()
xmax = lena.shape[0]
ymax = lena.shape[1]

def shuffle_indices( size ):
    arr = numpy.arange( size )
    numpy.random.shuffle( arr )
  
    return arr

xindices = shuffle_indices( xmax )
numpy.testing.assert_equal( len( xindices ), xmax )
yindices = shuffle_indices( ymax )
numpy.testing.assert_equal( len( yindices ), ymax )

# 绘制数组 Lena
matplotlib.pyplot.imshow( lena[numpy.ix_( xindices, yindices )] )
matplotlib.pyplot.show()