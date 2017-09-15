. urllib 是一个处理URLs 相关功能的几个模块的集合包. 属于基本库, 不用单独下载安装, Python3 以后, 将urllib , urllib2 合并在一起为urllib了.
  1. urllib.request   打开并读取URLs

  2. urllib.error     urllib.request 的异常

  3. urllib.parse     解析URLs

  4. urllib.robotparser     解析 robots.txt文件

    """
         call back function
         a    downloaded data size
         b    data size
         c  remote file size
    """

-------------------------------------

>>> import urllib.request
>>> help(urllib.request.urlretrieve)
Help on function urlretrieve in module urllib.request:

urlretrieve(url, filename=None, reporthook=None, data=None)
    Retrieve a URL into a temporary location on disk.

    Requires a URL argument. If a filename is passed, it is used as
    the temporary file location. The reporthook argument should be
    a callable that accepts a block number, a read size, and the
    total file size of the URL target. The data argument should be
    valid URL encoded data.

    If a filename is passed and the URL points to a local resource,
    the result is a copy from local file to new file.

    Returns a tuple containing the path to the newly created
    data file as well as the resulting HTTPMessage object.

>>>