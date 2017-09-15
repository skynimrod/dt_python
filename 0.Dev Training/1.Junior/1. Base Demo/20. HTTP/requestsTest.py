#-*- coding:utf8 -*-
import threading,sys
import requests
import time
import os

class DownloadThread(threading.Thread):
    def __init__(self,url,startpos,endpos,f):
        super(DownloadThread,self).__init__()
        self.url = url
        self.startpos = startpos
        self.endpos = endpos
        self.fd = f

    def download(self):
        print("start thread:%s at %s" % (self.getName(), time.time()))
        '''
        # 由于JS 的获取可能cninfo 不处理 if-None-Match, 只返回200, 没有返回304， 所以还是在应用中对ETag 进行判断
        ETag = "2068b64-28f4d-54c93c2ffc9c0"
        
        headers = {"If-None-Match":ETag}
        res = requests.get(self.url,headers=headers)
        print(res.headers)
        print("Thread(%s):%d" % (self.getName(), res.status_code))
        '''
        headers = {"Range":"bytes=%s-%s"%(self.startpos,self.endpos)}
        res = requests.get(self.url,headers=headers)
        #print(res.headers)
        #print("Thread(%s):%d" % (self.getName(), res.status_code))
        # res.text 是将get获取的byte类型数据自动编码，是str类型， res.content是原始的byte类型数据
        # 所以下面是直接write(res.content)
        self.fd.seek(self.startpos)
        self.fd.write(res.content)
        print("stop thread:%s at %s" % (self.getName(), time.time()))
        # f.close()

    def run(self):
        self.download()

'''
/*
 * 2. MulThreadDownload()
 *        多线程下载.
 *    入口参数:
 *        url           需要下载的URL
 *        desfile       下载后的文件存放名称(含路径, 如果没有路径存放在当前路径下)
 *        threadnum     线程数量, 最大为5， 缺省为3
 *    出口参数:
 *        无
 *    返回值:
 *        "" 表示下载失败. 下载则返回对应的ETag, 便于后续判断是否该文件与之前下载的一样, 再决定是否要进行一部处理.
 *    说明:
 *        如果文件大小拆分为5个后, 仍有多余的(), 那么就有可能会有第6个线程启动来处理剩余部分进行下载.
 */
'''
def MultThreadDownload( url, desfile, threadnum = 3 ):
    ret = ""
    filesize = int(requests.head(url).headers['Content-Length'])
    print("%s filesize:%s"%("要下载的文件大小为:",filesize))

    ETag = requests.head(url).headers['ETag']
    print("ETag:%s"%(ETag))
    
    #线程数最大不能超过5个, 缺省为3个
    if ( threadnum > 5 ):
        return ret
    
    #信号量，同时只允许指定个数的线程运行
    threading.BoundedSemaphore(threadnum)
    # 默认3线程现在，也可以通过传参的方式设置线程数
    step = filesize // threadnum
    mtd_list = []
    start, end = 0, -1

    # 请空并生成文件
    tempf = open(desfile,'w')
    tempf.close()
    # rb+ ，二进制打开，可任意位置读写
    with open(desfile,'rb+') as  f:
        fileno = f.fileno()
        # 如果文件大小为11字节，那就是获取文件0-10的位置的数据。如果end = 10，说明数据已经获取完了。
        while end < filesize -1:
            start = end +1
            end = start + step -1
            if end > filesize:
                end = filesize
            # print("start:%s, end:%s"%(start,end))
            # 复制文件句柄
            dup = os.dup(fileno)
            # print(dup)
            # 打开文件
            fd = os.fdopen(dup,'rb+',-1)
            # print(fd)
            t = DownloadThread(url,start,end,fd)
            t.start()
            mtd_list.append(t)

        for i in  mtd_list:
            i.join()    #  http://blog.csdn.net/zhiyuan_2007/article/details/48807761

    return ETag
                        #

if __name__ == "__main__":
    #url = sys.argv[1]
    url = "http://www.cninfo.com.cn/disclosure/fulltext/plate/cyblatest_24h.js"
    ret = MultThreadDownload(url,"./abc.txt",5)
    print(ret)
    '''
    #获取文件的大小和文件名
    filename = url.split('/')[-1]
    filesize = int(requests.head(url).headers['Content-Length'])
    print("%s filesize:%s"%(filename,filesize))

    #线程数
    threadnum = 3
    #信号量，同时只允许3个线程运行
    threading.BoundedSemaphore(threadnum)
    # 默认3线程现在，也可以通过传参的方式设置线程数
    step = filesize // threadnum
    mtd_list = []
    start = 0
    end = -1

    # 请空并生成文件
    tempf = open(filename,'w')
    tempf.close()
    # rb+ ，二进制打开，可任意位置读写
    with open(filename,'rb+') as  f:
        fileno = f.fileno()
        # 如果文件大小为11字节，那就是获取文件0-10的位置的数据。如果end = 10，说明数据已经获取完了。
        while end < filesize -1:
            start = end +1
            end = start + step -1
            if end > filesize:
                end = filesize
            # print("start:%s, end:%s"%(start,end))
            # 复制文件句柄
            dup = os.dup(fileno)
            # print(dup)
            # 打开文件
            fd = os.fdopen(dup,'rb+',-1)
            # print(fd)
            t = DownloadThread(url,start,end,fd)
            t.start()
            mtd_list.append(t)
            print(t)
            print(mtd_list)

        for i in  mtd_list:
            i.join()
    '''
