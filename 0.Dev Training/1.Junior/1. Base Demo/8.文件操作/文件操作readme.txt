参见:

     http://www.cnblogs.com/rollenholt/archive/2012/04/23/2466179.html

     Python 2.7.12 document->The Python Standard Library ->File Formats, File and Directory Access

. Python 中对文件、文件夹(文件操作函数)的操作需要涉及到os模块和shutil模块.

. 1. 获得当前工作目录

     os.getcwd()

  2. 获得指定目录下的所有文件和目录名

     os.listdir()

  3. 删除一个文件

     os.remove()

  4. 删除多个目录

     os.removedirs( r "c:\python")

  5. 判断给定的路径是否是一个文件

     os.path.isfile()

  6. 判断给定的路径是否是一个目录

     os.path.isdir()

  7. 判断似乎否是绝对路径

     os.path.isabs()

  8. 检查给定的路径(或文件)是否存在

     os.path.exists()

  9. 返回一个路径的目录名和文件名

     os.path.split()

     比如: os.path.split('/home/swaroop/byte/code/pem.txt')   结果:('/home/swaroop/byte/code', 'poem.txt')

  10. 分离扩展名

     os.path.splitext()

  11. 获取路径名

      os.path.dirname()

  12. 获取文件名

      os.path.basename()

  13. 运行shell命令

      os.system()

  14. 读取和设置环境变量

      os.getenv()  与  os.putenv(0

  15. 给出当前平台使用的行终止符

      os.linesep       Windows使用'\r\n', Linux 使用'\n'   而 Mac 使用 '\r'

  16. 指示你正在使用的平台:

      os.name     对于Windows, 它是'nt', 而对于 Linux/Unix 用户， 它是 'posix'

  17. 重命名

      os.rename( old, new )

  18. 创建多级目录

      os.makedirs(r "c:\python\test")

  19. 创建单个目录

      os.mkdir( "test" )

  20. 获取文件属性

      os.stat( file )

  21. 修改文件权限与时间戳

      os.chomd( file )

  22. 终止当前进程

      os.exit()

  23. 获取文件大小

      os.path.getsize( filename )

. 文件操作

  1. 创建空文件

     os.mknod("test.txt")

  2. 直接打开一个文件, 如果文件不存在则创建文件

     fp = open("text.txt", w)  

     关于 open 模式:

         w    以 写方式打开

         a    以追加模式打开( 从 EOF 开始, 必要时创建新文件)

         r+   以读写模式打开

         w+   以读写模式打开 (参见 w)

         a+   以读写方式打开 (参见 a)

         rb   以二进制读模式打开

         wb   以二进制写模式打开(参见 w)

         ab   以二进制追加模式打开(参见 a)

         rb+  以二进制读写模式打开 (参见 r+)

         wb+  以二进制读写模式打开( 参见 w+ )

         ab+  以二进制读写模式打开( 参见 a+)

r   以只读模式打开文件

w   以只写模式打开文件，且先把文件内容清空（truncate the file first）

a   以添加模式打开文件，写文件的时候总是写到文件末尾，用seek也无用。打开的文件也是不能读的

r+  以读写方式打开文件，文件可读可写，可写到文件的任何位置

w+ 和r+不同的是，它会truncate the file first

a+ 和r+不同的是，它只能写到文件末尾

  3. 读取指定长度字节的内容

     fp.read([size])        # size 为读取的长度, 以 byte 为单位

  4. 读取文件内容

     fp = open(filename)
     buf = fp.read()       # 注意, 读取应该没问题, 但是显示会有中文问题

     print(buf)            # 如果有中文, 会显示为乱码。

  5. 判断文件是否存在

     if not os.access( filename, os.F_OK ):
        return False             # 文件不存在

  6. 写文件

     fp.write(str)                      #把str写到文件中，write()并不会在str后加上一个换行符

  7. windows下python检查文件是否被其它文件打开.md

     http://www.cnblogs.com/plwang1990/p/5863560.html

     http://stackoverflow.com/questions/8231719/how-to-check-whether-a-file-is-open-and-the-open-status-in-python

     from ctypes import cdll
import os

_sopen = cdll.msvcrt._sopen
_close = cdll.msvcrt._close
_SH_DENYRW = 0x10

def is_open(filename):
    if not os.access(filename, os.F_OK):
        return False # file doesn't exist
    h = _sopen(filename, 0, _SH_DENYRW, 0)
    if h == 3:
        _close(h)
        return False # file is not opened by anyone else
    return True # file is already open

print is_open("test.txt")

  8. 覆盖文件的某一行或某个位置的内容

     这个功能实际上是先读文件的所有内容, 然后再内存中进行修改后, 再重新返写到文件.

     已经实现了, 参见: file_tools.py->insertContent()