# coding=gbk

import scipy.misc
import matplotlib.pyplot

# 加载 数组 Lena
lena = scipy.misc.lena()

# 绘制数组Lena
matplotlib.pyplot.subplot( 221 )
matplotlib.pyplot.imshow( lena )

# 绘制翻转后的数组
matplotlib.pyplot.subplot( 222 )
matplotlib.pyplot.imshow( lena[:, ::-1] )

# 绘制数组的一部分
matplotlib.pyplot.subplot( 223 )
matplotlib.pyplot.imshow( lena[: lena.shape[0]/2, :lena.shape[1]/2] )

# 应用遮罩的效果
mask = lena % 2 == 0
masked_lena = lena.copy()
masked_lena[mask] = 0
matplotlib.pyplot.subplot( 224 )
matplotlib.pyplot.imshow( masked_lena )

matplotlib.pyplot.show()