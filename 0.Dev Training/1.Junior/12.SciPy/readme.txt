. SciPy 是一个 和 NumPy密切相关的Python 科学计算库.  实际上, 很多年前, SciPy 和 NumPy 归属于同一个项目. 

. 安装

  1. 从源文件安装

     如果已经安装了git, 可以使用如下命令复制SciPy 的版本库

     git clone https://github.com/scipy/scipy.git

     python setup.py build
    
     python setup.py install --user

     上面这2条命令把 SciPy 安装到了你的用户目录, 要求Python 的版本不低于2.6

     构建安装文件之前, 你还需要安装以下 依赖包:

        BLAS 和  LAPACK 库

        C 和 Fortran 编译器

     作为NumPy 安装文件的一部分, 你有可能已经安装好这些软件了.

