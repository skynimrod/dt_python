. 安装

  pip install virtualenv

. 激活/注销

  Windows : 进入Script子目录， 然后运行  activate/deactivate

. 说明

   参见:

        http://blog.sina.com.cn/s/blog_55646c98010179og.html 

  VirtualEnv  用于在一台机器上创建多个python 运行环境, VirtualEnvWrapper 为前者提供了一些便利的命令行上的封装。 

. 为什么要用:

  1. 隔离项目之间的第三方依赖, 比如  A项目 依赖 django1.2.5, B 项目依赖 django1.3

  2. 为部署应用提供方便, 把开发环境的虚拟环境打包到生产环境即可, 不需要在服务器上再折腾一遍.

. virtualenv 怎么用

  1. 创建 虚拟环境

     virtualenv [env1]

     就会在当前路径下创建一个env1 的子目录。 例如:

E:\t_tmp\test>virtualenv env1
New python executable in E:\t_tmp\test\env1\Scripts\python.exe
Installing setuptools, pip, wheel...done.

E:\t_tmp\test>

     在env1 子目录中, 就是一个完整的python  开发环境. 


. virtualenvwrapper 怎么用

  1. 安装

     pip install virtualenvwrapper

     把下面这句 加到~/.bash_profile里面, 如不嫌麻烦, 也可以每次都手动执行.

     source /usr/local/bin/virtualenvwrapper.sh

. 常用命令

  1. 创建的虚拟环境
 
     mkvirtualenv [env1]

         该命令会帮我们创建一个新环境, 默认情况下, 环境的目录是.virtualenv/env1, 创建过程中它会自动帮我们安装pip, 以后我们要安装新依赖时可直接使用pip 命令.

         创建完之后, zidong切换到该环境下工作, 可看到提示符变为:

         (env1)$

         在这个环境下安装的依赖不会影响到其他的环境

  2. 显示该环境中所安装的包

     lssitepackages

  3. 切换环境
  
     workon [env]

     随时使用"workon 环境名" 进行环境切换, 如果不带环境名参数, 则显示当前使用的环境

  4. deactivate  

     推出当前的环境

  5. cpvirtualenv [source] [dest]

     复制一份虚拟环境

  6. cdvirtualenv [subdir] 

     把当前工作目录设置为所在的环境目录

  7. cdsitepackages [subdir]

     把当前工作目录设置为所在环境的sitepackages 路径

  8. add2virtualenv [dir] [dir] 

     把指定的目录加入当前使用的环境的path 中, 这常使用与在多个project 里面同时使用一个较大的库 的情况.

  9. toggleglobalsitepackages -q

     控制当前的环境是否使用全局的sitepackages 目录.

. FAQ:

  1. 通过pip install virutalenvwrapper 安装 virtualenvwrapper 后， 在命令行下面切换虚拟开发环境的时候提示workon 不存在. 应该是virutalenvwrapper 相关的执行文件所在路径没有添加到path 中。 

  解决:

       对于linux 环境而言, 需要每次运行  source /usr/local/bin/virtualenvwrapper.sh， 那么对于windows 而言, 只需要运行对应的 virtualenvwrapper.sh.bat 即可。 

      但是运行上面的bat文件的时候, 对于xp环境而言, 会出现一些错误.  该 bat 文件所在目录为python 2.7\Scripts, 安装完Python 后就已经在path 中了, 可以直接运行. 

E:\t_tmp\test>virtualenvwrapper.sh
Welcome to Git (version 1.9.4-preview20140611)


Run 'git help git' to display the help index.
Run 'git help <command>' to display help for specific commands.
C:\Python27\Scripts\virtualenvwrapper.sh: line 197: mktemp: command not found
touch: creating `': No such file or directory
ERROR: virtualenvwrapper could not create a temporary file name.

  看错误提示可知， 197行的 mktemp 命令在windows 环境下没有。 

  busybox for windows 里面有 mktemp 命令.  参见:

      http://www.zhihu.com/question/21175572?sort=created

  这个URL 提供了许多有用的小软件介绍. 

      http://www.downloadcrew.com/article/32376-busybox_for_windows    这个可以下载 Windows 版本的busybox

  由于 virtualenvwrapper 是面向linux 的版本, 对应的virtualenvwrapper.sh.bat脚本中的有些命令是linux的命令,包括一些常用变量(比如@$之类的), 即便使用了busybox for windows ，运行也是有点问题的， 因为解析有些变量有问题。

  解决办法是, 使用virtualenvwrapper-win, 下载地址为:

       https://pypi.python.org/pypi/virtualenvwrapper-win

       http://www.cnblogs.com/skynet/p/4124763.html        一个相关的技术文档

  或者使用 

       pip install virtualenvwrapper-win

  来进行安装

  virtualenvwrapper-win 将安装在 python 的根目录下面. 如  D:\python34   

  virtualenvwrapper-win和virtualenvwrapper的使用方式完全一样.


  基于virtualenv + virtualenvwrapper可以很好的完成环境隔离，保证对每个应用的环境是干净的。而且对一个干净的环境可以通过：

pip freeze > requirements.txt将包依赖信息保存在requirements.txt文件

pip install -r requirements.txt会自动从网上下载并安装所有包

   注意, 如果安装过程中某个package失败, 会导致所有安装都失败, 为此, 从requirements.txt 中删除了失败的package（稍后可以单独安装, 下载whl 等方式）

   一般都是在 pypi 中下载. 例如:  https://pypi.python.org/pypi/microsofttranslator/0.8

方便应用部署分发，关于pip软件包管理再下一篇介绍。

.  virtualenvwrapper-win 的主要命令:

  1. mkvirtualenv <name>

  2. lsvirtualenv           察看当前有哪些开发环境

  3. rmvirtualenv <name>

  4. workon [<name>]

  5. deactivate

  6. add2virtualenv <full or relative path>   

  传统命令

  1. cdproject

  2. cdsitepackages

  3. cdvirtualenv

  4. lssitepackages

  5. setprojectdir <full or relative path>

  6. toggleglobalsitepackages

  7. whereis <file>  
