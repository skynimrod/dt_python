�μ�:

   Python 3.4.2 documentation -> The Python Standard Library -> Built-in Types->Sequence Types  �� Lists ����

   http://www.cnblogs.com/zhengyuxin/articles/1938300.html

. 1. �����б����ظ����ֵ���ĸ���

items = ['trailer<<', 'Size 97 ', 'Root 1 0 R ', 'Info 3 0 R ', 'test','test','test']
for item in items:
    print(item)

l = len(items)//3
print(l)
for i in range(0, l ):
    print(items[i])

c = items.count("test")
print(c)


  
. 2. ȥ�� list ���ظ���Ԫ��

   aa = [1, 2, 2, 3, 2, 4]

   bb = list(set(aa))    # [1,2,3,4]

. 3. �б������

   aa  = [3,2,1,5,2]

   bb = sorted(aa)
  
   print(bb)

        with open("F:/F_t_tmp/tmp1/xrefAll.txt","w") as fs:
            fs.write("len(xref) = %d\r\n" % len(xref) )
            for key in sorted(xref.keys()):
                buf =  self.getObjContent( key, xref )
                #print(key)
                #print(type(key))
                fs.write( key + "||" +buf + "\r\n\r\n" ) 

. 4. ɾ���б��е�һ�γ��ֵ�ֵ

    l1 = [2,3,2,"hello"]
    print(l1)
    l1.remove(2)
    print(l1)

. 5. list �ϲ���ȥ���ظ���Ȼ������

    la = [38,48,68,98,109]
    lb = [38,48,59,89,110]

    lc = sorted(set(la + lb))

    print(la)
    print(lb)
    print(lc)
    print(type(lc))

