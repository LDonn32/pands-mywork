# Messing with Histograms
# Author: Laura Donnelly

import numpy as np
import matplotlib.pyplot as plt
'''
# np.random.seed(1)
# This line of code generates the same random data each time when ran
# Handy for debuging

normData = np.random.normal(size=10)

plt.hist(normData)
plt.show()
'''

fruit = np.array(["Apples", "Orange", "Banana",])
numbers = np.array([23,77,500])

plt.pie(numbers,labels = fruit)
plt.legend()
plt.show()