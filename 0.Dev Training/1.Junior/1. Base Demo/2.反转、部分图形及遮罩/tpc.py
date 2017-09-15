# coding=gbk

import scipy.misc
import matplotlib.pyplot

# ���� ���� Lena
lena = scipy.misc.lena()

# ��������Lena
matplotlib.pyplot.subplot( 221 )
matplotlib.pyplot.imshow( lena )

# ���Ʒ�ת�������
matplotlib.pyplot.subplot( 222 )
matplotlib.pyplot.imshow( lena[:, ::-1] )

# ���������һ����
matplotlib.pyplot.subplot( 223 )
matplotlib.pyplot.imshow( lena[: lena.shape[0]/2, :lena.shape[1]/2] )

# Ӧ�����ֵ�Ч��
mask = lena % 2 == 0
masked_lena = lena.copy()
masked_lena[mask] = 0
matplotlib.pyplot.subplot( 224 )
matplotlib.pyplot.imshow( masked_lena )

matplotlib.pyplot.show()