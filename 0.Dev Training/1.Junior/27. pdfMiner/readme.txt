. 参见:

      http://www.cnblogs.com/jamespei/p/5339769.html

      https://pypi.python.org/pypi/pdfminer/

. PDFMiner 是一个从PDF文档解析信息的工具. 不像其他PDF工具, 它专注于获取并分析文本数据. PDFMiner 允许

. 支持Python 2.4 +, 不支持Python 3 ,  pdfminer3k 1.3.1 才支持Python 3. 在https://pypi.python.org 搜索PDF 可以找到PDF相关的包

. 一个比较好的Demo

    http://denis.papathanasiou.org/posts/2010.08.04.post.html

. pdfminer.six 20160614

  PDFMiner 扩展, 用six表示 Python 2+3 兼容.

  python setup.py install

  安装的时候会同时安装需要的包: ply>=3.4(装的是3.9), pytest>=2.0(装的是3.0.4),  colorama(0.3.7), py>=1.4.29(装的是1.4.31)

. (env3) E:\E_1_Developement Tools\7 Python\0.Dev Training\1.Junior\27. pdfMiner\p
dfminer3k-1.3.1\pdfminer3k-1.3.1>python tools/pdf2txt.py samples/simple1.pdf
Hello

World

Hello

World

H e l l o

W o r l d

H e l l o

W o r l d

. 为了支持CJK 语言(也就是中日韩语言)， 安装之前需要一个附加的步骤:

# make cmap
python tools/conv_cmap.py pdfminer/cmap Adobe-CNS1 cmaprsrc/cid2code_Adobe_CNS1.txt
reading 'cmaprsrc/cid2code_Adobe_CNS1.txt'...
writing 'CNS1_H.py'...
...
(this may take several minutes)

# python setup.py install

对于windows 机器, 用下面的命令:

mkdir pdfminer\cmap
python tools\conv_cmap.py -c B5=cp950 -c UniCNS-UTF8=utf-8 pdfminer\cmap Adobe-CNS1 cmaprsrc\cid2code_Adobe_CNS1.txt
python tools\conv_cmap.py -c GBK-EUC=cp936 -c UniGB-UTF8=utf-8 pdfminer\cmap Adobe-GB1 cmaprsrc\cid2code_Adobe_GB1.txt
python tools\conv_cmap.py -c RKSJ=cp932 -c EUC=euc-jp -c UniJIS-UTF8=utf-8 pdfminer\cmap Adobe-Japan1 cmaprsrc\cid2code_Adobe_Japan1.txt
python tools\conv_cmap.py -c KSC-EUC=euc-kr -c KSC-Johab=johab -c KSCms-UHC=cp949 -c UniKS-UTF8=utf-8 pdfminer\cmap Adobe-Korea1 cmaprsrc\cid2code_Adobe_Korea1.txt
python setup.py install

实际上有个build_cmap.py，直接运行这个文件即可. python build_cmap.py

尝试处理了一个公告的季报, 处理结果很差, 完全不能满足需要, 特别是表格根本没有处理, 造成表格每一个单元格的内容都占用了一行, 基本难以处理....

看来还得把原来的产品进行移植.