. ��д���������ٲ���������ѧ��ʽ, Notebook ʹ��MathJax �������LaTeX �ı�ת��Ϊ��ѧ��ʽ.  ���� MathJax ��ϴ�, m���м̳е�IPython �У� ����ֱ�Ӵ�MathJax ��������, �����������û������, ���޷���ȷ��ʾ��ѧ��ʽ. Ϊ�˽���������, �����ڵ�Ԫ���������³���, ����������MathJax ������Ӳ��.

  from IPython.external.mathjax import install_mathjax, default_dest
  install_mathjax()

  MathJax ��ȫ��ѹ֮��, Լ��100MB �ռ�, ���д���Ϊ�ɰ������׼����PNG ����ͼ���ļ�.  ִ������������Կ���ɾ�����PNG����ͼƬ���ļ���

  from os import path
  import shutil

  png_path = path.join( default_dest, "fonts/HTML-CSS/TeX/png")
  shutil.rmtree( png_path )

  ���������������֮��, ������ģʽ�� ��m ������Ԫ��ʽ�л���Markdown. Ȼ����������LaTeX�ı�:

     $e^{i\pi} + 1 = 0$

  �� Shift+Enter ��ݼ�֮��, �����ݽ���ת����ѧ��ʽ��ʾ: e�� i�ƴη� +1 = 0 

   