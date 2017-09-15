# coding=gbk
# ע�⣬ ��һ��ע��������֧�����ĵģ� ���û�еĻ��� ע���������Ҳ����ʾ����ġ�
# ����: python sizeChange.py 2 2         # �����2 2 �����ŵ����ݣ�Ҳ�������ŵĲ���. 

import scipy.misc
import sys
import matplotlib.pyplot
import numpy.testing

# ����ű���������SciPy����ͼ��Lena �Ĵ�С

if ( len( sys.argv ) != 3 ):
    print "Usage python %s yfactor xfactor" % ( sys.argv[0] )
    sys.exit()

# ����ͼ��Lena ��һ������
lena = scipy.misc.lena()

# ͼ��Lena �Ĺ��
LENA_X = 512
LENA_Y = 512

# �������Lena ����״
numpy.testing.assert_equal( ( LENA_X, LENA_Y ), lena.shape )

# ��ȡ����ϵ��
yfactor = float( sys.argv[1] )
xfactor = float( sys.argv[2] )

# ��������Lena �Ĵ�С
resized = lena.repeat( yfactor, axis = 0 ).repeat( xfactor, axis = 1 )

# ����С��������������״
numpy.testing.assert_equal( ( yfactor * LENA_Y, xfactor * LENA_X ), resized.shape )

# ��������Lena
matplotlib.pyplot.subplot( 211 )
matplotlib.pyplot.imshow( lena )

# ���ƴ�С�����������
matplotlib.pyplot.subplot( 212 )
matplotlib.pyplot.imshow( resized )
matplotlib.pyplot.show()