. pylab 是 matplotlib 和 IPython 提供的一个模块, 提供了类似 Matlab 的语法, 在启动 IPython 时 可以使用 --pylab 启动, 它相当于当入了如下库:

import numpy
import matplotlib
from matplotlib import pylab, mlab, pyplot
np = numpy
plt = pyplot
from IPython.display import display
from IPython.core.pylabtools import figsize, getfigs
from pylab import *
from numpy import *