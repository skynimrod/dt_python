. urllib ��һ������URLs ��ع��ܵļ���ģ��ļ��ϰ�. ���ڻ�����, ���õ������ذ�װ, Python3 �Ժ�, ��urllib , urllib2 �ϲ���һ��Ϊurllib��.
  1. urllib.request   �򿪲���ȡURLs

  2. urllib.error     urllib.request ���쳣

  3. urllib.parse     ����URLs

  4. urllib.robotparser     ���� robots.txt�ļ�

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