�μ�:

    http://www.jb51.net/article/47956.htm    ��ȫ

    http://www.cnblogs.com/huangcong/archive/2011/08/29/2158268.html

. 1. �ַ�������

     str = 'a string test'
     l = len(str)

. 2. ����ת�ַ���

     str = " a test string"
     n = 34
     ret = str + "%d" % n

. 3. �ж��ַ������Ƿ���ָ�������ַ���

     buf = "hello world"
     item = "hello"
     if (item not in buf):
         print("û��"+buf)
     else:
         print("��"+item)

. 4. ��ȡ�ַ������Ӵ�

     str = "hello world"

     substr = str[:4]    # "hell"

. 5. �ָ��ַ���

     str = "��ľ�ɷݣ��״ι�������A�������깺�������ǩ�ʹ���"

     print( str.split("��")[0])    # ���� "��ľ�ɷ�", ע��: ����ķָ�������ʹ����, Ҳ����˵��ʵ�Ǹ��ַ���

. 6. �����ַ���ת����

     buf = "18"

     n = int( buf )
 
     16�����ַ��� ת����

     buf = 'ff'
     n = int(buf, 16)    # �����255

. 7. ��Сдת��

     http://www.centoscn.com/python/2013/0807/1127.html

     buf = "abcdE"

     buf.upper()

     buf.lower()

. 8. �ַ����滻
    
     buf = "�� �� ��"
     buf = buf.replace(' ', '')     # ɾ���ո�

. 9. ɾ���ַ���ǰ��Ŀո�

     a = "  aasdf  "
     b = a.strip()    # ɾ��ǰ��Ŀո�
     b = a.lstrip()   # ɾ����ߵĿո�
     b = a.rstrip()   # ɾ������Ŀո�

. 10. ��ȡָ���ַ�֮����Ӵ�

      p1, p2 = tmp[i].index('['),  tmp[i].index(']')    # ��ȡ'[' , ']' ��λ��
      buf = tmp[i][ p1+1 : p2 ].strip()     # ȡ�������е�����

     ���Ҫ��ȡ���з���ָ���ַ������Ӵ�, ��Ҫ��������ʽ

            reg = re.compile(r'(\(.+?\))')      # ����Ҫ������ı���Ϣ��������ʽ
            l = re.findall( reg, buf )          # ���ؽ���Ǹ�List, ����ͬ

            print(" ����Ҫ������ı�����%d" % len(l) )
            for item in l:   #  ������ȡ����Ҫ������ı���Ϣ
                retbuf += item

. 11. ���ڿ��ַ���, ���ַ����ж���False

    a = ""
    if ( a ):
        print(" ���ַ�����True")
    else:
        print(" ���ַ�����False")

   ���н��:

      ���ַ�����False

. 12. ������2���ַ��������ַ����ĳ���

    b = '����a��'
    c = b.encode("utf-8")
    print("b=%s, ����=%d" % (b,len(b) ))
    print("c����=%d" % (len(c) ))
    rl = (len(c)-len(b))/2 + len(b)
    print('������2���ַ�, ��b �ĳ���Ϊ:%d' % rl)

. 13. �̶���������ַ���,������ÿո����

    �μ�:

         http://www.jb51.net/article/65258.htm

    s1 = "ello:"
    s2 = "sdfs "
    s3 = ""
    print("|%s|" % s1.ljust(20))
    print("|%s|" % s2.ljust(20))
    print("|%s|" % s3.ljust(20))

    ���Ҫ�Ҷ���, ����rjust(), ������м������� center()

    ���������·���:

    s1 = "ello:"
    s2 = "sdfs "
    s3 = ""
    print("|%30s|" % s1)
    print("|%-30s|" % s1)
    print("|%30s|" % s2)
    print("|%-30s|" % s2)
    print("|%30s|" % s3)
    print("|%-30s|" % s3)



. 14. �̶������������, ������ÿո����

    a = 18
    print("%-8d" % a)      # �����, �������ÿո����
    print("%8d" % a)       # �Ҷ���, �������ÿո����


. 15. �̶������������, ������ÿո����

    f = 18.2
    print("%-8.2f" % f)     # �����, �������ÿո����
    print("%8.2f" % f)      # �Ҷ���, �������ÿո����

. 16. ɾ���ַ�����ָ�����ַ�

    
. 17. ��ʽ������ַ���

   str1 = "sttr1"
   d1 = 2

   buf = "%s. --> %d" % (str1, d1)
    
