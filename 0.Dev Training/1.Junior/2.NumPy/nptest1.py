# coding = gbk

import numpy as np

x, y = np.ogrid[-2:2:20j, -2:2:20j]
z = x * np.exp( - x ** 2 - y ** 2)

