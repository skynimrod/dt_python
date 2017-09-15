参见:

    http://www.jb51.net/article/47956.htm    很全

    http://www.cnblogs.com/huangcong/archive/2011/08/29/2158268.html

. 1. 字符串长度

     str = 'a string test'
     l = len(str)

. 2. 数字转字符串

     str = " a test string"
     n = 34
     ret = str + "%d" % n

. 3. 判断字符串中是否有指定的子字符串

     buf = "hello world"
     item = "hello"
     if (item not in buf):
         print("没有"+buf)
     else:
         print("有"+item)

. 4. 获取字符串的子串

     str = "hello world"

     substr = str[:4]    # "hell"

. 5. 分割字符串

     str = "徕木股份：首次公开发行A股网上申购情况及中签率公告"

     print( str.split("：")[0])    # 返回 "徕木股份", 注意: 这儿的分隔符可以使汉字, 也就是说其实是个字符串

. 6. 数字字符串转数字

     buf = "18"

     n = int( buf )
 
     16进制字符串 转数字

     buf = 'ff'
     n = int(buf, 16)    # 结果是255

. 7. 大小写转换

     http://www.centoscn.com/python/2013/0807/1127.html

     buf = "abcdE"

     buf.upper()

     buf.lower()

. 8. 字符串替换
    
     buf = "中 国 人"
     buf = buf.replace(' ', '')     # 删除空格

. 9. 删除字符串前后的空格

     a = "  aasdf  "
     b = a.strip()    # 删除前后的空格
     b = a.lstrip()   # 删除左边的空格
     b = a.rstrip()   # 删除右面的空格

. 10. 获取指定字符之间的子串

      p1, p2 = tmp[i].index('['),  tmp[i].index(']')    # 获取'[' , ']' 的位置
      buf = tmp[i][ p1+1 : p2 ].strip()     # 取方括号中的内容

     如果要获取所有符合指定字符键的子串, 需要用正则表达式

            reg = re.compile(r'(\(.+?\))')      # 不需要解码的文本信息的正则表达式
            l = re.findall( reg, buf )          # 返回结果是各List, 以下同

            print(" 不需要解码的文本数量%d" % len(l) )
            for item in l:   #  逐条获取不需要解码的文本信息
                retbuf += item

. 11. 关于空字符串, 空字符串判断是False

    a = ""
    if ( a ):
        print(" 空字符串是True")
    else:
        print(" 空字符串是False")

   运行结果:

      空字符串是False

. 12. 中文算2个字符来计算字符串的长度

    b = '中文a书'
    c = b.encode("utf-8")
    print("b=%s, 长度=%d" % (b,len(b) ))
    print("c长度=%d" % (len(c) ))
    rl = (len(c)-len(b))/2 + len(b)
    print('中文算2个字符, 则b 的长度为:%d' % rl)

. 13. 固定长度输出字符串,不足的用空格填充

    参见:

         http://www.jb51.net/article/65258.htm

    s1 = "ello:"
    s2 = "sdfs "
    s3 = ""
    print("|%s|" % s1.ljust(20))
    print("|%s|" % s2.ljust(20))
    print("|%s|" % s3.ljust(20))

    如果要右对齐, 就用rjust(), 如果用中间对齐就用 center()

    或者用如下方法:

    s1 = "ello:"
    s2 = "sdfs "
    s3 = ""
    print("|%30s|" % s1)
    print("|%-30s|" % s1)
    print("|%30s|" % s2)
    print("|%-30s|" % s2)
    print("|%30s|" % s3)
    print("|%-30s|" % s3)



. 14. 固定长度输出整数, 不足的用空格填充

    a = 18
    print("%-8d" % a)      # 左对齐, 不够的用空格填充
    print("%8d" % a)       # 右对齐, 不够的用空格填充


. 15. 固定长度输出整数, 不足的用空格填充

    f = 18.2
    print("%-8.2f" % f)     # 左对齐, 不够的用空格填充
    print("%8.2f" % f)      # 右对齐, 不够的用空格填充

. 16. 删除字符串中指定的字符

    
. 17. 格式化组合字符串

   str1 = "sttr1"
   d1 = 2

   buf = "%s. --> %d" % (str1, d1)
    
