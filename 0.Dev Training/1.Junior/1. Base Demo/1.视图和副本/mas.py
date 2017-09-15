# coding=gbk

import scipy.misc
import matplotlib.pyplot

lena = scipy .misc.lena()
acopy = lena.copy()
aview = lena.view()

# ��������Lena
matplotlib.pyplot.subplot( 221 )
matplotlib.pyplot.imshow( lena )

# ��������Lena �ĸ���
matplotlib.pyplot.subplot( 222 )
matplotlib.pyplot.imshow( acopy )

# ���� ����Lena ����ͼ
matplotlib.pyplot.subplot( 223 )
matplotlib.pyplot.imshow( aview )

# �ı���ͼ���ݺ��ڻ�����ͼ
aview.flat = 0
matplotlib.pyplot.subplot( 224 )
matplotlib.pyplot.imshow( aview )

matplotlib.pyplot.show()