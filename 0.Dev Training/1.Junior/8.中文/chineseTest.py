# coding=gbk
s = "����"
print s
print len(s)

s1 = u"����"
s2 = unicode(s,"gbk")	#ʡ�Բ�������pythonĬ�ϵ�ASCII������
s3 = s.decode("gbk")	#��strת����unicode��decode��unicode����������֮��ͬ

print len(s1)
print len(s2)
print len(s3)