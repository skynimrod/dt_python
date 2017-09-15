# -*- coding:utf-8  -*-

import os

print('获得当前工作目录' + os.getcwd())

os.listdir('.')       # 列出当前目录下的所有子目录及文件

fname = 'iptest1.txt'
if os.access( fname, os.F_OK ):  # 如果文件存在才删除
    os.remove( fname )		# 删除一个文件

path = "./ada/ee"
if not os.path.exists(path):
    os.makedirs( path )      # 必须用双引号， 用单引号的话会提示错误？？？ 有问题， 运行不能通过， 提示语法错误

path = "./ada/dd"
if not os.path.exists( path ):
    os.mkdir( path )

path = "'./t1/t2/t3'"
if not os.path.exists( path ):
    os.makedirs( path )      # 一次创建多层目录 

if os.path.exists('./ada/ee'):
    print('目录./ada/ee 存在')

path = './ada'
if not os.path.exists( path ):
    os.removedirs( path )       # 递归删除目录. 如果子目录无法删除, 则会抛出异常

if os.path.isfile('iptest2.txt'):
    print('iptest2.txt 是一个文件')

if os.path.isdir('iptest2.txt'):
    print('iptest2.txt 不是一个目录')

if os.path.isabs('./iptest2.txt'):
    print('./iptest2.txt 不是绝对路径')

os.path.split( 'F:/1 Developement Tools/7 Python/0.Dev Training/1.Junior/1.Python Demo/8.文件操作/filetest.py')

os.path.splitext('F:\1 Developement Tools/7 Python/0.Dev Training/1.Junior/1.Python Demo/8.文件操作/filetest.py')

os.path.dirname( 'F:\1 Developement Tools/7 Python/0.Dev Training/1.Junior/1.Python Demo/8.文件操作/filetest.py')

os.path.basename('F:\1 Developement Tools/7 Python/0.Dev Training/1.Junior/1.Python Demo/8.文件操作/filetest.py')

os.system('dir')

pathenv = os.getenv('PATH')
print(pathenv)

print(os.name)

os.stat('E:/E_1_Developement Tools/7 Python/0.Dev Training/1.Junior/1. Base Demo/8.文件操作/filetest.py')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logfile = BASE_DIR + '/log/debug.log'

print(BASE_DIR)
print(logfile)


