# coding=gbk

import scipy.misc
import matplotlib.pyplot

# 通过把对角线上的值 置0, 演示了高级索引的用法

# 加载数组Lena
lena = scipy.misc.lena()
xmax = lena.shape[0]
ymax = lena.shape[1]

# 高级索引
# 把对角线位置的值置0
# x 0-xmax
# y 0-ymax
lena[ range(xmax), range(ymax) ] = 0

# 把另一条对角线位置上的值置0
# x xmax - 0
# y 0-ymax
lena[ range( xmax-1, -1, -1 ), range( ymax ) ] = 0

# 绘制对角线 置0 后的图像 Lena
matplotlib.pyplot.imshow( lena )
matplotlib.pyplot.show()