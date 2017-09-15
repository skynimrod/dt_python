�μ�:

     http://www.cnblogs.com/rollenholt/archive/2012/04/23/2466179.html

     Python 2.7.12 document->The Python Standard Library ->File Formats, File and Directory Access

. Python �ж��ļ����ļ���(�ļ���������)�Ĳ�����Ҫ�漰��osģ���shutilģ��.

. 1. ��õ�ǰ����Ŀ¼

     os.getcwd()

  2. ���ָ��Ŀ¼�µ������ļ���Ŀ¼��

     os.listdir()

  3. ɾ��һ���ļ�

     os.remove()

  4. ɾ�����Ŀ¼

     os.removedirs( r "c:\python")

  5. �жϸ�����·���Ƿ���һ���ļ�

     os.path.isfile()

  6. �жϸ�����·���Ƿ���һ��Ŀ¼

     os.path.isdir()

  7. �ж��ƺ����Ǿ���·��

     os.path.isabs()

  8. ��������·��(���ļ�)�Ƿ����

     os.path.exists()

  9. ����һ��·����Ŀ¼�����ļ���

     os.path.split()

     ����: os.path.split('/home/swaroop/byte/code/pem.txt')   ���:('/home/swaroop/byte/code', 'poem.txt')

  10. ������չ��

     os.path.splitext()

  11. ��ȡ·����

      os.path.dirname()

  12. ��ȡ�ļ���

      os.path.basename()

  13. ����shell����

      os.system()

  14. ��ȡ�����û�������

      os.getenv()  ��  os.putenv(0

  15. ������ǰƽ̨ʹ�õ�����ֹ��

      os.linesep       Windowsʹ��'\r\n', Linux ʹ��'\n'   �� Mac ʹ�� '\r'

  16. ָʾ������ʹ�õ�ƽ̨:

      os.name     ����Windows, ����'nt', ������ Linux/Unix �û��� ���� 'posix'

  17. ������

      os.rename( old, new )

  18. �����༶Ŀ¼

      os.makedirs(r "c:\python\test")

  19. ��������Ŀ¼

      os.mkdir( "test" )

  20. ��ȡ�ļ�����

      os.stat( file )

  21. �޸��ļ�Ȩ����ʱ���

      os.chomd( file )

  22. ��ֹ��ǰ����

      os.exit()

  23. ��ȡ�ļ���С

      os.path.getsize( filename )

. �ļ�����

  1. �������ļ�

     os.mknod("test.txt")

  2. ֱ�Ӵ�һ���ļ�, ����ļ��������򴴽��ļ�

     fp = open("text.txt", w)  

     ���� open ģʽ:

         w    �� д��ʽ��

         a    ��׷��ģʽ��( �� EOF ��ʼ, ��Ҫʱ�������ļ�)

         r+   �Զ�дģʽ��

         w+   �Զ�дģʽ�� (�μ� w)

         a+   �Զ�д��ʽ�� (�μ� a)

         rb   �Զ����ƶ�ģʽ��

         wb   �Զ�����дģʽ��(�μ� w)

         ab   �Զ�����׷��ģʽ��(�μ� a)

         rb+  �Զ����ƶ�дģʽ�� (�μ� r+)

         wb+  �Զ����ƶ�дģʽ��( �μ� w+ )

         ab+  �Զ����ƶ�дģʽ��( �μ� a+)

r   ��ֻ��ģʽ���ļ�

w   ��ֻдģʽ���ļ������Ȱ��ļ�������գ�truncate the file first��

a   �����ģʽ���ļ���д�ļ���ʱ������д���ļ�ĩβ����seekҲ���á��򿪵��ļ�Ҳ�ǲ��ܶ���

r+  �Զ�д��ʽ���ļ����ļ��ɶ���д����д���ļ����κ�λ��

w+ ��r+��ͬ���ǣ�����truncate the file first

a+ ��r+��ͬ���ǣ���ֻ��д���ļ�ĩβ

  3. ��ȡָ�������ֽڵ�����

     fp.read([size])        # size Ϊ��ȡ�ĳ���, �� byte Ϊ��λ

  4. ��ȡ�ļ�����

     fp = open(filename)
     buf = fp.read()       # ע��, ��ȡӦ��û����, ������ʾ������������

     print(buf)            # ���������, ����ʾΪ���롣

  5. �ж��ļ��Ƿ����

     if not os.access( filename, os.F_OK ):
        return False             # �ļ�������

  6. д�ļ�

     fp.write(str)                      #��strд���ļ��У�write()��������str�����һ�����з�

  7. windows��python����ļ��Ƿ������ļ���.md

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

  8. �����ļ���ĳһ�л�ĳ��λ�õ�����

     �������ʵ�������ȶ��ļ�����������, Ȼ�����ڴ��н����޸ĺ�, �����·�д���ļ�.

     �Ѿ�ʵ����, �μ�: file_tools.py->insertContent()