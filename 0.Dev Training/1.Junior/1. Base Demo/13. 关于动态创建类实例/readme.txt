. �μ�:

      http://www.cnblogs.com/zhangjing0502/archive/2012/05/16/2503702.html

      mysite2 ������Ŀ�е�report ���ִ���

.    print('-------------------------------------------')
    tt = __import__('report.reportlist.downloadReportList',
                    globals(),locals,['test'])

    test = tt.test

    print(tt)
    test.showname()
    print('===============')

    tt.getReportList(reportUrls, desDir)


. class testclass():
    name = ""
    def setname(self, strs):
        self.name = strs
        
    def show(self):
        print(self.name)


m = __import__('��ǰ����py����', globals(), locals(), ['testclass']) 
c = getattr(m, 'testclass') 
myobject = c()

print(myobject)

 