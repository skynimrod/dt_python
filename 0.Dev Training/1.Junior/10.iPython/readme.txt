. ��Windows �а�װIPython ��setuptools

  ��IPython�Ĺ�����������������Python 2 �� Python 3 �Ķ�����Windows ��װ�ļ�. ���尲װ���̲��� 

      http://ipython.org/ipython-doc/stable/install/install.html#windows

  �� https://pypi.python.org/pypi/setuptools#files ��� setuptools �İ�װ�ļ�����ɰ�װ. ֮�������װpip. ���岽������:

    cd  c:\python27\scripts

    python .\easy_install-27-script.py pip

. ��װ

  Ҫ�� Python 2.7 ���� 3.3+

      pip install "ipython[all]"

  �����װ����, �����ز���װIPython �Լ���Ҫ�Ŀ�ѡ������֧�� notebook, qtconsole, tests,�Լ�����һЩ����. ��һЩ����(����Qt, PyQt�� pandoc��) ����ͨ��pip ��װ. 

  ���԰�װ���:

  iptest

  ���������װipython ���� �����������:

  pip install ipython

. 

. IPython ��һ��Python �Ľ���ʽ shell , ��Ĭ�ϵ�python shell ���õĶ�, ֧�ֱ����Զ���ȫ, �Զ�����, ֧�� bash shell ����, �������������õĹ��ܺ���.  �� ubuntu �� ֻҪ sudo apt-get install ipython ��װ����, ͨ��ipython ����. 

. ������ ipython �м����򵥺��õ�magic ����

  %bg function�� function �ŵ���ִ̨��.  ����: %bg myfunc(x, y, z = 1), ֮������� jobs ������ȡ��.  myvar = jobs.result(5) �� myvar = jobs[5].result.  ����, jobs.status() ���Բ������������״̬.

  %ed �� %edit �༭һ���ļ���ִ��, ���ֻ�༭��ִ��, �� ed -x filename ���ɡ�

  %env  ��ʾ��������

  %hist  �� %history ��ʾ��ʷ��¼

  %macro name n1-n2 n3-n4 ... n5 .. n6 ...  ����һ������Ϊname �ĺ�, ִ��name ����ִ�� n1-n2 n3-n4 ... n5 ... n6 .. ��Щ����

  %pwd  ��ʾ��ǰĿ¼

  %pycat filename ���﷨������ʾһ��python �ļ�(���ü� .py ��׺��)

  %save filename n1-n2 n3-n4 ... n5 ... n6 ... ��ִ�й�����뱣��Ϊ�ļ�

  %time statement  ����һ�δ����ִ��ʱ��

  %timeit statement �Զ�ѡ���ظ���ѭ����������һ�δ����ִ��ʱ��, ̫������

  ����, ipython ���� ! ��ʾִ��shell ����, �� $ ��python �ı���ת��Ϊshell ����.  ͨ������������, ���ǾͿ���������shell ����֮��Ľ���, k����ǳ����������ิ�ӵĹ���. ��������Ժܷ���Ĵ���һ��Ŀ¼:

  for i in range(10):
    
       s = "dir%s" % i
       !mkdir $s

  ����д���ϻ�����һЩ����, $����ֻ�ܸ�������, ����ֱ��д���ӱ��ʽ, $"dir%s"%i ���Ǵ����д����, ����Ҫ����ȫ���� python �ı����Ժ�����.  ��������÷�Ҳ�Ǵ����:

     for i in !ls: print i

   ����дΪ:

     a = !ls
     
     for i in a: print i

   ����һ����Ҫ˵��, ����ִ����ͨ��shell �����������$ �Ļ���Ҫ������ $. ����ԭ����echo $PAHT���ڵ�д�� $echo$$PATH

   �ڽ��µ�ipython �汾��, ����� ipython notebook �Ĺ���, �ֲ���ipython shell �´��벻�ױ����ȱ��, ������ʹ�� --pylab inline ѡ���, �����ڴ���ִ�к�������ʾ���н��(����ͼƬ, ���ݱ���), ��������ݷ���������ʮ�ֹ㷺. 

. �� IPython �� pylab ģʽ��, ����ʹ�� help �����NumPy�������ֲ�ҳ��. �㲢����Ҫ֪�����к���������, ��Ϊ�����ڼ��������ַ�����Tab �� �����Զ���ȫ. ����:

  In [2]: help ar<Tab>
      
     ��������ar ��ͷ�ĺ�������

  In [2]: help arrange

