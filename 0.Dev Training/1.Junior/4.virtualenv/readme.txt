. ��װ

  pip install virtualenv

. ����/ע��

  Windows : ����Script��Ŀ¼�� Ȼ������  activate/deactivate

. ˵��

   �μ�:

        http://blog.sina.com.cn/s/blog_55646c98010179og.html 

  VirtualEnv  ������һ̨�����ϴ������python ���л���, VirtualEnvWrapper Ϊǰ���ṩ��һЩ�������������ϵķ�װ�� 

. ΪʲôҪ��:

  1. ������Ŀ֮��ĵ���������, ����  A��Ŀ ���� django1.2.5, B ��Ŀ���� django1.3

  2. Ϊ����Ӧ���ṩ����, �ѿ������������⻷�������������������, ����Ҫ�ڷ�������������һ��.

. virtualenv ��ô��

  1. ���� ���⻷��

     virtualenv [env1]

     �ͻ��ڵ�ǰ·���´���һ��env1 ����Ŀ¼�� ����:

E:\t_tmp\test>virtualenv env1
New python executable in E:\t_tmp\test\env1\Scripts\python.exe
Installing setuptools, pip, wheel...done.

E:\t_tmp\test>

     ��env1 ��Ŀ¼��, ����һ��������python  ��������. 


. virtualenvwrapper ��ô��

  1. ��װ

     pip install virtualenvwrapper

     ��������� �ӵ�~/.bash_profile����, �粻���鷳, Ҳ����ÿ�ζ��ֶ�ִ��.

     source /usr/local/bin/virtualenvwrapper.sh

. ��������

  1. ���������⻷��
 
     mkvirtualenv [env1]

         �����������Ǵ���һ���»���, Ĭ�������, ������Ŀ¼��.virtualenv/env1, ���������������Զ������ǰ�װpip, �Ժ�����Ҫ��װ������ʱ��ֱ��ʹ��pip ����.

         ������֮��, zidong�л����û����¹���, �ɿ�����ʾ����Ϊ:

         (env1)$

         ����������°�װ����������Ӱ�쵽�����Ļ���

  2. ��ʾ�û���������װ�İ�

     lssitepackages

  3. �л�����
  
     workon [env]

     ��ʱʹ��"workon ������" ���л����л�, �����������������, ����ʾ��ǰʹ�õĻ���

  4. deactivate  

     �Ƴ���ǰ�Ļ���

  5. cpvirtualenv [source] [dest]

     ����һ�����⻷��

  6. cdvirtualenv [subdir] 

     �ѵ�ǰ����Ŀ¼����Ϊ���ڵĻ���Ŀ¼

  7. cdsitepackages [subdir]

     �ѵ�ǰ����Ŀ¼����Ϊ���ڻ�����sitepackages ·��

  8. add2virtualenv [dir] [dir] 

     ��ָ����Ŀ¼���뵱ǰʹ�õĻ�����path ��, �ⳣʹ�����ڶ��project ����ͬʱʹ��һ���ϴ�Ŀ� �����.

  9. toggleglobalsitepackages -q

     ���Ƶ�ǰ�Ļ����Ƿ�ʹ��ȫ�ֵ�sitepackages Ŀ¼.

. FAQ:

  1. ͨ��pip install virutalenvwrapper ��װ virtualenvwrapper �� �������������л����⿪��������ʱ����ʾworkon ������. Ӧ����virutalenvwrapper ��ص�ִ���ļ�����·��û����ӵ�path �С� 

  ���:

       ����linux ��������, ��Ҫÿ������  source /usr/local/bin/virtualenvwrapper.sh�� ��ô����windows ����, ֻ��Ҫ���ж�Ӧ�� virtualenvwrapper.sh.bat ���ɡ� 

      �������������bat�ļ���ʱ��, ����xp��������, �����һЩ����.  �� bat �ļ�����Ŀ¼Ϊpython 2.7\Scripts, ��װ��Python ����Ѿ���path ����, ����ֱ������. 

E:\t_tmp\test>virtualenvwrapper.sh
Welcome to Git (version 1.9.4-preview20140611)


Run 'git help git' to display the help index.
Run 'git help <command>' to display help for specific commands.
C:\Python27\Scripts\virtualenvwrapper.sh: line 197: mktemp: command not found
touch: creating `': No such file or directory
ERROR: virtualenvwrapper could not create a temporary file name.

  ��������ʾ��֪�� 197�е� mktemp ������windows ������û�С� 

  busybox for windows ������ mktemp ����.  �μ�:

      http://www.zhihu.com/question/21175572?sort=created

  ���URL �ṩ��������õ�С�������. 

      http://www.downloadcrew.com/article/32376-busybox_for_windows    ����������� Windows �汾��busybox

  ���� virtualenvwrapper ������linux �İ汾, ��Ӧ��virtualenvwrapper.sh.bat�ű��е���Щ������linux������,����һЩ���ñ���(����@$֮���), ����ʹ����busybox for windows ������Ҳ���е�����ģ� ��Ϊ������Щ���������⡣

  ����취��, ʹ��virtualenvwrapper-win, ���ص�ַΪ:

       https://pypi.python.org/pypi/virtualenvwrapper-win

       http://www.cnblogs.com/skynet/p/4124763.html        һ����صļ����ĵ�

  ����ʹ�� 

       pip install virtualenvwrapper-win

  �����а�װ

  virtualenvwrapper-win ����װ�� python �ĸ�Ŀ¼����. ��  D:\python34   

  virtualenvwrapper-win��virtualenvwrapper��ʹ�÷�ʽ��ȫһ��.


  ����virtualenv + virtualenvwrapper���Ժܺõ���ɻ������룬��֤��ÿ��Ӧ�õĻ����Ǹɾ��ġ����Ҷ�һ���ɾ��Ļ�������ͨ����

pip freeze > requirements.txt����������Ϣ������requirements.txt�ļ�

pip install -r requirements.txt���Զ����������ز���װ���а�

   ע��, �����װ������ĳ��packageʧ��, �ᵼ�����а�װ��ʧ��, Ϊ��, ��requirements.txt ��ɾ����ʧ�ܵ�package���Ժ���Ե�����װ, ����whl �ȷ�ʽ��

   һ�㶼���� pypi ������. ����:  https://pypi.python.org/pypi/microsofttranslator/0.8

����Ӧ�ò���ַ�������pip�������������һƪ���ܡ�

.  virtualenvwrapper-win ����Ҫ����:

  1. mkvirtualenv <name>

  2. lsvirtualenv           �쿴��ǰ����Щ��������

  3. rmvirtualenv <name>

  4. workon [<name>]

  5. deactivate

  6. add2virtualenv <full or relative path>   

  ��ͳ����

  1. cdproject

  2. cdsitepackages

  3. cdvirtualenv

  4. lssitepackages

  5. setprojectdir <full or relative path>

  6. toggleglobalsitepackages

  7. whereis <file>  
