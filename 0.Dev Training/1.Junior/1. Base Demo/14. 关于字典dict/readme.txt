�μ�:

     http://www.cnblogs.com/yangyongzhi/archive/2012/09/17/2688326.html

     http://www.cnblogs.com/sysu-blackbear/p/3283993.html

     Python 3.4.2 documentation ->The Python Standard Library -> Built-in Types ->Mapping Types--dict

. 1. �ж��ֵ����Ƿ��Ѿ�����ָ��������

dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"}
#���key���б�
print(dict.keys())
#���value���б�
print (dict.values())

if ("apple" in dict.values()):
    print("find it")

dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4}
#���key���б�
print(dict.keys())
#���value���б�
print (dict.values())

if ( 1 in dict.values()):
    print("find it again")

. 2. ɾ���ֵ��е�����

  del(dict['a'])

. 3. ��������

   python �ֵ䣨dict�����ص��������ģ����ռ���key������ȡ��Ӧֵ��value�������������Ҫ�ֵ䰴ֵ����Ļ����ǿ���������ķ��������У�

   3.1 ������ǰ���value��ֵ�Ӵ�С��˳��������

   dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
   dict= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
   print dict

   ����Ľ����
   [('aa', 74), ('a', 31), ('bc', 5), ('asd', 4), ('c', 3), ('d', 0)]

   �������Ƿֽ��´���
    print dic.iteritems() �õ�[(����ֵ)]���б�
    Ȼ����sorted������ͨ��key���������ָ�������ǰ���value��Ҳ���ǵ�һ��Ԫ��d[1��ֵ������reverse = True��ʾ����Ҫ��ת�ģ�Ĭ���Ǵ�С���󣬷�ת�Ļ����Ǿ��ǴӴ�С��

   3.2 ���ֵ䰴����key������

   dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
   dict= sorted(dic.iteritems(), key=lambda d:d[0]) d[0]��ʾ�ֵ�ļ�,   d[1] ��ʾ�ֵ��ֵ

   print dict


   3.3  ���������򷽷�

    d = {4:2, 3:3, 2:18, 5:"hello", 6:2, 7:2}
    r_dict = lambda _dict:dict(val[::-1] for val in _dict.items())
    r_dict(r_dict(d))
    print(d)

   3.4. ���Ӿ��ȸߵ�����ƥ��

    colMap = {1: {'w': 105.98, 'x': 84.864}, 2: {'w': 52.68, 'x': 191.45}, 3: {'w': 52.8, 'x': 244.61}, 4: {'w': 52.824, 'x': 297.89}, 5: {'w': 52.68, 'x': 351.19}, 6: {'w': 52.824, 'x': 404.47}, 7: {'w': 52.8, 'x': 457.78}, 8: {'w': 52.8, 'x': 84.864}, 9: {'w': 52.704, 'x': 138.14}, 10: {'w': 106.1, 'x': 244.61}}    
    print("===================")
    for k,v in sorted( colMap.items(), key=lambda d:d[0] ):
        print(k)
        print(v)

    print("===================")
    for k,v in sorted( colMap.items(), key=lambda d:d[1]['w'] ):   # ���� colMap[1]['w']��������
        print(k)
        print(v)


. 4. ���� �ֵ�

        with open("F:/F_t_tmp/tmp/Rowpages.txt","rw") as fs:
            for key in pages: 
                buf =  self.getObjContent( pages[key], xref )
                fs.writeChars( item.value + "|" + buf + "\r\n\r\n" ) 
        
    ����Keyֵ�����������, ������ʱ��:

    dd = {1: '1:550.2,51.65', 2: '2:517.668,51.65'}

    for k,v in sorted(dd.items(), key=lambda d:d[0]):
        xy = dd[k].split(":")[1].split(" ")
        print(xy)

    ���ֱ���� 
    for k,v in dd:
        xy = dd[k].split(":")[1].split(" ")
        print(xy)

     ����ʾ: 

    Traceback (most recent call last):
      File "file_tools.py", line 302, in <module>
        for k,v in dd:
    TypeError: 'int' object is not iterable                

. 5. �ֵ�ϲ�

    update([other])
    ���ֵ�other�е�Ԫ�ؼӵ�dict�У�key�ظ�ʱ����other�е�ֵ����
    Python����  
    d = {"name":"nico", "age":23}  
    d2 = {"name":"jack", "abcd":123}  
    d.update(d2)  
    print d     #{'abcd': 123, 'age': 23, 'name': 'jack'}  

. 6. �ж��ֵ����Ƿ���ָ����key

        if ( "curpos" in tmpmap.keys() ):
            del(tmpmap["curpos"])

. 7. ɾ���ֵ���value �ظ�����

    d = {4:2, 3:3, 2:18, 5:"hello", 6:2, 7:2}
    t = {}
    for k in d.keys():
        if v not in t.values():
            t[k] = d[k]
    print(t)

. 8. �ֵ��key����ʹ�ֵ�, �����������Ǵ����:

    d2 = {{"x":1,"y":2}:2, {"x":3,"y":3}:3}
    print(d2)

Traceback (most recent call last):
  File "file_tools.py", line 300, in <module>
    d2 = {{"x":1,"y":2}:2, {"x":3,"y":3}:3}
TypeError: unhashable type: 'dict'

. 9. �ж�2��dict�Ƿ���ͬ

    d1 = {"ox":1, "oy":2}
    d2 = {"ox":1, "oy":3}
    if ( d1 == d2 ):
        print("Equal")

. 10. ����ֵ������

   �μ�:

       http://www.pythontab.com/html/2013/pythonjichu_0507/385.html

   ����

       dict ={"a":1, "b":2}
       x = dict

       x.clear()    # ��������ǳ���, ��ֱ�����x��dict . ���ֱ�Ӹ�ֵ{}, ��ôdict ʵ������û����յģ�ֻ�������x   
   
. 11. ƴ���ַ����б�

    signature   = "signature"
    timestamp   = "timestamp"
    nonce       = "nonce"
    echostr     = "echostr"

    token = "rMoonSta1234oHello1234"
    print("signature=%s,timestamp=%s,nonce=%s,echostr=%s" % (signature, timestamp, nonce, echostr ) )

    al = [ token, timestamp, nonce ]

    print(al)
    a2 = sorted(al)

    print(a2)
    tmp = ''.join(a2)
    print(tmp)
   
    
 
