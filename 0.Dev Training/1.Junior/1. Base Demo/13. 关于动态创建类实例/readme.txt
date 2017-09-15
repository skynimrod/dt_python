. 参见:

      http://www.cnblogs.com/zhangjing0502/archive/2012/05/16/2503702.html

      mysite2 测试项目中的report 部分代码

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


m = __import__('当前所在py名称', globals(), locals(), ['testclass']) 
c = getattr(m, 'testclass') 
myobject = c()

print(myobject)

 