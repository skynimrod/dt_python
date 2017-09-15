# coding=gbk

import pandas as pd

columsn = 'user_id', 'age', 'sex', 'occupation', 'zip_code'

df = pd.read_csv( "./data/u.user", delimiter=",", header=None, names = columns )

print df.head()

# 这儿会显示出带栏头的数据

# 下面使用职业栏对用户数据进行分组, 计算魅族的平均年龄, 按年龄排序之后将结果显示为柱状图. 可以看到如此复杂的运算在Pandas 中可以 使用一行代码完成

df.groupby("occupation").age.mean().order().plot(kind="bar", figsize=(12,4) )