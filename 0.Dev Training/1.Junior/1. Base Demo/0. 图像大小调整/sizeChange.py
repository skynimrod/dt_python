# coding=gbk
# 注意， 第一行注释是用来支持中文的， 如果没有的话， 注释里的中文也会提示出错的。
# 运行: python sizeChange.py 2 2         # 后面的2 2 是缩放的数据，也就是缩放的参数. 

import scipy.misc
import sys
import matplotlib.pyplot
import numpy.testing

# 这个脚本用来调整SciPy库中图像Lena 的大小

if ( len( sys.argv ) != 3 ):
    print "Usage python %s yfactor xfactor" % ( sys.argv[0] )
    sys.exit()

# 加载图像Lena 到一数组中
lena = scipy.misc.lena()

# 图像Lena 的规格
LENA_X = 512
LENA_Y = 512

# 检查数组Lena 的形状
numpy.testing.assert_equal( ( LENA_X, LENA_Y ), lena.shape )

# 获取调整系数
yfactor = float( sys.argv[1] )
xfactor = float( sys.argv[2] )

# 调整数组Lena 的大小
resized = lena.repeat( yfactor, axis = 0 ).repeat( xfactor, axis = 1 )

# 检查大小调整后的数组的形状
numpy.testing.assert_equal( ( yfactor * LENA_Y, xfactor * LENA_X ), resized.shape )

# 绘制数组Lena
matplotlib.pyplot.subplot( 211 )
matplotlib.pyplot.imshow( lena )

# 绘制大小调整后的数组
matplotlib.pyplot.subplot( 212 )
matplotlib.pyplot.imshow( resized )
matplotlib.pyplot.show()