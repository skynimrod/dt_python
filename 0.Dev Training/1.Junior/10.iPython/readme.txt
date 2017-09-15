. 在Windows 中安装IPython 和setuptools

  在IPython的官网可以下载适用于Python 2 和 Python 3 的二进制Windows 安装文件. 具体安装过程参阅 

      http://ipython.org/ipython-doc/stable/install/install.html#windows

  从 https://pypi.python.org/pypi/setuptools#files 获得 setuptools 的安装文件并完成安装. 之后继续安装pip. 具体步骤如下:

    cd  c:\python27\scripts

    python .\easy_install-27-script.py pip

. 安装

  要求 Python 2.7 或者 3.3+

      pip install "ipython[all]"

  这个安装命令, 会下载并安装IPython 以及主要的可选依赖来支持 notebook, qtconsole, tests,以及其他一些功能. 有一些依赖(比如Qt, PyQt， pandoc等) 不能通过pip 安装. 

  测试安装结果:

  iptest

  如果仅仅安装ipython 自身， 用下面的命令:

  pip install ipython

. 

. IPython 是一个Python 的交互式 shell , 比默认的python shell 好用的多, 支持变量自动补全, 自动缩进, 支持 bash shell 命令, 内置了许多很有用的功能函数.  在 ubuntu 下 只要 sudo apt-get install ipython 就装好了, 通过ipython 启动. 

. 下面是 ipython 中几个简单好用的magic 函数

  %bg function把 function 放到后台执行.  例如: %bg myfunc(x, y, z = 1), 之后可以用 jobs 将其结果取回.  myvar = jobs.result(5) 或 myvar = jobs[5].result.  另外, jobs.status() 可以产看现有任务的状态.

  %ed 或 %edit 编辑一个文件并执行, 如果只编辑不执行, 用 ed -x filename 即可。

  %env  显示环境变量

  %hist  或 %history 显示历史记录

  %macro name n1-n2 n3-n4 ... n5 .. n6 ...  创建一个名称为name 的宏, 执行name 就是执行 n1-n2 n3-n4 ... n5 ... n6 .. 这些代码

  %pwd  显示当前目录

  %pycat filename 用语法高亮显示一个python 文件(不用加 .py 后缀名)

  %save filename n1-n2 n3-n4 ... n5 ... n6 ... 将执行过多代码保存为文件

  %time statement  计算一段代码的执行时间

  %timeit statement 自动选择重复和循环次数计算一段代码的执行时间, 太方便了

  另外, ipython 中用 ! 表示执行shell 命令, 用 $ 将python 的变量转化为shell 变量.  通过这两个符号, 我们就可以做到和shell 命令之间的交互, k恶意非常方便的做许多复杂的工作. 比如你可以很方便的创建一组目录:

  for i in range(10):
    
       s = "dir%s" % i
       !mkdir $s

  不过写法上还是有一些限制, $后面只能跟变量名, 不能直接写复杂表达式, $"dir%s"%i 就是错误的写法了, 所以要先完全产生 python 的变量以后再用.  像下面的用法也是错误的:

     for i in !ls: print i

   可以写为:

     a = !ls
     
     for i in a: print i

   还有一点需要说明, 就是执行普通的shell 命令中如果有$ 的话需要用两个 $. 比如原来的echo $PAHT现在得写成 $echo$$PATH

   在较新的ipython 版本中, 添加了 ipython notebook 的功能, 弥补了ipython shell 下代码不易保存等缺点, 并且在使用 --pylab inline 选项后, 可以在代码执行后立即显示运行结果(包括图片, 数据表格等), 因此在数据分析中运用十分广泛. 

. 在 IPython 的 pylab 模式下, 可以使用 help 命令打开NumPy函数的手册页面. 你并不需要知道所有函数的名字, 因为可以在键入少量字符后按下Tab 键 进行自动补全. 例如:

  In [2]: help ar<Tab>
      
     返回所有ar 开头的函数名称

  In [2]: help arrange

