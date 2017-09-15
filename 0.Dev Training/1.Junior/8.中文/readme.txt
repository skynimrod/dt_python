. 关于中文

  参见:

       http://www.cnblogs.com/rollenholt/archive/2011/08/01/2123889.html

  http://www.python.org/peps/pep-0263.html

. 文件保存的编码方式没有用。  如果文件里有非ASCII字符, 需要在第一行或第二行指定编码声明. 例如:

  # coding=gbk
  s = "中文"
  print s

  