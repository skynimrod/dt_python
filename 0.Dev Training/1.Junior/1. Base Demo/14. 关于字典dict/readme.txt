参见:

     http://www.cnblogs.com/yangyongzhi/archive/2012/09/17/2688326.html

     http://www.cnblogs.com/sysu-blackbear/p/3283993.html

     Python 3.4.2 documentation ->The Python Standard Library -> Built-in Types ->Mapping Types--dict

. 1. 判断字典中是否已经存在指定的内容

dict = {"a" : "apple", "b" : "banana", "c" : "grape", "d" : "orange"}
#输出key的列表
print(dict.keys())
#输出value的列表
print (dict.values())

if ("apple" in dict.values()):
    print("find it")

dict = {"a" : 1, "b" : 2, "c" : 3, "d" : 4}
#输出key的列表
print(dict.keys())
#输出value的列表
print (dict.values())

if ( 1 in dict.values()):
    print("find it again")

. 2. 删除字典中的内容

  del(dict['a'])

. 3. 关于排序

   python 字典（dict）的特点就是无序的，按照键（key）来提取相应值（value），如果我们需要字典按值排序的话，那可以用下面的方法来进行：

   3.1 下面的是按照value的值从大到小的顺序来排序。

   dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
   dict= sorted(dic.iteritems(), key=lambda d:d[1], reverse = True)
   print dict

   输出的结果：
   [('aa', 74), ('a', 31), ('bc', 5), ('asd', 4), ('c', 3), ('d', 0)]

   下面我们分解下代码
    print dic.iteritems() 得到[(键，值)]的列表。
    然后用sorted方法，通过key这个参数，指定排序是按照value，也就是第一个元素d[1的值来排序。reverse = True表示是需要翻转的，默认是从小到大，翻转的话，那就是从大到小。

   3.2 对字典按键（key）排序：

   dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}
   dict= sorted(dic.iteritems(), key=lambda d:d[0]) d[0]表示字典的键,   d[1] 表示字典的值

   print dict


   3.3  第三种排序方法

    d = {4:2, 3:3, 2:18, 5:"hello", 6:2, 7:2}
    r_dict = lambda _dict:dict(val[::-1] for val in _dict.items())
    r_dict(r_dict(d))
    print(d)

   3.4. 更加精度高的排序匹配

    colMap = {1: {'w': 105.98, 'x': 84.864}, 2: {'w': 52.68, 'x': 191.45}, 3: {'w': 52.8, 'x': 244.61}, 4: {'w': 52.824, 'x': 297.89}, 5: {'w': 52.68, 'x': 351.19}, 6: {'w': 52.824, 'x': 404.47}, 7: {'w': 52.8, 'x': 457.78}, 8: {'w': 52.8, 'x': 84.864}, 9: {'w': 52.704, 'x': 138.14}, 10: {'w': 106.1, 'x': 244.61}}    
    print("===================")
    for k,v in sorted( colMap.items(), key=lambda d:d[0] ):
        print(k)
        print(v)

    print("===================")
    for k,v in sorted( colMap.items(), key=lambda d:d[1]['w'] ):   # 按照 colMap[1]['w']进行排序
        print(k)
        print(v)


. 4. 遍历 字典

        with open("F:/F_t_tmp/tmp/Rowpages.txt","rw") as fs:
            for key in pages: 
                buf =  self.getObjContent( pages[key], xref )
                fs.writeChars( item.value + "|" + buf + "\r\n\r\n" ) 
        
    对于Key值是整数的情况, 遍历的时候:

    dd = {1: '1:550.2,51.65', 2: '2:517.668,51.65'}

    for k,v in sorted(dd.items(), key=lambda d:d[0]):
        xy = dd[k].split(":")[1].split(" ")
        print(xy)

    如果直接用 
    for k,v in dd:
        xy = dd[k].split(":")[1].split(" ")
        print(xy)

     会提示: 

    Traceback (most recent call last):
      File "file_tools.py", line 302, in <module>
        for k,v in dd:
    TypeError: 'int' object is not iterable                

. 5. 字典合并

    update([other])
    将字典other中的元素加到dict中，key重复时将用other中的值覆盖
    Python代码  
    d = {"name":"nico", "age":23}  
    d2 = {"name":"jack", "abcd":123}  
    d.update(d2)  
    print d     #{'abcd': 123, 'age': 23, 'name': 'jack'}  

. 6. 判断字典中是否有指定的key

        if ( "curpos" in tmpmap.keys() ):
            del(tmpmap["curpos"])

. 7. 删除字典中value 重复的项

    d = {4:2, 3:3, 2:18, 5:"hello", 6:2, 7:2}
    t = {}
    for k in d.keys():
        if v not in t.values():
            t[k] = d[k]
    print(t)

. 8. 字典的key不能使字典, 如下面的情况是错误的:

    d2 = {{"x":1,"y":2}:2, {"x":3,"y":3}:3}
    print(d2)

Traceback (most recent call last):
  File "file_tools.py", line 300, in <module>
    d2 = {{"x":1,"y":2}:2, {"x":3,"y":3}:3}
TypeError: unhashable type: 'dict'

. 9. 判断2个dict是否相同

    d1 = {"ox":1, "oy":2}
    d2 = {"ox":1, "oy":3}
    if ( d1 == d2 ):
        print("Equal")

. 10. 清空字典的内容

   参见:

       http://www.pythontab.com/html/2013/pythonjichu_0507/385.html

   是用

       dict ={"a":1, "b":2}
       x = dict

       x.clear()    # 这个方法非常好, 会直接清空x和dict . 如果直接赋值{}, 那么dict 实际上是没有清空的，只是清空了x   
   
. 11. 拼接字符串列表

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
   
    
 
