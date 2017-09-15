# coding=gbk
s = "中文"
print s
print len(s)

s1 = u"中文"
s2 = unicode(s,"gbk")	#省略参数将用python默认的ASCII来解码
s3 = s.decode("gbk")	#把str转换成unicode是decode，unicode函数作用与之相同

print len(s1)
print len(s2)
print len(s3)