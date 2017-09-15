# coding=gbk

import scipy.misc
import matplotlib.pyplot

lena = scipy .misc.lena()
acopy = lena.copy()
aview = lena.view()

# 绘制数组Lena
matplotlib.pyplot.subplot( 221 )
matplotlib.pyplot.imshow( lena )

# 绘制数组Lena 的副本
matplotlib.pyplot.subplot( 222 )
matplotlib.pyplot.imshow( acopy )

# 绘制 数组Lena 的视图
matplotlib.pyplot.subplot( 223 )
matplotlib.pyplot.imshow( aview )

# 改变视图内容后在绘制视图
aview.flat = 0
matplotlib.pyplot.subplot( 224 )
matplotlib.pyplot.imshow( aview )

matplotlib.pyplot.show()