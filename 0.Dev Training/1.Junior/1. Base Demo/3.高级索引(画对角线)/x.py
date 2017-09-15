# coding=gbk

import scipy.misc
import matplotlib.pyplot

# ͨ���ѶԽ����ϵ�ֵ ��0, ��ʾ�˸߼��������÷�

# ��������Lena
lena = scipy.misc.lena()
xmax = lena.shape[0]
ymax = lena.shape[1]

# �߼�����
# �ѶԽ���λ�õ�ֵ��0
# x 0-xmax
# y 0-ymax
lena[ range(xmax), range(ymax) ] = 0

# ����һ���Խ���λ���ϵ�ֵ��0
# x xmax - 0
# y 0-ymax
lena[ range( xmax-1, -1, -1 ), range( ymax ) ] = 0

# ���ƶԽ��� ��0 ���ͼ�� Lena
matplotlib.pyplot.imshow( lena )
matplotlib.pyplot.show()