. 编写技术资料少不了输入数学公式, Notebook 使用MathJax 将输入的LaTeX 文本转换为数学公式.  由于 MathJax 库较大, m诶有继承到IPython 中， 而是直接从MathJax 官网载入, 因此如果计算机没有联网, 就无法正确显示数学公式. 为了解决这个问题, 可以在单元中输入如下程序, 它将会下载MathJax 到本地硬盘.

  from IPython.external.mathjax import install_mathjax, default_dest
  install_mathjax()

  MathJax 完全解压之后, 约需100MB 空间, 其中大都是为旧版浏览器准备的PNG 字体图像文件.  执行下面的语句可以快死删除存放PNG字体图片的文件夹

  from os import path
  import shutil

  png_path = path.join( default_dest, "fonts/HTML-CSS/TeX/png")
  shutil.rmtree( png_path )

  运行完上面的命令之后, 在命令模式下 按m 键将单元样式切换到Markdown. 然后输入如下LaTeX文本:

     $e^{i\pi} + 1 = 0$

  按 Shift+Enter 快捷键之后, 其内容将被转成数学公式显示: e的 i牌次方 +1 = 0 

   