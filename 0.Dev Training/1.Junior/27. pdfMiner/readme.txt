. �μ�:

      http://www.cnblogs.com/jamespei/p/5339769.html

      https://pypi.python.org/pypi/pdfminer/

. PDFMiner ��һ����PDF�ĵ�������Ϣ�Ĺ���. ��������PDF����, ��רע�ڻ�ȡ�������ı�����. PDFMiner ����

. ֧��Python 2.4 +, ��֧��Python 3 ,  pdfminer3k 1.3.1 ��֧��Python 3. ��https://pypi.python.org ����PDF �����ҵ�PDF��صİ�

. һ���ȽϺõ�Demo

    http://denis.papathanasiou.org/posts/2010.08.04.post.html

. pdfminer.six 20160614

  PDFMiner ��չ, ��six��ʾ Python 2+3 ����.

  python setup.py install

  ��װ��ʱ���ͬʱ��װ��Ҫ�İ�: ply>=3.4(װ����3.9), pytest>=2.0(װ����3.0.4),  colorama(0.3.7), py>=1.4.29(װ����1.4.31)

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

. Ϊ��֧��CJK ����(Ҳ�������պ�����)�� ��װ֮ǰ��Ҫһ�����ӵĲ���:

# make cmap
python tools/conv_cmap.py pdfminer/cmap Adobe-CNS1 cmaprsrc/cid2code_Adobe_CNS1.txt
reading 'cmaprsrc/cid2code_Adobe_CNS1.txt'...
writing 'CNS1_H.py'...
...
(this may take several minutes)

# python setup.py install

����windows ����, �����������:

mkdir pdfminer\cmap
python tools\conv_cmap.py -c B5=cp950 -c UniCNS-UTF8=utf-8 pdfminer\cmap Adobe-CNS1 cmaprsrc\cid2code_Adobe_CNS1.txt
python tools\conv_cmap.py -c GBK-EUC=cp936 -c UniGB-UTF8=utf-8 pdfminer\cmap Adobe-GB1 cmaprsrc\cid2code_Adobe_GB1.txt
python tools\conv_cmap.py -c RKSJ=cp932 -c EUC=euc-jp -c UniJIS-UTF8=utf-8 pdfminer\cmap Adobe-Japan1 cmaprsrc\cid2code_Adobe_Japan1.txt
python tools\conv_cmap.py -c KSC-EUC=euc-kr -c KSC-Johab=johab -c KSCms-UHC=cp949 -c UniKS-UTF8=utf-8 pdfminer\cmap Adobe-Korea1 cmaprsrc\cid2code_Adobe_Korea1.txt
python setup.py install

ʵ�����и�build_cmap.py��ֱ����������ļ�����. python build_cmap.py

���Դ�����һ������ļ���, �������ܲ�, ��ȫ����������Ҫ, �ر��Ǳ�����û�д���, ��ɱ��ÿһ����Ԫ������ݶ�ռ����һ��, �������Դ���....

�������ð�ԭ���Ĳ�Ʒ������ֲ.