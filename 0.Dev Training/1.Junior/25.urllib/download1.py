import urllib.request

def urlcallback( a, b, c ):
    """
         call back function
         a    downloaded data size
         b    data size
         c  remote file size
    """
    print('callback')
    prec = 100.0*a*b/c
    if 100<prec:
        prec = 100
    print("%.2f%%" % prec, end = '' )


f = urllib.request.urlretrieve('http://www.cninfo.com.cn/disclosure/fulltext/plate/shmblatest_24h.js',
                       filename='f:/f_3_test/3_Python/text.txt',
                    reporthook = urlcallback )

