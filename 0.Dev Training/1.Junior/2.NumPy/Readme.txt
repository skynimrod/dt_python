. NumPy

  http://www.scipy.org/scipylib/download.html   �������ص�ַ�� ����Դ�����������

. Windows �����°�װ Python ��(��) �ķ���

  http://www.lfd.uci.edu/~gohlke/pythonlibs/

  ����NumPy ������˵��  http://www.scipy.org/install.html  -> Windows packages ����

  Windows û���κ�������Linux �İ������ߡ� ������Ҫ��װ.  ���ǣ� ����������ַ����ģ� ����������URL˵�ķ�����

  �ӹ�������NumPy 1.11.1.zip �� ��ѹ�� Ȼ������ѹ���Ŀ¼, �и�INSTALL.rst.txt ��ϸ�����˰�װNumPy��˵��.

  ����Windows �汾. ִ���������������:

      python setup.py build -j 4 install --prefix $HOME/.local

   �����������˼: ��4 CPUs  �ϱ���numpy , ����װnumpy ��ָ����ǰ׺.

   ���ִ��ԭ�ذ�װ�� ��������:

     python setup.py build_ext --inplace -j 2

  ���Ǳ�����Ҫ��ǰ��������:

   1. ��װ��Python 2.6+ �� Python 3.2+

   2. Cython  0.19+               http://cython.org/#download -> https://pypi.python.org/pypi/Cython/

   3. nose__  1.0+    ������Ϊ�˲�����.    http://somethingaboutorange.com/mrl/projects/nose/

  ���������Ϊ�˱���Numpy Ȼ��Numpy ������, ʹ�� runtests.py , ���:

      http://docs.scipy.org/doc/numpy-dev/dev/development_environment.html

. ͨ�����µ����װNumPy ���ɣ� �������������������NumPy Դ���

  e:\> pip install NumPy

. NumPy �Ը�Ч�ʵ���������, ����ԭ�����������������. 

. �鿴��ǰPython �е�NumPy �İ汾�Լ��ļ�

>>> import numpy
>>> print numpy.__version__
1.11.1
>>> print numpy.__file__
C:\Python27\lib\site-packages\numpy\__init__.pyc


. ��seed() ����ʼ��α�����������, ���� random() ��������������ͬ���������ֵ. ��ʱ����ǳ�����, ���ұ�Ԥ�� ��������������浽�ļ���Ҫ��. �ڶ��ַ����������ǿ��е�, ��Ϊ��Ҫ�󱣴�(�����Ǵ�����) ���ݵ��ļ�ϵͳ.

  ��������������ɵ������ظ�, �Ƽ�ʹ��random.SystemRandom, ��ײ�ʹ�� os.urandom.   os.urandom �ṩ�˶Ը�����Դ( entropy source) �ķ���. ���ʹ�����������������ӿ�, seed() �� setstate() û��Ӱ��. ����һ��, y�����Ͳ��ǿ����ֵ���. 

  �����ҪһЩ����ĵ���, (Linuxϵͳ��) ��򵥵�Ŷ���������� /usr/share/dict/words.  Windows �û�����ʹ�ôӸ��������Դ���ɵ��ļ�(Project Gutenberg��Wiktionary��British National Corpus ���� Dr Peter Norvig ��http://norvig.com/big.txt)
  