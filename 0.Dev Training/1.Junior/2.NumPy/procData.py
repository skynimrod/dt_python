import numpy
import Image
import matplotlib.pyplot as plt


bug = Image.open('stinkbug.png')
arr = numpy.array( bug.getdata(), numpy.uint8).reshape(bug.size[1], bug.size[0], -1 )

plt.gray()
plt.imshow( arr)
plt.colorbar()

plt.show()