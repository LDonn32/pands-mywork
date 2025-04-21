

import matplotlib.pyplot as plt
import numpy as np

minSalary = 20000
maxSalary = 80000
numberOfEnteries = 10

np.random.seed(1) 
salaries = np.random.randint(minSalary, maxSalary, numberOfEnteries)
ages = np.random.randint(low=21, high = 65, size = numberOfEnteries)

plt.scatter(ages, salaries)

#add xsquared
xpoints = np.array(range(1, 101))
ypoints = xpoints * xpoints # multiply entry by itself for the xsquared

plt.plot(xpoints, ypoints, color = 'r', label = "x squared")

plt.title("random plot")
plt.xlabel("Salaries")
plt.ylabel("ages")
plt.legend()


#plt.show()
plt.savefig('prettier-plot.png')