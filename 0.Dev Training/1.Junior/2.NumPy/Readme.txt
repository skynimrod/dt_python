. NumPy

  http://www.scipy.org/scipylib/download.html   官网下载地址， 包括源代码与二进制

. Windows 环境下安装 Python 包(库) 的方法

  http://www.lfd.uci.edu/~gohlke/pythonlibs/

  按照NumPy 官网的说法  http://www.scipy.org/install.html  -> Windows packages 部分

  Windows 没有任何类似于Linux 的包管理工具。 所以需要安装.  但是， 如果不用这种方法的， 可以用上面URL说的方法来

  从官网下载NumPy 1.11.1.zip 后， 解压， 然后进入解压后的目录, 有个INSTALL.rst.txt 详细介绍了安装NumPy的说明.

  对于Windows 版本. 执行类似下面的命令:

      python setup.py build -j 4 install --prefix $HOME/.local

   这条命令的意思: 在4 CPUs  上编译numpy , 并安装numpy 到指定的前缀.

   如果执行原地安装， 命令如下:

     python setup.py build_ext --inplace -j 2

  但是编译需要的前置条件是:

   1. 安装了Python 2.6+ 或 Python 3.2+

   2. Cython  0.19+               http://cython.org/#download -> https://pypi.python.org/pypi/Cython/

   3. nose__  1.0+    仅仅是为了测试用.    http://somethingaboutorange.com/mrl/projects/nose/

  如果仅仅是为了编译Numpy 然后Numpy 自身用, 使用 runtests.py , 详见:

      http://docs.scipy.org/doc/numpy-dev/dev/development_environment.html

. 通过如下的命令安装NumPy 即可， 上面的是用来分析编译NumPy 源码的

  e:\> pip install NumPy

. NumPy 以高效率的数组著称, 部分原因归于索引的易用性. 

. 查看当前Python 中的NumPy 的版本以及文件

>>> import numpy
>>> print numpy.__version__
1.11.1
>>> print numpy.__file__
C:\Python27\lib\site-packages\numpy\__init__.pyc


. 用seed() 来初始化伪随机数生成器, 这样 random() 方法就能生成相同的期望随机值. 有时候这非常有用, 并且比预先 生成随机数并保存到文件中要好. 第二种方法并不总是可行的, 因为它要求保存(可能是大量的) 数据到文件系统.

  如果想避免随机生成的序列重复, 推荐使用random.SystemRandom, 其底层使用 os.urandom.   os.urandom 提供了对更多熵源( entropy source) 的访问. 如果使用这个随机数生成器接口, seed() 和 setstate() 没有影响. 这样一来, y昂本就不是可重现的了. 

  如果想要一些随机的单词, (Linux系统中) 最简单的哦方法就是用 /usr/share/dict/words.  Windows 用户可以使用从各种免费资源生成的文件(Project Gutenberg、Wiktionary、British National Corpus 或者 Dr Peter Norvig 的http://norvig.com/big.txt)
  