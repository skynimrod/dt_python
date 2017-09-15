# coding=gbk

import pandas as pd

columsn = 'user_id', 'age', 'sex', 'occupation', 'zip_code'

df = pd.read_csv( "./data/u.user", delimiter=",", header=None, names = columns )

print df.head()

# �������ʾ������ͷ������

# ����ʹ��ְҵ�����û����ݽ��з���, ���������ƽ������, ����������֮�󽫽����ʾΪ��״ͼ. ���Կ�����˸��ӵ�������Pandas �п��� ʹ��һ�д������

df.groupby("occupation").age.mean().order().plot(kind="bar", figsize=(12,4) )